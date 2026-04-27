# yaml_frontmatter:
#   id: 'gradiente_derivada_direccional'
#   title: 'Gradiente y derivada direccional'
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


    setup_style,
    get_colors,
    get_output_dir_for_topic,
    save_figure,
)


def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig = plt.figure(figsize=(14, 7), layout='constrained')
    gs = fig.add_gridspec(1, 3, width_ratios=[1.3, 1.2, 0.9])
    
    ax_field = fig.add_subplot(gs[0])
    ax_dir = fig.add_subplot(gs[1])
    ax_info = fig.add_subplot(gs[2])
    
    # =========================================
    # Función: f(x,y) = x² + y² 
    # Gradiente: ∇f = (2x, 2y)
    # =========================================
    x = np.linspace(-2.5, 2.5, 20)
    y = np.linspace(-2.5, 2.5, 20)
    X, Y = np.meshgrid(x, y)
    
    # Gradiente
    U = 2*X
    V = 2*Y
    
    # Normalizar para visualización
    magnitude = np.sqrt(U**2 + V**2)
    magnitude[magnitude == 0] = 1
    U_norm = U / magnitude
    V_norm = V / magnitude
    
    # =========================================
    # PANEL 1: Campo de gradientes
    # =========================================
    ax_field.set_aspect('equal')
    
    # Curvas de nivel de fondo
    x_fine = np.linspace(-2.5, 2.5, 100)
    y_fine = np.linspace(-2.5, 2.5, 100)
    X_fine, Y_fine = np.meshgrid(x_fine, y_fine)
    Z_fine = X_fine**2 + Y_fine**2
    
    ax_field.contourf(X_fine, Y_fine, Z_fine, levels=15, cmap='viridis', alpha=0.4)
    cs = ax_field.contour(X_fine, Y_fine, Z_fine, levels=[1, 2, 3, 4, 5], colors='gray', linewidths=1)
    ax_field.clabel(cs, inline=True, fontsize=8, fmt='%.0f')
    
    # Campo de vectores gradiente (normalizado)
    ax_field.quiver(X, Y, U_norm, V_norm, magnitude, cmap='Reds', alpha=0.8,
                   scale=25, width=0.004)
    
    # Punto destacado
    P = np.array([1.5, 1])
    grad_P = np.array([2*P[0], 2*P[1]])
    grad_P_norm = grad_P / np.linalg.norm(grad_P)
    
    ax_field.plot(*P, 'o', color=colors['accent'], markersize=12, zorder=5)
    ax_field.annotate('', xy=P + grad_P_norm*0.8, xytext=P,
                     arrowprops=dict(arrowstyle='->', color='#dc2626', lw=3))
    ax_field.text(P[0]+0.15, P[1]-0.3, 'P', fontsize=11, fontweight='bold', color=colors['accent'])
    ax_field.text(P[0]+grad_P_norm[0]*0.8+0.1, P[1]+grad_P_norm[1]*0.8+0.1, r'$\nabla f$', 
                 fontsize=11, fontweight='bold', color='#dc2626')
    
    ax_field.set_xlabel('x', fontsize=11)
    ax_field.set_ylabel('y', fontsize=11)
    ax_field.set_title(r'Campo gradiente $\nabla f = (2x, 2y)$', fontsize=11, fontweight='bold')
    ax_field.grid(True, linestyle='--', alpha=0.3)
    
    # =========================================
    # PANEL 2: Derivada direccional
    # =========================================
    ax_dir.set_aspect('equal')
    
    # Curvas de nivel
    ax_dir.contour(X_fine, Y_fine, Z_fine, levels=[1, 2, 3, 4, 5], colors='gray', 
                  linewidths=1, alpha=0.7)
    
    # Punto P
    ax_dir.plot(*P, 'o', color=colors['accent'], markersize=12, zorder=5)
    ax_dir.text(P[0]+0.1, P[1]-0.25, 'P', fontsize=11, fontweight='bold', color=colors['accent'])
    
    # Gradiente
    scale = 0.5
    ax_dir.annotate('', xy=P + grad_P_norm*scale, xytext=P,
                   arrowprops=dict(arrowstyle='->', color='#dc2626', lw=3))
    ax_dir.text(P[0]+grad_P_norm[0]*scale+0.1, P[1]+grad_P_norm[1]*scale+0.1, 
               r'$\nabla f$', fontsize=11, fontweight='bold', color='#dc2626')
    
    # Diferentes direcciones u
    angles = [0, np.pi/6, np.pi/3, np.pi/2, 2*np.pi/3, np.pi]
    dir_colors = ['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899', '#6b7280']
    
    for ang, col in zip(angles, dir_colors):
        u = np.array([np.cos(ang), np.sin(ang)])
        ax_dir.annotate('', xy=P + u*scale*0.7, xytext=P,
                       arrowprops=dict(arrowstyle='->', color=col, lw=2, alpha=0.8))
    
    # Etiqueta para dirección de máximo crecimiento
    ax_dir.text(1.8, 2.2, 'Máx crecimiento', fontsize=9, color='#dc2626', fontweight='bold')
    ax_dir.annotate('', xy=P + grad_P_norm*0.3, xytext=(1.75, 2.1),
                   arrowprops=dict(arrowstyle='->', color='#dc2626', lw=1))
    
    # Círculo unitario centrado en P (para mostrar direcciones)
    theta = np.linspace(0, 2*np.pi, 100)
    ax_dir.plot(P[0] + 0.3*np.cos(theta), P[1] + 0.3*np.sin(theta), 
               '--', color='#9ca3af', linewidth=1, alpha=0.5)
    
    ax_dir.set_xlabel('x', fontsize=11)
    ax_dir.set_ylabel('y', fontsize=11)
    ax_dir.set_title('Derivada direccional', fontsize=11, fontweight='bold')
    ax_dir.set_xlim([0, 2.5])
    ax_dir.set_ylim([0, 2.5])
    ax_dir.grid(True, linestyle='--', alpha=0.3)
    
    # =========================================
    # PANEL INFO
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Gradiente
    ax_info.add_patch(plt.Rectangle((0.02, 0.75), 0.96, 0.23,
                                    facecolor='#fef2f2', edgecolor='#dc2626',
                                    linewidth=2))
    ax_info.text(0.5, 0.94, 'GRADIENTE', fontsize=10,
                fontweight='bold', ha='center', color='#dc2626')
    ax_info.text(0.5, 0.82, r'$\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$',
                fontsize=11, ha='center', color=colors['text'])
    
    # Derivada direccional
    ax_info.add_patch(plt.Rectangle((0.02, 0.48), 0.96, 0.24,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=2))
    ax_info.text(0.5, 0.68, 'DERIVADA DIRECCIONAL', fontsize=9,
                fontweight='bold', ha='center', color=colors['primary'])
    ax_info.text(0.5, 0.55, r'$D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}$',
                fontsize=12, ha='center', color=colors['text'])
    
    # Propiedades
    ax_info.add_patch(plt.Rectangle((0.02, 0.12), 0.96, 0.32,
                                    facecolor='#f0fdf4', edgecolor='#10b981',
                                    linewidth=1.5))
    ax_info.text(0.5, 0.40, 'PROPIEDADES', fontsize=9,
                fontweight='bold', ha='center', color='#10b981')
    ax_info.text(0.5, 0.32, r'$\|\nabla f\| = $ tasa máx. crecimiento',
                fontsize=9, ha='center', color=colors['text'])
    ax_info.text(0.5, 0.24, r'Dirección de $\nabla f$: máx. crecimiento',
                fontsize=9, ha='center', color=colors['text'])
    ax_info.text(0.5, 0.16, r'$\nabla f \perp$ curvas de nivel',
                fontsize=9, ha='center', color=colors['text'])
    
    fig.suptitle('Gradiente y Derivada Direccional', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "gradiente_derivada_direccional.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'gradiente_derivada_direccional.svg'}")
