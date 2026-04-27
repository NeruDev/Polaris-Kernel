# yaml_frontmatter:
#   id: 'producto_punto_cruz'
#   title: 'Producto escalar (punto) y producto vectorial (cruz)'
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
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

    setup_style,
    get_colors,
    get_output_dir_for_topic,
    save_figure,
)


def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig = plt.figure(figsize=(14, 9), layout='constrained')
    gs = fig.add_gridspec(2, 2, height_ratios=[1.2, 1], hspace=0.2, wspace=0.15)
    
    ax_dot = fig.add_subplot(gs[0, 0], projection='3d')
    ax_cross = fig.add_subplot(gs[0, 1], projection='3d')
    ax_info = fig.add_subplot(gs[1, :])
    
    origin = np.array([0, 0, 0])
    
    # =========================================
    # PANEL 1: Producto Punto (proyección)
    # =========================================
    u = np.array([2, 1, 0.5])
    v = np.array([1, 2, 0])
    
    # Proyección de u sobre v
    proj_scalar = np.dot(u, v) / np.linalg.norm(v)
    proj_vec = (np.dot(u, v) / np.dot(v, v)) * v
    
    ax_dot.quiver(*origin, *u, color=colors['primary'], arrow_length_ratio=0.08, linewidth=3)
    ax_dot.quiver(*origin, *v, color=colors['secondary'], arrow_length_ratio=0.08, linewidth=3)
    ax_dot.quiver(*origin, *proj_vec, color=colors['accent'], arrow_length_ratio=0.1, linewidth=2.5)
    
    # Línea de proyección
    ax_dot.plot([u[0], proj_vec[0]], [u[1], proj_vec[1]], [u[2], proj_vec[2]], 
               '--', color='#9ca3af', linewidth=1.5)
    
    # Arco para el ángulo
    t = np.linspace(0, np.arccos(np.dot(u, v)/(np.linalg.norm(u)*np.linalg.norm(v))), 20)
    r = 0.5
    u_unit = u / np.linalg.norm(u)
    v_unit = v / np.linalg.norm(v)
    
    ax_dot.text(u[0]+0.1, u[1]+0.1, u[2]+0.2, r'$\mathbf{u}$', fontsize=13, 
               color=colors['primary'], fontweight='bold')
    ax_dot.text(v[0]+0.1, v[1]+0.1, v[2]+0.1, r'$\mathbf{v}$', fontsize=13, 
               color=colors['secondary'], fontweight='bold')
    ax_dot.text(proj_vec[0]/2-0.2, proj_vec[1]/2+0.3, 0.1, r'$\mathrm{proy}_\mathbf{v}\mathbf{u}$', 
               fontsize=10, color=colors['accent'])
    ax_dot.text(0.4, 0.5, 0.1, r'$\theta$', fontsize=12, color='#6b7280')
    
    ax_dot.scatter(*origin, color='#374151', s=50, zorder=5)
    ax_dot.set_xlim([0, 3])
    ax_dot.set_ylim([0, 3])
    ax_dot.set_zlim([0, 2])
    ax_dot.set_box_aspect([1.5, 1.5, 1])
    ax_dot.view_init(elev=25, azim=30)
    ax_dot.xaxis.pane.fill = False
    ax_dot.yaxis.pane.fill = False
    ax_dot.zaxis.pane.fill = False
    ax_dot.set_title('Producto Punto y Proyección', fontsize=11, fontweight='bold', pad=5)
    
    # =========================================
    # PANEL 2: Producto Cruz
    # =========================================
    u2 = np.array([2, 0, 0])
    v2 = np.array([1, 2, 0])
    cross = np.cross(u2, v2)
    
    ax_cross.quiver(*origin, *u2, color=colors['primary'], arrow_length_ratio=0.08, linewidth=3)
    ax_cross.quiver(*origin, *v2, color=colors['secondary'], arrow_length_ratio=0.08, linewidth=3)
    ax_cross.quiver(*origin, *cross, color='#dc2626', arrow_length_ratio=0.05, linewidth=3.5)
    
    # Paralelogramo
    verts = [[origin, u2, u2+v2, v2]]
    poly = Poly3DCollection(verts, alpha=0.3, facecolor=colors['tertiary'], edgecolor=colors['tertiary'])
    ax_cross.add_collection3d(poly)
    
    ax_cross.text(u2[0]+0.1, u2[1]+0.1, 0.1, r'$\mathbf{u}$', fontsize=13, 
                 color=colors['primary'], fontweight='bold')
    ax_cross.text(v2[0]-0.3, v2[1]+0.1, 0.1, r'$\mathbf{v}$', fontsize=13, 
                 color=colors['secondary'], fontweight='bold')
    ax_cross.text(0.2, 0.2, cross[2]/2+0.5, r'$\mathbf{u} \times \mathbf{v}$', fontsize=12, 
                 color='#dc2626', fontweight='bold')
    
    ax_cross.scatter(*origin, color='#374151', s=50, zorder=5)
    ax_cross.set_xlim([0, 3])
    ax_cross.set_ylim([0, 3])
    ax_cross.set_zlim([0, 5])
    ax_cross.set_box_aspect([1, 1, 1.5])
    ax_cross.view_init(elev=20, azim=35)
    ax_cross.xaxis.pane.fill = False
    ax_cross.yaxis.pane.fill = False
    ax_cross.zaxis.pane.fill = False
    ax_cross.set_title('Producto Cruz y Paralelogramo', fontsize=11, fontweight='bold', pad=5)
    
    # =========================================
    # PANEL INFO: Fórmulas
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Producto punto
    ax_info.add_patch(plt.Rectangle((0.02, 0.52), 0.46, 0.45,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=2))
    ax_info.text(0.25, 0.90, 'PRODUCTO PUNTO', fontsize=11,
                fontweight='bold', ha='center', color=colors['primary'])
    ax_info.text(0.25, 0.80, r'$\mathbf{u} \cdot \mathbf{v} = u_xv_x + u_yv_y + u_zv_z$',
                fontsize=11, ha='center', color=colors['text'])
    ax_info.text(0.25, 0.70, r'$= \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta$',
                fontsize=11, ha='center', color=colors['text'])
    ax_info.text(0.25, 0.58, r'$\mathbf{u} \perp \mathbf{v} \Leftrightarrow \mathbf{u} \cdot \mathbf{v} = 0$',
                fontsize=10, ha='center', color='#6b7280')
    
    # Producto cruz
    ax_info.add_patch(plt.Rectangle((0.52, 0.52), 0.46, 0.45,
                                    facecolor='#fef2f2', edgecolor='#dc2626',
                                    linewidth=2))
    ax_info.text(0.75, 0.90, 'PRODUCTO CRUZ', fontsize=11,
                fontweight='bold', ha='center', color='#dc2626')
    ax_info.text(0.75, 0.78, r'$(u_yv_z - u_zv_y)\mathbf{i} - (u_xv_z - u_zv_x)\mathbf{j}$',
                fontsize=9, ha='center', color=colors['text'])
    ax_info.text(0.75, 0.68, r'$+ (u_xv_y - u_yv_x)\mathbf{k}$',
                fontsize=9, ha='center', color=colors['text'])
    ax_info.text(0.75, 0.58, r'$\|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{u}\| \|\mathbf{v}\| \sin\theta$',
                fontsize=10, ha='center', color='#6b7280')
    
    # Proyección
    ax_info.add_patch(plt.Rectangle((0.02, 0.05), 0.46, 0.42,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=1.5))
    ax_info.text(0.25, 0.42, 'PROYECCIÓN', fontsize=10,
                fontweight='bold', ha='center', color='#f59e0b')
    ax_info.text(0.25, 0.32, r'$\mathrm{comp}_\mathbf{v}\mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|}$',
                fontsize=11, ha='center', color=colors['text'])
    ax_info.text(0.25, 0.20, r'$\mathrm{proy}_\mathbf{v}\mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2}\mathbf{v}$',
                fontsize=11, ha='center', color=colors['text'])
    ax_info.text(0.25, 0.10, '(escalar)  →  (vector)', fontsize=9, ha='center', color='#6b7280')
    
    # Propiedades del producto cruz
    ax_info.add_patch(plt.Rectangle((0.52, 0.05), 0.46, 0.42,
                                    facecolor='#f0fdf4', edgecolor=colors['secondary'],
                                    linewidth=1.5))
    ax_info.text(0.75, 0.42, 'PROPIEDADES DEL CRUZ', fontsize=10,
                fontweight='bold', ha='center', color=colors['secondary'])
    props = [
        r'$\mathbf{u} \times \mathbf{v} \perp \mathbf{u}$ y $\perp \mathbf{v}$',
        r'$\mathbf{v} \times \mathbf{u} = -(\mathbf{u} \times \mathbf{v})$',
        r'$\|\mathbf{u} \times \mathbf{v}\| =$ área del paralelogramo',
    ]
    for i, p in enumerate(props):
        ax_info.text(0.75, 0.32 - i*0.10, p, fontsize=9, ha='center', color='#6b7280')
    
    fig.suptitle('Producto Escalar y Producto Vectorial', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "producto_punto_cruz.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'producto_punto_cruz.svg'}")
