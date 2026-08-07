#!/usr/bin/env python3
"""
Glosario matemático de referencia en español para la traducción de la DLMF.
Contiene los términos matemáticos estandarizados verificados mediante literatura académica (AMS, SMM, NIST).
"""

GLOSARIO_MATEMATICO = {
    # Capítulo 1: Métodos Algebraicos y Analíticos
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

    # Términos técnicos frecuentes
    "real variables": "variables reales",
    "complex variable": "variable compleja",
    "nonnegative integers": "enteros no negativos",
    "inner, or scalar, product": "producto interno o escalar",
    "derivatives with respect to": "derivadas con respecto a",
    "column vectors": "vectores columna",
    "identity matrix": "matriz identidad",
    "determinant of the square matrix": "determinante de la matriz cuadrada",
    "trace of the square matrix": "traza de la matriz cuadrada",
    "adjoint of the square matrix": "adjunta de la matriz cuadrada",
    "complex conjugate": "conjugado complejo",
    "transpose of the matrix": "traspuesta de la matriz",
    "Hermitian conjugate": "conjugado hermitiano",
    "linear operator": "operador lineal",
    "dual manifold": "variedad dual",
    "Schwarzian derivative": "derivada schwarziana",
    "Fourier cosine transform": "transformada de Fourier en coseno",
    "Fourier sine transform": "transformada de Fourier en seno",
    "Hilbert transform": "transformada de Hilbert",
    "Heaviside function": "función de Heaviside",
    "Dirac delta distribution": "distribución delta de Dirac",
    "Cauchy principal value": "valor principal de Cauchy",
    "binomial coefficient": "coeficiente binomial",
    "weighted mean": "media ponderada",
    "arithmetic mean": "media aritmética",
    "harmonic mean": "media armónica",
    "continuously differentiable": "continuamente diferenciable",
    "half-closed interval": "intervalo semiabierto",
    "open interval": "intervalo abierto",
    "closed interval": "intervalo cerrado"
}


def buscar_termino(term: str) -> str:
    """Devuelve la traducción estándar del término matemático si existe en el glosario."""
    return GLOSARIO_MATEMATICO.get(term, term)
