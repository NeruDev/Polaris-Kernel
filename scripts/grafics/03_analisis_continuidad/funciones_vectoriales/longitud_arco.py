# yaml_frontmatter:
#   id: 'longitud_arco'
#   title: 'Longitud de arco como parámetro y reparametrización'
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
    
    fig = plt.figure(figsize=(14, 7), layout='constrained')
    gs = fig.add_gridspec(1, 3, width_ratios=[1.2, 1.2, 1])
    
    ax_curve = fig.add_subplot(gs[0])
    ax_func = fig.add_subplot(gs[1])
    ax_info = fig.add_subplot(gs[2])
    
    # =========================================
    # PANEL 1: Curva con longitud de arco
    # =========================================
    ax_curve.set_aspect('equal')
    ax_curve.grid(True, linestyle='--', alpha=0.3)
    
    # Curva paramétrica: r(t) = (cos(t), sin(t), t/2) proyectada en 2D
    # Usamos una espiral para mejor visualización
    t = np.linspace(0, 2*np.pi, 200)
    x = t * np.cos(t) / 4
    y = t * np.sin(t) / 4
    
    ax_curve.plot(x, y, color=colors['primary'], linewidth=3)
    
    # Puntos de referencia para mostrar longitud de arco
    t_points = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    colors_points = ['#dc2626', '#f59e0b', '#10b981', '#3b82f6', '#8b5cf6']
    labels = [r'$t=0$', r'$t=\pi/2$', r'$t=\pi$', r'$t=3\pi/2$', r'$t=2\pi$']
    
    for i, (ti, col, lab) in enumerate(zip(t_points, colors_points, labels)):
        xi = ti * np.cos(ti) / 4
        yi = ti * np.sin(ti) / 4
        ax_curve.plot(xi, yi, 'o', color=col, markersize=10, zorder=5)
        offset_x = 0.2 if np.cos(ti) >= 0 else -0.4
        offset_y = 0.15 if np.sin(ti) >= 0 else -0.25
        ax_curve.text(xi+offset_x, yi+offset_y, lab, fontsize=9, color=col, fontweight='bold')
    
    # Mostrar segmentos de arco con diferentes colores
    for i in range(len(t_points)-1):
        t_seg = np.linspace(t_points[i], t_points[i+1], 50)
        x_seg = t_seg * np.cos(t_seg) / 4
        y_seg = t_seg * np.sin(t_seg) / 4
        ax_curve.plot(x_seg, y_seg, color=colors_points[i+1], linewidth=4, alpha=0.6)
    
    ax_curve.set_xlabel('x', fontsize=11)
    ax_curve.set_ylabel('y', fontsize=11)
    ax_curve.set_title('Curva con segmentos de arco', fontsize=11, fontweight='bold')
    
    # =========================================
    # PANEL 2: Función s(t) longitud de arco
    # =========================================
    ax_func.grid(True, linestyle='--', alpha=0.3)
    
    # Calcular longitud de arco numéricamente
    # Para r(t) = (t*cos(t)/4, t*sin(t)/4):
    # r'(t) = ((cos(t) - t*sin(t))/4, (sin(t) + t*cos(t))/4)
    # |r'(t)| = sqrt(1 + t²) / 4
    
    t_dense = np.linspace(0, 2*np.pi, 500)
    
    # Integral numérica de |r'(t)|
    def arc_length(t_arr):
        ds = np.sqrt(1 + t_arr**2) / 4
        s = np.zeros_like(t_arr)
        for i in range(1, len(t_arr)):
            s[i] = s[i-1] + ds[i] * (t_arr[i] - t_arr[i-1])
        return s
    
    s = arc_length(t_dense)
    
    ax_func.plot(t_dense, s, color=colors['secondary'], linewidth=3, label=r'$s(t) = \int_0^t \|\mathbf{r}^\prime(u)\| \, du$')
    
    # Marcar puntos correspondientes
    for i, (ti, col) in enumerate(zip(t_points, colors_points)):
        si = np.interp(ti, t_dense, s)
        ax_func.plot(ti, si, 'o', color=col, markersize=10, zorder=5)
        ax_func.plot([ti, ti], [0, si], '--', color=col, alpha=0.5, linewidth=1)
        ax_func.plot([0, ti], [si, si], '--', color=col, alpha=0.5, linewidth=1)
    
    ax_func.set_xlabel('t (parámetro)', fontsize=11)
    ax_func.set_ylabel('s (longitud de arco)', fontsize=11)
    ax_func.set_title('Longitud de arco s(t)', fontsize=11, fontweight='bold')
    ax_func.legend(loc='upper left', fontsize=9)
    ax_func.set_xlim([0, 2*np.pi])
    ax_func.set_ylim([0, None])
    
    # =========================================
    # PANEL INFO: Fórmulas
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Longitud de arco
    ax_info.add_patch(plt.Rectangle((0.02, 0.72), 0.96, 0.25,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=2))
    ax_info.text(0.5, 0.92, 'LONGITUD DE ARCO', fontsize=10,
                fontweight='bold', ha='center', color=colors['primary'])
    ax_info.text(0.5, 0.80, r'$L = \int_a^b \|\mathbf{r}^\prime(t)\| \, dt$',
                fontsize=12, ha='center', color=colors['text'])
    
    # Función longitud de arco
    ax_info.add_patch(plt.Rectangle((0.02, 0.44), 0.96, 0.24,
                                    facecolor='#f0fdf4', edgecolor='#10b981',
                                    linewidth=2))
    ax_info.text(0.5, 0.64, 'FUNCIÓN s(t)', fontsize=10,
                fontweight='bold', ha='center', color='#10b981')
    ax_info.text(0.5, 0.52, r'$s(t) = \int_a^t \|\mathbf{r}^\prime(u)\| \, du$',
                fontsize=12, ha='center', color=colors['text'])
    
    # Reparametrización
    ax_info.add_patch(plt.Rectangle((0.02, 0.16), 0.96, 0.24,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=2))
    ax_info.text(0.5, 0.36, 'REPARAMETRIZACIÓN', fontsize=10,
                fontweight='bold', ha='center', color='#f59e0b')
    ax_info.text(0.5, 0.24, r'$\frac{ds}{dt} = \|\mathbf{r}^\prime(t)\|$',
                fontsize=12, ha='center', color=colors['text'])
    
    # Nota
    ax_info.text(0.5, 0.07, 'Si s es el parámetro:',
                fontsize=9, ha='center', color='#6b7280', style='italic')
    ax_info.text(0.5, 0.01, r'$\|\mathbf{r}^\prime(s)\| = 1$',
                fontsize=11, ha='center', color=colors['primary'])
    
    fig.suptitle('Longitud de Arco', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "longitud_arco.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'longitud_arco.svg'}")
