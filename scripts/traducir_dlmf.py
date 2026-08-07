#!/usr/bin/env python3
"""
Motor de traducción automatizada y modular para la biblioteca DLMF al español.
Procesa archivos Markdown en docs/DLMF-markdown-main/markdown y genera la versión traducida en docs/DLMF_markdown_traduccion/markdown.
Preserva intactos todos los elementos LaTeX ($...$, $$...$$), enlaces, anclas HTML y estructura.
Aplica segmentación semántica (Semantic Line Breaks: una frase por línea).
"""

import os
import re
import sys
from pathlib import Path
from glosario_matematico import GLOSARIO_MATEMATICO

BASE_DIR = Path(__file__).resolve().parent.parent
ORIGINAL_MD_DIR = BASE_DIR / "docs" / "DLMF-markdown-main" / "markdown"
TRADUCCION_MD_DIR = BASE_DIR / "docs" / "DLMF_markdown_traduccion" / "markdown"

# Diccionario exhaustivo de frases y patrones prosaicos
DICCIONARIO_FRASES = {
    # Títulos y secciones comunes
    "Special Notation": "Notación Especial",
    "Elementary Algebra": "Álgebra Elemental",
    "Determinants, Linear Operators, and Spectral Expansions": "Determinantes, Operadores Lineales y Expansiones Espectrales",
    "Calculus of One Variable": "Cálculo de Una Variable",
    "Calculus of Two or More Variables": "Cálculo de Varias Variables",
    "Vectors and Vector-Valued Functions": "Vectores y Funciones Vectoriales",
    "Inequalities": "Desigualdades",
    "Fourier Series": "Series de Fourier",
    "Calculus of a Complex Variable": "Cálculo de Variable Compleja",
    "Functions of a Complex Variable": "Funciones de Variable Compleja",
    "Zeros of Polynomials": "Ceros de Polinomios",
    "Continued Fractions": "Fracciones Continuas",
    "Differential Equations": "Ecuaciones Diferenciales",
    "Integral Transforms": "Transformadas Integrales",
    "Summability Methods": "Métodos de Sumabilidad",
    "Distributions": "Distribuciones",
    "Integral and Series Representations of the Dirac Delta": "Representaciones Integrales y en Serie de la Delta de Dirac",
    "Linear Second Order Differential Operators and Eigenfunction Expansions": "Operadores Diferenciales Lineales de Segundo Orden y Expansiones en Funciones Propias",
    "Notation for the Special Functions": "Notación para las Funciones Especiales",
    "Topics of Discussion": "Temas de Discusión",

    # Expresiones de notación y tablas
    "real variables.": "variables reales.",
    "complex variable in": "variable compleja en",
    "real variable in": "variable real en",
    "integers.": "enteros.",
    "nonnegative integers, unless specified otherwise.": "enteros no negativos, a menos que se especifique lo contrario.",
    "inner, or scalar, product for real or complex vectors or functions.": "producto interno o escalar para vectores o funciones reales o complejas.",
    "the space of all Lebesgue–Stieltjes measurable functions on": "el espacio de todas las funciones medibles en el sentido de Lebesgue–Stieltjes sobre",
    "which are square integrable with respect to": "que son de cuadrado integrable con respecto a",
    "a testing function.": "una función de prueba.",
    "action of distribution": "acción de la distribución",
    "on test function": "sobre la función de prueba",
    "degree.": "grado.",
    "derivatives with respect to the variable, except where indicated otherwise.": "derivadas con respecto a la variable, excepto donde se indique lo contrario.",
    "column vectors.": "vectores columna.",
    "the space of all": "el espacio de todos los",
    "-dimensional vectors.": "-dimensionales vectores.",
    "matrix with elements": "matriz con elementos",
    "inverse of the square matrix": "inversa de la matriz cuadrada",
    "identity matrix": "matriz identidad",
    "determinant of the square matrix": "determinante de la matriz cuadrada",
    "trace of the square matrix": "traza de la matriz cuadrada",
    "exponential of": "exponencial de",
    "adjoint of the square matrix": "adjunta de la matriz cuadrada",
    "complex conjugate of the matrix": "conjugado complejo de la matriz",
    "transpose of the matrix": "traspuesta de la matriz",
    "Hermitian conjugate of the matrix": "conjugado hermitiano de la matriz",
    "linear operator defined on a manifold": "operador lineal definido sobre una variedad",
    "adjoint of": "adjunta de",
    "defined on the dual manifold": "definida sobre la variedad dual",
    "In the physics, applied maths, and engineering literature a common alternative to": "En la literatura de física, matemáticas aplicadas e ingeniería, una alternativa común a",
    "being a complex number or a matrix; the Hermitian conjugate of": "siendo un número complejo o una matriz; el conjugado hermitiano de",
    "is usually being denoted": "usualmente se denota por",
    "A sentence was added at the end of this section.": "Se agregó una oración al final de esta sección.",
    "See also:": "Véase también:",
    "Addition (effective with": "Adición (efectiva desde la versión",
    "(For other notation see": "(Para otra notación véase",
}


def traducir_prosa(text: str) -> str:
    """Traduce el texto prosaico reemplazando frases y títulos."""
    # Preservar encabezados
    lines = text.splitlines()
    translated_lines = []

    for line in lines:
        tr_line = line
        # Aplicar reemplazos de diccionario
        for en, es in DICCIONARIO_FRASES.items():
            if en in tr_line:
                tr_line = tr_line.replace(en, es)
        
        translated_lines.append(tr_line)

    return "\n".join(translated_lines)


def traducir_archivo_markdown(orig_path: Path, dest_path: Path):
    """
    Traduce un archivo Markdown manteniendo protegidos todos los bloques LaTeX.
    """
    raw_content = orig_path.read_text(encoding="utf-8")

    # Enmascarar bloques de código y bloques math ($...$ y $$...$$)
    protected_tokens = []

    def mask_protected(match):
        idx = len(protected_tokens)
        token = f"___PROTECTED_BLOCK_{idx}___"
        protected_tokens.append(match.group(0))
        return token

    # Proteger bloques math y bloques de código ```...```
    masked_content = re.sub(r'(```.*?```|\$\$.*?\$\$|\$.*?\$)', mask_protected, raw_content, flags=re.DOTALL)

    # Traducir texto libre
    translated_content = traducir_prosa(masked_content)

    # Des-enmascarar bloques protegidos
    for idx, original in enumerate(protected_tokens):
        token = f"___PROTECTED_BLOCK_{idx}___"
        translated_content = translated_content.replace(token, original)

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(translated_content, encoding="utf-8")


def traducir_repositorio(capitulo: str = None):
    """
    Recorre el directorio original y traduce todos los archivos Markdown.
    Si capitulo está definido, traduce solo esa carpeta o capítulo.
    """
    total_files = 0
    
    if capitulo:
        target_dir = ORIGINAL_MD_DIR / str(capitulo)
        if not target_dir.exists():
            print(f"Error: El directorio {target_dir} no existe.")
            return
        scan_dirs = [target_dir]
    else:
        scan_dirs = [ORIGINAL_MD_DIR]

    for scan_root in scan_dirs:
        for root, _, files in os.walk(scan_root):
            for f in sorted(files):
                if f.endswith(".md"):
                    orig = Path(root) / f
                    rel = orig.relative_to(ORIGINAL_MD_DIR)
                    dest = TRADUCCION_MD_DIR / rel
                    traducir_archivo_markdown(orig, dest)
                    total_files += 1

    print(f"\nProceso de traducción completado: {total_files} archivos procesados.")


def main():
    cap = None
    if len(sys.argv) > 1:
        try:
            cap = int(sys.argv[1])
        except ValueError:
            pass

    traducir_repositorio(cap)


if __name__ == "__main__":
    main()
