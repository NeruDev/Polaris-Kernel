# yaml_frontmatter:
#   id: 'pitagoras_visual'
#   title: 'Representacion visual del teorema de Pitagoras con cuadrados'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria', 'teorema']

import sys
from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt

# Configurar path para imports del proyecto
PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.templates import get_colors, setup_style


def generate():
    setup_style()
    colors = get_colors()
    fig, ax = plt.subplots(figsize=(6, 6))

    # Triangulo
    triangle = patches.Polygon([[0, 0], [4, 0], [0, 3]], closed=True, color=colors["primary"], alpha=0.3)
    ax.add_patch(triangle)

    # Cuadrados sobre los catetos y la hipotenusa
    ax.add_patch(patches.Rectangle((0, 0), 4, -4, color=colors["secondary"], alpha=0.4, label="$a^2$"))
    ax.add_patch(patches.Rectangle((0, 0), -3, 3, color=colors["accent"], alpha=0.4, label="$b^2$"))

    ax.set_xlim(-4, 6)
    ax.set_ylim(-5, 5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Teorema de Pitágoras")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "04_espacio_forma"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "pitagoras_visual.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'pitagoras_visual.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
