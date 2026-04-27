# yaml_frontmatter:
#   id: 'triangulos_lados'
#   title: 'Clasificacion de triangulos por sus lados'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria', 'triangulos']

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
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    eq_pts = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])
    axs[0].add_patch(plt.Polygon(eq_pts, fill=True, color=colors["primary"], alpha=0.3))
    axs[0].plot(
        np.append(eq_pts[:, 0], eq_pts[0, 0]),
        np.append(eq_pts[:, 1], eq_pts[0, 1]),
        color=colors["primary"],
        lw=2,
    )
    axs[0].set_title("Equilátero (3 iguales)")
    iso_pts = np.array([[0, 0], [0.6, 0], [0.3, 1]])
    axs[1].add_patch(plt.Polygon(iso_pts, fill=True, color=colors["secondary"], alpha=0.3))
    axs[1].plot(
        np.append(iso_pts[:, 0], iso_pts[0, 0]),
        np.append(iso_pts[:, 1], iso_pts[0, 1]),
        color=colors["secondary"],
        lw=2,
    )
    axs[1].set_title("Isósceles (2 iguales)")
    esc_pts = np.array([[0, 0], [1, 0], [0.2, 0.6]])
    axs[2].add_patch(plt.Polygon(esc_pts, fill=True, color=colors["accent"], alpha=0.3))
    axs[2].plot(
        np.append(esc_pts[:, 0], esc_pts[0, 0]),
        np.append(esc_pts[:, 1], esc_pts[0, 1]),
        color=colors["accent"],
        lw=2,
    )
    axs[2].set_title("Escaleno (0 iguales)")
    for ax in axs:
        ax.set_aspect("equal")
        ax.axis("off")
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "04_espacio_forma"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "triangulos_lados.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'triangulos_lados.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
