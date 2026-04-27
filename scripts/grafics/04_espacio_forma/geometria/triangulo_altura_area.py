# yaml_frontmatter:
#   id: 'triangulo_altura_area'
#   title: 'Triángulo con altura marcada ilustrando la fórmula del área'
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
    
    fig, ax = plt.subplots(figsize=(9, 7), layout='constrained')
    
    # Definir vértices del triángulo
    A = np.array([0, 0])
    B = np.array([7, 0])
    C = np.array([2.5, 5])
    
    # Calcular pie de la altura (proyección de C sobre AB)
    H = np.array([C[0], 0])
    
    # Dibujar triángulo con relleno suave
    triangle = plt.Polygon([A, B, C], 
                           fill=True, 
                           facecolor=colors['primary'],
                           edgecolor=colors['primary'],
                           alpha=0.15,
                           linewidth=2.5)
    ax.add_patch(triangle)
    
    # Borde del triángulo más visible
    ax.plot([A[0], B[0]], [A[1], B[1]], color=colors['primary'], linewidth=2.5)
    ax.plot([B[0], C[0]], [B[1], C[1]], color=colors['primary'], linewidth=2.5)
    ax.plot([C[0], A[0]], [C[1], A[1]], color=colors['primary'], linewidth=2.5)
    
    # Dibujar altura (línea punteada)
    ax.plot([C[0], H[0]], [C[1], H[1]], 
            color=colors['secondary'], linewidth=2, linestyle='--',
            label='Altura $h$')
    
    # Marcar ángulo recto
    right_angle_size = 0.35
    right_angle = patches.Rectangle(
        (H[0], H[1]), 
        right_angle_size, 
        right_angle_size,
        fill=False, 
        edgecolor=colors['secondary'],
        linewidth=1.5
    )
    ax.add_patch(right_angle)
    
    # Puntos en los vértices
    for point in [A, B, C, H]:
        ax.plot(point[0], point[1], 'o', color=colors['text'], markersize=7)
    
    # Etiquetas de vértices
    ax.text(A[0] - 0.4, A[1] - 0.4, '$A$', fontsize=15, fontweight='bold',
            color=colors['text'])
    ax.text(B[0] + 0.3, B[1] - 0.4, '$B$', fontsize=15, fontweight='bold',
            color=colors['text'])
    ax.text(C[0] - 0.4, C[1] + 0.3, '$C$', fontsize=15, fontweight='bold',
            color=colors['text'])
    ax.text(H[0] + 0.3, H[1] - 0.4, '$H$', fontsize=13,
            color=colors['secondary'])
    
    # Etiqueta de altura
    mid_height = (C + H) / 2
    ax.text(mid_height[0] + 0.35, mid_height[1], '$h$', 
            fontsize=16, fontweight='bold',
            color=colors['secondary'])
    
    # Etiqueta de base con llaves
    base_y = -0.8
    ax.annotate('', xy=(A[0], base_y), xytext=(B[0], base_y),
                arrowprops=dict(arrowstyle='<->', color=colors['primary'], lw=2))
    ax.text((A[0] + B[0]) / 2, base_y - 0.4, '$b$', 
            fontsize=16, fontweight='bold', ha='center',
            color=colors['primary'])
    
    # Fórmula destacada
    formula_box = dict(boxstyle='round,pad=0.5', 
                      facecolor=colors['accent'], 
                      alpha=0.2,
                      edgecolor=colors['accent'])
    ax.text(5.5, 4, '$A = \\frac{b \\cdot h}{2}$', 
            fontsize=20, fontweight='bold',
            bbox=formula_box,
            color=colors['text'])
    
    # Configurar ejes
    ax.set_xlim(-1.5, 9)
    ax.set_ylim(-2, 6.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Título
    ax.set_title('Área del Triángulo', 
                fontsize=16, fontweight='bold', pad=15)
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "triangulo_altura_area.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'triangulo_altura_area.svg'}")
