# yaml_frontmatter:
#   id: 'diagrama_decision_series_potencias'
#   title: 'Diagrama de flujo para método de series de potencias'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'ecuaciones_diferenciales_5']

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
        ax.text(x, y + offset * 0.32, line, ha='center', va='center', 
                fontsize=fontsize, color=text_color, weight='bold',
                fontfamily='DejaVu Sans')
    return box


def draw_arrow(ax, start, end, color='#64748b'):
        ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=2,
                               connectionstyle='arc3,rad=0'))


def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig, ax = plt.subplots(figsize=(16, 14))
    ax.set_xlim(-1, 17)
    ax.set_ylim(-1, 15)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Colores
    c_primary = colors['primary']
    c_secondary = colors['secondary']
    c_accent = colors['accent']
    c_tertiary = colors['tertiary']
    c_header = '#1e3a5f'
    c_method = '#64748b'
    c_warning = '#dc2626'
    
    # =========================================
    # Nivel 1: EDO
    # =========================================
    draw_box(ax, 8, 14, 10, 1.3, "EDO lineal de segundo orden\ny'' + P(x)y' + Q(x)y = 0", 
             c_header, fontsize=12)
    
    draw_arrow(ax, (8, 13.35), (8, 12.6))
    
    # =========================================
    # Nivel 2: Clasificar punto
    # =========================================
    draw_box(ax, 8, 12, 4, 1, "Clasificar x₀", c_primary, fontsize=12)
    
    # Flechas a tres tipos de punto
    draw_arrow(ax, (4, 11.5), (4, 10.7))
    draw_arrow(ax, (8, 11.5), (8, 10.7))
    draw_arrow(ax, (12, 11.5), (12, 10.7))
    
    # =========================================
    # Nivel 3: Tipos de punto
    # =========================================
    draw_box(ax, 4, 10, 3.5, 1.2, "ORDINARIO\nP, Q analíticas", c_accent, fontsize=11)
    draw_box(ax, 8, 10, 3.8, 1.2, "SINGULAR\nREGULAR", c_tertiary, fontsize=11)
    draw_box(ax, 12, 10, 3.8, 1.2, "SINGULAR\nIRREGULAR", c_warning, fontsize=11)
    
    # =========================================
    # Rama Ordinario
    # =========================================
    draw_arrow(ax, (4, 9.4), (4, 8.6))
    draw_box(ax, 4, 8, 3.5, 1.2, "Series de potencias\ny = Σcₙxⁿ", c_method, fontsize=10)
    
    draw_arrow(ax, (4, 7.4), (4, 6.7))
    draw_box(ax, 4, 6.1, 3.5, 1, "c₀, c₁ arbitrarios\n→ 2 soluciones indep.", '#94a3b8', 
             fontsize=9, text_color='#1f2937')
    
    # =========================================
    # Rama Singular Regular (Frobenius)
    # =========================================
    draw_arrow(ax, (8, 9.4), (8, 8.6))
    draw_box(ax, 8, 8, 4, 1.2, "Método de Frobenius\ny = x^r Σcₙxⁿ", c_method, fontsize=10)
    
    draw_arrow(ax, (8, 7.4), (8, 6.7))
    draw_box(ax, 8, 6.1, 4, 1, "Ecuación indicial\nr² + (p₀-1)r + q₀ = 0", c_primary, fontsize=9)
    
    # Flechas a tres casos de Frobenius
    draw_arrow(ax, (6, 5.6), (6, 4.9))
    draw_arrow(ax, (8, 5.6), (8, 4.9))
    draw_arrow(ax, (10, 5.6), (10, 4.9))
    
    # =========================================
    # Tres casos de Frobenius
    # =========================================
    draw_box(ax, 6, 4.3, 2.8, 1.1, "CASO 1\nr₁ - r₂ ∉ ℤ", c_accent, fontsize=9)
    draw_box(ax, 8, 4.3, 2.8, 1.1, "CASO 2\nr₁ = r₂", c_tertiary, fontsize=9)
    draw_box(ax, 10, 4.3, 2.8, 1.1, "CASO 3\nr₁ - r₂ ∈ ℤ⁺", c_secondary, fontsize=9)
    
    # Soluciones para cada caso
    draw_arrow(ax, (6, 3.75), (6, 3.1))
    draw_arrow(ax, (8, 3.75), (8, 3.1))
    draw_arrow(ax, (10, 3.75), (10, 3.1))
    
    draw_box(ax, 6, 2.5, 3.2, 1, "y₁ = x^(r₁)Σaₙxⁿ\ny₂ = x^(r₂)Σbₙxⁿ", '#94a3b8', 
             fontsize=8, text_color='#1f2937')
    draw_box(ax, 8, 2.5, 3.2, 1, "y₁ = x^r Σaₙxⁿ\ny₂ = y₁ ln x + x^r Σbₙxⁿ", '#94a3b8', 
             fontsize=8, text_color='#1f2937')
    draw_box(ax, 10, 2.5, 3.5, 1, "y₁ = x^(r₁)Σaₙxⁿ\ny₂ = Cy₁ ln x + x^(r₂)Σbₙxⁿ", '#94a3b8', 
             fontsize=8, text_color='#1f2937')
    
    # =========================================
    # Rama Singular Irregular
    # =========================================
    draw_arrow(ax, (12, 9.4), (12, 8.6))
    draw_box(ax, 12, 8, 3.5, 1.2, "Métodos especiales\n(fuera del alcance)", c_method, fontsize=10)
    
    draw_arrow(ax, (12, 7.4), (12, 6.7))
    draw_box(ax, 12, 6.1, 3.8, 1, "Series asintóticas\no transformaciones", '#94a3b8', 
             fontsize=9, text_color='#1f2937')
    
    # =========================================
    # Ecuaciones especiales (parte inferior)
    # =========================================
    draw_box(ax, 8, 0.8, 14, 0.9, "ECUACIONES ESPECIALES", c_header, fontsize=11)
    
    # Tres ecuaciones especiales
    draw_box(ax, 3, -0.5, 3.5, 1.2, "AIRY\ny'' = xy", c_accent, fontsize=10)
    draw_box(ax, 8, -0.5, 4, 1.2, "BESSEL\nx²y'' + xy' + (x²-ν²)y = 0", c_tertiary, fontsize=9)
    draw_box(ax, 13, -0.5, 4.2, 1.2, "LEGENDRE\n(1-x²)y'' - 2xy' + n(n+1)y = 0", c_secondary, fontsize=9)
    
    # =========================================
    # Nota sobre criterio
    # =========================================
    note_text = (
        "Criterio para x₀ = 0:\n"
        "• Ordinario: P(0) y Q(0) finitos\n"
        "• Singular regular: xP(x) y x²Q(x) analíticos\n"
        "• Singular irregular: otro caso"
    )
    ax.text(14.5, 4.5, note_text, fontsize=9, fontfamily='DejaVu Sans',
            va='top', ha='left', color='#1f2937',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#f8fafc', 
                     edgecolor='#64748b', alpha=0.95))
    
    # =========================================
    # Leyenda
    # =========================================
    legend_y = 1.5
    ax.text(-0.5, legend_y + 0.3, "Tipo de punto:", fontsize=9, weight='bold', color='#1f2937')
    
    for i, (label, color) in enumerate([
        ("Ordinario", c_accent),
        ("Sing. regular", c_tertiary),
        ("Sing. irregular", c_warning),
    ]):
        box = FancyBboxPatch((-0.3, legend_y - i * 0.5 - 0.1), 0.3, 0.3, 
                             boxstyle="round,pad=0.02", facecolor=color, edgecolor='none')
        ax.add_patch(box)
        ax.text(0.2, legend_y - i * 0.5 + 0.05, label, fontsize=8, va='center', color='#1f2937')
    
    # Título
    fig.suptitle("Diagrama de Decisión: Método de Series de Potencias",
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
        fig.savefig(output_dir / "diagrama_decision_series_potencias.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'diagrama_decision_series_potencias.svg'}")
