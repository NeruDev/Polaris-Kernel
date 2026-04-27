# yaml_frontmatter:
#   id: 'identidades_suma_diferencia'
#   title: 'Identidades de suma y diferencia de ángulos'
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
    
    fig = plt.figure(figsize=(14, 10), layout='constrained')
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.2], hspace=0.2, wspace=0.1)
    
    ax_visual = fig.add_subplot(gs[0, 0])
    ax_visual2 = fig.add_subplot(gs[0, 1])
    ax_formulas = fig.add_subplot(gs[1, :])
    
    # =========================================
    # PANEL 1: Visualización geométrica de sin(α+β)
    # =========================================
    ax_visual.set_xlim(-0.1, 1.3)
    ax_visual.set_ylim(-0.1, 1.1)
    ax_visual.set_aspect('equal')
    ax_visual.axis('off')
    
    # Ángulos
    alpha = np.radians(35)
    beta = np.radians(25)
    
    # Punto en el círculo unitario
    P = np.array([np.cos(alpha + beta), np.sin(alpha + beta)])
    Q = np.array([np.cos(alpha), np.sin(alpha)])
    
    # Arco del círculo (cuarto)
    theta = np.linspace(0, np.pi/2, 50)
    ax_visual.plot(np.cos(theta), np.sin(theta), color=colors['primary'], linewidth=2)
    
    # Ejes
    ax_visual.arrow(0, 0, 1.15, 0, head_width=0.03, head_length=0.03, fc='#9ca3af', ec='#9ca3af')
    ax_visual.arrow(0, 0, 0, 0.95, head_width=0.03, head_length=0.03, fc='#9ca3af', ec='#9ca3af')
    
    # Radio a P
    ax_visual.plot([0, P[0]], [0, P[1]], color='#f59e0b', linewidth=2.5)
    ax_visual.plot(P[0], P[1], 'o', color='#f59e0b', markersize=8)
    ax_visual.text(P[0] + 0.05, P[1] + 0.05, 'P', fontsize=11, fontweight='bold', color='#f59e0b')
    
    # Proyecciones
    ax_visual.plot([P[0], P[0]], [0, P[1]], '--', color=colors['secondary'], linewidth=1.5)
    ax_visual.plot([0, P[0]], [0, 0], color=colors['tertiary'], linewidth=3)
    ax_visual.plot([0, 0], [0, P[1]], color=colors['secondary'], linewidth=3)
    
    # Etiquetas
    ax_visual.text(P[0]/2, -0.08, 'cos(α+β)', fontsize=9, ha='center', color=colors['tertiary'])
    ax_visual.text(-0.12, P[1]/2, 'sin(α+β)', fontsize=9, ha='center', rotation=90, 
                  color=colors['secondary'])
    
    # Arcos de ángulos
    arc_alpha = np.linspace(0, alpha, 20)
    ax_visual.plot(0.2*np.cos(arc_alpha), 0.2*np.sin(arc_alpha), color=colors['tertiary'], linewidth=2)
    ax_visual.text(0.28, 0.08, 'α', fontsize=11, color=colors['tertiary'], fontweight='bold')
    
    arc_beta = np.linspace(alpha, alpha + beta, 20)
    ax_visual.plot(0.25*np.cos(arc_beta), 0.25*np.sin(arc_beta), color=colors['secondary'], linewidth=2)
    ax_visual.text(0.32, 0.22, 'β', fontsize=11, color=colors['secondary'], fontweight='bold')
    
    ax_visual.set_title('Suma de ángulos: α + β', fontsize=11, fontweight='bold')
    
    # =========================================
    # PANEL 2: Diferencia de ángulos
    # =========================================
    ax_visual2.set_xlim(-0.1, 1.3)
    ax_visual2.set_ylim(-0.3, 1.1)
    ax_visual2.set_aspect('equal')
    ax_visual2.axis('off')
    
    # Arco del círculo
    theta = np.linspace(-0.3, np.pi/2, 50)
    ax_visual2.plot(np.cos(theta), np.sin(theta), color=colors['primary'], linewidth=2)
    
    # Ejes
    ax_visual2.arrow(0, 0, 1.15, 0, head_width=0.03, head_length=0.03, fc='#9ca3af', ec='#9ca3af')
    ax_visual2.arrow(0, 0, 0, 0.95, head_width=0.03, head_length=0.03, fc='#9ca3af', ec='#9ca3af')
    
    # Punto para α - β
    alpha = np.radians(50)
    beta = np.radians(20)
    P_diff = np.array([np.cos(alpha - beta), np.sin(alpha - beta)])
    
    # Radio a P
    ax_visual2.plot([0, P_diff[0]], [0, P_diff[1]], color='#ec4899', linewidth=2.5)
    ax_visual2.plot(P_diff[0], P_diff[1], 'o', color='#ec4899', markersize=8)
    ax_visual2.text(P_diff[0] + 0.05, P_diff[1] + 0.05, 'P', fontsize=11, fontweight='bold', 
                   color='#ec4899')
    
    # Proyecciones
    ax_visual2.plot([P_diff[0], P_diff[0]], [0, P_diff[1]], '--', color=colors['secondary'], linewidth=1.5)
    ax_visual2.plot([0, P_diff[0]], [0, 0], color=colors['tertiary'], linewidth=3)
    ax_visual2.plot([0, 0], [0, P_diff[1]], color=colors['secondary'], linewidth=3)
    
    # Etiquetas
    ax_visual2.text(P_diff[0]/2, -0.08, 'cos(α−β)', fontsize=9, ha='center', color=colors['tertiary'])
    ax_visual2.text(-0.12, P_diff[1]/2, 'sin(α−β)', fontsize=9, ha='center', rotation=90,
                   color=colors['secondary'])
    
    # Arcos
    arc_alpha = np.linspace(0, alpha, 20)
    ax_visual2.plot(0.3*np.cos(arc_alpha), 0.3*np.sin(arc_alpha), color='#9ca3af', 
                   linewidth=1.5, linestyle='--')
    ax_visual2.text(0.38, 0.2, 'α', fontsize=10, color='#6b7280')
    
    arc_result = np.linspace(0, alpha - beta, 20)
    ax_visual2.plot(0.2*np.cos(arc_result), 0.2*np.sin(arc_result), color='#ec4899', linewidth=2)
    ax_visual2.text(0.25, 0.1, 'α−β', fontsize=10, color='#ec4899', fontweight='bold')
    
    ax_visual2.set_title('Diferencia de ángulos: α − β', fontsize=11, fontweight='bold')
    
    # =========================================
    # PANEL INFERIOR: Fórmulas
    # =========================================
    ax_formulas.axis('off')
    ax_formulas.set_xlim(0, 1)
    ax_formulas.set_ylim(0, 1)
    
    # Seno suma y diferencia
    ax_formulas.add_patch(plt.Rectangle((0.02, 0.55), 0.47, 0.42,
                                        facecolor='#f0fdf4', edgecolor=colors['secondary'],
                                        linewidth=2))
    ax_formulas.text(0.255, 0.92, 'SENO', fontsize=12, fontweight='bold',
                    ha='center', color=colors['secondary'])
    
    ax_formulas.text(0.255, 0.8, r'$\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$',
                    fontsize=11, ha='center', color=colors['text'])
    ax_formulas.text(0.255, 0.65, r'$\sin(\alpha - \beta) = \sin\alpha\cos\beta - \cos\alpha\sin\beta$',
                    fontsize=11, ha='center', color=colors['text'])
    
    # Coseno suma y diferencia
    ax_formulas.add_patch(plt.Rectangle((0.51, 0.55), 0.47, 0.42,
                                        facecolor='#eff6ff', edgecolor=colors['tertiary'],
                                        linewidth=2))
    ax_formulas.text(0.745, 0.92, 'COSENO', fontsize=12, fontweight='bold',
                    ha='center', color=colors['tertiary'])
    
    ax_formulas.text(0.745, 0.8, r'$\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$',
                    fontsize=11, ha='center', color=colors['text'])
    ax_formulas.text(0.745, 0.65, r'$\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta$',
                    fontsize=11, ha='center', color=colors['text'])
    
    # Tangente
    ax_formulas.add_patch(plt.Rectangle((0.02, 0.08), 0.96, 0.42,
                                        facecolor='#fef3c7', edgecolor='#f59e0b',
                                        linewidth=2))
    ax_formulas.text(0.5, 0.45, 'TANGENTE', fontsize=12, fontweight='bold',
                    ha='center', color='#f59e0b')
    
    ax_formulas.text(0.5, 0.32, 
                    r'$\tan(\alpha + \beta) = \frac{\tan\alpha + \tan\beta}{1 - \tan\alpha\tan\beta}$',
                    fontsize=12, ha='center', color=colors['text'])
    ax_formulas.text(0.5, 0.17,
                    r'$\tan(\alpha - \beta) = \frac{\tan\alpha - \tan\beta}{1 + \tan\alpha\tan\beta}$',
                    fontsize=12, ha='center', color=colors['text'])
    
    fig.suptitle('Identidades de Suma y Diferencia de Ángulos', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "identidades_suma_diferencia.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'identidades_suma_diferencia.svg'}")
