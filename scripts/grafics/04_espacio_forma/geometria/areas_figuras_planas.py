# yaml_frontmatter:
#   id: 'areas_figuras_planas'
#   title: 'Fórmulas de área: cuadrado, rectángulo, triángulo, paralelogramo, trapecio, círculo'
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
    
    fig, axes = plt.subplots(2, 3, figsize=(14, 10), layout='constrained')
    axes = axes.flatten()
    
    # === Cuadrado ===
    ax = axes[0]
    sq = plt.Polygon([(0, 0), (1.5, 0), (1.5, 1.5), (0, 1.5)], 
                     fill=True, facecolor=colors['primary'], alpha=0.3,
                     edgecolor=colors['primary'], linewidth=2)
    ax.add_patch(sq)
    ax.text(0.75, -0.3, 'l', fontsize=12, ha='center', color=colors['primary'], fontweight='bold')
    ax.text(-0.25, 0.75, 'l', fontsize=12, ha='center', color=colors['primary'], fontweight='bold')
    ax.set_title('CUADRADO', fontsize=11, fontweight='bold', pad=10)
    ax.text(0.75, -0.7, r'$A = l^2$', fontsize=13, ha='center', color='#1f2937')
    
    # === Rectángulo ===
    ax = axes[1]
    rect = plt.Polygon([(0, 0), (2, 0), (2, 1.2), (0, 1.2)], 
                       fill=True, facecolor=colors['secondary'], alpha=0.3,
                       edgecolor=colors['secondary'], linewidth=2)
    ax.add_patch(rect)
    ax.text(1, -0.3, 'b', fontsize=12, ha='center', color=colors['secondary'], fontweight='bold')
    ax.text(-0.25, 0.6, 'h', fontsize=12, ha='center', color=colors['secondary'], fontweight='bold')
    ax.set_title('RECTÁNGULO', fontsize=11, fontweight='bold', pad=10)
    ax.text(1, -0.7, r'$A = b \cdot h$', fontsize=13, ha='center', color='#1f2937')
    
    # === Triángulo ===
    ax = axes[2]
    tri = plt.Polygon([(0, 0), (2, 0), (0.8, 1.4)], 
                      fill=True, facecolor=colors['accent'], alpha=0.3,
                      edgecolor=colors['accent'], linewidth=2)
    ax.add_patch(tri)
    # Altura
    ax.plot([0.8, 0.8], [0, 1.4], '--', color=colors['tertiary'], lw=1.5)
    ax.plot([0.8, 0.95], [0, 0], color=colors['tertiary'], lw=1.5)
    ax.plot([0.95, 0.95], [0, 0.15], color=colors['tertiary'], lw=1)
    ax.text(1, -0.3, 'b', fontsize=12, ha='center', color=colors['accent'], fontweight='bold')
    ax.text(0.55, 0.7, 'h', fontsize=12, ha='center', color=colors['tertiary'], fontweight='bold')
    ax.set_title('TRIÁNGULO', fontsize=11, fontweight='bold', pad=10)
    ax.text(1, -0.7, r'$A = \frac{b \cdot h}{2}$', fontsize=13, ha='center', color='#1f2937')
    
    # === Paralelogramo ===
    ax = axes[3]
    para = plt.Polygon([(0.4, 0), (2.2, 0), (2.6, 1.3), (0.8, 1.3)], 
                       fill=True, facecolor=colors['tertiary'], alpha=0.3,
                       edgecolor=colors['tertiary'], linewidth=2)
    ax.add_patch(para)
    # Altura
    ax.plot([1.5, 1.5], [0, 1.3], '--', color=colors['primary'], lw=1.5)
    ax.plot([1.5, 1.65], [0, 0], color=colors['primary'], lw=1.5)
    ax.text(1.3, -0.3, 'b', fontsize=12, ha='center', color=colors['tertiary'], fontweight='bold')
    ax.text(1.25, 0.65, 'h', fontsize=12, ha='center', color=colors['primary'], fontweight='bold')
    ax.set_title('PARALELOGRAMO', fontsize=11, fontweight='bold', pad=10)
    ax.text(1.5, -0.7, r'$A = b \cdot h$', fontsize=13, ha='center', color='#1f2937')
    
    # === Trapecio ===
    ax = axes[4]
    trap = plt.Polygon([(0.3, 0), (2.3, 0), (1.8, 1.2), (0.7, 1.2)], 
                       fill=True, facecolor='#f59e0b', alpha=0.3,
                       edgecolor='#f59e0b', linewidth=2)
    ax.add_patch(trap)
    # Altura
    ax.plot([1.3, 1.3], [0, 1.2], '--', color=colors['primary'], lw=1.5)
    ax.text(1.3, -0.3, 'B', fontsize=12, ha='center', color='#f59e0b', fontweight='bold')
    ax.text(1.25, 1.4, 'b', fontsize=12, ha='center', color='#f59e0b', fontweight='bold')
    ax.text(1.05, 0.6, 'h', fontsize=12, ha='center', color=colors['primary'], fontweight='bold')
    ax.set_title('TRAPECIO', fontsize=11, fontweight='bold', pad=10)
    ax.text(1.3, -0.7, r'$A = \frac{(B + b) \cdot h}{2}$', fontsize=13, ha='center', color='#1f2937')
    
    # === Círculo ===
    ax = axes[5]
    theta = np.linspace(0, 2*np.pi, 100)
    r = 0.9
    ax.fill(1 + r*np.cos(theta), 0.7 + r*np.sin(theta), 
            color='#ec4899', alpha=0.3)
    ax.plot(1 + r*np.cos(theta), 0.7 + r*np.sin(theta), 
            color='#ec4899', lw=2)
    # Radio
    ax.plot([1, 1+r], [0.7, 0.7], color=colors['primary'], lw=2)
    ax.plot(1, 0.7, 'o', color='#374151', markersize=4)
    ax.text(1.45, 0.85, 'r', fontsize=12, color=colors['primary'], fontweight='bold')
    ax.set_title('CÍRCULO', fontsize=11, fontweight='bold', pad=10)
    ax.text(1, -0.55, r'$A = \pi r^2$', fontsize=13, ha='center', color='#1f2937')
    
    for ax in axes:
        ax.set_xlim(-0.5, 2.7)
        ax.set_ylim(-1, 2)
        ax.set_aspect('equal')
        ax.axis('off')
    
    fig.suptitle('Fórmulas de Áreas de Figuras Planas', fontsize=14, 
                 fontweight='bold')
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "areas_figuras_planas.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'areas_figuras_planas.svg'}")
