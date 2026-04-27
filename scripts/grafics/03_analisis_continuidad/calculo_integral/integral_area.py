# yaml_frontmatter:
#   id: 'integral_area'
#   title: 'Area bajo la curva e integracion'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'analisis', 'integral', 'riemann']

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
    x = np.linspace(0, 4, 100)
    f = lambda x: 0.5 * x**2 + 1
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, f(x), color=colors["text"], lw=2)
    
    # Rellenar area entre 1 y 3
    a, b = 1, 3
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color=colors["secondary"], alpha=0.3, label="Área definida")
    
    # Rectangulos de Riemann (ejemplo con 4)
    n = 6
    dx = (b-a)/n
    x_rects = np.linspace(a, b-dx, n)
    ax.bar(x_rects, f(x_rects), width=dx, align='edge', 
           color='none', edgecolor=colors["primary"], alpha=0.5, label="Suma de Riemann")
    
    ax.set_title(r"Integral Definida: $\int_a^b f(x) \, dx$")
    ax.legend()
    
    return fig

if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "03_analisis_continuidad"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "integral_area.svg", format='svg')
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'integral_area.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
