import json
import os
import re


def parse_markdown_section(filepath):
    if not os.path.exists(filepath):
        return None

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title
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
                # Clean links [keyword](url) -> keyword
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
    formulas = []
    # Pattern to catch <a id="..."></a> optionally before $$
    formula_pattern = r'(?:<a\s+id="([^"]+)"></a>\s*)?\$\$\s*\n(.*?)\n\$\$'
    matches = re.findall(formula_pattern, content, re.DOTALL)

    for anchor_id, eq_body in matches:
        eq_clean = eq_body.strip()
        tag_match = re.search(r'\\tag\{([^}]+)\}', eq_clean)
        tag = tag_match.group(1) if tag_match else None

        formulas.append({
            "id": anchor_id if anchor_id else None,
            "tag": tag,
            "latex": eq_clean
        })

    # Extract tables (Markdown tables)
    tables = []
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
            tables.append({
                "encabezados": headers,
                "filas": rows
            })

    # Extract Cross References
    cross_refs = []
    ref_pattern = r'\[([^\]]+)\]\(\.\/([^\s\)]+)(?:\s+"([^"]+)")?\)'
    for text_ref, link_target, title_ref in re.findall(ref_pattern, content):
        cross_refs.append({
            "texto": text_ref,
            "archivo_destino": link_target,
            "titulo_referencia": title_ref if title_ref else ""
        })

    # Extract Clean Prose (strip note blocks, display formulas, tables, title)
    clean_text = content
    clean_text = re.sub(r':::\s*\{note\}\s*\n.*?\n:::', '', clean_text, flags=re.DOTALL)
    clean_text = re.sub(r'(?:<a\s+id="[^"]+"></a>\s*)?\$\$\s*\n.*?\n\$\$', '', clean_text, flags=re.DOTALL)
    clean_text = re.sub(r'\|[^\n]+\|\n\|[-:\s|]+\|\n(?:\|[^\n]+\|\n?)+', '', clean_text)
    clean_text = re.sub(r'^#+\s*.*$', '', clean_text, flags=re.MULTILINE)
    
    # Clean up empty lines
    prose_lines = [line.strip() for line in clean_text.splitlines() if line.strip()]
    prose = "\n".join(prose_lines)

    return {
        "titulo_seccion": title,
        "prosa_teorica": prose,
        "formulas_clave": formulas,
        "total_formulas": len(formulas),
        "tablas": tables,
        "referencias_cruzadas": cross_refs,
        "metadatos": {
            "defines": list(set(defines)),
            "palabras_clave": list(set(keywords)),
            "notas_referencias": notes,
            "referenciado_por": referenced_by,
            "simbolos": symbols,
            "abramowitz_stegun": as_refs
        }
    }

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    res = parse_markdown_section("docs/DLMF-markdown-main/markdown/1/1.2.md")
    print(json.dumps(res, indent=2, ensure_ascii=False)[:1500])

