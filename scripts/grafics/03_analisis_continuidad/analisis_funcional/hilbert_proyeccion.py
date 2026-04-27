# yaml_frontmatter:
#   id: 'hilbert_proyeccion'
#   title: 'Teorema de la proyeccion ortogonal en espacios funcionales'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'analisis', 'hilbert']

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
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, projection="3d")

    # Subespacio M (Plano)
    x = np.linspace(-1, 1, 10)
    y = np.linspace(-1, 1, 10)
    xx, yy = np.meshgrid(x, y)
    zz = 0 * xx
    ax.plot_surface(xx, yy, zz, alpha=0.2, color=colors["secondary"])

    # Vector v fuera del subespacio
    v = np.array([0.5, 0.5, 1.0])
    p = np.array([0.5, 0.5, 0.0])  # Proyeccion

    ax.quiver(0, 0, 0, v[0], v[1], v[2], color=colors["primary"], lw=3, label="Vector v")
    ax.quiver(0, 0, 0, p[0], p[1], p[2], color=colors["accent"], lw=3, label="Proyección P(v)")

    # Linea de error (Ortogonal)
    ax.plot(
        [v[0], p[0]], [v[1], p[1]], [v[2], p[2]], color=colors["danger"], ls="--", label="Error v - P(v)"
    )

    ax.set_title("Espacios de Hilbert: Proyeccion Ortogonal")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(0, 1.2)
    ax.axis("off")
    ax.legend()

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "03_analisis_continuidad"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "hilbert_proyeccion.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'hilbert_proyeccion.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
