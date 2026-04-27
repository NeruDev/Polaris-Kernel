# yaml_frontmatter:
#   id: 'teoremas_integrales'
#   title: 'Teoremas de Green, Stokes y Divergencia'
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
    
    fig = plt.figure(figsize=(15, 9), layout='constrained')
    gs = fig.add_gridspec(2, 3, height_ratios=[1.2, 1])
    
    ax_green = fig.add_subplot(gs[0, 0])
    ax_stokes = fig.add_subplot(gs[0, 1], projection='3d')
    ax_div = fig.add_subplot(gs[0, 2], projection='3d')
    
    ax_green_info = fig.add_subplot(gs[1, 0])
    ax_stokes_info = fig.add_subplot(gs[1, 1])
    ax_div_info = fig.add_subplot(gs[1, 2])
    
    # =========================================
    # TEOREMA DE GREEN (2D)
    # =========================================
    ax_green.set_aspect('equal')
    
    # Región D
    t = np.linspace(0, 2*np.pi, 100)
    r = 1.5 + 0.3*np.sin(3*t)  # Forma irregular
    x = r * np.cos(t)
    y = r * np.sin(t)
    
    ax_green.fill(x, y, color=colors['primary'], alpha=0.3)
    ax_green.plot(x, y, color=colors['primary'], linewidth=3)
    
    # Flecha de orientación
    idx = len(t)//4
    ax_green.annotate('', xy=(x[idx+5], y[idx+5]), xytext=(x[idx], y[idx]),
                     arrowprops=dict(arrowstyle='->', color='#dc2626', lw=2.5))
    ax_green.text(1.0, 1.8, 'C (+ orientada)', fontsize=10, color='#dc2626')
    
    # Campo vectorial (flechas)
    xq = np.linspace(-1.8, 1.8, 8)
    yq = np.linspace(-1.8, 1.8, 8)
    XQ, YQ = np.meshgrid(xq, yq)
    U = -YQ/3
    V = XQ/3
    ax_green.quiver(XQ, YQ, U, V, color='#10b981', alpha=0.6, scale=8)
    
    ax_green.text(0, 0, 'D', fontsize=16, fontweight='bold', ha='center', 
                 va='center', color=colors['primary'])
    ax_green.set_xlabel('x', fontsize=10)
    ax_green.set_ylabel('y', fontsize=10)
    ax_green.set_title('Teorema de Green', fontsize=11, fontweight='bold', color=colors['primary'])
    ax_green.grid(True, linestyle='--', alpha=0.3)
    ax_green.set_xlim([-2.5, 2.5])
    ax_green.set_ylim([-2.5, 2.5])
    
    # =========================================
    # TEOREMA DE STOKES (3D)
    # =========================================
    # Superficie con borde
    u = np.linspace(0, 2*np.pi, 50)
    v = np.linspace(0, 1, 30)
    U, V = np.meshgrid(u, v)
    
    X_st = V * np.cos(U)
    Y_st = V * np.sin(U)
    Z_st = 0.5 * (1 - V**2) * (1 + 0.3*np.sin(3*U))
    
    ax_stokes.plot_surface(X_st, Y_st, Z_st, cmap='Greens', alpha=0.6, edgecolor='none')
    
    # Borde (curva C)
    ax_stokes.plot(np.cos(u), np.sin(u), 0.5*0.3*np.sin(3*u), 
                  color='#dc2626', linewidth=3)
    
    # Vector normal (∇ × F)
    ax_stokes.quiver(0, 0, 0.3, 0, 0, 0.5, color='#f59e0b', 
                    arrow_length_ratio=0.2, linewidth=2.5)
    ax_stokes.text(0.1, 0.1, 0.9, r'$\nabla \times \mathbf{F}$', fontsize=10, color='#f59e0b')
    
    ax_stokes.text(0, 0, 0.2, 'S', fontsize=14, fontweight='bold', color='#10b981')
    ax_stokes.text(1.1, 0, 0.1, 'C', fontsize=12, fontweight='bold', color='#dc2626')
    
    ax_stokes.set_xlabel('x', fontsize=9)
    ax_stokes.set_ylabel('y', fontsize=9)
    ax_stokes.set_zlabel('z', fontsize=9)
    ax_stokes.set_title('Teorema de Stokes', fontsize=11, fontweight='bold', color='#10b981')
    ax_stokes.view_init(elev=25, azim=45)
    ax_stokes.set_box_aspect([1, 1, 0.6])
    
    # =========================================
    # TEOREMA DE LA DIVERGENCIA (3D)
    # =========================================
    # Superficie cerrada (esfera deformada)
    u = np.linspace(0, 2*np.pi, 40)
    v = np.linspace(0, np.pi, 30)
    U, V = np.meshgrid(u, v)
    
    r_d = 1 + 0.2*np.sin(3*V)*np.cos(2*U)
    X_d = r_d * np.sin(V) * np.cos(U)
    Y_d = r_d * np.sin(V) * np.sin(U)
    Z_d = r_d * np.cos(V)
    
    ax_div.plot_surface(X_d, Y_d, Z_d, cmap='Blues', alpha=0.5, edgecolor='none')
    
    # Vectores normales saliendo de la superficie
    for ang in np.linspace(0, 2*np.pi, 8):
        for phi_ang in [np.pi/4, np.pi/2, 3*np.pi/4]:
            r_n = 1 + 0.2*np.sin(3*phi_ang)*np.cos(2*ang)
            x_n = r_n * np.sin(phi_ang) * np.cos(ang)
            y_n = r_n * np.sin(phi_ang) * np.sin(ang)
            z_n = r_n * np.cos(phi_ang)
            # Normal hacia afuera
            norm = np.array([x_n, y_n, z_n])
            norm = norm / np.linalg.norm(norm) * 0.3
            ax_div.quiver(x_n, y_n, z_n, norm[0], norm[1], norm[2],
                         color='#dc2626', alpha=0.7, arrow_length_ratio=0.3, linewidth=1)
    
    ax_div.text(0, 0, 0, 'E', fontsize=14, fontweight='bold', color='#3b82f6')
    ax_div.text(1.2, 0, 0.8, 'S', fontsize=12, fontweight='bold', color='#6b7280')
    
    ax_div.set_xlabel('x', fontsize=9)
    ax_div.set_ylabel('y', fontsize=9)
    ax_div.set_zlabel('z', fontsize=9)
    ax_div.set_title('Teorema de la Divergencia', fontsize=11, fontweight='bold', color='#3b82f6')
    ax_div.view_init(elev=20, azim=45)
    ax_div.set_box_aspect([1, 1, 1])
    
    # =========================================
    # PANELES INFO
    # =========================================
    for ax in [ax_green_info, ax_stokes_info, ax_div_info]:
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
    
    # Green
    ax_green_info.add_patch(plt.Rectangle((0.02, 0.02), 0.96, 0.96,
                                          facecolor='#eff6ff', edgecolor=colors['primary'],
                                          linewidth=2))
    ax_green_info.text(0.5, 0.85, 'TEOREMA DE GREEN', fontsize=10,
                      fontweight='bold', ha='center', color=colors['primary'])
    ax_green_info.text(0.5, 0.65, r'$\oint_C (P\,dx + Q\,dy) =$',
                      fontsize=11, ha='center', color=colors['text'])
    ax_green_info.text(0.5, 0.45, r'$\iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA$',
                      fontsize=11, ha='center', color=colors['text'])
    ax_green_info.text(0.5, 0.20, 'Relaciona integral de línea\ncon integral doble',
                      fontsize=9, ha='center', color='#6b7280')
    
    # Stokes
    ax_stokes_info.add_patch(plt.Rectangle((0.02, 0.02), 0.96, 0.96,
                                           facecolor='#f0fdf4', edgecolor='#10b981',
                                           linewidth=2))
    ax_stokes_info.text(0.5, 0.85, 'TEOREMA DE STOKES', fontsize=10,
                       fontweight='bold', ha='center', color='#10b981')
    ax_stokes_info.text(0.5, 0.65, r'$\oint_C \mathbf{F} \cdot d\mathbf{r} =$',
                       fontsize=11, ha='center', color=colors['text'])
    ax_stokes_info.text(0.5, 0.45, r'$\iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}$',
                       fontsize=11, ha='center', color=colors['text'])
    ax_stokes_info.text(0.5, 0.20, 'Relaciona circulación\ncon rotacional',
                       fontsize=9, ha='center', color='#6b7280')
    
    # Divergencia
    ax_div_info.add_patch(plt.Rectangle((0.02, 0.02), 0.96, 0.96,
                                        facecolor='#eff6ff', edgecolor='#3b82f6',
                                        linewidth=2))
    ax_div_info.text(0.5, 0.85, 'TEOREMA DIVERGENCIA', fontsize=10,
                    fontweight='bold', ha='center', color='#3b82f6')
    ax_div_info.text(0.5, 0.65, r'$\oiint_S \mathbf{F} \cdot d\mathbf{S} =$',
                    fontsize=11, ha='center', color=colors['text'])
    ax_div_info.text(0.5, 0.45, r'$\iiint_E (\nabla \cdot \mathbf{F}) \, dV$',
                    fontsize=11, ha='center', color=colors['text'])
    ax_div_info.text(0.5, 0.20, 'Relaciona flujo\ncon divergencia',
                    fontsize=9, ha='center', color='#6b7280')
    
    fig.suptitle('Teoremas Fundamentales del Cálculo Vectorial', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "teoremas_integrales.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'teoremas_integrales.svg'}")
