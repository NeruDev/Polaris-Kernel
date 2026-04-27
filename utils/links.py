# yaml_frontmatter:
#   id: 'links'
#   title: 'Auditoria de enlaces internos rotos'
#   tags: ['utils', 'validation', 'links']

import os
import re
from pathlib import Path

HREF_PATTERN = re.compile(r'href="([^"]+)"')

def detect_broken_internal_links(generated_pages: list[str]) -> list[tuple[str, str]]:
    """Detecta enlaces que apuntan a archivos inexistentes en el sitio generado."""
    broken_links = []

    for html_path in generated_pages:
        path_obj = Path(html_path)
        if not path_obj.exists(): continue
        
        content = path_obj.read_text(encoding='utf-8')
        links = HREF_PATTERN.findall(content)

        for link in links:
            # Ignorar enlaces externos o anclas locales
            if any(link.startswith(s) for s in ["http", "mailto:", "#"]):
                continue

            # Limpiar anclas del link
            target = link.split("#", 1)[0]
            if not target or any(target.endswith(ext) for ext in [".css", ".js"]):
                continue

            # Verificar existencia fisica
            target_path = (path_obj.parent / target).resolve()
            if not target_path.exists():
                broken_links.append((html_path, link))

    return broken_links
