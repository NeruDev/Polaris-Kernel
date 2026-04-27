# yaml_frontmatter:
#   id: 'templates'
#   title: 'Estilos visuales unificados para gráficos Matplotlib'
#   tags: ['graphics', 'style']

import matplotlib.pyplot as plt


def get_colors():
    """Retorna la paleta de colores oficial del proyecto."""
    return {
        "primary": "#3498db",  # Azul (Funciones)
        "secondary": "#2ecc71",  # Verde (Áreas)
        "accent": "#f1c40f",  # Amarillo (Puntos de interés)
        "danger": "#e74c3c",  # Rojo (Asíntotas/Límites)
        "purple": "#9b59b6",  # Morado (Vectores)
        "text": "#2c3e50",  # Azul oscuro (Texto/Ejes)
    }


def setup_style():
    """Configura los parámetros globales de Matplotlib."""
    colors = get_colors()

    # Intentar usar un estilo limpio si está disponible
    try:
        plt.style.use("seaborn-v0_8-muted")
    except:
        plt.style.use("ggplot")

    plt.rcParams.update(
        {
            "axes.prop_cycle": plt.cycler(
                color=[
                    colors["primary"],
                    colors["secondary"],
                    colors["accent"],
                    colors["danger"],
                    colors["purple"],
                ]
            ),
            "figure.facecolor": "white",
            "axes.edgecolor": colors["text"],
            "axes.labelcolor": colors["text"],
            "xtick.color": colors["text"],
            "ytick.color": colors["text"],
            "text.color": colors["text"],
            "font.family": "sans-serif",
            "svg.fonttype": "none",  # Crucial para edición posterior del SVG
        }
    )
