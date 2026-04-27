# yaml_frontmatter:
#   id: 'aceleracion_componentes'
#   title: 'Componentes tangencial y normal de la aceleración'
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
    
    fig = plt.figure(figsize=(14, 8), layout='constrained')
    gs = fig.add_gridspec(1, 3, width_ratios=[1.3, 1.3, 0.9])
    
    ax_3d = fig.add_subplot(gs[0], projection='3d')
    ax_2d = fig.add_subplot(gs[1])
    ax_info = fig.add_subplot(gs[2])
    
    # =========================================
    # PANEL 1: Vista 3D - Hélice
    # =========================================
    # Hélice: r(t) = (cos(t), sin(t), t/2)
    t = np.linspace(0, 3*np.pi, 300)
    x = np.cos(t)
    y = np.sin(t)
    z = t / 2
    
    ax_3d.plot(x, y, z, color=colors['primary'], linewidth=2.5, label='Trayectoria')
    
    # Punto de análisis
    t0 = np.pi
    P = np.array([np.cos(t0), np.sin(t0), t0/2])
    ax_3d.scatter(*P, color=colors['accent'], s=100, zorder=5)
    
    # Velocidad: v = (-sin(t), cos(t), 1/2)
    v = np.array([-np.sin(t0), np.cos(t0), 0.5])
    v_norm = np.linalg.norm(v)
    T = v / v_norm  # Tangente unitario
    
    # Aceleración: a = (-cos(t), -sin(t), 0)
    a = np.array([-np.cos(t0), -np.sin(t0), 0])
    
    # Componentes
    a_T_scalar = np.dot(a, T)  # Componente tangencial (escalar)
    a_T = a_T_scalar * T       # Componente tangencial (vector)
    a_N = a - a_T              # Componente normal (vector)
    
    scale = 1.0
    
    # Dibujar vectores
    ax_3d.quiver(*P, *v*scale*0.7, color=colors['primary'], arrow_length_ratio=0.12, linewidth=2.5, label='v (velocidad)')
    ax_3d.quiver(*P, *a*scale, color='#dc2626', arrow_length_ratio=0.12, linewidth=2.5, label='a (aceleración)')
    ax_3d.quiver(*P, *a_N*scale, color='#10b981', arrow_length_ratio=0.12, linewidth=2.5, label=r'$a_N$ (normal)')
    
    ax_3d.set_xlabel('X', fontsize=10)
    ax_3d.set_ylabel('Y', fontsize=10)
    ax_3d.set_zlabel('Z', fontsize=10)
    ax_3d.set_title('Hélice con aceleración', fontsize=11, fontweight='bold')
    ax_3d.view_init(elev=25, azim=45)
    ax_3d.legend(loc='upper left', fontsize=8)
    
    # =========================================
    # PANEL 2: Vista 2D - Detalle
    # =========================================
    ax_2d.set_aspect('equal')
    ax_2d.grid(True, linestyle='--', alpha=0.3)
    
    # Curva circular en el plano
    theta = np.linspace(0, 2*np.pi, 100)
    ax_2d.plot(2*np.cos(theta), 2*np.sin(theta), '-', color='#e5e7eb', linewidth=8, alpha=0.5)
    ax_2d.plot(2*np.cos(theta), 2*np.sin(theta), color=colors['primary'], linewidth=2)
    
    # Punto de análisis (en el círculo)
    t0_2d = np.pi/3
    P2 = np.array([2*np.cos(t0_2d), 2*np.sin(t0_2d)])
    ax_2d.plot(*P2, 'o', color=colors['accent'], markersize=12, zorder=5)
    
    # Vectores para movimiento circular uniforme acelerado
    # v tangente al círculo
    v2_dir = np.array([-np.sin(t0_2d), np.cos(t0_2d)])
    # a_N hacia el centro
    a_N2_dir = np.array([-np.cos(t0_2d), -np.sin(t0_2d)])
    # a_T tangente (supongamos aceleración)
    a_T2_dir = v2_dir
    
    # Magnitudes para visualización
    v2 = v2_dir * 1.2
    a_N2 = a_N2_dir * 0.8
    a_T2 = a_T2_dir * 0.5
    a_total = a_N2 + a_T2
    
    # Dibujar vectores
    ax_2d.annotate('', xy=P2+v2, xytext=P2,
                  arrowprops=dict(arrowstyle='->', color=colors['primary'], lw=2.5))
    ax_2d.annotate('', xy=P2+a_total, xytext=P2,
                  arrowprops=dict(arrowstyle='->', color='#dc2626', lw=3))
    ax_2d.annotate('', xy=P2+a_N2, xytext=P2,
                  arrowprops=dict(arrowstyle='->', color='#10b981', lw=2.5))
    ax_2d.annotate('', xy=P2+a_T2, xytext=P2,
                  arrowprops=dict(arrowstyle='->', color='#f59e0b', lw=2.5))
    
    # Líneas discontinuas para mostrar composición
    ax_2d.plot([P2[0]+a_T2[0], P2[0]+a_total[0]], [P2[1]+a_T2[1], P2[1]+a_total[1]], 
              '--', color='#10b981', alpha=0.7, linewidth=1.5)
    ax_2d.plot([P2[0]+a_N2[0], P2[0]+a_total[0]], [P2[1]+a_N2[1], P2[1]+a_total[1]], 
              '--', color='#f59e0b', alpha=0.7, linewidth=1.5)
    
    # Etiquetas
    ax_2d.text(P2[0]+v2[0]+0.1, P2[1]+v2[1]+0.1, r'$\mathbf{v}$', fontsize=11, color=colors['primary'], fontweight='bold')
    ax_2d.text(P2[0]+a_total[0]+0.15, P2[1]+a_total[1], r'$\mathbf{a}$', fontsize=11, color='#dc2626', fontweight='bold')
    ax_2d.text(P2[0]+a_N2[0]-0.3, P2[1]+a_N2[1]+0.1, r'$a_N\mathbf{N}$', fontsize=11, color='#10b981', fontweight='bold')
    ax_2d.text(P2[0]+a_T2[0]+0.1, P2[1]+a_T2[1]+0.2, r'$a_T\mathbf{T}$', fontsize=11, color='#f59e0b', fontweight='bold')
    
    # Centro
    ax_2d.plot(0, 0, '+', color='#6b7280', markersize=10)
    ax_2d.text(0.1, -0.3, 'Centro', fontsize=9, color='#6b7280')
    
    ax_2d.set_xlabel('x', fontsize=11)
    ax_2d.set_ylabel('y', fontsize=11)
    ax_2d.set_title('Descomposición $\\mathbf{a} = a_T\\mathbf{T} + a_N\\mathbf{N}$', fontsize=11, fontweight='bold')
    ax_2d.set_xlim([-3.5, 3.5])
    ax_2d.set_ylim([-3.5, 3.5])
    
    # =========================================
    # PANEL INFO: Fórmulas
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Descomposición principal
    ax_info.add_patch(plt.Rectangle((0.02, 0.78), 0.96, 0.20,
                                    facecolor='#fef2f2', edgecolor='#dc2626',
                                    linewidth=2))
    ax_info.text(0.5, 0.94, 'ACELERACIÓN', fontsize=10,
                fontweight='bold', ha='center', color='#dc2626')
    ax_info.text(0.5, 0.83, r'$\mathbf{a} = a_T \mathbf{T} + a_N \mathbf{N}$',
                fontsize=13, ha='center', color=colors['text'])
    
    # Componente tangencial
    ax_info.add_patch(plt.Rectangle((0.02, 0.52), 0.96, 0.22,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=2))
    ax_info.text(0.5, 0.70, 'COMP. TANGENCIAL', fontsize=9,
                fontweight='bold', ha='center', color='#f59e0b')
    ax_info.text(0.5, 0.58, r'$a_T = \frac{d|\mathbf{v}|}{dt} = \frac{\mathbf{v} \cdot \mathbf{a}}{|\mathbf{v}|}$',
                fontsize=11, ha='center', color=colors['text'])
    
    # Componente normal
    ax_info.add_patch(plt.Rectangle((0.02, 0.26), 0.96, 0.22,
                                    facecolor='#f0fdf4', edgecolor='#10b981',
                                    linewidth=2))
    ax_info.text(0.5, 0.44, 'COMP. NORMAL', fontsize=9,
                fontweight='bold', ha='center', color='#10b981')
    ax_info.text(0.5, 0.32, r'$a_N = \kappa |\mathbf{v}|^2 = \frac{|\mathbf{v} \times \mathbf{a}|}{|\mathbf{v}|}$',
                fontsize=11, ha='center', color=colors['text'])
    
    # Interpretación
    ax_info.text(0.5, 0.16, 'Interpretación física:', fontsize=9, fontweight='bold', ha='center', color='#374151')
    ax_info.text(0.5, 0.09, r'$a_T$: cambio en rapidez', fontsize=9, ha='center', color='#f59e0b')
    ax_info.text(0.5, 0.02, r'$a_N$: cambio en dirección', fontsize=9, ha='center', color='#10b981')
    
    fig.suptitle('Componentes Tangencial y Normal de la Aceleración', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "aceleracion_componentes.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'aceleracion_componentes.svg'}")
