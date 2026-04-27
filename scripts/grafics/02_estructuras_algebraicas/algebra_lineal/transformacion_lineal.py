# yaml_frontmatter:
#   id: 'transformacion_lineal'
#   title: 'Deformacion del espacio por una transformacion lineal'
#   pilar: '02_estructuras_algebraicas'
#   tags: ['grafico', 'algebra', 'transformaciones']

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
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    # 1. Espacio Original (Cuadricula)
    x, y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
    axs[0].plot(x, y, color=colors["text"], alpha=0.3, lw=0.5)
    axs[0].plot(x.T, y.T, color=colors["text"], alpha=0.3, lw=0.5)
    axs[0].set_title("Espacio Original $V$")

    # 2. Espacio Transformado (Shear)
    t_mat = np.array([[1, 1], [0, 1]])  # Matriz de corte
    tx = t_mat[0, 0] * x + t_mat[0, 1] * y
    ty = t_mat[1, 0] * x + t_mat[1, 1] * y
    axs[1].plot(tx, ty, color=colors["primary"], alpha=0.6, lw=1)
    axs[1].plot(tx.T, ty.T, color=colors["primary"], alpha=0.6, lw=1)
    axs[1].set_title("Transformado $T(V)$")

    for ax in axs:
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_aspect("equal")
        ax.axhline(0, color="black", lw=1)
        ax.axvline(0, color="black", lw=1)

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "02_estructuras_algebraicas"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "transformacion_lineal.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'transformacion_lineal.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
