# yaml_frontmatter:
#   id: 'markdown'
#   title: 'Procesador de Markdown y validaciones semanticas para Quarto'
#   tags: ['utils', 'markdown', 'validation']

import re
from typing import List, Tuple

import markdown

# Configuración heredada para renderizado secundario/local
DEFAULT_EXTENSIONS = [
    "tables",
    "fenced_code",
    "toc",
    "admonition",
    "codehilite",
    "pymdownx.arithmatex",
    "pymdownx.superfences",
]

EXTENSION_CONFIGS = {
    "pymdownx.arithmatex": {
        "generic": True,
    },
}


def convert_md_to_html(md_text: str, asset_prefix: str = "") -> Tuple[str, int]:
    """
    [Heredado/Legacy] Convierte Markdown a HTML con soporte matemático básico.
    Nota: En el flujo principal, Quarto se encarga del renderizado HTML/PDF final.
    """
    html = markdown.markdown(
        md_text,
        extensions=DEFAULT_EXTENSIONS,
        extension_configs=EXTENSION_CONFIGS,
    )

    # Corregir enlaces a archivos .md para que apunten a .html
    html = re.sub(r'href="([^"]+)\.md(#[^"]*)?"', r'href="\1.html\2"', html)
    replacements = len(re.findall(r'href="[^"]+\.html(?:#[^"]*)?"', html))
    return html, replacements


def check_semantic_line_breaks(text: str) -> List[str]:
    """
    Verifica que el texto Markdown siga la convención de salto de línea semántico (Semantic Line Breaks).
    Retorna una lista de mensajes detallados con posibles infracciones.
    """
    warnings = []

    # Excluir YAML frontmatter si existe
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2]

    lines = text.splitlines()
    in_block_math = False
    in_code_block = False

    # Patrón para detectar un punto seguido:
    # Un punto seguido de espacio(s) y una letra mayúscula o número que inicia otra frase en la misma línea.
    punto_seguido_re = re.compile(r"\b[^.\n]+\.\s+[A-ZÁÉÍÓÚÑ]")

    for i, line in enumerate(lines, 1):
        stripped = line.strip()

        # Rastrear bloques de matemáticas exentos
        if stripped.startswith("$$"):
            in_block_math = not in_block_math
            continue
        if in_block_math:
            continue

        # Rastrear bloques de código exentos
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        # Omitir líneas vacías, encabezados, imágenes o tablas
        if not stripped or stripped.startswith("#") or stripped.startswith("!") or stripped.startswith("|"):
            continue

        # Validar punto y seguido en la misma línea de prosa
        if punto_seguido_re.search(line):
            warnings.append(
                f"Línea {i}: Se detectó punto y seguido en la misma línea. Usa saltos de línea semánticos."
            )

    return warnings
