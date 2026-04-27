# yaml_frontmatter:
#   id: 'ley_cosenos'
#   title: 'Ley de cosenos para resolución de triángulos oblicuángulos'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'trigonometria']

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[3]))
from templates import setup_style, get_colors
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


    setup_style,
    get_colors,
    get_output_dir_for_topic,
    save_figure,
)


def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig = plt.figure(figsize=(14, 8), layout='constrained')
    gs = fig.add_gridspec(1, 2, width_ratios=[1.2, 1], wspace=0.08)
    
    ax_triangle = fig.add_subplot(gs[0])
    ax_info = fig.add_subplot(gs[1])
    
    # =========================================
    # PANEL IZQUIERDO: Triángulo con proyección
    # =========================================
    
    # Definir vértices
    A = np.array([0.5, 0])
    B = np.array([5, 0])
    C = np.array([1.8, 3])
    
    # Proyección de C sobre AB
    H = np.array([C[0], 0])  # proyección ortogonal
    
    # Dibujar triángulo
    triangle = plt.Polygon([A, B, C], fill=True, facecolor='#eff6ff', 
                           edgecolor=colors['primary'], linewidth=2.5)
    ax_triangle.add_patch(triangle)
    
    # Altura desde C
    ax_triangle.plot([C[0], H[0]], [C[1], H[1]], '--', color='#9ca3af', linewidth=2)
    ax_triangle.text(C[0] + 0.1, C[1]/2, 'h', fontsize=11, color='#6b7280', style='italic')
    
    # Marca de ángulo recto
    sq = 0.15
    ax_triangle.plot([H[0]+sq, H[0]+sq, H[0]], [H[1], H[1]+sq, H[1]+sq], 
                    color='#6b7280', linewidth=1)
    
    # Lados con colores
    ax_triangle.plot([B[0], C[0]], [B[1], C[1]], color=colors['secondary'], linewidth=3)
    ax_triangle.plot([A[0], C[0]], [A[1], C[1]], color=colors['tertiary'], linewidth=3)
    ax_triangle.plot([A[0], B[0]], [A[1], B[1]], color='#f59e0b', linewidth=3)
    
    # Segmentos de proyección
    ax_triangle.plot([A[0], H[0]], [A[1], H[1]], color='#ec4899', linewidth=2.5)
    ax_triangle.text((A[0] + H[0])/2, -0.25, 'x', fontsize=11, ha='center',
                    color='#ec4899', fontweight='bold')
    
    ax_triangle.plot([H[0], B[0]], [H[1], B[1]], color='#8b5cf6', linewidth=2.5)
    ax_triangle.text((H[0] + B[0])/2, -0.25, 'c - x', fontsize=11, ha='center',
                    color='#8b5cf6', fontweight='bold')
    
    # Vértices
    for point, label, offset in [(A, 'A', (-0.3, -0.2)), 
                                  (B, 'B', (0.15, -0.2)), 
                                  (C, 'C', (0, 0.2)),
                                  (H, 'H', (0, -0.35))]:
        ax_triangle.plot(point[0], point[1], 'o', color=colors['primary'], markersize=8, zorder=5)
        ax_triangle.text(point[0] + offset[0], point[1] + offset[1], label,
                        fontsize=12, fontweight='bold', color=colors['primary'])
    
    # Etiquetas de lados
    mid_a = (B + C) / 2
    mid_b = (A + C) / 2
    mid_c = (A + B) / 2
    
    ax_triangle.text(mid_a[0] + 0.2, mid_a[1] + 0.1, 'a', fontsize=13, fontweight='bold',
                    color=colors['secondary'])
    ax_triangle.text(mid_b[0] - 0.35, mid_b[1], 'b', fontsize=13, fontweight='bold',
                    color=colors['tertiary'])
    ax_triangle.text(mid_c[0], mid_c[1] + 0.2, 'c', fontsize=13, fontweight='bold',
                    color='#f59e0b')
    
    # Arco del ángulo A
    v1 = B - A
    v2 = C - A
    angle1 = np.arctan2(v1[1], v1[0])
    angle2 = np.arctan2(v2[1], v2[0])
    arc = np.linspace(angle1, angle2, 30)
    ax_triangle.plot(A[0] + 0.5*np.cos(arc), A[1] + 0.5*np.sin(arc),
                    color='#f59e0b', linewidth=2)
    ax_triangle.text(A[0] + 0.65, A[1] + 0.25, 'A', fontsize=12, fontweight='bold',
                    color='#f59e0b')
    
    ax_triangle.set_xlim(-0.2, 5.8)
    ax_triangle.set_ylim(-0.7, 3.8)
    ax_triangle.set_aspect('equal')
    ax_triangle.axis('off')
    ax_triangle.set_title('Derivación Geométrica', fontsize=11, fontweight='bold')
    
    # =========================================
    # PANEL DERECHO: Fórmulas
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Ley de cosenos - fórmula principal
    ax_info.add_patch(plt.Rectangle((0.03, 0.72), 0.94, 0.24,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=2))
    ax_info.text(0.5, 0.9, 'LEY DE COSENOS', fontsize=12, fontweight='bold',
                ha='center', color='#f59e0b')
    ax_info.text(0.5, 0.78, r'$a^2 = b^2 + c^2 - 2bc\cos A$',
                fontsize=14, ha='center', color=colors['text'])
    
    # Tres formas
    ax_info.add_patch(plt.Rectangle((0.03, 0.42), 0.94, 0.26,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=1.5))
    ax_info.text(0.5, 0.63, 'Tres Formas Equivalentes', fontsize=10, fontweight='bold',
                ha='center', color=colors['primary'])
    
    formulas = [
        (r'$a^2 = b^2 + c^2 - 2bc\cos A$', colors['secondary']),
        (r'$b^2 = a^2 + c^2 - 2ac\cos B$', colors['tertiary']),
        (r'$c^2 = a^2 + b^2 - 2ab\cos C$', '#f59e0b'),
    ]
    y_pos = 0.56
    for formula, color in formulas:
        ax_info.text(0.5, y_pos, formula, fontsize=11, ha='center', color=color)
        y_pos -= 0.065
    
    # Para encontrar ángulos
    ax_info.add_patch(plt.Rectangle((0.03, 0.17), 0.94, 0.22,
                                    facecolor='#f0fdf4', edgecolor=colors['accent'],
                                    linewidth=1.5))
    ax_info.text(0.5, 0.34, 'Para Encontrar Ángulos', fontsize=10, fontweight='bold',
                ha='center', color=colors['accent'])
    ax_info.text(0.5, 0.24, r'$\cos A = \frac{b^2 + c^2 - a^2}{2bc}$',
                fontsize=12, ha='center', color=colors['text'])
    
    # Casos de aplicación
    ax_info.text(0.5, 0.1, 'Usar cuando se conocen:', fontsize=9, fontweight='bold',
                ha='center', color='#6b7280')
    ax_info.text(0.5, 0.04, 'LLL (tres lados) o LAL (dos lados y ángulo incluido)',
                fontsize=9, ha='center', color='#9ca3af', style='italic')
    
    fig.suptitle('Ley de Cosenos', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "ley_cosenos.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'ley_cosenos.svg'}")
