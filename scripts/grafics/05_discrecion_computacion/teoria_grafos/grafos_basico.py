# yaml_frontmatter:
#   id: 'grafos_basico'
#   title: 'Estructura basica de un grafo no dirigido'
#   pilar: '05_discrecion_computacion'
#   tags: ['grafico', 'computacion', 'grafos']

import sys
from pathlib import Path

import matplotlib.pyplot as plt

# Configurar path para imports del proyecto
PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.templates import get_colors, setup_style


def generate():
    setup_style()
    colors = get_colors()
    fig, ax = plt.subplots(figsize=(6, 6))

    # Nodos
    nodes = {"A": (0, 1), "B": (1, 2), "C": (2, 1), "D": (1, 0), "E": (1, 1)}
    edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("A", "E"), ("C", "E")]

    for start, end in edges:
        ax.plot(
            [nodes[start][0], nodes[end][0]],
            [nodes[start][1], nodes[end][1]],
            color=colors["text"],
            alpha=0.5,
            zorder=1,
        )

    for label, pos in nodes.items():
        ax.scatter(pos[0], pos[1], s=500, color=colors["accent"], zorder=2)
        ax.text(pos[0], pos[1], label, ha="center", va="center", fontweight="bold")

    ax.set_title("Teoria de Grafos: Vertices y Aristas")
    ax.axis("off")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "05_discrecion_computacion"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "grafos_basico.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'grafos_basico.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
