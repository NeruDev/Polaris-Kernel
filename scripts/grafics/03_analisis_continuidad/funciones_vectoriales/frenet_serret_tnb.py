# yaml_frontmatter:
#   id: 'frenet_serret_tnb'
#   title: 'Marco de Frenet-Serret: vectores T, N, B'
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
    
    fig = plt.figure(figsize=(14, 9), layout='constrained')
    gs = fig.add_gridspec(2, 2, height_ratios=[1.3, 1], hspace=0.15, wspace=0.12)
    
    ax_3d = fig.add_subplot(gs[0, :], projection='3d')
    ax_formulas = fig.add_subplot(gs[1, 0])
    ax_planos = fig.add_subplot(gs[1, 1])
    
    # =========================================
    # PANEL 3D: Curva con marco TNB
    # =========================================
    # Curva: hélice
    t = np.linspace(0, 3*np.pi, 150)
    a, b = 1.5, 0.25
    x = a * np.cos(t)
    y = a * np.sin(t)
    z = b * t
    
    ax_3d.plot(x, y, z, color=colors['primary'], linewidth=2.5, alpha=0.8)
    
    # Punto donde mostrar TNB
    t0 = 1.8 * np.pi
    P = np.array([a*np.cos(t0), a*np.sin(t0), b*t0])
    ax_3d.scatter(*P, color='#374151', s=100, zorder=5)
    ax_3d.text(P[0]-0.3, P[1]+0.3, P[2]+0.3, 'P', fontsize=12, fontweight='bold', color='#374151')
    
    # Calcular T, N, B para la hélice
    # r'(t) = <-a*sin(t), a*cos(t), b>
    r_prime = np.array([-a*np.sin(t0), a*np.cos(t0), b])
    speed = np.linalg.norm(r_prime)
    T = r_prime / speed
    
    # r''(t) = <-a*cos(t), -a*sin(t), 0>
    r_double = np.array([-a*np.cos(t0), -a*np.sin(t0), 0])
    
    # T'(t) = r''(t)/|r'(t)| - ... (usando la fórmula simplificada para hélice)
    # Para hélice: N siempre apunta hacia el eje z
    N = np.array([-np.cos(t0), -np.sin(t0), 0])
    
    # B = T × N
    B = np.cross(T, N)
    
    # Escalar para visualización
    scale = 1.0
    
    # Dibujar vectores TNB
    ax_3d.quiver(*P, *(T*scale), color='#dc2626', arrow_length_ratio=0.15, linewidth=3)
    ax_3d.quiver(*P, *(N*scale), color='#10b981', arrow_length_ratio=0.15, linewidth=3)
    ax_3d.quiver(*P, *(B*scale), color='#3b82f6', arrow_length_ratio=0.15, linewidth=3)
    
    # Etiquetas
    ax_3d.text(P[0]+T[0]*scale+0.15, P[1]+T[1]*scale+0.15, P[2]+T[2]*scale+0.1, 
              r'$\mathbf{T}$', fontsize=14, color='#dc2626', fontweight='bold')
    ax_3d.text(P[0]+N[0]*scale-0.3, P[1]+N[1]*scale, P[2]+N[2]*scale+0.1, 
              r'$\mathbf{N}$', fontsize=14, color='#10b981', fontweight='bold')
    ax_3d.text(P[0]+B[0]*scale+0.1, P[1]+B[1]*scale+0.15, P[2]+B[2]*scale+0.15, 
              r'$\mathbf{B}$', fontsize=14, color='#3b82f6', fontweight='bold')
    
    # Plano osculador (spanned by T and N)
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    plane_size = 0.8
    corners = [
        P + plane_size*T + plane_size*N,
        P + plane_size*T - plane_size*N,
        P - plane_size*T - plane_size*N,
        P - plane_size*T + plane_size*N,
    ]
    verts = [[c for c in corners]]
    poly = Poly3DCollection(verts, alpha=0.2, facecolor='#f59e0b', edgecolor='#f59e0b')
    ax_3d.add_collection3d(poly)
    ax_3d.text(P[0]+0.5, P[1]-0.8, P[2]+0.1, 'Plano\nosculador', fontsize=9, color='#f59e0b', ha='center')
    
    ax_3d.set_xlabel('X', fontsize=10)
    ax_3d.set_ylabel('Y', fontsize=10)
    ax_3d.set_zlabel('Z', fontsize=10)
    ax_3d.set_xlim([-2.5, 2.5])
    ax_3d.set_ylim([-2.5, 2.5])
    ax_3d.set_zlim([0, 3])
    ax_3d.set_box_aspect([1, 1, 0.6])
    ax_3d.view_init(elev=25, azim=40)
    ax_3d.xaxis.pane.fill = False
    ax_3d.yaxis.pane.fill = False
    ax_3d.zaxis.pane.fill = False
    ax_3d.set_title('Marco de Frenet-Serret en una Hélice', fontsize=11, fontweight='bold', pad=10)
    
    # =========================================
    # PANEL FÓRMULAS
    # =========================================
    ax_formulas.axis('off')
    ax_formulas.set_xlim(0, 1)
    ax_formulas.set_ylim(0, 1)
    
    # T
    ax_formulas.add_patch(plt.Rectangle((0.03, 0.70), 0.94, 0.27,
                                        facecolor='#fef2f2', edgecolor='#dc2626',
                                        linewidth=2))
    ax_formulas.text(0.5, 0.92, 'VECTOR TANGENTE UNITARIO', fontsize=10,
                    fontweight='bold', ha='center', color='#dc2626')
    ax_formulas.text(0.5, 0.80, r"$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}$",
                    fontsize=13, ha='center', color=colors['text'])
    
    # N
    ax_formulas.add_patch(plt.Rectangle((0.03, 0.38), 0.94, 0.28,
                                        facecolor='#f0fdf4', edgecolor='#10b981',
                                        linewidth=2))
    ax_formulas.text(0.5, 0.61, 'VECTOR NORMAL PRINCIPAL', fontsize=10,
                    fontweight='bold', ha='center', color='#10b981')
    ax_formulas.text(0.5, 0.48, r"$\mathbf{N}(t) = \frac{\mathbf{T}'(t)}{\|\mathbf{T}'(t)\|}$",
                    fontsize=13, ha='center', color=colors['text'])
    
    # B
    ax_formulas.add_patch(plt.Rectangle((0.03, 0.05), 0.94, 0.28,
                                        facecolor='#eff6ff', edgecolor='#3b82f6',
                                        linewidth=2))
    ax_formulas.text(0.5, 0.28, 'VECTOR BINORMAL', fontsize=10,
                    fontweight='bold', ha='center', color='#3b82f6')
    ax_formulas.text(0.5, 0.15, r'$\mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t)$',
                    fontsize=13, ha='center', color=colors['text'])
    
    # =========================================
    # PANEL PLANOS
    # =========================================
    ax_planos.axis('off')
    ax_planos.set_xlim(0, 1)
    ax_planos.set_ylim(0, 1)
    
    ax_planos.text(0.5, 0.95, 'PLANOS ASOCIADOS', fontsize=11,
                  fontweight='bold', ha='center', color='#374151')
    
    planos = [
        ('Osculador', r'$\mathbf{T}$ y $\mathbf{N}$', 'Plano de mejor ajuste local', '#f59e0b'),
        ('Normal', r'$\mathbf{N}$ y $\mathbf{B}$', 'Perpendicular a la tangente', '#8b5cf6'),
        ('Rectificante', r'$\mathbf{T}$ y $\mathbf{B}$', 'Perpendicular a la normal', '#06b6d4'),
    ]
    
    for i, (nombre, vectores, desc, color) in enumerate(planos):
        y_pos = 0.78 - i*0.28
        ax_planos.add_patch(plt.Rectangle((0.03, y_pos-0.02), 0.94, 0.24,
                                          facecolor=f'{color}15', edgecolor=color,
                                          linewidth=1.5))
        ax_planos.text(0.5, y_pos+0.17, f'Plano {nombre}', fontsize=10,
                      fontweight='bold', ha='center', color=color)
        ax_planos.text(0.5, y_pos+0.08, f'Generado por: {vectores}', fontsize=10,
                      ha='center', color=colors['text'])
        ax_planos.text(0.5, y_pos+0.00, desc, fontsize=9,
                      ha='center', color='#6b7280')
    
    fig.suptitle('Marco de Frenet-Serret (TNB)', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "frenet_serret_tnb.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'frenet_serret_tnb.svg'}")
