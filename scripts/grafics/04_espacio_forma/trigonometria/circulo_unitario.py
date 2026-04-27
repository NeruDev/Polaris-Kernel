# yaml_frontmatter:
#   id: 'circulo_unitario'
#   title: 'El circulo unitario y proyecciones trigonometricas'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'trigonometria', 'seno', 'coseno']

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from pathlib import Path

# Configurar path para imports del proyecto
PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.templates import setup_style, get_colors

def generate():
    setup_style()
    colors = get_colors()
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Dibujar circulo
    circle = patches.Circle((0,0), 1, fill=False, color=colors["text"], lw=1.5)
    ax.add_patch(circle)
    
    # Ejes
    ax.axhline(0, color=colors["text"], lw=0.8)
    ax.axvline(0, color=colors["text"], lw=0.8)
    
    # Angulo y proyecciones (45 grados)
    theta = np.radians(45)
    x, y = np.cos(theta), np.sin(theta)
    
    # Radio
    ax.plot([0, x], [0, y], color=colors["primary"], lw=2, label="Radio=1")
    # Coseno (Base)
    ax.plot([0, x], [0, 0], color=colors["accent"], lw=3, label="$\cos(\\theta)$")
    # Seno (Altura)
    ax.plot([x, x], [0, y], color=colors["secondary"], lw=3, label="$\sin(\\theta)$")
    
    # Arco de angulo
    arc = patches.Arc((0,0), 0.4, 0.4, theta1=0, theta2=45, color=colors["primary"], lw=1)
    ax.add_patch(arc)
    ax.text(0.25, 0.1, "$\\theta$", color=colors["primary"], fontsize=12)

    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.legend(loc="upper right", fontsize=8)
    ax.set_title("Círculo Unitario")
    
    return fig

if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "04_espacio_forma"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "circulo_unitario.svg", format='svg')
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'circulo_unitario.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
