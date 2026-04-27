# yaml_frontmatter:
#   id: 'identidades_pitagoricas'
#   title: 'Las tres identidades pitagóricas fundamentales'
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

import matplotlib.patches as patches

    setup_style,
    get_colors,
    get_output_dir_for_topic,
    save_figure,
)


def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig = plt.figure(figsize=(14, 9), layout='constrained')
    gs = fig.add_gridspec(2, 2, height_ratios=[1.2, 1], width_ratios=[1, 1], 
                         hspace=0.15, wspace=0.1)
    
    ax_circle = fig.add_subplot(gs[0, 0])
    ax_formulas = fig.add_subplot(gs[0, 1])
    ax_derivation = fig.add_subplot(gs[1, :])
    
    # =========================================
    # PANEL SUPERIOR IZQUIERDO: Círculo unitario
    # =========================================
    
    # Ejes
    ax_circle.axhline(y=0, color='#d1d5db', linewidth=1, zorder=1)
    ax_circle.axvline(x=0, color='#d1d5db', linewidth=1, zorder=1)
    
    # Círculo unitario
    theta_circle = np.linspace(0, 2*np.pi, 100)
    ax_circle.plot(np.cos(theta_circle), np.sin(theta_circle), 
                  color=colors['primary'], linewidth=2, zorder=2)
    
    # Ángulo de ejemplo
    theta = np.radians(55)
    P = np.array([np.cos(theta), np.sin(theta)])
    
    # Triángulo rectángulo
    ax_circle.fill([0, P[0], P[0], 0], [0, 0, P[1], 0], 
                  alpha=0.2, color=colors['accent'])
    
    # Lados del triángulo
    ax_circle.plot([0, P[0]], [0, 0], color=colors['tertiary'], linewidth=3, zorder=3,
                  label='cos θ = x')
    ax_circle.plot([P[0], P[0]], [0, P[1]], color=colors['secondary'], linewidth=3, zorder=3,
                  label='sin θ = y')
    ax_circle.plot([0, P[0]], [0, P[1]], color='#f59e0b', linewidth=3, zorder=3,
                  label='r = 1')
    
    # Punto P
    ax_circle.plot(P[0], P[1], 'o', color='#f59e0b', markersize=10, zorder=5)
    ax_circle.text(P[0] + 0.05, P[1] + 0.08, 'P', fontsize=12, fontweight='bold',
                  color='#f59e0b')
    
    # Arco del ángulo
    arc = np.linspace(0, theta, 30)
    ax_circle.plot(0.2*np.cos(arc), 0.2*np.sin(arc), color='#f59e0b', linewidth=2)
    ax_circle.text(0.3, 0.12, 'θ', fontsize=12, fontweight='bold', color='#f59e0b')
    
    # Etiquetas de lados
    ax_circle.text(P[0]/2, -0.1, 'x = cos θ', fontsize=10, ha='center', 
                  color=colors['tertiary'], fontweight='bold')
    ax_circle.text(P[0] + 0.08, P[1]/2, 'y = sin θ', fontsize=10, 
                  color=colors['secondary'], fontweight='bold')
    ax_circle.text(P[0]/2 - 0.12, P[1]/2 + 0.08, 'r = 1', fontsize=10, rotation=55,
                  color='#f59e0b', fontweight='bold')
    
    # Ángulo recto
    sq_size = 0.06
    ax_circle.plot([P[0]-sq_size, P[0]-sq_size, P[0]], [0, sq_size, sq_size], 
                  color='#6b7280', linewidth=1)
    
    ax_circle.set_xlim(-0.3, 1.3)
    ax_circle.set_ylim(-0.3, 1.2)
    ax_circle.set_aspect('equal')
    ax_circle.axis('off')
    ax_circle.set_title('En el Círculo Unitario', fontsize=11, fontweight='bold',
                       color=colors['text'])
    
    # =========================================
    # PANEL SUPERIOR DERECHO: Fórmulas
    # =========================================
    ax_formulas.axis('off')
    ax_formulas.set_xlim(0, 1)
    ax_formulas.set_ylim(0, 1)
    
    # Identidad principal
    ax_formulas.add_patch(plt.Rectangle((0.05, 0.68), 0.9, 0.28,
                                        facecolor='#fef3c7', edgecolor='#f59e0b',
                                        linewidth=2, zorder=1))
    ax_formulas.text(0.5, 0.88, 'IDENTIDAD FUNDAMENTAL', fontsize=10, fontweight='bold',
                    ha='center', color='#f59e0b')
    ax_formulas.text(0.5, 0.76, r'$\sin^2\theta + \cos^2\theta = 1$', fontsize=16,
                    ha='center', color=colors['text'], fontweight='bold')
    
    # Identidades derivadas
    ax_formulas.add_patch(plt.Rectangle((0.05, 0.05), 0.9, 0.58,
                                        facecolor='#f0fdf4', edgecolor=colors['accent'],
                                        linewidth=1.5))
    ax_formulas.text(0.5, 0.56, 'Identidades Derivadas', fontsize=10, fontweight='bold',
                    ha='center', color=colors['accent'])
    
    # Identidad con tangente
    ax_formulas.text(0.5, 0.44, r'$1 + \tan^2\theta = \sec^2\theta$', fontsize=13,
                    ha='center', color=colors['text'])
    ax_formulas.text(0.5, 0.35, '(dividiendo entre cos²θ)', fontsize=9, ha='center',
                    color='#6b7280', style='italic')
    
    # Identidad con cotangente
    ax_formulas.text(0.5, 0.22, r'$1 + \cot^2\theta = \csc^2\theta$', fontsize=13,
                    ha='center', color=colors['text'])
    ax_formulas.text(0.5, 0.13, '(dividiendo entre sin²θ)', fontsize=9, ha='center',
                    color='#6b7280', style='italic')
    
    ax_formulas.set_title('Las Tres Identidades Pitagóricas', fontsize=11, fontweight='bold',
                         color=colors['text'])
    
    # =========================================
    # PANEL INFERIOR: Derivación
    # =========================================
    ax_derivation.axis('off')
    ax_derivation.set_xlim(0, 1)
    ax_derivation.set_ylim(0, 1)
    
    # Caja de derivación
    ax_derivation.add_patch(plt.Rectangle((0.02, 0.05), 0.96, 0.88,
                                          facecolor='#eff6ff', edgecolor=colors['primary'],
                                          linewidth=1.5))
    
    ax_derivation.text(0.5, 0.88, 'Derivación desde el Teorema de Pitágoras', 
                      fontsize=11, fontweight='bold', ha='center', color=colors['primary'])
    
    # Pasos de derivación
    steps = [
        ('Paso 1:', 'En un triángulo rectángulo: ', r'$a^2 + b^2 = c^2$', 0.78),
        ('Paso 2:', 'Con cateto opuesto = y, cateto adyacente = x, hipotenusa = r:', 
         r'$x^2 + y^2 = r^2$', 0.65),
        ('Paso 3:', 'En el círculo unitario r = 1, y sabemos que x = cos θ, y = sin θ:', '', 0.52),
        ('', '', r'$\cos^2\theta + \sin^2\theta = 1^2$', 0.42),
        ('Paso 4:', 'Reordenando:', r'$\sin^2\theta + \cos^2\theta = 1$', 0.28),
    ]
    
    for step, text, formula, y_pos in steps:
        if step:
            ax_derivation.text(0.05, y_pos, step, fontsize=10, fontweight='bold',
                              color=colors['primary'])
            ax_derivation.text(0.15, y_pos, text, fontsize=10, color='#374151')
        if formula:
            ax_derivation.text(0.7, y_pos, formula, fontsize=12, ha='center',
                              color='#1f2937',
                              bbox=dict(facecolor='white', edgecolor='#e5e7eb', 
                                       boxstyle='round,pad=0.3'))
    
    # Resultado final
    ax_derivation.add_patch(plt.Rectangle((0.25, 0.08), 0.5, 0.12,
                                          facecolor='#fef3c7', edgecolor='#f59e0b',
                                          linewidth=2))
    ax_derivation.text(0.5, 0.135, r'$\sin^2\theta + \cos^2\theta = 1$',
                      fontsize=14, ha='center', color='#1f2937', fontweight='bold')
    
    fig.suptitle('Identidades Pitagóricas', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "identidades_pitagoricas.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'identidades_pitagoricas.svg'}")
