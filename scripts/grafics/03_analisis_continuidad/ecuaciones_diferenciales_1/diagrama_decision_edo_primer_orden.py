# yaml_frontmatter:
#   id: 'diagrama_decision_edo_primer_orden'
#   title: 'Diagrama de flujo para identificar tipo de EDO de primer orden'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'ecuaciones_diferenciales_1']

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
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

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
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color=text_color, weight='bold', wrap=True,
            fontfamily='DejaVu Sans')
    return box


def draw_arrow(ax, start, end, color='#64748b'):
        ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=2,
                               connectionstyle='arc3,rad=0'))


def draw_decision(ax, x, y, size, text, color):
        diamond = plt.Polygon([
        [x, y + size],
        [x + size, y],
        [x, y - size],
        [x - size, y]
    ], closed=True, facecolor=color, edgecolor='#1f2937', linewidth=2, alpha=0.9)
    ax.add_patch(diamond)
    ax.text(x, y, text, ha='center', va='center', fontsize=9,
            color='white', weight='bold', fontfamily='DejaVu Sans')


def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig, ax = plt.subplots(figsize=(16, 12))
    ax.set_xlim(-1, 17)
    ax.set_ylim(-1, 13)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Colores del diagrama
    c_primary = colors['primary']      # Azul
    c_secondary = colors['secondary']  # Rojo
    c_accent = colors['accent']        # Verde
    c_tertiary = colors['tertiary']    # Púrpura
    c_header = '#1e3a5f'               # Azul oscuro
    c_decision = '#f59e0b'             # Naranja para decisiones
    
    # =========================================
    # Nivel 1: Pregunta principal
    # =========================================
    draw_box(ax, 8, 12, 8, 1.2, "¿Qué forma tiene la EDO?", c_header, fontsize=14)
    
    # Flechas hacia nivel 2
    draw_arrow(ax, (4, 11.4), (4, 10.6))
    draw_arrow(ax, (8, 11.4), (8, 10.6))
    draw_arrow(ax, (12, 11.4), (12, 10.6))
    
    # =========================================
    # Nivel 2: Tipos principales
    # =========================================
    draw_box(ax, 4, 10, 3.5, 1.2, "y' = g(x)·h(y)\nSEPARABLE", c_primary, fontsize=10)
    draw_box(ax, 8, 10, 3.5, 1.2, "y' + P(x)y = Q(x)\nLINEAL", c_accent, fontsize=10)
    draw_box(ax, 12, 10, 3.5, 1.2, "M dx + N dy = 0\nDIFERENCIAL", c_secondary, fontsize=10)
    
    # Flecha desde separable a método
    draw_arrow(ax, (4, 9.4), (4, 8.6))
    draw_box(ax, 4, 8, 3, 0.9, "Separar e\nintegrar", '#64748b', fontsize=9)
    
    # Flecha desde lineal a método  
    draw_arrow(ax, (8, 9.4), (8, 8.6))
    draw_box(ax, 8, 8, 3, 0.9, "Factor integrante\nμ = e^∫P dx", '#64748b', fontsize=9)
    
    # Desde diferencial a decisión
    draw_arrow(ax, (12, 9.4), (12, 8.6))
    draw_decision(ax, 12, 8, 0.7, "¿Mᵧ=Nₓ?", c_decision)
    
    # Ramas de exacta/no exacta
    draw_arrow(ax, (11.3, 8), (10.2, 7.3))
    draw_arrow(ax, (12.7, 8), (13.8, 7.3))
    
    draw_box(ax, 10, 6.8, 2.2, 0.9, "EXACTA\nBuscar F", c_accent, fontsize=9)
    draw_box(ax, 14, 6.8, 2.5, 0.9, "FACTOR\nINTEGRANTE", c_tertiary, fontsize=9)
    
    ax.text(10.5, 7.8, "Sí", fontsize=9, color='#059669', weight='bold')
    ax.text(13.2, 7.8, "No", fontsize=9, color='#dc2626', weight='bold')
    
    # =========================================
    # Nivel 3: Casos especiales (título)
    # =========================================
    draw_box(ax, 8, 5, 10, 1, "CASOS ESPECIALES", c_header, fontsize=12)
    
    # Flechas hacia casos especiales
    draw_arrow(ax, (3, 4.5), (3, 3.8))
    draw_arrow(ax, (6.5, 4.5), (6.5, 3.8))
    draw_arrow(ax, (9.5, 4.5), (9.5, 3.8))
    draw_arrow(ax, (13, 4.5), (13, 3.8))
    
    # =========================================
    # Nivel 4: Tipos especiales
    # =========================================
    draw_box(ax, 3, 3.2, 3.2, 1.4, "y' + Py = Qyⁿ\nBERNOULLI", c_tertiary, fontsize=10)
    draw_box(ax, 6.5, 3.2, 3.2, 1.4, "y' = F(y/x)\nHOMOGÉNEA", c_primary, fontsize=10)
    draw_box(ax, 9.5, 3.2, 3.2, 1.4, "y' = f(ax+by+c)\nSUSTITUCIÓN", c_accent, fontsize=10)
    draw_box(ax, 13, 3.2, 3.2, 1.4, "y' = P+Qy+Ry²\nRICATTI", c_secondary, fontsize=10)
    
    # Flechas hacia métodos de casos especiales
    draw_arrow(ax, (3, 2.5), (3, 1.8))
    draw_arrow(ax, (6.5, 2.5), (6.5, 1.8))
    draw_arrow(ax, (9.5, 2.5), (9.5, 1.8))
    draw_arrow(ax, (13, 2.5), (13, 1.8))
    
    # Métodos de resolución
    draw_box(ax, 3, 1.2, 2.8, 0.9, "v = y^(1-n)", '#64748b', fontsize=9)
    draw_box(ax, 6.5, 1.2, 2.8, 0.9, "v = y/x", '#64748b', fontsize=9)
    draw_box(ax, 9.5, 1.2, 2.8, 0.9, "u = ax+by+c", '#64748b', fontsize=9)
    draw_box(ax, 13, 1.2, 2.8, 0.9, "Conocer y₁", '#64748b', fontsize=9)
    
    # =========================================
    # Leyenda
    # =========================================
    legend_y = 0
    ax.text(0.5, legend_y, "Leyenda:", fontsize=10, weight='bold', color='#1f2937')
    
    # Muestras de colores
    for i, (label, color) in enumerate([
        ("Separable", c_primary),
        ("Lineal", c_accent),
        ("Exacta/Diferencial", c_secondary),
        ("Casos especiales", c_tertiary),
    ]):
        x = 2.5 + i * 3.5
        box = FancyBboxPatch((x, legend_y - 0.3), 0.4, 0.4, boxstyle="round,pad=0.02",
                             facecolor=color, edgecolor='none')
        ax.add_patch(box)
        ax.text(x + 0.6, legend_y - 0.1, label, fontsize=9, va='center', color='#1f2937')
    
    # Título
    fig.suptitle("Diagrama de Decisión: EDO de Primer Orden",
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
        fig.savefig(output_dir / "diagrama_decision_edo_primer_orden.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'diagrama_decision_edo_primer_orden.svg'}")
