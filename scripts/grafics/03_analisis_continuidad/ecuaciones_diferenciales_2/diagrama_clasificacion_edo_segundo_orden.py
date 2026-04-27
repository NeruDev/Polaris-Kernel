# yaml_frontmatter:
#   id: 'diagrama_clasificacion_edo_segundo_orden'
#   title: 'Diagrama de flujo para clasificar EDO de segundo orden'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'ecuaciones_diferenciales_2']

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
from matplotlib.patches import FancyBboxPatch

    setup_style,
    get_colors,
    get_output_dir_for_topic,
    save_figure,
)

# ============================================================
# Metadatos del Gráfico
# ============================================================



def draw_box(ax, x, y, width, height, text, color, text_color='white', fontsize=10, 
             box_style='round', alpha=0.9, linewidth=2):
        box = FancyBboxPatch(
        (x - width/2, y - height/2), width, height,
        boxstyle=f"{box_style},pad=0.05,rounding_size=0.15",
        facecolor=color, edgecolor='#1f2937', linewidth=linewidth,
        alpha=alpha
    )
    ax.add_patch(box)
    
    lines = text.split('\n')
    n_lines = len(lines)
    for i, line in enumerate(lines):
        offset = (n_lines - 1) / 2 - i
        ax.text(x, y + offset * 0.35, line, ha='center', va='center', 
                fontsize=fontsize, color=text_color, weight='bold',
                fontfamily='DejaVu Sans')
    return box


def draw_arrow(ax, start, end, color='#64748b', style='-'):
        ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=2,
                               connectionstyle='arc3,rad=0', linestyle=style))


def draw_decision(ax, x, y, size, text, color):
        diamond = plt.Polygon([
        [x, y + size],
        [x + size, y],
        [x, y - size],
        [x - size, y]
    ], closed=True, facecolor=color, edgecolor='#1f2937', linewidth=2, alpha=0.9)
    ax.add_patch(diamond)
    ax.text(x, y, text, ha='center', va='center', fontsize=8,
            color='white', weight='bold', fontfamily='DejaVu Sans')


def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig, ax = plt.subplots(figsize=(18, 14))
    ax.set_xlim(-1, 19)
    ax.set_ylim(-1, 15)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Colores
    c_primary = colors['primary']
    c_secondary = colors['secondary']
    c_accent = colors['accent']
    c_tertiary = colors['tertiary']
    c_header = '#1e3a5f'
    c_decision = '#f59e0b'
    
    # =========================================
    # Nivel 1: EDO principal
    # =========================================
    draw_box(ax, 9, 14, 10, 1.5, "Ecuación de Segundo Orden\nay'' + by' + cy = f(x)", 
             c_header, fontsize=12)
    
    # Flecha hacia decisión
    draw_arrow(ax, (9, 13.25), (9, 12.3))
    
    # =========================================
    # Nivel 2: Decisión homogénea/no homogénea
    # =========================================
    draw_decision(ax, 9, 11.5, 0.8, "f(x)=0?", c_decision)
    
    # Ramas
    draw_arrow(ax, (8.2, 11.5), (6.5, 10.8))
    draw_arrow(ax, (9.8, 11.5), (11.5, 10.8))
    
    ax.text(7, 11.4, "Sí", fontsize=10, color='#059669', weight='bold')
    ax.text(10.8, 11.4, "No", fontsize=10, color='#dc2626', weight='bold')
    
    # =========================================
    # Nivel 3: Homogénea y No Homogénea
    # =========================================
    draw_box(ax, 5, 10, 4, 1.2, "HOMOGÉNEA\ny_h solución general", c_primary, fontsize=11)
    draw_box(ax, 13, 10, 4, 1.2, "NO HOMOGÉNEA\ny = y_h + y_p", c_secondary, fontsize=11)
    
    # Ramas desde homogénea
    draw_arrow(ax, (3.5, 9.4), (3.5, 8.6))
    draw_arrow(ax, (6.5, 9.4), (6.5, 8.6))
    
    # Ramas desde no homogénea
    draw_arrow(ax, (11.5, 9.4), (11.5, 8.6))
    draw_arrow(ax, (14.5, 9.4), (14.5, 8.6))
    
    # =========================================
    # Nivel 4: Tipos de coeficientes y métodos
    # =========================================
    # Homogénea
    draw_box(ax, 3.5, 8, 3.5, 1.3, "Coeficientes\nconstantes\na, b, c ∈ ℝ", c_accent, fontsize=10)
    draw_box(ax, 6.5, 8, 3.5, 1.3, "Cauchy-Euler\nax²y'' + bxy'\n+ cy = 0", c_tertiary, fontsize=10)
    
    # No homogénea
    draw_box(ax, 11.5, 8, 3.5, 1.3, "f(x) específica\npolin, exp,\nsin/cos", c_accent, fontsize=10)
    draw_box(ax, 14.5, 8, 3.5, 1.3, "f(x) general\ncualquier\nfunción", c_tertiary, fontsize=10)
    
    # Flechas a métodos
    draw_arrow(ax, (3.5, 7.35), (3.5, 6.6))
    draw_arrow(ax, (6.5, 7.35), (6.5, 6.6))
    draw_arrow(ax, (11.5, 7.35), (11.5, 6.6))
    draw_arrow(ax, (14.5, 7.35), (14.5, 6.6))
    
    # =========================================
    # Nivel 5: Métodos específicos
    # =========================================
    draw_box(ax, 3.5, 6, 3.2, 1.2, "Ec. característica\nar² + br + c = 0", '#64748b', fontsize=9)
    draw_box(ax, 6.5, 6, 3.2, 1.2, "Ec. auxiliar\nam² + (b-a)m\n+ c = 0", '#64748b', fontsize=9)
    draw_box(ax, 11.5, 6, 3.2, 1.2, "Coeficientes\nindeterminados", '#64748b', fontsize=9)
    draw_box(ax, 14.5, 6, 3.2, 1.2, "Variación de\nparámetros", '#64748b', fontsize=9)
    
    # Flechas a casos de raíces
    draw_arrow(ax, (3.5, 5.4), (3.5, 4.6))
    
    # =========================================
    # Nivel 6: Casos de raíces (solo para coef. constantes)
    # =========================================
    draw_box(ax, 3.5, 4, 7, 1, "CASOS SEGÚN RAÍCES DE ar² + br + c = 0", c_header, fontsize=10)
    
    # Flechas a los tres casos
    draw_arrow(ax, (1.5, 3.5), (1.5, 2.8))
    draw_arrow(ax, (3.5, 3.5), (3.5, 2.8))
    draw_arrow(ax, (5.5, 3.5), (5.5, 2.8))
    
    # Tres casos
    draw_box(ax, 1.5, 2.2, 2.4, 1.2, "Δ > 0\nr₁ ≠ r₂ reales", c_primary, fontsize=9)
    draw_box(ax, 3.5, 2.2, 2.4, 1.2, "Δ = 0\nr₁ = r₂ = r", c_accent, fontsize=9)
    draw_box(ax, 5.5, 2.2, 2.4, 1.2, "Δ < 0\nr = α ± βi", c_secondary, fontsize=9)
    
    # Flechas a soluciones
    draw_arrow(ax, (1.5, 1.6), (1.5, 0.9))
    draw_arrow(ax, (3.5, 1.6), (3.5, 0.9))
    draw_arrow(ax, (5.5, 1.6), (5.5, 0.9))
    
    # Soluciones
    draw_box(ax, 1.5, 0.3, 2.8, 0.9, "y = C₁e^(r₁x)\n+ C₂e^(r₂x)", '#94a3b8', fontsize=8, text_color='#1f2937')
    draw_box(ax, 3.5, 0.3, 2.8, 0.9, "y = (C₁+C₂x)\ne^(rx)", '#94a3b8', fontsize=8, text_color='#1f2937')
    draw_box(ax, 5.5, 0.3, 2.8, 0.9, "y = e^(αx)(C₁cosβx\n+ C₂sinβx)", '#94a3b8', fontsize=8, text_color='#1f2937')
    
    # =========================================
    # Caso adicional: Reducción de orden
    # =========================================
    draw_box(ax, 13, 4, 5, 1.2, "Caso especial:\nConocida una solución y₁", c_decision, 
             text_color='#1f2937', fontsize=10)
    draw_arrow(ax, (13, 3.4), (13, 2.6))
    draw_box(ax, 13, 2, 4, 1, "REDUCCIÓN DE ORDEN\ny₂ = y₁∫(e^(-∫P dx)/y₁²)dx", '#64748b', fontsize=9)
    
    # =========================================
    # Leyenda
    # =========================================
    legend_x, legend_y = 9, -0.5
    ax.text(legend_x - 4, legend_y, "Tipos:", fontsize=10, weight='bold', color='#1f2937')
    
    for i, (label, color) in enumerate([
        ("Homogénea", c_primary),
        ("No homogénea", c_secondary),
        ("Coef. constantes", c_accent),
        ("Cauchy-Euler", c_tertiary),
        ("Decisión", c_decision),
    ]):
        x = legend_x - 2.5 + i * 3
        box = FancyBboxPatch((x, legend_y - 0.25), 0.35, 0.35, boxstyle="round,pad=0.02",
                             facecolor=color, edgecolor='none')
        ax.add_patch(box)
        ax.text(x + 0.5, legend_y - 0.08, label, fontsize=8, va='center', color='#1f2937')
    
    # Título
    fig.suptitle("Diagrama de Clasificación: EDO de Segundo Orden",
                fontsize=16, weight='bold', y=0.98, color='#1f2937')
    
    plt.tight_layout()
    return fig


# ============================================================
# Ejecución directa para pruebas
# ============================================================

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "diagrama_clasificacion_edo_segundo_orden.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'diagrama_clasificacion_edo_segundo_orden.svg'}")
