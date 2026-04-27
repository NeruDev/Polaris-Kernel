# yaml_frontmatter:
#   id: 'geometria_diferencial_frenet'
#   title: 'Triedro de Frenet en una helice 3D'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria', 'curvas']

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

    # Helice
    t = np.linspace(0, 4 * np.pi, 200)
    x, y, z = np.cos(t), np.sin(t), 0.2 * t
    ax.plot(x, y, z, color=colors["primary"], lw=2, label=r"Curva $\gamma(t)$")

    # Triedro en un punto (t = pi)
    tp = np.pi
    px, py, pz = np.cos(tp), np.sin(tp), 0.2 * tp

    ax.quiver(
        px,
        py,
        pz,
        -np.sin(tp),
        np.cos(tp),
        0.2,
        color=colors["danger"],
        length=0.8,
        label="Tangente T",
    )
    ax.quiver(
        px, py, pz, -np.cos(tp), -np.sin(tp), 0, color=colors["secondary"], length=0.8, label="Normal N"
    )
    ax.quiver(px, py, pz, 0, 0, 1, color=colors["purple"], length=0.8, label="Binormal B")

    ax.set_title("Geometria Diferencial: Triedro de Frenet-Serret")
    ax.axis("off")
    ax.legend()

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "04_espacio_forma"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "geometria_diferencial_frenet.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'geometria_diferencial_frenet.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
