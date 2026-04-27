# yaml_frontmatter:
#   id: 'elipse'
#   title: 'La elipse: elementos, ecuaciones y propiedades'
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
    # PANEL PRINCIPAL: Elipse con elementos
    # =========================================
    ax_main.grid(True, linestyle='--', alpha=0.3)
    ax_main.axhline(y=0, color='#9ca3af', linewidth=1)
    ax_main.axvline(x=0, color='#9ca3af', linewidth=1)
    
    # Parámetros
    a = 4  # semieje mayor
    b = 2.5  # semieje menor
    c = np.sqrt(a**2 - b**2)  # distancia focal
    
    # Dibujar elipse
    theta = np.linspace(0, 2*np.pi, 200)
    x_ell = a * np.cos(theta)
    y_ell = b * np.sin(theta)
    ax_main.plot(x_ell, y_ell, color=colors['primary'], linewidth=2.5)
    ax_main.fill(x_ell, y_ell, color=colors['primary'], alpha=0.1)
    
    # Centro
    ax_main.plot(0, 0, 'o', color=colors['primary'], markersize=8, zorder=5)
    ax_main.text(0.2, 0.3, 'C', fontsize=11, fontweight='bold', color=colors['primary'])
    
    # Focos
    ax_main.plot(c, 0, '*', color='#f59e0b', markersize=15, zorder=5)
    ax_main.plot(-c, 0, '*', color='#f59e0b', markersize=15, zorder=5)
    ax_main.text(c + 0.2, 0.3, r'$F_2$', fontsize=11, color='#f59e0b')
    ax_main.text(-c - 0.5, 0.3, r'$F_1$', fontsize=11, color='#f59e0b')
    
    # Vértices del eje mayor
    ax_main.plot(a, 0, 'o', color=colors['secondary'], markersize=8, zorder=5)
    ax_main.plot(-a, 0, 'o', color=colors['secondary'], markersize=8, zorder=5)
    ax_main.text(a + 0.2, -0.4, r'$V_2$', fontsize=10, color=colors['secondary'])
    ax_main.text(-a - 0.5, -0.4, r'$V_1$', fontsize=10, color=colors['secondary'])
    
    # Vértices del eje menor
    ax_main.plot(0, b, 'o', color=colors['tertiary'], markersize=8, zorder=5)
    ax_main.plot(0, -b, 'o', color=colors['tertiary'], markersize=8, zorder=5)
    ax_main.text(0.2, b + 0.2, r'$B_1$', fontsize=10, color=colors['tertiary'])
    ax_main.text(0.2, -b - 0.4, r'$B_2$', fontsize=10, color=colors['tertiary'])
    
    # Semiejes
    ax_main.plot([0, a], [0, 0], color=colors['secondary'], linewidth=2.5)
    ax_main.text(a/2, -0.5, 'a', fontsize=14, fontweight='bold', ha='center',
                color=colors['secondary'])
    
    ax_main.plot([0, 0], [0, b], color=colors['tertiary'], linewidth=2.5)
    ax_main.text(0.3, b/2, 'b', fontsize=14, fontweight='bold',
                color=colors['tertiary'])
    
    # Distancia focal c
    ax_main.plot([0, c], [0.6, 0.6], color='#f59e0b', linewidth=2)
    ax_main.text(c/2, 0.9, 'c', fontsize=12, fontweight='bold', ha='center',
                color='#f59e0b')
    
    # Punto P y distancias a los focos
    Px, Py = a * np.cos(np.radians(60)), b * np.sin(np.radians(60))
    ax_main.plot(Px, Py, 'o', color=colors['accent'], markersize=10, zorder=5)
    ax_main.text(Px + 0.2, Py + 0.3, 'P', fontsize=11, fontweight='bold',
                color=colors['accent'])
    
    # Líneas a los focos (propiedad: d1 + d2 = 2a)
    ax_main.plot([Px, -c], [Py, 0], '--', color=colors['accent'], linewidth=1.5, alpha=0.7)
    ax_main.plot([Px, c], [Py, 0], '--', color=colors['accent'], linewidth=1.5, alpha=0.7)
    ax_main.text(-1, Py/2 + 0.5, r'$d_1$', fontsize=10, color=colors['accent'])
    ax_main.text(Px/2 + 0.5, Py/2, r'$d_2$', fontsize=10, color=colors['accent'])
    
    # Propiedad fundamental
    ax_main.text(0, -3.3, r'$d_1 + d_2 = 2a$ (definición de elipse)', fontsize=12,
                ha='center', color=colors['text'],
                bbox=dict(facecolor='white', edgecolor=colors['primary'], 
                         boxstyle='round,pad=0.4'))
    
    ax_main.set_xlim(-5.5, 5.5)
    ax_main.set_ylim(-4, 3.5)
    ax_main.set_aspect('equal')
    ax_main.set_title('Elipse con Eje Mayor Horizontal', fontsize=11, fontweight='bold')
    
    # =========================================
    # PANEL INFERIOR IZQUIERDO: Ecuaciones
    # =========================================
    ax_formulas.axis('off')
    ax_formulas.set_xlim(0, 1)
    ax_formulas.set_ylim(0, 1)
    
    ax_formulas.text(0.5, 0.95, 'ECUACIONES CANÓNICAS', fontsize=11,
                    fontweight='bold', ha='center', color=colors['primary'])
    
    # Eje mayor horizontal
    ax_formulas.add_patch(plt.Rectangle((0.03, 0.55), 0.94, 0.35,
                                        facecolor='#eff6ff', edgecolor=colors['secondary'],
                                        linewidth=1.5))
    ax_formulas.text(0.5, 0.84, 'Eje mayor horizontal (a > b)', fontsize=10,
                    fontweight='bold', ha='center', color=colors['secondary'])
    ax_formulas.text(0.5, 0.72, r'$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$',
                    fontsize=13, ha='center', color=colors['text'])
    ax_formulas.text(0.5, 0.6, r'Focos: $(\pm c, 0)$  •  Vértices: $(\pm a, 0)$',
                    fontsize=9, ha='center', color='#6b7280')
    
    # Eje mayor vertical
    ax_formulas.add_patch(plt.Rectangle((0.03, 0.12), 0.94, 0.38,
                                        facecolor='#f0fdf4', edgecolor=colors['tertiary'],
                                        linewidth=1.5))
    ax_formulas.text(0.5, 0.44, 'Eje mayor vertical (a > b)', fontsize=10,
                    fontweight='bold', ha='center', color=colors['tertiary'])
    ax_formulas.text(0.5, 0.32, r'$\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1$',
                    fontsize=13, ha='center', color=colors['text'])
    ax_formulas.text(0.5, 0.2, r'Focos: $(0, \pm c)$  •  Vértices: $(0, \pm a)$',
                    fontsize=9, ha='center', color='#6b7280')
    
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
    ax_props.text(0.5, 0.72, r'$c^2 = a^2 - b^2$  o  $a^2 = b^2 + c^2$',
                 fontsize=12, ha='center', color=colors['text'])
    
    # Excentricidad
    ax_props.add_patch(plt.Rectangle((0.03, 0.3), 0.94, 0.3,
                                     facecolor='#fce7f3', edgecolor='#ec4899',
                                     linewidth=1.5))
    ax_props.text(0.5, 0.54, 'Excentricidad', fontsize=10,
                 fontweight='bold', ha='center', color='#ec4899')
    ax_props.text(0.5, 0.44, r'$e = \frac{c}{a} = \sqrt{1 - \frac{b^2}{a^2}}$',
                 fontsize=12, ha='center', color=colors['text'])
    ax_props.text(0.5, 0.34, r'$0 < e < 1$ (elipse)',
                 fontsize=10, ha='center', color='#6b7280')
    
    # Interpretación de e
    ax_props.text(0.5, 0.2, 'Interpretación:', fontsize=9, fontweight='bold',
                 ha='center', color='#374151')
    ax_props.text(0.5, 0.12, r'$e \approx 0$: casi circular',
                 fontsize=9, ha='center', color='#6b7280')
    ax_props.text(0.5, 0.05, r'$e \approx 1$: muy alargada',
                 fontsize=9, ha='center', color='#6b7280')
    
    fig.suptitle('La Elipse', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "elipse.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'elipse.svg'}")
