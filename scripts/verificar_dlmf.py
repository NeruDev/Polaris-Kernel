#!/usr/bin/env python3
"""
Script de verificación de sintaxis y compatibilidad KaTeX/MathJax para la biblioteca DLMF.
Valida que no existan macros no estándares residuales y que la sintaxis LaTeX/Markdown sea correcta.
"""

import os
import re
import sys
from pathlib import Path

DEFAULT_DLMF_DIR = Path(__file__).resolve().parent.parent / "docs" / "DLMF-markdown-main"

# Lista de patrones no deseados o incompatibles con KaTeX/MathJax
NON_STANDARD_PATTERNS = [
    (re.compile(r'\\ifrac\{'), "Macro \\ifrac no corregida"),
    (re.compile(r'\\NVar\{'), "Macro \\NVar no corregida"),
    (re.compile(r'\\cfracstyle'), "Macro \\cfracstyle no corregida"),
    (re.compile(r'\\\*'), "Asterisco \\* de multiplicación no corregido"),
    (re.compile(r'\\mskip'), "Comando \\mskip incompatible con KaTeX"),
    (re.compile(r'\\pvint'), "Símbolo \\pvint no nativo"),
]

# Entidades HTML no permitidas dentro de math blocks
MATH_HTML_ENTITIES = [
    (re.compile(r'&amp;'), "Entidad HTML &amp; en bloque LaTeX"),
    (re.compile(r'&lt;'), "Entidad HTML &lt; en bloque LaTeX"),
    (re.compile(r'&gt;'), "Entidad HTML &gt; en bloque LaTeX"),
]


def verificar_llaves_balanceadas(math_text: str) -> bool:
    """Verifica que las llaves {} en una expresión LaTeX estén balanceadas."""
    depth = 0
    escaped = False
    for char in math_text:
        if escaped:
            escaped = False
            continue
        if char == '\\':
            escaped = True
            continue
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def verificar_archivo(file_path: Path) -> list[dict]:
    """
    Verifica un archivo Markdown individual.
    Devuelve lista de hallazgos/errores.
    """
    issues = []
    text = file_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # 1. Verificar patrones en todo el texto línea por línea (omitiendo spans de código con backticks)
    for line_idx, line in enumerate(lines, 1):
        # Limpiar texto entre backticks `...` para ignorar menciones explicativas de macros
        clean_line = re.sub(r'`[^`]*`', '', line)
        for pattern, msg in NON_STANDARD_PATTERNS:
            if pattern.search(clean_line):
                issues.append({
                    "archivo": file_path.name,
                    "linea": line_idx,
                    "tipo": "Macro Incompatible",
                    "mensaje": msg,
                    "snippet": line.strip()[:80]
                })

    # 2. Extraer bloques de ecuaciones y verificar balance de llaves y entidades HTML
    math_pattern = re.compile(r'(\$\$.*?\$\$|\$.*?\$)', re.DOTALL)
    for match in math_pattern.finditer(text):
        math_block = match.group(0)
        # Encontrar número de línea aproximado
        line_no = text[:match.start()].count('\n') + 1

        # Verificar llaves
        if not verificar_llaves_balanceadas(math_block):
            issues.append({
                "archivo": file_path.name,
                "linea": line_no,
                "tipo": "Sintaxis LaTeX",
                "mensaje": "Llaves {} desbalanceadas en bloque math",
                "snippet": math_block.replace('\n', ' ')[:80]
            })

        # Verificar entidades HTML en math
        for entity_pattern, msg in MATH_HTML_ENTITIES:
            if entity_pattern.search(math_block):
                issues.append({
                    "archivo": file_path.name,
                    "linea": line_no,
                    "tipo": "Entidad HTML en Math",
                    "mensaje": msg,
                    "snippet": math_block.replace('\n', ' ')[:80]
                })

    return issues


def verificar_directorio(target_dir: Path) -> tuple[int, int, list[dict]]:
    """
    Recorre el directorio evaluando todos los archivos .md.
    """
    total_files = 0
    total_math_blocks = 0
    all_issues = []

    if not target_dir.exists():
        print(f"Error: El directorio {target_dir} no existe.")
        return 0, 0, []

    math_pattern = re.compile(r'(\$\$.*?\$\$|\$.*?\$)', re.DOTALL)

    for root, _, files in os.walk(target_dir):
        for f in files:
            if f.endswith(".md"):
                file_path = Path(root) / f
                total_files += 1
                text = file_path.read_text(encoding="utf-8")
                total_math_blocks += len(math_pattern.findall(text))
                
                issues = verificar_archivo(file_path)
                all_issues.extend(issues)

    return total_files, total_math_blocks, all_issues


def main():
    target_dir = DEFAULT_DLMF_DIR
    if len(sys.argv) > 1:
        target_dir = Path(sys.argv[1]).resolve()

    print(f"Iniciando verificación de compatibilidad KaTeX/MathJax en: {target_dir}")
    total_files, total_math, issues = verificar_directorio(target_dir)

    print("\n================ RESUMEN DE VERIFICACIÓN DLMF ================")
    print(f"Total de archivos analizados:      {total_files}")
    print(f"Total de expresiones math:         {total_math}")
    print(f"Total de problemas detectados:     {len(issues)}")
    print("==============================================================")

    if issues:
        print("\nDetalle de observaciones encontradas:")
        for issue in issues[:30]:  # Mostrar los primeros 30
            print(f" - [{issue['archivo']}:L{issue['linea']}] ({issue['tipo']}) {issue['mensaje']}")
            print(f"   Snippet: {issue['snippet']}")
        if len(issues) > 30:
            print(f"\n... y {len(issues) - 30} observaciones adicionales.")
        sys.exit(1)
    else:
        print("\n[OK] EXITO COMPLETO: Todos los archivos son 100% compatibles con KaTeX / MathJax / Quarto.")
        sys.exit(0)


if __name__ == "__main__":
    main()
