# yaml_frontmatter:
#   id: 'distancia_punto_medio'
#   title: 'Fórmulas de distancia entre puntos y punto medio'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria_analitica']

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[3]))
from templates import setup_style, get_colors
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


    setup_style,
    get_colors,
    get_output_dir_for_topic,
    save_figure,
)


def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig = plt.figure(figsize=(14, 8), layout='constrained')
    gs = fig.add_gridspec(1, 2, width_ratios=[1.2, 1], wspace=0.1)
    
    ax_graph = fig.add_subplot(gs[0])
    ax_info = fig.add_subplot(gs[1])
    
    # =========================================
    # PANEL IZQUIERDO: Gráfica
    # =========================================
    
    # Puntos
    P1 = np.array([1, 1])
    P2 = np.array([6, 5])
    M = (P1 + P2) / 2  # Punto medio
    
    # Cuadrícula
    ax_graph.grid(True, linestyle='--', alpha=0.3, color='#9ca3af')
    ax_graph.axhline(y=0, color='#9ca3af', linewidth=1)
    ax_graph.axvline(x=0, color='#9ca3af', linewidth=1)
    
    # Segmento P1P2
    ax_graph.plot([P1[0], P2[0]], [P1[1], P2[1]], color=colors['primary'], 
                 linewidth=3, zorder=3)
    
    # Triángulo rectángulo (para mostrar Pitágoras)
    ax_graph.plot([P1[0], P2[0]], [P1[1], P1[1]], '--', color=colors['tertiary'], 
                 linewidth=2, zorder=2)
    ax_graph.plot([P2[0], P2[0]], [P1[1], P2[1]], '--', color=colors['secondary'], 
                 linewidth=2, zorder=2)
    
    # Puntos
    ax_graph.plot(*P1, 'o', color=colors['primary'], markersize=12, zorder=5)
    ax_graph.plot(*P2, 'o', color=colors['primary'], markersize=12, zorder=5)
    ax_graph.plot(*M, 's', color='#f59e0b', markersize=12, zorder=5)
    
    # Etiquetas de puntos
    ax_graph.text(P1[0] - 0.4, P1[1] + 0.4, r'$P_1(x_1, y_1)$', fontsize=11,
                 fontweight='bold', color=colors['primary'])
    ax_graph.text(P2[0] + 0.2, P2[1] + 0.3, r'$P_2(x_2, y_2)$', fontsize=11,
                 fontweight='bold', color=colors['primary'])
    ax_graph.text(M[0] + 0.2, M[1] + 0.4, 'M (punto medio)', fontsize=10,
                 fontweight='bold', color='#f59e0b')
    
    # Etiquetas de distancias
    ax_graph.text((P1[0] + P2[0])/2, P1[1] - 0.5, r'$\Delta x = x_2 - x_1$', 
                 fontsize=10, ha='center', color=colors['tertiary'])
    ax_graph.text(P2[0] + 0.3, (P1[1] + P2[1])/2, r'$\Delta y = y_2 - y_1$',
                 fontsize=10, color=colors['secondary'])
    ax_graph.text((P1[0] + P2[0])/2 - 0.8, (P1[1] + P2[1])/2 + 0.4, 'd',
                 fontsize=14, fontweight='bold', color=colors['primary'])
    
    # Ángulo recto
    sq_size = 0.3
    ax_graph.plot([P2[0]-sq_size, P2[0]-sq_size, P2[0]], 
                 [P1[1], P1[1]+sq_size, P1[1]+sq_size],
                 color='#6b7280', linewidth=1)
    
    # Proyecciones a los ejes
    ax_graph.plot([P1[0], P1[0]], [0, P1[1]], ':', color='#d1d5db', linewidth=1)
    ax_graph.plot([0, P1[0]], [P1[1], P1[1]], ':', color='#d1d5db', linewidth=1)
    ax_graph.plot([P2[0], P2[0]], [0, P2[1]], ':', color='#d1d5db', linewidth=1)
    ax_graph.plot([0, P2[0]], [P2[1], P2[1]], ':', color='#d1d5db', linewidth=1)
    
    ax_graph.set_xlim(-0.5, 8)
    ax_graph.set_ylim(-0.5, 7)
    ax_graph.set_aspect('equal')
    ax_graph.set_xlabel('x', fontsize=11)
    ax_graph.set_ylabel('y', fontsize=11)
    ax_graph.set_title('Distancia y Punto Medio', fontsize=11, fontweight='bold')
    
    # =========================================
    # PANEL DERECHO: Fórmulas
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Fórmula de distancia
    ax_info.add_patch(plt.Rectangle((0.03, 0.62), 0.94, 0.35,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=2))
    ax_info.text(0.5, 0.92, 'DISTANCIA ENTRE DOS PUNTOS', fontsize=11,
                fontweight='bold', ha='center', color=colors['primary'])
    
    ax_info.text(0.5, 0.8, r'$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$',
                fontsize=14, ha='center', color=colors['text'])
    
    ax_info.text(0.5, 0.68, 'Derivada del Teorema de Pitágoras:',
                fontsize=9, ha='center', color='#6b7280', style='italic')
    ax_info.text(0.5, 0.64, r'$d^2 = (\Delta x)^2 + (\Delta y)^2$',
                fontsize=10, ha='center', color='#6b7280')
    
    # Fórmula de punto medio
    ax_info.add_patch(plt.Rectangle((0.03, 0.28), 0.94, 0.3,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=2))
    ax_info.text(0.5, 0.53, 'PUNTO MEDIO', fontsize=11,
                fontweight='bold', ha='center', color='#f59e0b')
    
    ax_info.text(0.5, 0.42, r'$M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$',
                fontsize=14, ha='center', color=colors['text'])
    
    ax_info.text(0.5, 0.32, 'El promedio de las coordenadas',
                fontsize=9, ha='center', color='#6b7280', style='italic')
    
    # Ejemplo numérico
    ax_info.add_patch(plt.Rectangle((0.03, 0.03), 0.94, 0.22,
                                    facecolor='#f0fdf4', edgecolor=colors['accent'],
                                    linewidth=1.5))
    ax_info.text(0.5, 0.21, 'Ejemplo: P₁(1,1) y P₂(6,5)', fontsize=10,
                fontweight='bold', ha='center', color=colors['accent'])
    
    ax_info.text(0.5, 0.13, r'$d = \sqrt{(6-1)^2 + (5-1)^2} = \sqrt{25+16} = \sqrt{41}$',
                fontsize=9, ha='center', color='#374151')
    ax_info.text(0.5, 0.06, r'$M = \left(\frac{1+6}{2}, \frac{1+5}{2}\right) = (3.5, 3)$',
                fontsize=9, ha='center', color='#374151')
    
    fig.suptitle('Fórmulas Fundamentales de Geometría Analítica', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "distancia_punto_medio.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'distancia_punto_medio.svg'}")
