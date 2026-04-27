# yaml_frontmatter:
#   id: 'graficas_seno_coseno'
#   title: 'Comparativa de funciones trigonometrias seno y coseno'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'trigonometria', 'ondas']

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
    x = np.linspace(0, 2 * np.pi, 100)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, np.sin(x), label="Seno", color=colors["primary"], lw=2)
    ax.plot(x, np.cos(x), label="Coseno", color=colors["secondary"], lw=2)

    ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
    ax.set_xticklabels(["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_title("Funciones Trigonométricas")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "04_espacio_forma"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "graficas_seno_coseno.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'graficas_seno_coseno.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
