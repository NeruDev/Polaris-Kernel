# yaml_frontmatter:
#   id: 'pathing'
#   title: 'Utilidades de gestion de rutas y profundidad'
#   tags: ['utils', 'pathing']

import os
from pathlib import Path


def get_relative_html_path(md_path: Path, base_dir: Path) -> str:
    """Convierte una ruta MD en una ruta HTML relativa al directorio base."""
    rel_path = os.path.relpath(str(md_path), str(base_dir))
    return rel_path.replace(".md", ".html")


def compute_depth(rel_path: str) -> int:
    """Calcula la profundidad de directorios en una ruta relativa."""
    parts = Path(rel_path).parts
    return max(len(parts) - 1, 0)


def build_relative_prefix(depth: int) -> str:
    """Genera el prefijo de retroceso (../../) segun la profundidad."""
    return "../" * max(int(depth), 0)
