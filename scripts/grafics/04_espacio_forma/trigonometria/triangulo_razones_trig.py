# yaml_frontmatter:
#   id: 'triangulo_razones_trig'
#   title: 'Razones trigonométricas en triángulo rectángulo: SOH-CAH-TOA'
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

# ============================================================
# Metadatos del Gráfico
# ============================================================


# ============================================================
# Función de Generación
# ============================================================

def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    # Layout con GridSpec: figura a la izquierda, info a la derecha
    fig = plt.figure(figsize=(14, 8), layout='constrained')
    gs = fig.add_gridspec(1, 2, width_ratios=[1.2, 1], wspace=0.08)
    
    ax = fig.add_subplot(gs[0])
    ax_info = fig.add_subplot(gs[1])
    
    # =========================================
    # PANEL IZQUIERDO: Triángulo rectángulo
    # =========================================
    
    # Vértices del triángulo
    A = np.array([0, 0])       # Vértice del ángulo recto
    B = np.array([5, 0])       # Base
    C = np.array([0, 3.5])     # Altura
    
    # Dibujar triángulo
    triangle = plt.Polygon([A, B, C], fill=True, 
                           facecolor=colors['primary'], alpha=0.15,
                           edgecolor=colors['primary'], linewidth=2.5)
    ax.add_patch(triangle)
    
    # Símbolo de ángulo recto
    sq_size = 0.3
    ax.plot([sq_size, sq_size, 0], [0, sq_size, sq_size], 
            color=colors['primary'], linewidth=1.5)
    
    # Etiquetas de vértices
    ax.text(A[0] - 0.3, A[1] - 0.3, 'A', fontsize=14, fontweight='bold')
    ax.text(B[0] + 0.2, B[1] - 0.3, 'B', fontsize=14, fontweight='bold')
    ax.text(C[0] - 0.3, C[1] + 0.2, 'C', fontsize=14, fontweight='bold')
    
    # Etiquetas de lados con colores
    # Hipotenusa (c)
    mid_hyp = (B + C) / 2
    ax.text(mid_hyp[0] + 0.3, mid_hyp[1] + 0.2, 'c', fontsize=16, fontweight='bold',
            color=colors['secondary'],
            bbox=dict(facecolor='white', alpha=0.9, edgecolor='none', boxstyle='round,pad=0.2'))
    ax.text(mid_hyp[0] + 0.8, mid_hyp[1] - 0.3, '(hipotenusa)', fontsize=10,
            color=colors['secondary'], style='italic')
    
    # Cateto opuesto a θ (a)
    mid_opp = (A + C) / 2
    ax.text(mid_opp[0] - 0.5, mid_opp[1], 'a', fontsize=16, fontweight='bold',
            color=colors['accent'],
            bbox=dict(facecolor='white', alpha=0.9, edgecolor='none', boxstyle='round,pad=0.2'))
    ax.text(mid_opp[0] - 1.2, mid_opp[1] - 0.5, '(opuesto)', fontsize=10,
            color=colors['accent'], style='italic')
    
    # Cateto adyacente a θ (b)
    mid_adj = (A + B) / 2
    ax.text(mid_adj[0], mid_adj[1] - 0.5, 'b', fontsize=16, fontweight='bold',
            color=colors['tertiary'],
            bbox=dict(facecolor='white', alpha=0.9, edgecolor='none', boxstyle='round,pad=0.2'))
    ax.text(mid_adj[0] + 0.5, mid_adj[1] - 0.5, '(adyacente)', fontsize=10,
            color=colors['tertiary'], style='italic')
    
    # Arco del ángulo θ en B
    arc_radius = 0.8
    theta_angle = np.arctan2(C[1] - B[1], C[0] - B[0])  # Ángulo hacia C
    base_angle = np.pi  # 180° (hacia A)
    arc_angles = np.linspace(theta_angle, base_angle, 30)
    arc_x = B[0] + arc_radius * np.cos(arc_angles)
    arc_y = B[1] + arc_radius * np.sin(arc_angles)
    ax.plot(arc_x, arc_y, color='#f59e0b', linewidth=2.5)
    
    # Etiqueta del ángulo θ
    mid_arc_angle = (theta_angle + base_angle) / 2
    ax.text(B[0] + 1.1 * arc_radius * np.cos(mid_arc_angle),
            B[1] + 1.1 * arc_radius * np.sin(mid_arc_angle) + 0.1,
            'θ', fontsize=18, fontweight='bold', color='#f59e0b')
    
    # Puntos en vértices
    for p in [A, B, C]:
        ax.plot(p[0], p[1], 'o', color=colors['text'], markersize=6)
    
    ax.set_xlim(-2, 6.5)
    ax.set_ylim(-1.5, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # =========================================
    # PANEL DERECHO: Fórmulas e información
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Título del panel
    ax_info.text(0.5, 0.95, 'RAZONES TRIGONOMÉTRICAS', fontsize=13, fontweight='bold',
                ha='center', va='top', color=colors['text'])
    
    # Caja de fórmula principal
    ax_info.add_patch(plt.Rectangle((0.05, 0.68), 0.9, 0.22, 
                                    facecolor='#fffbeb', edgecolor='#f59e0b',
                                    linewidth=2, transform=ax_info.transAxes))
    
    # Fórmulas principales
    ax_info.text(0.5, 0.85, 'SOH - CAH - TOA', fontsize=14, fontweight='bold',
                ha='center', color='#f59e0b')
    
    formulas = [
        (r'$\sin\theta = \frac{a}{c} = \frac{\text{opuesto}}{\text{hipotenusa}}$', colors['accent']),
        (r'$\cos\theta = \frac{b}{c} = \frac{\text{adyacente}}{\text{hipotenusa}}$', colors['tertiary']),
        (r'$\tan\theta = \frac{a}{b} = \frac{\text{opuesto}}{\text{adyacente}}$', colors['secondary']),
    ]
    
    y_pos = 0.78
    for formula, color in formulas:
        ax_info.text(0.5, y_pos, formula, fontsize=12, ha='center', color=color)
        y_pos -= 0.05
    
    # Separador
    ax_info.axhline(y=0.62, xmin=0.05, xmax=0.95, color='#d1d5db', lw=1.5)
    
    # Razones recíprocas
    ax_info.text(0.5, 0.57, 'Razones Recíprocas', fontsize=11, fontweight='bold',
                ha='center', color=colors['text'])
    
    reciprocas = [
        r'$\csc\theta = \frac{1}{\sin\theta} = \frac{c}{a}$',
        r'$\sec\theta = \frac{1}{\cos\theta} = \frac{c}{b}$',
        r'$\cot\theta = \frac{1}{\tan\theta} = \frac{b}{a}$',
    ]
    
    y_pos = 0.50
    for rec in reciprocas:
        ax_info.text(0.5, y_pos, rec, fontsize=11, ha='center', color='#4b5563')
        y_pos -= 0.06
    
    # Separador
    ax_info.axhline(y=0.30, xmin=0.05, xmax=0.95, color='#d1d5db', lw=1.5)
    
    # Leyenda de colores
    ax_info.text(0.5, 0.25, 'Leyenda', fontsize=11, fontweight='bold',
                ha='center', color=colors['text'])
    
    legend_items = [
        ('a = cateto opuesto', colors['accent']),
        ('b = cateto adyacente', colors['tertiary']),
        ('c = hipotenusa', colors['secondary']),
        ('θ = ángulo agudo', '#f59e0b'),
    ]
    
    y_pos = 0.18
    for label, color in legend_items:
        ax_info.plot([0.12], [y_pos], 's', color=color, markersize=10)
        ax_info.text(0.18, y_pos, label, fontsize=10, va='center', color='#4b5563')
        y_pos -= 0.05
    
    fig.suptitle('Razones Trigonométricas en el Triángulo Rectángulo', 
                fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "triangulo_razones_trig.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'triangulo_razones_trig.svg'}")
