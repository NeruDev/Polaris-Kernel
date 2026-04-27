# yaml_frontmatter:
#   id: 'operaciones_matrices'
#   title: 'Visualizacion de operaciones con matrices'
#   pilar: '02_estructuras_algebraicas'
#   tags: ['grafico', 'algebra', 'matrices']

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
    fig, ax = plt.subplots(figsize=(8, 4))

    # Representacion simbolica de Multiplicacion (Renglon x Columna)
    ax.add_patch(plt.Rectangle((0.1, 0.4), 0.3, 0.4, fill=True, color=colors["primary"], alpha=0.2))
    ax.add_patch(
        plt.Rectangle((0.5, 0.4), 0.3, 0.4, fill=True, color=colors["secondary"], alpha=0.2)
    )

    # Resaltar fila y columna
    ax.add_patch(plt.Rectangle((0.1, 0.65), 0.3, 0.05, color=colors["danger"], label="Fila i"))
    ax.add_patch(plt.Rectangle((0.6, 0.4), 0.05, 0.4, color=colors["accent"], label="Columna j"))

    ax.text(0.42, 0.6, r"$\times$", fontsize=30, ha="center")
    ax.text(0.85, 0.6, r"=", fontsize=30, ha="center")
    ax.text(0.92, 0.6, r"$c_{ij}$", fontsize=20, ha="center", color=colors["danger"])

    ax.set_title(r"Multiplicacion de Matrices: Fila $\times$ Columna")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.legend(loc="lower center", ncol=2)

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "02_estructuras_algebraicas"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "operaciones_matrices.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'operaciones_matrices.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
