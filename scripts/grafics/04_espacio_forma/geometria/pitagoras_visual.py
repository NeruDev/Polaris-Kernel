# yaml_frontmatter:
#   id: 'pitagoras_visual'
#   title: 'Representación visual del teorema de Pitágoras con cuadrados'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria']

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

    setup_style,
    get_colors,
    get_output_dir_for_topic,
    save_figure,
)

# ============================================================
# Metadatos del Gráfico
# ============================================================


# ============================================================
# Función de Generación
# ============================================================

def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    # Layout con GridSpec: figura izquierda, info derecha
    fig = plt.figure(figsize=(14, 8), layout='constrained')
    gs = fig.add_gridspec(1, 2, width_ratios=[1.5, 1], wspace=0.08)
    
    ax = fig.add_subplot(gs[0])      # Panel izquierdo: figura
    ax_info = fig.add_subplot(gs[1]) # Panel derecho: información
    
    # =========================================
    # PANEL IZQUIERDO: Figura Geométrica
    # =========================================
    
    # Triángulo rectángulo 3-4-5 (escalado)
    scale = 1.5
    a, b = 3 * scale, 4 * scale  # catetos
    c = 5 * scale  # hipotenusa
    
    # Vértices del triángulo
    A = np.array([0, 0])  # Ángulo recto
    B = np.array([b, 0])  # Extremo del cateto b
    C = np.array([0, a])  # Extremo del cateto a
    
    # Dibujar el triángulo
    triangle = plt.Polygon([A, B, C], 
                           fill=True, 
                           facecolor=colors['text'],
                           edgecolor=colors['text'],
                           alpha=0.1,
                           linewidth=2)
    ax.add_patch(triangle)
    
    # Bordes del triángulo
    ax.plot([A[0], B[0]], [A[1], B[1]], color=colors['text'], linewidth=2.5)
    ax.plot([B[0], C[0]], [B[1], C[1]], color=colors['text'], linewidth=2.5)
    ax.plot([C[0], A[0]], [C[1], A[1]], color=colors['text'], linewidth=2.5)
    
    # Marcar ángulo recto
    right_angle_size = 0.4
    right_angle = patches.Rectangle(
        A, right_angle_size, right_angle_size,
        fill=False, edgecolor=colors['secondary'], linewidth=2
    )
    ax.add_patch(right_angle)
    
    # === Cuadrado sobre el cateto a (vertical, a la izquierda) ===
    sq_a_vertices = [
        A + np.array([-a, 0]),
        A,
        C,
        C + np.array([-a, 0]),
    ]
    sq_a = plt.Polygon(sq_a_vertices, 
                       fill=True, facecolor=colors['accent'],
                       edgecolor=colors['accent'], alpha=0.3, linewidth=2)
    ax.add_patch(sq_a)
    
    # Etiqueta del cuadrado a²
    sq_a_center = np.array([-a/2, a/2])
    ax.text(sq_a_center[0], sq_a_center[1], '$a^2$', 
            fontsize=18, fontweight='bold', ha='center', va='center',
            color=colors['accent'])
    
    # === Cuadrado sobre el cateto b (horizontal, abajo) ===
    sq_b_vertices = [
        A,
        B,
        B + np.array([0, -b]),
        A + np.array([0, -b]),
    ]
    sq_b = plt.Polygon(sq_b_vertices, 
                       fill=True, facecolor=colors['tertiary'],
                       edgecolor=colors['tertiary'], alpha=0.3, linewidth=2)
    ax.add_patch(sq_b)
    
    # Etiqueta del cuadrado b²
    sq_b_center = np.array([b/2, -b/2])
    ax.text(sq_b_center[0], sq_b_center[1], '$b^2$', 
            fontsize=18, fontweight='bold', ha='center', va='center',
            color=colors['tertiary'])
    
    # === Cuadrado sobre la hipotenusa c ===
    hyp_vec = B - C
    hyp_unit = hyp_vec / np.linalg.norm(hyp_vec)
    perp_unit = np.array([hyp_unit[1], -hyp_unit[0]])
    
    sq_c_vertices = [
        C,
        B,
        B + perp_unit * c,
        C + perp_unit * c,
    ]
    sq_c = plt.Polygon(sq_c_vertices, 
                       fill=True, facecolor=colors['secondary'],
                       edgecolor=colors['secondary'], alpha=0.3, linewidth=2)
    ax.add_patch(sq_c)
    
    # Etiqueta del cuadrado c²
    sq_c_center = (C + B) / 2 + perp_unit * c / 2
    ax.text(sq_c_center[0], sq_c_center[1], '$c^2$', 
            fontsize=18, fontweight='bold', ha='center', va='center',
            color=colors['secondary'])
    
    # === Etiquetas de los lados (mínimas) ===
    ax.text(-0.5, a/2, '$a$', fontsize=14, fontweight='bold',
            ha='center', va='center', color=colors['text'])
    ax.text(b/2, -0.5, '$b$', fontsize=14, fontweight='bold',
            ha='center', va='center', color=colors['text'])
    mid_hyp = (B + C) / 2
    ax.text(mid_hyp[0] + 0.4, mid_hyp[1] + 0.3, '$c$', 
            fontsize=14, fontweight='bold',
            ha='center', va='center', color=colors['text'])
    
    ax.set_xlim(-6, 10)
    ax.set_ylim(-7, 9)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # =========================================
    # PANEL DERECHO: Información
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # === Caja de Fórmula Principal (OBLIGATORIA) ===
    ax_info.add_patch(plt.Rectangle((0.05, 0.75), 0.9, 0.20, 
                                     facecolor='#fffbeb', edgecolor=colors['primary'],
                                     linewidth=2.5, transform=ax_info.transAxes))
    ax_info.text(0.5, 0.92, 'TEOREMA DE PITÁGORAS', fontsize=10, fontweight='bold',
                ha='center', va='center', color=colors['primary'])
    ax_info.text(0.5, 0.82, r'$c^2 = a^2 + b^2$', fontsize=24,
                ha='center', va='center', color=colors['primary'], fontweight='bold')
    
    # === Leyenda de Símbolos ===
    ax_info.axhline(y=0.70, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    ax_info.text(0.5, 0.66, 'Elementos', fontsize=10, fontweight='bold', ha='center', color='#374151')
    
    legend_items = [
        ('a', colors['accent'], 'cateto (lado menor)'),
        ('b', colors['tertiary'], 'cateto (lado mayor)'),
        ('c', colors['secondary'], 'hipotenusa (lado opuesto al ángulo recto)'),
    ]
    for i, (sym, col, desc) in enumerate(legend_items):
        y = 0.58 - i*0.08
        ax_info.text(0.08, y, sym, fontsize=13, fontweight='bold', color=col, va='center')
        ax_info.text(0.16, y, f'= {desc}', fontsize=9, color='#374151', va='center')
    
    # === Ejemplo Numérico ===
    ax_info.axhline(y=0.32, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    ax_info.text(0.5, 0.28, 'Ejemplo (terna pitagórica)', fontsize=10, fontweight='bold', 
                ha='center', color='#374151')
    
    ax_info.add_patch(plt.Rectangle((0.10, 0.12), 0.80, 0.12, 
                                     facecolor='#f0fdf4', edgecolor=colors['secondary'],
                                     linewidth=1, transform=ax_info.transAxes))
    ax_info.text(0.5, 0.18, r'$3^2 + 4^2 = 5^2$  →  $9 + 16 = 25$ ✓', fontsize=12,
                ha='center', va='center', color=colors['secondary'])
    
    # === Ternas Pitagóricas ===
    ax_info.axhline(y=0.08, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    ax_info.text(0.5, 0.04, 'Otras ternas: (5,12,13), (8,15,17), (7,24,25)', 
                fontsize=8, ha='center', va='center', color='#6b7280', style='italic')
    
    # Título general
    fig.suptitle('Teorema de Pitágoras — Demostración Visual', 
                fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "pitagoras_visual.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'pitagoras_visual.svg'}")
