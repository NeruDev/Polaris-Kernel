# yaml_frontmatter:
#   id: 'build'
#   title: 'Orquestador unificado de construccion y validacion'
#   tags: ['build', 'pipeline', 'automation']

import argparse
import json
import subprocess
import sys
from pathlib import Path

import jsonschema

# Configuracion de entorno para imports locales
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.config import BuildConfig, Paths
from scripts.core import encoding_validator, formula_validator
from scripts.core.error_handling import ErrorCollector
from scripts.io.file_manager import FileManager
from scripts.io.metadata_agent import MetadataAgent
from utils.logging import log_error, log_info, log_warn
from utils.markdown import convert_md_to_html
from utils.pathing import compute_depth


def parse_args() -> argparse.Namespace:
    # ... (parse_args se mantiene igual)
    parser = argparse.ArgumentParser(description="MathKernel Build System")
    parser.add_argument("--verbose", action="store_true", help="Logs detallados")
    parser.add_argument("--skip-assets", action="store_true", help="No generar imagenes")
    parser.add_argument("--strict", action="store_true", help="Falla en cualquier advertencia")
    return parser.parse_args()


def validate_project(config: BuildConfig, file_manager: FileManager, collector: ErrorCollector):
    """Ejecuta la suite de validacion: UTF-8, Estructura y Metadatos por Schema."""
    log_info("Validando integridad del proyecto...")

    schema_path = config.paths.schemas_dir / "content.schema.json"
    if not schema_path.exists():
        collector.add_message(
            "validation", "No se encontró el esquema JSON de contenido", critical=True
        )
        return

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    targets = [config.paths.src_dir, config.paths.scripts_dir, config.paths.project_root / "utils"]
    encoding_errors = encoding_validator.validate_paths(targets)
    for err in encoding_errors:
        collector.add_message("encoding", err, critical=True)

    for md_path in config.paths.src_dir.rglob("*.md"):
        try:
            metadata, content = file_manager.read_markdown_with_frontmatter(md_path)
            try:
                jsonschema.validate(instance=metadata, schema=schema)
            except jsonschema.exceptions.ValidationError as e:
                collector.add_message(
                    "schema", f"Error en {md_path.name}: {e.message}", critical=True
                )

            warnings = formula_validator.validate_markdown_math_tables(content, md_path.name)
            for warn in warnings:
                collector.add_message("math_syntax", warn, critical=config.strict)
        except Exception as e:
            collector.add_message("parser", f"Error procesando {md_path.name}: {e}", critical=True)


def run_assets(config: BuildConfig, collector: ErrorCollector):
    script_path = config.paths.scripts_dir / "generate_assets.py"
    log_info("Generando activos graficos...")
    result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
    if result.returncode != 0:
        collector.add_message("assets", f"Error en generacion: {result.stderr}", critical=True)
    elif config.verbose:
        print(result.stdout)


def run_site(config: BuildConfig, file_manager: FileManager, collector: ErrorCollector):
    paths = config.paths
    log_info("Generando sitio estatico en /site...")
    file_manager.remove_dir(paths.site_dir)
    file_manager.ensure_dir(paths.site_dir)
    if paths.site_src_dir.exists():
        file_manager.copy_dir(paths.site_src_dir, paths.site_dir)
    template = file_manager.read_text(paths.template_path)

    for pilar_dir in paths.src_dir.iterdir():
        if not pilar_dir.is_dir():
            continue
        for item in pilar_dir.iterdir():
            rel_path = item.relative_to(paths.src_dir)
            dest_path = paths.site_dir / rel_path
            if item.suffix == ".svg":
                import shutil

                file_manager.ensure_dir(dest_path.parent)
                shutil.copy2(item, dest_path)
            elif item.suffix == ".md":
                try:
                    metadata, content = file_manager.read_markdown_with_frontmatter(item)
                    html_body, _ = convert_md_to_html(content)
                    page_title = metadata.get("title", item.stem)
                    full_html = template.replace("{{TITLE}}", page_title)
                    full_html = full_html.replace("{{BODY}}", html_body)

                    depth = compute_depth(str(rel_path))
                    prefix = "../" * depth
                    full_html = full_html.replace("{{PREFIX}}", prefix)

                    file_manager.write_text(dest_path.with_suffix(".html"), full_html)
                except Exception as e:
                    collector.add_message("rendering", f"Error en {item.name}: {e}")


def run_build():
    args = parse_args()
    paths = Paths.from_project_root(PROJECT_ROOT)
    config = BuildConfig(paths=paths, verbose=args.verbose)
    collector = ErrorCollector()
    file_manager = FileManager()
    meta_agent = MetadataAgent(PROJECT_ROOT)

    # Pipeline
    log_info("Sincronizando metadatos adyacentes...")
    meta_agent.synchronize()

    validate_project(config, file_manager, collector)
    if not args.skip_assets:
        run_assets(config, collector)

    if collector.has_critical_errors:
        log_error("Build abortado debido a errores criticos:")
        for line in collector.format_summary():
            print(line)
        sys.exit(1)

    run_site(config, file_manager, collector)

    if collector.has_errors:
        log_warn("\nBuild finalizado con advertencias:")
        for line in collector.format_summary():
            print(line)
    else:
        log_info("Build completado exitosamente.")


if __name__ == "__main__":
    run_build()
