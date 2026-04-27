# yaml_frontmatter:
#   id: 'campo_vectorial'
#   title: 'Visualizacion de un campo vectorial rotacional'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'analisis', 'vectores', 'gradiente']

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

    x, y = np.meshgrid(np.linspace(-2, 2, 10), np.linspace(-2, 2, 10))
    u, v = -y, x  # Campo rotacional

    ax.quiver(x, y, u, v, color=colors["primary"], alpha=0.6)
    ax.set_title("Calculo Multivariable: Campo Vectorial")
    ax.axis("off")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "03_analisis_continuidad"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "campo_vectorial.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'campo_vectorial.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
