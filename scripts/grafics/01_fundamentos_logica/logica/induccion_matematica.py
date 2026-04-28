# yaml_frontmatter:
#   id: 'induccion_matematica'
#   title: 'Metafora del domino para el principio de induccion'
#   pilar: '01_fundamentos_logica'
#   tags: ['grafico', 'logica', 'demostracion']

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
    fig, ax = plt.subplots(figsize=(10, 4))

    # Piezas de domino
    for i in range(5):
        # Angulo de inclinacion simulado
        angle = 15 if i < 3 else 0
        rect = patches.Rectangle((i * 1.5, 0), 0.3, 2, angle=angle, color=colors["secondary"], alpha=0.6)
        ax.add_patch(rect)
        ax.text(i * 1.5 + 0.1, -0.3, f"n={i+1}", ha="center")

    # Anotaciones
    ax.annotate("Base: n=1", xy=(0.1, 1), xytext=(-1, 2.5), arrowprops=dict(arrowstyle="->", color=colors["text"]))
    ax.annotate("Paso Inductivo: n -> n+1", xy=(3.1, 1), xytext=(2, 2.5), arrowprops=dict(arrowstyle="->", color=colors["danger"]))

    ax.set_title("Metodos de Demostracion: Induccion Matematica")
    ax.set_xlim(-1.5, 8)
    ax.set_ylim(-1, 3)
    ax.axis("off")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "01_fundamentos_logica"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "induccion_matematica.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'induccion_matematica.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
