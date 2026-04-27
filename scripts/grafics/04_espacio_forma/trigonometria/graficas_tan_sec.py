# yaml_frontmatter:
#   id: 'graficas_tan_sec'
#   title: 'Gráficas de tangente, cotangente, secante y cosecante'
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
    
    fig = plt.figure(figsize=(14, 10), layout='constrained')
    gs = fig.add_gridspec(2, 2, hspace=0.25, wspace=0.15)
    
    ax_tan = fig.add_subplot(gs[0, 0])
    ax_cot = fig.add_subplot(gs[0, 1])
    ax_sec = fig.add_subplot(gs[1, 0])
    ax_csc = fig.add_subplot(gs[1, 1])
    
    # =========================================
    # TANGENTE
    # =========================================
    # Dibujar por ramas para evitar líneas verticales falsas
    for k in range(-2, 3):
        x_start = -np.pi/2 + k*np.pi + 0.01
        x_end = np.pi/2 + k*np.pi - 0.01
        x = np.linspace(x_start, x_end, 200)
        y = np.tan(x)
        ax_tan.plot(x, y, color=colors['secondary'], linewidth=2)
    
    # Asíntotas
    for k in range(-2, 3):
        ax_tan.axvline(x=np.pi/2 + k*np.pi, color='#d1d5db', linewidth=1, linestyle='--')
    
    ax_tan.axhline(y=0, color='#9ca3af', linewidth=1)
    ax_tan.axvline(x=0, color='#9ca3af', linewidth=1)
    
    ax_tan.set_xlim(-2*np.pi, 2*np.pi)
    ax_tan.set_ylim(-5, 5)
    ax_tan.set_title(r'$y = \tan(x) = \frac{\sin x}{\cos x}$', fontsize=11, 
                    fontweight='bold', color=colors['secondary'])
    ax_tan.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
    ax_tan.set_xticklabels(['-2π', '-π', '0', 'π', '2π'], fontsize=9)
    ax_tan.spines['top'].set_visible(False)
    ax_tan.spines['right'].set_visible(False)
    
    # Info
    ax_tan.text(0.95, 0.95, 'Periodo: π', transform=ax_tan.transAxes, fontsize=9,
               ha='right', va='top', color='#6b7280')
    ax_tan.text(0.95, 0.88, 'Asíntotas: x = π/2 + nπ', transform=ax_tan.transAxes, fontsize=9,
               ha='right', va='top', color='#6b7280')
    
    # =========================================
    # COTANGENTE
    # =========================================
    for k in range(-2, 3):
        x_start = k*np.pi + 0.01
        x_end = (k+1)*np.pi - 0.01
        x = np.linspace(x_start, x_end, 200)
        y = 1/np.tan(x)
        ax_cot.plot(x, y, color=colors['tertiary'], linewidth=2)
    
    # Asíntotas
    for k in range(-2, 3):
        ax_cot.axvline(x=k*np.pi, color='#d1d5db', linewidth=1, linestyle='--')
    
    ax_cot.axhline(y=0, color='#9ca3af', linewidth=1)
    ax_cot.axvline(x=0, color='#d1d5db', linewidth=1, linestyle='--')
    
    ax_cot.set_xlim(-2*np.pi, 2*np.pi)
    ax_cot.set_ylim(-5, 5)
    ax_cot.set_title(r'$y = \cot(x) = \frac{\cos x}{\sin x}$', fontsize=11,
                    fontweight='bold', color=colors['tertiary'])
    ax_cot.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
    ax_cot.set_xticklabels(['-2π', '-π', '0', 'π', '2π'], fontsize=9)
    ax_cot.spines['top'].set_visible(False)
    ax_cot.spines['right'].set_visible(False)
    
    ax_cot.text(0.95, 0.95, 'Periodo: π', transform=ax_cot.transAxes, fontsize=9,
               ha='right', va='top', color='#6b7280')
    ax_cot.text(0.95, 0.88, 'Asíntotas: x = nπ', transform=ax_cot.transAxes, fontsize=9,
               ha='right', va='top', color='#6b7280')
    
    # =========================================
    # SECANTE
    # =========================================
    for k in range(-2, 3):
        x_start = -np.pi/2 + k*np.pi + 0.01
        x_end = np.pi/2 + k*np.pi - 0.01
        x = np.linspace(x_start, x_end, 200)
        y = 1/np.cos(x)
        # Solo dibujar donde |y| > 1 (fuera del rango de cos)
        ax_sec.plot(x, y, color='#f59e0b', linewidth=2)
    
    # Asíntotas
    for k in range(-2, 3):
        ax_sec.axvline(x=np.pi/2 + k*np.pi, color='#d1d5db', linewidth=1, linestyle='--')
    
    ax_sec.axhline(y=0, color='#9ca3af', linewidth=1)
    ax_sec.axhline(y=1, color='#e5e7eb', linewidth=1, linestyle=':')
    ax_sec.axhline(y=-1, color='#e5e7eb', linewidth=1, linestyle=':')
    ax_sec.axvline(x=0, color='#9ca3af', linewidth=1)
    
    ax_sec.set_xlim(-2*np.pi, 2*np.pi)
    ax_sec.set_ylim(-5, 5)
    ax_sec.set_title(r'$y = \sec(x) = \frac{1}{\cos x}$', fontsize=11,
                    fontweight='bold', color='#f59e0b')
    ax_sec.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
    ax_sec.set_xticklabels(['-2π', '-π', '0', 'π', '2π'], fontsize=9)
    ax_sec.spines['top'].set_visible(False)
    ax_sec.spines['right'].set_visible(False)
    
    ax_sec.text(0.95, 0.95, 'Periodo: 2π', transform=ax_sec.transAxes, fontsize=9,
               ha='right', va='top', color='#6b7280')
    ax_sec.text(0.95, 0.88, 'Rango: (-∞,-1] ∪ [1,∞)', transform=ax_sec.transAxes, fontsize=9,
               ha='right', va='top', color='#6b7280')
    
    # =========================================
    # COSECANTE
    # =========================================
    for k in range(-2, 3):
        x_start = k*np.pi + 0.01
        x_end = (k+1)*np.pi - 0.01
        x = np.linspace(x_start, x_end, 200)
        y = 1/np.sin(x)
        ax_csc.plot(x, y, color='#ec4899', linewidth=2)
    
    # Asíntotas
    for k in range(-2, 3):
        ax_csc.axvline(x=k*np.pi, color='#d1d5db', linewidth=1, linestyle='--')
    
    ax_csc.axhline(y=0, color='#9ca3af', linewidth=1)
    ax_csc.axhline(y=1, color='#e5e7eb', linewidth=1, linestyle=':')
    ax_csc.axhline(y=-1, color='#e5e7eb', linewidth=1, linestyle=':')
    ax_csc.axvline(x=0, color='#d1d5db', linewidth=1, linestyle='--')
    
    ax_csc.set_xlim(-2*np.pi, 2*np.pi)
    ax_csc.set_ylim(-5, 5)
    ax_csc.set_title(r'$y = \csc(x) = \frac{1}{\sin x}$', fontsize=11,
                    fontweight='bold', color='#ec4899')
    ax_csc.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
    ax_csc.set_xticklabels(['-2π', '-π', '0', 'π', '2π'], fontsize=9)
    ax_csc.spines['top'].set_visible(False)
    ax_csc.spines['right'].set_visible(False)
    
    ax_csc.text(0.95, 0.95, 'Periodo: 2π', transform=ax_csc.transAxes, fontsize=9,
               ha='right', va='top', color='#6b7280')
    ax_csc.text(0.95, 0.88, 'Rango: (-∞,-1] ∪ [1,∞)', transform=ax_csc.transAxes, fontsize=9,
               ha='right', va='top', color='#6b7280')
    
    fig.suptitle('Las Otras Funciones Trigonométricas', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "graficas_tan_sec.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'graficas_tan_sec.svg'}")
