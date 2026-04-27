# yaml_frontmatter:
#   id: 'ley_senos'
#   title: 'Ley de senos para resolución de triángulos oblicuángulos'
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

import matplotlib.patches as patches

    setup_style,
    get_colors,
    get_output_dir_for_topic,
    save_figure,
)


def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig = plt.figure(figsize=(14, 8), layout='constrained')
    gs = fig.add_gridspec(1, 2, width_ratios=[1.3, 1], wspace=0.08)
    
    ax_triangle = fig.add_subplot(gs[0])
    ax_info = fig.add_subplot(gs[1])
    
    # =========================================
    # PANEL IZQUIERDO: Triángulo
    # =========================================
    
    # Definir vértices del triángulo (oblicuángulo)
    A = np.array([1, 0])
    B = np.array([5, 0])
    C = np.array([2.5, 3.5])
    
    # Calcular lados
    a = np.linalg.norm(B - C)  # lado opuesto a A
    b = np.linalg.norm(A - C)  # lado opuesto a B
    c = np.linalg.norm(A - B)  # lado opuesto a C
    
    # Dibujar triángulo
    triangle = plt.Polygon([A, B, C], fill=True, facecolor='#eff6ff', 
                           edgecolor=colors['primary'], linewidth=2.5)
    ax_triangle.add_patch(triangle)
    
    # Lados con colores
    ax_triangle.plot([B[0], C[0]], [B[1], C[1]], color=colors['secondary'], linewidth=3, 
                    label='a (opuesto a A)')
    ax_triangle.plot([A[0], C[0]], [A[1], C[1]], color=colors['tertiary'], linewidth=3,
                    label='b (opuesto a B)')
    ax_triangle.plot([A[0], B[0]], [A[1], B[1]], color='#f59e0b', linewidth=3,
                    label='c (opuesto a C)')
    
    # Vértices
    for point, label, offset in [(A, 'A', (-0.25, -0.35)), 
                                  (B, 'B', (0.15, -0.35)), 
                                  (C, 'C', (0, 0.2))]:
        ax_triangle.plot(point[0], point[1], 'o', color=colors['primary'], markersize=10, zorder=5)
        ax_triangle.text(point[0] + offset[0], point[1] + offset[1], label,
                        fontsize=14, fontweight='bold', color=colors['primary'])
    
    # Etiquetas de lados
    mid_a = (B + C) / 2
    mid_b = (A + C) / 2
    mid_c = (A + B) / 2
    
    ax_triangle.text(mid_a[0] + 0.25, mid_a[1], 'a', fontsize=14, fontweight='bold',
                    color=colors['secondary'])
    ax_triangle.text(mid_b[0] - 0.35, mid_b[1], 'b', fontsize=14, fontweight='bold',
                    color=colors['tertiary'])
    ax_triangle.text(mid_c[0], mid_c[1] - 0.35, 'c', fontsize=14, fontweight='bold',
                    color='#f59e0b')
    
    # Arcos de ángulos
    def draw_angle_arc(ax, vertex, p1, p2, radius=0.4, color='#6b7280'):
                v1 = p1 - vertex
        v2 = p2 - vertex
        angle1 = np.arctan2(v1[1], v1[0])
        angle2 = np.arctan2(v2[1], v2[0])
        if angle1 > angle2:
            angle1, angle2 = angle2, angle1
        angles = np.linspace(angle1, angle2, 30)
        ax.plot(vertex[0] + radius*np.cos(angles), vertex[1] + radius*np.sin(angles),
               color=color, linewidth=2)
    
    draw_angle_arc(ax_triangle, A, B, C, radius=0.5, color=colors['secondary'])
    draw_angle_arc(ax_triangle, B, A, C, radius=0.45, color=colors['tertiary'])
    draw_angle_arc(ax_triangle, C, A, B, radius=0.35, color='#f59e0b')
    
    # Etiquetas de ángulos
    ax_triangle.text(A[0] + 0.6, A[1] + 0.25, 'A', fontsize=12, color=colors['secondary'],
                    fontweight='bold')
    ax_triangle.text(B[0] - 0.65, B[1] + 0.22, 'B', fontsize=12, color=colors['tertiary'],
                    fontweight='bold')
    ax_triangle.text(C[0] + 0.1, C[1] - 0.55, 'C', fontsize=12, color='#f59e0b',
                    fontweight='bold')
    
    # Circunferencia circunscrita (opcional, muestra el radio R)
    # Calcular circuncentro y radio
    D = 2 * (A[0]*(B[1]-C[1]) + B[0]*(C[1]-A[1]) + C[0]*(A[1]-B[1]))
    ux = ((A[0]**2 + A[1]**2)*(B[1]-C[1]) + (B[0]**2 + B[1]**2)*(C[1]-A[1]) + 
          (C[0]**2 + C[1]**2)*(A[1]-B[1])) / D
    uy = ((A[0]**2 + A[1]**2)*(C[0]-B[0]) + (B[0]**2 + B[1]**2)*(A[0]-C[0]) + 
          (C[0]**2 + C[1]**2)*(B[0]-A[0])) / D
    center = np.array([ux, uy])
    R = np.linalg.norm(A - center)
    
    circle_angles = np.linspace(0, 2*np.pi, 100)
    ax_triangle.plot(center[0] + R*np.cos(circle_angles), 
                    center[1] + R*np.sin(circle_angles),
                    '--', color='#d1d5db', linewidth=1.5, alpha=0.7)
    
    # Radio
    ax_triangle.plot([center[0], C[0]], [center[1], C[1]], ':', color='#9ca3af', linewidth=1.5)
    ax_triangle.text((center[0] + C[0])/2 + 0.1, (center[1] + C[1])/2 + 0.15, 'R',
                    fontsize=10, color='#9ca3af', style='italic')
    
    ax_triangle.set_xlim(0, 6)
    ax_triangle.set_ylim(-0.8, 4.5)
    ax_triangle.set_aspect('equal')
    ax_triangle.axis('off')
    ax_triangle.set_title('Triángulo con Circunferencia Circunscrita', fontsize=11, 
                         fontweight='bold')
    
    # =========================================
    # PANEL DERECHO: Fórmulas
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Ley de senos principal
    ax_info.add_patch(plt.Rectangle((0.03, 0.72), 0.94, 0.24,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=2))
    ax_info.text(0.5, 0.9, 'LEY DE SENOS', fontsize=12, fontweight='bold',
                ha='center', color='#f59e0b')
    
    ax_info.text(0.5, 0.78, r'$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$',
                fontsize=14, ha='center', color=colors['text'])
    
    # Forma alternativa
    ax_info.add_patch(plt.Rectangle((0.03, 0.5), 0.94, 0.18,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=1.5))
    ax_info.text(0.5, 0.63, 'Forma equivalente', fontsize=10, fontweight='bold',
                ha='center', color=colors['primary'])
    ax_info.text(0.5, 0.54, r'$\frac{\sin A}{a} = \frac{\sin B}{b} = \frac{\sin C}{c}$',
                fontsize=12, ha='center', color=colors['text'])
    
    # Aplicación
    ax_info.add_patch(plt.Rectangle((0.03, 0.1), 0.94, 0.36,
                                    facecolor='#f0fdf4', edgecolor=colors['accent'],
                                    linewidth=1.5))
    ax_info.text(0.5, 0.41, 'Casos de Aplicación', fontsize=10, fontweight='bold',
                ha='center', color=colors['accent'])
    
    casos = [
        '• ALA: Dos ángulos y un lado',
        '• LAA: Un lado y dos ángulos',
        '• LLA: Dos lados y ángulo opuesto',
        '  (caso ambiguo)',
    ]
    y_pos = 0.34
    for caso in casos:
        ax_info.text(0.08, y_pos, caso, fontsize=9, color='#374151')
        y_pos -= 0.065
    
    # Nota sobre R
    ax_info.text(0.5, 0.03, 'R = radio de la circunferencia circunscrita',
                fontsize=9, ha='center', color='#6b7280', style='italic')
    
    fig.suptitle('Ley de Senos', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "ley_senos.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'ley_senos.svg'}")
