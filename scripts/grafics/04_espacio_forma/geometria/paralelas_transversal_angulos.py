# yaml_frontmatter:
#   id: 'paralelas_transversal_angulos'
#   title: 'Dos rectas paralelas cortadas por una transversal mostrando ángulos'
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
    
    fig, ax = plt.subplots(figsize=(10, 7), layout='constrained')
    
    # Parámetros
    y1, y2 = 4, 1  # Posiciones de las paralelas
    x_min, x_max = 0, 8
    
    # Transversal: pasa por puntos específicos para crear ángulos
    # La transversal tiene pendiente negativa
    t_start = (1.5, 5.5)
    t_end = (6.5, -0.5)
    
    # Calcular intersecciones
    m = (t_end[1] - t_start[1]) / (t_end[0] - t_start[0])
    b = t_start[1] - m * t_start[0]
    
    x_int1 = (y1 - b) / m
    x_int2 = (y2 - b) / m
    
    int1 = (x_int1, y1)  # Intersección con ℓ₁
    int2 = (x_int2, y2)  # Intersección con ℓ₂
    
    # Dibujar rectas paralelas
    ax.plot([x_min, x_max], [y1, y1], color=colors['primary'], 
            linewidth=2.5, label='$\\ell_1$')
    ax.plot([x_min, x_max], [y2, y2], color=colors['primary'], 
            linewidth=2.5, label='$\\ell_2$')
    
    # Dibujar transversal
    ax.plot([t_start[0], t_end[0]], [t_start[1], t_end[1]], 
            color=colors['secondary'], linewidth=2.5)
    
    # Etiquetas de las rectas
    ax.text(x_max + 0.3, y1, '$\\ell_1$', fontsize=14, va='center',
            color=colors['primary'], fontweight='bold')
    ax.text(x_max + 0.3, y2, '$\\ell_2$', fontsize=14, va='center',
            color=colors['primary'], fontweight='bold')
    
    # Calcular ángulo de la transversal (en grados)
    angle_trans = np.degrees(np.arctan(m))  # Negativo porque m < 0
    
    # Dibujar arcos de ángulos
    arc_radius = 0.6
    
    # Ángulo 1: arriba a la izquierda de la intersección con ℓ₁
    # Este ángulo está entre la paralela (hacia la izquierda) y la transversal (hacia arriba)
    angle1_start = 180
    angle1_end = 180 + angle_trans  # angle_trans es negativo
    arc1 = patches.Arc(int1, 2*arc_radius, 2*arc_radius,
                       angle=0, theta1=angle1_end, theta2=angle1_start,
                       color=colors['accent'], linewidth=2)
    ax.add_patch(arc1)
    
    # Etiqueta ∠1
    mid_angle1 = np.radians((angle1_start + angle1_end) / 2)
    label1_pos = (int1[0] + arc_radius * 1.4 * np.cos(mid_angle1),
                  int1[1] + arc_radius * 1.4 * np.sin(mid_angle1))
    ax.text(label1_pos[0], label1_pos[1], '$\\angle 1$', fontsize=13,
            ha='center', va='center', color=colors['accent'], fontweight='bold')
    
    # Ángulo 2: abajo a la izquierda de la intersección con ℓ₂
    angle2_start = 180
    angle2_end = 180 - abs(angle_trans)
    arc2 = patches.Arc(int2, 2*arc_radius, 2*arc_radius,
                       angle=0, theta1=angle2_end, theta2=angle2_start,
                       color=colors['tertiary'], linewidth=2)
    ax.add_patch(arc2)
    
    # Etiqueta ∠2
    mid_angle2 = np.radians((angle2_start + angle2_end) / 2)
    label2_pos = (int2[0] + arc_radius * 1.4 * np.cos(mid_angle2),
                  int2[1] + arc_radius * 1.4 * np.sin(mid_angle2))
    ax.text(label2_pos[0], label2_pos[1], '$\\angle 2$', fontsize=13,
            ha='center', va='center', color=colors['tertiary'], fontweight='bold')
    
    # Ángulo 3: en el medio de la transversal
    # Este es el ángulo que la transversal forma, mostrado en un punto intermedio
    mid_trans = ((int1[0] + int2[0]) / 2, (int1[1] + int2[1]) / 2)
    
    # Dibujamos ∠3 como el ángulo en la intersección inferior, lado derecho
    angle3_start = -abs(angle_trans)
    angle3_end = 0
    arc3 = patches.Arc(int2, 2*arc_radius, 2*arc_radius,
                       angle=0, theta1=angle3_start, theta2=angle3_end,
                       color=colors['secondary'], linewidth=2)
    ax.add_patch(arc3)
    
    # Etiqueta ∠3
    mid_angle3 = np.radians((angle3_start + angle3_end) / 2)
    label3_pos = (int2[0] + arc_radius * 1.5 * np.cos(mid_angle3),
                  int2[1] + arc_radius * 1.5 * np.sin(mid_angle3))
    ax.text(label3_pos[0], label3_pos[1], '$\\angle 3$', fontsize=13,
            ha='center', va='center', color=colors['secondary'], fontweight='bold')
    
    # Marcar puntos de intersección
    ax.plot(*int1, 'o', color=colors['text'], markersize=6)
    ax.plot(*int2, 'o', color=colors['text'], markersize=6)
    
    # Flechas de paralelismo
    arrow_y_offset = 0.15
    for y in [y1, y2]:
        ax.annotate('', xy=(4.5, y + arrow_y_offset), xytext=(4.0, y + arrow_y_offset),
                   arrowprops=dict(arrowstyle='->', color=colors['primary'], lw=1.5))
        ax.annotate('', xy=(4.8, y - arrow_y_offset), xytext=(4.3, y - arrow_y_offset),
                   arrowprops=dict(arrowstyle='->', color=colors['primary'], lw=1.5))
    
    # Información adicional
    info_text = (
        "Dado: $\\ell_1 \\parallel \\ell_2$\n"
        "$\\angle 1 = 65°$, $\\angle 2 = 40°$\n"
        "Hallar: $\\angle 3$"
    )
    ax.text(0.5, 5.3, info_text, fontsize=11,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
            verticalalignment='top')
    
    # Configurar ejes
    ax.set_xlim(-0.5, 9)
    ax.set_ylim(-1, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Título
    ax.set_title('Paralelas cortadas por una transversal', 
                fontsize=14, fontweight='bold', pad=15)
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "paralelas_transversal_angulos.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'paralelas_transversal_angulos.svg'}")
