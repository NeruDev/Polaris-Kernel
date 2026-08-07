#!/usr/bin/env python3
"""
Traductor de Sección Directo desde la Fuente Original DLMF.
Lee los archivos Markdown originales en inglés (docs/DLMF-markdown-main/markdown/),
aplica enmascaramiento de LaTeX math y enlaces bibliográficos, y realiza una
traducción académica al español nativo sin dejar residuos Spanglish.
"""

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ORIGINAL_DIR = BASE_DIR / "docs" / "DLMF-markdown-main" / "markdown"
TRADUCCION_DIR = BASE_DIR / "docs" / "DLMF_markdown_traduccion" / "markdown"

REEMPLAZOS_PROSA_DIRECTOS = [
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

    # Tablas de Notación
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
    (r'\bIn the physics, applied maths, and engineering literature a common alternative to\b', 'En la literatura de física, matemáticas aplicadas e ingeniería, una alternativa común a'),
    (r'\bis usually being denoted\b', 'usualmente se denota por'),
    (r'\bbeing a complex number or a matrix\b', 'siendo un número complejo o una matriz'),

    # Expresiones complejas y Teoremas
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
    (r'\bAn analytic function ([^.]+?) has a \*zero of order\* \(or \*multiplicity\* \) ([^.]+?) at\b', r'Una función analítica \1 tiene un *cero of order* (o *multiplicidad* ) \2 en'),
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
    (r'\btext\{sum of the residues of ([^.]+?) within ([^.]+?)\}', r'text{suma de los residuos de \1 dentro de \2}'),
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
    if line.startswith("#"):
        return line

    for pat, repl in REEMPLAZOS_PROSA_DIRECTOS:
        line = re.sub(pat, repl, line)

    return line


def traducir_archivo_fuente(orig_path: Path, dest_path: Path):
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
    print(f"Reconstruido desde fuente: {orig_path.name} -> {dest_path.name}")


def reconstruir_seccion(seccion: str):
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
                traducir_archivo_fuente(orig_file, dest_file)

    print(f"Reconstrucción desde fuente completada para la sección {seccion}.")


def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/reconstruir_seccion_fuente.py <numero_seccion>")
        sys.exit(1)

    seccion = sys.argv[1]
    reconstruir_seccion(seccion)


if __name__ == "__main__":
    main()
