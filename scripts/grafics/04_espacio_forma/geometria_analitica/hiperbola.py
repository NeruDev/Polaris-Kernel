# yaml_frontmatter:
#   id: 'hiperbola'
#   title: 'La hipérbola: elementos, ecuaciones y asíntotas'
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
    gs = fig.add_gridspec(2, 2, height_ratios=[1.3, 1], hspace=0.2, wspace=0.15)
    
    ax_main = fig.add_subplot(gs[0, :])
    ax_formulas = fig.add_subplot(gs[1, 0])
    ax_props = fig.add_subplot(gs[1, 1])
    
    # =========================================
    # PANEL PRINCIPAL: Hipérbola con elementos
    # =========================================
    ax_main.grid(True, linestyle='--', alpha=0.3)
    ax_main.axhline(y=0, color='#9ca3af', linewidth=1)
    ax_main.axvline(x=0, color='#9ca3af', linewidth=1)
    
    # Parámetros
    a = 2  # semieje transverso
    b = 1.5  # semieje conjugado
    c = np.sqrt(a**2 + b**2)  # distancia focal
    
    # Dibujar hipérbola (rama derecha e izquierda)
    # x²/a² - y²/b² = 1  =>  x = ±a*cosh(t), y = b*sinh(t)
    t = np.linspace(-2, 2, 200)
    
    # Rama derecha
    x_r = a * np.cosh(t)
    y_r = b * np.sinh(t)
    ax_main.plot(x_r, y_r, color=colors['primary'], linewidth=2.5)
    
    # Rama izquierda
    ax_main.plot(-x_r, y_r, color=colors['primary'], linewidth=2.5)
    
    # Asíntotas
    x_asym = np.linspace(-5, 5, 100)
    ax_main.plot(x_asym, (b/a)*x_asym, '--', color='#dc2626', linewidth=2,
                label=r'Asíntotas: $y = \pm\frac{b}{a}x$')
    ax_main.plot(x_asym, -(b/a)*x_asym, '--', color='#dc2626', linewidth=2)
    
    # Centro
    ax_main.plot(0, 0, 'o', color=colors['primary'], markersize=8, zorder=5)
    ax_main.text(0.2, 0.3, 'C', fontsize=11, fontweight='bold', color=colors['primary'])
    
    # Focos
    ax_main.plot(c, 0, '*', color='#f59e0b', markersize=15, zorder=5)
    ax_main.plot(-c, 0, '*', color='#f59e0b', markersize=15, zorder=5)
    ax_main.text(c + 0.2, 0.3, r'$F_2$', fontsize=11, color='#f59e0b')
    ax_main.text(-c - 0.5, 0.3, r'$F_1$', fontsize=11, color='#f59e0b')
    
    # Vértices
    ax_main.plot(a, 0, 'o', color=colors['secondary'], markersize=8, zorder=5)
    ax_main.plot(-a, 0, 'o', color=colors['secondary'], markersize=8, zorder=5)
    ax_main.text(a + 0.2, -0.5, r'$V_2$', fontsize=10, color=colors['secondary'])
    ax_main.text(-a - 0.5, -0.5, r'$V_1$', fontsize=10, color=colors['secondary'])
    
    # Semiejes
    ax_main.plot([0, a], [0, 0], color=colors['secondary'], linewidth=2.5)
    ax_main.text(a/2, -0.6, 'a', fontsize=14, fontweight='bold', ha='center',
                color=colors['secondary'])
    
    # Rectángulo auxiliar
    rect_x = [-a, a, a, -a, -a]
    rect_y = [-b, -b, b, b, -b]
    ax_main.plot(rect_x, rect_y, ':', color='#9ca3af', linewidth=1.5)
    ax_main.plot([0, 0], [0, b], color=colors['tertiary'], linewidth=2.5)
    ax_main.text(0.2, b/2, 'b', fontsize=14, fontweight='bold', color=colors['tertiary'])
    
    # Punto P y distancias (definición)
    Px = a * np.cosh(0.8)
    Py = b * np.sinh(0.8)
    ax_main.plot(Px, Py, 'o', color=colors['accent'], markersize=10, zorder=5)
    ax_main.text(Px + 0.2, Py + 0.2, 'P', fontsize=11, fontweight='bold',
                color=colors['accent'])
    
    # Líneas a los focos
    ax_main.plot([Px, -c], [Py, 0], ':', color=colors['accent'], linewidth=1.5, alpha=0.7)
    ax_main.plot([Px, c], [Py, 0], ':', color=colors['accent'], linewidth=1.5, alpha=0.7)
    
    ax_main.set_xlim(-5, 5)
    ax_main.set_ylim(-3.5, 3.5)
    ax_main.set_aspect('equal')
    ax_main.set_title('Hipérbola con Eje Transverso Horizontal', fontsize=11, fontweight='bold')
    ax_main.legend(loc='upper right', fontsize=9)
    
    # Definición
    ax_main.text(0, -3, r'$|d_1 - d_2| = 2a$ (definición de hipérbola)', fontsize=11,
                ha='center', color=colors['text'],
                bbox=dict(facecolor='white', edgecolor=colors['primary'],
                         boxstyle='round,pad=0.3'))
    
    # =========================================
    # PANEL INFERIOR IZQUIERDO: Ecuaciones
    # =========================================
    ax_formulas.axis('off')
    ax_formulas.set_xlim(0, 1)
    ax_formulas.set_ylim(0, 1)
    
    ax_formulas.text(0.5, 0.95, 'ECUACIONES CANÓNICAS', fontsize=11,
                    fontweight='bold', ha='center', color=colors['primary'])
    
    # Eje transverso horizontal
    ax_formulas.add_patch(plt.Rectangle((0.03, 0.55), 0.94, 0.35,
                                        facecolor='#eff6ff', edgecolor=colors['secondary'],
                                        linewidth=1.5))
    ax_formulas.text(0.5, 0.84, 'Eje transverso horizontal', fontsize=10,
                    fontweight='bold', ha='center', color=colors['secondary'])
    ax_formulas.text(0.5, 0.72, r'$\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$',
                    fontsize=13, ha='center', color=colors['text'])
    ax_formulas.text(0.5, 0.6, r'Asíntotas: $y = \pm\frac{b}{a}x$',
                    fontsize=10, ha='center', color='#6b7280')
    
    # Eje transverso vertical
    ax_formulas.add_patch(plt.Rectangle((0.03, 0.12), 0.94, 0.38,
                                        facecolor='#f0fdf4', edgecolor=colors['tertiary'],
                                        linewidth=1.5))
    ax_formulas.text(0.5, 0.44, 'Eje transverso vertical', fontsize=10,
                    fontweight='bold', ha='center', color=colors['tertiary'])
    ax_formulas.text(0.5, 0.32, r'$\frac{y^2}{a^2} - \frac{x^2}{b^2} = 1$',
                    fontsize=13, ha='center', color=colors['text'])
    ax_formulas.text(0.5, 0.2, r'Asíntotas: $y = \pm\frac{a}{b}x$',
                    fontsize=10, ha='center', color='#6b7280')
    
    # =========================================
    # PANEL INFERIOR DERECHO: Propiedades
    # =========================================
    ax_props.axis('off')
    ax_props.set_xlim(0, 1)
    ax_props.set_ylim(0, 1)
    
    ax_props.text(0.5, 0.95, 'RELACIONES Y PROPIEDADES', fontsize=11,
                 fontweight='bold', ha='center', color='#f59e0b')
    
    # Relación fundamental
    ax_props.add_patch(plt.Rectangle((0.03, 0.65), 0.94, 0.25,
                                     facecolor='#fef3c7', edgecolor='#f59e0b',
                                     linewidth=2))
    ax_props.text(0.5, 0.84, 'Relación Fundamental', fontsize=10,
                 fontweight='bold', ha='center', color='#f59e0b')
    ax_props.text(0.5, 0.72, r'$c^2 = a^2 + b^2$',
                 fontsize=13, ha='center', color=colors['text'])
    
    # Excentricidad
    ax_props.add_patch(plt.Rectangle((0.03, 0.3), 0.94, 0.3,
                                     facecolor='#fce7f3', edgecolor='#ec4899',
                                     linewidth=1.5))
    ax_props.text(0.5, 0.54, 'Excentricidad', fontsize=10,
                 fontweight='bold', ha='center', color='#ec4899')
    ax_props.text(0.5, 0.44, r'$e = \frac{c}{a} = \sqrt{1 + \frac{b^2}{a^2}}$',
                 fontsize=12, ha='center', color=colors['text'])
    ax_props.text(0.5, 0.34, r'$e > 1$ (hipérbola)',
                 fontsize=10, ha='center', color='#6b7280')
    
    # Hipérbola equilátera
    ax_props.text(0.5, 0.2, 'Hipérbola equilátera (a = b):', fontsize=9, 
                 fontweight='bold', ha='center', color='#374151')
    ax_props.text(0.5, 0.12, r'$x^2 - y^2 = a^2$',
                 fontsize=10, ha='center', color='#6b7280')
    ax_props.text(0.5, 0.05, r'Asíntotas: $y = \pm x$  •  $e = \sqrt{2}$',
                 fontsize=9, ha='center', color='#6b7280')
    
    fig.suptitle('La Hipérbola', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "hiperbola.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'hiperbola.svg'}")
