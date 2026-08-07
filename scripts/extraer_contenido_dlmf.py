import os
import json
import re
import sys

# Ensure UTF-8 output on Windows terminal
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(BASE_DIR, "docs", "DLMF-markdown-main", "markdown")
METADATA_DIR = os.path.join(BASE_DIR, "metadata", "DLMF_data")
INDEX_PATH = os.path.join(METADATA_DIR, "DLMF_indice_completo.json")

def parse_markdown_file(filepath):
    """Extract structured data with expected data types from a section markdown file."""
    if not os.path.exists(filepath):
        return None

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract header title
    title_match = re.search(r'^#\s*(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ""

    # Extract Infoboxes (:::{note} ... :::)
    note_blocks = re.findall(r':::\s*\{note\}\s*\n(.*?)\n:::', content, re.DOTALL)
    
    defines = []
    keywords = []
    notes = []
    referenced_by = []
    symbols = []
    as_refs = []

    for block in note_blocks:
        lines = block.splitlines()
        current_field = None
        current_text = []

        def flush_field(field, text_lines):
            val = " ".join(text_lines).strip()
            if not val:
                return
            if field == "Defines":
                defines.append(val)
            elif field == "Keywords":
                clean_kw = [re.sub(r'\[(.*?)\]\(.*?\)', r'\1', k.strip()) for k in val.split(',')]
                keywords.extend([k for k in clean_kw if k])
            elif field == "Notes":
                notes.append(val)
            elif field == "Referenced by":
                referenced_by.append(val)
            elif field == "Symbols":
                symbols.append(val)
            elif field == "A&S Ref":
                as_refs.append(val)

        for line in lines:
            m_field = re.match(r'^\*\*(Defines|Keywords|Notes|Referenced by|Symbols|A&S Ref|See also|Addition|Clarification|Errata|Erratum):\*\*', line.strip())
            if m_field:
                if current_field:
                    flush_field(current_field, current_text)
                current_field = m_field.group(1)
                current_text = []
            else:
                if current_field:
                    current_text.append(line.strip())
        if current_field:
            flush_field(current_field, current_text)

    # Extract display formulas ($$ ... $$)
    formulas_clave = []
    ecuaciones_latex = []
    formula_pattern = r'(?:<a\s+id="([^"]+)"></a>\s*)?\$\$\s*\n(.*?)\n\$\$'
    matches = re.findall(formula_pattern, content, re.DOTALL)

    for anchor_id, eq_body in matches:
        eq_clean = eq_body.strip()
        tag_match = re.search(r'\\tag\{([^}]+)\}', eq_clean)
        tag = tag_match.group(1) if tag_match else None

        formulas_clave.append({
            "id": anchor_id if anchor_id else "",
            "tag": tag if tag else "",
            "latex": eq_clean
        })
        ecuaciones_latex.append(eq_clean)

    # Extract Markdown tables
    tablas = []
    table_pattern = r'(\|[^\n]+\|\n\|[-:\s|]+\|\n(?:\|[^\n]+\|\n?)+)'
    raw_tables = re.findall(table_pattern, content)
    for raw_t in raw_tables:
        t_lines = [l.strip() for l in raw_t.strip().splitlines() if l.strip()]
        if len(t_lines) >= 3:
            headers = [h.strip() for h in t_lines[0].split('|')[1:-1]]
            rows = []
            for r in t_lines[2:]:
                cols = [c.strip() for c in r.split('|')[1:-1]]
                if len(cols) == len(headers):
                    rows.append(dict(zip(headers, cols)))
            tablas.append({
                "encabezados": headers,
                "filas": rows
            })

    # Extract Cross References
    referencias_cruzadas = []
    ref_pattern = r'\[([^\]]+)\]\(\.\/([^\s\)]+)(?:\s+"([^"]+)")?\)'
    for text_ref, link_target, title_ref in re.findall(ref_pattern, content):
        referencias_cruzadas.append({
            "texto": text_ref,
            "archivo_destino": link_target,
            "titulo_referencia": title_ref if title_ref else ""
        })

    # Clean prose extraction
    clean_text = content
    clean_text = re.sub(r':::\s*\{note\}\s*\n.*?\n:::', '', clean_text, flags=re.DOTALL)
    clean_text = re.sub(r'(?:<a\s+id="[^"]+"></a>\s*)?\$\$\s*\n.*?\n\$\$', '', clean_text, flags=re.DOTALL)
    clean_text = re.sub(r'\|[^\n]+\|\n\|[-:\s|]+\|\n(?:\|[^\n]+\|\n?)+', '', clean_text)
    clean_text = re.sub(r'^#+\s*.*$', '', clean_text, flags=re.MULTILINE)
    
    prose_lines = [line.strip() for line in clean_text.splitlines() if line.strip()]
    prosa_teorica = "\n".join(prose_lines)

    return {
        "titulo_seccion_md": title,
        "prosa_teorica": prosa_teorica,
        "formulas_clave": formulas_clave,
        "ecuaciones_latex": ecuaciones_latex,
        "tablas": tablas,
        "referencias_cruzadas": referencias_cruzadas,
        "metadatos": {
            "defines": list(dict.fromkeys(defines)),
            "palabras_clave": list(dict.fromkeys(keywords)),
            "notas_referencias": notes,
            "referenciado_por": referenced_by,
            "simbolos": symbols,
            "abramowitz_stegun": as_refs
        },
        "estado": "completado"
    }

def parse_chapter_main(filepath):
    """Extract chapter overview metadata from <num>/<num>.md."""
    if not os.path.exists(filepath):
        return {"resumen": "", "agradecimientos": "", "referencias": []}

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    ack_match = re.search(r'\*\*Acknowledgements:\*\*\s*\n\n(.*?)(?=\n\n\*\*|\n:::|$)', content, re.DOTALL)
    ref_match = re.search(r'\*\*Referenced by:\*\*\s*\n\n(.*?)(?=\n:::|$)', content, re.DOTALL)

    ack = ack_match.group(1).strip() if ack_match else ""
    refs_text = ref_match.group(1).strip() if ref_match else ""
    refs = [r.strip() for r in refs_text.split(',') if r.strip()]

    return {
        "agradecimientos": ack,
        "referencias_capitulo": refs
    }

def main():
    print("Iniciando proceso de extracción de contenido DLMF...")
    
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        index_data = json.load(f)

    total_capitulos = len(index_data["capitulos"])
    total_secciones_procesadas = 0
    total_formulas_extraidas = 0

    print(f"Total de capítulos a procesar: {total_capitulos}")

    for idx, cap in enumerate(index_data["capitulos"], 1):
        num = cap["capitulo"]
        json_file_rel = cap["archivo_metadata"]
        json_path = os.path.join(BASE_DIR, json_file_rel)

        print(f"\n[{idx}/{total_capitulos}] Procesando Sección {num}: {cap['titulo']}...")

        if not os.path.exists(json_path):
            print(f"  [ERROR] No existe el archivo JSON: {json_path}")
            continue

        with open(json_path, 'r', encoding='utf-8') as f:
            sec_json = json.load(f)

        # Chapter main overview info
        main_md_path = os.path.join(BASE_DIR, f"docs/DLMF-markdown-main/markdown/{num}/{num}.md")
        chap_meta = parse_chapter_main(main_md_path)
        sec_json["agradecimientos_capitulo"] = chap_meta["agradecimientos"]
        sec_json["referencias_capitulo"] = chap_meta["referencias_capitulo"]

        cap_formulas = 0
        cap_secciones = 0

        for cat in sec_json["categorias"]:
            for sec in cat["secciones"]:
                sec_id = sec["seccion_id"]
                rel_doc_path = sec["rutas"]["docs_original"]
                full_doc_path = os.path.join(BASE_DIR, rel_doc_path)

                parsed_content = parse_markdown_file(full_doc_path)
                if parsed_content:
                    sec["contenido"] = parsed_content
                    # Remove placeholder if present
                    if "placeholder_contenido" in sec:
                        del sec["placeholder_contenido"]

                    num_eqs = len(parsed_content["formulas_clave"])
                    cap_formulas += num_eqs
                    cap_secciones += 1
                else:
                    sec["contenido"] = {
                        "prosa_teorica": "",
                        "formulas_clave": [],
                        "ecuaciones_latex": [],
                        "tablas": [],
                        "referencias_cruzadas": [],
                        "metadatos": {},
                        "estado": "error_lectura"
                    }

        sec_json["estado_extraccion"] = "completado"
        sec_json["total_formulas_extraidas"] = cap_formulas

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(sec_json, f, ensure_ascii=False, indent=2)

        total_secciones_procesadas += cap_secciones
        total_formulas_extraidas += cap_formulas

        print(f"  └─ Completadas {cap_secciones} subsecciones, {cap_formulas} fórmulas extraídas.")

    print("\n" + "="*60)
    print("¡EXTRACCIÓN FINALIZADA CON ÉXITO!")
    print(f"Capítulos procesados: {total_capitulos}")
    print(f"Subsecciones extraídas: {total_secciones_procesadas}")
    print(f"Fórmulas matemáticas extraídas: {total_formulas_extraidas}")
    print("="*60)

if __name__ == "__main__":
    main()
