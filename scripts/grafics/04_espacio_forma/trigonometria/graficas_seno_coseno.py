# yaml_frontmatter:
#   id: 'graficas_seno_coseno'
#   title: 'Gráficas de las funciones seno y coseno'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'trigonometria']

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
    
    fig = plt.figure(figsize=(14, 9), layout='constrained')
    gs = fig.add_gridspec(3, 2, height_ratios=[1.2, 1.2, 0.6], hspace=0.25, wspace=0.1)
    
    ax_sin = fig.add_subplot(gs[0, :])
    ax_cos = fig.add_subplot(gs[1, :])
    ax_info = fig.add_subplot(gs[2, :])
    
    # Dominio
    x = np.linspace(-2*np.pi, 2*np.pi, 500)
    
    # =========================================
    # GRÁFICA DEL SENO
    # =========================================
    y_sin = np.sin(x)
    ax_sin.axhline(y=0, color='#d1d5db', linewidth=1, zorder=1)
    ax_sin.axvline(x=0, color='#d1d5db', linewidth=1, zorder=1)
    
    # Líneas de amplitud
    ax_sin.axhline(y=1, color='#e5e7eb', linewidth=1, linestyle='--')
    ax_sin.axhline(y=-1, color='#e5e7eb', linewidth=1, linestyle='--')
    
    # Curva del seno
    ax_sin.plot(x, y_sin, color=colors['secondary'], linewidth=2.5, label='y = sin x')
    
    # Puntos notables
    notable_x = [-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    notable_y = [np.sin(xi) for xi in notable_x]
    ax_sin.scatter(notable_x, notable_y, color=colors['secondary'], s=50, zorder=5)
    
    # Etiquetas en eje x
    x_ticks = [-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    x_labels = ['-2π', '-3π/2', '-π', '-π/2', '0', 'π/2', 'π', '3π/2', '2π']
    ax_sin.set_xticks(x_ticks)
    ax_sin.set_xticklabels(x_labels, fontsize=9)
    ax_sin.set_yticks([-1, 0, 1])
    
    # Anotaciones
    ax_sin.annotate('máx = 1', xy=(np.pi/2, 1), xytext=(np.pi/2 + 0.5, 1.3),
                   fontsize=9, color=colors['secondary'],
                   arrowprops=dict(arrowstyle='->', color=colors['secondary'], lw=1))
    ax_sin.annotate('mín = -1', xy=(-np.pi/2, -1), xytext=(-np.pi/2 - 0.8, -1.4),
                   fontsize=9, color=colors['secondary'],
                   arrowprops=dict(arrowstyle='->', color=colors['secondary'], lw=1))
    
    # Periodo
    ax_sin.annotate('', xy=(0, -1.6), xytext=(2*np.pi, -1.6),
                   arrowprops=dict(arrowstyle='<->', color='#6b7280', lw=1.5))
    ax_sin.text(np.pi, -1.75, 'Periodo = 2π', fontsize=9, ha='center', color='#6b7280')
    
    ax_sin.set_xlim(-2.2*np.pi, 2.2*np.pi)
    ax_sin.set_ylim(-2, 1.6)
    ax_sin.set_title('Función Seno: y = sin x', fontsize=11, fontweight='bold',
                    color=colors['secondary'])
    ax_sin.spines['top'].set_visible(False)
    ax_sin.spines['right'].set_visible(False)
    ax_sin.legend(loc='upper right', fontsize=9)
    
    # =========================================
    # GRÁFICA DEL COSENO
    # =========================================
    y_cos = np.cos(x)
    ax_cos.axhline(y=0, color='#d1d5db', linewidth=1, zorder=1)
    ax_cos.axvline(x=0, color='#d1d5db', linewidth=1, zorder=1)
    
    # Líneas de amplitud
    ax_cos.axhline(y=1, color='#e5e7eb', linewidth=1, linestyle='--')
    ax_cos.axhline(y=-1, color='#e5e7eb', linewidth=1, linestyle='--')
    
    # Curva del coseno
    ax_cos.plot(x, y_cos, color=colors['tertiary'], linewidth=2.5, label='y = cos x')
    
    # Puntos notables
    notable_y_cos = [np.cos(xi) for xi in notable_x]
    ax_cos.scatter(notable_x, notable_y_cos, color=colors['tertiary'], s=50, zorder=5)
    
    ax_cos.set_xticks(x_ticks)
    ax_cos.set_xticklabels(x_labels, fontsize=9)
    ax_cos.set_yticks([-1, 0, 1])
    
    # Anotaciones
    ax_cos.annotate('máx = 1', xy=(0, 1), xytext=(0.6, 1.3),
                   fontsize=9, color=colors['tertiary'],
                   arrowprops=dict(arrowstyle='->', color=colors['tertiary'], lw=1))
    ax_cos.annotate('mín = -1', xy=(np.pi, -1), xytext=(np.pi + 0.5, -1.4),
                   fontsize=9, color=colors['tertiary'],
                   arrowprops=dict(arrowstyle='->', color=colors['tertiary'], lw=1))
    
    ax_cos.set_xlim(-2.2*np.pi, 2.2*np.pi)
    ax_cos.set_ylim(-2, 1.6)
    ax_cos.set_title('Función Coseno: y = cos x', fontsize=11, fontweight='bold',
                    color=colors['tertiary'])
    ax_cos.spines['top'].set_visible(False)
    ax_cos.spines['right'].set_visible(False)
    ax_cos.legend(loc='upper right', fontsize=9)
    
    # =========================================
    # PANEL DE INFORMACIÓN
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Características del seno
    ax_info.add_patch(plt.Rectangle((0.02, 0.1), 0.46, 0.8,
                                    facecolor='#f0fdf4', edgecolor=colors['secondary'],
                                    linewidth=1.5))
    ax_info.text(0.25, 0.82, 'Características de sin x', fontsize=10, fontweight='bold',
                ha='center', color=colors['secondary'])
    
    sin_props = [
        'Dominio: ℝ (todos los reales)',
        'Rango: [-1, 1]',
        'Periodo: 2π',
        'Función impar: sin(-x) = -sin(x)',
        'Ceros: x = nπ, n ∈ ℤ',
    ]
    y_pos = 0.7
    for prop in sin_props:
        ax_info.text(0.05, y_pos, '• ' + prop, fontsize=9, color='#374151')
        y_pos -= 0.12
    
    # Características del coseno
    ax_info.add_patch(plt.Rectangle((0.52, 0.1), 0.46, 0.8,
                                    facecolor='#eff6ff', edgecolor=colors['tertiary'],
                                    linewidth=1.5))
    ax_info.text(0.75, 0.82, 'Características de cos x', fontsize=10, fontweight='bold',
                ha='center', color=colors['tertiary'])
    
    cos_props = [
        'Dominio: ℝ (todos los reales)',
        'Rango: [-1, 1]',
        'Periodo: 2π',
        'Función par: cos(-x) = cos(x)',
        'Ceros: x = π/2 + nπ, n ∈ ℤ',
    ]
    y_pos = 0.7
    for prop in cos_props:
        ax_info.text(0.55, y_pos, '• ' + prop, fontsize=9, color='#374151')
        y_pos -= 0.12
    
    fig.suptitle('Gráficas de las Funciones Seno y Coseno', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "graficas_seno_coseno.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'graficas_seno_coseno.svg'}")
