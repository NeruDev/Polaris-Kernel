# yaml_frontmatter:
#   id: 'operaciones_vectores_3d'
#   title: 'Suma de vectores y multiplicación por escalar en el espacio'
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
    
    fig = plt.figure(figsize=(14, 8), layout='constrained')
    gs = fig.add_gridspec(1, 2, width_ratios=[1.4, 1], wspace=0.08)
    
    ax_3d = fig.add_subplot(gs[0], projection='3d')
    ax_info = fig.add_subplot(gs[1])
    
    # =========================================
    # PANEL 3D: Suma de vectores
    # =========================================
    origin = np.array([0, 0, 0])
    
    # Vectores u y v
    u = np.array([2, 0.5, 1])
    v = np.array([0.5, 2, 1.5])
    w = u + v  # Suma
    
    # Ejes de referencia
    for i in range(4):
        ax_3d.plot([i, i], [0, 0], [0, 0], color='#e5e7eb', linewidth=0.5)
        ax_3d.plot([0, 0], [i, i], [0, 0], color='#e5e7eb', linewidth=0.5)
        ax_3d.plot([0, 0], [0, 0], [i, i], color='#e5e7eb', linewidth=0.5)
    
    # Vector u (desde origen)
    ax_3d.quiver(*origin, *u, color=colors['primary'], arrow_length_ratio=0.08, linewidth=3)
    ax_3d.text(u[0]/2-0.3, u[1]/2, u[2]/2+0.3, r'$\mathbf{u}$', fontsize=14, 
              color=colors['primary'], fontweight='bold')
    
    # Vector v (desde origen)
    ax_3d.quiver(*origin, *v, color=colors['secondary'], arrow_length_ratio=0.08, linewidth=3)
    ax_3d.text(v[0]/2+0.2, v[1]/2+0.2, v[2]/2, r'$\mathbf{v}$', fontsize=14, 
              color=colors['secondary'], fontweight='bold')
    
    # Vector suma w = u + v (desde origen)
    ax_3d.quiver(*origin, *w, color=colors['accent'], arrow_length_ratio=0.05, linewidth=3.5)
    ax_3d.text(w[0]/2+0.3, w[1]/2, w[2]/2+0.2, r'$\mathbf{u}+\mathbf{v}$', fontsize=12, 
              color=colors['accent'], fontweight='bold')
    
    # Regla del paralelogramo
    # v trasladado a la punta de u
    ax_3d.quiver(*u, *v, color=colors['secondary'], arrow_length_ratio=0.08, 
                linewidth=2, alpha=0.6, linestyle='dashed')
    # u trasladado a la punta de v
    ax_3d.quiver(*v, *u, color=colors['primary'], arrow_length_ratio=0.08, 
                linewidth=2, alpha=0.6, linestyle='dashed')
    
    # Origen
    ax_3d.scatter(*origin, color='#374151', s=60, zorder=5)
    ax_3d.text(-0.2, -0.2, -0.1, 'O', fontsize=10, color='#374151')
    
    # Etiquetas de ejes
    ax_3d.set_xlabel('X', fontsize=10, labelpad=5)
    ax_3d.set_ylabel('Y', fontsize=10, labelpad=5)
    ax_3d.set_zlabel('Z', fontsize=10, labelpad=5)
    
    # Configuración
    ax_3d.set_xlim([0, 3.5])
    ax_3d.set_ylim([0, 3.5])
    ax_3d.set_zlim([0, 3.5])
    ax_3d.set_box_aspect([1, 1, 1])
    ax_3d.view_init(elev=25, azim=35)
    
    ax_3d.xaxis.pane.fill = False
    ax_3d.yaxis.pane.fill = False
    ax_3d.zaxis.pane.fill = False
    
    ax_3d.set_title('Regla del Paralelogramo', fontsize=11, fontweight='bold', pad=10)
    
    # =========================================
    # PANEL INFO: Fórmulas
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Suma de vectores
    ax_info.add_patch(plt.Rectangle((0.03, 0.75), 0.94, 0.22,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=2))
    ax_info.text(0.5, 0.92, 'SUMA DE VECTORES', fontsize=10,
                fontweight='bold', ha='center', color=colors['primary'])
    ax_info.text(0.5, 0.82, r'$\mathbf{u} + \mathbf{v} = \langle u_x + v_x, u_y + v_y, u_z + v_z \rangle$',
                fontsize=12, ha='center', color=colors['text'])
    
    # Resta
    ax_info.add_patch(plt.Rectangle((0.03, 0.52), 0.94, 0.20,
                                    facecolor='#f0fdf4', edgecolor=colors['secondary'],
                                    linewidth=1.5))
    ax_info.text(0.5, 0.68, 'RESTA DE VECTORES', fontsize=10,
                fontweight='bold', ha='center', color=colors['secondary'])
    ax_info.text(0.5, 0.58, r'$\mathbf{u} - \mathbf{v} = \mathbf{u} + (-\mathbf{v})$',
                fontsize=12, ha='center', color=colors['text'])
    
    # Multiplicación por escalar
    ax_info.add_patch(plt.Rectangle((0.03, 0.27), 0.94, 0.22,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=1.5))
    ax_info.text(0.5, 0.44, 'MULTIPLICACIÓN POR ESCALAR', fontsize=10,
                fontweight='bold', ha='center', color='#f59e0b')
    ax_info.text(0.5, 0.34, r'$c\mathbf{v} = \langle cv_x, cv_y, cv_z \rangle$',
                fontsize=12, ha='center', color=colors['text'])
    
    # Propiedades
    ax_info.text(0.5, 0.20, 'Propiedades', fontsize=10, fontweight='bold', ha='center', color='#374151')
    props = [
        r'$\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$ (conmutativa)',
        r'$c(d\mathbf{v}) = (cd)\mathbf{v}$ (asociativa)',
        r'$c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$ (distributiva)',
    ]
    for i, prop in enumerate(props):
        ax_info.text(0.5, 0.14 - i*0.05, prop, fontsize=9, ha='center', color='#6b7280')
    
    fig.suptitle('Operaciones con Vectores en el Espacio', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "operaciones_vectores_3d.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'operaciones_vectores_3d.svg'}")
