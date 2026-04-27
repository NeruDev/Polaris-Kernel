# yaml_frontmatter:
#   id: 'triangulo_lineas_notables'
#   title: 'Las cuatro líneas notables del triángulo: mediana, altura, mediatriz, bisectriz'
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
    
    # Layout con GridSpec: 4 figuras arriba, info abajo
    fig = plt.figure(figsize=(14, 10), layout='constrained')
    gs = fig.add_gridspec(2, 4, height_ratios=[3, 1], hspace=0.15, wspace=0.1)
    
    axes = [fig.add_subplot(gs[0, i]) for i in range(4)]
    ax_info = fig.add_subplot(gs[1, :])
    
    # Triángulo base (mismo para todos)
    A = np.array([0, 0])
    B = np.array([6, 0])
    C = np.array([2, 4.5])
    vertices = [A, B, C]
    
    line_configs = [
        ('Mediana', colors['accent'], draw_median),
        ('Altura', colors['secondary'], draw_altura),
        ('Mediatriz', colors['tertiary'], draw_mediatriz),
        ('Bisectriz', '#f59e0b', draw_bisectriz),
    ]
    
    for ax, (title, color, draw_func) in zip(axes, line_configs):
        # Dibujar triángulo base
        triangle = plt.Polygon(vertices, fill=True,
                              facecolor=colors['primary'], alpha=0.1,
                              edgecolor=colors['primary'], linewidth=2)
        ax.add_patch(triangle)
        
        # Etiquetas de vértices (mínimas)
        ax.text(A[0] - 0.3, A[1] - 0.3, 'A', fontsize=11, fontweight='bold')
        ax.text(B[0] + 0.2, B[1] - 0.3, 'B', fontsize=11, fontweight='bold')
        ax.text(C[0] - 0.3, C[1] + 0.2, 'C', fontsize=11, fontweight='bold')
        
        # Dibujar línea notable específica
        draw_func(ax, A, B, C, color, minimal=True)
        
        # Configurar subplot
        ax.set_xlim(-1, 7)
        ax.set_ylim(-0.8, 5.5)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(title, fontsize=12, fontweight='bold', pad=8, color=color)
    
    # =========================================
    # PANEL INFERIOR: Información
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Línea separadora superior
    ax_info.axhline(y=0.95, xmin=0.02, xmax=0.98, color='#d1d5db', lw=1.5)
    
    # Tabla de definiciones (4 columnas)
    definitions = [
        ('Mediana', 'Une vértice con punto medio\ndel lado opuesto', 'Centroide (G)', colors['accent']),
        ('Altura', 'Perpendicular desde\nvértice al lado opuesto', 'Ortocentro (H)', colors['secondary']),
        ('Mediatriz', 'Perpendicular por el\npunto medio del lado', 'Circuncentro (O)', colors['tertiary']),
        ('Bisectriz', 'Divide el ángulo\nen dos partes iguales', 'Incentro (I)', '#f59e0b'),
    ]
    
    x_positions = [0.125, 0.375, 0.625, 0.875]
    for i, (name, defn, point, color) in enumerate(definitions):
        x = x_positions[i]
        ax_info.text(x, 0.82, name, fontsize=10, fontweight='bold', ha='center', color=color)
        ax_info.text(x, 0.55, defn, fontsize=8, ha='center', va='top', 
                    color='#4b5563', linespacing=1.3)
        ax_info.text(x, 0.18, point, fontsize=9, ha='center', 
                    color=color, fontweight='bold',
                    bbox=dict(facecolor='white', edgecolor=color, 
                             boxstyle='round,pad=0.2', linewidth=1))
    
    # Separadores verticales
    for x in [0.25, 0.5, 0.75]:
        ax_info.axvline(x=x, ymin=0.08, ymax=0.90, color='#e5e7eb', lw=1)
    
    # Título general
    fig.suptitle('Líneas Notables del Triángulo', fontsize=14, fontweight='bold')
    
    return fig


def draw_median(ax, A, B, C, color, minimal=False):
        M = (A + B) / 2  # Punto medio de AB
    
    ax.plot([C[0], M[0]], [C[1], M[1]], color=color, linewidth=2.5)
    ax.plot(*M, 'o', color=color, markersize=7)
    
    # Etiqueta del punto
    ax.text(M[0], M[1] - 0.4, 'M', fontsize=10, ha='center', color=color)
    
    if not minimal:
        ax.text(3, -0.8, 'Une vértice con punto\nmedio del lado opuesto',
                fontsize=10, ha='center', style='italic')
        ax.text(3, 5.3, 'Punto de concurrencia:\nCentroide (G)',
                fontsize=10, ha='center', color=color,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))


def draw_altura(ax, A, B, C, color, minimal=False):
        # Proyección de C sobre AB
    AB = B - A
    AC = C - A
    t = np.dot(AC, AB) / np.dot(AB, AB)
    H = A + t * AB
    
    ax.plot([C[0], H[0]], [C[1], H[1]], color=color, linewidth=2.5, linestyle='--')
    ax.plot(*H, 'o', color=color, markersize=7)
    
    # Ángulo recto
    size = 0.3
    AB_unit = AB / np.linalg.norm(AB)
    perp = np.array([-AB_unit[1], AB_unit[0]])
    
    ax.plot([H[0], H[0] + size * AB_unit[0]], 
            [H[1], H[1] + size * AB_unit[1]], color=color, linewidth=1.5)
    ax.plot([H[0] + size * AB_unit[0], H[0] + size * AB_unit[0] + size * perp[0]], 
            [H[1] + size * AB_unit[1], H[1] + size * AB_unit[1] + size * perp[1]], 
            color=color, linewidth=1.5)
    
    ax.text(H[0] + 0.3, H[1] - 0.3, 'H', fontsize=10, color=color)
    
    if not minimal:
        ax.text(3, -0.8, 'Perpendicular desde vértice\nal lado opuesto',
                fontsize=10, ha='center', style='italic')
        ax.text(3, 5.3, 'Punto de concurrencia:\nOrtocentro (H)',
                fontsize=10, ha='center', color=color,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))


def draw_mediatriz(ax, A, B, C, color, minimal=False):
        M = (A + B) / 2
    
    # Dirección perpendicular a AB
    AB = B - A
    perp = np.array([-AB[1], AB[0]])
    perp = perp / np.linalg.norm(perp)
    
    # Extender la mediatriz
    P1 = M - 2.0 * perp
    P2 = M + 2.0 * perp
    
    ax.plot([P1[0], P2[0]], [P1[1], P2[1]], color=color, linewidth=2.5)
    ax.plot(*M, 'o', color=color, markersize=7)
    
    # Marcas de igualdad en AM y MB
    mark_pos_1 = (A + M) / 2
    mark_pos_2 = (M + B) / 2
    mark_len = 0.12
    
    for pos in [mark_pos_1, mark_pos_2]:
        ax.plot([pos[0] - mark_len * perp[0], pos[0] + mark_len * perp[0]],
                [pos[1] - mark_len * perp[1], pos[1] + mark_len * perp[1]],
                color=color, linewidth=2)
    
    ax.text(M[0] + 0.3, M[1] - 0.3, 'M', fontsize=10, color=color)
    
    if not minimal:
        ax.text(3, -0.8, 'Perpendicular que pasa\npor punto medio del lado',
                fontsize=10, ha='center', style='italic')
        ax.text(3, 5.3, 'Punto de concurrencia:\nCircuncentro (O)',
                fontsize=10, ha='center', color=color,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))


def draw_bisectriz(ax, A, B, C, color, minimal=False):
        # Vectores desde C hacia A y B
    CA = A - C
    CB = B - C
    
    # Normalizar
    CA_unit = CA / np.linalg.norm(CA)
    CB_unit = CB / np.linalg.norm(CB)
    
    # Bisectriz es la suma de los vectores unitarios
    bisector_dir = CA_unit + CB_unit
    bisector_dir = bisector_dir / np.linalg.norm(bisector_dir)
    
    # Encontrar intersección con AB
    AB = B - A
    denom = bisector_dir[0] * AB[1] - bisector_dir[1] * AB[0]
    if abs(denom) > 1e-10:
        t = ((A[0] - C[0]) * AB[1] - (A[1] - C[1]) * AB[0]) / denom
        D = C + t * bisector_dir
    else:
        D = (A + B) / 2  # fallback
    
    ax.plot([C[0], D[0]], [C[1], D[1]], color=color, linewidth=2.5)
    ax.plot(*D, 'o', color=color, markersize=7)
    
    # Arcos para mostrar ángulos iguales
    arc_radius = 0.7
    angle_CA = np.degrees(np.arctan2(CA[1], CA[0]))
    angle_CB = np.degrees(np.arctan2(CB[1], CB[0]))
    angle_mid = np.degrees(np.arctan2(bisector_dir[1], bisector_dir[0]))
    
    arc1 = patches.Arc(C, 2*arc_radius, 2*arc_radius,
                       angle=0, theta1=min(angle_CA, angle_mid), 
                       theta2=max(angle_CA, angle_mid),
                       color=color, linewidth=1.5)
    arc2 = patches.Arc(C, 2*arc_radius, 2*arc_radius,
                       angle=0, theta1=min(angle_mid, angle_CB), 
                       theta2=max(angle_mid, angle_CB),
                       color=color, linewidth=1.5)
    ax.add_patch(arc1)
    ax.add_patch(arc2)
    
    ax.text(D[0] + 0.3, D[1] + 0.2, 'D', fontsize=10, color=color)
    
    if not minimal:
        ax.text(3, -0.8, 'Divide el ángulo\nen dos partes iguales',
                fontsize=10, ha='center', style='italic')
        ax.text(3, 5.3, 'Punto de concurrencia:\nIncentro (I)',
                fontsize=10, ha='center', color=color,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "triangulo_lineas_notables.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'triangulo_lineas_notables.svg'}")
