# yaml_frontmatter:
#   id: 'triangulos_clasificacion_angulos'
#   title: 'Clasificación de triángulos: acutángulo, rectángulo, obtusángulo'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria']

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[3]))
from templates import setup_style, get_colors
import matplotlib.pyplot as plt
import numpy as np
def draw_angle_arc(ax, vertex, p1, p2, radius, color, show_right=False):
        # Vectores desde el vértice
    v1 = np.array(p1) - np.array(vertex)
    v2 = np.array(p2) - np.array(vertex)
    
    # Ángulos
    angle1 = np.arctan2(v1[1], v1[0])
    angle2 = np.arctan2(v2[1], v2[0])
    
    if show_right:
        # Símbolo de ángulo recto
        v1_norm = v1 / np.linalg.norm(v1) * radius
        v2_norm = v2 / np.linalg.norm(v2) * radius
        corner = vertex + v1_norm
        corner2 = vertex + v1_norm + v2_norm
        corner3 = vertex + v2_norm
        ax.plot([corner[0], corner2[0], corner3[0]], 
               [corner[1], corner2[1], corner3[1]], color=color, lw=1.5)
    else:
        # Arco normal
        if angle2 < angle1:
            angle2 += 2 * np.pi
        angles = np.linspace(angle1, angle2, 30)
        arc_x = vertex[0] + radius * np.cos(angles)
        arc_y = vertex[1] + radius * np.sin(angles)
        ax.plot(arc_x, arc_y, color=color, lw=2)

def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig, axes = plt.subplots(1, 3, figsize=(14, 5), layout='constrained')
    
    # === Triángulo Acutángulo (todos < 90°) ===
    ax1 = axes[0]
    A1 = np.array([0, 0])
    B1 = np.array([2.5, 0])
    C1 = np.array([1.2, 1.8])
    
    triangle1 = plt.Polygon([A1, B1, C1], fill=True, facecolor=colors['primary'],
                            alpha=0.15, edgecolor=colors['primary'], linewidth=2.5)
    ax1.add_patch(triangle1)
    
    # Arcos en cada vértice
    draw_angle_arc(ax1, A1, B1, C1, 0.3, colors['accent'])
    draw_angle_arc(ax1, B1, C1, A1, 0.3, colors['accent'])
    draw_angle_arc(ax1, C1, A1, B1, 0.3, colors['accent'])
    
    ax1.text(0.15, 0.2, 'α', fontsize=10, color=colors['accent'])
    ax1.text(2.15, 0.2, 'β', fontsize=10, color=colors['accent'])
    ax1.text(1.2, 1.4, 'γ', fontsize=10, color=colors['accent'])
    
    ax1.set_title('ACUTÁNGULO\n(3 ángulos agudos)', fontsize=12, fontweight='bold', pad=10)
    ax1.text(1.25, -0.5, 'α, β, γ < 90°', ha='center', fontsize=11, color='#6b7280')
    
    # === Triángulo Rectángulo (uno = 90°) ===
    ax2 = axes[1]
    A2 = np.array([0, 0])
    B2 = np.array([2.5, 0])
    C2 = np.array([0, 1.8])
    
    triangle2 = plt.Polygon([A2, B2, C2], fill=True, facecolor=colors['secondary'],
                            alpha=0.15, edgecolor=colors['secondary'], linewidth=2.5)
    ax2.add_patch(triangle2)
    
    # Ángulo recto en A
    draw_angle_arc(ax2, A2, B2, C2, 0.2, colors['secondary'], show_right=True)
    # Otros ángulos
    draw_angle_arc(ax2, B2, C2, A2, 0.3, colors['accent'])
    draw_angle_arc(ax2, C2, A2, B2, 0.3, colors['accent'])
    
    ax2.text(2.1, 0.2, 'β', fontsize=10, color=colors['accent'])
    ax2.text(0.15, 1.4, 'γ', fontsize=10, color=colors['accent'])
    
    # Etiqueta hipotenusa
    mid_hyp = (B2 + C2) / 2
    ax2.text(mid_hyp[0] + 0.2, mid_hyp[1] + 0.1, 'hipotenusa', fontsize=9, 
             color=colors['secondary'], rotation=35)
    
    ax2.set_title('RECTÁNGULO\n(1 ángulo recto)', fontsize=12, fontweight='bold', pad=10)
    ax2.text(1.25, -0.5, 'Un ángulo = 90°', ha='center', fontsize=11, color='#6b7280')
    
    # === Triángulo Obtusángulo (uno > 90°) ===
    ax3 = axes[2]
    A3 = np.array([0, 0])
    B3 = np.array([3, 0])
    C3 = np.array([0.5, 1.2])
    
    triangle3 = plt.Polygon([A3, B3, C3], fill=True, facecolor=colors['tertiary'],
                            alpha=0.15, edgecolor=colors['tertiary'], linewidth=2.5)
    ax3.add_patch(triangle3)
    
    # Arcos
    draw_angle_arc(ax3, A3, B3, C3, 0.25, colors['tertiary'])
    draw_angle_arc(ax3, B3, C3, A3, 0.3, colors['accent'])
    draw_angle_arc(ax3, C3, A3, B3, 0.35, colors['accent'])
    
    ax3.text(0.35, 0.15, 'α', fontsize=10, color=colors['tertiary'], fontweight='bold')
    ax3.text(2.6, 0.2, 'β', fontsize=10, color=colors['accent'])
    ax3.text(0.6, 0.85, 'γ', fontsize=10, color=colors['accent'])
    
    ax3.set_title('OBTUSÁNGULO\n(1 ángulo obtuso)', fontsize=12, fontweight='bold', pad=10)
    ax3.text(1.5, -0.5, 'α > 90°', ha='center', fontsize=11, color='#6b7280')
    
    for ax in axes:
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_xlim(-0.5, 3.5)
        ax.set_ylim(-0.8, 2.2)
    
    fig.suptitle('Clasificación de Triángulos por Ángulos', fontsize=14, 
                 fontweight='bold')
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "triangulos_clasificacion_angulos.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'triangulos_clasificacion_angulos.svg'}")
