# yaml_frontmatter:
#   id: 'triangulo_equilatero_elementos'
#   title: 'Triángulo equilátero con altura, radio inscrito y circunscrito'
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
    
    fig, ax = plt.subplots(figsize=(10, 9), layout='constrained')
    
    # Triángulo equilátero de lado L
    L = 4
    h = L * np.sqrt(3) / 2  # altura
    
    A = np.array([0, 0])
    B = np.array([L, 0])
    C = np.array([L/2, h])
    
    # Centroide (G) = Incentro (I) = Circuncentro (O) en equilátero
    G = (A + B + C) / 3
    
    # Radio inscrito y circunscrito
    r_inscrito = h / 3
    r_circunscrito = 2 * h / 3
    
    # Triángulo
    triangle = plt.Polygon([A, B, C], fill=True, facecolor=colors['primary'],
                          alpha=0.15, edgecolor=colors['primary'], linewidth=2.5)
    ax.add_patch(triangle)
    
    # Altura desde C
    ax.plot([C[0], C[0]], [0, C[1]], '--', color=colors['secondary'], lw=2, 
            label=f'Altura h = L·√3/2')
    ax.plot([C[0]-0.15, C[0]-0.15, C[0]], [0, 0.15, 0.15], color=colors['secondary'], lw=1.5)
    
    # Punto medio de AB (pie de la altura)
    M = np.array([L/2, 0])
    ax.plot(M[0], M[1], 'o', color=colors['secondary'], markersize=6)
    ax.text(M[0], M[1]-0.25, 'M', fontsize=11, ha='center')
    
    # Centro
    ax.plot(G[0], G[1], 'o', color='#374151', markersize=8)
    ax.text(G[0]+0.15, G[1]+0.1, 'G', fontsize=11, fontweight='bold')
    
    # Círculo inscrito
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(G[0] + r_inscrito*np.cos(theta), G[1] + r_inscrito*np.sin(theta),
           color=colors['accent'], lw=2, label=f'r = h/3 = L·√3/6')
    
    # Radio inscrito
    ax.plot([G[0], G[0]], [G[1], G[1]-r_inscrito], color=colors['accent'], lw=1.5)
    ax.text(G[0]+0.1, G[1]-r_inscrito/2, 'r', fontsize=11, color=colors['accent'], fontweight='bold')
    
    # Círculo circunscrito
    ax.plot(G[0] + r_circunscrito*np.cos(theta), G[1] + r_circunscrito*np.sin(theta),
           color=colors['tertiary'], lw=2, linestyle='--', label=f'R = 2h/3 = L·√3/3')
    
    # Radio circunscrito
    ax.plot([G[0], C[0]], [G[1], C[1]], color=colors['tertiary'], lw=1.5)
    ax.text(G[0]+0.25, (G[1]+C[1])/2, 'R', fontsize=11, color=colors['tertiary'], fontweight='bold')
    
    # Vértices
    for p, label, offset in [(A, 'A', (-0.25, -0.2)), (B, 'B', (0.15, -0.2)), (C, 'C', (0, 0.2))]:
        ax.plot(p[0], p[1], 'o', color=colors['primary'], markersize=8)
        ax.text(p[0]+offset[0], p[1]+offset[1], label, fontsize=12, fontweight='bold')
    
    # Etiqueta lado
    ax.text(L/2, -0.4, 'L', fontsize=13, ha='center', color=colors['primary'], fontweight='bold')
    
    # Etiqueta altura
    ax.text(L/2 + 0.2, h/2, 'h', fontsize=13, color=colors['secondary'], fontweight='bold')
    
    # Cuadro de fórmulas
    formulas = [
        r'$h = \frac{L\sqrt{3}}{2}$',
        r'$A = \frac{L^2\sqrt{3}}{4}$',
        r'$r = \frac{L\sqrt{3}}{6}$',
        r'$R = \frac{L\sqrt{3}}{3}$',
    ]
    
    for i, formula in enumerate(formulas):
        ax.text(4.5, 3 - i*0.5, formula, fontsize=12, color='#1f2937',
               bbox=dict(boxstyle='round', facecolor='white', edgecolor='#d1d5db', alpha=0.9))
    
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 4.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.legend(loc='upper left', fontsize=10)
    
    ax.set_title('Triángulo Equilátero - Elementos', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "triangulo_equilatero_elementos.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'triangulo_equilatero_elementos.svg'}")
