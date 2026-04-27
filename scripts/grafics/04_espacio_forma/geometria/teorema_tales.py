# yaml_frontmatter:
#   id: 'teorema_tales'
#   title: 'Teorema de Tales: recta paralela divide lados proporcionalmente'
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
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), layout='constrained')
    
    # === Versión en triángulo ===
    A = np.array([2, 4])
    B = np.array([0, 0])
    C = np.array([5, 0])
    
    # Puntos D y E en los lados AB y AC
    t = 0.6  # proporción
    D = B + t * (A - B)
    E = C + t * (A - C)
    
    # Triángulo completo
    ax1.plot([A[0], B[0]], [A[1], B[1]], color=colors['primary'], lw=2.5)
    ax1.plot([A[0], C[0]], [A[1], C[1]], color=colors['primary'], lw=2.5)
    ax1.plot([B[0], C[0]], [B[1], C[1]], color=colors['primary'], lw=2.5)
    
    # Línea paralela DE
    ax1.plot([D[0], E[0]], [D[1], E[1]], color=colors['secondary'], lw=2.5, 
             label='DE ∥ BC')
    
    # Extender para mostrar paralelismo
    ax1.plot([B[0]-0.3, C[0]+0.3], [B[1], C[1]], '--', color=colors['primary'], 
             lw=1, alpha=0.5)
    ax1.plot([D[0]-0.2, E[0]+0.2], [D[1], E[1]], '--', color=colors['secondary'], 
             lw=1, alpha=0.5)
    
    # Vértices
    for p, label, offset in [(A, 'A', (0, 0.2)), (B, 'B', (-0.3, -0.1)), 
                              (C, 'C', (0.2, -0.1)), (D, 'D', (-0.35, 0)), 
                              (E, 'E', (0.2, 0))]:
        ax1.plot(p[0], p[1], 'o', color='#374151', markersize=6)
        ax1.text(p[0]+offset[0], p[1]+offset[1], label, fontsize=11, fontweight='bold')
    
    # Etiquetas de segmentos
    ax1.text((A[0]+D[0])/2 - 0.4, (A[1]+D[1])/2, 'AD', fontsize=10, color=colors['accent'])
    ax1.text((D[0]+B[0])/2 - 0.4, (D[1]+B[1])/2, 'DB', fontsize=10, color=colors['accent'])
    ax1.text((A[0]+E[0])/2 + 0.2, (A[1]+E[1])/2, 'AE', fontsize=10, color=colors['tertiary'])
    ax1.text((E[0]+C[0])/2 + 0.2, (E[1]+C[1])/2, 'EC', fontsize=10, color=colors['tertiary'])
    
    # Símbolo de paralelismo
    ax1.text(2.5, 1.5, '∥', fontsize=20, color='#6b7280', rotation=0)
    
    ax1.set_title('Teorema de Tales en Triángulo', fontsize=12, fontweight='bold', pad=10)
    ax1.text(2.5, -0.8, r'Si DE ∥ BC:', ha='center', fontsize=11, color='#374151')
    ax1.text(2.5, -1.3, r'$\frac{AD}{DB} = \frac{AE}{EC}$', ha='center', fontsize=14, 
             color=colors['primary'])
    
    ax1.set_xlim(-0.8, 5.8)
    ax1.set_ylim(-1.8, 4.8)
    ax1.set_aspect('equal')
    ax1.axis('off')
    
    # === Versión con rectas paralelas y transversales ===
    # Tres rectas paralelas horizontales
    y_lines = [0, 1.5, 3.5]
    for y in y_lines:
        ax2.axhline(y=y, color='#374151', lw=2, xmin=0.05, xmax=0.95)
    
    # Etiquetas de rectas paralelas
    ax2.text(-0.3, 0, 'ℓ₁', fontsize=11, color='#374151')
    ax2.text(-0.3, 1.5, 'ℓ₂', fontsize=11, color='#374151')
    ax2.text(-0.3, 3.5, 'ℓ₃', fontsize=11, color='#374151')
    
    # Primera transversal
    t1_x = [0.5, 1.5, 3]
    ax2.plot(t1_x, y_lines, color=colors['primary'], lw=2.5)
    for x, y in zip(t1_x, y_lines):
        ax2.plot(x, y, 'o', color=colors['primary'], markersize=7)
    ax2.text(t1_x[0]-0.1, y_lines[0]-0.35, 'A', fontsize=10, ha='center')
    ax2.text(t1_x[1]-0.1, y_lines[1]-0.35, 'B', fontsize=10, ha='center')
    ax2.text(t1_x[2]-0.1, y_lines[2]+0.2, 'C', fontsize=10, ha='center')
    
    # Segunda transversal
    t2_x = [2, 2.8, 4]
    ax2.plot(t2_x, y_lines, color=colors['secondary'], lw=2.5)
    for x, y in zip(t2_x, y_lines):
        ax2.plot(x, y, 'o', color=colors['secondary'], markersize=7)
    ax2.text(t2_x[0]+0.1, y_lines[0]-0.35, "A'", fontsize=10, ha='center')
    ax2.text(t2_x[1]+0.1, y_lines[1]-0.35, "B'", fontsize=10, ha='center')
    ax2.text(t2_x[2]+0.1, y_lines[2]+0.2, "C'", fontsize=10, ha='center')
    
    # Etiquetas de segmentos
    ax2.text(0.8, 0.75, 'a', fontsize=11, color=colors['accent'], fontweight='bold')
    ax2.text(2.0, 2.5, 'b', fontsize=11, color=colors['accent'], fontweight='bold')
    ax2.text(2.2, 0.75, "a'", fontsize=11, color=colors['tertiary'], fontweight='bold')
    ax2.text(3.2, 2.5, "b'", fontsize=11, color=colors['tertiary'], fontweight='bold')
    
    ax2.set_title('Teorema de Tales General', fontsize=12, fontweight='bold', pad=10)
    ax2.text(2.25, -0.8, 'Si ℓ₁ ∥ ℓ₂ ∥ ℓ₃:', ha='center', fontsize=11, color='#374151')
    ax2.text(2.25, -1.3, r"$\frac{a}{b} = \frac{a'}{b'}$", ha='center', fontsize=14, 
             color=colors['primary'])
    
    ax2.set_xlim(-0.6, 4.8)
    ax2.set_ylim(-1.8, 4.3)
    ax2.set_aspect('equal')
    ax2.axis('off')
    
    fig.suptitle('Teorema de Tales', fontsize=14, fontweight='bold')
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "teorema_tales.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'teorema_tales.svg'}")
