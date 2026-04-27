# yaml_frontmatter:
#   id: 'recta_plano_espacio'
#   title: 'Ecuación de la recta y el plano en el espacio 3D'
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
    gs = fig.add_gridspec(2, 2, height_ratios=[1.3, 1], hspace=0.2, wspace=0.15)
    
    ax_recta = fig.add_subplot(gs[0, 0], projection='3d')
    ax_plano = fig.add_subplot(gs[0, 1], projection='3d')
    ax_info = fig.add_subplot(gs[1, :])
    
    origin = np.array([0, 0, 0])
    
    # =========================================
    # PANEL 1: Recta en el espacio
    # =========================================
    P0 = np.array([1, 1, 1])
    v = np.array([1, 0.5, 0.8])  # Vector director
    
    # Recta parametrizada
    t_vals = np.linspace(-1, 2, 50)
    recta_x = P0[0] + v[0] * t_vals
    recta_y = P0[1] + v[1] * t_vals
    recta_z = P0[2] + v[2] * t_vals
    
    ax_recta.plot(recta_x, recta_y, recta_z, color=colors['primary'], linewidth=2.5)
    
    # Punto P0
    ax_recta.scatter(*P0, color=colors['accent'], s=100, zorder=5)
    ax_recta.text(P0[0]-0.3, P0[1]+0.2, P0[2]+0.3, r'$P_0$', fontsize=12, 
                 color=colors['accent'], fontweight='bold')
    
    # Vector director
    ax_recta.quiver(*P0, *v, color='#dc2626', arrow_length_ratio=0.15, linewidth=2.5)
    ax_recta.text(P0[0]+v[0]+0.1, P0[1]+v[1]+0.1, P0[2]+v[2]+0.2, r'$\mathbf{v}$', 
                 fontsize=13, color='#dc2626', fontweight='bold')
    
    # Ejes de referencia
    ax_recta.quiver(*origin, 3.5, 0, 0, color='#9ca3af', arrow_length_ratio=0.03, linewidth=1)
    ax_recta.quiver(*origin, 0, 3, 0, color='#9ca3af', arrow_length_ratio=0.04, linewidth=1)
    ax_recta.quiver(*origin, 0, 0, 3.5, color='#9ca3af', arrow_length_ratio=0.03, linewidth=1)
    ax_recta.text(3.6, 0, 0, 'X', fontsize=10, color='#6b7280')
    ax_recta.text(0, 3.1, 0, 'Y', fontsize=10, color='#6b7280')
    ax_recta.text(0, 0, 3.6, 'Z', fontsize=10, color='#6b7280')
    
    ax_recta.set_xlim([0, 4])
    ax_recta.set_ylim([0, 3])
    ax_recta.set_zlim([0, 4])
    ax_recta.set_box_aspect([1.3, 1, 1.3])
    ax_recta.view_init(elev=20, azim=35)
    ax_recta.xaxis.pane.fill = False
    ax_recta.yaxis.pane.fill = False
    ax_recta.zaxis.pane.fill = False
    ax_recta.set_title('Recta en el Espacio', fontsize=11, fontweight='bold', pad=5)
    
    # =========================================
    # PANEL 2: Plano en el espacio
    # =========================================
    P0_plane = np.array([1.5, 1.5, 1])
    n = np.array([1, 1, 2])  # Vector normal
    n_norm = n / np.linalg.norm(n)
    
    # Crear plano
    # Encontrar dos vectores en el plano
    if n[0] != 0:
        v1 = np.array([-n[1], n[0], 0])
    else:
        v1 = np.array([1, 0, 0])
    v1 = v1 / np.linalg.norm(v1)
    v2 = np.cross(n, v1)
    v2 = v2 / np.linalg.norm(v2)
    
    # Crear malla del plano
    s_range = np.linspace(-1.5, 1.5, 10)
    t_range = np.linspace(-1.5, 1.5, 10)
    S, T = np.meshgrid(s_range, t_range)
    X_plane = P0_plane[0] + S*v1[0] + T*v2[0]
    Y_plane = P0_plane[1] + S*v1[1] + T*v2[1]
    Z_plane = P0_plane[2] + S*v1[2] + T*v2[2]
    
    ax_plano.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.4, 
                         color=colors['secondary'], edgecolor='none')
    
    # Punto P0
    ax_plano.scatter(*P0_plane, color=colors['accent'], s=100, zorder=5)
    ax_plano.text(P0_plane[0]+0.2, P0_plane[1]+0.2, P0_plane[2]-0.3, r'$P_0$', 
                 fontsize=12, color=colors['accent'], fontweight='bold')
    
    # Vector normal
    scale = 1.2
    ax_plano.quiver(*P0_plane, *(n_norm*scale), color='#dc2626', 
                   arrow_length_ratio=0.15, linewidth=3)
    ax_plano.text(P0_plane[0]+n_norm[0]*scale+0.1, 
                 P0_plane[1]+n_norm[1]*scale+0.1, 
                 P0_plane[2]+n_norm[2]*scale+0.2, 
                 r'$\mathbf{n}$', fontsize=13, color='#dc2626', fontweight='bold')
    
    # Ejes
    ax_plano.quiver(*origin, 3.5, 0, 0, color='#9ca3af', arrow_length_ratio=0.03, linewidth=1)
    ax_plano.quiver(*origin, 0, 3.5, 0, color='#9ca3af', arrow_length_ratio=0.03, linewidth=1)
    ax_plano.quiver(*origin, 0, 0, 3.5, color='#9ca3af', arrow_length_ratio=0.03, linewidth=1)
    ax_plano.text(3.6, 0, 0, 'X', fontsize=10, color='#6b7280')
    ax_plano.text(0, 3.6, 0, 'Y', fontsize=10, color='#6b7280')
    ax_plano.text(0, 0, 3.6, 'Z', fontsize=10, color='#6b7280')
    
    ax_plano.set_xlim([0, 4])
    ax_plano.set_ylim([0, 4])
    ax_plano.set_zlim([0, 4])
    ax_plano.set_box_aspect([1, 1, 1])
    ax_plano.view_init(elev=25, azim=40)
    ax_plano.xaxis.pane.fill = False
    ax_plano.yaxis.pane.fill = False
    ax_plano.zaxis.pane.fill = False
    ax_plano.set_title('Plano en el Espacio', fontsize=11, fontweight='bold', pad=5)
    
    # =========================================
    # PANEL INFO: Fórmulas
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Ecuaciones de la recta
    ax_info.add_patch(plt.Rectangle((0.02, 0.52), 0.46, 0.45,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=2))
    ax_info.text(0.25, 0.92, 'ECUACIÓN DE LA RECTA', fontsize=10,
                fontweight='bold', ha='center', color=colors['primary'])
    
    ax_info.text(0.25, 0.82, 'Forma vectorial:', fontsize=9, 
                fontweight='bold', ha='center', color='#374151')
    ax_info.text(0.25, 0.75, r'$\mathbf{r}(t) = \mathbf{r}_0 + t\mathbf{v}$',
                fontsize=11, ha='center', color=colors['text'])
    
    ax_info.text(0.25, 0.66, 'Forma paramétrica:', fontsize=9, 
                fontweight='bold', ha='center', color='#374151')
    ax_info.text(0.25, 0.58, r'$x = x_0 + at$, $y = y_0 + bt$, $z = z_0 + ct$',
                fontsize=10, ha='center', color=colors['text'])
    
    # Ecuaciones del plano
    ax_info.add_patch(plt.Rectangle((0.52, 0.52), 0.46, 0.45,
                                    facecolor='#f0fdf4', edgecolor=colors['secondary'],
                                    linewidth=2))
    ax_info.text(0.75, 0.92, 'ECUACIÓN DEL PLANO', fontsize=10,
                fontweight='bold', ha='center', color=colors['secondary'])
    
    ax_info.text(0.75, 0.82, 'Forma normal (vectorial):', fontsize=9, 
                fontweight='bold', ha='center', color='#374151')
    ax_info.text(0.75, 0.75, r'$\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$',
                fontsize=11, ha='center', color=colors['text'])
    
    ax_info.text(0.75, 0.66, 'Forma escalar (general):', fontsize=9, 
                fontweight='bold', ha='center', color='#374151')
    ax_info.text(0.75, 0.58, r'$ax + by + cz = d$',
                fontsize=11, ha='center', color=colors['text'])
    
    # Fórmulas de distancia
    ax_info.add_patch(plt.Rectangle((0.02, 0.05), 0.46, 0.42,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=1.5))
    ax_info.text(0.25, 0.42, 'DISTANCIA PUNTO-PLANO', fontsize=10,
                fontweight='bold', ha='center', color='#f59e0b')
    ax_info.text(0.25, 0.28, r'$D = \frac{|ax_1 + by_1 + cz_1 - d|}{\sqrt{a^2 + b^2 + c^2}}$',
                fontsize=12, ha='center', color=colors['text'])
    ax_info.text(0.25, 0.12, r'donde $Q = (x_1, y_1, z_1)$',
                fontsize=9, ha='center', color='#6b7280')
    
    # Ángulos
    ax_info.add_patch(plt.Rectangle((0.52, 0.05), 0.46, 0.42,
                                    facecolor='#fce7f3', edgecolor='#ec4899',
                                    linewidth=1.5))
    ax_info.text(0.75, 0.42, 'ÁNGULOS', fontsize=10,
                fontweight='bold', ha='center', color='#ec4899')
    ax_info.text(0.75, 0.32, 'Entre dos planos:', fontsize=9, 
                fontweight='bold', ha='center', color='#374151')
    ax_info.text(0.75, 0.24, r'$\cos\theta = \frac{|\mathbf{n}_1 \cdot \mathbf{n}_2|}{\|\mathbf{n}_1\| \|\mathbf{n}_2\|}$',
                fontsize=10, ha='center', color=colors['text'])
    ax_info.text(0.75, 0.14, 'Entre recta y plano:', fontsize=9, 
                fontweight='bold', ha='center', color='#374151')
    ax_info.text(0.75, 0.06, r'$\sin\alpha = \frac{|\mathbf{v} \cdot \mathbf{n}|}{\|\mathbf{v}\| \|\mathbf{n}\|}$',
                fontsize=10, ha='center', color=colors['text'])
    
    fig.suptitle('Recta y Plano en el Espacio $\\mathbb{R}^3$', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "recta_plano_espacio.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'recta_plano_espacio.svg'}")
