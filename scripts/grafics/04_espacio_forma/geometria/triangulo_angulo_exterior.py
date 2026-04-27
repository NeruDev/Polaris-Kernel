# yaml_frontmatter:
#   id: 'triangulo_angulo_exterior'
#   title: 'Ángulo exterior del triángulo = suma de ángulos interiores no adyacentes'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria']

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[3]))
from templates import setup_style, get_colors
import matplotlib.pyplot as plt
import numpy as np
def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    # Crear figura con GridSpec: 2 columnas (figura | información)
    fig = plt.figure(figsize=(13, 7), layout='constrained')
    gs = fig.add_gridspec(1, 2, width_ratios=[1.3, 1], wspace=0.08)
    
    ax = fig.add_subplot(gs[0])      # Panel izquierdo: figura geométrica
    ax_info = fig.add_subplot(gs[1]) # Panel derecho: información
    
    # =========================================
    # PANEL IZQUIERDO: Figura Geométrica
    # =========================================
    
    # Triángulo ABC
    A = np.array([0, 0])
    B = np.array([5, 0])
    C = np.array([1.5, 3])
    
    # Extensión del lado BC más allá de C
    D = C + 2.5 * (C - B) / np.linalg.norm(C - B)
    
    # Triángulo
    triangle = plt.Polygon([A, B, C], fill=True, facecolor=colors['primary'],
                          alpha=0.15, edgecolor=colors['primary'], linewidth=2.5)
    ax.add_patch(triangle)
    
    # Extensión del lado
    ax.plot([B[0], D[0]], [B[1], D[1]], '--', color='#374151', lw=2)
    
    # Vértices (posiciones ajustadas para estar fuera de la figura)
    vertices_config = [
        (A, 'A', (-0.4, -0.35)),
        (B, 'B', (0.3, -0.35)), 
        (C, 'C', (-0.35, 0.25)),
        (D, 'D', (0.25, 0.15))
    ]
    for p, label, offset in vertices_config:
        ax.plot(p[0], p[1], 'o', color='#374151', markersize=7)
        ax.text(p[0]+offset[0], p[1]+offset[1], label, fontsize=12, fontweight='bold')
    
    # Ángulo en A (α)
    vA1 = B - A
    vA2 = C - A
    aA1 = np.arctan2(vA1[1], vA1[0])
    aA2 = np.arctan2(vA2[1], vA2[0])
    arc_A = np.linspace(aA1, aA2, 30)
    ax.plot(A[0] + 0.5*np.cos(arc_A), A[1] + 0.5*np.sin(arc_A), 
           color=colors['secondary'], lw=2.5)
    ax.text(A[0]+0.7, A[1]+0.4, 'α', fontsize=14, color=colors['secondary'], fontweight='bold')
    
    # Ángulo en B (β)
    vB1 = A - B
    vB2 = C - B
    aB1 = np.arctan2(vB1[1], vB1[0])
    aB2 = np.arctan2(vB2[1], vB2[0])
    arc_B = np.linspace(aB1, aB2, 30)
    ax.plot(B[0] + 0.5*np.cos(arc_B), B[1] + 0.5*np.sin(arc_B), 
           color=colors['accent'], lw=2.5)
    ax.text(B[0]-0.6, B[1]+0.55, 'β', fontsize=14, color=colors['accent'], fontweight='bold')
    
    # Ángulo interior en C (γ) - más pequeño
    vC1 = A - C
    vC2 = B - C
    aC1 = np.arctan2(vC1[1], vC1[0])
    aC2 = np.arctan2(vC2[1], vC2[0])
    if aC1 < aC2:
        arc_C = np.linspace(aC1, aC2, 30)
    else:
        arc_C = np.linspace(aC2, aC1, 30)
    ax.plot(C[0] + 0.35*np.cos(arc_C), C[1] + 0.35*np.sin(arc_C), 
           color='#6b7280', lw=2)
    ax.text(C[0]+0.2, C[1]-0.6, 'γ', fontsize=12, color='#6b7280')
    
    # ÁNGULO EXTERIOR en C (θ) - destacado
    vC_ext = D - C
    aC_ext = np.arctan2(vC_ext[1], vC_ext[0])
    if aC_ext < aC1:
        aC_ext += 2*np.pi
    arc_ext = np.linspace(aC1, aC_ext, 40)
    ax.fill(np.concatenate([[C[0]], C[0] + 0.7*np.cos(arc_ext), [C[0]]]),
            np.concatenate([[C[1]], C[1] + 0.7*np.sin(arc_ext), [C[1]]]),
            color=colors['tertiary'], alpha=0.25)
    ax.plot(C[0] + 0.7*np.cos(arc_ext), C[1] + 0.7*np.sin(arc_ext), 
           color=colors['tertiary'], lw=3)
    ax.text(C[0]-0.2, C[1]+0.95, 'θ', fontsize=16, color=colors['tertiary'], fontweight='bold')
    
    ax.set_xlim(-0.8, 5.5)
    ax.set_ylim(-0.8, 4.2)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Figura', fontsize=11, fontweight='bold', color='#6b7280')
    
    # =========================================
    # PANEL DERECHO: Información y Propiedades
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # === SECCIÓN 1: Fórmula Principal Destacada ===
    # Caja de fórmula (elemento didáctico principal)
    ax_info.add_patch(plt.Rectangle((0.05, 0.78), 0.9, 0.18, 
                                     facecolor='#fffbeb', edgecolor=colors['tertiary'],
                                     linewidth=2, transform=ax_info.transAxes,
                                     clip_on=False, zorder=1))
    ax_info.text(0.5, 0.90, 'FÓRMULA PRINCIPAL', fontsize=9, fontweight='bold',
                ha='center', va='center', color=colors['tertiary'])
    ax_info.text(0.5, 0.82, r'$\theta = \alpha + \beta$', fontsize=22,
                ha='center', va='center', color=colors['tertiary'], fontweight='bold')
    
    # === SECCIÓN 2: Leyenda de Símbolos ===
    ax_info.axhline(y=0.74, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    ax_info.text(0.5, 0.70, 'Leyenda de Símbolos', fontsize=10, fontweight='bold', 
                ha='center', color='#374151')
    
    legend_items = [
        ('α', colors['secondary'], 'ángulo interior en A'),
        ('β', colors['accent'], 'ángulo interior en B'),
        ('γ', '#6b7280', 'ángulo interior en C'),
        ('θ', colors['tertiary'], 'ángulo exterior en C'),
    ]
    for i, (sym, col, desc) in enumerate(legend_items):
        y = 0.62 - i*0.065
        ax_info.text(0.10, y, sym, fontsize=13, fontweight='bold', color=col, va='center')
        ax_info.text(0.18, y, f'= {desc}', fontsize=9, color='#374151', va='center')
    
    # === SECCIÓN 3: Propiedad ===
    ax_info.axhline(y=0.36, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    ax_info.text(0.5, 0.32, 'Propiedad', fontsize=10, fontweight='bold', ha='center', color='#374151')
    prop_text = (
        "El ángulo exterior de un triángulo es igual\n"
        "a la suma de los dos ángulos interiores\n"
        "no adyacentes a él."
    )
    ax_info.text(0.5, 0.28, prop_text, fontsize=9, ha='center', va='top',
                color='#4b5563', linespacing=1.3)
    
    # === SECCIÓN 4: Demostración ===
    ax_info.axhline(y=0.14, xmin=0.05, xmax=0.95, color='#e5e7eb', lw=1)
    ax_info.text(0.5, 0.10, 'Demostración', fontsize=10, fontweight='bold', ha='center', color='#6b7280')
    
    # Demostración en caja separada para evitar superposición
    demo_box = plt.Rectangle((0.08, 0.01), 0.84, 0.08, 
                              facecolor='#f9fafb', edgecolor='#d1d5db',
                              linewidth=1, transform=ax_info.transAxes)
    ax_info.add_patch(demo_box)
    ax_info.text(0.5, 0.05, r'$\alpha + \beta + \gamma = 180°$  y  $\theta + \gamma = 180°$  $\Rightarrow$  $\theta = \alpha + \beta$', 
                fontsize=9, ha='center', va='center', color='#4b5563')
    
    # Título general
    fig.suptitle('Ángulo Exterior del Triángulo', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "triangulo_angulo_exterior.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'triangulo_angulo_exterior.svg'}")
