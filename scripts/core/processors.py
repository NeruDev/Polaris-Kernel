# yaml_frontmatter:
#   id: 'processors'
#   title: 'Procesadores de contenido e inyección de activos'
#   tags: ['core', 'content', 'assets']

from typing import Tuple


def inject_image_markdown(
    raw_content: str, image_name: str, section_id: str, description: str = "Gráfico descriptivo"
) -> Tuple[str, bool]:
    """
    Inserta el markdown de una imagen en una sección específica.
    Retorna (nuevo_contenido, si_fue_insertado).
    """
    image_md = f"![{description}]({image_name})"

    # Evitar duplicados
    if image_md in raw_content:
        return raw_content, False

    lines = raw_content.splitlines()
    new_lines = []
    inserted = False

    for line in lines:
        new_lines.append(line)
        # Buscar el encabezado de sección (ej. ## 2.1 Concepto)
        if not inserted and line.startswith("##") and section_id in line:
            new_lines.append(f"\n{image_md}\n")
            inserted = True

    # Si no se encontró la sección, se añade al final
    if not inserted:
        new_lines.append(f"\n{image_md}\n")
        inserted = True

    return "\n".join(new_lines), inserted
