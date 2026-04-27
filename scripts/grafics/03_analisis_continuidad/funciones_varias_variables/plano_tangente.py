# yaml_frontmatter:
#   id: 'plano_tangente'
#   title: 'Plano tangente y aproximación lineal'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'funciones_varias_variables']

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
    gs = fig.add_gridspec(1, 2, width_ratios=[1.5, 1])
    
    ax_3d = fig.add_subplot(gs[0], projection='3d')
    ax_info = fig.add_subplot(gs[1])
    
    # =========================================
    # Función: z = x² + y²/2 (paraboloide)
    # Punto de tangencia: (1, 1, 1.5)
    # =========================================
    x = np.linspace(-1.5, 2.5, 100)
    y = np.linspace(-1.5, 2.5, 100)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2/2
    
    # Punto de tangencia
    x0, y0 = 1.0, 1.0
    z0 = x0**2 + y0**2/2
    
    # Derivadas parciales en (x0, y0)
    # ∂f/∂x = 2x, ∂f/∂y = y
    fx = 2*x0
    fy = y0
    
    # Ecuación del plano tangente: z - z0 = fx(x-x0) + fy(y-y0)
    # z = z0 + fx(x-x0) + fy(y-y0)
    Z_plane = z0 + fx*(X - x0) + fy*(Y - y0)
    
    # =========================================
    # PANEL 3D
    # =========================================
    # Superficie
    ax_3d.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, 
                      edgecolor='none', linewidth=0)
    
    # Plano tangente (solo en región cercana al punto)
    mask = (np.abs(X - x0) < 1.2) & (np.abs(Y - y0) < 1.2)
    X_plane = np.where(mask, X, np.nan)
    Y_plane = np.where(mask, Y, np.nan)
    Z_plane_masked = np.where(mask, Z_plane, np.nan)
    
    ax_3d.plot_surface(X_plane, Y_plane, Z_plane_masked, color='#f59e0b', alpha=0.5)
    
    # Punto de tangencia
    ax_3d.scatter([x0], [y0], [z0], color=colors['accent'], s=150, zorder=5)
    ax_3d.text(x0+0.1, y0+0.1, z0+0.3, f'P({x0}, {y0}, {z0})', fontsize=10, color=colors['accent'])
    
    # Vector normal al plano (gradiente, -1)
    # Normal = (fx, fy, -1) normalizado
    normal = np.array([fx, fy, -1])
    normal_unit = normal / np.linalg.norm(normal) * 0.8
    
    ax_3d.quiver(x0, y0, z0, normal_unit[0], normal_unit[1], normal_unit[2],
                color='#dc2626', arrow_length_ratio=0.15, linewidth=2.5)
    ax_3d.text(x0+normal_unit[0]+0.1, y0+normal_unit[1]+0.1, z0+normal_unit[2]+0.1, 
              r'$\mathbf{n}$', fontsize=11, color='#dc2626', fontweight='bold')
    
    # Vectores tangentes
    # T1 = (1, 0, fx) dirección x
    # T2 = (0, 1, fy) dirección y
    T1 = np.array([1, 0, fx]) / np.linalg.norm([1, 0, fx]) * 0.6
    T2 = np.array([0, 1, fy]) / np.linalg.norm([0, 1, fy]) * 0.6
    
    ax_3d.quiver(x0, y0, z0, T1[0], T1[1], T1[2],
                color=colors['primary'], arrow_length_ratio=0.15, linewidth=2)
    ax_3d.quiver(x0, y0, z0, T2[0], T2[1], T2[2],
                color='#10b981', arrow_length_ratio=0.15, linewidth=2)
    
    # Proyección del punto
    ax_3d.plot([x0, x0], [y0, y0], [0, z0], '--', color='gray', linewidth=1)
    ax_3d.scatter([x0], [y0], [0], color='gray', s=50, marker='x')
    
    ax_3d.set_xlabel('X', fontsize=10)
    ax_3d.set_ylabel('Y', fontsize=10)
    ax_3d.set_zlabel('Z', fontsize=10)
    ax_3d.set_title(r'Plano tangente a $z = x^2 + \frac{y^2}{2}$', fontsize=11, fontweight='bold')
    ax_3d.view_init(elev=20, azim=45)
    ax_3d.set_box_aspect([1, 1, 0.7])
    
    # Leyenda manual
    ax_3d.plot([], [], [], color='#f59e0b', linewidth=5, alpha=0.5, label='Plano tangente')
    ax_3d.plot([], [], [], color='#dc2626', linewidth=2.5, label='Normal n')
    ax_3d.legend(loc='upper left', fontsize=9)
    
    # =========================================
    # PANEL INFO
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Ecuación del plano tangente
    ax_info.add_patch(plt.Rectangle((0.02, 0.72), 0.96, 0.26,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=2))
    ax_info.text(0.5, 0.94, 'PLANO TANGENTE', fontsize=11,
                fontweight='bold', ha='center', color='#f59e0b')
    ax_info.text(0.5, 0.82, r'$z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)$',
                fontsize=10, ha='center', color=colors['text'])
    
    # Aproximación lineal
    ax_info.add_patch(plt.Rectangle((0.02, 0.48), 0.96, 0.20,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=2))
    ax_info.text(0.5, 0.64, 'APROXIMACIÓN LINEAL', fontsize=10,
                fontweight='bold', ha='center', color=colors['primary'])
    ax_info.text(0.5, 0.53, r'$L(x,y) = f(a,b) + \nabla f(a,b) \cdot (x-a, y-b)$',
                fontsize=10, ha='center', color=colors['text'])
    
    # Vector normal
    ax_info.add_patch(plt.Rectangle((0.02, 0.26), 0.96, 0.18,
                                    facecolor='#fef2f2', edgecolor='#dc2626',
                                    linewidth=1.5))
    ax_info.text(0.5, 0.40, 'VECTOR NORMAL', fontsize=9,
                fontweight='bold', ha='center', color='#dc2626')
    ax_info.text(0.5, 0.30, r'$\mathbf{n} = (f_x, f_y, -1)$ ó $(-f_x, -f_y, 1)$',
                fontsize=10, ha='center', color=colors['text'])
    
    # Ejemplo numérico
    ax_info.add_patch(plt.Rectangle((0.02, 0.03), 0.96, 0.20,
                                    facecolor='#f0fdf4', edgecolor='#10b981',
                                    linewidth=1.5))
    ax_info.text(0.5, 0.19, 'EJEMPLO', fontsize=9,
                fontweight='bold', ha='center', color='#10b981')
    ax_info.text(0.5, 0.11, f'En P(1,1,1.5): $f_x=2$, $f_y=1$',
                fontsize=9, ha='center', color=colors['text'])
    ax_info.text(0.5, 0.05, r'Plano: $z = 1.5 + 2(x-1) + (y-1)$',
                fontsize=9, ha='center', color=colors['text'])
    
    fig.suptitle('Plano Tangente y Aproximación Lineal', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "plano_tangente.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'plano_tangente.svg'}")
