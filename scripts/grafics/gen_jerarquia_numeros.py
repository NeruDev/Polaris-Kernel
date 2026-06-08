import subprocess
import sys
from pathlib import Path


def main():
    project_root = Path(__file__).resolve().parents[2]
    typ_file = project_root / "scripts" / "grafics" / "typst_src" / "jerarquia_numeros.typ"
    svg_file = project_root / "src" / "01_fundamentos_logica" / "assets" / "jerarquia_numeros.svg"
    
    # Asegurar que el directorio de destino exista
    svg_file.parent.mkdir(parents=True, exist_ok=True)

    result = subprocess.run(
        ["typst", "compile", str(typ_file), str(svg_file)],
        capture_output=True,
        text=True,
        shell=True # For Windows
    )
    
    if result.returncode != 0:
        print(f"Error compilando typst: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Generado exitosamente: {svg_file}")

if __name__ == "__main__":
    main()
