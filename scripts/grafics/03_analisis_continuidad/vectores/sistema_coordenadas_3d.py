# yaml_frontmatter:
#   id: 'sistema_coordenadas_3d'
#   title: 'Sistema de coordenadas cartesianas 3D con vectores canónicos i, j, k'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'vectores']

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[3]))
from templates import setup_style, get_colors
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from mpl_toolkits.mplot3d import Axes3D

    setup_style,
    get_colors,
    get_output_dir_for_topic,
    save_figure,
)


def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig = plt.figure(figsize=(14, 7), layout='constrained')
    gs = fig.add_gridspec(1, 2, width_ratios=[1.4, 1], wspace=0.08)
    
    ax_3d = fig.add_subplot(gs[0], projection='3d')
    ax_info = fig.add_subplot(gs[1])
    
    # =========================================
    # PANEL 3D: Sistema de coordenadas
    # =========================================
    origin = np.array([0, 0, 0])
    
    # Ejes coordenados (extendidos)
    ax_length = 3
    ax_3d.quiver(*origin, ax_length, 0, 0, color='#9ca3af', arrow_length_ratio=0.08, linewidth=1.5)
    ax_3d.quiver(*origin, 0, ax_length, 0, color='#9ca3af', arrow_length_ratio=0.08, linewidth=1.5)
    ax_3d.quiver(*origin, 0, 0, ax_length, color='#9ca3af', arrow_length_ratio=0.08, linewidth=1.5)
    
    # Vectores canónicos i, j, k
    ax_3d.quiver(*origin, 1, 0, 0, color='#dc2626', arrow_length_ratio=0.15, linewidth=3)
    ax_3d.quiver(*origin, 0, 1, 0, color='#10b981', arrow_length_ratio=0.15, linewidth=3)
    ax_3d.quiver(*origin, 0, 0, 1, color='#3b82f6', arrow_length_ratio=0.15, linewidth=3)
    
    # Etiquetas de vectores canónicos
    ax_3d.text(1.2, 0, 0.1, r'$\mathbf{i}$', fontsize=14, color='#dc2626', fontweight='bold')
    ax_3d.text(0.1, 1.2, 0, r'$\mathbf{j}$', fontsize=14, color='#10b981', fontweight='bold')
    ax_3d.text(0.1, 0, 1.2, r'$\mathbf{k}$', fontsize=14, color='#3b82f6', fontweight='bold')
    
    # Etiquetas de ejes
    ax_3d.text(ax_length + 0.2, 0, 0, 'X', fontsize=12, color='#374151')
    ax_3d.text(0, ax_length + 0.2, 0, 'Y', fontsize=12, color='#374151')
    ax_3d.text(0, 0, ax_length + 0.2, 'Z', fontsize=12, color='#374151')
    
    # Punto ejemplo P(2, 1.5, 2)
    P = np.array([2, 1.5, 2])
    ax_3d.scatter(*P, color=colors['accent'], s=100, zorder=5)
    ax_3d.text(P[0]+0.15, P[1]+0.15, P[2]+0.2, r'$P(2, 1.5, 2)$', fontsize=10, color=colors['accent'])
    
    # Vector posición OP
    ax_3d.quiver(*origin, *P, color=colors['accent'], arrow_length_ratio=0.05, linewidth=2.5)
    
    # Proyecciones (líneas discontinuas)
    ax_3d.plot([P[0], P[0]], [P[1], P[1]], [0, P[2]], '--', color='#9ca3af', linewidth=1, alpha=0.7)
    ax_3d.plot([P[0], P[0]], [0, P[1]], [0, 0], '--', color='#9ca3af', linewidth=1, alpha=0.7)
    ax_3d.plot([0, P[0]], [P[1], P[1]], [0, 0], '--', color='#9ca3af', linewidth=1, alpha=0.7)
    ax_3d.plot([P[0], P[0]], [P[1], P[1]], [0, 0], '--', color='#9ca3af', linewidth=1, alpha=0.7)
    ax_3d.plot([0, P[0]], [0, 0], [0, 0], '--', color='#dc2626', linewidth=1.5, alpha=0.7)
    ax_3d.plot([P[0], P[0]], [0, P[1]], [0, 0], '--', color='#10b981', linewidth=1.5, alpha=0.7)
    ax_3d.plot([P[0], P[0]], [P[1], P[1]], [0, P[2]], '--', color='#3b82f6', linewidth=1.5, alpha=0.7)
    
    # Origen
    ax_3d.scatter(*origin, color='#374151', s=60, zorder=5)
    ax_3d.text(-0.3, -0.3, -0.2, 'O', fontsize=11, color='#374151')
    
    # Configuración del gráfico 3D
    ax_3d.set_xlim([0, 3])
    ax_3d.set_ylim([0, 3])
    ax_3d.set_zlim([0, 3])
    ax_3d.set_box_aspect([1, 1, 1])
    ax_3d.view_init(elev=20, azim=45)
    
    # Limpiar paneles
    ax_3d.xaxis.pane.fill = False
    ax_3d.yaxis.pane.fill = False
    ax_3d.zaxis.pane.fill = False
    ax_3d.xaxis.pane.set_edgecolor('#e5e7eb')
    ax_3d.yaxis.pane.set_edgecolor('#e5e7eb')
    ax_3d.zaxis.pane.set_edgecolor('#e5e7eb')
    
    ax_3d.set_title('Sistema de Coordenadas en $\\mathbb{R}^3$', fontsize=11, fontweight='bold', pad=10)
    
    # =========================================
    # PANEL INFO: Fórmulas y definiciones
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Caja de fórmula principal
    ax_info.add_patch(plt.Rectangle((0.03, 0.78), 0.94, 0.18,
                                    facecolor='#fffbeb', edgecolor=colors['tertiary'],
                                    linewidth=2))
    ax_info.text(0.5, 0.92, 'VECTORES CANÓNICOS', fontsize=10,
                fontweight='bold', ha='center', color=colors['tertiary'])
    ax_info.text(0.5, 0.84, r'$\mathbf{i} = \langle 1,0,0 \rangle$  •  $\mathbf{j} = \langle 0,1,0 \rangle$  •  $\mathbf{k} = \langle 0,0,1 \rangle$',
                fontsize=11, ha='center', color=colors['text'])
    
    ax_info.axhline(y=0.74, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    
    # Vector posición
    ax_info.text(0.5, 0.68, 'Vector Posición', fontsize=10, fontweight='bold', ha='center', color=colors['primary'])
    ax_info.text(0.5, 0.60, r'$\overrightarrow{OP} = \langle x, y, z \rangle = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$',
                fontsize=12, ha='center', color=colors['text'])
    
    ax_info.axhline(y=0.54, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    
    # Magnitud
    ax_info.text(0.5, 0.48, 'Magnitud (Norma)', fontsize=10, fontweight='bold', ha='center', color=colors['secondary'])
    ax_info.text(0.5, 0.40, r'$\|\mathbf{v}\| = \sqrt{v_x^2 + v_y^2 + v_z^2}$',
                fontsize=13, ha='center', color=colors['text'])
    
    ax_info.axhline(y=0.34, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    
    # Vector unitario
    ax_info.text(0.5, 0.28, 'Vector Unitario', fontsize=10, fontweight='bold', ha='center', color='#f59e0b')
    ax_info.text(0.5, 0.20, r'$\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}$',
                fontsize=13, ha='center', color=colors['text'])
    
    ax_info.axhline(y=0.14, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    
    # Leyenda de colores
    ax_info.plot([0.1], [0.08], 's', color='#dc2626', markersize=10)
    ax_info.text(0.15, 0.08, r'$\mathbf{i}$ (eje X)', fontsize=9, va='center')
    ax_info.plot([0.4], [0.08], 's', color='#10b981', markersize=10)
    ax_info.text(0.45, 0.08, r'$\mathbf{j}$ (eje Y)', fontsize=9, va='center')
    ax_info.plot([0.7], [0.08], 's', color='#3b82f6', markersize=10)
    ax_info.text(0.75, 0.08, r'$\mathbf{k}$ (eje Z)', fontsize=9, va='center')
    
    fig.suptitle('Sistema de Coordenadas Cartesianas Tridimensional', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "sistema_coordenadas_3d.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'sistema_coordenadas_3d.svg'}")
