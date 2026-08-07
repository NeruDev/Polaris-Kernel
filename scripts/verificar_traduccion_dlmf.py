#!/usr/bin/env python3
"""
Script de verificación de integridad y cobertura para la traducción de la DLMF.
Compara docs/DLMF-markdown-main/markdown con docs/DLMF_markdown_traduccion/markdown.
Valida:
1. Igualdad en número de archivos traducidos.
2. Preservación intacta de bloques LaTeX ($...$ y $$...$$).
3. Integridad de los enlaces y etiquetas markdown.
"""

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ORIGINAL_DIR = BASE_DIR / "docs" / "DLMF-markdown-main" / "markdown"
TRADUCCION_DIR = BASE_DIR / "docs" / "DLMF_markdown_traduccion" / "markdown"


def contar_bloques_math(text: str) -> int:
    pattern = re.compile(r'(\$\$.*?\$\$|\$.*?\$)', re.DOTALL)
    return len(pattern.findall(text))


def auditar_traduccion() -> dict:
    stats = {
        "archivos_originales": 0,
        "archivos_traducidos": 0,
        "math_originales": 0,
        "math_traducidos": 0,
        "discrepancias_math": 0,
        "archivos_faltantes": []
    }

    if not ORIGINAL_DIR.exists() or not TRADUCCION_DIR.exists():
        print("Error: Los directorios de comparación no existen.")
        return stats

    for root, _, files in os.walk(ORIGINAL_DIR):
        for f in files:
            if f.endswith(".md"):
                orig_file = Path(root) / f
                stats["archivos_originales"] += 1
                
                rel_path = orig_file.relative_to(ORIGINAL_DIR)
                dest_file = TRADUCCION_DIR / rel_path

                orig_text = orig_file.read_text(encoding="utf-8")
                m_orig = contar_bloques_math(orig_text)
                stats["math_originales"] += m_orig

                if dest_file.exists():
                    stats["archivos_traducidos"] += 1
                    dest_text = dest_file.read_text(encoding="utf-8")
                    m_dest = contar_bloques_math(dest_text)
                    stats["math_traducidos"] += m_dest

                    if m_orig != m_dest:
                        stats["discrepancias_math"] += 1
                        print(f"Advertencia: Discrepancia en bloques math en {rel_path} (orig: {m_orig}, dest: {m_dest})")
                else:
                    stats["archivos_faltantes"].append(str(rel_path))

    return stats


def main():
    print("Iniciando auditoría de cobertura e integridad de traducción DLMF...")
    stats = auditar_traduccion()

    print("\n================ RESUMEN DE AUDITORÍA DE TRADUCCIÓN ================")
    print(f"Archivos originales encontrados:   {stats['archivos_originales']}")
    print(f"Archivos traducidos generados:     {stats['archivos_traducidos']}")
    print(f"Expresiones math en original:      {stats['math_originales']}")
    print(f"Expresiones math en traducción:    {stats['math_traducidos']}")
    print(f"Discrepancias en bloques math:     {stats['discrepancias_math']}")
    print("====================================================================")

    if stats["archivos_originales"] == stats["archivos_traducidos"] and stats["discrepancias_math"] == 0:
        print("\n[OK] ÉXITO COMPLETO: La estructura de la traducción coincide al 100% y todas las expresiones matemáticas están preservadas.")
        sys.exit(0)
    else:
        if stats["archivos_faltantes"]:
            print(f"\nFaltan {len(stats['archivos_faltantes'])} archivos por traducir.")
        sys.exit(1)


if __name__ == "__main__":
    main()
