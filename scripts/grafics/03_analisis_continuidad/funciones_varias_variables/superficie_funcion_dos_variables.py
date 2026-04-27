# yaml_frontmatter:
#   id: 'superficie_funcion_dos_variables'
#   title: 'Superficie z=f(x,y), dominio y rango'
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
    gs = fig.add_gridspec(2, 3, height_ratios=[1.4, 1], width_ratios=[1.3, 1.3, 0.8])
    
    ax_3d = fig.add_subplot(gs[0, :2], projection='3d')
    ax_dom = fig.add_subplot(gs[1, 0])
    ax_range = fig.add_subplot(gs[1, 1])
    ax_info = fig.add_subplot(gs[:, 2])
    
    # =========================================
    # PANEL 3D: Superficie
    # =========================================
    # Función: z = sin(sqrt(x² + y²))
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    
    # Superficie
    surf = ax_3d.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, 
                              edgecolor='none', linewidth=0)
    
    # Punto ejemplo
    x0, y0 = 1.5, 1.0
    z0 = np.sin(np.sqrt(x0**2 + y0**2))
    ax_3d.scatter([x0], [y0], [z0], color=colors['accent'], s=100, zorder=5)
    
    # Línea vertical desde dominio hasta superficie
    ax_3d.plot([x0, x0], [y0, y0], [-1.2, z0], '--', color=colors['accent'], linewidth=1.5)
    
    # Proyección del punto en el plano z=mínimo
    ax_3d.scatter([x0], [y0], [-1.2], color=colors['accent'], s=60, marker='x')
    
    ax_3d.set_xlabel('X', fontsize=10)
    ax_3d.set_ylabel('Y', fontsize=10)
    ax_3d.set_zlabel('Z = f(x,y)', fontsize=10)
    ax_3d.set_title(r'Superficie $z = \sin(\sqrt{x^2+y^2})$', fontsize=11, fontweight='bold')
    ax_3d.view_init(elev=25, azim=45)
    ax_3d.set_box_aspect([1, 1, 0.6])
    
    # =========================================
    # PANEL DOMINIO
    # =========================================
    ax_dom.set_aspect('equal')
    ax_dom.grid(True, linestyle='--', alpha=0.3)
    
    # Dominio circular
    theta = np.linspace(0, 2*np.pi, 100)
    ax_dom.fill(3*np.cos(theta), 3*np.sin(theta), color='#dbeafe', alpha=0.5, 
               edgecolor=colors['primary'], linewidth=2, label='Dominio D')
    
    # Punto (x₀, y₀)
    ax_dom.plot(x0, y0, 'o', color=colors['accent'], markersize=10, zorder=5)
    ax_dom.text(x0+0.2, y0+0.2, f'({x0}, {y0})', fontsize=10, color=colors['accent'])
    
    # Etiquetas
    ax_dom.text(0, 0, 'D', fontsize=14, fontweight='bold', ha='center', va='center',
               color=colors['primary'])
    
    ax_dom.set_xlabel('x', fontsize=11)
    ax_dom.set_ylabel('y', fontsize=11)
    ax_dom.set_title(r'Dominio $D \subseteq \mathbb{R}^2$', fontsize=11, fontweight='bold')
    ax_dom.set_xlim([-4, 4])
    ax_dom.set_ylim([-4, 4])
    ax_dom.axhline(y=0, color='k', linewidth=0.5)
    ax_dom.axvline(x=0, color='k', linewidth=0.5)
    
    # =========================================
    # PANEL RANGO
    # =========================================
    ax_range.grid(True, linestyle='--', alpha=0.3, axis='y')
    
    # Rango [-1, 1] para sin
    ax_range.fill_betweenx([-1, 1], 0, 1, color='#f0fdf4', alpha=0.5, 
                          edgecolor='#10b981', linewidth=2)
    
    # Valor z₀
    ax_range.axhline(y=z0, color=colors['accent'], linewidth=2, linestyle='--')
    ax_range.plot(0.5, z0, 'o', color=colors['accent'], markersize=10, zorder=5)
    ax_range.text(0.6, z0+0.1, f'z₀ = {z0:.2f}', fontsize=10, color=colors['accent'])
    
    ax_range.set_xlim([0, 1])
    ax_range.set_ylim([-1.5, 1.5])
    ax_range.set_ylabel('z', fontsize=11)
    ax_range.set_title(r'Rango $\subseteq \mathbb{R}$', fontsize=11, fontweight='bold')
    ax_range.set_xticks([])
    
    # Flecha indicando el rango
    ax_range.annotate('', xy=(0.5, 1), xytext=(0.5, -1),
                     arrowprops=dict(arrowstyle='<->', color='#10b981', lw=2))
    ax_range.text(0.55, 0, 'Rango', fontsize=10, color='#10b981', rotation=90, va='center')
    
    # =========================================
    # PANEL INFO
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Definición
    ax_info.add_patch(plt.Rectangle((0.02, 0.75), 0.96, 0.23,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=2))
    ax_info.text(0.5, 0.94, 'DEFINICIÓN', fontsize=10,
                fontweight='bold', ha='center', color=colors['primary'])
    ax_info.text(0.5, 0.84, r'$f: D \subseteq \mathbb{R}^2 \to \mathbb{R}$',
                fontsize=12, ha='center', color=colors['text'])
    ax_info.text(0.5, 0.77, r'$(x, y) \mapsto z = f(x, y)$',
                fontsize=11, ha='center', color=colors['text'])
    
    # Dominio
    ax_info.add_patch(plt.Rectangle((0.02, 0.50), 0.96, 0.22,
                                    facecolor='#dbeafe', edgecolor=colors['primary'],
                                    linewidth=1.5))
    ax_info.text(0.5, 0.68, 'DOMINIO', fontsize=9,
                fontweight='bold', ha='center', color=colors['primary'])
    ax_info.text(0.5, 0.57, r'$D = \{(x,y) \in \mathbb{R}^2 : f(x,y)$ definida$\}$',
                fontsize=9, ha='center', color=colors['text'])
    
    # Rango
    ax_info.add_patch(plt.Rectangle((0.02, 0.25), 0.96, 0.22,
                                    facecolor='#f0fdf4', edgecolor='#10b981',
                                    linewidth=1.5))
    ax_info.text(0.5, 0.43, 'RANGO', fontsize=9,
                fontweight='bold', ha='center', color='#10b981')
    ax_info.text(0.5, 0.32, r'$\{z \in \mathbb{R} : z = f(x,y),\, (x,y) \in D\}$',
                fontsize=9, ha='center', color=colors['text'])
    
    # Gráfica
    ax_info.text(0.5, 0.15, 'SUPERFICIE (GRÁFICA)', fontsize=9,
                fontweight='bold', ha='center', color='#8b5cf6')
    ax_info.text(0.5, 0.06, r'$S = \{(x,y,z): z=f(x,y),\, (x,y)\in D\}$',
                fontsize=9, ha='center', color=colors['text'])
    
    fig.suptitle('Función de Dos Variables y su Gráfica', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "superficie_funcion_dos_variables.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'superficie_funcion_dos_variables.svg'}")
