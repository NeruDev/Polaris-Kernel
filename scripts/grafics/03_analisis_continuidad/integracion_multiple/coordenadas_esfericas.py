# yaml_frontmatter:
#   id: 'coordenadas_esfericas'
#   title: 'Sistema de coordenadas esféricas'
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
    # PANEL 3D: Sistema de coordenadas esféricas
    # =========================================
    
    # Ejes coordenados
    ax_3d.quiver(0, 0, 0, 2.5, 0, 0, color='black', arrow_length_ratio=0.08, linewidth=1.5)
    ax_3d.quiver(0, 0, 0, 0, 2.5, 0, color='black', arrow_length_ratio=0.08, linewidth=1.5)
    ax_3d.quiver(0, 0, 0, 0, 0, 2.5, color='black', arrow_length_ratio=0.08, linewidth=1.5)
    ax_3d.text(2.7, 0, 0, 'x', fontsize=11, fontweight='bold')
    ax_3d.text(0, 2.7, 0, 'y', fontsize=11, fontweight='bold')
    ax_3d.text(0, 0, 2.7, 'z', fontsize=11, fontweight='bold')
    
    # Punto P en coordenadas esféricas (convención física: ρ, θ, φ)
    # ρ = radio, θ = ángulo azimutal (en xy desde x), φ = ángulo polar (desde z)
    rho, theta, phi = 2.0, np.pi/4, np.pi/3
    
    x_p = rho * np.sin(phi) * np.cos(theta)
    y_p = rho * np.sin(phi) * np.sin(theta)
    z_p = rho * np.cos(phi)
    
    # Punto P
    ax_3d.scatter([x_p], [y_p], [z_p], color=colors['accent'], s=150, zorder=5)
    ax_3d.text(x_p+0.15, y_p+0.15, z_p+0.15, 'P(ρ, θ, φ)', fontsize=11, 
              color=colors['accent'], fontweight='bold')
    
    # Radio ρ desde origen a P
    ax_3d.plot([0, x_p], [0, y_p], [0, z_p], '-', color='#dc2626', linewidth=2.5)
    ax_3d.text(x_p/2+0.1, y_p/2+0.1, z_p/2+0.1, 'ρ', fontsize=12, color='#dc2626', fontweight='bold')
    
    # Proyección en el plano xy
    r_xy = rho * np.sin(phi)  # Radio en xy
    ax_3d.scatter([x_p], [y_p], [0], color='#6b7280', s=80, marker='x', zorder=5)
    ax_3d.text(x_p+0.1, y_p+0.1, -0.15, "P'", fontsize=10, color='#6b7280')
    
    # Línea de P a su proyección
    ax_3d.plot([x_p, x_p], [y_p, y_p], [0, z_p], '--', color='#8b5cf6', linewidth=1.5, alpha=0.7)
    
    # Línea desde origen a proyección (r en plano xy)
    ax_3d.plot([0, x_p], [0, y_p], [0, 0], '-', color='#8b5cf6', linewidth=2)
    ax_3d.text(x_p/2, y_p/2, -0.15, 'r', fontsize=10, color='#8b5cf6')
    
    # Ángulo θ (azimutal, en plano xy)
    t_arc = np.linspace(0, theta, 30)
    r_arc = 0.7
    ax_3d.plot(r_arc*np.cos(t_arc), r_arc*np.sin(t_arc), np.zeros_like(t_arc), 
              '-', color='#10b981', linewidth=2)
    ax_3d.text(r_arc*np.cos(theta/2)+0.15, r_arc*np.sin(theta/2)+0.05, 0, 'θ', 
              fontsize=12, color='#10b981', fontweight='bold')
    
    # Ángulo φ (polar, desde eje z)
    phi_arc = np.linspace(0, phi, 30)
    r_phi = 0.8
    x_phi = r_phi * np.sin(phi_arc) * np.cos(theta)
    y_phi = r_phi * np.sin(phi_arc) * np.sin(theta)
    z_phi = r_phi * np.cos(phi_arc)
    ax_3d.plot(x_phi, y_phi, z_phi, '-', color='#f59e0b', linewidth=2)
    mid_phi = len(phi_arc)//2
    ax_3d.text(x_phi[mid_phi]+0.1, y_phi[mid_phi]+0.05, z_phi[mid_phi]+0.05, 'φ', 
              fontsize=12, color='#f59e0b', fontweight='bold')
    
    # Esfera transparente
    u = np.linspace(0, 2*np.pi, 40)
    v = np.linspace(0, np.pi, 30)
    U, V = np.meshgrid(u, v)
    X_sph = rho * np.sin(V) * np.cos(U)
    Y_sph = rho * np.sin(V) * np.sin(U)
    Z_sph = rho * np.cos(V)
    ax_3d.plot_surface(X_sph, Y_sph, Z_sph, alpha=0.1, color='#3b82f6', edgecolor='none')
    
    # Círculo ecuatorial
    ax_3d.plot(rho*np.cos(u), rho*np.sin(u), np.zeros_like(u), 
              '--', color='#3b82f6', linewidth=1, alpha=0.5)
    
    # Meridiano en θ = theta
    ax_3d.plot(rho*np.sin(v)*np.cos(theta), rho*np.sin(v)*np.sin(theta), rho*np.cos(v),
              '--', color='#10b981', linewidth=1, alpha=0.5)
    
    ax_3d.set_xlabel('X', fontsize=10)
    ax_3d.set_ylabel('Y', fontsize=10)
    ax_3d.set_zlabel('Z', fontsize=10)
    ax_3d.set_xlim([-0.5, 2.5])
    ax_3d.set_ylim([-0.5, 2.5])
    ax_3d.set_zlim([-0.5, 2.5])
    ax_3d.view_init(elev=20, azim=30)
    ax_3d.set_box_aspect([1, 1, 1])
    ax_3d.set_title('Coordenadas Esféricas (ρ, θ, φ)', fontsize=12, fontweight='bold')
    
    # =========================================
    # PANEL INFO
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Conversión
    ax_info.add_patch(plt.Rectangle((0.02, 0.68), 0.96, 0.30,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=2))
    ax_info.text(0.5, 0.94, 'CONVERSIÓN', fontsize=11,
                fontweight='bold', ha='center', color=colors['primary'])
    ax_info.text(0.33, 0.85, r'$x = \rho\sin\phi\cos\theta$', fontsize=10, ha='center', color=colors['text'])
    ax_info.text(0.33, 0.77, r'$y = \rho\sin\phi\sin\theta$', fontsize=10, ha='center', color=colors['text'])
    ax_info.text(0.33, 0.70, r'$z = \rho\cos\phi$', fontsize=10, ha='center', color=colors['text'])
    ax_info.text(0.75, 0.82, r'$\rho = \sqrt{x^2+y^2+z^2}$', fontsize=9, ha='center', color=colors['text'])
    ax_info.text(0.75, 0.72, r'$\phi = \arccos(z/\rho)$', fontsize=9, ha='center', color=colors['text'])
    
    # Jacobiano
    ax_info.add_patch(plt.Rectangle((0.02, 0.42), 0.96, 0.22,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=2))
    ax_info.text(0.5, 0.60, 'JACOBIANO', fontsize=10,
                fontweight='bold', ha='center', color='#f59e0b')
    ax_info.text(0.5, 0.48, r'$dV = \rho^2 \sin\phi \, d\rho \, d\theta \, d\phi$',
                fontsize=12, ha='center', color=colors['text'])
    
    # Integral triple
    ax_info.add_patch(plt.Rectangle((0.02, 0.16), 0.96, 0.22,
                                    facecolor='#f0fdf4', edgecolor='#10b981',
                                    linewidth=2))
    ax_info.text(0.5, 0.34, 'INTEGRAL TRIPLE', fontsize=10,
                fontweight='bold', ha='center', color='#10b981')
    ax_info.text(0.5, 0.22, r'$\iiint_E f \, dV = \iiint f \cdot \rho^2\sin\phi \, d\rho \, d\theta \, d\phi$',
                fontsize=9, ha='center', color=colors['text'])
    
    # Rangos
    ax_info.text(0.5, 0.08, 'Rangos:', fontsize=9, fontweight='bold', ha='center', color='#374151')
    ax_info.text(0.5, 0.02, r'$\rho \geq 0$, $0 \leq \theta \leq 2\pi$, $0 \leq \phi \leq \pi$',
                fontsize=9, ha='center', color='#6b7280')
    
    fig.suptitle('Sistema de Coordenadas Esféricas', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "coordenadas_esfericas.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'coordenadas_esfericas.svg'}")
