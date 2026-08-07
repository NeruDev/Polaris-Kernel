#!/usr/bin/env python3
"""
Script de sanitización para los archivos Markdown de DLMF (docs/DLMF-markdown-main).
Convierte macros LaTeX no estándares y entidades HTML escapadas al estándar reconocido por KaTeX / MathJax / Quarto.
"""

import os
import re
import sys
from pathlib import Path

# Directorio objetivo por defecto
DEFAULT_DLMF_DIR = Path(__file__).resolve().parent.parent / "docs" / "DLMF-markdown-main"


def unwrap_macro(text: str, macro_name: str, replacement_mode: str = "arg1") -> str:
    """
    Desenvuelve o reemplaza una macro LaTeX estilo \\macro{arg1}{arg2}... o \\macro{arg1}.
    replacement_mode:
      - 'arg1': reemplaza \\macro{X} por X
      - 'frac': reemplaza \\ifrac{A}{B} por \\frac{A}{B}
    """
    pattern = r'\\' + macro_name + r'\{'
    pos = 0
    while True:
        match = re.search(pattern, text[pos:])
        if not match:
            break
        
        start_idx = pos + match.start()
        # Parse braces starting from match.end()
        cursor = pos + match.end()
        
        # Helper to extract balanced group
        def extract_group(idx):
            if idx >= len(text) or text[idx] != '{':
                return None, idx
            depth = 1
            idx += 1
            group_start = idx
            while idx < len(text) and depth > 0:
                if text[idx] == '{':
                    depth += 1
                elif text[idx] == '}':
                    depth -= 1
                idx += 1
            if depth == 0:
                return text[group_start:idx-1], idx
            return None, idx

        if replacement_mode == "arg1":
            # Extraer 1 grupo de llaves
            arg1, next_idx = extract_group(cursor - 1)
            if arg1 is not None:
                text = text[:start_idx] + arg1 + text[next_idx:]
                pos = start_idx + len(arg1)
            else:
                pos = cursor
        elif replacement_mode == "frac":
            # Extraer 2 grupos de llaves consecutivos \\ifrac{A}{B}
            arg1, next_idx1 = extract_group(cursor - 1)
            if arg1 is not None:
                arg2, next_idx2 = extract_group(next_idx1)
                if arg2 is not None:
                    repl = f"\\frac{{{arg1}}}{{{arg2}}}"
                    text = text[:start_idx] + repl + text[next_idx2:]
                    pos = start_idx + len(repl)
                else:
                    pos = next_idx1
            else:
                pos = cursor
        else:
            pos = cursor

    return text


def sanitizar_contenido(content: str) -> tuple[str, dict]:
    """
    Aplica las reglas de sanitización sobre el contenido de un archivo Markdown.
    Devuelve (contenido_sanitizado, estadísticas_de_cambios).
    """
    stats = {
        "ifrac": 0,
        "NVar": 0,
        "cfracstyle": 0,
        "asterisco_multiplicacion": 0,
        "mskip": 0,
        "pvint": 0,
        "html_amp": 0,
        "html_lt_gt": 0
    }

    # 1. Contar y reemplazar \ifrac{A}{B} -> \frac{A}{B}
    ifrac_matches = len(re.findall(r'\\ifrac\{', content))
    if ifrac_matches > 0:
        stats["ifrac"] = ifrac_matches
        content = unwrap_macro(content, "ifrac", replacement_mode="frac")

    # 2. Contar y reemplazar \NVar{X} -> X
    nvar_matches = len(re.findall(r'\\NVar\{', content))
    if nvar_matches > 0:
        stats["NVar"] = nvar_matches
        content = unwrap_macro(content, "NVar", replacement_mode="arg1")

    # 3. Contar y reemplazar \cfracstyle{...} -> \displaystyle
    cfrac_matches = len(re.findall(r'\\cfracstyle\{[^{}]*\}', content))
    if cfrac_matches > 0:
        stats["cfracstyle"] = cfrac_matches
        content = re.sub(r'\\cfracstyle\{[^{}]*\}', r'\\displaystyle ', content)

    # 4. Reemplazar \* (multiplicación semántica/invisible en DLMF) por \, o espacio fino
    asterisk_matches = len(re.findall(r'\\\*', content))
    if asterisk_matches > 0:
        stats["asterisco_multiplicacion"] = asterisk_matches
        content = re.sub(r'\\\*', r'\\,', content)

    # 5. Reemplazar \mskip -> \mspace (ej. \mskip-3.0mu -> \mspace{-3mu})
    mskip_matches = len(re.findall(r'\\mskip', content))
    if mskip_matches > 0:
        stats["mskip"] = mskip_matches
        content = re.sub(r'\\mskip\s*(-?\d+(?:\.\d+)?)mu', r'\\mspace{\1mu}', content)
        content = re.sub(r'\\mskip', r'\\mspace', content)

    # 6. Reemplazar \pvint -> \fint
    pvint_matches = len(re.findall(r'\\pvint', content))
    if pvint_matches > 0:
        stats["pvint"] = pvint_matches
        content = re.sub(r'\\pvint', r'\\fint', content)

    # 8. Limpiar \text{$...$} y \mbox{...$...$} dentro de math blocks para evitar delimitadores $ anidados
    def clean_text_mbox(match):
        inner = match.group(1)
        # Quitar $ dentro del texto
        inner_clean = inner.replace('$', '')
        return f'\\text{{{inner_clean}}}'

    content = re.sub(r'\\(?:text|mbox)\{([^}]*\$[^}]*)\}', clean_text_mbox, content)

    # 9. Limpiar entidades HTML dentro de expresiones y matrices LaTeX (ej. &amp; -> &)
    def replace_html_entities_in_math(match):
        block = match.group(0)
        block = block.replace('&amp;', '&')
        block = block.replace('&lt;', '<')
        block = block.replace('&gt;', '>')
        return block

    # Bloques de ecuaciones inline $...$ y bloques $$...$$
    math_pattern = re.compile(r'(\$\$.*?\$\$|\$.*?\$)', re.DOTALL)

    new_content = []
    last_end = 0
    for match in math_pattern.finditer(content):
        # Texto fuera de math
        new_content.append(content[last_end:match.start()])
        # Math block
        math_block = match.group(0)
        
        # Contar sustituciones HTML en math
        stats["html_amp"] += math_block.count('&amp;')
        stats["html_lt_gt"] += math_block.count('&lt;') + math_block.count('&gt;')
        
        math_block_clean = math_block.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
        new_content.append(math_block_clean)
        last_end = match.end()

    new_content.append(content[last_end:])
    content = "".join(new_content)

    return content, stats


def sanitizar_directorio(target_dir: Path) -> dict:
    """
    Recorre iterativamente el directorio sanitizando todos los archivos .md.
    """
    total_stats = {
        "archivos_procesados": 0,
        "archivos_modificados": 0,
        "ifrac": 0,
        "NVar": 0,
        "cfracstyle": 0,
        "asterisco_multiplicacion": 0,
        "mskip": 0,
        "pvint": 0,
        "html_amp": 0,
        "html_lt_gt": 0
    }

    if not target_dir.exists():
        print(f"Error: El directorio {target_dir} no existe.")
        return total_stats

    print(f"Iniciando sanitización en: {target_dir}")

    for root, _, files in os.walk(target_dir):
        for f in files:
            if f.endswith(".md"):
                file_path = Path(root) / f
                total_stats["archivos_procesados"] += 1
                
                original_text = file_path.read_text(encoding="utf-8")
                clean_text, stats = sanitizar_contenido(original_text)
                
                # Si hubo cambios, sobrescribir
                if clean_text != original_text:
                    total_stats["archivos_modificados"] += 1
                    file_path.write_text(clean_text, encoding="utf-8")
                    for k in stats:
                        total_stats[k] += stats[k]

    return total_stats


def main():
    target_dir = DEFAULT_DLMF_DIR
    if len(sys.argv) > 1:
        target_dir = Path(sys.argv[1]).resolve()

    stats = sanitizar_directorio(target_dir)

    print("\n--- RESUMEN DE SANITIZACIÓN DLMF ---")
    print(f"Archivos evaluados:               {stats['archivos_procesados']}")
    print(f"Archivos modificados:             {stats['archivos_modificados']}")
    print(f"Macros \\ifrac reemplazadas:        {stats['ifrac']}")
    print(f"Macros \\NVar desenvueltas:         {stats['NVar']}")
    print(f"Macros \\cfracstyle ajustadas:     {stats['cfracstyle']}")
    print(f"Asteriscos \\* normalizados:      {stats['asterisco_multiplicacion']}")
    print(f"Comandos \\mskip convertidos:     {stats['mskip']}")
    print(f"Símbolos \\pvint convertidos:      {stats['pvint']}")
    print(f"Entidades HTML &amp; corregidas:  {stats['html_amp']}")
    print(f"Entidades HTML &lt;/&gt; corregidas: {stats['html_lt_gt']}")
    print("------------------------------------\n")


if __name__ == "__main__":
    main()
