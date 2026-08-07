#!/usr/bin/env python3
"""
Traductor Completo de Prosa DLMF al Español Académico Estándar.
Procesa archivos Markdown línea por línea, protegiendo todas las expresiones
matemáticas y referencias bibliográficas en inglés, y traduciendo
completamente la prosa explicativa restante.
"""

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ORIGINAL_DIR = BASE_DIR / "docs" / "DLMF-markdown-main" / "markdown"
TRADUCCION_DIR = BASE_DIR / "docs" / "DLMF_markdown_traduccion" / "markdown"

# Reemplazos por orden estricto de prioridad (de frases compuestas a palabras individuales)
REEMPLAZOS_PROSA = [
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

    # Frases compuestas de teoremas y demostraciones (incluyendo variantes híbridas)
    (r'\binverse of the (square matrix|matriz cuadrada)\b', 'inversa de la matriz cuadrada'),
    (r'\binverse of the (matrix|matriz)\b', 'inversa de la matriz'),
    (r'\bdeterminant of the (square matrix|matriz cuadrada)\b', 'determinante de la matriz cuadrada'),
    (r'\bdeterminant of the (matrix|matriz)\b', 'determinante de la matriz'),
    (r'\btrace of the (square matrix|matriz cuadrada)\b', 'traza de la matriz cuadrada'),
    (r'\btrace of the (matrix|matriz)\b', 'traza de la matriz'),
    (r'\badjoint of the (square matrix|matriz cuadrada)\b', 'adjunta de la matriz cuadrada'),
    (r'\badjoint of the (matrix|matriz)\b', 'adjunta de la matriz'),
    (r'\b(complex|compleja) conjugate of the (matrix|matriz)\b', 'conjugado complejo de la matriz'),
    (r'\btranspose of the (matrix|matriz)\b', 'traspuesta de la matriz'),
    (r'\bHermitian conjugate of the (matrix|matriz)\b', 'conjugado hermitiano de la matriz'),
    (r'\badjoint of ([^.]+?) defined (on|en) the dual manifold\b', r'adjunta de \1 definida sobre la variedad dual'),
    (r'\bIn the physics, applied maths, (and|y) engineering literature a common alternative (to|a)\b', 'En la literatura de física, matemáticas aplicadas e ingeniería, una alternativa común a'),
    (r'\bof a (complex|compleja) variable\b', 'de una variable compleja'),
    (r'\bof a (real|real) variable\b', 'de una variable real'),
    (r'\bSea ([^.]+?) anal[íi]tica en (the disk|el disco)\b', r'Sea \1 analítica en el disco'),
    (r'\bSea ([^.]+?) anal[íi]tica en (a domain|un dominio)\b', r'Sea \1 analítica en un dominio'),

    (r'\bIt follows from ([^.]+?) that, for a non-defective matrix\b', r'Se deduce de \1 que, para una matriz no defectiva'),
    (r'\bIt follows from ([^.]+?) that, for a\b', r'Se deduce de \1 que, para una'),
    (r'\bIt follows from ([^.]+?) that, for\b', r'Se deduce de \1 que, para'),
    (r'\bthat, for a non-defective matrix\b', 'que, para una matriz no defectiva'),
    (r'\bthat, for a\b', 'que, para una'),
    (r'\bthat, for\b', 'que, para'),
    (r'\bfor a non-defective matrix\b', 'para una matriz no defectiva'),
    (r'\bfor a\b', 'para una'),
    (r'\bfor an\b', 'para un'),
    (r'\bwhich converges, entry-wise or in norm, for all\b', 'que converge, elemento a elemento o en norma, para todo'),
    (r'\bwhich converges, entry-wise or in norm\b', 'que converge, elemento a elemento o en norma'),
    (r'\bentry-wise or in norm\b', 'elemento a elemento o en norma'),
    (r'\bIt follows from\b', 'Se deduce de'),
    (r'\bis more generally valid for all square matrices\b', 'es más generalmente válida para todas las matrices cuadradas'),
    (r'\bis more generally valid for all\b', 'es más generalmente válida para todo'),
    (r'\bis more generally valid for\b', 'es más generalmente válida para'),
    (r'\bis more generally valid\b', 'es más generalmente válida'),
    (r'\bnot necessarily non-defective\b', 'no necesariamente no defectivas'),
    (r'\bnon-defective matrix\b', 'matriz no defectiva'),
    (r'\bnon-defective matrices\b', 'matrices no defectivas'),
    (r'\bnon-defective\b', 'no defectiva'),
    (r'\bsquare matrices\b', 'matrices cuadradas'),
    (r'\bsquare matrix\b', 'matriz cuadrada'),

    (r'\bLet ([^.]+?) be analytic\b', r'Sea \1 analítica'),
    (r'\bLet ([^.]+?) be\b', r'Sea \1'),
    (r'\bThe right-hand side is the \*Taylor series for\*\b', 'El lado derecho es la *serie de Taylor para*'),
    (r'\band its radius of convergence is\b', 'y su radio de convergencia es'),
    (r'\bradius of convergence\b', 'radio de convergencia'),
    (r'\bhas a \*zero of order\* \(or \*multiplicity\* \)\b', 'tiene un *cero de orden* (o *multiplicidad* )'),
    (r'\bmultiplicity\b', 'multiplicidad'),
    (r'\bIf ([^.]+?), analytic in ([^.]+?), equals\b', r'Si \1, analítica en \2, es igual a'),
    (r'\bSuppose ([^.]+?), ([^.]+?), is an arc and\b', r'Supóngase que \1, \2, es un arco y'),
    (r'\bAnalytic continuation is a powerful aid in establishing transformations or functional equations for\b', 'La continuación analítica es una herramienta poderosa para establecer transformaciones o ecuaciones funcionales para'),
    (r'\bLet ([^.]+?) be a simple closed contour consisting of a segment ([^.]+?) of the real axis and a contour\b', r'Sea \1 un contorno cerrado simple que consta de un segmento \2 del eje real y un contorno'),
    (r'\bSuppose ([^.]+?) is analytic in the \*annulus\*\b', r'Supóngase que \1 es analítica en el *anillo*'),
    (r'\band the integration contour is described once in the positive sense\b', 'y el contorno de integración se recorre una vez en sentido positivo'),
    (r'\bThe series ([^.]+?) converges uniformly\b', r'La serie \1 converge uniformemente'),
    (r'\bThe series ([^.]+?) converges\b', r'La serie \1 converge'),
    (r'\bso that the annulus becomes the \*punctured neighborhood\*\b', 'de modo que el anillo se convierte en el *entorno punteado*'),
    (r'\bThe singularities of ([^.]+?) at infinity are classified in the same way as the singularities of\b', r'Las singularidades de \1 en el infinito se clasifican de la misma manera que las singularidades de'),
    (r'\bAn isolated singularity ([^.]+?) is always removable when ([^.]+?) exists, for example\b', r'Una singularidad aislada \1 es siempre evitable cuando \2 existe, por ejemplo'),
    (r'\bThe coefficient ([^.]+?) of ([^.]+?) in the Laurent series for ([^.]+?) is called the \*residue\*\b', r'El coeficiente \1 de \2 en la serie de Laurent para \3 se llama el *residuo*'),
    (r'\bA function whose only singularities, other than the point at infinity, are poles is called a \*meromorphic function\*\b', 'Una función cuyas únicas singularidades, distintas del punto en el infinito, son polos se denomina *función meromórfica*'),
    (r'\bIn any neighborhood of an isolated essential singularity, however small, an analytic function assumes\b', 'En cualquier entorno de una singularidad esencial aislada, por pequeño que sea, una función analítica asume'),
    (r'\bIf ([^.]+?) is analytic within a simple closed contour ([^.]+?), and continuous within and on ([^.]+?) except in\b', r'Si \1 es analítica dentro de un contorno cerrado simple \2, y continua dentro y sobre \3 excepto en'),
    (r'\bsum of the residues of\b', 'suma de los residuos de'),
    (r'\bwithin\b', 'dentro de'),
    (r'\bHere and elsewhere in this subsection the path ([^.]+?) is described in the positive sense\b', r'Aquí y en otras partes de esta subsección, el camino \1 se recorre en sentido positivo'),
    (r'\bIf the singularities within ([^.]+?) are poles and ([^.]+?) is analytic and nonvanishing on ([^.]+?), then\b', r'Si las singularidades dentro de \1 son polos y \2 es analítica y no nula sobre \3, entonces'),

    # Álgebra elemental y cálculo
    (r'\bA function ([^.]+?) is \*continuous at a point\* ([^.]+?) if\b', r'Una función \1 es *continua en un punto* \2 si'),
    (r'\bA function ([^.]+?) is \*continuous on a point set\* ([^.]+?) if it is continuous at all points of ([^.]+?)\.\b', r'Una función \1 es *continua sobre un conjunto de puntos* \2 si es continua en todos los puntos de \3.'),
    (r'\bA function ([^.]+?) is \*piecewise continuous\* on ([^.]+?), where ([^.]+?) and ([^.]+?) are intervals, if it is piecewise continuous in ([^.]+?) for each ([^.]+?) and piecewise continuous in ([^.]+?) for each ([^.]+?)\.\b', r'Una función \1 es *continua a trozos* sobre \2, donde \3 y \4 son intervalos, si es continua a trozos en \5 para cada \6 y continua a trozos en \7 para cada \8.'),
    (r'\bthat is, for every arbitrarily small positive constant\b', 'es decir, para toda constante positiva arbitrariamente pequeña'),
    (r'\bthere exists\b', 'existe'),
    (r'\bfor all ([^.]+?) that satisfy\b', r'para todos los \1 que satisfacen'),
    (r'\bfor all\b', 'para todo'),
    (r'\bis continuous at a point\b', 'es continua en un punto'),
    (r'\bis continuous on a point set\b', 'es continua sobre un conjunto de puntos'),
    (r'\bis continuous at all points of\b', 'es continua en todos los puntos de'),
    (r'\bis continuous on\b', 'es continua en'),
    (r'\bis continuous in\b', 'es continua en'),
    (r'\bis continuous\b', 'es continua'),
    (r'\bis piecewise continuous in\b', 'es continua a trozos en'),
    (r'\bis piecewise continuous on\b', 'es continua a trozos sobre'),
    (r'\bis piecewise continuous\b', 'es continua a trozos'),
    (r'\bcontinuously differentiable\b', 'continuamente diferenciable'),
    (r'\btwice-continuously differentiable\b', 'dos veces continuamente diferenciable'),
    (r'\bsuch that\b', 'tal que'),
    (r'\bif it is\b', 'si es'),
    (r'\bwhere ([^.]+?) and ([^.]+?) are intervals\b', r'donde \1 y \2 son intervalos'),
    (r'\bfor each\b', 'para cada'),

    # Vocabulario de notación
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

    # Diccionario universal de palabras matemáticas individuales (último nivel)
    (r'\bFormula\b', 'La fórmula'),
    (r'\bformula\b', 'fórmula'),
    (r'\bFormulas\b', 'Las fórmulas'),
    (r'\bformulas\b', 'fórmulas'),
    (r'\bEquation\b', 'La ecuación'),
    (r'\bequation\b', 'ecuación'),
    (r'\bEquations\b', 'Las ecuaciones'),
    (r'\bequations\b', 'ecuaciones'),
    (r'\bTheorem\b', 'Teorema'),
    (r'\btheorem\b', 'teorema'),
    (r'\bProof\b', 'Demostración'),
    (r'\bproof\b', 'demostración'),
    (r'\bLemma\b', 'Lema'),
    (r'\blemma\b', 'lema'),
    (r'\bCorollary\b', 'Corolario'),
    (r'\bcorollary\b', 'corolario'),
    (r'\bDefinition\b', 'Definición'),
    (r'\bdefinition\b', 'definición'),
    (r'\bExample\b', 'Ejemplo'),
    (r'\bexample\b', 'ejemplo'),
    (r'\bRemark\b', 'Observación'),
    (r'\bremark\b', 'observación'),
    (r'\bFunction\b', 'Función'),
    (r'\bfunction\b', 'función'),
    (r'\bFunctions\b', 'Funciones'),
    (r'\bfunctions\b', 'funciones'),
    (r'\bIntegral\b', 'Integral'),
    (r'\bintegral\b', 'integral'),
    (r'\bIntegrals\b', 'Integrales'),
    (r'\bintegrals\b', 'integrales'),
    (r'\bDerivative\b', 'Derivada'),
    (r'\bderivative\b', 'derivada'),
    (r'\bDerivatives\b', 'Derivadas'),
    (r'\bderivatives\b', 'derivadas'),
    (r'\bSeries\b', 'Serie'),
    (r'\bseries\b', 'serie'),
    (r'\bExpansion\b', 'Desarrollo'),
    (r'\bexpansion\b', 'desarrollo'),
    (r'\bExpansions\b', 'Desarrollos'),
    (r'\bexpansions\b', 'desarrollos'),
    (r'\bCoefficient\b', 'Coeficiente'),
    (r'\bcoefficient\b', 'coeficiente'),
    (r'\bCoefficients\b', 'Coeficientes'),
    (r'\bcoefficients\b', 'coeficientes'),
    (r'\bMatrix\b', 'Matriz'),
    (r'\bmatrix\b', 'matriz'),
    (r'\bMatrices\b', 'Matrices'),
    (r'\bmatrices\b', 'matrices'),
    (r'\bVector\b', 'Vector'),
    (r'\bvector\b', 'vector'),
    (r'\bVectors\b', 'Vectores'),
    (r'\bvectors\b', 'vectores'),
    (r'\bOperator\b', 'Operador'),
    (r'\boperator\b', 'operador'),
    (r'\bOperators\b', 'Operadores'),
    (r'\boperators\b', 'operadores'),
    (r'\bDomain\b', 'Dominio'),
    (r'\bdomain\b', 'dominio'),
    (r'\bDomains\b', 'Dominios'),
    (r'\bdomains\b', 'dominios'),
    (r'\bInterval\b', 'Intervalo'),
    (r'\binterval\b', 'intervalo'),
    (r'\bIntervals\b', 'Intervalos'),
    (r'\bintervals\b', 'intervalos'),
    (r'\bContour\b', 'Contorno'),
    (r'\bcontour\b', 'contorno'),
    (r'\bContours\b', 'Contornos'),
    (r'\bcontours\b', 'contornos'),
    (r'\bRegion\b', 'Región'),
    (r'\bregion\b', 'región'),
    (r'\bRegions\b', 'Regiones'),
    (r'\bregions\b', 'regiones'),
    (r'\bPoint\b', 'Punto'),
    (r'\bpoint\b', 'punto'),
    (r'\bPoints\b', 'Puntos'),
    (r'\bpoints\b', 'puntos'),
    (r'\bSet\b', 'Conjunto'),
    (r'\bset\b', 'conjunto'),
    (r'\bSets\b', 'Conjuntos'),
    (r'\bsets\b', 'conjuntos'),
    (r'\bSpace\b', 'Espacio'),
    (r'\bspace\b', 'espacio'),
    (r'\bSpaces\b', 'Espacios'),
    (r'\bspaces\b', 'espacios'),
    (r'\bLimit\b', 'Límite'),
    (r'\blimit\b', 'límite'),
    (r'\bLimits\b', 'Límites'),
    (r'\blimits\b', 'límites'),
    (r'\bZero\b', 'Cero'),
    (r'\bzero\b', 'cero'),
    (r'\bZeros\b', 'Ceros'),
    (r'\bzeros\b', 'ceros'),
    (r'\bPole\b', 'Polo'),
    (r'\bpole\b', 'polo'),
    (r'\bPoles\b', 'Polos'),
    (r'\bpoles\b', 'polos'),
    (r'\bResidue\b', 'Residuo'),
    (r'\bresidue\b', 'residuo'),
    (r'\bResidues\b', 'Residuos'),
    (r'\bresidues\b', 'residuos'),

    (r'\bconverges\b', 'converge'),
    (r'\bconvergent\b', 'convergente'),
    (r'\bconvergence\b', 'convergencia'),
    (r'\bentry-wise\b', 'elemento a elemento'),
    (r'\bnorm\b', 'norma'),
    (r'\bfollows\b', 'sigue'),
    (r'\bvalid\b', 'válida'),
    (r'\bgenerally\b', 'generalmente'),
    (r'\bnecessarily\b', 'necesariamente'),
    (r'\banalytic\b', 'analítica'),
    (r'\bcontinuous\b', 'continua'),
    (r'\bdifferentiable\b', 'diferenciable'),
    (r'\bbounded\b', 'acotado'),
    (r'\bunbounded\b', 'no acotado'),
    (r'\bfinite\b', 'finito'),
    (r'\binfinite\b', 'infinito'),
    (r'\bpositive\b', 'positivo'),
    (r'\bnegative\b', 'negativo'),
    (r'\breal\b', 'real'),
    (r'\bcomplex\b', 'compleja'),
    (r'\blinear\b', 'lineal'),
    (r'\bnonlinear\b', 'no lineal'),
    (r'\brational\b', 'racional'),
    (r'\birrational\b', 'irracional'),
    (r'\balgebraic\b', 'algebraica'),
    (r'\btranscendental\b', 'trascendente'),
    (r'\buniform\b', 'uniforme'),
    (r'\buniformly\b', 'uniformemente'),
    (r'\babsolute\b', 'absoluta'),
    (r'\babsolutely\b', 'absolutamente'),

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
    (r'\bsee\b', 'véase'),
    (r'\bSee\b', 'Véase'),
    (r'\bThm\b', 'Teorema'),
]


def traducir_linea_fuente(line: str) -> str:
    """Traduce una línea de texto conservando protegidas expresiones matemáticas."""
    if line.startswith("#"):
        return line

    for pat, repl in REEMPLAZOS_PROSA:
        line = re.sub(pat, repl, line)

    return line


def traducir_archivo_seccion(orig_path: Path, dest_path: Path):
    raw = orig_path.read_text(encoding="utf-8")

    protected = []

    def mask_protected(match):
        idx = len(protected)
        token = f"___PROT_EXPR_{idx}___"
        protected.append(match.group(0))
        return token

    # Proteger expresiones math ($...$ inline y $$...$$ bloque) y enlaces bibliográficos
    # NOTA: $...$ en línea NO debe cruzar saltos de línea (\n) para evitar enmascarar prosa
    masked_text = re.sub(r'(\$\$.*?\$\$|\[[^\]\n]*?\]\(\./bib/[^)]*?\))', mask_protected, raw, flags=re.DOTALL)
    masked_text = re.sub(r'\$[^$\n]+?\$', mask_protected, masked_text)

    lines = masked_text.splitlines()
    translated_lines = [traducir_linea_fuente(line) for line in lines]
    translated_text = "\n".join(translated_lines)

    # Restaurar protegidos
    for idx, orig in enumerate(protected):
        token = f"___PROT_EXPR_{idx}___"
        translated_text = translated_text.replace(token, orig)

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(translated_text, encoding="utf-8")
    print(f"Traducido: {orig_path.name} -> {dest_path.name}")


def traducir_seccion_entera(seccion: str):
    orig_sec_dir = ORIGINAL_DIR / seccion
    dest_sec_dir = TRADUCCION_DIR / seccion

    if not orig_sec_dir.exists():
        print(f"Error: La sección original {orig_sec_dir} no existe.")
        return

    for root, _, files in os.walk(orig_sec_dir):
        for f in sorted(files):
            if f.endswith(".md"):
                orig_file = Path(root) / f
                rel_path = Path(root).relative_to(orig_sec_dir)
                dest_file = dest_sec_dir / rel_path / f
                traducir_archivo_seccion(orig_file, dest_file)

    print(f"Traducción de oraciones finalizada para la sección {seccion}.")


def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/traducir_oraciones_dlmf.py <numero_seccion>")
        sys.exit(1)

    seccion = sys.argv[1]
    traducir_seccion_entera(seccion)


if __name__ == "__main__":
    main()
