import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(BASE_DIR, "docs", "DLMF-markdown-main", "markdown")
METADATA_DIR = os.path.join(BASE_DIR, "metadata", "DLMF_data")
INDEX_PATH = os.path.join(METADATA_DIR, "DLMF_indice_completo.json")
AUDIT_REPORT_PATH = os.path.join(METADATA_DIR, "AUDITORIA_METADATOS.json")

def extract_clean_keywords(raw_text):
    """Extract clean keywords as plain word concepts without stray brackets or URL noise."""
    if not raw_text:
        return []
    
    # Extract markdown link anchor texts: [term](url)
    link_keywords = re.findall(r'\[([^\]]+)\]\(.*?\)', raw_text)
    if link_keywords:
        kw_candidates = link_keywords
    else:
        kw_candidates = re.split(r'[,;]', raw_text)

    clean_keywords = []
    for kw in kw_candidates:
        # Remove any leading/trailing brackets, quotes, punctuation
        k = kw.strip().strip('[]"\'` \t\n\r')
        # Clean any remaining internal markdown links if nested
        k = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', k).strip()
        if k and k not in clean_keywords:
            clean_keywords.append(k)

    return clean_keywords

def clean_latex_expression(latex_str):
    """Sanitize LaTeX math expressions to ensure KaTeX/MathJax & LLM agent compatibility."""
    if not latex_str:
        return ""
    
    s = latex_str
    # Replace HTML entity &amp; with LaTeX matrix column separator &
    s = s.replace('&amp;', '&')
    # Replace non-standard macros if any remain
    s = s.replace('\\ifrac', '\\frac')
    s = s.replace('\\cfracstyle', '')
    s = s.replace('\\NVar', '')
    
    return s.strip()

def check_latex_integrity(latex_str):
    """Audit LaTeX formula for structural validity."""
    issues = []
    if '&amp;' in latex_str:
        issues.append("Entidad HTML &amp; no sanitizada")
    if r'\ifrac' in latex_str or r'\cfracstyle' in latex_str or r'\NVar' in latex_str:
        issues.append("Macro no estándar presente")
    
    # Check brace balance (ignoring escaped \{ and \})
    sanitized = re.sub(r'\\\{|\\\}', '', latex_str)
    open_curly = sanitized.count('{')
    close_curly = sanitized.count('}')
    if open_curly != close_curly:
        issues.append(f"Desbalance de llaves ({open_curly} abren vs {close_curly} cierran)")

    return issues

def parse_markdown_section_refined(filepath):
    """Parse section markdown with strict metadata typing and clean LaTeX math."""
    if not os.path.exists(filepath):
        return None

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Section Title
    title_match = re.search(r'^#\s*(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ""

    # Infobox Parsing (:::{note} ... :::)
    note_blocks = re.findall(r':::\s*\{note\}\s*\n(.*?)\n:::', content, re.DOTALL)
    
    raw_keywords = []
    defines = []
    notes = []
    referenced_by = []
    symbols = []
    as_refs = []
    ver_tambien = []
    historial_cambios = []

    for block in note_blocks:
        lines = block.splitlines()
        current_field = None
        current_text = []

        def flush_field(field, text_lines):
            val = " ".join(text_lines).strip()
            if not val:
                return
            if field == "Keywords":
                raw_keywords.append(val)
            elif field == "Defines":
                defines.append(val)
            elif field == "Notes":
                notes.append(val)
            elif field == "Referenced by":
                # Clean cross-reference text
                refs = [r.strip() for r in val.split(',') if r.strip()]
                referenced_by.extend(refs)
            elif field == "Symbols":
                symbols.append(val)
            elif field == "A&S Ref":
                as_refs.append(val)
            elif field == "See also":
                ver_tambien.append(val)
            elif any(k in field for k in ["Addition", "Clarification", "Correction", "Errata", "Modification", "Amendment"]):
                historial_cambios.append({
                    "tipo_evento": field,
                    "descripcion": val
                })

        for line in lines:
            m_field = re.match(r'^\*\*(Keywords|Defines|Notes|Referenced by|Symbols|A&S Ref|See also|Addition.*?|Clarification.*?|Correction.*?|Errata.*?|Modification.*?|Amendment.*?):\*\*', line.strip())
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

    # Process Clean Keywords
    clean_keywords = []
    for rk in raw_keywords:
        clean_keywords.extend(extract_clean_keywords(rk))
    clean_keywords = list(dict.fromkeys(clean_keywords))

    # Parse Formulas & Check LaTeX Integrity
    formulas_clave = []
    ecuaciones_latex = []
    formula_issues = []

    formula_pattern = r'(?:<a\s+id="([^"]+)"></a>\s*)?\$\$\s*\n(.*?)\n\$\$'
    matches = re.findall(formula_pattern, content, re.DOTALL)

    for anchor_id, eq_body in matches:
        eq_sanitized = clean_latex_expression(eq_body)
        tag_match = re.search(r'\\tag\{([^}]+)\}', eq_sanitized)
        tag = tag_match.group(1) if tag_match else ""

        issues = check_latex_integrity(eq_sanitized)
        if issues:
            formula_issues.append({"formula_id": anchor_id, "tag": tag, "problemas": issues})

        formulas_clave.append({
            "id": anchor_id if anchor_id else "",
            "tag": tag,
            "latex": eq_sanitized
        })
        ecuaciones_latex.append(eq_sanitized)

    # Markdown Tables
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

    # Cross References
    referencias_cruzadas = []
    ref_pattern = r'\[([^\]]+)\]\(\.\/([^\s\)]+)(?:\s+"([^"]+)")?\)'
    for text_ref, link_target, title_ref in re.findall(ref_pattern, content):
        referencias_cruzadas.append({
            "texto": text_ref,
            "archivo_destino": link_target,
            "titulo_referencia": title_ref if title_ref else ""
        })

    # Clean Prose
    clean_text = content
    clean_text = re.sub(r':::\s*\{note\}\s*\n.*?\n:::', '', clean_text, flags=re.DOTALL)
    clean_text = re.sub(r'(?:<a\s+id="[^"]+"></a>\s*)?\$\$\s*\n.*?\n\$\$', '', clean_text, flags=re.DOTALL)
    clean_text = re.sub(r'\|[^\n]+\|\n\|[-:\s|]+\|\n(?:\|[^\n]+\|\n?)+', '', clean_text)
    clean_text = re.sub(r'^#+\s*.*$', '', clean_text, flags=re.MULTILINE)
    
    prose_lines = [line.strip() for line in clean_text.splitlines() if line.strip()]
    prosa_teorica = "\n".join(prose_lines)

    # Build Clean Metadatos Object - Omit empty optional fields to prevent clutter
    metadatos = {}
    if clean_keywords:
        metadatos["palabras_clave"] = clean_keywords
    if defines:
        metadatos["definiciones"] = list(dict.fromkeys(defines))
    if symbols:
        metadatos["simbolos"] = list(dict.fromkeys(symbols))
    if referenced_by:
        metadatos["referenciado_por"] = list(dict.fromkeys(referenced_by))
    if notes:
        metadatos["notas_bibliograficas"] = notes
    if as_refs:
        metadatos["referencias_abramowitz_stegun"] = list(dict.fromkeys(as_refs))
    if ver_tambien:
        metadatos["ver_tambien"] = list(dict.fromkeys(ver_tambien))
    if historial_cambios:
        metadatos["historial_cambios"] = historial_cambios

    res = {
        "titulo_seccion_md": title,
        "prosa_teorica": prosa_teorica,
        "formulas_clave": formulas_clave,
        "ecuaciones_latex": ecuaciones_latex,
        "metadatos": metadatos,
        "estado": "completado"
    }

    if tablas:
        res["tablas"] = tablas
    if referencias_cruzadas:
        res["referencias_cruzadas"] = referencias_cruzadas

    return res, formula_issues

def main():
    print("Iniciando refactorización y verificación masiva de metadatos DLMF...")

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        index_data = json.load(f)

    total_capitulos = len(index_data["capitulos"])
    total_secciones = 0
    total_formulas = 0
    total_keywords_unicos = set()
    latex_errors = []

    for idx, cap in enumerate(index_data["capitulos"], 1):
        num = cap["capitulo"]
        json_file_rel = cap["archivo_metadata"]
        json_path = os.path.join(BASE_DIR, json_file_rel)

        if not os.path.exists(json_path):
            continue

        with open(json_path, 'r', encoding='utf-8') as f:
            sec_json = json.load(f)

        for cat in sec_json["categorias"]:
            for sec in cat["secciones"]:
                sec_id = sec["seccion_id"]
                rel_doc_path = sec["rutas"]["docs_original"]
                full_doc_path = os.path.join(BASE_DIR, rel_doc_path)

                parsed_data = parse_markdown_section_refined(full_doc_path)
                if parsed_data:
                    content_obj, f_issues = parsed_data
                    sec["contenido"] = content_obj

                    total_secciones += 1
                    total_formulas += len(content_obj["formulas_clave"])
                    
                    # Accumulate clean keywords
                    if "palabras_clave" in content_obj.get("metadatos", {}):
                        for kw in content_obj["metadatos"]["palabras_clave"]:
                            total_keywords_unicos.add(kw)

                    if f_issues:
                        for fi in f_issues:
                            latex_errors.append({
                                "capitulo": num,
                                "seccion": sec_id,
                                "detalle": fi
                            })

        sec_json["estado_metadatos"] = "verificado_y_refinado"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(sec_json, f, ensure_ascii=False, indent=2)

        print(f"[{idx:2d}/{total_capitulos}] Capítulo {num:2d} ({cap['titulo']}): Procesado y limpio.")

    print("\nGenerando informe de auditoría fina...")
    reporte_audit = {
        "titulo": "Auditoría de Calidad y Refinamiento de Metadatos DLMF",
        "resumen": {
            "total_capitulos_auditados": total_capitulos,
            "total_secciones_procesadas": total_secciones,
            "total_formulas_verificadas": total_formulas,
            "total_palabras_clave_conceptuales_unicas": len(total_keywords_unicos),
            "total_errores_latex": len(latex_errors),
            "estado_general": "ÉXITO TOTAL" if not latex_errors else "ALERTAS_DETECTADAS"
        },
        "muestra_palabras_clave_limpias": sorted(list(total_keywords_unicos))[:30],
        "errores_latex_detectados": latex_errors
    }

    with open(AUDIT_REPORT_PATH, 'w', encoding='utf-8') as f:
        json.dump(reporte_audit, f, ensure_ascii=False, indent=2)

    print("\n" + "="*70)
    print("           REPORTE FINAL DE CALIDAD Y REFINAMIENTO DE METADATOS         ")
    print("="*70)
    print(f" Capítulos procesados:                 {total_capitulos}/36")
    print(f" Subsecciones verificadas:             {total_secciones}/872")
    print(f" Fórmulas LaTeX verificadas:           {total_formulas}")
    print(f" Palabras clave conceptuales limpias:   {len(total_keywords_unicos)}")
    print(f" Errores de sintaxis LaTeX:            {len(latex_errors)}")
    print("="*70)

    print("\nMuestra de palabras clave conceptuales extraídas de forma limpia:")
    for kw in sorted(list(total_keywords_unicos))[:15]:
        print(f" - {kw}")

if __name__ == "__main__":
    main()
