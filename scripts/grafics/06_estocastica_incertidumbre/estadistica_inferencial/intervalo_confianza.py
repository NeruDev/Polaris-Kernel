# yaml_frontmatter:
#   id: 'intervalo_confianza'
#   title: 'Visualizacion del margen de error y nivel de confianza'
#   pilar: '06_estocastica_incertidumbre'
#   tags: ['grafico', 'estadistica', 'inferencia']

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Configurar path para imports del proyecto
PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.templates import get_colors, setup_style


def generate():
    setup_style()
    colors = get_colors()
    fig, ax = plt.subplots(figsize=(8, 4))

    # Campana de fondo
    x = np.linspace(-3, 3, 100)
    y = np.exp(-0.5 * x**2)
    ax.plot(x, y, color=colors["text"], alpha=0.2)

    # Intervalo (95%)
    z_val = 1.96
    ax.fill_between(
        x[(x > -z_val) & (x < z_val)],
        y[(x > -z_val) & (x < z_val)],
        color=colors["primary"],
        alpha=0.3,
    )
    ax.vlines([-z_val, z_val], 0, 0.2, colors=colors["danger"], ls="--", lw=2)

    ax.text(
        0, 0.4, "Confianza 95%", ha="center", fontweight="bold", color=colors["primary"]
    )
    ax.annotate(
        "Margen de Error",
        xy=(z_val, 0.1),
        xytext=(z_val + 0.5, 0.3),
        arrowprops=dict(arrowstyle="->", color=colors["text"]),
    )

    ax.set_title("Inferencia Estadistica: Intervalo de Confianza")
    ax.axis("off")

    return fig


if __name__ == "__main__":
    try:
        setup_style()
        fig = generate()
        out_dir = PROJECT_ROOT / "src" / "06_estocastica_incertidumbre"
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / "intervalo_confianza.svg", format="svg")
        plt.close(fig)
        print(f"Grafico generado: {out_dir / 'intervalo_confianza.svg'}")
    except Exception as e:
        print(f"Fallo: {e}", file=sys.stderr)
