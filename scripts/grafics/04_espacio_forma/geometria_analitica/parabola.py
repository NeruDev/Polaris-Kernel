# yaml_frontmatter:
#   id: 'parabola'
#   title: 'La parábola: elementos, ecuaciones y orientaciones'
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
    gs = fig.add_gridspec(2, 2, height_ratios=[1.3, 1], hspace=0.2, wspace=0.15)
    
    ax_main = fig.add_subplot(gs[0, 0])
    ax_types = fig.add_subplot(gs[0, 1])
    ax_formulas = fig.add_subplot(gs[1, :])
    
    # =========================================
    # PANEL 1: Parábola principal con elementos
    # =========================================
    ax_main.grid(True, linestyle='--', alpha=0.3)
    ax_main.axhline(y=0, color='#9ca3af', linewidth=1)
    ax_main.axvline(x=0, color='#9ca3af', linewidth=1)
    
    # Parámetro p
    p = 1.5
    
    # Parábola x² = 4py (abre arriba)
    x = np.linspace(-4, 4, 200)
    y = x**2 / (4*p)
    ax_main.plot(x, y, color=colors['primary'], linewidth=2.5)
    
    # Vértice
    ax_main.plot(0, 0, 'o', color=colors['primary'], markersize=10, zorder=5)
    ax_main.text(0.3, -0.5, 'V (vértice)', fontsize=10, color=colors['primary'])
    
    # Foco
    ax_main.plot(0, p, '*', color='#f59e0b', markersize=15, zorder=5)
    ax_main.text(0.3, p + 0.2, 'F (foco)', fontsize=10, color='#f59e0b')
    
    # Directriz
    ax_main.axhline(y=-p, color='#dc2626', linewidth=2, linestyle='--')
    ax_main.text(3, -p - 0.4, 'Directriz: y = -p', fontsize=10, color='#dc2626')
    
    # Eje de simetría
    ax_main.axvline(x=0, color=colors['tertiary'], linewidth=2, linestyle=':',
                   alpha=0.7)
    ax_main.text(0.3, 4, 'Eje de simetría', fontsize=9, color=colors['tertiary'])
    
    # Lado recto (4p)
    x_lr = 2*p
    y_lr = p
    ax_main.plot([-x_lr, x_lr], [y_lr, y_lr], color=colors['secondary'], linewidth=2.5)
    ax_main.text(x_lr + 0.2, y_lr, 'Lado recto = 4p', fontsize=9, color=colors['secondary'])
    
    # Distancia p
    ax_main.annotate('', xy=(2.5, 0), xytext=(2.5, p),
                    arrowprops=dict(arrowstyle='<->', color='#6b7280', lw=1.5))
    ax_main.text(2.7, p/2, 'p', fontsize=11, fontweight='bold', color='#6b7280')
    
    ax_main.annotate('', xy=(-2.5, 0), xytext=(-2.5, -p),
                    arrowprops=dict(arrowstyle='<->', color='#6b7280', lw=1.5))
    ax_main.text(-2.3, -p/2, 'p', fontsize=11, fontweight='bold', color='#6b7280')
    
    # Punto P y distancias iguales
    Px, Py = 2.5, 2.5**2 / (4*p)
    ax_main.plot(Px, Py, 'o', color=colors['accent'], markersize=8, zorder=5)
    ax_main.text(Px + 0.2, Py + 0.3, 'P', fontsize=10, color=colors['accent'])
    
    # Línea al foco
    ax_main.plot([Px, 0], [Py, p], ':', color=colors['accent'], linewidth=1.5)
    # Línea a directriz
    ax_main.plot([Px, Px], [Py, -p], ':', color=colors['accent'], linewidth=1.5)
    
    ax_main.set_xlim(-5, 5)
    ax_main.set_ylim(-2.5, 5)
    ax_main.set_aspect('equal')
    ax_main.set_title(r'Parábola $x^2 = 4py$ (abre arriba)', fontsize=11, fontweight='bold')
    
    # =========================================
    # PANEL 2: Las 4 orientaciones
    # =========================================
    ax_types.axis('off')
    ax_types.set_xlim(0, 1)
    ax_types.set_ylim(0, 1)
    
    ax_types.text(0.5, 0.95, 'Orientaciones de la Parábola', fontsize=11,
                 fontweight='bold', ha='center', color=colors['primary'])
    
    # Mini-gráficas esquemáticas
    orientations = [
        (0.25, 0.7, 'Abre arriba', r'$x^2 = 4py$', '↑', colors['secondary']),
        (0.75, 0.7, 'Abre abajo', r'$x^2 = -4py$', '↓', colors['tertiary']),
        (0.25, 0.35, 'Abre derecha', r'$y^2 = 4px$', '→', '#f59e0b'),
        (0.75, 0.35, 'Abre izquierda', r'$y^2 = -4px$', '←', '#ec4899'),
    ]
    
    for x, y, name, eq, arrow, color in orientations:
        ax_types.add_patch(plt.Rectangle((x-0.2, y-0.12), 0.4, 0.24,
                                         facecolor='#f9fafb', edgecolor=color,
                                         linewidth=1.5))
        ax_types.text(x, y + 0.08, name, fontsize=9, fontweight='bold',
                     ha='center', color=color)
        ax_types.text(x, y - 0.02, eq, fontsize=10, ha='center', color=colors['text'])
        ax_types.text(x + 0.15, y + 0.08, arrow, fontsize=14, ha='center', color=color)
    
    # Tabla de focos y directrices
    ax_types.add_patch(plt.Rectangle((0.05, 0.02), 0.9, 0.18,
                                     facecolor='#fef3c7', edgecolor='#f59e0b',
                                     linewidth=1))
    ax_types.text(0.5, 0.16, 'Vértice en origen:', fontsize=9, fontweight='bold',
                 ha='center', color='#f59e0b')
    ax_types.text(0.5, 0.09, 'Foco a distancia p del vértice en dirección de apertura',
                 fontsize=8, ha='center', color='#374151')
    ax_types.text(0.5, 0.04, 'Directriz a distancia p en dirección opuesta',
                 fontsize=8, ha='center', color='#374151')
    
    # =========================================
    # PANEL INFERIOR: Fórmulas y propiedades
    # =========================================
    ax_formulas.axis('off')
    ax_formulas.set_xlim(0, 1)
    ax_formulas.set_ylim(0, 1)
    
    # Definición
    ax_formulas.add_patch(plt.Rectangle((0.02, 0.55), 0.46, 0.42,
                                        facecolor='#f0fdf4', edgecolor=colors['accent'],
                                        linewidth=1.5))
    ax_formulas.text(0.25, 0.92, 'DEFINICIÓN', fontsize=11, fontweight='bold',
                    ha='center', color=colors['accent'])
    ax_formulas.text(0.25, 0.82, 'Lugar geométrico de puntos que', fontsize=9,
                    ha='center', color='#374151')
    ax_formulas.text(0.25, 0.74, 'equidistan de un punto fijo (foco)', fontsize=9,
                    ha='center', color='#374151')
    ax_formulas.text(0.25, 0.66, 'y una recta fija (directriz)', fontsize=9,
                    ha='center', color='#374151')
    ax_formulas.text(0.25, 0.58, r'$d(P, F) = d(P, \text{directriz})$', fontsize=11,
                    ha='center', color=colors['text'])
    
    # Elementos
    ax_formulas.add_patch(plt.Rectangle((0.52, 0.55), 0.46, 0.42,
                                        facecolor='#eff6ff', edgecolor=colors['primary'],
                                        linewidth=1.5))
    ax_formulas.text(0.75, 0.92, 'ELEMENTOS', fontsize=11, fontweight='bold',
                    ha='center', color=colors['primary'])
    
    elements = [
        ('Vértice V:', 'Punto medio entre F y directriz'),
        ('Foco F:', 'Punto fijo interior'),
        ('Parámetro p:', 'Distancia V a F'),
        ('Lado recto:', 'Longitud = 4p'),
    ]
    y_pos = 0.82
    for elem, desc in elements:
        ax_formulas.text(0.55, y_pos, elem, fontsize=9, fontweight='bold', color='#374151')
        ax_formulas.text(0.75, y_pos, desc, fontsize=9, color='#6b7280')
        y_pos -= 0.07
    
    # Ecuación con vértice desplazado
    ax_formulas.add_patch(plt.Rectangle((0.02, 0.08), 0.96, 0.42,
                                        facecolor='#fef3c7', edgecolor='#f59e0b',
                                        linewidth=1.5))
    ax_formulas.text(0.5, 0.45, 'Vértice en (h, k)', fontsize=11, fontweight='bold',
                    ha='center', color='#f59e0b')
    
    ax_formulas.text(0.25, 0.33, 'Eje vertical:', fontsize=9, fontweight='bold',
                    ha='center', color='#374151')
    ax_formulas.text(0.25, 0.23, r'$(x-h)^2 = \pm 4p(y-k)$', fontsize=11,
                    ha='center', color=colors['text'])
    
    ax_formulas.text(0.75, 0.33, 'Eje horizontal:', fontsize=9, fontweight='bold',
                    ha='center', color='#374151')
    ax_formulas.text(0.75, 0.23, r'$(y-k)^2 = \pm 4p(x-h)$', fontsize=11,
                    ha='center', color=colors['text'])
    
    ax_formulas.text(0.5, 0.12, '(+) abre en sentido positivo del eje  •  (−) abre en sentido negativo',
                    fontsize=9, ha='center', color='#6b7280', style='italic')
    
    fig.suptitle('La Parábola', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "parabola.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'parabola.svg'}")
