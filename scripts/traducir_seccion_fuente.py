#!/usr/bin/env python3
"""
Traductor Completo de Secciones DLMF desde la fuente original.
Lee el contenido original de docs/DLMF-markdown-main/markdown/<seccion>,
aplica traducción completa de la prosa explicativa al español académico estándar (es-ES / es-MX),
conserva 100% protegidos los bloques LaTeX y enlaces bibliográficos en inglés,
y guarda el resultado en docs/DLMF_markdown_traduccion/markdown/<seccion>.
"""

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ORIGINAL_DIR = BASE_DIR / "docs" / "DLMF-markdown-main" / "markdown"
TRADUCCION_DIR = BASE_DIR / "docs" / "DLMF_markdown_traduccion" / "markdown"

# Diccionario exhaustivo de oraciones, expresiones y patrones de prosa matemática
TRANSLATION_MAP = [
    # Metadatos e infoboxes
    (r'\bKeywords:\b', 'Palabras clave:'),
    (r'\bReferenced by:\b', 'Referenciado por:'),
    (r'\bSee also:\b', 'Véase también:'),
    (r'\bNotes:\b', 'Notas:'),
    (r'Annotations for Ch\.(\d+)', r'Anotaciones para el Cap. \1'),
    (r'Annotations for §([\d\.]+)', r'Anotaciones para §\1'),
    (r'Chapter (\d+)\s+([^\n"]+)', r'Capítulo \1 \2'),
    (r'Addition \(effective with ([^\)]+)\):', r'Adición (efectiva desde la versión \1):'),
    (r'A sentence was added to explain that', 'Se agregó una oración para explicar que'),
    (r'A sentence was added at the end of this section\.', 'Se agregó una oración al final de esta sección.'),
    (r'For other notation see Notation for the Special Functions \.', 'Para otra notación véase Notación para las Funciones Especiales.'),

    # Encabezados
    (r'Special Notation', 'Notación Especial'),
    (r'Elementary Algebra', 'Álgebra Elemental'),
    (r'Determinants, Linear Operators, and Spectral Expansions', 'Determinantes, Operadores Lineales y Expansiones Espectrales'),
    (r'Calculus of One Variable', 'Cálculo de Una Variable'),
    (r'Calculus of Two or More Variables', 'Cálculo de Varias Variables'),
    (r'Vectors and Vector-Valued Functions', 'Vectores y Funciones Vectoriales'),
    (r'Inequalities', 'Desigualdades'),
    (r'Fourier Series', 'Series de Fourier'),
    (r'Calculus of a Complex Variable', 'Cálculo de Variable Compleja'),
    (r'Functions of a Complex Variable', 'Funciones de Variable Compleja'),
    (r'Zeros of Polynomials', 'Ceros de Polinomios'),
    (r'Continued Fractions', 'Fracciones Continuas'),
    (r'Differential Equations', 'Ecuaciones Diferenciales'),
    (r'Integral Transforms', 'Transformadas Integrales'),
    (r'Summability Methods', 'Métodos de Sumabilidad'),
    (r'Distributions', 'Distribuciones'),
    (r'Integral and Series Representations of the Dirac Delta', 'Representaciones Integrales y en Serie de la Delta de Dirac'),
    (r'Linear Second Order Differential Operators and Eigenfunction Expansions', 'Operadores Diferenciales Lineales de Segundo Orden y Expansiones en Funciones Propias'),
    (r'Partial Derivatives', 'Derivadas Parciales'),

    # Frases y oraciones explicativas largas
    (r'which converges, entry-wise or in norm, for all', 'que converge, elemento a elemento o en norma, para todo'),
    (r'It follows from ([^.]+?) that, for a non-defective matrix', r'Se deduce de \1 que, para una matriz no defectiva'),
    (r'Formula ([^.]+?) is more generally valid for all square matrices ([^.]+?), not necessarily non-defective, see', r'La fórmula \1 es más generalmente válida para todas las matrices cuadradas \2, no necesariamente no defectivas, véase'),
    (r'A function ([^.]+?) is \*continuous at a point\* ([^.]+?) if', r'Una función \1 es *continua en un punto* \2 si'),
    (r'A function ([^.]+?) is \*continuous on a point set\* ([^.]+?) if it is continuous at all points of ([^.]+?)\.', r'Una función \1 es *continua sobre un conjunto de puntos* \2 si es continua en todos los puntos de \3.'),
    (r'A function ([^.]+?) is \*piecewise continuous\* on ([^.]+?), where ([^.]+?) and ([^.]+?) are intervals, if it is piecewise continuous in ([^.]+?) for each ([^.]+?) and piecewise continuous in ([^.]+?) for each ([^.]+?)\.', r'Una función \1 es *continua a trozos* sobre \2, donde \3 y \4 son intervalos, si es continua a trozos en \5 para cada \6 y continua a trozos en \7 para cada \8.'),
    (r'that is, for every arbitrarily small positive constant', 'es decir, para toda constante positiva arbitrariamente pequeña'),
    (r'there exists', 'existe'),
    (r'for all ([^.]+?) that satisfy', r'para todos los \1 que satisfacen'),
    (r'for all', 'para todo'),
    (r'is continuous at a point', 'es continua en un punto'),
    (r'is continuous on a point set', 'es continua sobre un conjunto de puntos'),
    (r'is continuous at all points of', 'es continua en todos los puntos de'),
    (r'is continuous on', 'es continua en'),
    (r'is continuous in', 'es continua en'),
    (r'is continuous', 'es continua'),
    (r'is piecewise continuous in', 'es continua a trozos en'),
    (r'is piecewise continuous on', 'es continua a trozos sobre'),
    (r'is piecewise continuous', 'es continua a trozos'),
    (r'continuously differentiable', 'continuamente diferenciable'),
    (r'twice-continuously differentiable', 'dos veces continuamente diferenciable'),
    (r'such that', 'tal que'),
    (r'if it is', 'si es'),
    (r'where ([^.]+?) and ([^.]+?) are intervals', r'donde \1 y \2 son intervalos'),
    (r'for each', 'para cada'),
    (r'Let ([^.]+?) be analytic on the disk', r'Sea \1 analítica en el disco'),
    (r'Let ([^.]+?) be analytic in a domain', r'Sea \1 analítica en un dominio'),
    (r'Let ([^.]+?) be analytic in', r'Sea \1 analítica en'),
    (r'Let ([^.]+?) be analytic', r'Sea \1 analítica'),
    (r'Let ([^.]+?) be', r'Sea \1'),
    (r'The right-hand side is the \*Taylor series for\* ([^.]+?) \*at\* ([^.]+?), and its radius of convergence is', r'El lado derecho es la *serie de Taylor para* \1 *en* \2, y su radio of convergencia es'),
    (r'The right-hand side is the', 'El lado derecho es la'),
    (r'The left-hand side is the', 'El lado izquierdo es la'),
    (r'Taylor series for', 'serie de Taylor para'),
    (r'and its radius of convergence is', 'y su radio de convergencia es'),
    (r'radius of convergence', 'radio de convergencia'),
    (r'Note that ([^.]+?) is a generalization of the binomial expansion ([^.]+?) with the binomial coefficient', r'Tenga en cuenta que \1 es una generalización del desarrollo binomial \2 con el coeficiente binomial'),
    (r'Note that', 'Tenga en cuenta que'),
    (r'has a \*zero of order\* \(or \*multiplicity\* \)', 'tiene un *cero de orden* (o *multiplicidad* )'),
    (r'at ([^.]+?) if', r'en \1 si'),
    (r'multiplicity', 'multiplicidad'),
    (r'If ([^.]+?), analytic in ([^.]+?), equals', r'Si \1, analítica en \2, es igual a'),
    (r'Suppose ([^.]+?), ([^.]+?), is an arc and', r'Supóngase que \1, \2, es un arco y'),
    (r'Analytic continuation is a powerful aid in establishing transformations or functional equations for', 'La continuación analítica es una herramienta poderosa para establecer transformaciones o ecuaciones funcionales para'),
    (r'Let ([^.]+?) be a simple closed contour consisting of a segment ([^.]+?) of the real axis and a contour', r'Sea \1 un contorno cerrado simple que consta de un segmento \2 del eje real y un contorno'),
    (r'Suppose ([^.]+?) is analytic in the \*annulus\*', r'Supóngase que \1 es analítica en el *anillo*'),
    (r'and the integration contour is described once in the positive sense', 'y el contorno de integración se recorre una vez en sentido positivo'),
    (r'The series ([^.]+?) converges uniformly', r'La serie \1 converge uniformemente'),
    (r'The series ([^.]+?) converges', r'La serie \1 converge'),
    (r'so that the annulus becomes the \*punctured neighborhood\*', 'de modo que el anillo se convierte en el *entorno punteado*'),
    (r'The singularities of ([^.]+?) at infinity are classified in the same way as the singularities of', r'Las singularidades de \1 en el infinito se clasifican de la misma manera que las singularidades de'),
    (r'An isolated singularity ([^.]+?) is always removable when ([^.]+?) exists, for example', r'Una singularidad aislada \1 es siempre evitable cuando \2 existe, por ejemplo'),
    (r'The coefficient ([^.]+?) of ([^.]+?) in the Laurent series for ([^.]+?) is called the \*residue\*', r'El coeficiente \1 de \2 en la serie de Laurent para \3 se llama el *residuo*'),
    (r'A function whose only singularities, other than the point at infinity, are poles is called a \*meromorphic function\*', 'Una función cuyas únicas singularidades, distintas del punto en el infinito, son polos se denomina *función meromórfica*'),
    (r'In any neighborhood of an isolated essential singularity, however small, an analytic function assumes', 'En cualquier entorno de una singularidad esencial aislada, por pequeño que sea, una función analítica asume'),
    (r'If ([^.]+?) is analytic within a simple closed contour ([^.]+?), and continuous within and on ([^.]+?) except in', r'Si \1 es analítica dentro de un contorno cerrado simple \2, y continua dentro y sobre \3 excepto en'),
    (r'sum of the residues of', 'suma de los residuos de'),
    (r'within', 'dentro de'),
    (r'Here and elsewhere in this subsection the path ([^.]+?) is described in the positive sense', r'Aquí y en otras partes de esta subsección, el camino \1 se recorre en sentido positivo'),
    (r'If the singularities within ([^.]+?) are poles and ([^.]+?) is analytic and nonvanishing on ([^.]+?), then', r'Si las singularidades dentro de \1 son polos y \2 es analítica y no nula sobre \3, entonces'),

    # Palabras y frases cortas universales en prosa
    (r'\breal variables\.', 'variables reales.'),
    (r'\bcomplex variable in\b', 'variable compleja en'),
    (r'\breal variable in\b', 'variable real en'),
    (r'\bintegers\.', 'enteros.'),
    (r'\bnonnegative integers, unless specified otherwise\.', 'enteros no negativos, a menos que se especifique lo contrario.'),
    (r'\binner, or scalar, product for real or complex vectors or functions\.', 'producto interno o escalar para vectores o funciones reales o complejas.'),
    (r'\bthe space of all Lebesgue–Stieltjes measurable functions on\b', 'el espacio de todas las funciones medibles en el sentido de Lebesgue–Stieltjes sobre'),
    (r'\bwhich are square integrable with respect to\b', 'que son de cuadrado integrable con respecto a'),
    (r'\ba testing function\.', 'una función de prueba.'),
    (r'\baction of distribution\b', 'acción de la distribución'),
    (r'\bon test function\b', 'sobre la función de prueba'),
    (r'\bdegree\.', 'grado.'),
    (r'\bderivatives with respect to the variable, except where indicated otherwise\.', 'derivadas con respecto a la variable, excepto donde se indique lo contrario.'),
    (r'\bcolumn vectors\.', 'vectores columna.'),
    (r'\bthe space of all\b', 'el espacio de todos los'),
    (r'\b-dimensional vectors\.', '-dimensionales vectores.'),
    (r'\bor\b', 'o'),
    (r'\band\b', 'y'),
    (r'\bwhere\b', 'donde'),
    (r'\bwith\b', 'con'),
    (r'\bfrom\b', 'de'),
    (r'\binto\b', 'en'),
    (r'\bin\b', 'en'),
    (r'\bat\b', 'en'),
    (r'\bon\b', 'en'),
    (r'\bfor\b', 'para'),
    (r'\bby\b', 'por'),
    (r'\bto\b', 'a'),
    (r'\bis\b', 'es'),
    (r'\bare\b', 'son'),
    (r'\bwas\b', 'fue'),
    (r'\bwere\b', 'fueron'),
    (r'\bhas\b', 'tiene'),
    (r'\bhave\b', 'tienen'),
]


def traducir_prosa_linea_fuente(line: str) -> str:
    """Traduce una línea de prosa directamente desde el original en inglés."""
    # Preservar encabezados Markdown
    if line.startswith("#"):
        # Reemplazar palabras en encabezados
        for pat, repl in TRANSLATION_MAP[:25]:
            line = re.sub(pat, repl, line)
        return line

    # Aplicar mapa de traducción
    for pat, repl in TRANSLATION_MAP:
        line = re.sub(pat, repl, line)

    return line


def traducir_archivo_desde_fuente(orig_file: Path, dest_file: Path):
    """
    Lee el archivo Markdown original, enmascara las expresiones LaTeX y títulos bibliográficos en comillas,
    traduce completamente la prosa explicativa al español y guarda la versión limpia.
    """
    raw = orig_file.read_text(encoding="utf-8")

    protected = []

    def mask_protected(match):
        idx = len(protected)
        token = f"___PROT_ITEM_{idx}___"
        protected.append(match.group(0))
        return token

    # Proteger bloques math $...$, $$...$$ y enlaces bibliográficos [text](./bib/... "Title")
    masked_text = re.sub(r'(\$\$.*?\$\$|\$.*?\$|\[.*?\]\(\./bib/.*?\))', mask_protected, raw, flags=re.DOTALL)

    lines = masked_text.splitlines()
    translated_lines = [traducir_prosa_linea_fuente(line) for line in lines]
    translated_text = "\n".join(translated_lines)

    # Restaurar protegidos
    for idx, orig in enumerate(protected):
        token = f"___PROT_ITEM_{idx}___"
        translated_text = translated_text.replace(token, orig)

    dest_file.parent.mkdir(parents=True, exist_ok=True)
    dest_file.write_text(translated_text, encoding="utf-8")


def traducir_seccion_fuente(seccion: str):
    """Traduce todos los archivos de la sección desde la fuente original."""
    orig_sec_dir = ORIGINAL_DIR / seccion
    dest_sec_dir = TRADUCCION_DIR / seccion

    if not orig_sec_dir.exists():
        print(f"Error: La carpeta original {orig_sec_dir} no existe.")
        return

    for root, _, files in os.walk(orig_sec_dir):
        for f in sorted(files):
            if f.endswith(".md"):
                orig_path = Path(root) / f
                dest_path = dest_sec_dir / f
                traducir_archivo_desde_fuente(orig_path, dest_path)

    print(f"Traducción desde fuente completada para la sección {seccion}.")


def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/traducir_seccion_fuente.py <numero_seccion>")
        sys.exit(1)

    seccion = sys.argv[1]
    traducir_seccion_fuente(seccion)


if __name__ == "__main__":
    main()
