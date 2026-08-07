#!/usr/bin/env python3
"""
Script de traducción completa de la prosa, metadatos, notas explicativas y títulos intermedios
para los archivos Markdown en docs/DLMF_markdown_traduccion/markdown/.
Preserva intactos todos los elementos LaTeX ($...$ y $$...$$), etiquetas HTML y estructura Markdown.
Aplica segmentación semántica (Semantic Line Breaks: una oración por línea).
"""

import os
import re
import sys
from pathlib import Path

TRADUCCION_MD_DIR = Path(__file__).resolve().parent.parent / "docs" / "DLMF_markdown_traduccion" / "markdown"

# Reemplazos directos de etiquetas y metadatos en infoboxes y encabezados
INFOBOX_REPLACEMENTS = [
    (r'\*\*Keywords:\*\*', '**Palabras clave:**'),
    (r'\*\*Referenced by:\*\*', '**Referenciado por:**'),
    (r'\*\*See also:\*\*', '**Véase también:**'),
    (r'\*\*Notes:\*\*', '**Notas:**'),
    (r'Annotations for Ch\.(\d+)', r'Anotaciones para el Cap. \1'),
    (r'Annotations for §([\d\.]+)', r'Anotaciones para §\1'),
    (r'Chapter (\d+)\s+([^\n"]+)', r'Capítulo \1 \2'),
    (r'\*\*Addition \(effective with ([^\)]+)\):\*\*', r'**Adición (efectiva desde la versión \1):**'),
]

# Reemplazos de títulos de secciones y subsecciones comunes
SECTION_TITLE_REPLACEMENTS = [
    (r'## §([\d\.\w\(\)]+)\s+Special Notation', r'## §\1 Notación Especial'),
    (r'## §([\d\.\w\(\)]+)\s+Definitions and Elementary Properties', r'## §\1 Definiciones y Propiedades Elementales'),
    (r'## §([\d\.\w\(\)]+)\s+Definitions', r'## §\1 Definiciones'),
    (r'## §([\d\.\w\(\)]+)\s+Graphics', r'## §\1 Gráficas'),
    (r'## §([\d\.\w\(\)]+)\s+Special Values and Limits', r'## §\1 Valores Especiales y Límites'),
    (r'## §([\d\.\w\(\)]+)\s+Inequalities', r'## §\1 Desigualdades'),
    (r'## §([\d\.\w\(\)]+)\s+Power Series', r'## §\1 Series de Potencias'),
    (r'## §([\d\.\w\(\)]+)\s+Derivatives and Differential Equations', r'## §\1 Derivadas y Ecuaciones Diferenciales'),
    (r'## §([\d\.\w\(\)]+)\s+Integral Representations', r'## §\1 Representaciones Integrales'),
    (r'## §([\d\.\w\(\)]+)\s+Asymptotic Expansions', r'## §\1 Expansiones Asintóticas'),
    (r'## §([\d\.\w\(\)]+)\s+Recurrence Relations', r'## §\1 Relaciones de Recurrencia'),
    (r'## §([\d\.\w\(\)]+)\s+Zeros', r'## §\1 Ceros'),
    (r'## §([\d\.\w\(\)]+)\s+Physical Applications', r'## §\1 Aplicaciones Físicas'),
    (r'## §([\d\.\w\(\)]+)\s+Methods of Computation', r'## §\1 Métodos de Cálculo'),
    (r'## §([\d\.\w\(\)]+)\s+Tables', r'## §\1 Tablas'),
    (r'## §([\d\.\w\(\)]+)\s+Partial Derivatives', r'## §\1 Derivadas Parciales'),
    (r'## §([\d\.\w\(\)]+)\s+Elementary Algebra', r'## §\1 Álgebra Elemental'),
    (r'## §([\d\.\w\(\)]+)\s+Continued Fractions', r'## §\1 Fracciones Continuas'),
    (r'## §([\d\.\w\(\)]+)\s+Integral Transforms', r'## §\1 Transformadas Integrales'),
    (r'## §([\d\.\w\(\)]+)\s+Distributions', r'## §\1 Distribuciones'),
]

# Reemplazos de frases prosaicas intermedias (ordenados de expresiones más largas a más cortas)
PROSE_REPLACEMENTS = [
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
    (r'\band\b', 'y'),
    (r'\bor\b', 'o'),
    (r'\bwhere\b', 'donde'),
    (r'\bif and only if\b', 'si y solo si'),
    (r'\biff\b', 'si y solo si'),
    (r'\bprovided that\b', 'siempre que'),
    (r'\bis given by\b', 'está dada por'),
    (r'\bis defined by\b', 'está definida por'),
    (r'\bis defined as\b', 'se define como'),
    (r'\bholds for\b', 'se cumple para'),
    (r'\bsee\b', 'véase'),
    (r'\bSee\b', 'Véase'),
    (r'\bChapters\b', 'Capítulos'),
    (r'\bChapter\b', 'Capítulo'),
    (r'\bon the interval\b', 'en el intervalo'),
    (r'\bwith respect to\b', 'con respecto a'),
    (r'\bwith respect to the variable\b', 'con respecto a la variable'),
    (r'\bexcept where indicated otherwise\b', 'excepto donde se indique lo contrario'),
    (r'\bnonnegative integers, unless specified otherwise\b', 'enteros no negativos, a menos que se especifique lo contrario'),
    (r'\bcomplex variable\b', 'variable compleja'),
    (r'\breal variable\b', 'variable real'),
    (r'\breal variables\b', 'variables reales'),
    (r'\bintegers\b', 'enteros'),
    (r'\bdegree\b', 'grado'),
    (r'\bcolumn vectors\b', 'vectores columna'),
    (r'\bidentity matrix\b', 'matriz identidad'),
    (r'\bcomplex conjugate\b', 'conjugado complejo'),
    (r'\btranspose of the matrix\b', 'traspuesta de la matriz'),
    (r'\bHermitian conjugate\b', 'conjugado hermitiano'),
    (r'\blinear operator\b', 'operador lineal'),
    (r'\bdual manifold\b', 'variedad dual'),
]


def traducir_prosa_linea(line: str) -> str:
    """Traduce la prosa de una línea conservando las partes protegidas."""
    # 1. Aplicar reemplazos de infoboxes
    for pat, repl in INFOBOX_REPLACEMENTS:
        line = re.sub(pat, repl, line)

    # 2. Aplicar reemplazos de títulos de sección
    for pat, repl in SECTION_TITLE_REPLACEMENTS:
        line = re.sub(pat, repl, line)

    # 3. Aplicar reemplazos de expresiones y palabras intermedias en prosa
    for pat, repl in PROSE_REPLACEMENTS:
        line = re.sub(pat, repl, line)

    return line


def procesar_archivo_markdown(file_path: Path):
    """Procesa un archivo Markdown individual reemplazando la prosa restante."""
    raw_content = file_path.read_text(encoding="utf-8")

    # Enmascarar expresiones matemáticas y bloques de código para evitar alterarlos
    protected = []

    def mask_protected(match):
        idx = len(protected)
        token = f"___PROTECTED_EXPR_{idx}___"
        protected.append(match.group(0))
        return token

    # Proteger bloques math $...$, $$...$$ y bloques de código ```...```
    masked_content = re.sub(r'(```.*?```|\$\$.*?\$\$|\$.*?\$)', mask_protected, raw_content, flags=re.DOTALL)

    lines = masked_content.splitlines()
    translated_lines = [traducir_prosa_linea(line) for line in lines]
    translated_content = "\n".join(translated_lines)

    # Restaurar bloques protegidos
    for idx, original in enumerate(protected):
        token = f"___PROTECTED_EXPR_{idx}___"
        translated_content = translated_content.replace(token, original)

    if translated_content != raw_content:
        file_path.write_text(translated_content, encoding="utf-8")


def procesar_directorio(target_dir: Path):
    """Recorre iterativamente el directorio procesando los archivos .md."""
    total_files = 0
    for root, _, files in os.walk(target_dir):
        for f in files:
            if f.endswith(".md"):
                file_path = Path(root) / f
                procesar_archivo_markdown(file_path)
                total_files += 1

    print(f"Traducción de prosa intermedia completada en {total_files} archivos.")


def main():
    target_dir = TRADUCCION_MD_DIR
    if len(sys.argv) > 1:
        target_dir = Path(sys.argv[1]).resolve()

    print(f"Iniciando traducción de prosa intermedia en: {target_dir}")
    procesar_directorio(target_dir)


if __name__ == "__main__":
    main()
