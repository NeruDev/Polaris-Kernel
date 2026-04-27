# yaml_frontmatter:
#   id: 'regiones_integracion_doble'
#   title: 'Regiones Tipo I y Tipo II'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'integracion_multiple']

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
    gs = fig.add_gridspec(1, 3, width_ratios=[1.2, 1.2, 0.8])
    
    ax_type1 = fig.add_subplot(gs[0])
    ax_type2 = fig.add_subplot(gs[1])
    ax_info = fig.add_subplot(gs[2])
    
    # =========================================
    # TIPO I: a ≤ x ≤ b, g₁(x) ≤ y ≤ g₂(x)
    # =========================================
    ax_type1.set_aspect('equal')
    ax_type1.grid(True, linestyle='--', alpha=0.3)
    
    # Límites
    a, b = 0.5, 3.0
    x = np.linspace(a, b, 200)
    
    # Funciones límite
    g1 = 0.3*x  # Curva inferior
    g2 = np.sqrt(x) + 0.5  # Curva superior
    
    # Región sombreada
    ax_type1.fill_between(x, g1, g2, color=colors['primary'], alpha=0.3)
    
    # Curvas límite
    x_ext = np.linspace(0, 3.5, 200)
    ax_type1.plot(x_ext, 0.3*x_ext, color='#dc2626', linewidth=2, label=r'$y = g_1(x)$')
    ax_type1.plot(x_ext, np.sqrt(np.maximum(x_ext, 0)) + 0.5, color='#10b981', linewidth=2, label=r'$y = g_2(x)$')
    
    # Líneas verticales en a y b
    ax_type1.axvline(x=a, color=colors['primary'], linewidth=2, linestyle='--')
    ax_type1.axvline(x=b, color=colors['primary'], linewidth=2, linestyle='--')
    
    # Elemento diferencial (franja vertical)
    x_strip = 1.8
    y1_strip = 0.3*x_strip
    y2_strip = np.sqrt(x_strip) + 0.5
    ax_type1.fill_between([x_strip-0.08, x_strip+0.08], [y1_strip, y1_strip], 
                         [y2_strip, y2_strip], color='#f59e0b', alpha=0.6)
    ax_type1.annotate('', xy=(x_strip, y2_strip), xytext=(x_strip, y1_strip),
                     arrowprops=dict(arrowstyle='<->', color='#f59e0b', lw=2))
    ax_type1.text(x_strip+0.15, (y1_strip+y2_strip)/2, 'dy', fontsize=10, 
                 color='#f59e0b', fontweight='bold')
    ax_type1.annotate('', xy=(x_strip+0.08, 0.1), xytext=(x_strip-0.08, 0.1),
                     arrowprops=dict(arrowstyle='<->', color='#f59e0b', lw=1.5))
    ax_type1.text(x_strip, 0.02, 'dx', fontsize=9, color='#f59e0b', ha='center')
    
    # Etiquetas
    ax_type1.text(a, -0.25, 'a', fontsize=11, ha='center', color=colors['primary'])
    ax_type1.text(b, -0.25, 'b', fontsize=11, ha='center', color=colors['primary'])
    ax_type1.text(1.5, 1.0, 'R', fontsize=14, fontweight='bold', color=colors['primary'])
    
    ax_type1.set_xlim([0, 3.5])
    ax_type1.set_ylim([-0.3, 2.5])
    ax_type1.set_xlabel('x', fontsize=11)
    ax_type1.set_ylabel('y', fontsize=11)
    ax_type1.set_title('TIPO I: Integrar primero en y', fontsize=11, fontweight='bold', color=colors['primary'])
    ax_type1.legend(loc='upper left', fontsize=9)
    
    # =========================================
    # TIPO II: c ≤ y ≤ d, h₁(y) ≤ x ≤ h₂(y)
    # =========================================
    ax_type2.set_aspect('equal')
    ax_type2.grid(True, linestyle='--', alpha=0.3)
    
    # Límites
    c, d = 0.5, 2.2
    y = np.linspace(c, d, 200)
    
    # Funciones límite
    h1 = y**2 / 3  # Curva izquierda
    h2 = 2.5 - y/2  # Curva derecha
    
    # Región sombreada
    ax_type2.fill_betweenx(y, h1, h2, color='#10b981', alpha=0.3)
    
    # Curvas límite
    y_ext = np.linspace(0, 2.5, 200)
    ax_type2.plot(y_ext**2/3, y_ext, color='#dc2626', linewidth=2, label=r'$x = h_1(y)$')
    ax_type2.plot(2.5 - y_ext/2, y_ext, color=colors['primary'], linewidth=2, label=r'$x = h_2(y)$')
    
    # Líneas horizontales en c y d
    ax_type2.axhline(y=c, color='#10b981', linewidth=2, linestyle='--')
    ax_type2.axhline(y=d, color='#10b981', linewidth=2, linestyle='--')
    
    # Elemento diferencial (franja horizontal)
    y_strip = 1.4
    x1_strip = y_strip**2 / 3
    x2_strip = 2.5 - y_strip/2
    ax_type2.fill_between([x1_strip, x2_strip], [y_strip-0.06, y_strip-0.06], 
                         [y_strip+0.06, y_strip+0.06], color='#f59e0b', alpha=0.6)
    ax_type2.annotate('', xy=(x2_strip, y_strip), xytext=(x1_strip, y_strip),
                     arrowprops=dict(arrowstyle='<->', color='#f59e0b', lw=2))
    ax_type2.text((x1_strip+x2_strip)/2, y_strip+0.15, 'dx', fontsize=10, 
                 color='#f59e0b', fontweight='bold', ha='center')
    ax_type2.annotate('', xy=(0.1, y_strip+0.06), xytext=(0.1, y_strip-0.06),
                     arrowprops=dict(arrowstyle='<->', color='#f59e0b', lw=1.5))
    ax_type2.text(0.02, y_strip, 'dy', fontsize=9, color='#f59e0b', va='center')
    
    # Etiquetas
    ax_type2.text(-0.2, c, 'c', fontsize=11, ha='center', va='center', color='#10b981')
    ax_type2.text(-0.2, d, 'd', fontsize=11, ha='center', va='center', color='#10b981')
    ax_type2.text(1.2, 1.35, 'R', fontsize=14, fontweight='bold', color='#10b981')
    
    ax_type2.set_xlim([-0.3, 2.8])
    ax_type2.set_ylim([0, 2.5])
    ax_type2.set_xlabel('x', fontsize=11)
    ax_type2.set_ylabel('y', fontsize=11)
    ax_type2.set_title('TIPO II: Integrar primero en x', fontsize=11, fontweight='bold', color='#10b981')
    ax_type2.legend(loc='upper right', fontsize=9)
    
    # =========================================
    # PANEL INFO
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Tipo I
    ax_info.add_patch(plt.Rectangle((0.02, 0.60), 0.96, 0.38,
                                    facecolor='#eff6ff', edgecolor=colors['primary'],
                                    linewidth=2))
    ax_info.text(0.5, 0.94, 'TIPO I', fontsize=11,
                fontweight='bold', ha='center', color=colors['primary'])
    ax_info.text(0.5, 0.82, r'$\iint_R f \, dA =$',
                fontsize=10, ha='center', color=colors['text'])
    ax_info.text(0.5, 0.68, r'$\int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y) \, dy \, dx$',
                fontsize=10, ha='center', color=colors['text'])
    
    # Tipo II
    ax_info.add_patch(plt.Rectangle((0.02, 0.18), 0.96, 0.38,
                                    facecolor='#f0fdf4', edgecolor='#10b981',
                                    linewidth=2))
    ax_info.text(0.5, 0.52, 'TIPO II', fontsize=11,
                fontweight='bold', ha='center', color='#10b981')
    ax_info.text(0.5, 0.40, r'$\iint_R f \, dA =$',
                fontsize=10, ha='center', color=colors['text'])
    ax_info.text(0.5, 0.26, r'$\int_c^d \int_{h_1(y)}^{h_2(y)} f(x,y) \, dx \, dy$',
                fontsize=10, ha='center', color=colors['text'])
    
    # Nota
    ax_info.text(0.5, 0.08, 'Cambio de orden: Tipo I ↔ Tipo II',
                fontsize=9, ha='center', color='#6b7280', style='italic')
    
    fig.suptitle('Regiones de Integración Doble', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "regiones_integracion_doble.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'regiones_integracion_doble.svg'}")
