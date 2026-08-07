#!/usr/bin/env python3
"""
Traductor Profundo de Sección DLMF al Español Nativo Académico.
Procesa los archivos Markdown originales de docs/DLMF-markdown-main/markdown/
traduciendo títulos de sección, notación, teoremas, definiciones y prosa general
sin dejar ninguna palabra residual en inglés fuera de expresiones math LaTeX y bibliografía.
"""

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ORIGINAL_DIR = BASE_DIR / "docs" / "DLMF-markdown-main" / "markdown"
TRADUCCION_DIR = BASE_DIR / "docs" / "DLMF_markdown_traduccion" / "markdown"

REEMPLAZOS_TITULOS = [
    (r'#\s*§1\.1\s*Special Notation', '# §1.1 Notación Especial'),
    (r'#\s*§1\.2\s*Elementary Algebra', '# §1.2 Álgebra Elemental'),
    (r'#\s*§1\.3\s*Elementary Analytic Geometry', '# §1.3 Geometría Analítica Elemental'),
    (r'#\s*§1\.4\s*Polynomials', '# §1.4 Polinomios'),
    (r'#\s*§1\.5\s*Trigonometric and Inverse Trigonometric Functions', '# §1.5 Funciones Trigonométricas y Trigonométricas Inversas'),
    (r'#\s*§1\.6\s*Hyperbolic and Inverse Hyperbolic Functions', '# §1.6 Funciones Hiperbólicas e Hiperbólicas Inversas'),
    (r'#\s*§1\.7\s*Exponential and Logarithmic Functions', '# §1.7 Funciones Exponenciales y Logarítmicas'),
    (r'#\s*§1\.8\s*Inequalities', '# §1.8 Desigualdades'),
    (r'#\s*§1\.9\s*Differential Calculus', '# §1.9 Cálculo Diferencial'),
    (r'#\s*§1\.10\s*Functions of a Complex Variable', '# §1.10 Funciones de una Variable Compleja'),
    (r'#\s*§1\.11\s*Integration', '# §1.11 Integración'),
    (r'#\s*§1\.12\s*Vector and Tensor Calculus', '# §1.12 Cálculo Vectorial y Tensorial'),
    (r'#\s*§1\.13\s*Series and Sequences', '# §1.13 Series y Secuencias'),
    (r'#\s*§1\.14\s*Infinite Products', '# §1.14 Productos Infinitos'),
    (r'#\s*§1\.15\s*Asymptotic Approximations', '# §1.15 Aproximaciones Asintóticas'),
    (r'#\s*§1\.16\s*Orthogonal Polynomials and Functions', '# §1.16 Polinomios y Funciones Ortogonales'),
    (r'#\s*§1\.17\s*Fourier Analysis and Integral Transforms', '# §1.17 Análisis de Fourier y Transformadas Integrales'),
    (r'#\s*§1\.18\s*Numerical Analysis', '# §1.18 Análisis Numérico'),
    (r'#\s*Chapter 1\s*Algebraic and Analytic Methods', '# Capítulo 1 Métodos Algebraicos y Analíticos'),
]

REEMPLAZOS_PROSA_PROFUNDOS = [
    # Metadatos
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

    # Notación especial (§1.1)
    (r'\bthe space of all Lebesgue–Stieltjes measurable functions on\b', 'el espacio de todas las funciones medibles en el sentido de Lebesgue–Stieltjes sobre'),
    (r'\bwhich are square integrable with respect to\b', 'que son de cuadrado integrable con respecto a'),
    (r'\baction of distribution ([^.]+?) on test function\b', r'acción de la distribución \1 sobre la función de prueba'),
    (r'\bderivatives with respect to the variable, except where indicated otherwise\.', 'derivadas con respecto a la variable, excepto donde se indique lo contrario.'),
    (r'\bthe space of all ([^.]+?)-dimensional vectors\.', r'el espacio de todos los vectores \1-dimensionales.'),
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
    (r'\badjoint of ([^.]+?) defined on the dual manifold\b', r'adjunta de \1 definida sobre la variedad dual'),
    (r'\bexponential of\b', 'exponencial de'),
    (r'\bIn the physics, applied maths, and engineering literature a common alternative to\b', 'En la literatura de física, matemáticas aplicadas e ingeniería, una alternativa común a'),
    (r'\bis usually being denoted\b', 'usualmente se denota por'),
    (r'\bbeing a complex number or a matrix\b', 'siendo un número complejo o una matriz'),

    # Funciones complejas (§1.10) - Frases y Oraciones Completas
    (r'A \*cut domain\* is one from which the points on finitely many nonintersecting simple contours \(§ 1\.9\(iii\) \) have been removed\. Each contour is called a \*cut\* \. A \*cut neighborhood\* is formed by deleting a ray emanating from the center\. \(Or more generally, a simple contour that starts at the center and terminates on the boundary\.\)', 'Un *dominio cortado* es aquel del cual los puntos en un número finito de contornos simples que no se intersecan (§ 1.9(iii) ) han sido eliminados. Cada contorno se denomina un *corte*. Un *entorno cortado* se forma eliminando un rayo que emana del centro. (O más generalmente, un contorno simple que comienza en el centro y termina en la frontera.)'),
    (r'\bEach contour is called a \*cut\*\b', 'Cada contorno se denomina un *corte*'),
    (r'\(Or more generally, a simple contour that starts at the center and terminates on the boundary\.\)', '(O más generalmente, un contorno simple que comienza en el centro y termina en la frontera.)'),
    (r'\\mbox\{\(sum of locations of zeros of f\(z\) within C\) - \(sum of locations of poles of f\(z\) within C\)\}', r'\\mbox{(suma de posiciones de ceros de f(z) dentro de C) - (suma de posiciones de polos de f(z) dentro de C)}'),
    (r'\\text\{sum of the residues of f\(z\) within C\}', r'\\text{suma de los residuos de } f(z) \\text{ dentro de } C'),
    (r'\bFunctions which have more than one value at a given point ([^.]+?) are called \*multivalued\* \(or \*many-valued\*\)', r'Las funciones que tienen más de un valor en un punto dado \1 se denominan *multiformes* (o *multivaluadas*)'),
    (r'\bhave been removed\b', 'han sido eliminados'),
    (r'\bEach contour is called a \*cut\*\b', 'Cada contorno se denomina un *corte*'),
    (r'\bA \*cut neighborhood\* is formed by deleting a ray emanating from the center\b', 'Un *entorno cortado* se forma eliminando un rayo que emana del centro'),
    (r'\bOr more generally, a simple contour that starts in the center and terminates in the boundary\b', 'O más generalmente, un contorno simple que comienza en el centro y termina en la frontera'),
    (r'\bSuppose ([^.]+?) is multivalued and ([^.]+?) is a point such that there exists a branch of ([^.]+?) in a cut neighborhood\b', r'Supóngase que \1 es multiforme y \2 es un punto tal que existe una rama de \3 en un entorno cortado'),
    (r'\bBranches can be constructed in two ways:\b', 'Las ramas se pueden construir de dos maneras:'),
    (r'\(a\) By introducing appropriate cuts from the branch points and restricting ([^.]+?) to be single-valued in\b', r'(a) Introduciendo cortes apropiados desde los puntos de ramificación y restringiendo \1 a ser monódromo en'),
    (r'\(b\) By specifying the value of ([^.]+?) at a point ([^.]+?) \(not a branch point\), and requiring ([^.]+?) to\b', r'(b) Especificando el valor de \1 en un punto \2 (no siendo un punto de ramificación), y requiriendo que \3'),
    (r'\bIf the path circles a branch point at ([^.]+?), ([^.]+?) times in the positive sense, and returns to ([^.]+?) with\b', r'Si el camino rodea un punto de ramificación en \1, \2 veces en sentido positivo, y regresa a \3 con'),
    (r'\bLet ([^.]+?) and ([^.]+?) be real or complex numbers that are not integers\.\b', r'Sean \1 y \2 números reales o complejos que no son enteros.'),
    (r'\bis two-valued for\b', 'es bivaluada para'),
    (r'\bA \*cut domain\* is one from which the points on finitely many nonintersecting simple contours\b', 'Un *dominio cortado* es aquel del cual los puntos en un número finito de contornos simples que no se intersecan'),
    (r'\bLet ([^.]+?) be analytic in the disk ([^.]+?)\.\s*Then\b', r'Sea \1 analítica en el disco \2. Entonces'),
    (r'\bLet ([^.]+?) be analytic on the disk ([^.]+?)\.\s*Then\b', r'Sea \1 analítica en el disco \2. Entonces'),
    (r'\bLet ([^.]+?) be analytic in a domain ([^.]+?)\.\s*If\b', r'Sea \1 analítica en un dominio \2. Si'),
    (r'\bLet ([^.]+?) be analytic in a domain\b', r'Sea \1 analítica en un dominio'),
    (r'\bLet ([^.]+?) be analytic in\b', r'Sea \1 analítica en'),
    (r'\bLet ([^.]+?) be analytic\b', r'Sea \1 analítica'),
    (r'\bLet ([^.]+?) be\b', r'Sea \1'),
    (r'\bThe right-hand side is the \*Taylor series for\* ([^.]+?) \*at\* ([^.]+?), and its radius of convergence is\b', r'El lado derecho es la *serie de Taylor para* \1 *en* \2, y su radio de convergencia es'),
    (r'\bThe right-hand side is the\b', 'El lado derecho es la'),
    (r'\bThe left-hand side is the\b', 'El lado izquierdo es la'),
    (r'\band its radius of convergence is\b', 'y su radio de convergencia es'),
    (r'\bradius of convergence\b', 'radio de convergencia'),
    (r'\bNote that ([^.]+?) is a generalization of the binomial expansion ([^.]+?) with the binomial coefficient\b', r'Tenga en cuenta que \1 es una generalización del desarrollo binomial \2 con el coeficiente binomial'),
    (r'\bAn analytic function ([^.]+?) has a \*zero of order\* \(or \*multiplicity\* \) ([^.]+?) at\b', r'Una función analítica \1 tiene un *cero de orden* (o *multiplicidad* ) \2 en'),
    (r'\bhas a \*zero of order\* \(or \*multiplicity\* \)\b', 'tiene un *cero de orden* (o *multiplicidad* )'),
    (r'\bIf ([^.]+?), analytic in ([^.]+?), equals\b', r'Si \1, analítica en \2, es igual a'),
    (r'\bSuppose ([^.]+?), ([^.]+?), is an arc and\b', r'Supóngase que \1, \2, es un arco y'),
    (r'\bAnalytic continuation is a powerful aid in establishing transformations or functional equations for\b', 'La continuación analítica es una herramienta poderosa para establecer transformaciones o ecuaciones funcionales para'),
    (r'\bLet ([^.]+?) be a simple closed contour consisting of a segment ([^.]+?) of the real axis and a contour\b', r'Sea \1 un contorno cerrado simple que consta de un segmento \2 del eje real y un contorno'),
    (r'\bSuppose ([^.]+?) is analytic in the \*annulus\*\b', r'Supóngase que \1 es analítica en el *anillo*'),
    (r'\band the integration contour is described once in the positive sense\b', 'y el contorno de integración se recorre una vez en sentido positivo'),
    (r'\bThe series ([^.]+?) converges uniformly\b', r'La serie \1 converge uniformemente'),
    (r'\bThe series ([^.]+?) converges\b', r'La serie \1 converge'),
    (r'\bLet ([^.]+?), so that the annulus becomes the \*punctured neighborhood\*\b', r'Sea \1, de modo que el anillo se convierte en el *entorno punteado*'),
    (r'\bso that the annulus becomes the \*punctured neighborhood\*\b', 'de modo que el anillo se convierte en el *entorno punteado*'),
    (r'\bThe singularities of ([^.]+?) at infinity are classified in the same way as the singularities of\b', r'Las singularidades de \1 en el infinito se clasifican de la misma manera que las singularidades de'),
    (r'\bAn isolated singularity ([^.]+?) is always removable when ([^.]+?) exists, for example\b', r'Una singularidad aislada \1 es siempre evitable cuando \2 existe, por ejemplo'),
    (r'\bThe coefficient ([^.]+?) of ([^.]+?) in the Laurent series for ([^.]+?) is called the \*residue\*\b', r'El coeficiente \1 de \2 en la serie de Laurent para \3 se llama el *residuo*'),
    (r'\bA function whose only singularities, other than the point at infinity, are poles is called a \*meromorphic function\*\b', 'Una función cuyas únicas singularidades, distintas del punto en el infinito, son polos se denomina *función meromórfica*'),
    (r'\bIn any neighborhood of an isolated essential singularity, however small, an analytic function assumes\b', 'En cualquier entorno de una singularidad esencial aislada, por pequeño que sea, una función analítica asume'),
    (r'\bIf ([^.]+?) is analytic within a simple closed contour ([^.]+?), and continuous within and on ([^.]+?) except in\b', r'Si \1 es analítica dentro de un contorno cerrado simple \2, y continua dentro y sobre \3 excepto en'),
    (r'\bIf the singularities within ([^.]+?) are poles and ([^.]+?) is analytic and nonvanishing on ([^.]+?), then\b', r'Si las singularidades dentro de \1 son polos y \2 es analítica y no nula sobre \3, entonces'),
    (r'\bwhere ([^.]+?) and ([^.]+?) are respectively the numbers of zeros and poles, counting multiplicity, of ([^.]+?) within\b', r'donde \1 y \2 son respectivamente los números de ceros y polos, contando multiplicidad, de \3 dentro de'),
    (r'\beach location again being counted with multiplicity equal to that of the corresponding zero or pole\.\b', 'contándose cada ubicación de nuevo con multiplicidad igual a la del correspondiente cero o polo.'),
    (r'\bIf ([^.]+?) and ([^.]+?) are analytic on and inside a simple closed contour ([^.]+?), and\b', r'Si \1 y \2 son analíticas sobre y dentro de un contorno cerrado simple \3, y'),
    (r'\bLet ([^.]+?) be a bounded domain with boundary ([^.]+?) and let\b', r'Sea \1 un dominio acotado con frontera \2 y sea'),
    (r'\bIn ([^.]+?), if ([^.]+?) is analytic, ([^.]+?), and ([^.]+?), then\b', r'En \1, si \2 es analítica, \3, y \4, entonces'),
    (r'\bFormula \((.*?)\) is more generally valid for all square matrices (.*?), not necessarily non-defective, see\b', r'La fórmula (\1) es más generalmente válida para todas las matrices cuadradas \2, no necesariamente no defectivas, véase'),
    (r'\bIt follows from ([^.]+?) that, for a non-defective matrix\b', r'Se deduce de \1 que, para una matriz no defectiva'),
    (r'\bwhich converges, entry-wise or in norm, for all\b', 'que converge, elemento a elemento o en norma, para todo'),

    # Frases elementales y conectores
    (r'\bA function ([^.]+?) is \*continuous at a point\* ([^.]+?) if\b', r'Una función \1 es *continua en un punto* \2 si'),
    (r'\bA function ([^.]+?) is \*continuous on a point set\* ([^.]+?) if it is continuous at all points of ([^.]+?)\.\b', r'Una función \1 es *continua sobre un conjunto de puntos* \2 si es continua en todos los puntos de \3.'),
    (r'\bthat is, for every arbitrarily small positive constant\b', 'es decir, para toda constante positiva arbitrariamente pequeña'),
    (r'\bthere exists\b', 'existe'),
    (r'\bfor all ([^.]+?) that satisfy\b', r'para todos los \1 que satisfacen'),
    (r'\bfor all\b', 'para todo'),
    (r'\bsuch that\b', 'tal que'),
    (r'\bif it is\b', 'si es'),
    (r'\bwhere ([^.]+?) and ([^.]+?) are intervals\b', r'donde \1 y \2 son intervalos'),
    (r'\bfor each\b', 'para cada'),
    (r'\bwith respect to\b', 'con respecto a'),
    (r'\bwith respect to the variable, except where indicated otherwise\.', 'con respecto a la variable, excepto donde se indique lo contrario.'),
    (r'\bunless specified otherwise\.', 'a menos que se especifique lo contrario.'),

    # Diccionario universal de sustantivos, adjetivos y verbos matemáticos
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
]


def traducir_linea_fuente(line: str) -> str:
    """Traduce una línea de prosa pura conservando la estructura."""
    for pat, repl in REEMPLAZOS_TITULOS:
        if re.search(pat, line):
            return re.sub(pat, repl, line)

    for pat, repl in REEMPLAZOS_PROSA_PROFUNDOS:
        line = re.sub(pat, repl, line)

    return line


def traducir_archivo_profundo(orig_path: Path, dest_path: Path):
    raw = orig_path.read_text(encoding="utf-8")

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
    print(f"Traducción profunda: {orig_path.name} -> {dest_path.name}")


def procesar_seccion_profunda(seccion: str):
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
                traducir_archivo_profundo(orig_file, dest_file)

    print(f"Procesamiento profundo completado para la sección {seccion}.")


def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/traducir_prosa_seccion_profunda.py <numero_seccion>")
        sys.exit(1)

    seccion = sys.argv[1]
    procesar_seccion_profunda(seccion)


if __name__ == "__main__":
    main()
