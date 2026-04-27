# yaml_frontmatter:
#   id: 'limite_concepto'
#   title: 'Definicion visual de limite de una funcion'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'analisis', 'limite']

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.templates import setup_style, get_colors

def generate():
    setup_style()
    colors = get_colors()
    x = np.linspace(0.5, 2.5, 100)
    y = x**2
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y, color=colors["primary"], lw=2, label=r"$f(x) = x^2$")
    
    # Punto de limite
    a, L = 1.5, 1.5**2
    ax.scatter(a, L, color=colors["danger"], zorder=5)
    
    # Lineas de tendencia
    ax.hlines(L, 0, a, colors=colors["text"], ls="--", alpha=0.3)
    ax.vlines(a, 0, L, colors=colors["text"], ls="--", alpha=0.3)
    
    # Flechas de acercamiento
    ax.annotate("", xy=(a-0.1, 0.1), xytext=(a-0.5, 0.1), arrowprops=dict(arrowstyle="->", color=colors["accent"]))
    ax.annotate("", xy=(a+0.1, 0.1), xytext=(a+0.5, 0.1), arrowprops=dict(arrowstyle="->", color=colors["accent"]))
    
    ax.set_title(r"Concepto de Límite: $\lim_{x \to a} f(x) = L$")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    
    return fig

if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "03_analisis_continuidad"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "limite_concepto.svg", format='svg')
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'limite_concepto.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
