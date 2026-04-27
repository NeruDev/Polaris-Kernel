# yaml_frontmatter:
#   id: 'primos_criba'
#   title: 'Representacion esquematica de numeros primos'
#   pilar: '05_discrecion_computacion'
#   tags: ['grafico', 'numeros', 'primos']

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
    fig, ax = plt.subplots(figsize=(8, 4))

    for i in range(1, 11):
        color = colors["primary"] if i in [2, 3, 5, 7] else colors["text"]
        ax.add_patch(patches.Rectangle((i, 0), 0.8, 0.8, color=color, alpha=0.3))
        ax.text(i + 0.4, 0.4, str(i), ha="center", va="center", fontweight="bold")

    ax.set_title("Teoria de Numeros: Numeros Primos")
    ax.set_xlim(0.5, 11)
    ax.set_ylim(-0.5, 1.5)
    ax.axis("off")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "05_discrecion_computacion"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "primos_criba.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'primos_criba.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
