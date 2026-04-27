# yaml_frontmatter:
#   id: 'diagrama_decision_laplace'
#   title: 'Diagrama de flujo para métodos de Transformada de Laplace'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'ecuaciones_diferenciales_4']

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



def draw_box(ax, x, y, width, height, text, color, text_color='white', fontsize=10):
        box = FancyBboxPatch(
        (x - width/2, y - height/2), width, height,
        boxstyle="round,pad=0.05,rounding_size=0.15",
        facecolor=color, edgecolor='#1f2937', linewidth=2, alpha=0.9
    )
    ax.add_patch(box)
    
    lines = text.split('\n')
    n_lines = len(lines)
    for i, line in enumerate(lines):
        offset = (n_lines - 1) / 2 - i
        ax.text(x, y + offset * 0.3, line, ha='center', va='center', 
                fontsize=fontsize, color=text_color, weight='bold',
                fontfamily='DejaVu Sans')
    return box


def draw_arrow(ax, start, end, color='#64748b'):
        ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=2,
                               connectionstyle='arc3,rad=0'))


def draw_decision(ax, x, y, size, text, color):
        diamond = plt.Polygon([
        [x, y + size],
        [x + size * 0.9, y],
        [x, y - size],
        [x - size * 0.9, y]
    ], closed=True, facecolor=color, edgecolor='#1f2937', linewidth=2, alpha=0.9)
    ax.add_patch(diamond)
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        offset = (len(lines) - 1) / 2 - i
        ax.text(x, y + offset * 0.25, line, ha='center', va='center', fontsize=8,
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
    c_method = '#64748b'
    
    # =========================================
    # Nivel 1: Pregunta principal
    # =========================================
    draw_box(ax, 9, 14, 8, 1.2, "¿Qué tipo de problema?", c_header, fontsize=14)
    
    # Flechas a tres tipos
    draw_arrow(ax, (5, 13.4), (5, 12.6))
    draw_arrow(ax, (9, 13.4), (9, 12.6))
    draw_arrow(ax, (13, 13.4), (13, 12.6))
    
    # =========================================
    # Nivel 2: Tipos de problema
    # =========================================
    draw_box(ax, 5, 12, 3.5, 1.2, "Calcular\n𝓛{f(t)}", c_primary, fontsize=11)
    draw_box(ax, 9, 12, 3.5, 1.2, "Calcular\n𝓛⁻¹{F(s)}", c_secondary, fontsize=11)
    draw_box(ax, 13, 12, 3.5, 1.2, "Resolver\nPVI", c_accent, fontsize=11)
    
    # =========================================
    # Rama: Calcular 𝓛 (izquierda)
    # =========================================
    draw_arrow(ax, (5, 11.4), (5, 10.6))
    draw_decision(ax, 5, 10, 0.6, "¿e^(at)·f?", c_decision)
    
    # SÍ
    draw_arrow(ax, (4.4, 10), (3, 9.5))
    ax.text(3.5, 10, "Sí", fontsize=9, color='#059669', weight='bold')
    draw_box(ax, 2.5, 9, 2.2, 0.9, "1ª traslación\nF(s-a)", c_method, fontsize=9)
    
    # NO
    draw_arrow(ax, (5.6, 10), (6.5, 9.5))
    ax.text(6.2, 10, "No", fontsize=9, color='#dc2626', weight='bold')
    draw_decision(ax, 6.5, 9, 0.55, "¿u(t-a)?", c_decision)
    
    # u(t-a) SÍ
    draw_arrow(ax, (5.95, 9), (5, 8.3))
    ax.text(5.2, 8.8, "Sí", fontsize=8, color='#059669', weight='bold')
    draw_box(ax, 4.5, 7.8, 2.2, 0.8, "2ª traslación\ne^(-as)F(s)", c_method, fontsize=8)
    
    # u(t-a) NO
    draw_arrow(ax, (7.05, 9), (8, 8.3))
    ax.text(7.7, 8.8, "No", fontsize=8, color='#dc2626', weight='bold')
    draw_box(ax, 8, 7.8, 2, 0.8, "Usar tabla\ndirecta", c_method, fontsize=8)
    
    # =========================================
    # Rama: Calcular 𝓛⁻¹ (centro)
    # =========================================
    draw_arrow(ax, (9, 11.4), (9, 10.6))
    draw_decision(ax, 9, 10, 0.6, "¿Racional?", c_decision)
    
    # SÍ
    draw_arrow(ax, (9, 9.4), (9, 8.6))
    ax.text(9.3, 9.1, "Sí", fontsize=9, color='#059669', weight='bold')
    draw_box(ax, 9, 8, 2.5, 0.9, "Fracciones\nparciales", c_method, fontsize=9)
    
    draw_arrow(ax, (9, 7.55), (9, 6.9))
    draw_decision(ax, 9, 6.3, 0.55, "¿Cuadrático\nirreducible?", c_decision)
    
    # Cuadrático SÍ
    draw_arrow(ax, (8.45, 6.3), (7.5, 5.7))
    ax.text(7.7, 6.1, "Sí", fontsize=8, color='#059669', weight='bold')
    draw_box(ax, 7, 5.2, 2.2, 0.8, "Completar\ncuadrado", c_method, fontsize=8)
    
    draw_arrow(ax, (7, 4.8), (7, 4.2))
    draw_box(ax, 7, 3.7, 2.5, 0.8, "Identificar\ncos/sin amort.", c_method, fontsize=8)
    
    # Cuadrático NO
    draw_arrow(ax, (9.55, 6.3), (10.5, 5.7))
    ax.text(10.3, 6.1, "No", fontsize=8, color='#dc2626', weight='bold')
    draw_box(ax, 11, 5.2, 2.2, 0.8, "Separar\nfracciones", c_method, fontsize=8)
    
    draw_arrow(ax, (11, 4.8), (11, 4.2))
    draw_box(ax, 11, 3.7, 2.2, 0.8, "Usar tabla\ninversa", c_method, fontsize=8)
    
    # =========================================
    # Rama: Resolver PVI (derecha)
    # =========================================
    draw_arrow(ax, (13, 11.4), (13, 10.6))
    draw_box(ax, 13, 10, 2.5, 0.9, "Aplicar 𝓛\na la EDO", c_tertiary, fontsize=9)
    
    draw_arrow(ax, (13, 9.55), (13, 8.9))
    draw_box(ax, 13, 8.4, 2.5, 0.9, "Sustituir\nderivadas", c_method, fontsize=9)
    
    draw_arrow(ax, (13, 7.95), (13, 7.3))
    draw_box(ax, 13, 6.8, 2.5, 0.9, "Despejar\nY(s)", c_method, fontsize=9)
    
    draw_arrow(ax, (13, 6.35), (13, 5.7))
    draw_box(ax, 13, 5.2, 2.5, 0.9, "Fracciones\nparciales", c_method, fontsize=9)
    
    draw_arrow(ax, (13, 4.75), (13, 4.1))
    draw_box(ax, 13, 3.6, 2.5, 0.9, "Aplicar 𝓛⁻¹", c_method, fontsize=9)
    
    draw_arrow(ax, (13, 3.15), (13, 2.5))
    draw_box(ax, 13, 2, 2.8, 0.9, "y(t) = 𝓛⁻¹{Y(s)}", c_accent, fontsize=10)
    
    # =========================================
    # Casos especiales (parte inferior izquierda)
    # =========================================
    draw_box(ax, 3.5, 5.5, 6, 0.9, "FUNCIONES ESPECIALES", c_header, fontsize=10)
    
    draw_arrow(ax, (1.5, 5.05), (1.5, 4.4))
    draw_arrow(ax, (3.5, 5.05), (3.5, 4.4))
    draw_arrow(ax, (5.5, 5.05), (5.5, 4.4))
    
    draw_box(ax, 1.5, 3.9, 1.8, 0.8, "δ(t-a)\nImpulso", c_tertiary, fontsize=8)
    draw_box(ax, 3.5, 3.9, 1.8, 0.8, "u(t-a)\nEscalón", c_primary, fontsize=8)
    draw_box(ax, 5.5, 3.9, 1.8, 0.8, "Periódica\nf(t+T)=f(t)", c_secondary, fontsize=8)
    
    draw_arrow(ax, (1.5, 3.5), (1.5, 2.9))
    draw_arrow(ax, (3.5, 3.5), (3.5, 2.9))
    draw_arrow(ax, (5.5, 3.5), (5.5, 2.9))
    
    draw_box(ax, 1.5, 2.4, 1.9, 0.8, "e^(-as)", '#94a3b8', fontsize=8, text_color='#1f2937')
    draw_box(ax, 3.5, 2.4, 1.9, 0.8, "e^(-as)/s", '#94a3b8', fontsize=8, text_color='#1f2937')
    draw_box(ax, 5.5, 2.4, 2.2, 0.8, "F₀(s)/(1-e^(-sT))", '#94a3b8', fontsize=8, text_color='#1f2937')
    
    # =========================================
    # Leyenda
    # =========================================
    legend_y = 0.5
    ax.text(0.5, legend_y, "Tipo de problema:", fontsize=9, weight='bold', color='#1f2937')
    
    for i, (label, color) in enumerate([
        ("𝓛 directa", c_primary),
        ("𝓛⁻¹ inversa", c_secondary),
        ("Resolver PVI", c_accent),
        ("Especiales", c_tertiary),
    ]):
        x = 4 + i * 3.5
        box = FancyBboxPatch((x, legend_y - 0.25), 0.35, 0.35, boxstyle="round,pad=0.02",
                             facecolor=color, edgecolor='none')
        ax.add_patch(box)
        ax.text(x + 0.5, legend_y - 0.08, label, fontsize=9, va='center', color='#1f2937')
    
    # Título
    fig.suptitle("Diagrama de Decisión: Transformada de Laplace",
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
        fig.savefig(output_dir / "diagrama_decision_laplace.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'diagrama_decision_laplace.svg'}")
