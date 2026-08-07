#!/usr/bin/env python3
"""
Script de inicialización de la estructura de traducción DLMF al español.
Lee toc.md y toc_full.md de docs/DLMF-markdown-main/markdown y genera:
- docs/DLMF_markdown_traduccion/markdown/toc_es.md
- docs/DLMF_markdown_traduccion/markdown/toc_full_es.md
- La estructura de carpetas (1 a 36) en docs/DLMF_markdown_traduccion/markdown/
- Un archivo JSON de mapeo de títulos traducidos (metadata/mapeo_titulos_dlmf.json)
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ORIGINAL_MD_DIR = BASE_DIR / "docs" / "DLMF-markdown-main" / "markdown"
TRADUCCION_MD_DIR = BASE_DIR / "docs" / "DLMF_markdown_traduccion" / "markdown"
METADATA_DIR = BASE_DIR / "metadata"

# Diccionario oficial de traducción de capítulos
CAPITULOS_TRADUCCION = {
    "1 - Algebraic and Analytic Methods": "1 - Métodos Algebraicos y Analíticos",
    "2 - Asymptotic Approximations": "2 - Aproximaciones Asintóticas",
    "3 - Numerical Methods": "3 - Métodos Numéricos",
    "4 - Elementary Functions": "4 - Funciones Elementales",
    "5 - Gamma Function": "5 - Función Gamma",
    "6 - Exponential, Logarithmic, Sine, and Cosine Integrals": "6 - Integrales Exponenciales, Logarítmicas, Seno y Coseno",
    "7 - Error Functions, Dawson’s and Fresnel Integrals": "7 - Funciones de Error e Integrales de Dawson y Fresnel",
    "8 - Incomplete Gamma and Related Functions": "8 - Función Gamma Incompleta y Funciones Relacionadas",
    "9 - Airy and Related Functions": "9 - Funciones de Airy y Relacionadas",
    "10 - Bessel Functions": "10 - Funciones de Bessel",
    "11 - Struve and Related Functions": "11 - Funciones de Struve y Relacionadas",
    "12 - Parabolic Cylinder Functions": "12 - Funciones del Cilindro Parabólico",
    "13 - Confluent Hypergeometric Functions": "13 - Funciones Hipergeométricas Confluyentes",
    "14 - Legendre and Related Functions": "14 - Funciones de Legendre y Relacionadas",
    "15 - Hypergeometric Function": "15 - Función Hipergeométrica",
    "16 - Generalized Hypergeometric Functions and Meijer G-Function": "16 - Funciones Hipergeométricas Generalizadas y Función G de Meijer",
    "17 - q-Hypergeometric and Related Functions": "17 - Funciones q-Hipergeométricas y Relacionadas",
    "18 - Orthogonal Polynomials": "18 - Polinomios Ortogonales",
    "19 - Elliptic Integrals": "19 - Integrales Elípticas",
    "20 - Theta Functions": "20 - Funciones Theta",
    "21 - Multidimensional Theta Functions": "21 - Funciones Theta Multidimensionales",
    "22 - Jacobian Elliptic Functions": "22 - Funciones Elípticas Jacobianas",
    "23 - Weierstrass Elliptic and Modular Functions": "23 - Funciones Elípticas y Modulares de Weierstrass",
    "24 - Bernoulli and Euler Polynomials": "24 - Polinomios de Bernoulli y Euler",
    "25 - Zeta and Related Functions": "25 - Funciones Zeta y Relacionadas",
    "26 - Combinatorial Analysis": "26 - Análisis Combinatorio",
    "27 - Functions of Number Theory": "27 - Funciones de Teoría de Números",
    "28 - Mathieu Functions and Hill’s Equation": "28 - Funciones de Mathieu y Ecuación de Hill",
    "29 - Lamé Functions": "29 - Funciones de Lamé",
    "30 - Spheroidal Wave Functions": "30 - Funciones de Onda Esferoidales",
    "31 - Heun Functions": "31 - Funciones de Heun",
    "32 - Painlevé Transcendents": "32 - Trascendentes de Painlevé",
    "33 - Coulomb Functions": "33 - Funciones de Coulomb",
    "34 - 3⁢j,6⁢j,9⁢j Symbols": "34 - Símbolos 3j, 6j, 9j",
    "35 - Functions of Matrix Argument": "35 - Funciones de Argumento Matricial",
    "36 - Integrals with Coalescing Saddles": "36 - Integrales con Puntos de Silla Coalescentes"
}

# Subsecciones comunes
SUBSECCIONES_TRADUCCION = {
    "Notation": "Notación",
    "Topics of Discussion": "Temas de Discusión",
    "Areas": "Áreas",
    "Properties": "Propiedades",
    "Applications": "Aplicaciones",
    "Computation": "Cálculo Computacional"
}


def generar_toc_es():
    """Genera toc_es.md a partir de toc.md."""
    toc_orig = ORIGINAL_MD_DIR / "toc.md"
    if not toc_orig.exists():
        print(f"Error: No existe {toc_orig}")
        return

    lines = toc_orig.read_text(encoding="utf-8").splitlines()
    new_lines = ["# Tabla de Contenidos", ""]

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("- "):
            item = stripped[2:].strip()
            item_tr = CAPITULOS_TRADUCCION.get(item, item)
            new_lines.append(f"- {item_tr}")
        elif stripped and not stripped.startswith("#"):
            new_lines.append(line)

    toc_es_file = TRADUCCION_MD_DIR / "toc_es.md"
    TRADUCCION_MD_DIR.mkdir(parents=True, exist_ok=True)
    toc_es_file.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    print(f"Creado: {toc_es_file}")


def generar_toc_full_es():
    """Genera toc_full_es.md traduciendo títulos de capítulos y secciones."""
    toc_full_orig = ORIGINAL_MD_DIR / "toc_full.md"
    if not toc_full_orig.exists():
        print(f"Error: No existe {toc_full_orig}")
        return

    lines = toc_full_orig.read_text(encoding="utf-8").splitlines()
    new_lines = ["# Tabla de Contenidos Completa", ""]

    for line in lines:
        # Reemplazar encabezados principales
        if line.startswith("- ") and not line.startswith("  - "):
            cap = line[2:].strip()
            cap_tr = CAPITULOS_TRADUCCION.get(cap, cap)
            new_lines.append(f"- {cap_tr}")
        elif "**" in line:
            # Subsecciones tipo **Notation** -> **Notación**
            line_tr = line
            for en, es in SUBSECCIONES_TRADUCCION.items():
                line_tr = line_tr.replace(f"**{en}**", f"**{es}**")
            new_lines.append(line_tr)
        else:
            new_lines.append(line)

    toc_full_es_file = TRADUCCION_MD_DIR / "toc_full_es.md"
    toc_full_es_file.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    print(f"Creado: {toc_full_es_file}")


def crear_estructura_carpetas():
    """Crea los subdirectorios 1 a 36 en docs/DLMF_markdown_traduccion/markdown/."""
    for i in range(1, 37):
        cap_dir = TRADUCCION_MD_DIR / str(i)
        cap_dir.mkdir(parents=True, exist_ok=True)
    print("Estructura de 36 carpetas de capítulos creada en:", TRADUCCION_MD_DIR)


def main():
    generar_toc_es()
    generar_toc_full_es()
    crear_estructura_carpetas()
    print("\nInicialización de infraestructura de traducción completada con éxito.")


if __name__ == "__main__":
    main()
