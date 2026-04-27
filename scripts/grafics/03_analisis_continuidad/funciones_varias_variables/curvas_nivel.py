# yaml_frontmatter:
#   id: 'curvas_nivel'
#   title: 'Curvas de nivel y mapa de contorno'
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
    
    fig = plt.figure(figsize=(14, 7), layout='constrained')
    gs = fig.add_gridspec(1, 3, width_ratios=[1.3, 1.3, 0.8])
    
    ax_3d = fig.add_subplot(gs[0], projection='3d')
    ax_contour = fig.add_subplot(gs[1])
    ax_info = fig.add_subplot(gs[2])
    
    # =========================================
    # Función: z = x² + y² (paraboloide)
    # =========================================
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2
    
    # =========================================
    # PANEL 3D: Superficie con curvas de nivel
    # =========================================
    # Superficie transparente
    ax_3d.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, 
                      edgecolor='none', linewidth=0)
    
    # Curvas de nivel en la superficie
    levels = [0.5, 1, 2, 3, 4]
    cmap = plt.cm.plasma
    
    for i, c in enumerate(levels):
        # Círculo de radio sqrt(c)
        r = np.sqrt(c)
        theta = np.linspace(0, 2*np.pi, 100)
        x_curve = r * np.cos(theta)
        y_curve = r * np.sin(theta)
        z_curve = np.full_like(theta, c)
        
        color = cmap(i / len(levels))
        ax_3d.plot(x_curve, y_curve, z_curve, color=color, linewidth=2.5)
        
        # Línea vertical de proyección
        ax_3d.plot([r, r], [0, 0], [0, c], '--', color=color, alpha=0.5, linewidth=1)
    
    # Proyecciones en z=0
    for i, c in enumerate(levels):
        r = np.sqrt(c)
        theta = np.linspace(0, 2*np.pi, 100)
        x_curve = r * np.cos(theta)
        y_curve = r * np.sin(theta)
        z_curve = np.zeros_like(theta)
        
        color = cmap(i / len(levels))
        ax_3d.plot(x_curve, y_curve, z_curve, '--', color=color, linewidth=1.5, alpha=0.7)
    
    ax_3d.set_xlabel('X', fontsize=10)
    ax_3d.set_ylabel('Y', fontsize=10)
    ax_3d.set_zlabel('Z', fontsize=10)
    ax_3d.set_title(r'$z = x^2 + y^2$ con curvas de nivel', fontsize=11, fontweight='bold')
    ax_3d.view_init(elev=25, azim=45)
    ax_3d.set_box_aspect([1, 1, 0.8])
    
    # =========================================
    # PANEL CONTORNO: Mapa de curvas de nivel
    # =========================================
    ax_contour.set_aspect('equal')
    
    # Curvas de nivel rellenas
    cf = ax_contour.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.7)
    
    # Curvas de nivel con etiquetas
    cs = ax_contour.contour(X, Y, Z, levels=levels, colors='black', linewidths=1.5)
    ax_contour.clabel(cs, inline=True, fontsize=9, fmt='%.1f')
    
    # Colorbar
    cbar = plt.colorbar(cf, ax=ax_contour, shrink=0.8)
    cbar.set_label('z = f(x,y)', fontsize=10)
    
    ax_contour.set_xlabel('x', fontsize=11)
    ax_contour.set_ylabel('y', fontsize=11)
    ax_contour.set_title('Mapa de Contorno (vista superior)', fontsize=11, fontweight='bold')
    ax_contour.grid(True, linestyle='--', alpha=0.3)
    
    # =========================================
    # PANEL INFO
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Definición
    ax_info.add_patch(plt.Rectangle((0.02, 0.75), 0.96, 0.22,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=2))
    ax_info.text(0.5, 0.93, 'CURVA DE NIVEL', fontsize=10,
                fontweight='bold', ha='center', color=colors['primary'])
    ax_info.text(0.5, 0.82, r'$\{(x,y) \in D : f(x,y) = c\}$',
                fontsize=12, ha='center', color=colors['text'])
    
    # Propiedades
    ax_info.add_patch(plt.Rectangle((0.02, 0.42), 0.96, 0.30,
                                    facecolor='#f0fdf4', edgecolor='#10b981',
                                    linewidth=1.5))
    ax_info.text(0.5, 0.68, 'PROPIEDADES', fontsize=9,
                fontweight='bold', ha='center', color='#10b981')
    ax_info.text(0.5, 0.58, '• Puntos de igual altura', fontsize=9, ha='center', color=colors['text'])
    ax_info.text(0.5, 0.50, '• No se cruzan', fontsize=9, ha='center', color=colors['text'])
    ax_info.text(0.5, 0.44, '• ∇f perpendicular a curva', fontsize=9, ha='center', color=colors['text'])
    
    # Ejemplo
    ax_info.add_patch(plt.Rectangle((0.02, 0.12), 0.96, 0.26,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=1.5))
    ax_info.text(0.5, 0.34, 'EJEMPLO', fontsize=9,
                fontweight='bold', ha='center', color='#f59e0b')
    ax_info.text(0.5, 0.24, r'$f(x,y) = x^2 + y^2$',
                fontsize=11, ha='center', color=colors['text'])
    ax_info.text(0.5, 0.15, r'Niveles: círculos $x^2+y^2=c$',
                fontsize=9, ha='center', color=colors['text'])
    
    fig.suptitle('Curvas de Nivel', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "curvas_nivel.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'curvas_nivel.svg'}")
