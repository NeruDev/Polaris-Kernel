# yaml_frontmatter:
#   id: 'triangulos_congruencia'
#   title: 'Criterios de congruencia: LLL, LAL, ALA, AAL'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria']

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[3]))
from templates import setup_style, get_colors
import matplotlib.pyplot as plt
import numpy as np
def draw_marked_triangle(ax, vertices, marks_config, colors_dict, x_offset=0):
        A, B, C = [np.array(v) + np.array([x_offset, 0]) for v in vertices]
    
    # Dibujar triángulo
    triangle = plt.Polygon([A, B, C], fill=True, facecolor=colors_dict['primary'],
                          alpha=0.1, edgecolor=colors_dict['primary'], linewidth=2)
    ax.add_patch(triangle)
    
    # Marcas en los lados
    sides = [(A, B, 'c'), (B, C, 'a'), (C, A, 'b')]
    for (p1, p2, name), mark_info in zip(sides, marks_config.get('sides', [])):
        if mark_info > 0:
            mid = (p1 + p2) / 2
            dx, dy = p2 - p1
            length = np.sqrt(dx**2 + dy**2)
            perp = np.array([-dy/length, dx/length])
            
            mark_len = 0.08
            for i in range(mark_info):
                offset = (i - (mark_info-1)/2) * 0.06
                mx = mid[0] + offset * dx/length
                my = mid[1] + offset * dy/length
                ax.plot([mx - mark_len*perp[0], mx + mark_len*perp[0]],
                       [my - mark_len*perp[1], my + mark_len*perp[1]],
                       color=colors_dict['secondary'], lw=2)
    
    # Arcos de ángulos
    angle_vertices = [(A, B, C), (B, C, A), (C, A, B)]
    for (vertex, p1, p2), highlight in zip(angle_vertices, marks_config.get('angles', [])):
        if highlight:
            v1 = p1 - vertex
            v2 = p2 - vertex
            angle1 = np.arctan2(v1[1], v1[0])
            angle2 = np.arctan2(v2[1], v2[0])
            if angle2 < angle1:
                angle2 += 2 * np.pi
            angles = np.linspace(angle1, angle2, 20)
            r = 0.15
            ax.plot(vertex[0] + r*np.cos(angles), vertex[1] + r*np.sin(angles),
                   color=colors_dict['accent'], lw=2)

def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10), layout='constrained')
    axes = axes.flatten()
    
    # Vértices base
    base_tri = [(0, 0), (1.5, 0), (0.5, 1.2)]
    
    criterios = [
        {
            'name': 'LLL (Lado-Lado-Lado)',
            'desc': '3 lados iguales',
            'sides': [1, 1, 1],
            'angles': [False, False, False]
        },
        {
            'name': 'LAL (Lado-Ángulo-Lado)',
            'desc': '2 lados y el ángulo comprendido',
            'sides': [1, 0, 2],
            'angles': [True, False, False]
        },
        {
            'name': 'ALA (Ángulo-Lado-Ángulo)',
            'desc': '2 ángulos y el lado comprendido',
            'sides': [1, 0, 0],
            'angles': [True, True, False]
        },
        {
            'name': 'AAL (Ángulo-Ángulo-Lado)',
            'desc': '2 ángulos y un lado opuesto',
            'sides': [0, 1, 0],
            'angles': [True, True, False]
        }
    ]
    
    for ax, criterio in zip(axes, criterios):
        ax.set_xlim(-0.5, 4)
        ax.set_ylim(-0.5, 1.8)
        ax.set_aspect('equal')
        ax.axis('off')
        
        config = {
            'sides': criterio['sides'],
            'angles': criterio['angles']
        }
        
        # Dibujar dos triángulos congruentes
        draw_marked_triangle(ax, base_tri, config, colors, x_offset=0)
        draw_marked_triangle(ax, base_tri, config, colors, x_offset=2)
        
        # Símbolo de congruencia
        ax.text(1.75, 0.6, '≅', fontsize=24, ha='center', va='center', 
                color=colors['tertiary'], fontweight='bold')
        
        # Título
        ax.text(1.75, 1.6, criterio['name'], fontsize=12, ha='center', 
                fontweight='bold', color='#1f2937')
        ax.text(1.75, 1.35, criterio['desc'], fontsize=10, ha='center', 
                color='#6b7280', style='italic')
    
    fig.suptitle('Criterios de Congruencia de Triángulos', fontsize=14, 
                 fontweight='bold')
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "triangulos_congruencia.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'triangulos_congruencia.svg'}")
