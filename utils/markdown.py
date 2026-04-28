# yaml_frontmatter:
#   id: 'markdown'
#   title: 'Procesador avanzado de Markdown a HTML'
#   tags: ['utils', 'markdown', 'render']

import re

import markdown

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


def convert_md_to_html(md_text: str, asset_prefix: str = "") -> tuple[str, int]:
    """
    Convierte Markdown a HTML con soporte matematico y correccion de enlaces.
    """
    html = markdown.markdown(
        md_text,
        extensions=DEFAULT_EXTENSIONS,
        extension_configs=EXTENSION_CONFIGS,
    )

    # 1. Corregir enlaces a archivos .md para que apunten a .html
    html = re.sub(r'href="([^"]+)\.md(#[^"]*)?"', r'href="\1.html\2"', html)

    # 2. En nuestro repo actual, los SVG estan en el mismo directorio.
    # No hace falta un mapeo complejo de assets/ si estan locales,
    # pero mantenemos asset_prefix por si se usa en sub-vistas.

    replacements = len(re.findall(r'href="[^"]+\.html(?:#[^"]*)?"', html))
    return html, replacements
