# yaml_frontmatter:
#   id: 'solidos_geometricos'
#   title: 'Sólidos: prisma, pirámide, cilindro, cono, esfera'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria']

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[3]))
from templates import setup_style, get_colors
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig = plt.figure(figsize=(16, 10))
    
    # === Prisma Rectangular ===
    ax1 = fig.add_subplot(2, 3, 1, projection='3d')
    
    # Vértices del prisma
    vertices = [
        [0, 0, 0], [1, 0, 0], [1, 0.6, 0], [0, 0.6, 0],  # base inferior
        [0, 0, 1.2], [1, 0, 1.2], [1, 0.6, 1.2], [0, 0.6, 1.2]  # base superior
    ]
    
    # Caras
    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # frontal
        [vertices[1], vertices[2], vertices[6], vertices[5]],  # derecha
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # trasera
        [vertices[3], vertices[0], vertices[4], vertices[7]],  # izquierda
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # inferior
        [vertices[4], vertices[5], vertices[6], vertices[7]],  # superior
    ]
    
    ax1.add_collection3d(Poly3DCollection(faces, alpha=0.3, facecolor=colors['primary'],
                                          edgecolor=colors['primary'], linewidth=1))
    ax1.set_title('PRISMA', fontsize=11, fontweight='bold', pad=5)
    ax1.text2D(0.5, -0.05, r'$V = A_b \cdot h$', fontsize=10, ha='center', 
               transform=ax1.transAxes)
    
    # === Pirámide ===
    ax2 = fig.add_subplot(2, 3, 2, projection='3d')
    
    # Base cuadrada y vértice
    base = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]]
    apex = [0.5, 0.5, 1.3]
    
    # Caras de la pirámide
    pyr_faces = [
        [base[0], base[1], apex],
        [base[1], base[2], apex],
        [base[2], base[3], apex],
        [base[3], base[0], apex],
        base  # base
    ]
    
    ax2.add_collection3d(Poly3DCollection(pyr_faces, alpha=0.3, facecolor=colors['secondary'],
                                          edgecolor=colors['secondary'], linewidth=1))
    ax2.set_title('PIRÁMIDE', fontsize=11, fontweight='bold', pad=5)
    ax2.text2D(0.5, -0.05, r'$V = \frac{1}{3} A_b \cdot h$', fontsize=10, ha='center',
               transform=ax2.transAxes)
    
    # === Cilindro ===
    ax3 = fig.add_subplot(2, 3, 3, projection='3d')
    
    # Parámetros del cilindro
    z = np.linspace(0, 1.2, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    r = 0.5
    x_grid = r * np.cos(theta_grid)
    y_grid = r * np.sin(theta_grid)
    
    ax3.plot_surface(x_grid, y_grid, z_grid, alpha=0.3, color=colors['accent'])
    
    # Tapas
    theta_circle = np.linspace(0, 2*np.pi, 50)
    x_circle = r * np.cos(theta_circle)
    y_circle = r * np.sin(theta_circle)
    ax3.plot(x_circle, y_circle, np.zeros_like(x_circle), color=colors['accent'], lw=1.5)
    ax3.plot(x_circle, y_circle, np.ones_like(x_circle)*1.2, color=colors['accent'], lw=1.5)
    
    ax3.set_title('CILINDRO', fontsize=11, fontweight='bold', pad=5)
    ax3.text2D(0.5, -0.05, r'$V = \pi r^2 h$', fontsize=10, ha='center',
               transform=ax3.transAxes)
    
    # === Cono ===
    ax4 = fig.add_subplot(2, 3, 4, projection='3d')
    
    # Parámetros del cono
    z_cone = np.linspace(0, 1.3, 50)
    theta_cone = np.linspace(0, 2*np.pi, 50)
    theta_grid_c, z_grid_c = np.meshgrid(theta_cone, z_cone)
    r_cone = 0.5 * (1 - z_grid_c/1.3)  # radio decrece con la altura
    x_cone = r_cone * np.cos(theta_grid_c)
    y_cone = r_cone * np.sin(theta_grid_c)
    
    ax4.plot_surface(x_cone, y_cone, z_grid_c, alpha=0.3, color=colors['tertiary'])
    
    # Base circular
    ax4.plot(0.5*np.cos(theta_circle), 0.5*np.sin(theta_circle), 
             np.zeros_like(theta_circle), color=colors['tertiary'], lw=1.5)
    
    ax4.set_title('CONO', fontsize=11, fontweight='bold', pad=5)
    ax4.text2D(0.5, -0.05, r'$V = \frac{1}{3} \pi r^2 h$', fontsize=10, ha='center',
               transform=ax4.transAxes)
    
    # === Esfera ===
    ax5 = fig.add_subplot(2, 3, 5, projection='3d')
    
    # Parámetros de la esfera
    u = np.linspace(0, 2*np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    r_sphere = 0.6
    x_sphere = r_sphere * np.outer(np.cos(u), np.sin(v))
    y_sphere = r_sphere * np.outer(np.sin(u), np.sin(v))
    z_sphere = r_sphere * np.outer(np.ones(np.size(u)), np.cos(v))
    
    ax5.plot_surface(x_sphere, y_sphere, z_sphere + 0.6, alpha=0.3, color='#ec4899')
    
    ax5.set_title('ESFERA', fontsize=11, fontweight='bold', pad=5)
    ax5.text2D(0.5, -0.05, r'$V = \frac{4}{3} \pi r^3$', fontsize=10, ha='center',
               transform=ax5.transAxes)
    
    # === Resumen de fórmulas ===
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.axis('off')
    
    formulas_text =     
    ax6.text(0.1, 0.95, formulas_text, fontsize=11, verticalalignment='top',
             fontfamily='monospace', color='#1f2937',
             bbox=dict(boxstyle='round', facecolor='#f3f4f6', edgecolor='#d1d5db'))
    
    # Configurar ejes 3D
    for ax in [ax1, ax2, ax3, ax4, ax5]:
        ax.set_xlim(-0.8, 1.2)
        ax.set_ylim(-0.8, 1.2)
        ax.set_zlim(0, 1.5)
        ax.set_box_aspect([1, 1, 1.2])
        ax.axis('off')
    
    fig.suptitle('Sólidos Geométricos', fontsize=14, fontweight='bold', y=0.98)
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "solidos_geometricos.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'solidos_geometricos.svg'}")
