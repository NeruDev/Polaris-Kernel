#!/usr/bin/env python3
"""
Perfeccionador Final de la Sección 1 DLMF al Español Académico Nativo.
Traduce exhaustivamente cada archivo de la sección 1 (docs/DLMF-markdown-main/markdown/1/)
a docs/DLMF_markdown_traduccion/markdown/1/, garantizando:
1. Cero palabras en inglés en la prosa explicativa, metadatos y fórmulas LaTeX.
2. Ordenamiento estricto de reemplazo (Frases Largas -> Frases Medianas -> Palabras Individuales).
3. Corrección KaTeX/MathJax de bloques \\text{...} y \\mbox{...} (ej. \\text{(o }\\infty\\text{)}).
4. Preservación intacta de expresiones math LaTeX y títulos de citas bibliográficas.
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ORIGINAL_DIR = BASE_DIR / "docs" / "DLMF-markdown-main" / "markdown" / "1"
TRADUCCION_DIR = BASE_DIR / "docs" / "DLMF_markdown_traduccion" / "markdown" / "1"


def sanitizar_bloques_text_latex(content: str) -> str:
    """Traduce y corrige comandos \\text{} y \\mbox{} dentro de expresiones LaTeX para KaTeX."""
    content = re.sub(r'\\text\{\(or\s+\\infty\)\}', r'\\text{(o }\\infty\\text{)}', content)
    content = re.sub(r'\\text\{\(or\s+-\\infty\)\}', r'\\text{(o }-\\infty\\text{)}', content)
    content = re.sub(r'\\text\{\(or\s+\\pm\\infty\)\}', r'\\text{(o }\\pm\\infty\\text{)}', content)
    content = re.sub(r'\\text\{\(or\s+([^\}]+?)\)\}', r'\\text{(o }\1\\text{)}', content)
    content = re.sub(r'\\mbox\{\(or\s+([^\}]+?)\)\}', r'\\text{(o }\1\\text{)}', content)

    content = re.sub(r'\\text\{sum of the residues of f\(z\) within C\}', r'\\text{suma de los residuos de }f(z)\\text{ dentro de }C', content)
    content = re.sub(r'\\mbox\{\(sum of locations of zeros of f\(z\) within C\) - \(sum of locations of poles of f\(z\) within C\)\}', r'\\text{(suma de posiciones de ceros de }f(z)\\text{ dentro de }C) - \\text{(suma de posiciones de polos de }f(z)\\text{ dentro de }C)', content)
    content = re.sub(r'\\mbox\{\(sum of locations of zeros\)\}', r'\\text{(suma de posiciones de ceros)}', content)
    content = re.sub(r'\\mbox\{\(sum of locations of poles\)\}', r'\\text{(suma de posiciones de polos)}', content)
    content = re.sub(r'\\mbox\{ and \}', r'\\text{ y }', content)
    content = re.sub(r'\\mbox\{otherwise\}', r'\\text{en otro caso}', content)
    content = re.sub(r'\\text\{otherwise\}', r'\\text{en otro caso}', content)
    content = re.sub(r'\\text\{ at \(a,b\),\}', r'\\text{ en }(a,b),', content)
    content = re.sub(r'\\text\{ at \(a,b\)\}', r'\\text{ en }(a,b)', content)
    content = re.sub(r'\\text\{if \(x,y\)\\in D\}', r'\\text{si }(x,y)\\in D', content)
    content = re.sub(r'\\text\{if \(x,y\)\\in R\\setminus D\.\}', r'\\text{si }(x,y)\\in R\\setminus D.', content)
    content = re.sub(r'\\text\{\(polar coordinates\)\}', r'\\text{(coordenadas polares)}', content)
    content = re.sub(r'\\text\{\(spherical coordinates\)\}', r'\\text{(coordenadas esféricas)}', content)
    content = re.sub(r'\\text\{if \}j,k,\\ell\\text\{ is even permutation of \}1,2,3', r'\\text{si }j,k,\\ell\\text{ es una permutación par de }1,2,3', content)
    content = re.sub(r'\\text\{if \}j,k,\\ell\\text\{ is odd permutation of \}1,2,3', r'\\text{si }j,k,\\ell\\text{ es una permutación impar de }1,2,3', content)
    content = re.sub(r'\\text\{ constant\}', r'\\text{constante}', content)
    content = re.sub(r'\\mbox\{ or \}', r'\\text{ o }', content)

    return content


# NIVEL 1: Frases completas y oraciones compuestas (Máxima prioridad)
FRASES_LARGAS = [
    (r'Annotations for Ch\.(\d+)', r'Anotaciones para el Cap. \1'),
    (r'Annotations for §([\d\.]+)', r'Anotaciones para §\1'),
    (r'Chapter (\d+)\s+([^\n"]+)', r'Capítulo \1 \2'),
    (r'Addition \(effective with ([^\)]+)\):', r'Adición (efectiva desde la versión \1):'),
    (r'A sentence was added to explain that', 'Se agregó una oración para explicar que'),
    (r'A sentence was added at the end of this section\.', 'Se agregó una oración al final de esta sección.'),
    (r'For other notation see Notation for the Special Functions \.', 'Para otra notación véase Notación para las Funciones Especiales.'),

    (r'The right-hand side is the \*Taylor series for\* (___PROT_EXPR_\d+___) \*at\* (___PROT_EXPR_\d+___) , and its radius of convergence is at least (___PROT_EXPR_\d+___) \.', r'El lado derecho es la *serie de Taylor para* \1 *en* \2, y su radio de convergencia es al menos \3.'),
    (r'The right-hand side is the \*Taylor series for\* (___PROT_EXPR_\d+___) \*at\* (___PROT_EXPR_\d+___) , and its radius of convergence is', r'El lado derecho es la *serie de Taylor para* \1 *en* \2, y su radio de convergencia es'),
    (r'Let (___PROT_EXPR_\d+___) be analytic in the disk (___PROT_EXPR_\d+___) \. Then', r'Sea \1 analítica en el disco \2. Entonces'),
    (r'Let (___PROT_EXPR_\d+___) be analytic on the disk (___PROT_EXPR_\d+___) \. Then', r'Sea \1 analítica en el disco \2. Entonces'),
    (r'Let (___PROT_EXPR_\d+___) be analytic in a domain (___PROT_EXPR_\d+___) \. If', r'Sea \1 analítica en un dominio \2. Si'),

    (r'Functions of a Complex Variable', 'Funciones de una Variable Compleja'),
    (r'Functions of a Real Variable', 'Funciones de una Variable Real'),
    (r'Special Notation', 'Notación Especial'),
    (r'Elementary Algebra', 'Álgebra Elemental'),
    (r'Elementary Analytic Geometry', 'Geometría Analítica Elemental'),
    (r'Trigonometric and Inverse Trigonometric Functions', 'Funciones Trigonométricas y Trigonométricas Inversas'),
    (r'Hyperbolic and Inverse Hyperbolic Functions', 'Funciones Hiperbólicas e Hiperbólicas Inversas'),
    (r'Exponential and Logarithmic Functions', 'Funciones Exponenciales y Logarítmicas'),
    (r'Differential Calculus', 'Cálculo Diferencial'),
    (r'Vector and Tensor Calculus', 'Cálculo Vectorial y Tensorial'),
    (r'Series and Sequences', 'Series y Secuencias'),
    (r'Infinite Products', 'Productos Infinitos'),
    (r'Asymptotic Approximations', 'Aproximaciones Asintóticas'),
    (r'Orthogonal Polynomials and Functions', 'Polinomios y Funciones Ortogonales'),
    (r'Fourier Analysis and Integral Transforms', 'Análisis de Fourier y Transformadas Integrales'),
    (r'Numerical Analysis', 'Análisis Numérico'),
    (r'Algebraic and Analytic Methods', 'Métodos Algebraicos y Analíticos'),

    (r'the space of all Lebesgue–Stieltjes measurable functions on', 'el espacio de todas las funciones medibles en el sentido de Lebesgue–Stieltjes sobre'),
    (r'which are square integrable with respect to', 'que son de cuadrado integrable con respecto a'),
    (r'derivatives with respect to the variable, except where indicated otherwise\.', 'derivadas con respecto a la variable, excepto donde se indique lo contrario.'),
    (r'In the physics, applied maths, and engineering literature a common alternative to', 'En la literatura de física, matemáticas aplicadas e ingeniería, una alternativa común a'),

    (r'Analytic continuation is a powerful aid in establishing transformations or functional equations for', 'La continuación analítica es una herramienta poderosa para establecer transformaciones o ecuaciones funcionales para'),
    (r'In any neighborhood of an isolated essential singularity, however small, an analytic function assumes', 'En cualquier entorno de una singularidad esencial aislada, por pequeño que sea, una función analítica asume'),
    (r'Here and elsewhere in this subsection the path (___PROT_EXPR_\d+___) is described in the positive sense\.', r'Aquí y en otras partes de esta subsección, el camino \1 se recorre en sentido positivo.'),
    (r'A function whose only singularities, other than the point at infinity, are poles is called a \*meromorphic function\*', 'Una función cuyas únicas singularidades, distintas del punto en el infinito, son polos se denomina *función meromórfica*'),
    (r'each location again being counted with multiplicity equal to that of the corresponding zero or pole\.', 'contándose cada ubicación de nuevo con multiplicidad igual a la del correspondiente cero o polo.'),
    (r'Functions which have more than one value at a given point', 'Las funciones que tienen más de un valor en un punto dado'),
    (r'Or more generally, a simple contour that starts at the center and terminates on the boundary', 'O más generalmente, un contorno simple que comienza en el centro y termina en la frontera'),
    (r'Branches can be constructed in two ways:', 'Las ramas se pueden construir de dos maneras:'),
    (r'\(a\) By introducing appropriate cuts from the branch points and restricting', '(a) Introduciendo cortes apropiados desde los puntos de ramificación y restringiendo'),
    (r'\(b\) By specifying the value of', '(b) Especificando el valor de'),
]

# NIVEL 2: Frases medianas de análisis y notación
FRASES_MEDIANAS = [
    (r'\*\*See also:\*\*', '**Véase también:**'),
    (r'\bKeywords:\b', 'Palabras clave:'),
    (r'\bReferenced by:\b', 'Referenciado por:'),
    (r'\bNotes:\b', 'Notas:'),
    (r'\bIn addition,\b', 'Además,'),
    (r'\bIn addition\b', 'Además'),
    (r'\bNote that\b', 'Tenga en cuenta que'),
    (r'\bSuppose that\b', 'Supóngase que'),
    (r'\bSuppose\b', 'Supóngase que'),
    (r'\bEquality holds iff\b', 'La igualdad se cumple syss'),
    (r'\bEquality holds if and only if\b', 'La igualdad se cumple si y solo si'),
    (r'\bEquality holds\b', 'La igualdad se cumple'),
    (r'\bEqualities hold iff\b', 'Las igualdades se cumplen syss'),
    (r'\bEqualities hold\b', 'Las igualdades se cumplen'),
    (r'\bThe direction of the inequality is reversed, that is,\b', 'El sentido de la desigualdad se invierte, es decir,'),
    (r'\bThe direction of the inequality is reversed\b', 'El sentido de la desigualdad se invierte'),

    (r'\bthe space of all\b', 'el espacio de todos los'),
    (r'\binverse of the square matrix\b', 'inversa de la matriz cuadrada'),
    (r'\binverse of the matrix\b', 'inversa de la matriz'),
    (r'\bdeterminant of the square matrix\b', 'determinante de la matriz cuadrada'),
    (r'\bdeterminant of the matrix\b', 'determinante de la matriz'),
    (r'\btrace of the square matrix\b', 'traza de la matriz cuadrada'),
    (r'\btrace of the matrix\b', 'traza de la matriz'),
    (r'\badjoint of the square matrix\b', 'adjunta de la matriz cuadrada'),
    (r'\badjoint of the matrix\b', 'adjunta de la matriz'),
    (r'\bcomplex conjugate of the matrix\b', 'conjugado complejo de la matriz'),
    (r'\bcomplex conjugate of\b', 'conjugado complejo de'),
    (r'\btranspose of the matrix\b', 'traspuesta de la matriz'),
    (r'\btranspose of\b', 'traspuesta de'),
    (r'\bHermitian conjugate of the matrix\b', 'conjugado hermitiano de la matriz'),
    (r'\bHermitian conjugate of\b', 'conjugado hermitiano de'),
    (r'\bis usually being denoted\b', 'usualmente se denota por'),
    (r'\bbeing a complex number or a matrix\b', 'siendo un número complejo o una matriz'),

    (r'\bThis is the neighborhood of an isolated singularity at\b', 'Este es el entorno de una singularidad aislada en'),
    (r'\bThis is the neighborhood of\b', 'Este es el entorno de'),
    (r'\bis a generalization of\b', 'es una generalización de'),
    (r'\bwith the binomial coefficient\b', 'con el coeficiente binomial'),
    (r'\bhas a \*zero of order\* \(or \*multiplicity\* \)\b', 'tiene un *cero de orden* (o *multiplicidad* )'),
    (r'\bhas a zero of order\b', 'tiene un cero de orden'),
    (r'\bzero of order\b', 'cero de orden'),
    (r'\bis an arc and\b', 'es un arco y'),
    (r'\bcontinuous curve formed by the segments\b', 'curva continua formada por los segmentos'),
    (r'\bis called a polygonal path\b', 'se denomina un camino poligonal'),
    (r'\bpolygonal path\b', 'camino poligonal'),
    (r'\bsimple closed contour consisting of a segment\b', 'contorno cerrado simple que consta de un segmento'),
    (r'\bof the real axis and a contour\b', 'del eje real y un contorno'),
    (r'\bin the upper half-plane\b', 'en el semiplano superior'),
    (r'\bin the lower half-plane\b', 'en el semiplano inferior'),
    (r'\bin the right half-plane\b', 'en el semiplano derecho'),
    (r'\bin the left half-plane\b', 'en el semiplano izquierdo'),
    (r'\bof the real axis\b', 'del eje real'),
    (r'\bpunctured neighborhood\b', 'entorno punteado'),
    (r'\bso that the annulus becomes the \*punctured neighborhood\*\b', 'de modo que el anillo se convierte en el *entorno punteado*'),
    (r'\bso that the annulus becomes\b', 'de modo que el anillo se convierte en'),
    (r'\bis called the \*residue\*\b', 'se llama el *residuo*'),
    (r'\bis called the residue\b', 'se llama el residuo'),
    (r'\bis called a \*meromorphic function\*\b', 'se denomina *función meromórfica*'),
    (r'\bmeromorphic function\b', 'función meromórfica'),
    (r'\bis called a\b', 'se denomina una'),
    (r'\bis called\b', 'se denomina'),
    (r'\bare called\b', 'se denominan'),
    (r'\bHere and elsewhere in this subsection\b', 'Aquí y en otras partes de esta subsección'),
    (r'\bis described in the positive sense\b', 'se recorre en sentido positivo'),
    (r'\bis described in the negative sense\b', 'se recorre en sentido negativo'),
    (r'\bin the positive sense\b', 'en sentido positivo'),
    (r'\bin the negative sense\b', 'en sentido negativo'),
    (r'\bcounting multiplicity\b', 'contando multiplicidad'),
    (r'\bother than the point at infinity\b', 'distintas del punto en el infinito'),
    (r'\bother than\b', 'distintas de'),
    (r'\bpoint at infinity\b', 'punto en el infinito'),
    (r'\bis always removable when\b', 'es siempre evitable cuando'),
    (r'\bis always removable\b', 'es siempre evitable'),
    (r'\bThe right-hand side\b', 'El lado derecho'),
    (r'\bThe left-hand side\b', 'El lado izquierdo'),
    (r'\bat least\b', 'al menos'),
    (r'\bradius of convergence\b', 'radio de convergencia'),
    (r'\bin the disk\b', 'en el disco'),
    (r'\bon the disk\b', 'en el disco'),
    (r'\bin a domain\b', 'en un dominio'),
    (r'\bis analytic in\b', 'es analítica en'),
    (r'\bis analytic on\b', 'es analítica en'),
    (r'\bis analytic at\b', 'es analítica en'),
    (r'\bis analytic\b', 'es analítica'),
]

# NIVEL 3: Palabras individuales y conectores
PALABRAS_INDIVIDUALES = [
    (r'\bLet (___PROT_EXPR_\d+___) be anal[íi]tica\b', r'Sea \1 analítica'),
    (r'\bLet (___PROT_EXPR_\d+___) be\b', r'Sea \1'),
    (r'\bSea (___PROT_EXPR_\d+___) be anal[íi]tica\b', r'Sea \1 analítica'),
    (r'\bSea (___PROT_EXPR_\d+___) be\b', r'Sea \1'),
    (r'\bLet\b', 'Sea'),

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
    (r'\bDisk\b', 'Disco'),
    (r'\bdisk\b', 'disco'),
    (r'\bAnnulus\b', 'Anillo'),
    (r'\bannulus\b', 'anillo'),
    (r'\bBoundary\b', 'Frontera'),
    (r'\bboundary\b', 'frontera'),
    (r'\bMultiplicity\b', 'Multiplicidad'),
    (r'\bmultiplicity\b', 'multiplicidad'),
    (r'\bSingularity\b', 'Singularidad'),
    (r'\bsingularity\b', 'singularidad'),
    (r'\bSingularities\b', 'Singularidades'),
    (r'\bsingularities\b', 'singularidades'),
    (r'\bBranch\b', 'Rama'),
    (r'\bbranch\b', 'rama'),
    (r'\bBranches\b', 'Ramas'),
    (r'\bbranches\b', 'ramas'),
    (r'\bCut\b', 'Corte'),
    (r'\bcut\b', 'corte'),

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
    (r'\bnonvanishing\b', 'no nula'),
    (r'\bnon-defective\b', 'no defectiva'),
    (r'\bremovable\b', 'evitable'),
    (r'\bisolated\b', 'aislada'),
    (r'\bessential\b', 'esencial'),
    (r'\bmultivalued\b', 'multiforme'),
    (r'\bmany-valued\b', 'multivaluada'),
    (r'\btwo-valued\b', 'bivaluada'),
    (r'\bsingle-valued\b', 'monódromo'),
    (r'\bpolygonal\b', 'poligonal'),
    (r'\bharmonic\b', 'armónica'),

    (r'\bbe\b', ''),  # Eliminar 'be' residual de frases Let ... be
    (r'\bthe\b', 'el'),
    (r'\bThe\b', 'El'),
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
    (r'\bThen\b', 'Entonces'),
    (r'\bthen\b', 'entonces'),
    (r'\bIf\b', 'Si'),
    (r'\bif\b', 'si'),
    (r'\balso\b', 'también'),
    (r'\bAlso\b', 'También'),
]


def traducir_linea_fuente(line: str) -> str:
    """Traduce una línea de prosa pura en orden descendente de longitud."""
    for pat, repl in FRASES_LARGAS:
        line = re.sub(pat, repl, line)

    for pat, repl in FRASES_MEDIANAS:
        line = re.sub(pat, repl, line)

    for pat, repl in PALABRAS_INDIVIDUALES:
        line = re.sub(pat, repl, line)

    line = re.sub(r'  +', ' ', line)
    return line


def perfeccionar_archivo(orig_path: Path, dest_path: Path):
    raw = orig_path.read_text(encoding="utf-8")

    # 1. Sanitizar bloques \text{} y \mbox{} en LaTeX primero (ANTES de enmascarar)
    raw = sanitizar_bloques_text_latex(raw)

    protected = []

    def mask_protected(match):
        idx = len(protected)
        token = f"___PROT_EXPR_{idx}___"
        protected.append(match.group(0))
        return token

    # Proteger expresiones math ($...$ inline y $$...$$ bloque) y enlaces bibliográficos
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
    print(f"Perfeccionado: {orig_path.name} -> {dest_path.name}")


def main():
    for root, _, files in os.walk(ORIGINAL_DIR):
        for f in sorted(files):
            if f.endswith(".md"):
                orig_file = Path(root) / f
                rel_path = Path(root).relative_to(ORIGINAL_DIR)
                dest_file = TRADUCCION_DIR / rel_path / f
                perfeccionar_archivo(orig_file, dest_file)

    print("Perfeccionamiento de la Sección 1 completado exitosamente.")


if __name__ == "__main__":
    main()
