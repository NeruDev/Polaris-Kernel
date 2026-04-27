# yaml_frontmatter:
#   id: 'plano_cartesiano'
#   title: 'Sistema de coordenadas cartesianas con cuadrantes'
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
    
    fig = plt.figure(figsize=(12, 10), layout='constrained')
    gs = fig.add_gridspec(1, 2, width_ratios=[1.3, 1], wspace=0.1)
    
    ax_plane = fig.add_subplot(gs[0])
    ax_info = fig.add_subplot(gs[1])
    
    # =========================================
    # PANEL IZQUIERDO: Plano cartesiano
    # =========================================
    
    # Cuadrícula
    ax_plane.grid(True, linestyle='--', alpha=0.3, color='#9ca3af')
    
    # Ejes principales
    ax_plane.axhline(y=0, color='#374151', linewidth=2)
    ax_plane.axvline(x=0, color='#374151', linewidth=2)
    
    # Flechas de ejes
    ax_plane.annotate('', xy=(6.2, 0), xytext=(6, 0),
                     arrowprops=dict(arrowstyle='->', color='#374151', lw=2))
    ax_plane.annotate('', xy=(0, 6.2), xytext=(0, 6),
                     arrowprops=dict(arrowstyle='->', color='#374151', lw=2))
    
    # Etiquetas de ejes
    ax_plane.text(6.3, 0.3, 'x', fontsize=14, fontweight='bold', color='#374151')
    ax_plane.text(0.3, 6.3, 'y', fontsize=14, fontweight='bold', color='#374151')
    ax_plane.text(-0.5, -0.5, 'O', fontsize=12, fontweight='bold', color='#374151')
    
    # Puntos de ejemplo en cada cuadrante
    points = [
        (3, 4, 'P(3, 4)', colors['secondary'], 'I'),
        (-4, 3, 'Q(-4, 3)', colors['tertiary'], 'II'),
        (-3, -2, 'R(-3, -2)', '#f59e0b', 'III'),
        (4, -3, 'S(4, -3)', '#ec4899', 'IV'),
    ]
    
    for x, y, label, color, quad in points:
        # Punto
        ax_plane.plot(x, y, 'o', color=color, markersize=10, zorder=5)
        # Líneas punteadas a los ejes
        ax_plane.plot([x, x], [0, y], '--', color=color, alpha=0.5, linewidth=1)
        ax_plane.plot([0, x], [y, y], '--', color=color, alpha=0.5, linewidth=1)
        # Etiqueta
        offset_x = 0.3 if x > 0 else -0.3
        offset_y = 0.4
        ha = 'left' if x > 0 else 'right'
        ax_plane.text(x + offset_x, y + offset_y, label, fontsize=10, 
                     fontweight='bold', color=color, ha=ha)
    
    # Etiquetas de cuadrantes
    ax_plane.text(3, 5.2, 'Cuadrante I', fontsize=11, ha='center', 
                 color=colors['secondary'], fontweight='bold',
                 bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
    ax_plane.text(-3, 5.2, 'Cuadrante II', fontsize=11, ha='center',
                 color=colors['tertiary'], fontweight='bold',
                 bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
    ax_plane.text(-3, -5.2, 'Cuadrante III', fontsize=11, ha='center',
                 color='#f59e0b', fontweight='bold',
                 bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
    ax_plane.text(3, -5.2, 'Cuadrante IV', fontsize=11, ha='center',
                 color='#ec4899', fontweight='bold',
                 bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
    
    # Signos en cada cuadrante
    ax_plane.text(4.5, 4.5, '(+, +)', fontsize=10, color='#6b7280', ha='center')
    ax_plane.text(-4.5, 4.5, '(−, +)', fontsize=10, color='#6b7280', ha='center')
    ax_plane.text(-4.5, -4.5, '(−, −)', fontsize=10, color='#6b7280', ha='center')
    ax_plane.text(4.5, -4.5, '(+, −)', fontsize=10, color='#6b7280', ha='center')
    
    ax_plane.set_xlim(-6.5, 6.8)
    ax_plane.set_ylim(-6.5, 6.8)
    ax_plane.set_aspect('equal')
    ax_plane.set_xticks(range(-6, 7))
    ax_plane.set_yticks(range(-6, 7))
    ax_plane.tick_params(labelsize=9)
    ax_plane.spines['top'].set_visible(False)
    ax_plane.spines['right'].set_visible(False)
    ax_plane.spines['bottom'].set_visible(False)
    ax_plane.spines['left'].set_visible(False)
    
    # =========================================
    # PANEL DERECHO: Información
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Definiciones
    ax_info.add_patch(plt.Rectangle((0.03, 0.65), 0.94, 0.32,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=1.5))
    ax_info.text(0.5, 0.92, 'Elementos del Plano Cartesiano', fontsize=11, 
                fontweight='bold', ha='center', color=colors['primary'])
    
    elements = [
        ('Eje x (abscisas):', 'Recta horizontal'),
        ('Eje y (ordenadas):', 'Recta vertical'),
        ('Origen O:', 'Punto de intersección (0, 0)'),
        ('Coordenadas P(x, y):', 'Par ordenado'),
    ]
    y_pos = 0.85
    for name, desc in elements:
        ax_info.text(0.08, y_pos, name, fontsize=9, fontweight='bold', color='#374151')
        ax_info.text(0.45, y_pos, desc, fontsize=9, color='#6b7280')
        y_pos -= 0.055
    
    # Cuadrantes
    ax_info.add_patch(plt.Rectangle((0.03, 0.25), 0.94, 0.36,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=1.5))
    ax_info.text(0.5, 0.56, 'Signos por Cuadrante', fontsize=11,
                fontweight='bold', ha='center', color='#f59e0b')
    
    quad_info = [
        ('I:', '(+, +)', 'x > 0, y > 0', colors['secondary']),
        ('II:', '(−, +)', 'x < 0, y > 0', colors['tertiary']),
        ('III:', '(−, −)', 'x < 0, y < 0', '#f59e0b'),
        ('IV:', '(+, −)', 'x > 0, y < 0', '#ec4899'),
    ]
    y_pos = 0.48
    for quad, signs, cond, color in quad_info:
        ax_info.text(0.1, y_pos, quad, fontsize=10, fontweight='bold', color=color)
        ax_info.text(0.25, y_pos, signs, fontsize=10, color='#374151')
        ax_info.text(0.5, y_pos, cond, fontsize=9, color='#6b7280')
        y_pos -= 0.055
    
    # Abscisa y ordenada
    ax_info.add_patch(plt.Rectangle((0.03, 0.03), 0.94, 0.18,
                                    facecolor='#f0fdf4', edgecolor=colors['accent'],
                                    linewidth=1.5))
    ax_info.text(0.5, 0.17, 'Para un punto P(x, y)', fontsize=10,
                fontweight='bold', ha='center', color=colors['accent'])
    ax_info.text(0.5, 0.1, 'x = abscisa (distancia horizontal)',
                fontsize=9, ha='center', color='#374151')
    ax_info.text(0.5, 0.05, 'y = ordenada (distancia vertical)',
                fontsize=9, ha='center', color='#374151')
    
    fig.suptitle('Sistema de Coordenadas Cartesianas', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "plano_cartesiano.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'plano_cartesiano.svg'}")
