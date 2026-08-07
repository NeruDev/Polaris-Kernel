import os
import json
import re

# Defined paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(BASE_DIR, "docs", "DLMF-markdown-main", "markdown")
METADATA_DIR = os.path.join(BASE_DIR, "metadata", "DLMF_data")

TOC_PATH = os.path.join(DOCS_DIR, "toc.md")
TOC_FULL_PATH = os.path.join(DOCS_DIR, "toc_full.md")

os.makedirs(METADATA_DIR, exist_ok=True)

def sanitize_filename_title(title: str) -> str:
    """Clean chapter title to create safe snake_case filenames without unicode artifacts."""
    # Remove unicode invisible multiplication sign \u2062 and typographic apostrophes
    clean = title.replace('\u2062', '').replace('’', '').replace("'", "")
    # Normalize accents
    clean = clean.replace('é', 'e').replace('è', 'e').replace('á', 'a').replace('ó', 'o')
    # Replace non-alphanumeric chars with underscores
    clean = re.sub(r'[^a-zA-Z0-9]+', '_', clean).strip('_')
    return clean

def parse_toc_simple():
    """Parse simplified Table of Contents (toc.md)."""
    with open(TOC_PATH, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    capitulos = []
    for line in lines:
        m = re.match(r'^-\s*(\d+)\s*-\s*(.+)$', line)
        if m:
            num = int(m.group(1))
            title = m.group(2).strip()
            clean_title = sanitize_filename_title(title)
            json_filename = f"{num}_{clean_title}.json"

            cap_entry = {
                "capitulo": num,
                "titulo": title,
                "archivo_metadata": f"metadata/DLMF_data/{json_filename}",
                "rutas_docs": {
                    "docs_original": f"docs/DLMF-markdown-main/markdown/{num}/{num}.md",
                    "docs_directorio_original": f"docs/DLMF-markdown-main/markdown/{num}/",
                    "docs_traduccion": f"docs/DLMF_markdown_traduccion/markdown/{num}/{num}.md"
                }
            }
            capitulos.append(cap_entry)

    return {
        "titulo": "Índice Simplificado de DLMF (Digital Library of Mathematical Functions)",
        "fuente_original": "docs/DLMF-markdown-main/markdown/toc.md",
        "descripcion": "Índice general por capítulos de la Digital Library of Mathematical Functions (DLMF), con referencias cruzadas a metadata y docs.",
        "total_capitulos": len(capitulos),
        "capitulos": capitulos
    }

def parse_toc_full():
    """Parse full Table of Contents (toc_full.md)."""
    with open(TOC_FULL_PATH, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    chapters = []
    current_chapter = None
    current_category = None

    for line in lines:
        m_chap = re.match(r'^\s*-\s*(\d+)\s*-\s*(.+)$', line)
        m_cat = re.match(r'^\s*-\s*\*\*(.+)\*\*\s*$', line)
        m_sec = re.match(r'^\s*-\s*(\d+\.\d+)\s*-\s*(.+)$', line)

        if m_chap:
            num = int(m_chap.group(1))
            title = m_chap.group(2).strip()
            clean_title = sanitize_filename_title(title)
            json_filename = f"{num}_{clean_title}.json"

            current_chapter = {
                "capitulo": num,
                "titulo": title,
                "archivo_metadata": f"metadata/DLMF_data/{json_filename}",
                "rutas_docs": {
                    "docs_original": f"docs/DLMF-markdown-main/markdown/{num}/{num}.md",
                    "docs_directorio_original": f"docs/DLMF-markdown-main/markdown/{num}/",
                    "docs_traduccion": f"docs/DLMF_markdown_traduccion/markdown/{num}/{num}.md"
                },
                "categorias": []
            }
            chapters.append(current_chapter)
            current_category = None
        elif m_cat:
            if current_chapter is not None:
                cat_name = m_cat.group(1).strip()
                current_category = {
                    "categoria": cat_name,
                    "secciones": []
                }
                current_chapter["categorias"].append(current_category)
        elif m_sec:
            sec_id = m_sec.group(1).strip()
            sec_title = m_sec.group(2).strip()

            if current_chapter is not None:
                num = current_chapter["capitulo"]
                sec_item = {
                    "seccion_id": sec_id,
                    "titulo": sec_title,
                    "rutas": {
                        "docs_original": f"docs/DLMF-markdown-main/markdown/{num}/{sec_id}.md",
                        "docs_traduccion": f"docs/DLMF_markdown_traduccion/markdown/{num}/{sec_id}.md"
                    }
                }
                if current_category is None:
                    current_category = {
                        "categoria": "General",
                        "secciones": []
                    }
                    current_chapter["categorias"].append(current_category)
                current_category["secciones"].append(sec_item)

    return {
        "titulo": "Índice Completo de DLMF (Digital Library of Mathematical Functions)",
        "fuente_original": "docs/DLMF-markdown-main/markdown/toc_full.md",
        "descripcion": "Estructura jerárquica detallada por capítulos, categorías temáticas y subsecciones de la Digital Library of Mathematical Functions (DLMF).",
        "total_capitulos": len(chapters),
        "capitulos": chapters
    }

def main():
    print("Parsing toc.md...")
    indice_simplificado = parse_toc_simple()
    
    path_simplificado = os.path.join(METADATA_DIR, "DLMF_indice_simplificado.json")
    with open(path_simplificado, 'w', encoding='utf-8') as f:
        json.dump(indice_simplificado, f, ensure_ascii=False, indent=2)
    print(f"Escrito: {path_simplificado}")

    print("Parsing toc_full.md...")
    indice_completo = parse_toc_full()

    # Write both exact name with space and snake_case name for standard compliance
    path_completo_space = os.path.join(METADATA_DIR, "DLMF_indice completo.json")
    path_completo_snake = os.path.join(METADATA_DIR, "DLMF_indice_completo.json")

    with open(path_completo_space, 'w', encoding='utf-8') as f:
        json.dump(indice_completo, f, ensure_ascii=False, indent=2)
    print(f"Escrito: {path_completo_space}")

    with open(path_completo_snake, 'w', encoding='utf-8') as f:
        json.dump(indice_completo, f, ensure_ascii=False, indent=2)
    print(f"Escrito: {path_completo_snake}")

    # Generate individual section JSON files in metadata/DLMF_data/
    print("Generando archivos JSON por sección...")
    for cap in indice_completo["capitulos"]:
        num = cap["capitulo"]
        title = cap["titulo"]
        clean_title = sanitize_filename_title(title)
        json_filename = f"{num}_{clean_title}.json"
        target_path = os.path.join(METADATA_DIR, json_filename)

        # Build section file content with placeholder structures
        sec_file_data = {
            "capitulo": num,
            "titulo_original": title,
            "archivo_metadata": f"metadata/DLMF_data/{json_filename}",
            "rutas_docs": cap["rutas_docs"],
            "total_categorias": len(cap["categorias"]),
            "total_secciones": sum(len(c["secciones"]) for c in cap["categorias"]),
            "categorias": []
        }

        for cat in cap["categorias"]:
            cat_data = {
                "categoria": cat["categoria"],
                "secciones": []
            }
            for sec in cat["secciones"]:
                sec_entry = {
                    "seccion_id": sec["seccion_id"],
                    "titulo_original": sec["titulo"],
                    "rutas": sec["rutas"],
                    "placeholder_contenido": {
                        "resumen": "",
                        "prosa_teorica": "",
                        "formulas_clave": [],
                        "ecuaciones_latex": [],
                        "graficos_typst": [],
                        "referencias_cruzadas": [],
                        "metadatos": {
                            "msc_ids": [],
                            "palabras_clave": []
                        },
                        "estado": "pendiente_de_llenado"
                    }
                }
                cat_data["secciones"].append(sec_entry)
            sec_file_data["categorias"].append(cat_data)

        with open(target_path, 'w', encoding='utf-8') as f:
            json.dump(sec_file_data, f, ensure_ascii=False, indent=2)
        print(f"Generado: {json_filename}")

    print("¡Proceso completado exitosamente!")

if __name__ == "__main__":
    main()
