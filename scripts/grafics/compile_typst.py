# yaml_frontmatter:
#   id: 'compile_typst'
#   title: 'Compilador de graficos Typst a SVG'
#   tags: ['scripts', 'graphics', 'typst']

import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
GRAFICS_DIR = PROJECT_ROOT / "scripts" / "grafics"
TYPST_SRC_DIR = GRAFICS_DIR / "typst_src"
SRC_DIR = PROJECT_ROOT / "src"
ASSETS_REGISTRY = PROJECT_ROOT / "metadata" / "GENERATED_ASSETS.md"

# Regla Arquitectónica: Las imágenes generadas (.svg) deben tener un nombre único
# y descriptivo sin números al inicio (ej. no heredar "01_" del archivo .qmd)
# para que se identifiquen fácilmente dentro de su carpeta de dificultad
# y no se confundan con los metadatos o los archivos fuente.
# El nombre del archivo Typst debe reflejar este nombre: pilar___nivel___nombre_sin_numeros.typ


def compile_all():
    print("Compilando archivos Typst...")
    if not ASSETS_REGISTRY.parent.exists():
        ASSETS_REGISTRY.parent.mkdir(parents=True, exist_ok=True)

    if not ASSETS_REGISTRY.exists():
        with open(ASSETS_REGISTRY, "w", encoding="utf-8") as f:
            f.write("# Registro de Activos Generados (GENERATED_ASSETS)\n\n")
            f.write("| Generador | Activo SVG | Pilar |\n")
            f.write("|-----------|------------|-------|\n")

    registry_entries = set()
    if ASSETS_REGISTRY.exists():
        with open(ASSETS_REGISTRY, "r", encoding="utf-8") as f:
            registry_entries = set(f.read().splitlines())

    for typ_file in TYPST_SRC_DIR.glob("*.typ"):
        parts = typ_file.stem.split("___")
        if len(parts) == 3:
            folder_name, subfolder, svg_stem = parts
            svg_name = f"{svg_stem}.svg"
            svg_path = SRC_DIR / folder_name / subfolder / svg_name
        elif len(parts) == 2:
            folder_name, svg_stem = parts
            svg_name = f"{svg_stem}.svg"
            svg_path = SRC_DIR / folder_name / svg_name
        else:
            continue

        try:
            svg_path.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(["typst", "compile", str(typ_file), str(svg_path)], check=True)
            print(f"[OK] Generado: {svg_path.relative_to(PROJECT_ROOT)}")
            
            registry_line = f"- `{svg_path.relative_to(PROJECT_ROOT).as_posix()}` (Generado desde `{typ_file.name}`)"
            if registry_line not in registry_entries:
                with open(ASSETS_REGISTRY, "a", encoding="utf-8") as f:
                    f.write(registry_line + "\n")
                registry_entries.add(registry_line)
        except Exception as e:
            print(f"[ERROR] Error al compilar {typ_file.name}: {e}\n")


if __name__ == "__main__":
    compile_all()
