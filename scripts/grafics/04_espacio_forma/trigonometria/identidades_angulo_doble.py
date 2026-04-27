# yaml_frontmatter:
#   id: 'identidades_angulo_doble'
#   title: 'Identidades de ángulo doble y medio ángulo'
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
    gs = fig.add_gridspec(2, 1, height_ratios=[1, 1], hspace=0.15)
    
    ax_double = fig.add_subplot(gs[0])
    ax_half = fig.add_subplot(gs[1])
    
    # =========================================
    # PANEL SUPERIOR: Ángulo Doble
    # =========================================
    ax_double.axis('off')
    ax_double.set_xlim(0, 1)
    ax_double.set_ylim(0, 1)
    
    ax_double.add_patch(plt.Rectangle((0.02, 0.02), 0.96, 0.94,
                                      facecolor='#f9fafb', edgecolor='#d1d5db',
                                      linewidth=1.5))
    
    ax_double.text(0.5, 0.92, 'IDENTIDADES DE ÁNGULO DOBLE', fontsize=13, fontweight='bold',
                  ha='center', color=colors['primary'])
    
    # Seno del doble
    ax_double.add_patch(plt.Rectangle((0.03, 0.68), 0.3, 0.2,
                                      facecolor='#f0fdf4', edgecolor=colors['secondary'],
                                      linewidth=1.5))
    ax_double.text(0.18, 0.84, 'sin(2θ)', fontsize=11, fontweight='bold',
                  ha='center', color=colors['secondary'])
    ax_double.text(0.18, 0.73, r'$\sin(2\theta) = 2\sin\theta\cos\theta$',
                  fontsize=10, ha='center', color=colors['text'])
    
    # Coseno del doble (tres formas)
    ax_double.add_patch(plt.Rectangle((0.35, 0.45), 0.3, 0.43,
                                      facecolor='#eff6ff', edgecolor=colors['tertiary'],
                                      linewidth=1.5))
    ax_double.text(0.5, 0.84, 'cos(2θ)', fontsize=11, fontweight='bold',
                  ha='center', color=colors['tertiary'])
    ax_double.text(0.5, 0.73, r'$\cos(2\theta) = \cos^2\theta - \sin^2\theta$',
                  fontsize=10, ha='center', color=colors['text'])
    ax_double.text(0.5, 0.62, r'$\cos(2\theta) = 2\cos^2\theta - 1$',
                  fontsize=10, ha='center', color=colors['text'])
    ax_double.text(0.5, 0.51, r'$\cos(2\theta) = 1 - 2\sin^2\theta$',
                  fontsize=10, ha='center', color=colors['text'])
    
    # Tangente del doble
    ax_double.add_patch(plt.Rectangle((0.67, 0.68), 0.3, 0.2,
                                      facecolor='#fef3c7', edgecolor='#f59e0b',
                                      linewidth=1.5))
    ax_double.text(0.82, 0.84, 'tan(2θ)', fontsize=11, fontweight='bold',
                  ha='center', color='#f59e0b')
    ax_double.text(0.82, 0.73, r'$\tan(2\theta) = \frac{2\tan\theta}{1-\tan^2\theta}$',
                  fontsize=10, ha='center', color=colors['text'])
    
    # Formas despejadas (útiles para integración)
    ax_double.add_patch(plt.Rectangle((0.03, 0.08), 0.62, 0.32,
                                      facecolor='#fef9c3', edgecolor='#ca8a04',
                                      linewidth=1.5))
    ax_double.text(0.34, 0.36, 'Formas Despejadas (útiles para integración)', fontsize=10, 
                  fontweight='bold', ha='center', color='#ca8a04')
    ax_double.text(0.34, 0.25, r'$\sin^2\theta = \frac{1 - \cos(2\theta)}{2}$',
                  fontsize=10, ha='center', color=colors['text'])
    ax_double.text(0.34, 0.14, r'$\cos^2\theta = \frac{1 + \cos(2\theta)}{2}$',
                  fontsize=10, ha='center', color=colors['text'])
    
    # Nota
    ax_double.add_patch(plt.Rectangle((0.67, 0.08), 0.3, 0.32,
                                      facecolor='#fee2e2', edgecolor='#dc2626',
                                      linewidth=1.5))
    ax_double.text(0.82, 0.36, 'Tip', fontsize=10, fontweight='bold',
                  ha='center', color='#dc2626')
    ax_double.text(0.82, 0.26, 'Se obtienen de', fontsize=9, ha='center', color='#6b7280')
    ax_double.text(0.82, 0.18, 'las identidades de', fontsize=9, ha='center', color='#6b7280')
    ax_double.text(0.82, 0.1, 'suma con α = β', fontsize=9, ha='center', color='#6b7280')
    
    # =========================================
    # PANEL INFERIOR: Medio Ángulo
    # =========================================
    ax_half.axis('off')
    ax_half.set_xlim(0, 1)
    ax_half.set_ylim(0, 1)
    
    ax_half.add_patch(plt.Rectangle((0.02, 0.02), 0.96, 0.94,
                                    facecolor='#f9fafb', edgecolor='#d1d5db',
                                    linewidth=1.5))
    
    ax_half.text(0.5, 0.92, 'IDENTIDADES DE MEDIO ÁNGULO', fontsize=13, fontweight='bold',
                ha='center', color=colors['primary'])
    
    # Seno del medio
    ax_half.add_patch(plt.Rectangle((0.03, 0.5), 0.3, 0.35,
                                    facecolor='#f0fdf4', edgecolor=colors['secondary'],
                                    linewidth=1.5))
    ax_half.text(0.18, 0.8, r'$\sin\frac{\theta}{2}$', fontsize=12, fontweight='bold',
                ha='center', color=colors['secondary'])
    ax_half.text(0.18, 0.65, r'$\sin\frac{\theta}{2} = \pm\sqrt{\frac{1-\cos\theta}{2}}$',
                fontsize=10, ha='center', color=colors['text'])
    
    # Coseno del medio
    ax_half.add_patch(plt.Rectangle((0.35, 0.5), 0.3, 0.35,
                                    facecolor='#eff6ff', edgecolor=colors['tertiary'],
                                    linewidth=1.5))
    ax_half.text(0.5, 0.8, r'$\cos\frac{\theta}{2}$', fontsize=12, fontweight='bold',
                ha='center', color=colors['tertiary'])
    ax_half.text(0.5, 0.65, r'$\cos\frac{\theta}{2} = \pm\sqrt{\frac{1+\cos\theta}{2}}$',
                fontsize=10, ha='center', color=colors['text'])
    
    # Tangente del medio
    ax_half.add_patch(plt.Rectangle((0.67, 0.5), 0.3, 0.35,
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=1.5))
    ax_half.text(0.82, 0.8, r'$\tan\frac{\theta}{2}$', fontsize=12, fontweight='bold',
                ha='center', color='#f59e0b')
    ax_half.text(0.82, 0.68, r'$\tan\frac{\theta}{2} = \pm\sqrt{\frac{1-\cos\theta}{1+\cos\theta}}$',
                fontsize=9, ha='center', color=colors['text'])
    ax_half.text(0.82, 0.56, r'$= \frac{\sin\theta}{1+\cos\theta} = \frac{1-\cos\theta}{\sin\theta}$',
                fontsize=9, ha='center', color='#6b7280')
    
    # Nota sobre signo
    ax_half.add_patch(plt.Rectangle((0.15, 0.12), 0.7, 0.3,
                                    facecolor='#fce7f3', edgecolor='#ec4899',
                                    linewidth=1.5))
    ax_half.text(0.5, 0.37, '⚠️ El signo (±) depende del cuadrante donde se encuentra θ/2',
                fontsize=10, ha='center', color='#be185d', fontweight='bold')
    
    ax_half.text(0.5, 0.27, 'Cuadrante I: sin, cos, tan son positivos',
                fontsize=9, ha='center', color='#374151')
    ax_half.text(0.5, 0.2, 'Cuadrante II: solo sin es positivo',
                fontsize=9, ha='center', color='#374151')
    ax_half.text(0.5, 0.13, 'Cuadrante III: solo tan es positivo  •  Cuadrante IV: solo cos es positivo',
                fontsize=9, ha='center', color='#374151')
    
    fig.suptitle('Identidades de Ángulo Doble y Medio Ángulo', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "identidades_angulo_doble.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'identidades_angulo_doble.svg'}")
