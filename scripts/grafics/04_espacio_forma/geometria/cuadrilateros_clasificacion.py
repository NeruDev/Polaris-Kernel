# yaml_frontmatter:
#   id: 'cuadrilateros_clasificacion'
#   title: 'Diagrama jerárquico de clasificación de cuadriláteros'
#   pilar: '04_espacio_forma'
#   tags: ['grafico', 'geometria']

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[3]))
from templates import setup_style, get_colors
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path

# Añadir el directorio de templates al path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import matplotlib.patches as patches

    setup_style,
    get_colors,
    get_output_dir_for_topic,
    save_figure,
)

# ============================================================
# Metadatos del Gráfico
# ============================================================


# ============================================================
# Función de Generación
# ============================================================

def generate() -> plt.Figure:
        setup_style()
    colors = get_colors()
    
    # Crear figura con GridSpec: diagrama arriba, leyenda abajo
    fig = plt.figure(figsize=(13, 10), layout='constrained')
    gs = fig.add_gridspec(2, 1, height_ratios=[3, 1], hspace=0.08)
    
    ax = fig.add_subplot(gs[0])      # Panel superior: diagrama jerárquico
    ax_info = fig.add_subplot(gs[1]) # Panel inferior: descripciones
    
    # =========================================
    # PANEL SUPERIOR: Diagrama Jerárquico
    # =========================================
    
    # Configuración del diagrama (más compacto)
    box_width = 2.2
    box_height = 0.55
    v_spacing = 1.5
    y_start = 5
    
    # Definir estructura jerárquica (sin subnotas dentro de las cajas)
    boxes = [
        # Nivel 0 - Raíz
        ("Cuadriláteros", 0, 0, 'primary'),
        
        # Nivel 1 - Primera división
        ("Paralelogramos", -3, 1, 'primary'),
        ("No Paralelogramos", 3, 1, 'tertiary'),
        
        # Nivel 2 - Tipos específicos
        ("Rectángulo", -4.8, 2, 'accent'),
        ("Rombo", -1.5, 2, 'accent'),
        ("Trapecio", 2, 2, 'secondary'),
        ("Trapezoide", 4.8, 2, 'secondary'),
        
        # Nivel 3 - Caso especial
        ("Cuadrado", -3.15, 3, 'accent'),
    ]
    
    # Diccionario de posiciones
    positions = {}
    
    # Dibujar cajas
    for name, x, level, color_key in boxes:
        y = y_start - level * v_spacing
        
        # Seleccionar colores
        if color_key == 'primary':
            face_color = colors['primary']
            alpha = 0.15
        elif color_key == 'accent':
            face_color = colors['accent']
            alpha = 0.2
        elif color_key == 'secondary':
            face_color = colors['secondary']
            alpha = 0.15
        else:
            face_color = colors['tertiary']
            alpha = 0.15
        
        # Dibujar caja con esquinas redondeadas
        rect = patches.FancyBboxPatch(
            (x - box_width/2, y - box_height/2),
            box_width, box_height,
            boxstyle="round,pad=0.05,rounding_size=0.2",
            facecolor=face_color,
            edgecolor=colors['text'],
            alpha=alpha,
            linewidth=2
        )
        ax.add_patch(rect)
        
        # Borde más oscuro
        rect_border = patches.FancyBboxPatch(
            (x - box_width/2, y - box_height/2),
            box_width, box_height,
            boxstyle="round,pad=0.05,rounding_size=0.2",
            facecolor='none',
            edgecolor=face_color,
            linewidth=2,
            alpha=0.8
        )
        ax.add_patch(rect_border)
        
        # Solo nombre (sin subnota)
        ax.text(x, y, name, 
                ha='center', va='center',
                fontsize=10, fontweight='bold',
                color=colors['text'])
        
        positions[name] = (x, y)
    
    # Definir conexiones
    connections = [
        ("Cuadriláteros", "Paralelogramos"),
        ("Cuadriláteros", "No Paralelogramos"),
        ("Paralelogramos", "Rectángulo"),
        ("Paralelogramos", "Rombo"),
        ("No Paralelogramos", "Trapecio"),
        ("No Paralelogramos", "Trapezoide"),
        ("Rectángulo", "Cuadrado"),
        ("Rombo", "Cuadrado"),
    ]
    
    # Dibujar conexiones
    for parent, child in connections:
        px, py = positions[parent]
        cx, cy = positions[child]
        
        # Punto de salida (abajo del padre)
        start_y = py - box_height/2
        # Punto de llegada (arriba del hijo)
        end_y = cy + box_height/2
        
        # Punto medio para curva
        mid_y = (start_y + end_y) / 2
        
        # Dibujar línea con curva suave
        ax.plot([px, px], [start_y, mid_y], 
                color=colors['text'], linewidth=1.5, alpha=0.5)
        ax.plot([px, cx], [mid_y, mid_y], 
                color=colors['text'], linewidth=1.5, alpha=0.5)
        ax.plot([cx, cx], [mid_y, end_y], 
                color=colors['text'], linewidth=1.5, alpha=0.5)
    
    # Dibujar pequeños ejemplos de figuras al lado de cada caja
    example_size = 0.32
    examples = {
        "Rectángulo": 'rectangle',
        "Rombo": 'rhombus', 
        "Cuadrado": 'square',
        "Trapecio": 'trapezoid',
        "Trapezoide": 'trapezium',
    }
    
    for name, shape in examples.items():
        x, y = positions[name]
        x_offset = box_width/2 + 0.45
        draw_mini_shape(ax, (x + x_offset, y), shape, example_size, colors)
    
    # Configurar ejes
    ax.set_xlim(-7, 7)
    ax.set_ylim(-0.8, 5.8)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # =========================================
    # PANEL INFERIOR: Descripciones
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Línea separadora superior
    ax_info.axhline(y=0.95, xmin=0.02, xmax=0.98, color='#d1d5db', lw=1.5)
    
    # Título del panel
    ax_info.text(0.5, 0.88, 'Definiciones', fontsize=11, fontweight='bold', 
                ha='center', color=colors['primary'])
    
    # Descripciones en dos columnas
    descriptions_left = [
        ('Paralelogramos', 'Lados opuestos paralelos', colors['primary']),
        ('Rectángulo', '4 ángulos rectos', colors['accent']),
        ('Rombo', '4 lados iguales', colors['accent']),
        ('Cuadrado', 'Rectángulo + Rombo', colors['accent']),
    ]
    
    descriptions_right = [
        ('No Paralelogramos', 'Sin 2 pares paralelos', colors['tertiary']),
        ('Trapecio', '1 par de lados paralelos', colors['secondary']),
        ('Trapezoide', 'Ningún lado paralelo', colors['secondary']),
    ]
    
    # Columna izquierda
    for i, (name, desc, col) in enumerate(descriptions_left):
        y = 0.72 - i*0.18
        ax_info.text(0.05, y, '•', fontsize=12, color=col, va='center', fontweight='bold')
        ax_info.text(0.08, y, f'{name}:', fontsize=9, color='#374151', va='center', fontweight='bold')
        ax_info.text(0.23, y, desc, fontsize=9, color='#6b7280', va='center')
    
    # Columna derecha
    for i, (name, desc, col) in enumerate(descriptions_right):
        y = 0.72 - i*0.18
        ax_info.text(0.55, y, '•', fontsize=12, color=col, va='center', fontweight='bold')
        ax_info.text(0.58, y, f'{name}:', fontsize=9, color='#374151', va='center', fontweight='bold')
        ax_info.text(0.78, y, desc, fontsize=9, color='#6b7280', va='center')
    
    # Línea vertical separadora
    ax_info.axvline(x=0.50, ymin=0.10, ymax=0.85, color='#e5e7eb', lw=1)
    
    # Título general
    fig.suptitle('Clasificación de Cuadriláteros', fontsize=14, fontweight='bold')
    
    return fig


def draw_mini_shape(ax, center, shape_type, size, colors):
        cx, cy = center
    s = size
    
    if shape_type == 'square':
        verts = [(cx-s, cy-s), (cx+s, cy-s), (cx+s, cy+s), (cx-s, cy+s)]
    elif shape_type == 'rectangle':
        verts = [(cx-s*1.3, cy-s*0.7), (cx+s*1.3, cy-s*0.7), 
                (cx+s*1.3, cy+s*0.7), (cx-s*1.3, cy+s*0.7)]
    elif shape_type == 'rhombus':
        verts = [(cx, cy-s), (cx+s*0.8, cy), (cx, cy+s), (cx-s*0.8, cy)]
    elif shape_type == 'trapezoid':
        verts = [(cx-s, cy-s*0.6), (cx+s, cy-s*0.6),
                (cx+s*0.6, cy+s*0.6), (cx-s*0.6, cy+s*0.6)]
    else:  # trapezium
        verts = [(cx-s, cy-s*0.6), (cx+s*0.8, cy-s*0.4),
                (cx+s*0.4, cy+s*0.5), (cx-s*0.6, cy+s*0.3)]
    
    polygon = patches.Polygon(
        verts,
        closed=True,
        facecolor=colors['primary'],
        edgecolor=colors['text'],
        alpha=0.3,
        linewidth=1
    )
    ax.add_patch(polygon)

if __name__ == "__main__":
    fig = generate()
    if fig is not None:
        output_dir = Path(__file__).resolve().parents[4] / "src" / "04_espacio_forma"
        output_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_dir / "cuadrilateros_clasificacion.svg", format='svg', bbox_inches='tight')
        plt.close(fig)
        print(f"Grafico generado en {output_dir / 'cuadrilateros_clasificacion.svg'}")
