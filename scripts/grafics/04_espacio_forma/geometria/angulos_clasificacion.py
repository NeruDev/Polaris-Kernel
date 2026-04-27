# yaml_frontmatter:
#   id: 'angulos_clasificacion'
#   title: 'Clasificacion de angulos por su amplitud'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria', 'angulos']

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

def draw_angle(ax, center, angle, label, color):
    # Dibujar semirrectas
    ax.plot([center[0], center[0] + 1.5], [center[1], center[1]], 
            color=color, lw=2)
    rad = np.radians(angle)
    ax.plot([center[0], center[0] + 1.5 * np.cos(rad)], 
            [center[1], center[1] + 1.5 * np.sin(rad)], 
            color=color, lw=2)
    # Arco
    arc = patches.Arc(center, 0.8, 0.8, theta1=0, theta2=angle, 
                      color=color, lw=1.5, ls='--')
    ax.add_patch(arc)
    ax.text(center[0] + 0.5, center[1] + 0.8, label, 
            ha='center', fontsize=10, fontweight='bold')

def generate():
    setup_style()
    colors = get_colors()
    fig, axs = plt.subplots(1, 4, figsize=(15, 4))
    
    # Agudo (45)
    draw_angle(axs[0], (0,0), 45, "Agudo (<90)", colors["primary"])
    # Recto (90)
    draw_angle(axs[1], (0,0), 90, "Recto (90)", colors["secondary"])
    # Obtuso (135)
    draw_angle(axs[2], (0,0), 135, "Obtuso (>90)", colors["accent"])
    # Llano (180)
    draw_angle(axs[3], (0,0), 180, "Llano (180)", colors["danger"])

    for ax in axs:
        ax.set_xlim(-1.8, 1.8)
        ax.set_ylim(-0.5, 1.8)
        ax.set_aspect('equal')
        ax.axis('off')

    fig.tight_layout()
    return fig

if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "04_espacio_forma"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "angulos_clasificacion.svg", format='svg')
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'angulos_clasificacion.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
