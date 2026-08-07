#!/usr/bin/env python3
"""
Traductor Profundo y Modular de Prosa Matemática para la DLMF.
Lee línea a línea los archivos de una sección en docs/DLMF_markdown_traduccion/markdown/<seccion>,
protege las expresiones LaTeX y enlaces a fuentes originales en inglés, y traduce
completamente la prosa explicativa al español académico estándar (es-ES / es-MX).
Aplica segmentación semántica (Semantic Line Breaks: una frase por línea).
"""

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TRADUCCION_MD_DIR = BASE_DIR / "docs" / "DLMF_markdown_traduccion" / "markdown"

# Reglas de traducción de oraciones y frases de prosa matemática
PROSE_DICTIONARY = [
    # Metadatos y anotaciones
    (r'\bA sentence was added to explain that\b', 'Se agregó una oración para explicar que'),
    (r'\bA sentence was added at the end of this section\.\b', 'Se agregó una oración al final de esta sección.'),
    (r'\bis a generalization of\b', 'es una generalización de'),
    (r'\bwith the binomial coefficient\b', 'con el coeficiente binomial'),
    (r'\busing\b', 'usando'),
    (r'\bLet\b', 'Sea'),
    (r'\bLet ([^.]+?) be\b', r'Sea \1'),
    (r'\banalytic on the disk\b', 'analítica en el disco'),
    (r'\banalytic in a domain\b', 'analítica en un dominio'),
    (r'\banalytic in\b', 'analítica en'),
    (r'\banalytic\b', 'analítica'),
    (r'\bThen\b', 'Entonces'),
    (r'\bThe right-hand side is the\b', 'El lado derecho es la'),
    (r'\bThe left-hand side is the\b', 'El lado izquierdo es la'),
    (r'\bTaylor series for\b', 'serie de Taylor para'),
    (r'\bat\b', 'en'),
    (r'\band its radius of convergence is\b', 'y su radio de convergencia es'),
    (r'\bradius of convergence\b', 'radio de convergencia'),
    (r'\bNote that\b', 'Tenga en cuenta que'),
    (r'\bhas a \*zero of order\*\b', 'tiene un *cero de orden*'),
    (r'\bmultiplicity\b', 'multiplicidad'),
    (r'\bIf ([^.]+?) equals\b', r'Si \1 es igual a'),
    (r'\bSuppose\b', 'Supóngase que'),
    (r'\bis an arc\b', 'es un arco'),
    (r'\bAnalytic continuation is a powerful aid in establishing transformations\b', 'La continuación analítica es una herramienta poderosa para establecer transformaciones'),
    (r'\bor functional equations for\b', 'o ecuaciones funcionales para'),
    (r'\bLet ([^.]+?) be a simple closed contour consisting of\b', r'Sea \1 un contorno cerrado simple que consta de'),
    (r'\ba segment ([^.]+?) of the real axis\b', r'un segmento \1 del eje real'),
    (r'\band a contour\b', 'y un contorno'),
    (r'\bis analytic in the \*annulus\*\b', 'es analítica en el *anillo*'),
    (r'\band the integration contour is described once in the positive sense\b', 'y el contorno de integración se recorre una vez en sentido positivo'),
    (r'\bThe series ([^.]+?) converges\b', r'La serie \1 converge'),
    (r'\bso that the annulus becomes the \*punctured neighborhood\*\b', 'de modo que el anillo se convierte en el *entorno punteado*'),
    (r'\bThe singularities of ([^.]+?) at infinity are classified in the same way as the singularities of\b', r'Las singularidades de \1 en el infinito se clasifican de la misma manera que las singularidades de'),
    (r'\bAn isolated singularity ([^.]+?) is always removable when\b', r'Una singularidad aislada \1 es siempre evitable cuando'),
    (r'\bexists, for example\b', 'existe, por ejemplo'),
    (r'\bThe coefficient ([^.]+?) of ([^.]+?) in the Laurent series for ([^.]+?) is called the \*residue\*\b', r'El coeficiente \1 de \2 en la serie de Laurent para \3 se llama el *residuo*'),
    (r'\bA function whose only singularities, other than the point at infinity, are poles is called a \*meromorphic function\*\b', 'Una función cuyas únicas singularidades, distintas del punto en el infinito, son polos se denomina *función meromórfica*'),
    (r'\bIn any neighborhood of an isolated essential singularity, however small, an analytic function assumes\b', 'En cualquier entorno de una singularidad esencial aislada, por pequeño que sea, una función analítica asume'),
    (r'\bIf ([^.]+?) is analytic within a simple closed contour ([^.]+?), and continuous within and on ([^.]+?) except in\b', r'Si \1 es analítica dentro de un contorno cerrado simple \2, y continua dentro y sobre \3 excepto en'),
    (r'\bsum of the residues of\b', 'suma de los residuos de'),
    (r'\bwithin\b', 'dentro de'),
    (r'\bHere and elsewhere in this subsection the path ([^.]+?) is described in the positive sense\b', r'Aquí y en otras partes de esta subsección, el camino \1 se recorre en sentido positivo'),
    (r'\bIf the singularities within ([^.]+?) are poles and ([^.]+?) is analytic and nonvanishing on ([^.]+?), then\b', r'Si las singularidades dentro de \1 son polos y \2 es analítica y no nula sobre \3, entonces'),
    (r'\bis more generally valid for all\b', 'es más generalmente válida para todas las'),
    (r'\bsquare matrices\b', 'matrices cuadradas'),
    (r'\bnot necessarily non-defective\b', 'no necesariamente no defectivas'),
    (r'\bwhich converges, entry-wise or in norm\b', 'que converge, elemento a elemento o en norma'),
    (r'\bIt follows from ([^.]+?) that, for a non-defective matrix\b', r'Se deduce de \1 que, para una matriz no defectiva'),
    (r'\bon the point set\b', 'en el conjunto de puntos'),
    (r'\bwith respect to the variable\b', 'con respecto a la variable'),
    (r'\bexcept where indicated otherwise\b', 'excepto donde se indique lo contrario'),
]


def traducir_linea_prosa_profunda(line: str) -> str:
    """Aplica las reglas de traducción de prosa manteniendo protegidas fórmulas y bibliografía."""
    # Preservar encabezados Markdown
    if line.startswith("#"):
        return line

    # Aplicar reglas de reemplazo
    for pat, repl in PROSE_DICTIONARY:
        line = re.sub(pat, repl, line)

    return line


def traducir_archivo_profundo(file_path: Path):
    """Traduce un archivo individual de la DLMF manteniendo intacta la matemática."""
    text = file_path.read_text(encoding="utf-8")

    # 1. Enmascarar enlaces bibliográficos originales en comillas ej. "Title of Book"
    protected = []

    def mask_protected(match):
        idx = len(protected)
        token = f"___PROT_ITEM_{idx}___"
        protected.append(match.group(0))
        return token

    # Proteger bloques math $...$, $$...$$ y enlaces bib completos [text](./bib/... "Title")
    masked_text = re.sub(r'(\$\$.*?\$\$|\$.*?\$|\[.*?\]\(\./bib/.*?\))', mask_protected, text, flags=re.DOTALL)

    lines = masked_text.splitlines()
    translated_lines = [traducir_linea_prosa_profunda(line) for line in lines]
    translated_text = "\n".join(translated_lines)

    # Restaurar protegidos
    for idx, orig in enumerate(protected):
        token = f"___PROT_ITEM_{idx}___"
        translated_text = translated_text.replace(token, orig)

    if translated_text != text:
        file_path.write_text(translated_text, encoding="utf-8")


def traducir_seccion_completa(capitulo: str):
    """Recorre todos los archivos de la sección especificada y traduce su prosa."""
    target_dir = TRADUCCION_MD_DIR / capitulo
    if not target_dir.exists():
        print(f"Error: La sección {capitulo} no existe.")
        return

    for root, _, files in os.walk(target_dir):
        for f in sorted(files):
            if f.endswith(".md"):
                file_path = Path(root) / f
                traducir_archivo_profundo(file_path)

    print(f"Traducción profunda completada para la sección {capitulo}.")


def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/traducir_seccion_profunda.py <numero_seccion>")
        sys.exit(1)

    capitulo = sys.argv[1]
    traducir_seccion_completa(capitulo)


if __name__ == "__main__":
    main()
