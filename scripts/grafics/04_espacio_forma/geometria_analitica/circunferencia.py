# yaml_frontmatter:
#   id: 'circunferencia'
#   title: 'La circunferencia: elementos y ecuaciones'
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
    
    fig = plt.figure(figsize=(14, 8), layout='constrained')
    gs = fig.add_gridspec(1, 2, width_ratios=[1.2, 1], wspace=0.1)
    
    ax_circle = fig.add_subplot(gs[0])
    ax_info = fig.add_subplot(gs[1])
    
    # =========================================
    # PANEL IZQUIERDO: Circunferencia
    # =========================================
    ax_circle.grid(True, linestyle='--', alpha=0.3)
    ax_circle.axhline(y=0, color='#9ca3af', linewidth=1)
    ax_circle.axvline(x=0, color='#9ca3af', linewidth=1)
    
    # Centro y radio
    h, k = 3, 2
    r = 2.5
    
    # Dibujar circunferencia
    theta = np.linspace(0, 2*np.pi, 100)
    x_circ = h + r * np.cos(theta)
    y_circ = k + r * np.sin(theta)
    ax_circle.plot(x_circ, y_circ, color=colors['primary'], linewidth=2.5)
    ax_circle.fill(x_circ, y_circ, color=colors['primary'], alpha=0.1)
    
    # Centro
    ax_circle.plot(h, k, 'o', color=colors['primary'], markersize=10, zorder=5)
    ax_circle.text(h + 0.2, k + 0.3, 'C(h, k)', fontsize=11, fontweight='bold',
                  color=colors['primary'])
    
    # Radio
    angle_r = np.radians(35)
    Pr = np.array([h + r*np.cos(angle_r), k + r*np.sin(angle_r)])
    ax_circle.plot([h, Pr[0]], [k, Pr[1]], color='#f59e0b', linewidth=2.5)
    ax_circle.text(h + r/2*np.cos(angle_r) - 0.2, k + r/2*np.sin(angle_r) + 0.3, 
                  'r', fontsize=14, fontweight='bold', color='#f59e0b')
    
    # Punto P sobre la circunferencia
    ax_circle.plot(*Pr, 'o', color=colors['secondary'], markersize=8, zorder=5)
    ax_circle.text(Pr[0] + 0.2, Pr[1] + 0.2, 'P(x, y)', fontsize=10,
                  color=colors['secondary'])
    
    # Diámetro
    ax_circle.plot([h-r, h+r], [k, k], '--', color=colors['tertiary'], linewidth=2)
    ax_circle.text(h + r + 0.2, k, 'd = 2r', fontsize=10, color=colors['tertiary'])
    
    # Punto interior
    ax_circle.plot(h + 0.8, k - 0.5, 's', color=colors['accent'], markersize=8)
    ax_circle.text(h + 1, k - 0.7, 'interior', fontsize=9, color=colors['accent'])
    
    # Punto exterior
    ax_circle.plot(h - 1, k + 3.5, '^', color='#dc2626', markersize=8)
    ax_circle.text(h - 0.8, k + 3.7, 'exterior', fontsize=9, color='#dc2626')
    
    # Ecuación
    ax_circle.text(0.5, 5.5, r'$(x-h)^2 + (y-k)^2 = r^2$', fontsize=12,
                  color=colors['text'],
                  bbox=dict(facecolor='white', edgecolor=colors['primary'], 
                           boxstyle='round,pad=0.4'))
    
    ax_circle.set_xlim(-1, 7)
    ax_circle.set_ylim(-1.5, 6)
    ax_circle.set_aspect('equal')
    ax_circle.set_xlabel('x', fontsize=11)
    ax_circle.set_ylabel('y', fontsize=11)
    ax_circle.set_title('Circunferencia con Centro C(h, k) y Radio r', 
                       fontsize=11, fontweight='bold')
    
    # =========================================
    # PANEL DERECHO: Información
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Ecuación canónica
    ax_info.add_patch(plt.Rectangle((0.03, 0.72), 0.94, 0.25,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=2))
    ax_info.text(0.5, 0.92, 'ECUACIÓN CANÓNICA', fontsize=11,
                fontweight='bold', ha='center', color='#f59e0b')
    ax_info.text(0.5, 0.82, r'$(x - h)^2 + (y - k)^2 = r^2$',
                fontsize=13, ha='center', color=colors['text'])
    ax_info.text(0.5, 0.74, 'Centro (h, k) y radio r',
                fontsize=9, ha='center', color='#6b7280')
    
    # Ecuación general
    ax_info.add_patch(plt.Rectangle((0.03, 0.45), 0.94, 0.24,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=1.5))
    ax_info.text(0.5, 0.64, 'ECUACIÓN GENERAL', fontsize=11,
                fontweight='bold', ha='center', color=colors['primary'])
    ax_info.text(0.5, 0.55, r'$x^2 + y^2 + Dx + Ey + F = 0$',
                fontsize=12, ha='center', color=colors['text'])
    ax_info.text(0.5, 0.47, r'Centro: $(-D/2, -E/2)$  •  Radio: $r = \sqrt{\frac{D^2+E^2}{4}-F}$',
                fontsize=9, ha='center', color='#6b7280')
    
    # Posiciones relativas
    ax_info.add_patch(plt.Rectangle((0.03, 0.15), 0.94, 0.27,
                                    facecolor='#f0fdf4', edgecolor=colors['accent'],
                                    linewidth=1.5))
    ax_info.text(0.5, 0.38, 'Posición de un Punto P respecto al Centro', 
                fontsize=10, fontweight='bold', ha='center', color=colors['accent'])
    
    positions = [
        ('d < r', 'Punto interior', colors['accent']),
        ('d = r', 'Punto sobre la circunferencia', colors['secondary']),
        ('d > r', 'Punto exterior', '#dc2626'),
    ]
    y_pos = 0.31
    for cond, desc, color in positions:
        ax_info.text(0.15, y_pos, cond, fontsize=10, fontweight='bold', color=color)
        ax_info.text(0.35, y_pos, '→', fontsize=10, color='#6b7280')
        ax_info.text(0.45, y_pos, desc, fontsize=10, color='#374151')
        y_pos -= 0.06
    
    # Nota
    ax_info.text(0.5, 0.08, 'd = distancia del punto P al centro C',
                fontsize=9, ha='center', color='#9ca3af', style='italic')
    
    fig.suptitle('La Circunferencia', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "circunferencia.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'circunferencia.svg'}")
