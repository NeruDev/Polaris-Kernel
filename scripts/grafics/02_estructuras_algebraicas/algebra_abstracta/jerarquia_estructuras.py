# yaml_frontmatter:
#   id: 'jerarquia_estructuras'
#   title: 'Jerarquia de Monoides, Grupos, Anillos y Campos'
#   pilar: '02_estructuras_algebraicas'
#   tags: ['grafico', 'algebra', 'estructuras']

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
    fig, ax = plt.subplots(figsize=(8, 6))

    # Conjuntos anidados (Jerarquia)
    ax.add_patch(
        patches.Ellipse((0.5, 0.5), 0.9, 0.8, color=colors["primary"], alpha=0.1, label="Monoide")
    )
    ax.add_patch(
        patches.Ellipse((0.5, 0.45), 0.7, 0.6, color=colors["secondary"], alpha=0.2, label="Grupo")
    )
    ax.add_patch(
        patches.Ellipse((0.5, 0.4), 0.5, 0.4, color=colors["accent"], alpha=0.3, label="Anillo")
    )
    ax.add_patch(
        patches.Ellipse((0.5, 0.35), 0.3, 0.2, color=colors["danger"], alpha=0.4, label="Campo")
    )

    ax.text(0.5, 0.85, "Estructuras Algebraicas", ha="center", fontweight="bold")
    ax.legend(loc="upper right")

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
        fig.savefig(out_dir / "jerarquia_estructuras.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'jerarquia_estructuras.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
