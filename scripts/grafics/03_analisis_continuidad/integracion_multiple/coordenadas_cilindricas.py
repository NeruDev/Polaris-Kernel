# yaml_frontmatter:
#   id: 'coordenadas_cilindricas'
#   title: 'Sistema de coordenadas cilíndricas'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'integracion_multiple']

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
    
    fig = plt.figure(figsize=(14, 8), layout='constrained')
    gs = fig.add_gridspec(1, 2, width_ratios=[1.4, 1])
    
    ax_3d = fig.add_subplot(gs[0], projection='3d')
    ax_info = fig.add_subplot(gs[1])
    
    # =========================================
    # PANEL 3D: Sistema de coordenadas cilíndricas
    # =========================================
    
    # Ejes coordenados
    ax_3d.quiver(0, 0, 0, 2.5, 0, 0, color='black', arrow_length_ratio=0.08, linewidth=1.5)
    ax_3d.quiver(0, 0, 0, 0, 2.5, 0, color='black', arrow_length_ratio=0.08, linewidth=1.5)
    ax_3d.quiver(0, 0, 0, 0, 0, 2.5, color='black', arrow_length_ratio=0.08, linewidth=1.5)
    ax_3d.text(2.7, 0, 0, 'x', fontsize=11, fontweight='bold')
    ax_3d.text(0, 2.7, 0, 'y', fontsize=11, fontweight='bold')
    ax_3d.text(0, 0, 2.7, 'z', fontsize=11, fontweight='bold')
    
    # Punto P en coordenadas cilíndricas
    r, theta, z_p = 1.8, np.pi/4, 1.5
    x_p = r * np.cos(theta)
    y_p = r * np.sin(theta)
    
    # Punto P
    ax_3d.scatter([x_p], [y_p], [z_p], color=colors['accent'], s=150, zorder=5)
    ax_3d.text(x_p+0.15, y_p+0.15, z_p+0.15, 'P(r, θ, z)', fontsize=11, color=colors['accent'], fontweight='bold')
    
    # Proyección en el plano xy
    ax_3d.scatter([x_p], [y_p], [0], color='#6b7280', s=80, marker='x', zorder=5)
    ax_3d.text(x_p+0.1, y_p+0.1, -0.15, "P'", fontsize=10, color='#6b7280')
    
    # Línea vertical de P a proyección
    ax_3d.plot([x_p, x_p], [y_p, y_p], [0, z_p], '--', color=colors['primary'], linewidth=2)
    ax_3d.text(x_p+0.12, y_p+0.12, z_p/2, 'z', fontsize=11, color=colors['primary'], fontweight='bold')
    
    # Radio r desde origen a proyección
    ax_3d.plot([0, x_p], [0, y_p], [0, 0], '-', color='#dc2626', linewidth=2.5)
    ax_3d.text(x_p/2-0.1, y_p/2+0.1, 0.1, 'r', fontsize=12, color='#dc2626', fontweight='bold')
    
    # Ángulo θ
    t_arc = np.linspace(0, theta, 30)
    r_arc = 0.6
    ax_3d.plot(r_arc*np.cos(t_arc), r_arc*np.sin(t_arc), np.zeros_like(t_arc), 
              '-', color='#10b981', linewidth=2)
    ax_3d.text(r_arc*np.cos(theta/2)+0.1, r_arc*np.sin(theta/2), 0.1, 'θ', 
              fontsize=12, color='#10b981', fontweight='bold')
    
    # Cilindro transparente (superficie r = constante)
    theta_cyl = np.linspace(0, 2*np.pi, 50)
    z_cyl = np.linspace(0, 2, 20)
    THETA_CYL, Z_CYL = np.meshgrid(theta_cyl, z_cyl)
    X_CYL = r * np.cos(THETA_CYL)
    Y_CYL = r * np.sin(THETA_CYL)
    ax_3d.plot_surface(X_CYL, Y_CYL, Z_CYL, alpha=0.15, color='#3b82f6', edgecolor='none')
    
    # Círculo en z = z_p
    ax_3d.plot(r*np.cos(theta_cyl), r*np.sin(theta_cyl), 
              np.full_like(theta_cyl, z_p), '--', color='#3b82f6', linewidth=1.5, alpha=0.7)
    
    # Plano θ = constante (semiplano)
    r_plane = np.linspace(0, 2.2, 2)
    z_plane = np.linspace(0, 2.2, 2)
    R_PLANE, Z_PLANE = np.meshgrid(r_plane, z_plane)
    X_PLANE = R_PLANE * np.cos(theta)
    Y_PLANE = R_PLANE * np.sin(theta)
    ax_3d.plot_surface(X_PLANE, Y_PLANE, Z_PLANE, alpha=0.15, color='#10b981', edgecolor='none')
    
    ax_3d.set_xlabel('X', fontsize=10)
    ax_3d.set_ylabel('Y', fontsize=10)
    ax_3d.set_zlabel('Z', fontsize=10)
    ax_3d.set_xlim([-0.5, 2.5])
    ax_3d.set_ylim([-0.5, 2.5])
    ax_3d.set_zlim([0, 2.5])
    ax_3d.view_init(elev=20, azim=30)
    ax_3d.set_box_aspect([1, 1, 0.8])
    ax_3d.set_title('Coordenadas Cilíndricas (r, θ, z)', fontsize=12, fontweight='bold')
    
    # =========================================
    # PANEL INFO
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Conversión
    ax_info.add_patch(plt.Rectangle((0.02, 0.72), 0.96, 0.26,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=2))
    ax_info.text(0.5, 0.94, 'CONVERSIÓN', fontsize=11,
                fontweight='bold', ha='center', color=colors['primary'])
    ax_info.text(0.25, 0.84, r'$x = r\cos\theta$', fontsize=11, ha='center', color=colors['text'])
    ax_info.text(0.75, 0.84, r'$r = \sqrt{x^2+y^2}$', fontsize=11, ha='center', color=colors['text'])
    ax_info.text(0.25, 0.76, r'$y = r\sin\theta$', fontsize=11, ha='center', color=colors['text'])
    ax_info.text(0.75, 0.76, r'$\theta = \arctan(y/x)$', fontsize=11, ha='center', color=colors['text'])
    
    # Jacobiano
    ax_info.add_patch(plt.Rectangle((0.02, 0.48), 0.96, 0.20,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=2))
    ax_info.text(0.5, 0.64, 'JACOBIANO', fontsize=10,
                fontweight='bold', ha='center', color='#f59e0b')
    ax_info.text(0.5, 0.53, r'$dV = r \, dr \, d\theta \, dz$',
                fontsize=13, ha='center', color=colors['text'])
    
    # Integral triple
    ax_info.add_patch(plt.Rectangle((0.02, 0.20), 0.96, 0.24,
                                    facecolor='#f0fdf4', edgecolor='#10b981',
                                    linewidth=2))
    ax_info.text(0.5, 0.40, 'INTEGRAL TRIPLE', fontsize=10,
                fontweight='bold', ha='center', color='#10b981')
    ax_info.text(0.5, 0.28, r'$\iiint_E f \, dV = \iiint f(r\cos\theta, r\sin\theta, z) \cdot r \, dr \, d\theta \, dz$',
                fontsize=9, ha='center', color=colors['text'])
    
    # Rangos
    ax_info.text(0.5, 0.10, 'Rangos típicos:', fontsize=9, fontweight='bold', ha='center', color='#374151')
    ax_info.text(0.5, 0.03, r'$r \geq 0$, $0 \leq \theta \leq 2\pi$, $z \in \mathbb{R}$',
                fontsize=9, ha='center', color='#6b7280')
    
    fig.suptitle('Sistema de Coordenadas Cilíndricas', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "coordenadas_cilindricas.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'coordenadas_cilindricas.svg'}")
