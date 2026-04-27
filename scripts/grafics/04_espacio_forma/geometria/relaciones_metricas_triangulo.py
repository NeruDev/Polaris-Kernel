# yaml_frontmatter:
#   id: 'relaciones_metricas_triangulo'
#   title: 'Relaciones métricas: proyecciones, altura sobre hipotenusa'
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
    
    # Crear figura con GridSpec: 2 filas (figura | fórmulas)
    fig = plt.figure(figsize=(10, 9), layout='constrained')
    gs = fig.add_gridspec(2, 1, height_ratios=[2, 1], hspace=0.08)
    
    ax = fig.add_subplot(gs[0])      # Panel superior: figura geométrica
    ax_info = fig.add_subplot(gs[1]) # Panel inferior: fórmulas
    
    # =========================================
    # PANEL SUPERIOR: Figura Geométrica
    # =========================================
    
    # Triángulo rectángulo con ángulo recto en C
    A = np.array([0, 0])
    B = np.array([8, 0])
    C = np.array([2.5, 4])
    H = np.array([2.5, 0])  # Pie de la altura
    
    # Triángulo principal (rellenado ligeramente)
    triangle = plt.Polygon([A, B, C], fill=True, facecolor=colors['primary'],
                          alpha=0.08, edgecolor='none')
    ax.add_patch(triangle)
    
    # Lados del triángulo
    ax.plot([A[0], B[0]], [A[1], B[1]], color=colors['primary'], lw=3)
    ax.plot([B[0], C[0]], [B[1], C[1]], color=colors['secondary'], lw=3)
    ax.plot([C[0], A[0]], [C[1], A[1]], color=colors['accent'], lw=3)
    
    # Altura (línea discontinua)
    ax.plot([C[0], H[0]], [C[1], H[1]], color=colors['tertiary'], lw=2.5, linestyle='--')
    
    # Proyecciones sobre la hipotenusa
    ax.plot([A[0], H[0]], [A[1], H[1]], color='#f59e0b', lw=5, alpha=0.5)
    ax.plot([H[0], B[0]], [H[1], B[1]], color='#ec4899', lw=5, alpha=0.5)
    
    # Símbolo de ángulo recto en C
    sq = 0.3
    ax.plot([C[0]-sq, C[0]-sq, C[0]], [C[1], C[1]-sq, C[1]-sq], color='#374151', lw=1.5)
    
    # Símbolo de ángulo recto en H
    ax.plot([H[0]+0.25, H[0]+0.25, H[0]], [H[1], H[1]+0.25, H[1]+0.25], color='#374151', lw=1.5)
    
    # Vértices (etiquetas fuera de la figura)
    vertices = [
        (A, 'A', (-0.4, -0.3)),
        (B, 'B', (0.3, -0.3)), 
        (C, 'C', (-0.4, 0.2)),
        (H, 'H', (0.1, -0.4))
    ]
    for p, label, offset in vertices:
        ax.plot(p[0], p[1], 'o', color='#374151', markersize=8)
        ax.text(p[0]+offset[0], p[1]+offset[1], label, fontsize=13, fontweight='bold')
    
    # Etiquetas de segmentos (posicionadas estratégicamente fuera de la figura)
    ax.text(4, -0.65, 'c', fontsize=13, ha='center', color=colors['primary'], fontweight='bold')
    ax.text(5.9, 2.5, 'a', fontsize=13, color=colors['secondary'], fontweight='bold')
    ax.text(0.7, 2.5, 'b', fontsize=13, color=colors['accent'], fontweight='bold')
    ax.text(2.05, 2.0, 'h', fontsize=13, color=colors['tertiary'], fontweight='bold')
    ax.text(1.1, 0.35, 'm', fontsize=12, color='#f59e0b', fontweight='bold')
    ax.text(5.0, 0.35, 'n', fontsize=12, color='#ec4899', fontweight='bold')
    
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # =========================================
    # PANEL INFERIOR: Fórmulas y Leyenda
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Línea separadora superior
    ax_info.axhline(y=0.95, xmin=0.05, xmax=0.95, color='#d1d5db', lw=1)
    
    # --- Columna izquierda: Leyenda ---
    ax_info.text(0.02, 0.88, 'Elementos', fontsize=11, fontweight='bold', color='#374151')
    
    legend_items = [
        ('c', colors['primary'], 'hipotenusa'),
        ('a', colors['secondary'], 'cateto mayor'),
        ('b', colors['accent'], 'cateto menor'),
        ('h', colors['tertiary'], 'altura sobre hipotenusa'),
        ('m', '#f59e0b', 'proyección de b sobre c'),
        ('n', '#ec4899', 'proyección de a sobre c'),
    ]
    for i, (sym, col, desc) in enumerate(legend_items):
        y = 0.78 - i*0.12
        ax_info.text(0.04, y, sym, fontsize=12, fontweight='bold', color=col, va='center')
        ax_info.text(0.09, y, f'= {desc}', fontsize=9, color='#374151', va='center')
    
    # --- Columna derecha: Fórmulas ---
    ax_info.text(0.55, 0.88, 'Relaciones Métricas', fontsize=11, fontweight='bold', color=colors['tertiary'])
    
    formulas = [
        (r'$h^2 = m \cdot n$', 'altura media proporcional'),
        (r'$a^2 = n \cdot c$', 'cateto, proyección e hipotenusa'),
        (r'$b^2 = m \cdot c$', 'cateto, proyección e hipotenusa'),
        (r'$a \cdot b = c \cdot h$', 'producto de catetos'),
    ]
    
    for i, (formula, desc) in enumerate(formulas):
        y = 0.75 - i*0.16
        ax_info.text(0.55, y, formula, fontsize=13, color='#1f2937', va='center',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='#f0f9ff', 
                             edgecolor='#93c5fd', alpha=0.9))
        ax_info.text(0.80, y, desc, fontsize=8, color='#6b7280', va='center', style='italic')
    
    # Línea vertical separadora
    ax_info.axvline(x=0.50, ymin=0.05, ymax=0.90, color='#e5e7eb', lw=1)
    
    # Título general
    fig.suptitle('Relaciones Métricas en el Triángulo Rectángulo', 
                 fontsize=14, fontweight='bold')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "relaciones_metricas_triangulo.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'relaciones_metricas_triangulo.svg'}")
