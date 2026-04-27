# yaml_frontmatter:
#   id: 'transformaciones_trig'
#   title: 'Transformaciones de funciones trigonométricas: amplitud, periodo, desfase'
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
    gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.15)
    
    ax_amp = fig.add_subplot(gs[0, 0])
    ax_period = fig.add_subplot(gs[0, 1])
    ax_phase = fig.add_subplot(gs[1, 0])
    ax_vertical = fig.add_subplot(gs[1, 1])
    ax_formula = fig.add_subplot(gs[2, :])
    
    x = np.linspace(-np.pi, 3*np.pi, 500)
    
    # =========================================
    # AMPLITUD
    # =========================================
    ax_amp.axhline(y=0, color='#d1d5db', linewidth=1)
    ax_amp.axvline(x=0, color='#d1d5db', linewidth=1)
    
    ax_amp.plot(x, np.sin(x), color='#9ca3af', linewidth=1.5, linestyle='--', 
               label='sin x (A=1)')
    ax_amp.plot(x, 2*np.sin(x), color=colors['secondary'], linewidth=2.5, 
               label='2 sin x (A=2)')
    ax_amp.plot(x, 0.5*np.sin(x), color=colors['tertiary'], linewidth=2.5,
               label='0.5 sin x (A=0.5)')
    
    ax_amp.axhline(y=2, color=colors['secondary'], linewidth=1, linestyle=':')
    ax_amp.axhline(y=-2, color=colors['secondary'], linewidth=1, linestyle=':')
    
    ax_amp.set_xlim(-np.pi, 3*np.pi)
    ax_amp.set_ylim(-2.5, 2.5)
    ax_amp.set_title('Amplitud (A)', fontsize=11, fontweight='bold')
    ax_amp.legend(loc='upper right', fontsize=8)
    ax_amp.set_xticks([0, np.pi, 2*np.pi])
    ax_amp.set_xticklabels(['0', 'π', '2π'], fontsize=9)
    ax_amp.spines['top'].set_visible(False)
    ax_amp.spines['right'].set_visible(False)
    
    # =========================================
    # PERIODO
    # =========================================
    ax_period.axhline(y=0, color='#d1d5db', linewidth=1)
    ax_period.axvline(x=0, color='#d1d5db', linewidth=1)
    
    ax_period.plot(x, np.sin(x), color='#9ca3af', linewidth=1.5, linestyle='--',
                  label='sin x (B=1, T=2π)')
    ax_period.plot(x, np.sin(2*x), color=colors['secondary'], linewidth=2.5,
                  label='sin 2x (B=2, T=π)')
    ax_period.plot(x, np.sin(0.5*x), color=colors['tertiary'], linewidth=2.5,
                  label='sin 0.5x (B=0.5, T=4π)')
    
    # Marcadores de periodo
    ax_period.annotate('', xy=(0, -1.6), xytext=(np.pi, -1.6),
                      arrowprops=dict(arrowstyle='<->', color=colors['secondary'], lw=1.5))
    ax_period.text(np.pi/2, -1.85, 'T=π', fontsize=9, ha='center', color=colors['secondary'])
    
    ax_period.set_xlim(-np.pi, 3*np.pi)
    ax_period.set_ylim(-2.2, 1.5)
    ax_period.set_title('Periodo (T = 2π/B)', fontsize=11, fontweight='bold')
    ax_period.legend(loc='upper right', fontsize=8)
    ax_period.set_xticks([0, np.pi, 2*np.pi, 3*np.pi])
    ax_period.set_xticklabels(['0', 'π', '2π', '3π'], fontsize=9)
    ax_period.spines['top'].set_visible(False)
    ax_period.spines['right'].set_visible(False)
    
    # =========================================
    # DESFASE (FASE)
    # =========================================
    ax_phase.axhline(y=0, color='#d1d5db', linewidth=1)
    ax_phase.axvline(x=0, color='#d1d5db', linewidth=1)
    
    ax_phase.plot(x, np.sin(x), color='#9ca3af', linewidth=1.5, linestyle='--',
                 label='sin x')
    ax_phase.plot(x, np.sin(x - np.pi/2), color=colors['secondary'], linewidth=2.5,
                 label='sin(x - π/2)')
    ax_phase.plot(x, np.sin(x + np.pi/4), color=colors['tertiary'], linewidth=2.5,
                 label='sin(x + π/4)')
    
    # Flechas de desplazamiento
    ax_phase.annotate('', xy=(np.pi/2, 0.8), xytext=(0, 0.8),
                     arrowprops=dict(arrowstyle='->', color=colors['secondary'], lw=1.5))
    ax_phase.text(np.pi/4, 1.05, '→ π/2', fontsize=8, ha='center', color=colors['secondary'])
    
    ax_phase.annotate('', xy=(-np.pi/4, 0.6), xytext=(0, 0.6),
                     arrowprops=dict(arrowstyle='->', color=colors['tertiary'], lw=1.5))
    ax_phase.text(-np.pi/8, 0.4, '← π/4', fontsize=8, ha='center', color=colors['tertiary'])
    
    ax_phase.set_xlim(-np.pi, 3*np.pi)
    ax_phase.set_ylim(-1.5, 1.5)
    ax_phase.set_title('Desfase (C)', fontsize=11, fontweight='bold')
    ax_phase.legend(loc='upper right', fontsize=8)
    ax_phase.set_xticks([0, np.pi, 2*np.pi])
    ax_phase.set_xticklabels(['0', 'π', '2π'], fontsize=9)
    ax_phase.spines['top'].set_visible(False)
    ax_phase.spines['right'].set_visible(False)
    
    # =========================================
    # DESPLAZAMIENTO VERTICAL
    # =========================================
    ax_vertical.axhline(y=0, color='#d1d5db', linewidth=1)
    ax_vertical.axvline(x=0, color='#d1d5db', linewidth=1)
    
    ax_vertical.plot(x, np.sin(x), color='#9ca3af', linewidth=1.5, linestyle='--',
                    label='sin x')
    ax_vertical.plot(x, np.sin(x) + 1.5, color=colors['secondary'], linewidth=2.5,
                    label='sin x + 1.5')
    ax_vertical.plot(x, np.sin(x) - 1, color=colors['tertiary'], linewidth=2.5,
                    label='sin x - 1')
    
    # Líneas de equilibrio
    ax_vertical.axhline(y=1.5, color=colors['secondary'], linewidth=1, linestyle=':')
    ax_vertical.axhline(y=-1, color=colors['tertiary'], linewidth=1, linestyle=':')
    
    ax_vertical.set_xlim(-np.pi, 3*np.pi)
    ax_vertical.set_ylim(-2.5, 3)
    ax_vertical.set_title('Desplazamiento Vertical (D)', fontsize=11, fontweight='bold')
    ax_vertical.legend(loc='upper right', fontsize=8)
    ax_vertical.set_xticks([0, np.pi, 2*np.pi])
    ax_vertical.set_xticklabels(['0', 'π', '2π'], fontsize=9)
    ax_vertical.spines['top'].set_visible(False)
    ax_vertical.spines['right'].set_visible(False)
    
    # =========================================
    # FÓRMULA GENERAL
    # =========================================
    ax_formula.axis('off')
    ax_formula.set_xlim(0, 1)
    ax_formula.set_ylim(0, 1)
    
    ax_formula.add_patch(plt.Rectangle((0.02, 0.15), 0.96, 0.8,
                                       facecolor='#fef3c7', edgecolor='#f59e0b',
                                       linewidth=2))
    
    ax_formula.text(0.5, 0.85, 'FORMA GENERAL', fontsize=12, fontweight='bold',
                   ha='center', color='#f59e0b')
    
    ax_formula.text(0.5, 0.68, r'$y = A \sin(Bx - C) + D$  o  $y = A \cos(Bx - C) + D$',
                   fontsize=14, ha='center', color=colors['text'])
    
    params = [
        ('A', 'Amplitud', '|A| = altura desde la línea media al máximo'),
        ('B', 'Frecuencia angular', 'Periodo T = 2π/|B|'),
        ('C/B', 'Desfase', 'Desplazamiento horizontal = C/B'),
        ('D', 'Desplazamiento vertical', 'Nueva línea media'),
    ]
    
    x_positions = [0.12, 0.38, 0.64, 0.9]
    for i, (param, name, desc) in enumerate(params):
        x_pos = x_positions[i]
        ax_formula.text(x_pos, 0.48, param, fontsize=12, fontweight='bold',
                       ha='center', color=colors['primary'])
        ax_formula.text(x_pos, 0.36, name, fontsize=9, fontweight='bold',
                       ha='center', color='#374151')
        # Descripción en dos líneas si es necesario
        if len(desc) > 25:
            parts = desc.split(' = ')
            ax_formula.text(x_pos, 0.26, parts[0] + ' =', fontsize=8, ha='center', color='#6b7280')
            if len(parts) > 1:
                ax_formula.text(x_pos, 0.18, parts[1], fontsize=8, ha='center', color='#6b7280')
        else:
            ax_formula.text(x_pos, 0.24, desc, fontsize=8, ha='center', color='#6b7280')
    
    fig.suptitle('Transformaciones de Funciones Trigonométricas', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "transformaciones_trig.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'transformaciones_trig.svg'}")
