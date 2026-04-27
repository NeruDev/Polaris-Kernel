# yaml_frontmatter:
#   id: 'topologia_vecindarios'
#   title: 'Puntos interiores y vecindarios en un conjunto'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'topologia', 'metricas']

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

    # Un conjunto "amorfo"
    pts = np.array([[0.2, 0.2], [0.8, 0.3], [0.9, 0.8], [0.4, 0.9], [0.1, 0.6]])
    poly = plt.Polygon(
        pts, fill=True, color=colors["secondary"], alpha=0.2, ls="--", lw=2, label="Conjunto Abierto U"
    )
    ax.add_patch(poly)

    # Vecindario de un punto
    p_val = [0.5, 0.5]
    circle = plt.Circle(
        p_val, 0.1, color=colors["danger"], fill=False, lw=1, label="Vecindario B(x,r)"
    )
    ax.add_patch(circle)
    ax.scatter(p_val[0], p_val[1], color=colors["danger"], s=20)
    ax.text(p_val[0] + 0.02, p_val[1] + 0.02, "x")

    ax.set_title("Espacios Metricis: Vecindarios y Apertura")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.legend(loc="lower right")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "04_espacio_forma"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "topologia_vecindarios.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'topologia_vecindarios.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
