# yaml_frontmatter:
#   id: 'build'
#   title: 'Orquestador unificado de construccion y validacion'
#   tags: ['build', 'pipeline', 'automation']

"""
Orquestador Principal de Construcción.
Bajo el nuevo paradigma, este script delega el renderizado final de HTML/PDF
a Quarto (y por ende a Typst) usando el comando `quarto render`.
El flujo de CI/CD en GitHub Actions (`pages.yml`) utiliza este script
antes de empaquetar la carpeta `site/` con `upload-pages-artifact`.
"""

# ruff: noqa: I001

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
# Las funciones de conversion HTML y calculo de profundidad ya no son necesarias gracias a Quarto

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="MathKernel Build System")
    parser.add_argument("--verbose", action="store_true", help="Logs detallados")
    parser.add_argument("--generate-assets", action="store_true", help="Ejecutar scripts manuales para generar imágenes SVG (Restringido por defecto para Quarto/Typst)")
    parser.add_argument("--strict", action="store_true", help="Falla en cualquier advertencia")
    return parser.parse_args()

def validate_project(config: BuildConfig, file_manager: FileManager, collector: ErrorCollector):
    log_info("Validando integridad del proyecto...")
    schema_path = config.paths.schemas_dir / "content.schema.json"
    if not schema_path.exists():
        collector.add_message("validation", "No se encontró el esquema JSON de contenido", critical=True)
        return
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    targets = [config.paths.src_dir, config.paths.scripts_dir, config.paths.project_root / "utils"]
    encoding_errors = encoding_validator.validate_paths(targets)
    for err in encoding_errors:
        collector.add_message("encoding", err, critical=True)
    for md_path in [p for ext in ("*.md", "*.qmd") for p in config.paths.src_dir.rglob(ext)]:
        try:
            metadata, content = file_manager.read_markdown_with_frontmatter(md_path)
            try:
                jsonschema.validate(instance=metadata, schema=schema)
            except jsonschema.exceptions.ValidationError as e:
                collector.add_message("schema", f"Error en {md_path.name}: {e.message}", critical=True)
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
    log_info("Orquestando renderizado con Quarto en /site...")
    # Ejecutamos Quarto, que ahora maneja la generacion de HTML, PDF y copia de SVG
    try:
        # Nota: En Windows a veces se necesita shell=True para comandos globales.
        # Pasamos el comando como string cuando shell=True para evitar bugs en POSIX.
        result = subprocess.run("quarto render", capture_output=True, text=True, cwd=str(PROJECT_ROOT), shell=True)
        if result.returncode != 0:
            collector.add_message("rendering", f"Error en Quarto:\n{result.stderr}", critical=True)
        else:
            if config.verbose:
                print(result.stdout)
            log_info("Sitio Quarto generado correctamente.")
    except FileNotFoundError:
        collector.add_message("rendering", "Quarto CLI no está instalado o no se encuentra en el PATH.", critical=True)
    except Exception as e:
        collector.add_message("rendering", f"Fallo al invocar Quarto: {e}", critical=True)

def run_build():
    args = parse_args()
    paths = Paths.from_project_root(PROJECT_ROOT)
    config = BuildConfig(paths=paths, verbose=args.verbose)
    collector = ErrorCollector()
    file_manager = FileManager()
    meta_agent = MetadataAgent(PROJECT_ROOT)
    log_info("Sincronizando metadatos...")
    meta_agent.synchronize()
    validate_project(config, file_manager, collector)
    if args.generate_assets:
        run_assets(config, collector)
    if collector.has_critical_errors:
        log_error("Build abortado debido a errores criticos:")
        for line in collector.format_summary(): print(line)
        sys.exit(1)
    run_site(config, file_manager, collector)
    if collector.has_critical_errors:
        log_error("\nBuild finalizado con errores críticos en el renderizado:")
        for line in collector.format_summary(): print(line)
        sys.exit(1)
    elif collector.has_errors:
        log_warn("\nBuild finalizado con advertencias:")
        for line in collector.format_summary(): print(line)
    else:
        log_info("Build completado exitosamente.")

if __name__ == "__main__":
    run_build()
