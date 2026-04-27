# yaml_frontmatter:
#   id: 'markov_estados'
#   title: 'Diagrama de transicion de estados de una cadena de Markov'
#   pilar: '06_estocastica_incertidumbre'
#   tags: ['grafico', 'procesos', 'markov']

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

    # Nodos de estados
    ax.scatter([0.2, 0.8], [0.5, 0.5], s=2000, color=colors["primary"], alpha=0.3)
    ax.text(0.2, 0.5, "A", fontsize=15, ha="center", va="center", fontweight="bold")
    ax.text(0.8, 0.5, "B", fontsize=15, ha="center", va="center", fontweight="bold")

    # Transiciones (Flechas)
    # A -> B
    ax.annotate(
        "",
        xy=(0.7, 0.55),
        xytext=(0.3, 0.55),
        arrowprops=dict(arrowstyle="->", lw=2, color=colors["secondary"]),
    )
    ax.text(0.5, 0.6, "0.4", color=colors["secondary"])

    # B -> A
    ax.annotate(
        "",
        xy=(0.3, 0.45),
        xytext=(0.7, 0.45),
        arrowprops=dict(arrowstyle="->", lw=2, color=colors["accent"]),
    )
    ax.text(0.5, 0.35, "0.3", color=colors["accent"])

    # Auto-bucles
    ax.add_patch(
        patches.Arc((0.15, 0.6), 0.2, 0.2, theta1=0, theta2=270, color=colors["primary"], lw=1.5)
    )
    ax.text(0.05, 0.7, "0.6")

    ax.set_title("Modelos Estocasticos: Cadena de Markov")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "06_estocastica_incertidumbre"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "markov_estados.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'markov_estados.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
