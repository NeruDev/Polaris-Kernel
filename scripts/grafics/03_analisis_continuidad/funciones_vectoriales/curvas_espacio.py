# yaml_frontmatter:
#   id: 'curvas_espacio'
#   title: 'Funciones vectoriales r(t) y curvas en el espacio'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'funciones_vectoriales']

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
    # PANEL 3D: Hélice y vector tangente
    # =========================================
    t = np.linspace(0, 4*np.pi, 200)
    a, b = 1.5, 0.3
    
    # Hélice: r(t) = <a*cos(t), a*sin(t), b*t>
    x = a * np.cos(t)
    y = a * np.sin(t)
    z = b * t
    
    ax_3d.plot(x, y, z, color=colors['primary'], linewidth=2.5, label='Hélice')
    
    # Punto específico t0
    t0 = 2.5
    P = np.array([a*np.cos(t0), a*np.sin(t0), b*t0])
    ax_3d.scatter(*P, color=colors['accent'], s=100, zorder=5)
    ax_3d.text(P[0]+0.2, P[1]+0.2, P[2]+0.3, r'$\mathbf{r}(t_0)$', fontsize=11, 
              color=colors['accent'], fontweight='bold')
    
    # Vector tangente r'(t0) = <-a*sin(t), a*cos(t), b>
    tangent = np.array([-a*np.sin(t0), a*np.cos(t0), b])
    tangent_norm = tangent / np.linalg.norm(tangent) * 1.2
    ax_3d.quiver(*P, *tangent_norm, color='#dc2626', arrow_length_ratio=0.12, linewidth=2.5)
    ax_3d.text(P[0]+tangent_norm[0]+0.1, P[1]+tangent_norm[1], P[2]+tangent_norm[2]+0.2, 
              r"$\mathbf{r}'(t_0)$", fontsize=11, color='#dc2626', fontweight='bold')
    
    # Vector posición desde el origen
    origin = np.array([0, 0, 0])
    ax_3d.plot([0, P[0]], [0, P[1]], [0, P[2]], '--', color='#9ca3af', linewidth=1.5, alpha=0.7)
    
    # Cilindro de referencia (proyección)
    theta_cyl = np.linspace(0, 2*np.pi, 50)
    z_cyl = np.linspace(0, b*4*np.pi, 2)
    THETA, Z_CYL = np.meshgrid(theta_cyl, z_cyl)
    X_cyl = a * np.cos(THETA)
    Y_cyl = a * np.sin(THETA)
    ax_3d.plot_surface(X_cyl, Y_cyl, Z_CYL, alpha=0.1, color='#9ca3af')
    
    # Proyección en el plano xy
    ax_3d.plot(x, y, np.zeros_like(z), '--', color='#9ca3af', linewidth=1, alpha=0.5)
    
    # Ejes
    ax_3d.set_xlabel('X', fontsize=10, labelpad=5)
    ax_3d.set_ylabel('Y', fontsize=10, labelpad=5)
    ax_3d.set_zlabel('Z', fontsize=10, labelpad=5)
    
    ax_3d.set_xlim([-2.5, 2.5])
    ax_3d.set_ylim([-2.5, 2.5])
    ax_3d.set_zlim([0, 4])
    ax_3d.set_box_aspect([1, 1, 0.8])
    ax_3d.view_init(elev=20, azim=35)
    ax_3d.xaxis.pane.fill = False
    ax_3d.yaxis.pane.fill = False
    ax_3d.zaxis.pane.fill = False
    ax_3d.set_title('Hélice Circular', fontsize=11, fontweight='bold', pad=10)
    
    # =========================================
    # PANEL INFO: Fórmulas
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Definición
    ax_info.add_patch(plt.Rectangle((0.03, 0.75), 0.94, 0.22,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=2))
    ax_info.text(0.5, 0.92, 'FUNCIÓN VECTORIAL', fontsize=11,
                fontweight='bold', ha='center', color=colors['primary'])
    ax_info.text(0.5, 0.82, r'$\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle$',
                fontsize=13, ha='center', color=colors['text'])
    
    ax_info.axhline(y=0.71, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    
    # Derivada
    ax_info.text(0.5, 0.66, 'VECTOR TANGENTE', fontsize=10,
                fontweight='bold', ha='center', color='#dc2626')
    ax_info.text(0.5, 0.57, r"$\mathbf{r}'(t) = \langle x'(t), y'(t), z'(t) \rangle$",
                fontsize=12, ha='center', color=colors['text'])
    
    ax_info.axhline(y=0.51, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    
    # Cinemática
    ax_info.text(0.5, 0.46, 'INTERPRETACIÓN CINEMÁTICA', fontsize=10,
                fontweight='bold', ha='center', color=colors['secondary'])
    
    cinem = [
        (r'$\mathbf{r}(t)$', 'Posición'),
        (r"$\mathbf{v}(t) = \mathbf{r}'(t)$", 'Velocidad'),
        (r"$\mathbf{a}(t) = \mathbf{r}''(t)$", 'Aceleración'),
        (r"$v = \|\mathbf{r}'(t)\|$", 'Rapidez'),
    ]
    for i, (formula, desc) in enumerate(cinem):
        ax_info.text(0.35, 0.38 - i*0.07, formula, fontsize=10, ha='right', color=colors['text'])
        ax_info.text(0.40, 0.38 - i*0.07, f'→ {desc}', fontsize=9, ha='left', color='#6b7280')
    
    ax_info.axhline(y=0.10, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    
    # Ejemplo de hélice
    ax_info.add_patch(plt.Rectangle((0.03, 0.01), 0.94, 0.08,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=1.5))
    ax_info.text(0.5, 0.05, r'Hélice: $\mathbf{r}(t) = \langle a\cos t, a\sin t, bt \rangle$',
                fontsize=10, ha='center', color='#92400e')
    
    fig.suptitle('Funciones Vectoriales y Curvas en el Espacio', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "curvas_espacio.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'curvas_espacio.svg'}")
