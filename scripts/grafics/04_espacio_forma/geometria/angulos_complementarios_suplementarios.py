# yaml_frontmatter:
#   id: 'angulos_complementarios_suplementarios'
#   title: 'Ángulos complementarios (90°) y suplementarios (180°)'
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
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), layout='constrained')
    
    # === Ángulos Complementarios (suman 90°) ===
    ax1.set_xlim(-0.5, 3)
    ax1.set_ylim(-0.5, 2.5)
    ax1.set_aspect('equal')
    ax1.axis('off')
    
    # Punto origen
    O = (0, 0)
    length = 2.0
    
    # Ángulo α = 35°
    alpha = 35
    alpha_rad = np.radians(alpha)
    
    # Ángulo β = 55° (complementario)
    beta = 55
    
    # Rayo horizontal
    ax1.annotate('', xy=(length, 0), xytext=O,
                arrowprops=dict(arrowstyle='->', color='#374151', lw=2))
    
    # Rayo a 35°
    ax1.annotate('', xy=(length * np.cos(alpha_rad), length * np.sin(alpha_rad)), 
                xytext=O, arrowprops=dict(arrowstyle='->', color=colors['primary'], lw=2))
    
    # Rayo vertical (90°)
    ax1.annotate('', xy=(0, length), xytext=O,
                arrowprops=dict(arrowstyle='->', color='#374151', lw=2))
    
    # Arco para α
    arc1 = np.linspace(0, alpha_rad, 30)
    ax1.plot(0.5 * np.cos(arc1), 0.5 * np.sin(arc1), color=colors['primary'], lw=2)
    ax1.text(0.7, 0.2, 'α', fontsize=14, color=colors['primary'], fontweight='bold')
    
    # Arco para β
    arc2 = np.linspace(alpha_rad, np.pi/2, 30)
    ax1.plot(0.4 * np.cos(arc2), 0.4 * np.sin(arc2), color=colors['secondary'], lw=2)
    ax1.text(0.2, 0.6, 'β', fontsize=14, color=colors['secondary'], fontweight='bold')
    
    # Símbolo de ángulo recto
    rect_size = 0.15
    ax1.plot([rect_size, rect_size, 0], [0, rect_size, rect_size], color='#374151', lw=1.5)
    
    # Etiquetas
    ax1.text(1.0, -0.3, 'α + β = 90°', fontsize=12, ha='center', fontweight='bold')
    ax1.text(1.0, 2.2, 'Ángulos Complementarios', fontsize=13, ha='center', 
             fontweight='bold', color='#1f2937')
    ax1.text(1.0, 1.9, f'α = {alpha}°, β = {beta}°', fontsize=11, ha='center', 
             color='#6b7280')
    
    # === Ángulos Suplementarios (suman 180°) ===
    ax2.set_xlim(-2.5, 2.5)
    ax2.set_ylim(-0.5, 2)
    ax2.set_aspect('equal')
    ax2.axis('off')
    
    # Ángulo α = 60°
    alpha2 = 60
    alpha2_rad = np.radians(alpha2)
    
    # Ángulo β = 120° (suplementario)
    beta2 = 120
    
    # Recta base (180°)
    ax2.annotate('', xy=(2, 0), xytext=(-2, 0),
                arrowprops=dict(arrowstyle='<->', color='#374151', lw=2))
    
    # Rayo a 60° desde el origen
    ax2.annotate('', xy=(length * np.cos(alpha2_rad), length * np.sin(alpha2_rad)), 
                xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=colors['accent'], lw=2))
    
    # Arco para α (lado derecho)
    arc3 = np.linspace(0, alpha2_rad, 30)
    ax2.plot(0.5 * np.cos(arc3), 0.5 * np.sin(arc3), color=colors['primary'], lw=2)
    ax2.text(0.6, 0.3, 'α', fontsize=14, color=colors['primary'], fontweight='bold')
    
    # Arco para β (lado izquierdo)
    arc4 = np.linspace(alpha2_rad, np.pi, 30)
    ax2.plot(0.4 * np.cos(arc4), 0.4 * np.sin(arc4), color=colors['secondary'], lw=2)
    ax2.text(-0.5, 0.4, 'β', fontsize=14, color=colors['secondary'], fontweight='bold')
    
    # Etiquetas
    ax2.text(0, -0.3, 'α + β = 180°', fontsize=12, ha='center', fontweight='bold')
    ax2.text(0, 1.8, 'Ángulos Suplementarios', fontsize=13, ha='center', 
             fontweight='bold', color='#1f2937')
    ax2.text(0, 1.5, f'α = {alpha2}°, β = {beta2}°', fontsize=11, ha='center', 
             color='#6b7280')
    
    return fig

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "angulos_complementarios_suplementarios.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'angulos_complementarios_suplementarios.svg'}")
