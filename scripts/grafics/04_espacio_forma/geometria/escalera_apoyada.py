# yaml_frontmatter:
#   id: 'escalera_apoyada'
#   title: 'Problema de escalera apoyada - aplicación del teorema de Pitágoras'
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
    
    # Parámetros: escalera de 5m, base a 3m → altura = 4m
    base = 3
    escalera = 5
    altura = 4  # sqrt(5² - 3²)
    
    # Pared
    ax.fill([0, 0, 0.15, 0.15], [0, 5.5, 5.5, 0], color='#9ca3af', alpha=0.4)
    ax.plot([0, 0], [0, 5.5], color='#374151', lw=3)
    
    # Suelo
    ax.fill([-0.5, 4, 4, -0.5], [0, 0, -0.15, -0.15], color='#d1d5db', alpha=0.5)
    ax.plot([-0.5, 4], [0, 0], color='#374151', lw=3)
    
    # Escalera
    ax.plot([base, 0], [0, altura], color=colors['secondary'], lw=4)
    
    # Puntos
    A = np.array([0, 0])      # esquina
    B = np.array([base, 0])   # pie de escalera
    C = np.array([0, altura]) # contacto con pared
    
    ax.plot(B[0], B[1], 'o', color=colors['primary'], markersize=10)
    ax.plot(C[0], C[1], 'o', color=colors['primary'], markersize=10)
    
    # Ángulo recto
    sq = 0.25
    ax.plot([sq, sq, 0], [0, sq, sq], color='#374151', lw=1.5)
    
    # Etiquetas de distancias
    ax.text(base/2, -0.5, f'{base} m', fontsize=13, ha='center', 
            color=colors['accent'], fontweight='bold')
    ax.annotate('', xy=(base, -0.3), xytext=(0, -0.3),
               arrowprops=dict(arrowstyle='<->', color=colors['accent'], lw=1.5))
    
    ax.text(-0.6, altura/2, f'{altura} m', fontsize=13, ha='center', 
            color=colors['tertiary'], fontweight='bold', rotation=90)
    ax.annotate('', xy=(-0.35, altura), xytext=(-0.35, 0),
               arrowprops=dict(arrowstyle='<->', color=colors['tertiary'], lw=1.5))
    
    # Etiqueta de escalera
    mid_esc = (B + C) / 2
    ax.text(mid_esc[0]+0.4, mid_esc[1]+0.3, f'{escalera} m', fontsize=13, 
            color=colors['secondary'], fontweight='bold', rotation=53)
    
    # Triángulo resaltado (punteado)
    ax.plot([A[0], B[0]], [A[1], B[1]], '--', color=colors['primary'], lw=1.5, alpha=0.5)
    ax.plot([A[0], C[0]], [A[1], C[1]], '--', color=colors['primary'], lw=1.5, alpha=0.5)
    
    # Cuadro del teorema
    ax.text(2.5, 4.5, 'Teorema de Pitágoras:', fontsize=11, fontweight='bold', 
            color='#374151')
    ax.text(2.5, 4, r'$escalera^2 = altura^2 + base^2$', fontsize=11)
    ax.text(2.5, 3.5, r'$5^2 = 4^2 + 3^2$', fontsize=11, color=colors['primary'])
    ax.text(2.5, 3, r'$25 = 16 + 9$ ✓', fontsize=11, color=colors['accent'])
    
    # Detalles visuales
    # Peldaños de la escalera
    for i in range(1, 10):
        t = i / 10
        px = base * (1 - t)
        py = altura * t
        dx = 0.08
        ax.plot([px-dx, px+dx], [py-dx*altura/base, py+dx*altura/base], 
               color=colors['secondary'], lw=1.5, alpha=0.7)
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 5.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    ax.set_title('Problema de la Escalera Apoyada', fontsize=14, fontweight='bold', pad=15)
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "escalera_apoyada.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'escalera_apoyada.svg'}")
