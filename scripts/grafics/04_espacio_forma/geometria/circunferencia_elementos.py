# yaml_frontmatter:
#   id: 'circunferencia_elementos'
#   title: 'Elementos principales de la circunferencia: radio, diámetro, cuerda, tangente'
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
    
    fig, ax = plt.subplots(figsize=(11, 10), layout='constrained')
    
    # Parámetros de la circunferencia
    center = np.array([5, 5])
    radius = 3.5
    
    # Dibujar circunferencia
    circle = patches.Circle(center, radius,
                           fill=False,
                           edgecolor=colors['primary'],
                           linewidth=2.5)
    ax.add_patch(circle)
    
    # Marcar centro
    ax.plot(*center, 'o', color=colors['text'], markersize=8)
    ax.text(center[0] + 0.2, center[1] + 0.2, '$O$', fontsize=14, fontweight='bold')
    
    # === RADIO ===
    angle_r = 45
    P_radius = center + radius * np.array([np.cos(np.radians(angle_r)), 
                                            np.sin(np.radians(angle_r))])
    ax.plot([center[0], P_radius[0]], [center[1], P_radius[1]], 
            color=colors['secondary'], linewidth=2.5)
    ax.plot(*P_radius, 'o', color=colors['secondary'], markersize=6)
    
    # Etiqueta radio
    mid_r = (center + P_radius) / 2
    ax.text(mid_r[0] + 0.2, mid_r[1] + 0.3, '$r$', 
            fontsize=15, fontweight='bold', color=colors['secondary'])
    ax.text(P_radius[0] + 0.2, P_radius[1] + 0.2, '$P$', fontsize=12)
    
    # === DIÁMETRO ===
    angle_d = 160
    P1_diam = center + radius * np.array([np.cos(np.radians(angle_d)), 
                                           np.sin(np.radians(angle_d))])
    P2_diam = center - radius * np.array([np.cos(np.radians(angle_d)), 
                                           np.sin(np.radians(angle_d))])
    ax.plot([P1_diam[0], P2_diam[0]], [P1_diam[1], P2_diam[1]], 
            color=colors['accent'], linewidth=2.5)
    ax.plot(*P1_diam, 'o', color=colors['accent'], markersize=6)
    ax.plot(*P2_diam, 'o', color=colors['accent'], markersize=6)
    
    # Etiqueta diámetro
    ax.text(P1_diam[0] - 0.4, P1_diam[1] + 0.2, '$A$', fontsize=12)
    ax.text(P2_diam[0] + 0.2, P2_diam[1] - 0.3, '$B$', fontsize=12)
    ax.text(center[0] - 0.8, center[1] - 0.6, '$d = 2r$', 
            fontsize=13, color=colors['accent'], fontweight='bold')
    
    # === CUERDA ===
    angle_c1, angle_c2 = 200, 280
    C1 = center + radius * np.array([np.cos(np.radians(angle_c1)), 
                                      np.sin(np.radians(angle_c1))])
    C2 = center + radius * np.array([np.cos(np.radians(angle_c2)), 
                                      np.sin(np.radians(angle_c2))])
    ax.plot([C1[0], C2[0]], [C1[1], C2[1]], 
            color=colors['tertiary'], linewidth=2.5)
    ax.plot(*C1, 'o', color=colors['tertiary'], markersize=6)
    ax.plot(*C2, 'o', color=colors['tertiary'], markersize=6)
    
    # Etiqueta cuerda
    mid_c = (C1 + C2) / 2
    ax.text(mid_c[0] - 0.5, mid_c[1] - 0.3, 'cuerda', 
            fontsize=12, color=colors['tertiary'], fontweight='bold')
    ax.text(C1[0] - 0.4, C1[1], '$C$', fontsize=12)
    ax.text(C2[0] + 0.2, C2[1] - 0.3, '$D$', fontsize=12)
    
    # === ARCO ===
    arc_start, arc_end = 45, 120
    arc = patches.Arc(center, 2*radius, 2*radius,
                     angle=0, theta1=arc_start, theta2=arc_end,
                     color=colors['secondary'], linewidth=4, linestyle='-')
    ax.add_patch(arc)
    
    # Etiqueta arco
    arc_mid_angle = np.radians((arc_start + arc_end) / 2)
    arc_label_pos = center + (radius + 0.5) * np.array([np.cos(arc_mid_angle), 
                                                         np.sin(arc_mid_angle)])
    ax.text(arc_label_pos[0], arc_label_pos[1], 'arco', 
            fontsize=12, color=colors['secondary'], fontweight='bold', ha='center')
    
    # === TANGENTE ===
    angle_t = 0  # Punto de tangencia
    T = center + radius * np.array([np.cos(np.radians(angle_t)), 
                                     np.sin(np.radians(angle_t))])
    # Tangente es perpendicular al radio
    tang_dir = np.array([0, 1])  # Perpendicular a [1, 0]
    tang_len = 2.5
    T1 = T - tang_len * tang_dir
    T2 = T + tang_len * tang_dir
    
    ax.plot([T1[0], T2[0]], [T1[1], T2[1]], 
            color='#f59e0b', linewidth=2.5)  # Naranja
    ax.plot(*T, 'o', color='#f59e0b', markersize=8)
    
    # Marcar ángulo recto
    right_size = 0.25
    ax.plot([T[0] - right_size, T[0] - right_size], 
            [T[1], T[1] + right_size], color='#f59e0b', linewidth=1.5)
    ax.plot([T[0] - right_size, T[0]], 
            [T[1] + right_size, T[1] + right_size], color='#f59e0b', linewidth=1.5)
    
    # Etiqueta tangente
    ax.text(T2[0] + 0.2, T2[1], 'tangente', 
            fontsize=12, color='#f59e0b', fontweight='bold')
    ax.text(T[0] + 0.2, T[1] - 0.4, '$T$', fontsize=12)
    
    # === SECANTE ===
    sec_angle = 30
    sec_dir = np.array([np.cos(np.radians(sec_angle)), np.sin(np.radians(sec_angle))])
    # Punto exterior
    ext_point = center + (radius + 2) * sec_dir
    # Calcular intersecciones con la circunferencia
    # Simplificado: usamos dos puntos conocidos
    S1_angle, S2_angle = 10, 50
    S1 = center + radius * np.array([np.cos(np.radians(S1_angle)), 
                                      np.sin(np.radians(S1_angle))])
    S2 = center + radius * np.array([np.cos(np.radians(S2_angle)), 
                                      np.sin(np.radians(S2_angle))])
    
    # Extender la línea
    direction = S2 - S1
    direction = direction / np.linalg.norm(direction)
    line_start = S1 - 1.5 * direction
    line_end = S2 + 2 * direction
    
    ax.plot([line_start[0], line_end[0]], [line_start[1], line_end[1]], 
            color='#06b6d4', linewidth=2, linestyle='--')  # Cyan
    ax.plot(*S1, 'o', color='#06b6d4', markersize=6)
    ax.plot(*S2, 'o', color='#06b6d4', markersize=6)
    
    # Etiqueta secante
    ax.text(line_end[0] + 0.2, line_end[1], 'secante', 
            fontsize=12, color='#06b6d4', fontweight='bold')
    
    # === LEYENDA ===
    legend_items = [
        (colors['secondary'], 'Radio ($r$)'),
        (colors['accent'], 'Diámetro ($d = 2r$)'),
        (colors['tertiary'], 'Cuerda'),
        ('#f59e0b', 'Tangente'),
        ('#06b6d4', 'Secante'),
    ]
    
    legend_y = 9.5
    for i, (color, label) in enumerate(legend_items):
        x = 0.5 + (i % 3) * 3.5
        y = legend_y - (i // 3) * 0.6
        ax.plot([x, x + 0.4], [y, y], color=color, linewidth=3)
        ax.text(x + 0.6, y, label, fontsize=11, va='center')
    
    # Configurar ejes
    ax.set_xlim(-0.5, 11)
    ax.set_ylim(0, 10.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Título
    ax.set_title('Elementos de la Circunferencia', 
                fontsize=16, fontweight='bold', pad=15)
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "circunferencia_elementos.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'circunferencia_elementos.svg'}")
