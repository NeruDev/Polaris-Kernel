# yaml_frontmatter:
#   id: 'diagrama_conmutativo'
#   title: 'Morfismos f, g y su composicion en una categoria'
#   pilar: '02_estructuras_algebraicas'
#   tags: ['grafico', 'categorias', 'morfismos']

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
    fig, ax = plt.subplots(figsize=(6, 6))

    # Objetos
    objs = {"A": (0.2, 0.8), "B": (0.8, 0.8), "C": (0.8, 0.2)}
    for name, pos in objs.items():
        ax.text(pos[0], pos[1], name, fontsize=20, ha="center", va="center", fontweight="bold")

    # Morfismos (Flechas)
    # f: A -> B
    ax.annotate(
        "",
        xy=(0.7, 0.8),
        xytext=(0.3, 0.8),
        arrowprops=dict(arrowstyle="->", lw=2, color=colors["primary"]),
    )
    ax.text(0.5, 0.85, "f", color=colors["primary"], fontsize=15)

    # g: B -> C
    ax.annotate(
        "",
        xy=(0.8, 0.3),
        xytext=(0.8, 0.7),
        arrowprops=dict(arrowstyle="->", lw=2, color=colors["secondary"]),
    )
    ax.text(0.85, 0.5, "g", color=colors["secondary"], fontsize=15)

    # h = g o f: A -> C
    ax.annotate(
        "",
        xy=(0.75, 0.25),
        xytext=(0.25, 0.75),
        arrowprops=dict(arrowstyle="->", lw=2, color=colors["danger"], ls="--"),
    )
    ax.text(0.4, 0.4, r"$g \circ f$", color=colors["danger"], fontsize=15)

    ax.set_title("Categorias: Diagrama Conmutativo")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "02_estructuras_algebraicas"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "diagrama_conmutativo.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'diagrama_conmutativo.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
