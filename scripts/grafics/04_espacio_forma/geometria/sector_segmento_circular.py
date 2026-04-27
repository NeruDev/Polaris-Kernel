# yaml_frontmatter:
#   id: 'sector_segmento_circular'
#   title: 'Sector circular y segmento circular con fórmulas'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria']

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[3]))
from templates import setup_style, get_colors
import matplotlib.pyplot as plt
import numpy as np
def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), layout='constrained')
    
    r = 2.0
    theta1 = np.radians(20)
    theta2 = np.radians(100)
    
    # === SECTOR CIRCULAR ===
    # Circunferencia completa (línea tenue)
    theta_full = np.linspace(0, 2*np.pi, 100)
    ax1.plot(r*np.cos(theta_full), r*np.sin(theta_full), color='#d1d5db', lw=1.5)
    
    # Sector (relleno)
    theta_sector = np.linspace(theta1, theta2, 50)
    sector_x = np.concatenate([[0], r*np.cos(theta_sector), [0]])
    sector_y = np.concatenate([[0], r*np.sin(theta_sector), [0]])
    ax1.fill(sector_x, sector_y, color=colors['primary'], alpha=0.4)
    ax1.plot(r*np.cos(theta_sector), r*np.sin(theta_sector), color=colors['primary'], lw=3)
    
    # Radios
    ax1.plot([0, r*np.cos(theta1)], [0, r*np.sin(theta1)], color=colors['secondary'], lw=2.5)
    ax1.plot([0, r*np.cos(theta2)], [0, r*np.sin(theta2)], color=colors['secondary'], lw=2.5)
    
    # Centro
    ax1.plot(0, 0, 'o', color='#374151', markersize=6)
    ax1.text(0.15, -0.35, 'O', fontsize=11, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.1'))
    
    # Arco del ángulo central
    arc_angle = np.linspace(theta1, theta2, 30)
    ax1.plot(0.4*np.cos(arc_angle), 0.4*np.sin(arc_angle), color=colors['accent'], lw=2)
    ax1.text(0.55, 0.55, 'θ', fontsize=14, color=colors['accent'], fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.1'))
    
    # Etiquetas con bbox
    ax1.text(r*np.cos((theta1+theta2)/2)*1.2, r*np.sin((theta1+theta2)/2)*1.2, 
            'arco', fontsize=10, color=colors['primary'], fontweight='bold', ha='center',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.2'))
    ax1.text(r*np.cos(theta1)*0.55, r*np.sin(theta1)*0.55 - 0.2, 
            'r', fontsize=12, color=colors['secondary'], fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.1'))
    
    ax1.set_title('SECTOR CIRCULAR', fontsize=12, fontweight='bold', pad=15)
    
    # Fórmulas - en un cuadro separado debajo
    formula_box = dict(facecolor='#f8fafc', alpha=0.95, edgecolor='#e2e8f0', 
                       boxstyle='round,pad=0.5', linewidth=1)
    ax1.text(0, -3.0, 'Área: $A = \\frac{\\theta}{360°} \\cdot \\pi r^2$\n\nArco: $L = \\frac{\\theta}{360°} \\cdot 2\\pi r$', 
            fontsize=11, ha='center', va='top', color='#1f2937', bbox=formula_box)
    
    ax1.set_xlim(-2.8, 2.8)
    ax1.set_ylim(-4.2, 2.8)
    ax1.set_aspect('equal')
    ax1.axis('off')
    
    # === SEGMENTO CIRCULAR ===
    # Circunferencia completa
    ax2.plot(r*np.cos(theta_full), r*np.sin(theta_full), color='#d1d5db', lw=1.5)
    
    # Segmento (región entre cuerda y arco)
    A = np.array([r*np.cos(theta1), r*np.sin(theta1)])
    B = np.array([r*np.cos(theta2), r*np.sin(theta2)])
    
    # Relleno del segmento
    segment_x = np.concatenate([r*np.cos(theta_sector), [A[0]]])
    segment_y = np.concatenate([r*np.sin(theta_sector), [A[1]]])
    ax2.fill(segment_x, segment_y, color=colors['tertiary'], alpha=0.4)
    
    # Arco
    ax2.plot(r*np.cos(theta_sector), r*np.sin(theta_sector), color=colors['tertiary'], lw=3)
    
    # Cuerda
    ax2.plot([A[0], B[0]], [A[1], B[1]], color=colors['secondary'], lw=2.5, 
            label='Cuerda')
    
    # Centro
    ax2.plot(0, 0, 'o', color='#374151', markersize=6)
    ax2.text(0.15, -0.35, 'O', fontsize=11, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.1'))
    
    # Radios (punteados)
    ax2.plot([0, A[0]], [0, A[1]], '--', color='#9ca3af', lw=1.5)
    ax2.plot([0, B[0]], [0, B[1]], '--', color='#9ca3af', lw=1.5)
    
    # Puntos A y B
    ax2.plot(A[0], A[1], 'o', color=colors['secondary'], markersize=7)
    ax2.plot(B[0], B[1], 'o', color=colors['secondary'], markersize=7)
    ax2.text(A[0]+0.2, A[1]-0.25, 'A', fontsize=11, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.1'))
    ax2.text(B[0]-0.15, B[1]+0.25, 'B', fontsize=11, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.1'))
    
    # Etiquetas con bbox
    mid_chord = (A + B) / 2
    ax2.text(mid_chord[0]-0.4, mid_chord[1]-0.35, 'cuerda', fontsize=10, 
            color=colors['secondary'], fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.2'))
    ax2.text(0.4, 2.0, 'segmento', fontsize=10, color=colors['tertiary'], 
            fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.2'))
    
    ax2.set_title('SEGMENTO CIRCULAR', fontsize=12, fontweight='bold', pad=15)
    
    # Fórmulas - en un cuadro separado debajo
    formula_box2 = dict(facecolor='#f8fafc', alpha=0.95, edgecolor='#e2e8f0', 
                        boxstyle='round,pad=0.5', linewidth=1)
    ax2.text(0, -3.0, '$A_{seg} = A_{sector} - A_{triángulo}$\n\n$A_{seg} = \\frac{r^2}{2}(\\theta - \\sin\\theta)$  (θ en rad)', 
            fontsize=11, ha='center', va='top', color='#1f2937', bbox=formula_box2)
    
    ax2.set_xlim(-2.8, 2.8)
    ax2.set_ylim(-4.2, 2.8)
    ax2.set_aspect('equal')
    ax2.axis('off')
    
    fig.suptitle('Sector y Segmento Circular', fontsize=14, fontweight='bold')
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "sector_segmento_circular.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'sector_segmento_circular.svg'}")
