# yaml_frontmatter:
#   id: 'semejanza_criterios'
#   title: 'Criterios de semejanza: AA, LAL, LLL'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria']

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[3]))
from templates import setup_style, get_colors
import matplotlib.pyplot as plt
import numpy as np
def draw_similar_triangles(ax, tri1, tri2, marks_config, colors_dict):
        
    # Triángulo 1 (más pequeño)
    t1 = plt.Polygon(tri1, fill=True, facecolor=colors_dict['primary'],
                     alpha=0.15, edgecolor=colors_dict['primary'], linewidth=2.5)
    ax.add_patch(t1)
    
    # Triángulo 2 (más grande)
    t2 = plt.Polygon(tri2, fill=True, facecolor=colors_dict['secondary'],
                     alpha=0.15, edgecolor=colors_dict['secondary'], linewidth=2.5)
    ax.add_patch(t2)
    
    # Vértices (solo puntos, etiquetas en leyenda)
    for v in tri1:
        ax.plot(v[0], v[1], 'o', color=colors_dict['primary'], markersize=6)
    
    for v in tri2:
        ax.plot(v[0], v[1], 'o', color=colors_dict['secondary'], markersize=6)
    
    # Marcas de ángulos iguales
    for i, highlight in enumerate(marks_config.get('angles', [])):
        if highlight:
            for tri, r in [(tri1, 0.18), (tri2, 0.25)]:
                vertex = np.array(tri[i])
                p1 = np.array(tri[(i-1) % 3])
                p2 = np.array(tri[(i+1) % 3])
                
                v1 = p1 - vertex
                v2 = p2 - vertex
                a1 = np.arctan2(v1[1], v1[0])
                a2 = np.arctan2(v2[1], v2[0])
                if a2 < a1:
                    a2 += 2 * np.pi
                
                arc = np.linspace(a1, a2, 20)
                ax.plot(vertex[0] + r*np.cos(arc), vertex[1] + r*np.sin(arc),
                       color=colors_dict['accent'], lw=2)
    
    # Símbolo de semejanza (centrado entre triángulos)
    ax.text(1.6, 0.7, '~', fontsize=26, ha='center', va='center', 
            color=colors_dict['tertiary'], fontweight='bold')

def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    # Crear figura con GridSpec: 2 filas (3 figuras arriba | leyenda abajo)
    fig = plt.figure(figsize=(13, 7), layout='constrained')
    gs = fig.add_gridspec(2, 3, height_ratios=[2.5, 1], hspace=0.12, wspace=0.15)
    
    ax_aa = fig.add_subplot(gs[0, 0])
    ax_lal = fig.add_subplot(gs[0, 1])
    ax_lll = fig.add_subplot(gs[0, 2])
    ax_info = fig.add_subplot(gs[1, :])  # Panel inferior completo
    
    # Triángulos base (escalados para mejor visualización)
    tri1_base = [(0, 0), (1.4, 0), (0.5, 1.1)]
    tri2_base = [(2.2, 0), (4.2, 0), (2.9, 1.6)]
    
    # =========================================
    # PANEL AA (Ángulo-Ángulo)
    # =========================================
    config_aa = {'angles': [True, True, False]}
    draw_similar_triangles(ax_aa, tri1_base, tri2_base, config_aa, colors)
    ax_aa.set_xlim(-0.4, 4.6)
    ax_aa.set_ylim(-0.3, 2.0)
    ax_aa.set_aspect('equal')
    ax_aa.axis('off')
    ax_aa.set_title('AA', fontsize=13, fontweight='bold', color=colors['primary'])
    
    # =========================================
    # PANEL LAL (Lado-Ángulo-Lado)
    # =========================================
    config_lal = {'angles': [True, False, False]}
    draw_similar_triangles(ax_lal, tri1_base, tri2_base, config_lal, colors)
    # Marcas de proporcionalidad en lados (simples)
    ax_lal.plot([0.25, 0.25], [0.5, 0.6], color=colors['accent'], lw=2)  # Lado izq tri1
    ax_lal.plot([0.95, 0.95], [0.5, 0.6], color=colors['accent'], lw=2)  # Lado der tri1
    ax_lal.plot([2.55, 2.55], [0.7, 0.85], color=colors['accent'], lw=2)  # Lado izq tri2
    ax_lal.plot([2.56, 2.56], [0.72, 0.87], color=colors['accent'], lw=2)
    ax_lal.plot([3.55, 3.55], [0.7, 0.85], color=colors['accent'], lw=2)  # Lado der tri2
    ax_lal.plot([3.56, 3.56], [0.72, 0.87], color=colors['accent'], lw=2)
    ax_lal.set_xlim(-0.4, 4.6)
    ax_lal.set_ylim(-0.3, 2.0)
    ax_lal.set_aspect('equal')
    ax_lal.axis('off')
    ax_lal.set_title('LAL', fontsize=13, fontweight='bold', color=colors['primary'])
    
    # =========================================
    # PANEL LLL (Lado-Lado-Lado)
    # =========================================
    config_lll = {'angles': [False, False, False]}
    draw_similar_triangles(ax_lll, tri1_base, tri2_base, config_lll, colors)
    # Marcas de proporcionalidad en todos los lados (1, 2, 3 marcas)
    # Triángulo 1
    ax_lll.plot([0.7, 0.7], [-0.08, 0.02], color=colors['primary'], lw=2)  # Base: 1 marca
    ax_lll.plot([0.95, 1.0], [0.5, 0.55], color=colors['primary'], lw=2)   # Lado der: 2
    ax_lll.plot([0.9, 0.95], [0.52, 0.57], color=colors['primary'], lw=2)
    ax_lll.plot([0.2, 0.25], [0.5, 0.55], color=colors['primary'], lw=2)   # Lado izq: 3
    ax_lll.plot([0.22, 0.27], [0.52, 0.57], color=colors['primary'], lw=2)
    ax_lll.plot([0.24, 0.29], [0.54, 0.59], color=colors['primary'], lw=2)
    # Triángulo 2 (mismas marcas pero más separadas)
    ax_lll.plot([3.2, 3.2], [-0.08, 0.02], color=colors['secondary'], lw=2)
    ax_lll.plot([3.6, 3.65], [0.7, 0.78], color=colors['secondary'], lw=2)
    ax_lll.plot([3.55, 3.60], [0.72, 0.80], color=colors['secondary'], lw=2)
    ax_lll.plot([2.5, 2.55], [0.7, 0.78], color=colors['secondary'], lw=2)
    ax_lll.plot([2.52, 2.57], [0.72, 0.80], color=colors['secondary'], lw=2)
    ax_lll.plot([2.54, 2.59], [0.74, 0.82], color=colors['secondary'], lw=2)
    ax_lll.set_xlim(-0.4, 4.6)
    ax_lll.set_ylim(-0.3, 2.0)
    ax_lll.set_aspect('equal')
    ax_lll.axis('off')
    ax_lll.set_title('LLL', fontsize=13, fontweight='bold', color=colors['primary'])
    
    # =========================================
    # PANEL INFERIOR: Descripciones y Leyenda
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Línea separadora superior
    ax_info.axhline(y=0.95, xmin=0.02, xmax=0.98, color='#d1d5db', lw=1.5)
    
    # Descripciones de cada criterio (3 columnas)
    criteria = [
        ('AA', 'Ángulo-Ángulo', 
         'Dos triángulos son semejantes si\ntienen dos ángulos iguales.'),
        ('LAL', 'Lado-Ángulo-Lado', 
         'Dos triángulos son semejantes si\ntienen dos lados proporcionales\ny el ángulo comprendido igual.'),
        ('LLL', 'Lado-Lado-Lado', 
         'Dos triángulos son semejantes si\ntienen los tres lados proporcionales.'),
    ]
    
    x_positions = [0.17, 0.5, 0.83]
    for i, (abbr, name, desc) in enumerate(criteria):
        x = x_positions[i]
        ax_info.text(x, 0.82, abbr, fontsize=12, fontweight='bold', ha='center',
                    color=colors['tertiary'])
        ax_info.text(x, 0.68, name, fontsize=10, ha='center', color='#374151')
        ax_info.text(x, 0.50, desc, fontsize=9, ha='center', va='top',
                    color='#6b7280', linespacing=1.3)
    
    # Separadores verticales
    ax_info.axvline(x=0.33, ymin=0.1, ymax=0.9, color='#e5e7eb', lw=1)
    ax_info.axvline(x=0.67, ymin=0.1, ymax=0.9, color='#e5e7eb', lw=1)
    
    # Leyenda de colores en la parte inferior
    ax_info.text(0.5, 0.12, 'Leyenda:', fontsize=9, fontweight='bold', ha='center', color='#374151')
    ax_info.plot([0.35, 0.38], [0.05, 0.05], color=colors['primary'], lw=4)
    ax_info.text(0.39, 0.05, 'Triángulo pequeño', fontsize=8, va='center')
    ax_info.plot([0.58, 0.61], [0.05, 0.05], color=colors['secondary'], lw=4)
    ax_info.text(0.62, 0.05, 'Triángulo grande', fontsize=8, va='center')
    
    # Título general
    fig.suptitle('Criterios de Semejanza de Triángulos', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "semejanza_criterios.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'semejanza_criterios.svg'}")
