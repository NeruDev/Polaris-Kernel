# yaml_frontmatter:
#   id: 'combinatoria_arbol'
#   title: 'Diagrama de arbol para principios de conteo'
#   pilar: '05_discrecion_computacion'
#   tags: ['grafico', 'computacion', 'combinatoria']

import sys
from pathlib import Path

import matplotlib.pyplot as plt

# Configurar path para imports del proyecto
PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.templates import get_colors, setup_style


def generate():
    setup_style()
    colors = get_colors()
    fig, ax = plt.subplots(figsize=(8, 5))

    # Simular diagrama de árbol
    ax.plot([0, 1, 2], [0, 1, 1.5], marker="o", color=colors["primary"], label="Opcion A")
    ax.plot([0, 1, 2], [0, 1, 0.5], marker="o", color=colors["primary"])
    ax.plot(
        [0, 1, 2], [0, -1, -0.5], marker="o", color=colors["secondary"], label="Opcion B"
    )
    ax.plot([0, 1, 2], [0, -1, -1.5], marker="o", color=colors["secondary"])

    ax.set_title("Combinatoria: Diagrama de Arbol de Decisiones")
    ax.axis("off")
    ax.legend()

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "05_discrecion_computacion"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "combinatoria_arbol.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'combinatoria_arbol.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
