# yaml_frontmatter:
#   id: 'topologia_homeomorfismo'
#   title: 'Equivalencia entre una dona y una taza'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'topologia', 'homeomorfismo']

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
    fig, ax = plt.subplots(figsize=(8, 4))

    # Dona (Toro)
    ax.add_patch(plt.Circle((0.3, 0.5), 0.15, color=colors["primary"], alpha=0.6))
    ax.add_patch(plt.Circle((0.3, 0.5), 0.05, color="white"))

    ax.text(0.5, 0.5, r"$\cong$", fontsize=30, ha="center", va="center")

    # Taza (Esquematica)
    ax.add_patch(plt.Rectangle((0.65, 0.4), 0.2, 0.2, color=colors["primary"], alpha=0.6))
    ax.add_patch(plt.Circle((0.85, 0.5), 0.05, fill=False, color=colors["primary"], lw=4))

    ax.set_title("Topologia: Homeomorfismo (Equivalencia Continua)")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "04_espacio_forma"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "topologia_homeomorfismo.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'topologia_homeomorfismo.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
