# yaml_frontmatter:
#   id: 'analisis_complejo_contorno'
#   title: 'Integral de contorno y residuos en el plano complejo'
#   pilar: '03_analisis_continuidad'
#   tags: ['grafico', 'analisis', 'complejo']

import sys
from pathlib import Path

import matplotlib.patches as patches
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

    # Ejes complejo
    ax.axhline(0, color=colors["text"], lw=1, alpha=0.5)
    ax.axvline(0, color=colors["text"], lw=1, alpha=0.5)

    # Contorno circular
    circle = patches.Circle((0, 0), 1, fill=False, color=colors["primary"], lw=2, label="Contorno C")
    ax.add_patch(circle)

    # Flechas de direccion (antihorario)
    ax.annotate(
        "",
        xy=(-1, 0.1),
        xytext=(-1, -0.1),
        arrowprops=dict(arrowstyle="->", color=colors["primary"], lw=2),
    )

    # Polos (Singularidades)
    ax.scatter([0.3], [0.4], color=colors["danger"], marker="x", s=100, label="Polo $z_0$")
    ax.text(0.35, 0.45, r"$z_0$", color=colors["danger"], fontsize=12)

    ax.set_title("Analisis Complejo: Integral de Contorno")
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.legend()

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "03_analisis_continuidad"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "analisis_complejo_contorno.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'analisis_complejo_contorno.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
