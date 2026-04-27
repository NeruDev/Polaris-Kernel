# yaml_frontmatter:
#   id: 'derivada_concepto'
#   title: 'Interpretacion geometrica de la derivada'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'analisis', 'derivada', 'tangente']

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
    x = np.linspace(0, 2, 100)

    def f(x):
        return x**3 - 2 * x + 2

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, f(x), color=colors["text"], lw=2, label="f(x)")

    # Punto de tangencia
    a = 1.0
    fa = f(a)
    dfa = 3 * a**2 - 2  # f'(x) = 3x^2 - 2

    # Recta tangente
    def tangent(x):
        return fa + dfa * (x - a)

    ax.plot(x, tangent(x), color=colors["primary"], lw=1.5, ls="--", label="Recta Tangente")
    ax.scatter(a, fa, color=colors["primary"], s=50, zorder=5)

    ax.set_title(r"Derivada: Pendiente de la Tangente $f'(a)$")
    ax.set_ylim(0, 4)
    ax.legend()

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "03_analisis_continuidad"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "derivada_concepto.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'derivada_concepto.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
