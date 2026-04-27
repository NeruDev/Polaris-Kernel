# yaml_frontmatter:
#   id: 'histograma_ejemplo'
#   title: 'Ejemplo de histograma para datos estadisticos'
#   pilar: '06_estocastica_incertidumbre'
#   tags: ['grafico', 'estadistica', 'datos']

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
    np.random.seed(42)
    data = np.random.normal(10, 2, 500)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(data, bins=20, color=colors["secondary"], alpha=0.6, edgecolor=colors["text"])

    ax.set_title("Estadistica Descriptiva: Histograma de Frecuencias")
    ax.set_xlabel("Valor")
    ax.set_ylabel("Frecuencia")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "06_estocastica_incertidumbre"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "histograma_ejemplo.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'histograma_ejemplo.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
