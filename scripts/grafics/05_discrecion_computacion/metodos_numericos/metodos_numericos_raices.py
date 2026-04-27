# yaml_frontmatter:
#   id: 'metodos_numericos_raices'
#   title: 'Visualizacion del metodo de biseccion'
#   pilar: '05_discrecion_computacion'
#   tags: ['grafico', 'numerico', 'raices']

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
    x = np.linspace(0.5, 4.5, 100)

    def f(x):
        return np.log(x) - 1  # Raiz en x=e

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, f(x), color=colors["primary"], lw=2)
    ax.axhline(0, color="black", lw=1)

    # Intervalo de biseccion
    a_val, b_val = 1, 4
    ax.axvline(a_val, color=colors["danger"], ls="--", label="a")
    ax.axvline(b_val, color=colors["secondary"], ls="--", label="b")

    ax.set_title("Metodos Numericos: Localizacion de Raices")
    ax.legend()

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "05_discrecion_computacion"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "metodos_numericos_raices.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'metodos_numericos_raices.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
