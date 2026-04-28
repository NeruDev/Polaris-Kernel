# yaml_frontmatter:
#   id: 'venn_triple'
#   title: 'Diagrama de Venn de tres conjuntos'
#   pilar: '01_fundamentos_logica'
#   tags: ['grafico', 'conjuntos', 'venn']

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

    # Definir circulos
    ax.add_patch(patches.Circle((0, 0.2), 0.5, color=colors["primary"], alpha=0.2, label="A"))
    ax.add_patch(patches.Circle((0.3, -0.2), 0.5, color=colors["secondary"], alpha=0.2, label="B"))
    ax.add_patch(patches.Circle((-0.3, -0.2), 0.5, color=colors["accent"], alpha=0.2, label="C"))

    ax.text(0, 0.4, "A", fontsize=14, fontweight="bold")
    ax.text(0.5, -0.4, "B", fontsize=14, fontweight="bold")
    ax.text(-0.5, -0.4, "C", fontsize=14, fontweight="bold")

    ax.set_title("Teoria de Conjuntos: Relaciones Multiples")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect("equal")
    ax.axis("off")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "01_fundamentos_logica"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "diagrama_venn_triple.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'diagrama_venn_triple.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
