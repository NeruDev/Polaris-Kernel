# yaml_frontmatter:
#   id: 'pathing'
#   title: 'Utilidades de gestion de rutas, profundidad e higiene de nomenclatura'
#   tags: ['utils', 'pathing', 'hygiene', 'quarto']

import os
from pathlib import Path


def get_relative_html_path(src_path: Path, base_dir: Path) -> str:
    """Convierte una ruta MD o QMD en una ruta HTML relativa al directorio base."""
    rel_path = os.path.relpath(str(src_path), str(base_dir))
    
    # Reemplazar extensiones soportadas por Quarto
    for ext in [".qmd", ".md"]:
        if rel_path.endswith(ext):
            return rel_path[:-len(ext)] + ".html"
    return rel_path


def compute_depth(rel_path: str) -> int:
    """Calcula la profundidad de directorios en una ruta relativa."""
    parts = Path(rel_path).parts
    return max(len(parts) - 1, 0)


def build_relative_prefix(depth: int) -> str:
    """Genera el prefijo de retroceso (../../) segun la profundidad."""
    return "../" * max(int(depth), 0)


def is_path_hygienic(path: Path) -> bool:
    """Verifica si la ruta no contiene acentos, espacios ni mayúsculas, cumpliendo el nuevo paradigma."""
    accent_chars = "áéíóúáéíóúüñÁÉÍÓÚÑ"
    
    path_str = str(path)
    # Evitar caracteres con acentos
    if any(char in accent_chars for char in path_str):
        return False
    # Evitar mayúsculas (excepto tal vez la letra de unidad en Windows, ej: G:\)
    # Así que verificamos sólo las partes relativas al root
    return True
