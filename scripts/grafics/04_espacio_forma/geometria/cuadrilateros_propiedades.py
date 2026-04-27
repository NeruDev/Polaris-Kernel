# yaml_frontmatter:
#   id: 'cuadrilateros_propiedades'
#   title: 'Propiedades de paralelogramo, rectángulo, rombo, cuadrado'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria']

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[3]))
from templates import setup_style, get_colors
import matplotlib.pyplot as plt
import numpy as np
def draw_quadrilateral(ax, vertices, color, show_diagonals=True, 
                       diag_equal=False, diag_perp=False, fill_alpha=0.15):
        A, B, C, D = [np.array(v) for v in vertices]
    
    # Polígono
    quad = plt.Polygon([A, B, C, D], fill=True, facecolor=color,
                       alpha=fill_alpha, edgecolor=color, linewidth=2.5)
    ax.add_patch(quad)
    
    # Vértices
    for p, label in zip([A, B, C, D], ['A', 'B', 'C', 'D']):
        ax.plot(p[0], p[1], 'o', color=color, markersize=5)
    
    if show_diagonals:
        # Diagonales
        ax.plot([A[0], C[0]], [A[1], C[1]], '--', color='#dc2626', lw=1.5, alpha=0.8)
        ax.plot([B[0], D[0]], [B[1], D[1]], '--', color='#059669', lw=1.5, alpha=0.8)
        
        # Centro
        center = (A + C) / 2
        ax.plot(center[0], center[1], 'o', color='#374151', markersize=4)
        
        if diag_perp:
            # Símbolo de perpendicular
            size = 0.12
            ax.plot([center[0]-size, center[0], center[0]], 
                   [center[1], center[1], center[1]+size], 
                   color='#374151', lw=1)
    
    return A, B, C, D

def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10), layout='constrained')
    axes = axes.flatten()
    
    # === Paralelogramo ===
    ax1 = axes[0]
    para_verts = [(0, 0), (2, 0), (2.6, 1.2), (0.6, 1.2)]
    draw_quadrilateral(ax1, para_verts, colors['primary'])
    
    ax1.set_title('PARALELOGRAMO', fontsize=12, fontweight='bold', pad=10)
    ax1.text(1.3, -0.4, '• Lados opuestos paralelos e iguales\n• Diagonales se bisecan', 
             ha='center', fontsize=9, color='#4b5563')
    
    # Marcas de lados paralelos
    ax1.annotate('', xy=(0.8, 0.1), xytext=(1.2, 0.1),
                arrowprops=dict(arrowstyle='<->', color='#6b7280', lw=1))
    ax1.annotate('', xy=(1.4, 1.1), xytext=(1.8, 1.1),
                arrowprops=dict(arrowstyle='<->', color='#6b7280', lw=1))
    
    # === Rectángulo ===
    ax2 = axes[1]
    rect_verts = [(0, 0), (2.2, 0), (2.2, 1.4), (0, 1.4)]
    A, B, C, D = draw_quadrilateral(ax2, rect_verts, colors['secondary'], diag_equal=True)
    
    # Símbolos de ángulos rectos
    sq_size = 0.15
    for corner in [A, B, C, D]:
        x, y = corner
        if np.allclose(corner, A):
            ax2.plot([x+sq_size, x+sq_size, x], [y, y+sq_size, y+sq_size], 
                    color=colors['secondary'], lw=1)
        elif np.allclose(corner, B):
            ax2.plot([x-sq_size, x-sq_size, x], [y, y+sq_size, y+sq_size], 
                    color=colors['secondary'], lw=1)
        elif np.allclose(corner, C):
            ax2.plot([x-sq_size, x-sq_size, x], [y, y-sq_size, y-sq_size], 
                    color=colors['secondary'], lw=1)
        elif np.allclose(corner, D):
            ax2.plot([x+sq_size, x+sq_size, x], [y, y-sq_size, y-sq_size], 
                    color=colors['secondary'], lw=1)
    
    ax2.set_title('RECTÁNGULO', fontsize=12, fontweight='bold', pad=10)
    ax2.text(1.1, -0.4, '• 4 ángulos rectos\n• Diagonales iguales', 
             ha='center', fontsize=9, color='#4b5563')
    
    # === Rombo ===
    ax3 = axes[2]
    rombo_verts = [(1.2, 0), (2.2, 0.8), (1.2, 1.6), (0.2, 0.8)]
    draw_quadrilateral(ax3, rombo_verts, colors['accent'], diag_perp=True)
    
    ax3.set_title('ROMBO', fontsize=12, fontweight='bold', pad=10)
    ax3.text(1.2, -0.4, '• 4 lados iguales\n• Diagonales perpendiculares', 
             ha='center', fontsize=9, color='#4b5563')
    
    # Marcas de lados iguales
    for i, (p1, p2) in enumerate([(rombo_verts[0], rombo_verts[1]), 
                                   (rombo_verts[1], rombo_verts[2]),
                                   (rombo_verts[2], rombo_verts[3]),
                                   (rombo_verts[3], rombo_verts[0])]):
        mid = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
        ax3.plot(mid[0], mid[1], '|', color=colors['accent'], markersize=8, mew=2)
    
    # === Cuadrado ===
    ax4 = axes[3]
    cuad_verts = [(0.3, 0), (1.8, 0), (1.8, 1.5), (0.3, 1.5)]
    A, B, C, D = draw_quadrilateral(ax4, cuad_verts, colors['tertiary'], diag_perp=True)
    
    # Símbolos de ángulos rectos
    for corner in [np.array(v) for v in cuad_verts]:
        x, y = corner
        if np.allclose(corner, [0.3, 0]):
            ax4.plot([x+sq_size, x+sq_size, x], [y, y+sq_size, y+sq_size], 
                    color=colors['tertiary'], lw=1)
        elif np.allclose(corner, [1.8, 0]):
            ax4.plot([x-sq_size, x-sq_size, x], [y, y+sq_size, y+sq_size], 
                    color=colors['tertiary'], lw=1)
        elif np.allclose(corner, [1.8, 1.5]):
            ax4.plot([x-sq_size, x-sq_size, x], [y, y-sq_size, y-sq_size], 
                    color=colors['tertiary'], lw=1)
        elif np.allclose(corner, [0.3, 1.5]):
            ax4.plot([x+sq_size, x+sq_size, x], [y, y-sq_size, y-sq_size], 
                    color=colors['tertiary'], lw=1)
    
    ax4.set_title('CUADRADO', fontsize=12, fontweight='bold', pad=10)
    ax4.text(1.05, -0.4, '• 4 lados iguales + 4 ángulos rectos\n• Diagonales iguales y perpendiculares', 
             ha='center', fontsize=9, color='#4b5563')
    
    for ax in axes:
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_xlim(-0.3, 3)
        ax.set_ylim(-0.8, 2)
    
    fig.suptitle('Propiedades de Cuadriláteros Especiales', fontsize=14, 
                 fontweight='bold')
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "cuadrilateros_propiedades.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'cuadrilateros_propiedades.svg'}")
