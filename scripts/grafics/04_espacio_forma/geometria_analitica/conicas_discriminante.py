# yaml_frontmatter:
#   id: 'conicas_discriminante'
#   title: 'Clasificación de cónicas mediante el discriminante B²-4AC'
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
    
    fig = plt.figure(figsize=(14, 10), layout='constrained')
    gs = fig.add_gridspec(2, 3, height_ratios=[0.5, 1], hspace=0.25, wspace=0.2)
    
    ax_eq = fig.add_subplot(gs[0, :])
    ax_elipse = fig.add_subplot(gs[1, 0])
    ax_parabola = fig.add_subplot(gs[1, 1])
    ax_hiperbola = fig.add_subplot(gs[1, 2])
    
    # =========================================
    # PANEL SUPERIOR: Ecuación general
    # =========================================
    ax_eq.axis('off')
    ax_eq.set_xlim(0, 1)
    ax_eq.set_ylim(0, 1)
    
    # Ecuación general
    ax_eq.add_patch(plt.Rectangle((0.05, 0.5), 0.9, 0.45,
                                  facecolor='#eff6ff', edgecolor=colors['primary'],
                                  linewidth=2))
    ax_eq.text(0.5, 0.82, 'ECUACIÓN GENERAL DE SEGUNDO GRADO', fontsize=12,
              fontweight='bold', ha='center', color=colors['primary'])
    ax_eq.text(0.5, 0.62, r'$Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$',
              fontsize=14, ha='center', color=colors['text'])
    
    # Discriminante
    ax_eq.add_patch(plt.Rectangle((0.2, 0.05), 0.6, 0.35,
                                  facecolor='#fef3c7', edgecolor='#f59e0b',
                                  linewidth=2))
    ax_eq.text(0.5, 0.32, 'DISCRIMINANTE', fontsize=11,
              fontweight='bold', ha='center', color='#f59e0b')
    ax_eq.text(0.5, 0.17, r'$\Delta = B^2 - 4AC$',
              fontsize=16, ha='center', color=colors['text'])
    
    # =========================================
    # PANEL: Elipse (Delta < 0)
    # =========================================
    ax_elipse.grid(True, linestyle='--', alpha=0.3)
    ax_elipse.axhline(y=0, color='#9ca3af', linewidth=0.8)
    ax_elipse.axvline(x=0, color='#9ca3af', linewidth=0.8)
    
    # Dibujar elipse
    t = np.linspace(0, 2*np.pi, 100)
    a, b = 2, 1.2
    ax_elipse.plot(a*np.cos(t), b*np.sin(t), color=colors['primary'], linewidth=2.5)
    ax_elipse.fill(a*np.cos(t), b*np.sin(t), color=colors['primary'], alpha=0.2)
    
    ax_elipse.set_xlim(-3, 3)
    ax_elipse.set_ylim(-2, 2)
    ax_elipse.set_aspect('equal')
    ax_elipse.set_title('ELIPSE', fontsize=12, fontweight='bold', color=colors['primary'])
    
    # Condición
    ax_elipse.text(0, -1.6, r'$\Delta < 0$', fontsize=14, ha='center',
                  color=colors['primary'], fontweight='bold',
                  bbox=dict(facecolor='#eff6ff', edgecolor=colors['primary'],
                           boxstyle='round,pad=0.3'))
    ax_elipse.text(0, 1.6, r'$B^2 - 4AC < 0$', fontsize=10, ha='center',
                  color='#6b7280')
    
    # Caso especial: circunferencia
    ax_elipse.text(0, -2.4, 'Si A = C y B = 0:', fontsize=9, ha='center',
                  color='#6b7280')
    ax_elipse.text(0, -2.75, 'Circunferencia', fontsize=9, ha='center',
                  color=colors['primary'], fontweight='bold')
    
    # =========================================
    # PANEL: Parábola (Delta = 0)
    # =========================================
    ax_parabola.grid(True, linestyle='--', alpha=0.3)
    ax_parabola.axhline(y=0, color='#9ca3af', linewidth=0.8)
    ax_parabola.axvline(x=0, color='#9ca3af', linewidth=0.8)
    
    # Dibujar parábola
    x = np.linspace(-2, 2, 100)
    y = x**2 / 2
    ax_parabola.plot(x, y - 0.5, color=colors['secondary'], linewidth=2.5)
    ax_parabola.fill_between(x, y - 0.5, color=colors['secondary'], alpha=0.2)
    
    ax_parabola.set_xlim(-3, 3)
    ax_parabola.set_ylim(-2, 2)
    ax_parabola.set_aspect('equal')
    ax_parabola.set_title('PARÁBOLA', fontsize=12, fontweight='bold', color=colors['secondary'])
    
    # Condición
    ax_parabola.text(0, -1.6, r'$\Delta = 0$', fontsize=14, ha='center',
                    color=colors['secondary'], fontweight='bold',
                    bbox=dict(facecolor='#f0fdf4', edgecolor=colors['secondary'],
                             boxstyle='round,pad=0.3'))
    ax_parabola.text(0, 1.6, r'$B^2 - 4AC = 0$', fontsize=10, ha='center',
                    color='#6b7280')
    
    # Caso especial
    ax_parabola.text(0, -2.4, 'Sólo un término', fontsize=9, ha='center',
                    color='#6b7280')
    ax_parabola.text(0, -2.75, 'cuadrático en x o en y', fontsize=9, ha='center',
                    color='#6b7280')
    
    # =========================================
    # PANEL: Hipérbola (Delta > 0)
    # =========================================
    ax_hiperbola.grid(True, linestyle='--', alpha=0.3)
    ax_hiperbola.axhline(y=0, color='#9ca3af', linewidth=0.8)
    ax_hiperbola.axvline(x=0, color='#9ca3af', linewidth=0.8)
    
    # Dibujar hipérbola
    t = np.linspace(-1.5, 1.5, 100)
    a, b = 1, 0.8
    x_r = a * np.cosh(t)
    y_r = b * np.sinh(t)
    ax_hiperbola.plot(x_r, y_r, color='#dc2626', linewidth=2.5)
    ax_hiperbola.plot(-x_r, y_r, color='#dc2626', linewidth=2.5)
    
    # Asíntotas
    x_as = np.linspace(-2.8, 2.8, 50)
    ax_hiperbola.plot(x_as, (b/a)*x_as, '--', color='#dc2626', linewidth=1, alpha=0.5)
    ax_hiperbola.plot(x_as, -(b/a)*x_as, '--', color='#dc2626', linewidth=1, alpha=0.5)
    
    ax_hiperbola.set_xlim(-3, 3)
    ax_hiperbola.set_ylim(-2, 2)
    ax_hiperbola.set_aspect('equal')
    ax_hiperbola.set_title('HIPÉRBOLA', fontsize=12, fontweight='bold', color='#dc2626')
    
    # Condición
    ax_hiperbola.text(0, -1.6, r'$\Delta > 0$', fontsize=14, ha='center',
                     color='#dc2626', fontweight='bold',
                     bbox=dict(facecolor='#fef2f2', edgecolor='#dc2626',
                              boxstyle='round,pad=0.3'))
    ax_hiperbola.text(0, 1.6, r'$B^2 - 4AC > 0$', fontsize=10, ha='center',
                     color='#6b7280')
    
    # Caso especial
    ax_hiperbola.text(0, -2.4, 'Incluye rectas', fontsize=9, ha='center',
                     color='#6b7280')
    ax_hiperbola.text(0, -2.75, 'cruzadas si es degenerada', fontsize=9, ha='center',
                     color='#6b7280')
    
    fig.suptitle('Clasificación de Cónicas por el Discriminante', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "conicas_discriminante.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'conicas_discriminante.svg'}")
