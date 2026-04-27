# yaml_frontmatter:
#   id: 'distribucion_normal'
#   title: 'Visualizacion de la campana de Gauss'
#   pilar: '06_estocastica_incertidumbre'
#   tags: ['grafico', 'probabilidad', 'distribucion']

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
    mu, sigma = 0, 1
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 100)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, y, color=colors["primary"], lw=2, label="Distribucion Normal")
    ax.fill_between(x, y, color=colors["primary"], alpha=0.1)

    # Marcadores de desviacion
    ax.axvline(mu, color=colors["danger"], ls="--", alpha=0.5, label="Media")

    ax.set_title("Teoria de Probabilidad: Distribucion Gaussiana")
    ax.legend()

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "06_estocastica_incertidumbre"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "distribucion_normal.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'distribucion_normal.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
