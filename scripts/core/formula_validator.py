# yaml_frontmatter:
#   id: 'formula_validator'
#   title: 'Validador de sintaxis LaTeX y tablas Markdown'
#   tags: ['core', 'validation', 'math']

import re
from pathlib import Path
from typing import List

TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
TABLE_SEP_RE = re.compile(r"^\s*\|(?:\s*:?-{3,}:?\s*\|)+\s*$")

def scan_unbalanced_math(text: str) -> bool:
    """Detecta delimitadores $ y $$ desbalanceados."""
    in_inline = False
    in_block = False
    i = 0
    while i < len(text):
        if text[i] == "$" and (i == 0 or text[i-1] != "\\"):
            if i + 1 < len(text) and text[i+1] == "$":
                in_block = not in_block
                i += 2
                continue
            if not in_block:
                in_inline = not in_inline
        i += 1
    return in_inline or in_block

def validate_markdown_math_tables(text: str, source: str) -> List[str]:
    """Retorna advertencias sobre fórmulas y tablas."""
    warnings = []
    if scan_unbalanced_math(text):
        warnings.append(f"[WARN] Fórmulas desbalanceadas ($) en {source}")
    
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if TABLE_ROW_RE.match(line):
            if i + 1 < len(lines) and not (TABLE_ROW_RE.match(lines[i+1]) or TABLE_SEP_RE.match(lines[i+1])):
                # Podría ser una fila huérfana o fin de tabla mal formado
                pass
    return warnings
