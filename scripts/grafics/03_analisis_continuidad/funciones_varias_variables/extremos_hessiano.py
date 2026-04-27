# yaml_frontmatter:
#   id: 'extremos_hessiano'
#   title: 'Puntos críticos y criterio de la segunda derivada'
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
    
    fig = plt.figure(figsize=(15, 9), layout='constrained')
    gs = fig.add_gridspec(2, 4, height_ratios=[1.2, 1])
    
    # =========================================
    # Fila 1: Tres tipos de puntos críticos
    # =========================================
    ax_min = fig.add_subplot(gs[0, 0], projection='3d')
    ax_max = fig.add_subplot(gs[0, 1], projection='3d')
    ax_saddle = fig.add_subplot(gs[0, 2], projection='3d')
    ax_info = fig.add_subplot(gs[0, 3])
    
    x = np.linspace(-2, 2, 80)
    y = np.linspace(-2, 2, 80)
    X, Y = np.meshgrid(x, y)
    
    # MÍNIMO: z = x² + y²
    Z_min = X**2 + Y**2
    ax_min.plot_surface(X, Y, Z_min, cmap='Greens', alpha=0.8, edgecolor='none')
    ax_min.scatter([0], [0], [0], color='#10b981', s=100, zorder=5)
    ax_min.set_title('Mínimo Local', fontsize=10, fontweight='bold', color='#10b981')
    ax_min.set_xlabel('x', fontsize=9)
    ax_min.set_ylabel('y', fontsize=9)
    ax_min.set_zlabel('z', fontsize=9)
    ax_min.view_init(elev=25, azim=45)
    ax_min.set_box_aspect([1, 1, 0.6])
    
    # MÁXIMO: z = -x² - y²
    Z_max = -X**2 - Y**2
    ax_max.plot_surface(X, Y, Z_max, cmap='Reds', alpha=0.8, edgecolor='none')
    ax_max.scatter([0], [0], [0], color='#dc2626', s=100, zorder=5)
    ax_max.set_title('Máximo Local', fontsize=10, fontweight='bold', color='#dc2626')
    ax_max.set_xlabel('x', fontsize=9)
    ax_max.set_ylabel('y', fontsize=9)
    ax_max.set_zlabel('z', fontsize=9)
    ax_max.view_init(elev=25, azim=45)
    ax_max.set_box_aspect([1, 1, 0.6])
    
    # PUNTO DE SILLA: z = x² - y²
    Z_saddle = X**2 - Y**2
    ax_saddle.plot_surface(X, Y, Z_saddle, cmap='coolwarm', alpha=0.8, edgecolor='none')
    ax_saddle.scatter([0], [0], [0], color='#8b5cf6', s=100, zorder=5)
    ax_saddle.set_title('Punto de Silla', fontsize=10, fontweight='bold', color='#8b5cf6')
    ax_saddle.set_xlabel('x', fontsize=9)
    ax_saddle.set_ylabel('y', fontsize=9)
    ax_saddle.set_zlabel('z', fontsize=9)
    ax_saddle.view_init(elev=25, azim=45)
    ax_saddle.set_box_aspect([1, 1, 0.6])
    
    # =========================================
    # PANEL INFO (fila 1)
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    ax_info.add_patch(plt.Rectangle((0.02, 0.55), 0.96, 0.42,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=2))
    ax_info.text(0.5, 0.93, 'HESSIANO', fontsize=11,
                fontweight='bold', ha='center', color=colors['primary'])
    ax_info.text(0.5, 0.80, r'$H_{ij} = f_{x_ix_j}$  (matriz de segundas derivadas)',
                fontsize=10, ha='center', color=colors['text'])
    ax_info.text(0.5, 0.63, r'$D = f_{xx}f_{yy} - (f_{xy})^2 = \det(H)$',
                fontsize=11, ha='center', color=colors['text'])
    
    # Criterios
    ax_info.add_patch(plt.Rectangle((0.02, 0.02), 0.96, 0.50,
                                    facecolor='#fafafa', edgecolor='#9ca3af',
                                    linewidth=1.5))
    ax_info.text(0.5, 0.48, 'CRITERIO', fontsize=10,
                fontweight='bold', ha='center', color='#374151')
    ax_info.text(0.5, 0.38, r'$D > 0, f_{xx} > 0 \Rightarrow$ Mínimo',
                fontsize=9, ha='center', color='#10b981')
    ax_info.text(0.5, 0.28, r'$D > 0, f_{xx} < 0 \Rightarrow$ Máximo',
                fontsize=9, ha='center', color='#dc2626')
    ax_info.text(0.5, 0.18, r'$D < 0 \Rightarrow$ Punto de silla',
                fontsize=9, ha='center', color='#8b5cf6')
    ax_info.text(0.5, 0.08, r'$D = 0 \Rightarrow$ Inconcluso',
                fontsize=9, ha='center', color='#6b7280')
    
    # =========================================
    # Fila 2: Curvas de nivel para cada caso
    # =========================================
    ax_cont_min = fig.add_subplot(gs[1, 0])
    ax_cont_max = fig.add_subplot(gs[1, 1])
    ax_cont_saddle = fig.add_subplot(gs[1, 2])
    ax_process = fig.add_subplot(gs[1, 3])
    
    # Contornos - Mínimo
    ax_cont_min.set_aspect('equal')
    cs = ax_cont_min.contour(X, Y, Z_min, levels=8, cmap='Greens')
    ax_cont_min.clabel(cs, inline=True, fontsize=8)
    ax_cont_min.plot(0, 0, 'o', color='#10b981', markersize=10)
    ax_cont_min.set_title(r'$z = x^2 + y^2$', fontsize=10)
    ax_cont_min.set_xlabel('x', fontsize=9)
    ax_cont_min.set_ylabel('y', fontsize=9)
    ax_cont_min.grid(True, linestyle='--', alpha=0.3)
    ax_cont_min.text(0.1, -1.8, 'D > 0, fxx > 0', fontsize=8, color='#10b981', fontweight='bold')
    
    # Contornos - Máximo  
    ax_cont_max.set_aspect('equal')
    cs = ax_cont_max.contour(X, Y, Z_max, levels=8, cmap='Reds_r')
    ax_cont_max.clabel(cs, inline=True, fontsize=8)
    ax_cont_max.plot(0, 0, 'o', color='#dc2626', markersize=10)
    ax_cont_max.set_title(r'$z = -x^2 - y^2$', fontsize=10)
    ax_cont_max.set_xlabel('x', fontsize=9)
    ax_cont_max.set_ylabel('y', fontsize=9)
    ax_cont_max.grid(True, linestyle='--', alpha=0.3)
    ax_cont_max.text(0.1, -1.8, 'D > 0, fxx < 0', fontsize=8, color='#dc2626', fontweight='bold')
    
    # Contornos - Punto de silla
    ax_cont_saddle.set_aspect('equal')
    cs = ax_cont_saddle.contour(X, Y, Z_saddle, levels=[-3, -2, -1, 0, 1, 2, 3], cmap='coolwarm')
    ax_cont_saddle.clabel(cs, inline=True, fontsize=8)
    ax_cont_saddle.plot(0, 0, 'o', color='#8b5cf6', markersize=10)
    ax_cont_saddle.set_title(r'$z = x^2 - y^2$', fontsize=10)
    ax_cont_saddle.set_xlabel('x', fontsize=9)
    ax_cont_saddle.set_ylabel('y', fontsize=9)
    ax_cont_saddle.grid(True, linestyle='--', alpha=0.3)
    ax_cont_saddle.text(0.1, -1.8, 'D < 0', fontsize=8, color='#8b5cf6', fontweight='bold')
    
    # =========================================
    # PROCESO (fila 2)
    # =========================================
    ax_process.axis('off')
    ax_process.set_xlim(0, 1)
    ax_process.set_ylim(0, 1)
    
    ax_process.add_patch(plt.Rectangle((0.02, 0.02), 0.96, 0.96,
                                       facecolor='#fef3c7', edgecolor='#f59e0b',
                                       linewidth=2))
    ax_process.text(0.5, 0.92, 'PROCESO', fontsize=11,
                   fontweight='bold', ha='center', color='#f59e0b')
    
    steps = [
        '1. Calcular ∇f = 0',
        '2. Encontrar puntos críticos',
        '3. Calcular Hessiano H',
        '4. Evaluar D = det(H)',
        '5. Aplicar criterio'
    ]
    
    for i, step in enumerate(steps):
        y_pos = 0.78 - i*0.14
        ax_process.text(0.08, y_pos, step, fontsize=9, color=colors['text'], va='center')
    
    fig.suptitle('Extremos y Criterio del Hessiano', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "extremos_hessiano.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'extremos_hessiano.svg'}")
