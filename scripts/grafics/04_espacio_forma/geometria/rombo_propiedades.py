# yaml_frontmatter:
#   id: 'rombo_propiedades'
#   title: 'Rombo con diagonales, perpendiculares y fórmulas'
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
    
    fig, ax = plt.subplots(figsize=(10, 8), layout='constrained')
    
    # Rombo con diagonales D=8 y d=6
    D = 4  # semi-diagonal mayor
    d = 3  # semi-diagonal menor
    
    A = np.array([D, 0])   # derecha
    B = np.array([0, d])   # arriba
    C = np.array([-D, 0])  # izquierda
    E = np.array([0, -d])  # abajo (uso E para no confundir con D diagonal)
    
    O = np.array([0, 0])  # centro
    
    # Rombo
    rombo = plt.Polygon([A, B, C, E], fill=True, facecolor=colors['primary'],
                        alpha=0.2, edgecolor=colors['primary'], linewidth=2.5)
    ax.add_patch(rombo)
    
    # Diagonales
    ax.plot([C[0], A[0]], [C[1], A[1]], color=colors['secondary'], lw=2.5,
            label='Diagonal mayor D')
    ax.plot([E[0], B[0]], [E[1], B[1]], color=colors['accent'], lw=2.5,
            label='Diagonal menor d')
    
    # Símbolo de perpendicular en el centro
    sq = 0.25
    ax.plot([sq, sq, 0], [0, sq, sq], color='#374151', lw=1.5)
    
    # Centro
    ax.plot(0, 0, 'o', color='#374151', markersize=8)
    ax.text(0.2, -0.35, 'O', fontsize=11, fontweight='bold',
           bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.1'))
    
    # Vértices
    for p, label, offset in [(A, 'A', (0.2, 0)), (B, 'B', (0.2, 0.2)), 
                              (C, 'C', (-0.4, 0)), (E, 'D', (0.2, -0.2))]:
        ax.plot(p[0], p[1], 'o', color=colors['primary'], markersize=7)
        ax.text(p[0]+offset[0], p[1]+offset[1], label, fontsize=11, fontweight='bold',
               bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.1'))
    
    # Lado (calculado con Pitágoras)
    lado = np.sqrt(D**2 + d**2) / 1  # En realidad es sqrt((D/2)^2 + (d/2)^2) para semi-diagonales
    # Corregido: lado = sqrt(D^2 + d^2) donde D y d son SEMI-diagonales
    lado_real = np.sqrt(D**2 + d**2)
    
    # Etiqueta del lado
    mid_AB = (A + B) / 2
    ax.text(mid_AB[0]+0.3, mid_AB[1]+0.2, 'L', fontsize=12, color=colors['primary'], fontweight='bold')
    
    # Marcas de lados iguales
    for p1, p2 in [(A, B), (B, C), (C, E), (E, A)]:
        mid = (p1 + p2) / 2
        ax.plot(mid[0], mid[1], '|', color=colors['tertiary'], markersize=10, mew=2,
               transform=ax.transData)
    
    # Etiquetas de diagonales
    ax.text(D/2, -0.4, 'D/2', fontsize=11, ha='center', color=colors['secondary'])
    ax.text(-D/2, -0.4, 'D/2', fontsize=11, ha='center', color=colors['secondary'])
    ax.text(0.3, d/2, 'd/2', fontsize=11, color=colors['accent'])
    ax.text(0.3, -d/2, 'd/2', fontsize=11, color=colors['accent'])
    
    # Triángulo rectángulo auxiliar (sombreado)
    tri_aux = plt.Polygon([O, A, B], fill=True, facecolor=colors['tertiary'],
                          alpha=0.15, edgecolor='none')
    ax.add_patch(tri_aux)
    ax.text(1.5, 1, 'L² = (D/2)² + (d/2)²', fontsize=9, color=colors['tertiary'],
           style='italic')
    
    # Cuadro de fórmulas
    formulas = [
        ('Área:', r'$A = \frac{D \cdot d}{2}$'),
        ('Lado:', r'$L = \sqrt{\left(\frac{D}{2}\right)^2 + \left(\frac{d}{2}\right)^2}$'),
        ('Perímetro:', r'$P = 4L$'),
    ]
    
    y_start = -1.5
    for i, (label, formula) in enumerate(formulas):
        ax.text(-3.5, y_start - i*0.6, label, fontsize=10, fontweight='bold', color='#374151')
        ax.text(-2.5, y_start - i*0.6, formula, fontsize=11, color='#1f2937')
    
    # Propiedades
    props = [
        '• Las diagonales son perpendiculares',
        '• Las diagonales se bisecan mutuamente',
        '• Los 4 lados son iguales',
    ]
    
    for i, prop in enumerate(props):
        ax.text(-3.5, 3.8 - i*0.4, prop, fontsize=9, color='#6b7280')
    
    ax.set_xlim(-5, 5.5)
    ax.set_ylim(-3.5, 4.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.legend(loc='upper right', fontsize=10)
    
    ax.set_title('Rombo - Diagonales y Propiedades', fontsize=14, fontweight='bold', pad=15)
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "rombo_propiedades.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'rombo_propiedades.svg'}")
