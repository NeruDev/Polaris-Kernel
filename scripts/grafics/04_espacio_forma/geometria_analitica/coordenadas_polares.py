# yaml_frontmatter:
#   id: 'coordenadas_polares'
#   title: 'Coordenadas polares y conversión cartesiana-polar'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria_analitica']

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
    gs = fig.add_gridspec(2, 3, height_ratios=[1.2, 1], hspace=0.2, wspace=0.2)
    
    ax_main = fig.add_subplot(gs[0, :2])
    ax_conv = fig.add_subplot(gs[0, 2])
    ax_curvas = fig.add_subplot(gs[1, :], projection='polar')
    
    # =========================================
    # PANEL PRINCIPAL: Sistema polar
    # =========================================
    ax_main.grid(True, linestyle='--', alpha=0.3)
    ax_main.axhline(y=0, color='#9ca3af', linewidth=1)
    ax_main.axvline(x=0, color='#9ca3af', linewidth=1)
    
    # Punto ejemplo
    r = 3
    theta = np.pi/3  # 60°
    Px = r * np.cos(theta)
    Py = r * np.sin(theta)
    
    # Dibujar radio vector
    ax_main.annotate('', xy=(Px, Py), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color=colors['primary'],
                                   linewidth=2.5))
    
    # Punto P
    ax_main.plot(Px, Py, 'o', color=colors['accent'], markersize=12, zorder=5)
    ax_main.text(Px + 0.2, Py + 0.3, r'$P(r, \theta)$', fontsize=12,
                fontweight='bold', color=colors['accent'])
    ax_main.text(Px + 0.2, Py - 0.5, r'$P(3, 60°)$', fontsize=10, color='#6b7280')
    
    # Arco para el ángulo
    theta_arc = np.linspace(0, theta, 30)
    r_arc = 0.8
    ax_main.plot(r_arc*np.cos(theta_arc), r_arc*np.sin(theta_arc),
                color=colors['secondary'], linewidth=2)
    ax_main.text(0.8, 0.3, r'$\theta$', fontsize=14, color=colors['secondary'],
                fontweight='bold')
    
    # Radio r
    ax_main.text(r/2*np.cos(theta) - 0.3, r/2*np.sin(theta) + 0.3,
                'r', fontsize=14, fontweight='bold', color=colors['primary'])
    
    # Polo y eje polar
    ax_main.plot(0, 0, 'o', color='#374151', markersize=8)
    ax_main.text(0.15, -0.4, 'Polo', fontsize=10, color='#374151')
    ax_main.annotate('', xy=(4, 0), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color='#374151',
                                   linewidth=1.5))
    ax_main.text(4, -0.4, 'Eje polar', fontsize=10, color='#374151')
    
    # Proyecciones (coordenadas cartesianas)
    ax_main.plot([Px, Px], [0, Py], ':', color='#9ca3af', linewidth=1.5)
    ax_main.plot([0, Px], [Py, Py], ':', color='#9ca3af', linewidth=1.5)
    ax_main.text(Px, -0.4, f'x = r cos θ', fontsize=9, ha='center', color='#6b7280')
    ax_main.text(-0.8, Py, f'y = r sin θ', fontsize=9, va='center', color='#6b7280')
    
    # Círculos de referencia
    for ri in [1, 2, 3, 4]:
        circle = plt.Circle((0, 0), ri, fill=False, color='#e5e7eb', linestyle='--',
                            linewidth=0.8)
        ax_main.add_patch(circle)
        ax_main.text(ri*0.71, ri*0.71, str(ri), fontsize=8, color='#9ca3af')
    
    ax_main.set_xlim(-1, 5)
    ax_main.set_ylim(-1, 4)
    ax_main.set_aspect('equal')
    ax_main.set_xlabel('x', fontsize=11)
    ax_main.set_ylabel('y', fontsize=11)
    ax_main.set_title('Sistema de Coordenadas Polares', fontsize=11, fontweight='bold')
    
    # =========================================
    # PANEL DERECHO: Conversiones
    # =========================================
    ax_conv.axis('off')
    ax_conv.set_xlim(0, 1)
    ax_conv.set_ylim(0, 1)
    
    ax_conv.text(0.5, 0.95, 'CONVERSIONES', fontsize=11,
                fontweight='bold', ha='center', color=colors['primary'])
    
    # Polar a Cartesiana
    ax_conv.add_patch(plt.Rectangle((0.02, 0.52), 0.96, 0.38,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=1.5))
    ax_conv.text(0.5, 0.84, 'Polar → Cartesiana', fontsize=10,
                fontweight='bold', ha='center', color=colors['primary'])
    ax_conv.text(0.5, 0.72, r'$x = r \cos\theta$', fontsize=12, ha='center')
    ax_conv.text(0.5, 0.58, r'$y = r \sin\theta$', fontsize=12, ha='center')
    
    # Cartesiana a Polar
    ax_conv.add_patch(plt.Rectangle((0.02, 0.08), 0.96, 0.40,
                                    facecolor='#f0fdf4', edgecolor=colors['secondary'],
                                    linewidth=1.5))
    ax_conv.text(0.5, 0.42, 'Cartesiana → Polar', fontsize=10,
                fontweight='bold', ha='center', color=colors['secondary'])
    ax_conv.text(0.5, 0.30, r'$r = \sqrt{x^2 + y^2}$', fontsize=12, ha='center')
    ax_conv.text(0.5, 0.16, r'$\theta = \arctan\left(\frac{y}{x}\right)$',
                fontsize=12, ha='center')
    
    # =========================================
    # PANEL INFERIOR: Curvas polares famosas
    # =========================================
    ax_curvas.set_title('Curvas en Coordenadas Polares', fontsize=11, 
                       fontweight='bold', pad=10)
    
    theta_full = np.linspace(0, 2*np.pi, 300)
    
    # Cardioide: r = 1 + cos(θ)
    r_cardioide = 1 + np.cos(theta_full)
    ax_curvas.plot(theta_full, r_cardioide, color=colors['primary'], 
                  linewidth=2, label=r'Cardioide: $r = 1 + \cos\theta$')
    
    # Rosa de 3 pétalos: r = cos(3θ)
    r_rosa = np.abs(np.cos(3*theta_full))
    ax_curvas.plot(theta_full, r_rosa, color=colors['secondary'],
                  linewidth=2, label=r'Rosa: $r = \cos(3\theta)$')
    
    # Espiral de Arquímedes: r = θ/4
    theta_espiral = np.linspace(0, 4*np.pi, 300)
    r_espiral = theta_espiral / 4
    ax_curvas.plot(theta_espiral, r_espiral, color='#f59e0b',
                  linewidth=2, label=r'Espiral: $r = \theta/4$')
    
    # Lemniscata: r² = cos(2θ)
    theta_lem = np.linspace(-np.pi/4, np.pi/4, 100)
    r_lem = np.sqrt(np.abs(np.cos(2*theta_lem)))
    ax_curvas.plot(theta_lem, r_lem, color='#dc2626', linewidth=2,
                  label=r'Lemniscata: $r^2 = \cos(2\theta)$')
    ax_curvas.plot(theta_lem + np.pi, r_lem, color='#dc2626', linewidth=2)
    
    ax_curvas.set_rmax(3)
    ax_curvas.legend(loc='lower left', bbox_to_anchor=(-0.15, -0.25), 
                    fontsize=9, ncol=2)
    
    fig.suptitle('Coordenadas Polares', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "coordenadas_polares.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'coordenadas_polares.svg'}")
