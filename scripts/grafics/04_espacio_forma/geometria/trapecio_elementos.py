# yaml_frontmatter:
#   id: 'trapecio_elementos'
#   title: 'Trapecio con bases, altura, mediana y fórmulas'
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
    
    fig, ax = plt.subplots(figsize=(11, 8), layout='constrained')
    
    # Trapecio ABCD
    A = np.array([0, 0])
    B = np.array([6, 0])
    C = np.array([5, 2.5])
    D = np.array([1.5, 2.5])
    
    # Trapecio
    trap = plt.Polygon([A, B, C, D], fill=True, facecolor=colors['primary'],
                       alpha=0.2, edgecolor=colors['primary'], linewidth=2.5)
    ax.add_patch(trap)
    
    # Base mayor (AB) - destacada
    ax.plot([A[0], B[0]], [A[1], B[1]], color=colors['secondary'], lw=3)
    ax.text(3, -0.4, 'B (base mayor)', fontsize=11, ha='center', 
            color=colors['secondary'], fontweight='bold')
    
    # Base menor (CD) - destacada
    ax.plot([D[0], C[0]], [D[1], C[1]], color=colors['accent'], lw=3)
    ax.text(3.25, 2.8, 'b (base menor)', fontsize=11, ha='center', 
            color=colors['accent'], fontweight='bold')
    
    # Altura
    H = np.array([3, 0])  # pie de la altura
    ax.plot([3, 3], [0, 2.5], '--', color=colors['tertiary'], lw=2)
    ax.plot([3-0.15, 3-0.15, 3], [0, 0.15, 0.15], color=colors['tertiary'], lw=1.5)
    ax.text(3.2, 1.25, 'h', fontsize=12, color=colors['tertiary'], fontweight='bold',
           bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.1'))
    
    # Mediana (línea media)
    M1 = (A + D) / 2
    M2 = (B + C) / 2
    ax.plot([M1[0], M2[0]], [M1[1], M2[1]], '-.', color='#f59e0b', lw=2.5)
    ax.text((M1[0]+M2[0])/2 + 0.3, (M1[1]+M2[1])/2 + 0.2, 'm (mediana)', 
            fontsize=10, color='#f59e0b', fontweight='bold')
    
    # Puntos medios
    ax.plot(M1[0], M1[1], 'o', color='#f59e0b', markersize=6)
    ax.plot(M2[0], M2[1], 'o', color='#f59e0b', markersize=6)
    
    # Vértices
    for p, label, offset in [(A, 'A', (-0.3, -0.2)), (B, 'B', (0.2, -0.2)), 
                              (C, 'C', (0.2, 0.1)), (D, 'D', (-0.3, 0.1))]:
        ax.plot(p[0], p[1], 'o', color=colors['primary'], markersize=7)
        ax.text(p[0]+offset[0], p[1]+offset[1], label, fontsize=11, fontweight='bold',
               bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.1'))
    
    # Diagonales (punteadas)
    ax.plot([A[0], C[0]], [A[1], C[1]], ':', color='#9ca3af', lw=1.5, alpha=0.7)
    ax.plot([B[0], D[0]], [B[1], D[1]], ':', color='#9ca3af', lw=1.5, alpha=0.7)
    
    # Símbolos de paralelismo
    ax.text(0.5, 1.25, '∥', fontsize=14, color='#6b7280', rotation=90)
    
    # Cuadro de fórmulas
    formulas = [
        ('Área:', r'$A = \frac{(B + b) \cdot h}{2}$'),
        ('Mediana:', r'$m = \frac{B + b}{2}$'),
        ('Perímetro:', r'$P = B + b + c_1 + c_2$'),
    ]
    
    ax.text(7.5, 2.3, 'FÓRMULAS', fontsize=11, fontweight='bold', color='#374151')
    for i, (label, formula) in enumerate(formulas):
        ax.text(7.5, 1.8 - i*0.6, label, fontsize=10, color='#374151')
        ax.text(7.5, 1.5 - i*0.6, formula, fontsize=11, color='#1f2937')
    
    # Tipos de trapecio
    ax.text(7.5, -0.2, 'TIPOS:', fontsize=10, fontweight='bold', color='#374151')
    tipos = ['• Isósceles: lados no paralelos iguales',
             '• Rectángulo: un lado perpendicular',
             '• Escaleno: todos los lados diferentes']
    for i, tipo in enumerate(tipos):
        ax.text(7.5, -0.5 - i*0.35, tipo, fontsize=9, color='#6b7280')
    
    ax.set_xlim(-1, 12)
    ax.set_ylim(-1.8, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    ax.set_title('Trapecio - Elementos y Fórmulas', fontsize=14, fontweight='bold', pad=15)
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "trapecio_elementos.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'trapecio_elementos.svg'}")
