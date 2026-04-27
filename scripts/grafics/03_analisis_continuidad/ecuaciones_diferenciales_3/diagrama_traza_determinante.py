# yaml_frontmatter:
#   id: 'diagrama_traza_determinante'
#   title: 'Diagrama de clasificación de puntos de equilibrio usando traza y determinante'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'ecuaciones_diferenciales_3']

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
from matplotlib.patches import FancyBboxPatch

    setup_style,
    get_colors,
    get_output_dir_for_topic,
    save_figure,
)

# ============================================================
# Metadatos del Gráfico
# ============================================================



def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Límites del diagrama
    tau_max = 6
    delta_max = 10
    
    ax.set_xlim(-tau_max, tau_max)
    ax.set_ylim(-delta_max * 0.3, delta_max)
    
    # Colores
    c_stable = colors['accent']      # Verde - estable
    c_unstable = colors['secondary'] # Rojo - inestable
    c_saddle = colors['tertiary']    # Púrpura - punto silla
    c_center = colors['primary']     # Azul - centro
    
    # =========================================
    # Regiones del diagrama
    # =========================================
    
    # Parábola Δ = τ²/4 (frontera entre nodos y espirales)
    tau_parab = np.linspace(-tau_max, tau_max, 500)
    delta_parab = tau_parab**2 / 4
    
    # Región: Punto silla (Δ < 0)
    ax.fill_between([-tau_max, tau_max], [-delta_max*0.3, -delta_max*0.3], [0, 0],
                    color=c_saddle, alpha=0.25, label='Punto silla (inestable)')
    
    # Región: Nodos estables (Δ > 0, τ < 0, encima de parábola)
    tau_left = np.linspace(-tau_max, 0, 250)
    delta_left = tau_left**2 / 4
    ax.fill_between(tau_left, delta_left, [delta_max]*len(tau_left),
                    color=c_stable, alpha=0.3, label='Nodo estable')
    
    # Región: Nodos inestables (Δ > 0, τ > 0, encima de parábola)
    tau_right = np.linspace(0, tau_max, 250)
    delta_right = tau_right**2 / 4
    ax.fill_between(tau_right, delta_right, [delta_max]*len(tau_right),
                    color=c_unstable, alpha=0.3, label='Nodo inestable')
    
    # Región: Espirales estables (0 < Δ < τ²/4, τ < 0)
    tau_spiral_left = np.linspace(-tau_max, 0, 250)
    delta_spiral_left = tau_spiral_left**2 / 4
    ax.fill_between(tau_spiral_left, [0]*len(tau_spiral_left), delta_spiral_left,
                    color=c_stable, alpha=0.5, label='Espiral estable')
    
    # Región: Espirales inestables (0 < Δ < τ²/4, τ > 0)
    tau_spiral_right = np.linspace(0, tau_max, 250)
    delta_spiral_right = tau_spiral_right**2 / 4
    ax.fill_between(tau_spiral_right, [0]*len(tau_spiral_right), delta_spiral_right,
                    color=c_unstable, alpha=0.5, label='Espiral inestable')
    
    # =========================================
    # Curvas y ejes
    # =========================================
    
    # Eje Δ (línea vertical en τ = 0)
    ax.axvline(x=0, color='#1f2937', linewidth=2, zorder=5)
    
    # Eje τ (línea horizontal en Δ = 0)
    ax.axhline(y=0, color='#1f2937', linewidth=2, zorder=5)
    
    # Parábola Δ = τ²/4 (frontera nodo/espiral)
    ax.plot(tau_parab, delta_parab, 'k--', linewidth=2.5, 
            label=r'$\Delta = \tau^2/4$ (frontera)', zorder=6)
    
    # =========================================
    # Etiquetas de regiones
    # =========================================
    
    # Punto silla
    ax.text(0, -1.5, 'PUNTO SILLA\n(inestable)', ha='center', va='center',
            fontsize=12, weight='bold', color='#5b21b6',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#5b21b6', alpha=0.9))
    
    # Espirales estables
    ax.text(-3, 1.5, 'ESPIRAL\nESTABLE', ha='center', va='center',
            fontsize=11, weight='bold', color='#047857',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#047857', alpha=0.9))
    
    # Espirales inestables
    ax.text(3, 1.5, 'ESPIRAL\nINESTABLE', ha='center', va='center',
            fontsize=11, weight='bold', color='#b91c1c',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#b91c1c', alpha=0.9))
    
    # Nodos estables
    ax.text(-3.5, 6, 'NODO\nESTABLE', ha='center', va='center',
            fontsize=11, weight='bold', color='#047857',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#047857', alpha=0.9))
    
    # Nodos inestables
    ax.text(3.5, 6, 'NODO\nINESTABLE', ha='center', va='center',
            fontsize=11, weight='bold', color='#b91c1c',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#b91c1c', alpha=0.9))
    
    # Centro (sobre el eje τ = 0, Δ > 0)
    ax.plot(0, 4, 'o', markersize=12, color=c_center, zorder=7)
    ax.text(0.8, 4, 'CENTRO\n(neutralmente estable)', ha='left', va='center',
            fontsize=10, weight='bold', color='#1d4ed8',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#1d4ed8', alpha=0.9))
    
    # =========================================
    # Configuración de ejes
    # =========================================
    
    ax.set_xlabel(r'$\tau$ (traza)', fontsize=14, weight='bold')
    ax.set_ylabel(r'$\Delta$ (determinante)', fontsize=14, weight='bold')
    
    # Grid
    ax.grid(True, linestyle=':', alpha=0.4, color='#9ca3af')
    ax.set_axisbelow(True)
    
    # Marcas en ejes
    ax.set_xticks(range(-int(tau_max), int(tau_max)+1))
    ax.set_yticks(range(-2, int(delta_max)+1, 2))
    
    # =========================================
    # Anotaciones adicionales
    # =========================================
    
    # Flecha indicando estabilidad
    ax.annotate('', xy=(-5.5, 8), xytext=(-5.5, 2),
                arrowprops=dict(arrowstyle='->', color='#059669', lw=3))
    ax.text(-5.5, 5, 'Más\nestable', ha='center', va='center', fontsize=9,
            color='#059669', weight='bold', rotation=90)
    
    ax.annotate('', xy=(5.5, 8), xytext=(5.5, 2),
                arrowprops=dict(arrowstyle='->', color='#dc2626', lw=3))
    ax.text(5.5, 5, 'Más\ninestable', ha='center', va='center', fontsize=9,
            color='#dc2626', weight='bold', rotation=90)
    
    # Fórmulas
    formula_box = (
        r"$\tau = \text{tr}(A) = \lambda_1 + \lambda_2$" + "\n" +
        r"$\Delta = \det(A) = \lambda_1 \cdot \lambda_2$" + "\n" +
        r"$D = \tau^2 - 4\Delta = (\lambda_1 - \lambda_2)^2$"
    )
    ax.text(tau_max - 0.3, delta_max - 0.5, formula_box, ha='right', va='top',
            fontsize=10, fontfamily='DejaVu Sans',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#f8fafc', edgecolor='#64748b', alpha=0.95))
    
    # =========================================
    # Leyenda y título
    # =========================================
    
    ax.legend(loc='lower right', fontsize=9, framealpha=0.95)
    
    fig.suptitle("Clasificación de Puntos de Equilibrio: Diagrama Traza-Determinante",
                fontsize=15, weight='bold', y=0.98, color='#1f2937')
    
    plt.tight_layout()
    return fig


# ============================================================
# Ejecución directa para pruebas
# ============================================================

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "03_analisis_continuidad"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "diagrama_traza_determinante.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'diagrama_traza_determinante.svg'}")
