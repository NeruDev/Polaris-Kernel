# yaml_frontmatter:
#   id: 'conicas_analitica'
#   title: 'Representacion de elipse y parabola'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria', 'analitica']

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Configurar path para imports del proyecto
PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.templates import get_colors, setup_style


def generate():
    setup_style()
    colors = get_colors()
    fig, ax = plt.subplots(figsize=(6, 6))

    t = np.linspace(0, 2 * np.pi, 100)
    # Elipse
    ax.plot(1.5 * np.cos(t), 1.0 * np.sin(t), color=colors["primary"], lw=2, label="Elipse")

    # Parabola
    x = np.linspace(-1.5, 1.5, 100)
    ax.plot(x, x**2 - 1, color=colors["secondary"], lw=2, label="Parabola")

    ax.set_title("Geometria Analitica: Conicas")
    ax.legend()
    ax.axis("off")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "04_espacio_forma"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "conicas_analitica.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'conicas_analitica.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
