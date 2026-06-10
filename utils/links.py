# yaml_frontmatter:
#   id: 'links'
#   title: 'Auditoria de enlaces internos y recursos rotos para Quarto'
#   tags: ['utils', 'validation', 'links']

import re
from pathlib import Path

HREF_PATTERN = re.compile(r'href="([^"]+)"')
SRC_PATTERN = re.compile(r'src="([^"]+)"')


def detect_broken_internal_links(site_dir: Path) -> list[tuple[str, str]]:
    """
    Escanea recursivamente el directorio compilado (site/) buscando enlaces e imágenes rotas.
    Retorna una lista de tuplas (archivo_origen, enlace_roto).
    """
    broken_links = []

    if not site_dir.exists():
        return broken_links

    # Encontrar todos los HTML
    html_files = list(site_dir.rglob("*.html"))

    for html_path in html_files:
        try:
            content = html_path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        # Encontrar hrefs y srcs
        links = HREF_PATTERN.findall(content) + SRC_PATTERN.findall(content)

        for link in links:
            # Ignorar enlaces externos, mails, llamadas javascript, anclas locales puras o vacíos
            if not link or any(link.startswith(s) for s in ["http://", "https://", "mailto:", "javascript:", "#"]):
                continue

            # Limpiar anclas y parámetros de consulta del link
            target = link.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue

            # Construir ruta absoluta y resolver
            target_path = (html_path.parent / target).resolve()

            # Verificar existencia física
            if not target_path.exists():
                broken_links.append((str(html_path.relative_to(site_dir)), link))

    return broken_links
