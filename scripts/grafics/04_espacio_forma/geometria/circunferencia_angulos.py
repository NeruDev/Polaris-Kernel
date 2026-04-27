# yaml_frontmatter:
#   id: 'circunferencia_angulos'
#   title: 'Tipos de ángulos: central, inscrito, semi-inscrito'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria']

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[3]))
from templates import setup_style, get_colors
import matplotlib.pyplot as plt
import numpy as np
def draw_circle_with_angle(ax, angle_type, colors_dict):
        # Circunferencia
    theta = np.linspace(0, 2*np.pi, 100)
    r = 1.0
    ax.plot(r*np.cos(theta), r*np.sin(theta), color='#374151', lw=2)
    
    # Centro
    ax.plot(0, 0, 'o', color='#374151', markersize=5)
    ax.text(0.1, -0.15, 'O', fontsize=10, color='#374151')
    
    if angle_type == 'central':
        # Ángulo central (vértice en el centro)
        A = np.array([r*np.cos(np.radians(30)), r*np.sin(np.radians(30))])
        B = np.array([r*np.cos(np.radians(100)), r*np.sin(np.radians(100))])
        O = np.array([0, 0])
        
        ax.plot([O[0], A[0]], [O[1], A[1]], color=colors_dict['primary'], lw=2)
        ax.plot([O[0], B[0]], [O[1], B[1]], color=colors_dict['primary'], lw=2)
        ax.plot(A[0], A[1], 'o', color=colors_dict['secondary'], markersize=6)
        ax.plot(B[0], B[1], 'o', color=colors_dict['secondary'], markersize=6)
        ax.text(A[0]+0.15, A[1], 'A', fontsize=10)
        ax.text(B[0]-0.2, B[1]+0.1, 'B', fontsize=10)
        
        # Arco del ángulo
        arc = np.linspace(np.radians(30), np.radians(100), 30)
        ax.plot(0.25*np.cos(arc), 0.25*np.sin(arc), color=colors_dict['accent'], lw=2)
        ax.text(0.15, 0.35, 'α', fontsize=12, color=colors_dict['accent'], fontweight='bold')
        
        # Arco subtendido (destacado)
        arc_ext = np.linspace(np.radians(30), np.radians(100), 30)
        ax.plot(r*np.cos(arc_ext), r*np.sin(arc_ext), color=colors_dict['secondary'], lw=4, alpha=0.5)
        
        ax.set_title('ÁNGULO CENTRAL', fontsize=11, fontweight='bold', pad=10)
        ax.text(0, -1.5, 'α = arco AB', ha='center', fontsize=10, color='#4b5563')
        
    elif angle_type == 'inscrito':
        # Ángulo inscrito (vértice en la circunferencia)
        A = np.array([r*np.cos(np.radians(20)), r*np.sin(np.radians(20))])
        B = np.array([r*np.cos(np.radians(120)), r*np.sin(np.radians(120))])
        P = np.array([r*np.cos(np.radians(220)), r*np.sin(np.radians(220))])
        
        ax.plot([P[0], A[0]], [P[1], A[1]], color=colors_dict['primary'], lw=2)
        ax.plot([P[0], B[0]], [P[1], B[1]], color=colors_dict['primary'], lw=2)
        ax.plot(A[0], A[1], 'o', color=colors_dict['secondary'], markersize=6)
        ax.plot(B[0], B[1], 'o', color=colors_dict['secondary'], markersize=6)
        ax.plot(P[0], P[1], 'o', color=colors_dict['accent'], markersize=6)
        ax.text(A[0]+0.15, A[1], 'A', fontsize=10)
        ax.text(B[0]-0.2, B[1]+0.1, 'B', fontsize=10)
        ax.text(P[0]-0.2, P[1]-0.15, 'P', fontsize=10)
        
        # Arco del ángulo en P
        v1 = A - P
        v2 = B - P
        a1 = np.arctan2(v1[1], v1[0])
        a2 = np.arctan2(v2[1], v2[0])
        if a1 < a2:
            arc = np.linspace(a1, a2, 30)
        else:
            arc = np.linspace(a1, a2 + 2*np.pi, 30)
        ax.plot(P[0]+0.2*np.cos(arc), P[1]+0.2*np.sin(arc), color=colors_dict['accent'], lw=2)
        ax.text(P[0]+0.25, P[1]+0.3, 'β', fontsize=12, color=colors_dict['accent'], fontweight='bold')
        
        # Arco subtendido
        arc_ext = np.linspace(np.radians(20), np.radians(120), 30)
        ax.plot(r*np.cos(arc_ext), r*np.sin(arc_ext), color=colors_dict['secondary'], lw=4, alpha=0.5)
        
        ax.set_title('ÁNGULO INSCRITO', fontsize=11, fontweight='bold', pad=10)
        ax.text(0, -1.5, 'β = arco AB / 2', ha='center', fontsize=10, color='#4b5563')
        
    elif angle_type == 'semicirculo':
        # Ángulo inscrito en semicírculo
        A = np.array([-r, 0])
        B = np.array([r, 0])
        P = np.array([r*np.cos(np.radians(60)), r*np.sin(np.radians(60))])
        
        ax.plot([A[0], B[0]], [A[1], B[1]], color='#374151', lw=2)  # diámetro
        ax.plot([P[0], A[0]], [P[1], A[1]], color=colors_dict['primary'], lw=2)
        ax.plot([P[0], B[0]], [P[1], B[1]], color=colors_dict['primary'], lw=2)
        
        ax.plot(A[0], A[1], 'o', color=colors_dict['secondary'], markersize=6)
        ax.plot(B[0], B[1], 'o', color=colors_dict['secondary'], markersize=6)
        ax.plot(P[0], P[1], 'o', color=colors_dict['accent'], markersize=6)
        ax.text(A[0]-0.2, A[1], 'A', fontsize=10)
        ax.text(B[0]+0.1, B[1], 'B', fontsize=10)
        ax.text(P[0]+0.1, P[1]+0.1, 'P', fontsize=10)
        
        # Ángulo recto en P
        v1 = (A - P) / np.linalg.norm(A - P) * 0.15
        v2 = (B - P) / np.linalg.norm(B - P) * 0.15
        corner = P + v1
        corner2 = P + v1 + v2
        corner3 = P + v2
        ax.plot([corner[0], corner2[0], corner3[0]], 
               [corner[1], corner2[1], corner3[1]], color=colors_dict['secondary'], lw=1.5)
        
        ax.set_title('ÁNGULO EN SEMICÍRCULO', fontsize=11, fontweight='bold', pad=10)
        ax.text(0, -1.5, '∠APB = 90°', ha='center', fontsize=10, color='#4b5563')
        ax.text(0, -1.8, '(AB es diámetro)', ha='center', fontsize=9, color='#6b7280', style='italic')

def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig, axes = plt.subplots(1, 3, figsize=(14, 5), layout='constrained')
    
    for ax, angle_type in zip(axes, ['central', 'inscrito', 'semicirculo']):
        ax.set_xlim(-1.6, 1.6)
        ax.set_ylim(-2, 1.5)
        ax.set_aspect('equal')
        ax.axis('off')
        draw_circle_with_angle(ax, angle_type, colors)
    
    fig.suptitle('Ángulos en la Circunferencia', fontsize=14, fontweight='bold')
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "circunferencia_angulos.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'circunferencia_angulos.svg'}")
