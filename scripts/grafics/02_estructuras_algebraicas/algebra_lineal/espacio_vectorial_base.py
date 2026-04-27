# yaml_frontmatter:
#   id: 'espacio_vectorial_base'
#   title: 'Base canonica en R3'
#   pilar: '02_estructuras_algebraicas'
#   tags: ['grafico', 'algebra', 'vectores', 'base']

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
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    # Vectores base
    ax.quiver(0, 0, 0, 1, 0, 0, color=colors["danger"], lw=3, label=r"$\hat{i}$")
    ax.quiver(0, 0, 0, 0, 1, 0, color=colors["secondary"], lw=3, label=r"$\hat{j}$")
    ax.quiver(0, 0, 0, 0, 0, 1, color=colors["primary"], lw=3, label=r"$\hat{k}$")
    
    ax.set_xlim(0, 1.2)
    ax.set_ylim(0, 1.2)
    ax.set_zlim(0, 1.2)
    ax.set_title("Base Canónica en $\mathbb{R}^3$")
    ax.legend()
    
    return fig

if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "02_estructuras_algebraicas"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "espacio_vectorial_base.svg", format='svg')
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'espacio_vectorial_base.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
