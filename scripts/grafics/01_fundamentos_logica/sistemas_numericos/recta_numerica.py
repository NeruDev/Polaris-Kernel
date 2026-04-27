# yaml_frontmatter:
#   id: 'recta_numerica'
#   title: 'Representacion de la recta real y conjuntos'
#   pilar: '01_fundamentos_logica'
#   tags: ['grafico', 'fundamentos', 'numeros']

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
    fig, ax = plt.subplots(figsize=(10, 2))

    # Recta
    ax.axhline(0, color=colors["text"], lw=2)
    points = [-2, -1, 0, 1, 2]
    for p in points:
        ax.plot([p, p], [-0.1, 0.1], color=colors["text"])
        ax.text(p, -0.4, str(p), ha="center")

    # Conjuntos
    ax.text(0.5, 0.5, r"$\mathbb{N}$", color=colors["primary"], fontweight="bold")
    ax.text(-1.5, 0.5, r"$\mathbb{Z}$", color=colors["secondary"], fontweight="bold")
    ax.text(1.7, 0.5, r"$\mathbb{R}$", color=colors["danger"], fontweight="bold")

    ax.set_ylim(-1, 1)
    ax.set_xlim(-3, 3)
    ax.axis("off")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "01_fundamentos_logica"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "recta_numerica.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'recta_numerica.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
