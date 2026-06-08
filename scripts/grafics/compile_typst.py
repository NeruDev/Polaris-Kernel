import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
GRAFICS_DIR = PROJECT_ROOT / "scripts" / "grafics"
TYPST_SRC_DIR = GRAFICS_DIR / "typst_src"
SRC_DIR = PROJECT_ROOT / "src"
ASSETS_REGISTRY = PROJECT_ROOT / "metadata" / "GENERATED_ASSETS.md"

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
        if len(parts) != 2:
            continue
        folder_name, svg_stem = parts
        svg_name = f"{svg_stem}.svg"
        svg_path = SRC_DIR / folder_name / svg_name
        
        # Ejecutar typst compile
        result = subprocess.run(["typst", "compile", str(typ_file), str(svg_path)], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[OK] Generado: {svg_path.relative_to(PROJECT_ROOT)}")
            
            # Registrar en GENERATED_ASSETS.md
            entry = f"| `scripts/grafics/typst_src/{typ_file.name}` | `src/{folder_name}/{svg_name}` | {folder_name} |"
            if entry not in registry_entries:
                with open(ASSETS_REGISTRY, "a", encoding="utf-8") as f:
                    f.write(f"{entry}\n")
                registry_entries.add(entry)
        else:
            print(f"[ERROR] Error al compilar {typ_file.name}: {result.stderr}")

if __name__ == "__main__":
    compile_all()
