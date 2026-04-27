# yaml_frontmatter:
#   id: 'curvatura_circulo_osculador'
#   title: 'Curvatura, radio de curvatura y círculo osculador'
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


    setup_style,
    get_colors,
    get_output_dir_for_topic,
    save_figure,
)


def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig = plt.figure(figsize=(14, 8), layout='constrained')
    gs = fig.add_gridspec(1, 2, width_ratios=[1.3, 1], wspace=0.1)
    
    ax_fig = fig.add_subplot(gs[0])
    ax_info = fig.add_subplot(gs[1])
    
    # =========================================
    # PANEL FIGURA: Curva con círculo osculador
    # =========================================
    ax_fig.set_aspect('equal')
    ax_fig.grid(True, linestyle='--', alpha=0.3)
    
    # Curva: y = x³/6 para x en [-2, 3]
    x = np.linspace(-1.5, 2.5, 200)
    y = x**3 / 6
    
    ax_fig.plot(x, y, color=colors['primary'], linewidth=3, label=r'$y = \frac{x^3}{6}$')
    
    # Punto de tangencia
    x0 = 1.2
    y0 = x0**3 / 6
    P = np.array([x0, y0])
    ax_fig.plot(*P, 'o', color=colors['accent'], markersize=12, zorder=5)
    ax_fig.text(P[0]+0.15, P[1]-0.3, 'P', fontsize=12, fontweight='bold', color=colors['accent'])
    
    # Derivadas para curvatura
    # y' = x²/2, y'' = x
    y_prime = x0**2 / 2
    y_double = x0
    
    # Curvatura: κ = |y''| / (1 + y'²)^(3/2)
    kappa = abs(y_double) / (1 + y_prime**2)**(3/2)
    rho = 1 / kappa  # Radio de curvatura
    
    # Vector tangente unitario
    T = np.array([1, y_prime])
    T = T / np.linalg.norm(T)
    
    # Vector normal (apunta hacia el centro de curvatura)
    # Para y'' > 0, curva hacia arriba, N apunta hacia arriba
    N = np.array([-T[1], T[0]])  # Perpendicular a T
    if y_double < 0:
        N = -N
    
    # Centro de curvatura
    C = P + rho * N
    ax_fig.plot(*C, '*', color='#dc2626', markersize=15, zorder=5)
    ax_fig.text(C[0]+0.15, C[1]+0.15, 'Centro', fontsize=10, color='#dc2626')
    
    # Círculo osculador
    theta = np.linspace(0, 2*np.pi, 100)
    circ_x = C[0] + rho * np.cos(theta)
    circ_y = C[1] + rho * np.sin(theta)
    ax_fig.plot(circ_x, circ_y, '--', color='#dc2626', linewidth=2, alpha=0.8, 
               label='Círculo osculador')
    
    # Radio de curvatura (línea de P a C)
    ax_fig.plot([P[0], C[0]], [P[1], C[1]], '-', color='#f59e0b', linewidth=2)
    mid = (P + C) / 2
    ax_fig.text(mid[0]-0.3, mid[1], r'$\rho$', fontsize=14, color='#f59e0b', fontweight='bold')
    
    # Vectores T y N
    scale = 0.8
    ax_fig.annotate('', xy=P+T*scale, xytext=P,
                   arrowprops=dict(arrowstyle='->', color=colors['primary'], lw=2.5))
    ax_fig.annotate('', xy=P+N*scale, xytext=P,
                   arrowprops=dict(arrowstyle='->', color='#10b981', lw=2.5))
    ax_fig.text(P[0]+T[0]*scale+0.1, P[1]+T[1]*scale+0.1, r'$\mathbf{T}$', 
               fontsize=12, color=colors['primary'], fontweight='bold')
    ax_fig.text(P[0]+N[0]*scale-0.2, P[1]+N[1]*scale+0.1, r'$\mathbf{N}$', 
               fontsize=12, color='#10b981', fontweight='bold')
    
    ax_fig.set_xlim([-2, 3.5])
    ax_fig.set_ylim([-1.5, 4])
    ax_fig.set_xlabel('x', fontsize=11)
    ax_fig.set_ylabel('y', fontsize=11)
    ax_fig.legend(loc='upper left', fontsize=9)
    ax_fig.set_title('Círculo Osculador y Radio de Curvatura', fontsize=11, fontweight='bold')
    
    # =========================================
    # PANEL INFO: Fórmulas
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Curvatura principal
    ax_info.add_patch(plt.Rectangle((0.03, 0.72), 0.94, 0.25,
                                    facecolor='#fffbeb', edgecolor=colors['tertiary'],
                                    linewidth=2))
    ax_info.text(0.5, 0.92, 'CURVATURA', fontsize=11,
                fontweight='bold', ha='center', color=colors['tertiary'])
    ax_info.text(0.5, 0.80, r'$\kappa = \left\| \frac{d\mathbf{T}}{ds} \right\| = \frac{\|\mathbf{r}^\prime \times \mathbf{r}^{\prime\prime}\|}{\|\mathbf{r}^\prime\|^3}$',
                fontsize=12, ha='center', color=colors['text'])
    
    ax_info.axhline(y=0.68, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    
    # Fórmulas para curvas planas
    ax_info.text(0.5, 0.62, 'Curva plana $y = f(x)$:', fontsize=10,
                fontweight='bold', ha='center', color='#374151')
    ax_info.text(0.5, 0.52, r'$\kappa = \frac{|y^{\prime\prime}|}{[1 + (y^\prime)^2]^{3/2}}$',
                fontsize=13, ha='center', color=colors['text'])
    
    ax_info.axhline(y=0.46, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    
    # Radio de curvatura
    ax_info.add_patch(plt.Rectangle((0.03, 0.25), 0.94, 0.18,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=1.5))
    ax_info.text(0.5, 0.39, 'RADIO DE CURVATURA', fontsize=10,
                fontweight='bold', ha='center', color='#f59e0b')
    ax_info.text(0.5, 0.29, r'$\rho = \frac{1}{\kappa}$',
                fontsize=14, ha='center', color=colors['text'])
    
    # Centro de curvatura
    ax_info.add_patch(plt.Rectangle((0.03, 0.03), 0.94, 0.18,
                                    facecolor='#fef2f2', edgecolor='#dc2626',
                                    linewidth=1.5))
    ax_info.text(0.5, 0.17, 'CENTRO DE CURVATURA', fontsize=10,
                fontweight='bold', ha='center', color='#dc2626')
    ax_info.text(0.5, 0.07, r'Centro $= \mathbf{r}(t) + \rho\mathbf{N}(t)$',
                fontsize=11, ha='center', color=colors['text'])
    
    fig.suptitle('Curvatura y Círculo Osculador', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "curvatura_circulo_osculador.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'curvatura_circulo_osculador.svg'}")
