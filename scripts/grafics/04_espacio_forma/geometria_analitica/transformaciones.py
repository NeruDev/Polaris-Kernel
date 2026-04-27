# yaml_frontmatter:
#   id: 'transformaciones'
#   title: 'Transformaciones geométricas: traslación, rotación, reflexión, escalamiento'
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
    
    fig = plt.figure(figsize=(14, 10), layout='constrained')
    gs = fig.add_gridspec(2, 2, hspace=0.25, wspace=0.2)
    
    ax_traslacion = fig.add_subplot(gs[0, 0])
    ax_rotacion = fig.add_subplot(gs[0, 1])
    ax_reflexion = fig.add_subplot(gs[1, 0])
    ax_escala = fig.add_subplot(gs[1, 1])
    
    # Triángulo original (se usará en todas)
    tri_x = np.array([1, 2, 1.5, 1])
    tri_y = np.array([1, 1, 2, 1])
    
    # =========================================
    # PANEL 1: Traslación
    # =========================================
    ax = ax_traslacion
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.axhline(y=0, color='#9ca3af', linewidth=0.8)
    ax.axvline(x=0, color='#9ca3af', linewidth=0.8)
    
    # Original
    ax.fill(tri_x, tri_y, color=colors['primary'], alpha=0.5, edgecolor=colors['primary'],
           linewidth=2)
    ax.text(1.5, 1.3, 'Original', fontsize=9, ha='center', color=colors['primary'])
    
    # Trasladado (h=2, k=1)
    h, k = 2, 1
    ax.fill(tri_x + h, tri_y + k, color=colors['secondary'], alpha=0.5,
           edgecolor=colors['secondary'], linewidth=2)
    ax.text(3.5, 2.3, 'Trasladado', fontsize=9, ha='center', color=colors['secondary'])
    
    # Vector de traslación
    ax.annotate('', xy=(tri_x[0]+h, tri_y[0]+k), xytext=(tri_x[0], tri_y[0]),
               arrowprops=dict(arrowstyle='->', color='#f59e0b', linewidth=2))
    ax.text(1.8, 1.8, '(h,k)', fontsize=10, color='#f59e0b')
    
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 4)
    ax.set_aspect('equal')
    ax.set_title('TRASLACIÓN', fontsize=12, fontweight='bold', color=colors['primary'])
    
    # Fórmulas
    ax.text(2.5, -0.1, r"$x' = x + h$", fontsize=10, ha='center',
           bbox=dict(facecolor='white', edgecolor='none'))
    ax.text(2.5, -0.5, r"$y' = y + k$", fontsize=10, ha='center',
           bbox=dict(facecolor='white', edgecolor='none'))
    
    # =========================================
    # PANEL 2: Rotación
    # =========================================
    ax = ax_rotacion
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.axhline(y=0, color='#9ca3af', linewidth=0.8)
    ax.axvline(x=0, color='#9ca3af', linewidth=0.8)
    
    # Centrar triángulo en el origen para rotar
    cx, cy = 1.5, 1.5
    tri_cent_x = tri_x - cx + 2
    tri_cent_y = tri_y - cy + 2
    
    # Original
    ax.fill(tri_cent_x, tri_cent_y, color=colors['primary'], alpha=0.5,
           edgecolor=colors['primary'], linewidth=2)
    ax.text(2.5, 2.3, 'Original', fontsize=9, ha='center', color=colors['primary'])
    
    # Rotado 45°
    theta = np.pi/4
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    # Rotar alrededor del punto (2, 2)
    pivot_x, pivot_y = 2, 2
    rel_x = tri_cent_x - pivot_x
    rel_y = tri_cent_y - pivot_y
    rot_x = pivot_x + rel_x * cos_t - rel_y * sin_t
    rot_y = pivot_y + rel_x * sin_t + rel_y * cos_t
    
    ax.fill(rot_x, rot_y, color=colors['secondary'], alpha=0.5,
           edgecolor=colors['secondary'], linewidth=2)
    ax.text(1.3, 2.8, 'Rotado 45°', fontsize=9, ha='center', color=colors['secondary'])
    
    # Centro de rotación
    ax.plot(pivot_x, pivot_y, 'o', color='#f59e0b', markersize=10, zorder=5)
    ax.text(pivot_x + 0.2, pivot_y - 0.3, 'Centro', fontsize=9, color='#f59e0b')
    
    # Arco indicando rotación
    arc_t = np.linspace(0, theta, 20)
    arc_r = 0.6
    ax.plot(pivot_x + arc_r*np.cos(arc_t), pivot_y + arc_r*np.sin(arc_t),
           color='#f59e0b', linewidth=2)
    ax.text(pivot_x + 0.7, pivot_y + 0.35, 'θ', fontsize=12, color='#f59e0b')
    
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 4)
    ax.set_aspect('equal')
    ax.set_title('ROTACIÓN', fontsize=12, fontweight='bold', color=colors['secondary'])
    
    # Fórmulas
    ax.text(2, -0.1, r"$x' = x\cos\theta - y\sin\theta$", fontsize=9, ha='center',
           bbox=dict(facecolor='white', edgecolor='none'))
    ax.text(2, -0.5, r"$y' = x\sin\theta + y\cos\theta$", fontsize=9, ha='center',
           bbox=dict(facecolor='white', edgecolor='none'))
    
    # =========================================
    # PANEL 3: Reflexión
    # =========================================
    ax = ax_reflexion
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.axhline(y=0, color='#9ca3af', linewidth=0.8)
    ax.axvline(x=0, color='#9ca3af', linewidth=0.8)
    
    # Triángulo desplazado
    tri_ref_x = tri_x + 0.5
    tri_ref_y = tri_y + 0.5
    
    # Original
    ax.fill(tri_ref_x, tri_ref_y, color=colors['primary'], alpha=0.5,
           edgecolor=colors['primary'], linewidth=2)
    ax.text(2, 2, 'Original', fontsize=9, ha='center', color=colors['primary'])
    
    # Eje de reflexión (y = x)
    ax.plot([0, 4], [0, 4], '--', color='#dc2626', linewidth=2, label='Eje: y = x')
    
    # Reflejado respecto a y=x (intercambiar x,y)
    ax.fill(tri_ref_y, tri_ref_x, color=colors['tertiary'], alpha=0.5,
           edgecolor=colors['tertiary'], linewidth=2)
    ax.text(1.5, 1.7, 'Reflejado', fontsize=9, ha='center', color=colors['tertiary'])
    
    # Reflexión respecto al eje x
    ax.fill(tri_ref_x + 2, -tri_ref_y + 3, color='#f59e0b', alpha=0.3,
           edgecolor='#f59e0b', linewidth=2, linestyle='--')
    ax.text(4, 1.8, 'Ref. eje x', fontsize=8, ha='center', color='#f59e0b')
    
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 4)
    ax.set_aspect('equal')
    ax.set_title('REFLEXIÓN', fontsize=12, fontweight='bold', color='#dc2626')
    ax.legend(loc='upper left', fontsize=8)
    
    # Fórmulas
    ax.text(2.5, -0.1, r"Eje x: $y' = -y$  |  Eje y: $x' = -x$", fontsize=9, ha='center',
           bbox=dict(facecolor='white', edgecolor='none'))
    ax.text(2.5, -0.5, r"y=x: $(x',y') = (y,x)$", fontsize=9, ha='center',
           bbox=dict(facecolor='white', edgecolor='none'))
    
    # =========================================
    # PANEL 4: Escalamiento
    # =========================================
    ax = ax_escala
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.axhline(y=0, color='#9ca3af', linewidth=0.8)
    ax.axvline(x=0, color='#9ca3af', linewidth=0.8)
    
    # Original pequeño
    ax.fill(tri_x, tri_y, color=colors['primary'], alpha=0.5,
           edgecolor=colors['primary'], linewidth=2)
    ax.text(1.5, 1.3, 'Original', fontsize=9, ha='center', color=colors['primary'])
    
    # Escalado uniformemente (factor 1.5)
    s = 1.5
    ax.fill(tri_x * s, tri_y * s, color=colors['secondary'], alpha=0.3,
           edgecolor=colors['secondary'], linewidth=2)
    ax.text(2.25, 2.1, f'k={s}', fontsize=9, ha='center', color=colors['secondary'])
    
    # Escalado no uniforme (kx=2, ky=1)
    kx, ky = 2, 0.8
    ax.fill(tri_x * kx, tri_y * ky + 2.5, color='#f59e0b', alpha=0.3,
           edgecolor='#f59e0b', linewidth=2)
    ax.text(3, 3.3, f'kx={kx}, ky={ky}', fontsize=9, ha='center', color='#f59e0b')
    
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 4.5)
    ax.set_aspect('equal')
    ax.set_title('ESCALAMIENTO', fontsize=12, fontweight='bold', color='#f59e0b')
    
    # Fórmulas
    ax.text(2.5, -0.1, r"Uniforme: $x' = kx$, $y' = ky$", fontsize=9, ha='center',
           bbox=dict(facecolor='white', edgecolor='none'))
    ax.text(2.5, -0.5, r"No uniforme: $x' = k_x x$, $y' = k_y y$", fontsize=9, ha='center',
           bbox=dict(facecolor='white', edgecolor='none'))
    
    fig.suptitle('Transformaciones Geométricas en el Plano', fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "transformaciones.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'transformaciones.svg'}")
