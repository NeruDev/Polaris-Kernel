# yaml_frontmatter:
#   id: 'pendiente_recta'
#   title: 'Pendiente y ecuaciones de la línea recta'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria_analitica']

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
    
    fig = plt.figure(figsize=(14, 9), layout='constrained')
    gs = fig.add_gridspec(2, 2, height_ratios=[1.2, 1], hspace=0.2, wspace=0.15)
    
    ax_slope = fig.add_subplot(gs[0, 0])
    ax_types = fig.add_subplot(gs[0, 1])
    ax_formulas = fig.add_subplot(gs[1, :])
    
    # =========================================
    # PANEL 1: Concepto de pendiente
    # =========================================
    ax_slope.grid(True, linestyle='--', alpha=0.3)
    ax_slope.axhline(y=0, color='#9ca3af', linewidth=1)
    ax_slope.axvline(x=0, color='#9ca3af', linewidth=1)
    
    # Puntos y recta
    P1 = np.array([1, 1])
    P2 = np.array([5, 4])
    
    # Extender la recta
    x_line = np.linspace(-1, 7, 100)
    m = (P2[1] - P1[1]) / (P2[0] - P1[0])
    b = P1[1] - m * P1[0]
    y_line = m * x_line + b
    
    ax_slope.plot(x_line, y_line, color=colors['primary'], linewidth=2.5)
    
    # Triángulo de pendiente
    ax_slope.plot([P1[0], P2[0]], [P1[1], P1[1]], '--', color=colors['tertiary'], 
                 linewidth=2, label=r'$\Delta x$ (carrera)')
    ax_slope.plot([P2[0], P2[0]], [P1[1], P2[1]], '--', color=colors['secondary'],
                 linewidth=2, label=r'$\Delta y$ (elevación)')
    
    # Puntos
    ax_slope.plot(*P1, 'o', color=colors['primary'], markersize=10, zorder=5)
    ax_slope.plot(*P2, 'o', color=colors['primary'], markersize=10, zorder=5)
    
    ax_slope.text(P1[0] - 0.3, P1[1] - 0.5, r'$P_1(x_1, y_1)$', fontsize=10,
                 color=colors['primary'])
    ax_slope.text(P2[0] + 0.2, P2[1] + 0.2, r'$P_2(x_2, y_2)$', fontsize=10,
                 color=colors['primary'])
    
    # Etiquetas delta
    ax_slope.text((P1[0]+P2[0])/2, P1[1]-0.4, r'$\Delta x = x_2 - x_1$', 
                 fontsize=9, ha='center', color=colors['tertiary'])
    ax_slope.text(P2[0]+0.3, (P1[1]+P2[1])/2, r'$\Delta y$', fontsize=9,
                 color=colors['secondary'])
    
    # Ángulo theta
    theta = np.arctan(m)
    arc = np.linspace(0, theta, 30)
    r_arc = 1.2
    ax_slope.plot(P1[0] + r_arc*np.cos(arc), P1[1] + r_arc*np.sin(arc),
                 color='#f59e0b', linewidth=2)
    ax_slope.text(P1[0] + 1.5, P1[1] + 0.3, r'$\theta$', fontsize=12, 
                 color='#f59e0b', fontweight='bold')
    
    # Fórmula de pendiente
    ax_slope.text(0.5, 5, r'$m = \frac{\Delta y}{\Delta x} = \frac{y_2-y_1}{x_2-x_1} = \tan\theta$',
                 fontsize=12, color=colors['text'],
                 bbox=dict(facecolor='white', edgecolor=colors['primary'], boxstyle='round,pad=0.3'))
    
    ax_slope.set_xlim(-1, 7)
    ax_slope.set_ylim(-1, 6)
    ax_slope.set_aspect('equal')
    ax_slope.set_title('Concepto de Pendiente', fontsize=11, fontweight='bold')
    ax_slope.legend(loc='lower right', fontsize=8)
    
    # =========================================
    # PANEL 2: Tipos de pendiente
    # =========================================
    ax_types.axhline(y=0, color='#9ca3af', linewidth=1)
    ax_types.axvline(x=0, color='#9ca3af', linewidth=1)
    
    x = np.linspace(-3, 3, 50)
    
    # m > 0 (ascendente)
    ax_types.plot(x, 0.8*x + 2, color=colors['secondary'], linewidth=2.5,
                 label='m > 0 (ascendente)')
    
    # m < 0 (descendente)
    ax_types.plot(x, -0.6*x - 1, color=colors['tertiary'], linewidth=2.5,
                 label='m < 0 (descendente)')
    
    # m = 0 (horizontal)
    ax_types.axhline(y=1, color='#f59e0b', linewidth=2.5, label='m = 0 (horizontal)')
    
    # Vertical (m indefinida)
    ax_types.axvline(x=2, color='#ec4899', linewidth=2.5, label='m = ∄ (vertical)')
    
    ax_types.set_xlim(-3.5, 3.5)
    ax_types.set_ylim(-3.5, 4.5)
    ax_types.set_aspect('equal')
    ax_types.set_title('Tipos de Pendiente', fontsize=11, fontweight='bold')
    ax_types.legend(loc='upper left', fontsize=8)
    ax_types.grid(True, linestyle='--', alpha=0.3)
    
    # =========================================
    # PANEL INFERIOR: Formas de la ecuación
    # =========================================
    ax_formulas.axis('off')
    ax_formulas.set_xlim(0, 1)
    ax_formulas.set_ylim(0, 1)
    
    # Título
    ax_formulas.text(0.5, 0.95, 'FORMAS DE LA ECUACIÓN DE LA RECTA', fontsize=12,
                    fontweight='bold', ha='center', color=colors['primary'])
    
    forms = [
        ('Punto-Pendiente', r'$y - y_1 = m(x - x_1)$', 'Conocidos un punto y m', 
         '#f0fdf4', colors['secondary']),
        ('Pendiente-Ordenada', r'$y = mx + b$', 'Conocidos m y ordenada b',
         '#eff6ff', colors['tertiary']),
        ('Forma Simétrica', r'$\frac{x}{a} + \frac{y}{b} = 1$', 'Intersecciones con ejes',
         '#fef3c7', '#f59e0b'),
        ('Forma General', r'$Ax + By + C = 0$', 'Forma estándar',
         '#fce7f3', '#ec4899'),
    ]
    
    x_positions = [0.13, 0.38, 0.63, 0.88]
    
    for i, (name, formula, desc, bg_color, border_color) in enumerate(forms):
        x_pos = x_positions[i]
        
        ax_formulas.add_patch(plt.Rectangle((x_pos - 0.11, 0.4), 0.22, 0.48,
                                            facecolor=bg_color, edgecolor=border_color,
                                            linewidth=1.5))
        
        ax_formulas.text(x_pos, 0.82, name, fontsize=9, fontweight='bold',
                        ha='center', color=border_color)
        ax_formulas.text(x_pos, 0.65, formula, fontsize=10, ha='center',
                        color=colors['text'])
        ax_formulas.text(x_pos, 0.48, desc, fontsize=8, ha='center',
                        color='#6b7280', style='italic')
    
    # Relaciones paralelas y perpendiculares
    ax_formulas.add_patch(plt.Rectangle((0.02, 0.05), 0.46, 0.28,
                                        facecolor='#f9fafb', edgecolor='#6b7280',
                                        linewidth=1.5))
    ax_formulas.text(0.25, 0.28, 'Rectas Paralelas y Perpendiculares', fontsize=10,
                    fontweight='bold', ha='center', color='#374151')
    ax_formulas.text(0.25, 0.18, r'Paralelas: $m_1 = m_2$', fontsize=10, ha='center')
    ax_formulas.text(0.25, 0.1, r'Perpendiculares: $m_1 \cdot m_2 = -1$', fontsize=10, ha='center')
    
    # Distancia punto-recta
    ax_formulas.add_patch(plt.Rectangle((0.52, 0.05), 0.46, 0.28,
                                        facecolor='#fef2f2', edgecolor='#dc2626',
                                        linewidth=1.5))
    ax_formulas.text(0.75, 0.28, 'Distancia de Punto a Recta', fontsize=10,
                    fontweight='bold', ha='center', color='#dc2626')
    ax_formulas.text(0.75, 0.15, r'$d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}$',
                    fontsize=11, ha='center', color=colors['text'])
    
    fig.suptitle('La Línea Recta', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "pendiente_recta.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'pendiente_recta.svg'}")
