# yaml_frontmatter:
#   id: 'geometria_variedad_tangente'
#   title: 'Plano tangente a una superficie curva'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria', 'variedades']

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
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")

    # Superficie (Silla de montar)
    x = np.linspace(-1, 1, 30)
    y = np.linspace(-1, 1, 30)
    xx, yy = np.meshgrid(x, y)
    zz = xx**2 - yy**2
    ax.plot_surface(xx, yy, zz, color=colors["primary"], alpha=0.3, edgecolor="none")

    # Plano tangente en (0.5, 0.5)
    x0, y0 = 0.5, 0.5
    z0 = x0**2 - y0**2
    px, py = np.meshgrid(np.linspace(0.2, 0.8, 10), np.linspace(0.2, 0.8, 10))
    pz = z0 + 2 * x0 * (px - x0) - 2 * y0 * (py - y0)
    ax.plot_surface(px, py, pz, color=colors["accent"], alpha=0.7)

    ax.set_title(r"Variedades: Espacio Tangente $T_pM$")
    ax.axis("off")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "04_espacio_forma"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "geometria_variedad_tangente.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'geometria_variedad_tangente.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
