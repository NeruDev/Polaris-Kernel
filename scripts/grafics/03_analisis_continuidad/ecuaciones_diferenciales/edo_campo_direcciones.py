# yaml_frontmatter:
#   id: 'edo_campo_direcciones'
#   title: 'Campo de pendientes para una EDO de primer orden'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'analisis', 'edo']

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

    x, y = np.meshgrid(np.linspace(0, 4, 15), np.linspace(0, 4, 15))
    dy = y - x  # y' = y - x
    dx = np.ones(dy.shape)

    ax.quiver(x, y, dx, dy, color=colors["secondary"], alpha=0.5)
    ax.set_title("EDO: Campo de Direcciones")
    ax.axis("off")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "03_analisis_continuidad"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "edo_campo_direcciones.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'edo_campo_direcciones.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
