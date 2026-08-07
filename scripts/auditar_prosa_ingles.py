#!/usr/bin/env python3
"""
Auditor de Prosa en Inglés Residual para DLMF Traducción.
Examina un capítulo o sección en docs/DLMF_markdown_traduccion/markdown/
omitiendo bloques LaTeX, URLs de búsqueda NIST y enlaces bibliográficos en inglés,
e identifica líneas que aún contengan oraciones o palabras en inglés no traducidas en la prosa.
"""

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TRADUCCION_MD_DIR = BASE_DIR / "docs" / "DLMF_markdown_traduccion" / "markdown"

# Indicadores de prosa en inglés residual
ENGLISH_INDICATORS = [
    r'\bwhich\b', r'\bconverges\b', r'\bentry-wise\b', r'\bin norm\b', r'\bIt follows from\b',
    r'\bthat\b', r'\bfor a\b', r'\bnon-defective\b', r'\bmatrix\b', r'\bFormula\b', r'\bis more generally\b',
    r'\bvalid\b', r'\bsquare matrices\b', r'\bnot necessarily\b', r'\bThm\b', r'\bProof\b',
    r'\bSuppose that\b', r'\bLet\b', r'\bbe a\b', r'\bwhere\b', r'\bdefined by\b', r'\bif and only if\b',
    r'\bwith respect to\b', r'\bon the interval\b', r'\bis given by\b', r'\bholds for\b', r'\bdenoted by\b',
    r'\bshows that\b', r'\bimplies that\b', r'\bwhen\b', r'\bsuch that\b', r'\bthere exists\b',
    r'\bfor every\b', r'\bby means of\b', r'\bin terms of\b', r'\bwith\b', r'\bfrom\b', r'\binto\b',
    r'\bthe\b', r'\bof\b', r'\bto\b', r'\bin\b', r'\bis\b', r'\bare\b', r'\bwas\b', r'\bwere\b', r'\bbe\b',
    r'\bbeen\b', r'\bhave\b', r'\bhas\b', r'\bhad\b', r'\bthis\b', r'\bthese\b', r'\bthose\b'
]

ENGLISH_REGEX = re.compile('|'.join(ENGLISH_INDICATORS), re.IGNORECASE)


def auditar_archivo(file_path: Path) -> list[dict]:
    """
    Audita un archivo individual en busca de prosa explicativa en inglés.
    Omite expresiones LaTeX, URLs de búsqueda y referencias bibliográficas.
    """
    text = file_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    findings = []

    for line_no, line in enumerate(lines, 1):
        # 1. Omitir líneas de código, delimitadores o etiquetas HTML
        stripped = line.strip()
        if stripped.startswith(":::") or stripped.startswith("```") or stripped.startswith("<a ") or stripped == "---":
            continue

        # 2. Omitir bibliografía [text](./bib/...) y URLs de búsqueda NIST (http://dlmf.nist.gov/search/...)
        clean_line = re.sub(r'\[.*?\]\(\./bib/.*?\)', '', line)
        clean_line = re.sub(r'\[.*?\]\(http://dlmf\.nist\.gov/search/.*?\)', '', clean_line)
        clean_line = re.sub(r'https?://[^\s\)]+', '', clean_line)
        clean_line = re.sub(r'".*?"', '', clean_line)
        clean_line = re.sub(r'<[^>]+>', '', clean_line)

        # 3. Omitir bloques LaTeX ($...$ inline y $$...$$ bloque)
        clean_line = re.sub(r'\$\$.*?\$\$', '', clean_line)
        clean_line = re.sub(r'\$[^$\n]+?\$', '', clean_line)

        # 4. Buscar palabras indicativas de prosa en inglés en la parte explicativa restante
        matches = ENGLISH_REGEX.findall(clean_line)
        clean_str = clean_line.strip()
        
        # Considerar residuo de prosa solo si hay 2 o más palabras o 1 palabra significativa en prosa de >20 caracteres
        if len(matches) >= 2 or (len(matches) == 1 and len(clean_str) > 20):
            findings.append({
                "line_no": line_no,
                "line_content": line[:100],
                "matches": matches,
                "clean_line": clean_str[:80]
            })

    return findings


def auditar_seccion(seccion: str):
    sec_dir = TRADUCCION_MD_DIR / seccion
    if not sec_dir.exists():
        print(f"Error: La sección {sec_dir} no existe.")
        return

    all_findings = []
    total_files = 0

    for root, _, files in os.walk(sec_dir):
        for f in sorted(files):
            if f.endswith(".md"):
                total_files += 1
                file_path = Path(root) / f
                findings = auditar_archivo(file_path)
                for item in findings:
                    item["filename"] = file_path.name
                    all_findings.append(item)

    print(f"\n================ AUDITORÍA DE SECCIÓN {seccion} ================")
    print(f"Archivos auditados: {total_files}")
    print(f"Líneas con prosa en inglés residuales: {len(all_findings)}")
    print("=========================================================\n")

    if all_findings:
        print("Detalle de líneas que requieren traducción:")
        for item in all_findings[:30]:  # Mostrar los primeros 30 hallazgos
            print(f" - [{item['filename']}:L{item['line_no']}] {item['line_content']}")
        if len(all_findings) > 30:
            print(f"... y {len(all_findings) - 30} líneas adicionales.")
    else:
        print("¡SECCIÓN 100% VERIFICADA Y LIMPIA EN ESPAÑOL!")


def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/auditar_prosa_ingles.py <numero_seccion>")
        sys.exit(1)

    seccion = sys.argv[1]
    auditar_seccion(seccion)


if __name__ == "__main__":
    main()
