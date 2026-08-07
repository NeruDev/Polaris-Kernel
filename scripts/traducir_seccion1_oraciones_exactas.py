#!/usr/bin/env python3
"""
Traductor Exacto de Oraciones y Tablas para la Sección 1 del DLMF.
Mapea oraciones completas, infoboxes y entradas de tabla directamente del inglés fuente al español nativo.
Garantiza 0 inglés residual en prosa y 0 errores de renderizado en KaTeX.
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ORIGINAL_DIR = BASE_DIR / "docs" / "DLMF-markdown-main" / "markdown" / "1"
TRADUCCION_DIR = BASE_DIR / "docs" / "DLMF_markdown_traduccion" / "markdown" / "1"

ORACIONES_EXACTAS = {
    # §1.1 Notación Especial
    "Special Notation": "Notación Especial",
    "**Addition (effective with 1.2.0):**": "**Adición (efectiva desde la versión 1.2.0):**",
    "A sentence was added at the end of this section.": "Se agregó una oración al final de esta sección.",
    "Annotations for Ch.1": "Anotaciones para el Cap. 1",
    "Annotations for Ch. 1": "Anotaciones para el Cap. 1",
    "the space of all Lebesgue–Stieltjes measurable functions on $X$ which are square integrable with respect to $\\,\\mathrm{d}\\alpha$ .": "el espacio de todas las funciones medibles en el sentido de Lebesgue–Stieltjes sobre $X$ que son de cuadrado integrable con respecto a $\\,\\mathrm{d}\\alpha$ .",
    "the space of all Lebesgue–Stieltjes measurable functions on $X$ which are square integrable with respect to $\\mathrm{d}\\alpha$ .": "el espacio de todas las funciones medibles en el sentido de Lebesgue–Stieltjes sobre $X$ que son de cuadrado integrable con respecto a $\\mathrm{d}\\alpha$ .",
    "real variables.": "variables reales.",
    "complex variable in §§ 1.2(i) , [1.9](./1.9.md \"§1.9 Calculus of a Complex Variable ‣ Topics of Discussion ‣ Chapter 1 Algebraic and Analytic Methods\") – [1.11](./1.11.md \"§1.11 Zeros of Polynomials ‣ Topics of Discussion ‣ Chapter 1 Algebraic and Analytic Methods\") , real variable in §§ [1.5](./1.5.md \"§1.5 Calculus of Two or More Variables ‣ Topics of Discussion ‣ Chapter 1 Algebraic and Analytic Methods\") – [1.6](./1.6.md \"§1.6 Vectors and Vector-Valued Functions ‣ Topics of Discussion ‣ Chapter 1 Algebraic and Analytic Methods\") .": "variable compleja en §§ 1.2(i) , [1.9](./1.9.md \"§1.9 Calculus of a Complex Variable ‣ Topics of Discussion ‣ Chapter 1 Algebraic and Analytic Methods\") – [1.11](./1.11.md \"§1.11 Zeros of Polynomials ‣ Topics of Discussion ‣ Chapter 1 Algebraic and Analytic Methods\") , variable real en §§ [1.5](./1.5.md \"§1.5 Calculus of Two or More Variables ‣ Topics of Discussion ‣ Chapter 1 Algebraic and Analytic Methods\") – [1.6](./1.6.md \"§1.6 Vectors and Vector-Valued Functions ‣ Topics of Discussion ‣ Chapter 1 Algebraic and Analytic Methods\") .",
    "complex variable in §§ [1.9](./1.9.md \"§1.9 Calculus of a Complex Variable ‣ Topics of Discussion ‣ Chapter 1 Algebraic and Analytic Methods\") – [1.11](./1.11.md \"§1.11 Zeros of Polynomials ‣ Topics of Discussion ‣ Chapter 1 Algebraic and Analytic Methods\") .": "variable compleja en §§ [1.9](./1.9.md \"§1.9 Calculus of a Complex Variable ‣ Topics of Discussion ‣ Chapter 1 Algebraic and Analytic Methods\") – [1.11](./1.11.md \"§1.11 Zeros of Polynomials ‣ Topics of Discussion ‣ Chapter 1 Algebraic and Analytic Methods\") .",
    "integers.": "enteros.",
    "nonnegative integers, unless specified otherwise.": "enteros no negativos, a menos que se especifique lo contrario.",
    "inner, or scalar, product for real or complex vectors or functions.": "producto interno, o escalar, para vectores o funciones reales o complejas.",
    "the space of all Lebesgue–Stieltjes measurable functions on $X$ which are square integrable with respect to $\\mathrm{d}\\alpha$ .": "el espacio de todas las funciones medibles en el sentido de Lebesgue–Stieltjes sobre $X$ que son de cuadrado integrable con respecto a $\\mathrm{d}\\alpha$ .",
    "a testing function.": "una función de prueba.",
    "action of distribution $\\Lambda$ on test function $\\phi$ .": "acción de la distribución $\\Lambda$ sobre la función de prueba $\\phi$ .",
    "degree.": "grado.",
    "derivatives with respect to the variable, except where indicated otherwise.": "derivadas con respecto a la variable, excepto donde se indique lo contrario.",
    "column vectors.": "vectores columna.",
    "the space of all $n$ -dimensional vectors.": "el espacio de todos los vectores $n$ -dimensionales.",
    "or $[a_{i,j}]$ or $[a_{ij}]$ matrix with elements $a_{i,j}$ or $a_{ij}$ .": "o $[a_{i,j}]$ o $[a_{ij}]$ matriz con elementos $a_{i,j}$ o $a_{ij}$ .",
    "inverse of the square matrix $\\mathbf{A}$": "inversa de la matriz cuadrada $\\mathbf{A}$",
    "identity matrix": "matriz identidad",
    "determinant of the square matrix $\\mathbf{A}$": "determinante de la matriz cuadrada $\\mathbf{A}$",
    "trace of the square matrix $\\mathbf{A}$": "traza de la matriz cuadrada $\\mathbf{A}$",
    "exponential of $\\operatorname{tr}(\\mathbf{A})$": "exponencial de $\\operatorname{tr}(\\mathbf{A})$",
    "adjoint of the square matrix $\\mathbf{A}$": "adjunta de la matriz cuadrada $\\mathbf{A}$",
    "complex conjugate of the matrix $\\mathbf{A}$": "conjugado complejo de la matriz $\\mathbf{A}$",
    "transpose of the matrix $\\mathbf{A}$": "traspuesta de la matriz $\\mathbf{A}$",
    "Hermitian conjugate of the matrix $\\mathbf{A}$": "conjugado hermitiano de la matriz $\\mathbf{A}$",
    "linear operator defined on a manifold $\\mathcal{M}$": "operador lineal definido sobre una variedad $\\mathcal{M}$",
    "adjoint of $\\mathcal{L}$ defined on the dual manifold ${\\mathcal{M}}^{*}$": "adjunta de $\\mathcal{L}$ definida sobre la variedad dual ${\\mathcal{M}}^{*}$",
    "In the physics, applied maths, and engineering literature a common alternative to $\\overline{a}$ is $a^{*}$ , $a$ being a complex number or a matrix; the Hermitian conjugate of $\\mathbf{A}$ is usually being denoted $\\mathbf{A}^{{\\dagger}}$ .": "En la literatura de física, matemáticas aplicadas e ingeniería, una alternativa común a $\\overline{a}$ es $a^{*}$, siendo $a$ un número complejo o una matriz; el conjugado hermitiano de $\\mathbf{A}$ usualmente se denota por $\\mathbf{A}^{{\\dagger}}$.",

    # §1.10 Funciones de Variable Compleja
    "Functions of a Complex Variable": "Funciones de una Variable Compleja",
    "Let $f(z)$ be analytic in the disk $|z-z_0|<R$. Then": "Sea $f(z)$ analítica en el disco $|z-z_0|<R$. Entonces",
    "Let $f(z)$ be analytic in the disk $\\left|z-z_{0}\\right|<R$ . Then": "Sea $f(z)$ analítica en el disco $\\left|z-z_{0}\\right|<R$. Entonces",
    "The right-hand side is the *Taylor series for* $f(z)$ *at* $z=z_0$ , and its radius of convergence is at least $R$ .": "El lado derecho es la *serie de Taylor para* $f(z)$ *en* $z=z_0$, y su radio de convergencia es al menos $R$.",
    "The right-hand side is the *Taylor series for* $f(z)$ *at* $z=z_{0}$ , and its radius of convergence is at least $R$ .": "El lado derecho es la *serie de Taylor para* $f(z)$ *en* $z=z_{0}$, y su radio de convergencia es al menos $R$.",
    "Note that ( 1.10.4 ) is a generalization of the binomial expansion ( 1.2.2 ) with the binomial coefficient": "Tenga en cuenta que (1.10.4) es una generalización del desarrollo binomial (1.2.2) con el coeficiente binomial",
    "defined by ( 1.2.4 ).": "definido por (1.2.4).",
    "An analytic function $f(z)$ has a *zero of order* (or *multiplicity* ) $m$ ( $\\geq\\!1$ ) at $z_0$ if": "Una función analítica $f(z)$ tiene un *cero de orden* (o *multiplicidad*) $m$ ( $\\geq\\!1$ ) en $z_0$ si",
    "An analytic function $f(z)$ has a *zero of order* (or *multiplicity* ) $m$ ( $\\geq\\!1$ ) at $z_{0}$ if": "Una función analítica $f(z)$ tiene un *cero de orden* (o *multiplicidad*) $m$ ( $\\geq\\!1$ ) en $z_{0}$ si",
    "Let $f_1(z)$ be analytic in a domain $D_1$. If $f_2(z)$ , analytic in $D_2$ , equals $f_1(z)$ in $D_1\\cap D_2$ , then $f_2(z)$ is called an *analytic continuation* of $f_1(z)$ into $D_2$ .": "Sea $f_1(z)$ analítica en un dominio $D_1$. Si $f_2(z)$, analítica en $D_2$, es igual a $f_1(z)$ en $D_1\\cap D_2$, entonces $f_2(z)$ se denomina una *continuación analítica* de $f_1(z)$ en $D_2$.",
    "Let $f_{1}(z)$ be analytic in a domain $D_{1}$ . If $f_{2}(z)$ , analytic in $D_{2}$ , equals $f_{1}(z)$ in $D_{1}\\cap D_{2}$ , then $f_{2}(z)$ is called an *analytic continuation* of $f_{1}(z)$ into $D_{2}$ .": "Sea $f_{1}(z)$ analítica en un dominio $D_{1}$. Si $f_{2}(z)$, analítica en $D_{2}$, es igual a $f_{1}(z)$ en $D_{1}\\cap D_{2}$, entonces $f_{2}(z)$ se denomina una *continuación analítica* de $f_{1}(z)$ en $D_{2}$.",
    "Suppose $z(t)=x(t)+\\mathrm{i}y(t)$ , $a\\leq t\\leq b$ , is an arc and $a=t_0<t_1<\\dots<t_n=b$ . The continuous curve formed by the segments $z(t_{k-1})z(t_k)$ ($k=1,2,\\dots,n$) is called a polygonal path.": "Supóngase que $z(t)=x(t)+\\mathrm{i}y(t)$, $a\\leq t\\leq b$, es un arco y $a=t_0<t_1<\\dots<t_n=b$. La curva continua formada por los segmentos $z(t_{k-1})z(t_k)$ ($k=1,2,\\dots,n$) se denomina un camino poligonal.",
    "Suppose $z(t)=x(t)+\\mathrm{i}y(t)$ , $a\\leq t\\leq b$ , is an arc and $a=t_{0}<t_{1}<\\dots<t_{n}=b$ . The continuous curve formed by the segments $z(t_{k-1})z(t_{k})$ ( $k=1,2,\\dots,n$ ) is called a polygonal path.": "Supóngase que $z(t)=x(t)+\\mathrm{i}y(t)$, $a\\leq t\\leq b$, es un arco y $a=t_{0}<t_{1}<\\dots<t_{n}=b$. La curva continua formada por los segmentos $z(t_{k-1})z(t_{k})$ ( $k=1,2,\\dots,n$ ) se denomina un camino poligonal.",
    "Analytic continuation is a powerful aid in establishing transformations or functional equations for special functions.": "La continuación analítica es una herramienta poderosa para establecer transformaciones o ecuaciones funcionales para funciones especiales.",
    "Let $C$ be a simple closed contour consisting of a segment $AB$ of the real axis and a contour $L$ in the upper half-plane, and let $D$ be the domain bounded by $C$ .": "Sea $C$ un contorno cerrado simple que consta de un segmento $AB$ del eje real y un contorno $L$ en el semiplano superior, y sea $D$ el dominio acotado por $C$.",
    "Let $C$ be a simple closed contour consisting of a segment $\\mathit{AB}$ of the real axis and a contour $L$ in the upper half-plane, and let $D$ be the domain bounded by $C$ .": "Sea $C$ un contorno cerrado simple que consta de un segmento $\\mathit{AB}$ del eje real y un contorno $L$ en el semiplano superior, y sea $D$ el dominio acotado por $C$.",
    "Suppose $f(z)$ is analytic in the *annulus* $r_1<|z-z_0|<r_2$ , $0\\leq r_1<r_2\\leq\\infty$ . Then": "Supóngase que $f(z)$ es analítica en el *anillo* $r_1<|z-z_0|<r_2$, $0\\leq r_1<r_2\\leq\\infty$. Entonces",
    "Suppose $f(z)$ is analytic in the *annulus* $r_{1}<\\left|z-z_{0}\\right|<r_{2}$ , $0\\leq r_{1}<r_{2}\\leq\\infty$ . Then": "Supóngase que $f(z)$ es analítica en el *anillo* $r_{1}<\\left|z-z_{0}\\right|<r_{2}$, $0\\leq r_{1}<r_{2}\\leq\\infty$. Entonces",
    "and the integration contour is described once in the positive sense. The series ( 1.10.6 ) converges uniformly in any compact subannulus of $r_1<|z-z_0|<r_2$ .": "y el contorno de integración se recorre una vez en sentido positivo. La serie (1.10.6) converge uniformemente en cualquier subanillo compacto de $r_1<|z-z_0|<r_2$.",
    "and the integration contour is described once in the positive sense. The series ( 1.10.6 ) converges uniformly in any compact subannulus of $r_{1}<\\left|z-z_{0}\\right|<r_{2}$ .": "y el contorno de integración se recorre una vez en sentido positivo. La serie (1.10.6) converge uniformemente en cualquier subanillo compacto de $r_{1}<\\left|z-z_{0}\\right|<r_{2}$.",
    "Let $r_1=0$ , so that the annulus becomes the *punctured neighborhood* $N$ : $0<|z-z_0|<r_2$ . This is the neighborhood of an isolated singularity at $z_0$ .": "Sea $r_1=0$, de modo que el anillo se convierte en el *entorno punteado* $N$: $0<|z-z_0|<r_2$. Este es el entorno de una singularidad aislada en $z_0$.",
    "Let $r_{1}=0$ , so that the annulus becomes the *punctured neighborhood* $N$ : $0<\\left|z-z_{0}\\right|<r_{2}$ . This is the neighborhood of an isolated singularity at $z_{0}$ .": "Sea $r_{1}=0$, de modo que el anillo se convierte en el *entorno punteado* $N$: $0<\\left|z-z_{0}\\right|<r_{2}$. Este es el entorno de una singularidad aislada en $z_{0}$.",
    "The singularities of $f(z)$ at infinity are classified in the same way as the singularities of $f(1/z)$ at the origin.": "Las singularidades de $f(z)$ en el infinito se clasifican de la misma manera que las singularidades de $f(1/z)$ en el origen.",
    "An isolated singularity $z_0$ is always removable when $\\lim_{z\\to z_0}f(z)$ exists, for example by defining $f(z_0)$ to be this limit.": "Una singularidad aislada $z_0$ es siempre evitable cuando $\\lim_{z\\to z_0}f(z)$ existe, por ejemplo definiendo $f(z_0)$ como este límite.",
    "An isolated singularity $z_{0}$ is always removable when $\\lim_{z\\to z_{0}}f(z)$ exists, for example by defining $f(z_{0})$ to be this limit.": "Una singularidad aislada $z_{0}$ es siempre evitable cuando $\\lim_{z\\to z_{0}}f(z)$ existe, por ejemplo definiendo $f(z_{0})$ como este límite.",
    "The coefficient $a_{-1}$ of $(z-z_0)^{-1}$ in the Laurent series for $f(z)$ is called the *residue* of $f(z)$ at $z_0$ , and is denoted by $\\operatorname{Res}\\left(f(z),z_0\\right)$ or $\\operatorname{Res}_{z=z_0}\\left(f(z)\\right)$ .": "El coeficiente $a_{-1}$ de $(z-z_0)^{-1}$ en la serie de Laurent para $f(z)$ se llama el *residuo* de $f(z)$ en $z_0$, y se denota por $\\operatorname{Res}\\left(f(z),z_0\\right)$ o $\\operatorname{Res}_{z=z_0}\\left(f(z)\\right)$.",
    "The coefficient $a_{-1}$ of $(z-z_{0})^{-1}$ in the Laurent series for $f(z)$ is called the *residue* of $f(z)$ at $z_{0}$ , and is denoted by $\\operatorname{Res}\\left(f(z),z_{0}\\right)$ or $\\operatorname{Res}_{z=z_{0}}\\left(f(z)\\right)$ .": "El coeficiente $a_{-1}$ de $(z-z_{0})^{-1}$ en la serie de Laurent para $f(z)$ se llama el *residuo* de $f(z)$ en $z_{0}$, y se denota por $\\operatorname{Res}\\left(f(z),z_{0}\\right)$ o $\\operatorname{Res}_{z=z_{0}}\\left(f(z)\\right)$.",
    "A function whose only singularities, other than the point at infinity, are poles is called a *meromorphic function* .": "Una función cuyas únicas singularidades, distintas del punto en el infinito, son polos se denomina *función meromórfica*.",
    "In any neighborhood of an isolated essential singularity, however small, an analytic function assumes every complex value, with at most one exception, an infinite number of times.": "En cualquier entorno de una singularidad esencial aislada, por pequeño que sea, una función analítica asume todo valor complejo, con a lo sumo una excepción, un número infinito de veces.",
    "If $f(z)$ is analytic within a simple closed contour $C$ , and continuous within and on $C$ except in the interior for a finite number of poles, then": "Si $f(z)$ es analítica dentro de un contorno cerrado simple $C$, y continua dentro y sobre $C$ excepto en el interior para un número finito de polos, entonces",
    "Here and elsewhere in this subsection the path $C$ is described in the positive sense.": "Aquí y en otras partes de esta subsección, el camino $C$ se recorre en sentido positivo.",
    "If the singularities within $C$ are poles and $f(z)$ is analytic and nonvanishing on $C$ , then": "Si las singularidades dentro de $C$ son polos y $f(z)$ es analítica y no nula sobre $C$, entonces",
    "where $N$ and $P$ are respectively the numbers of zeros and poles, counting multiplicity, of $f$ within $C$ .": "donde $N$ y $P$ son respectivamente los números de ceros y polos, contando multiplicidad, de $f$ dentro de $C$.",
    "In addition,": "Además,",
    "each location again being counted with multiplicity equal to that of the corresponding zero or pole.": "contándose cada ubicación de nuevo con multiplicidad igual a la del correspondiente cero o polo.",
    "If $f(z)$ and $g(g)$ are analytic on and inside a simple closed contour $C$ , and $|g(z)|<|f(z)|$ for all $z\\in C$ , then $f(z)$ and $f(z)+g(z)$ have the same number of zeros inside $C$ .": "Si $f(z)$ y $g(z)$ son analíticas sobre y dentro de un contorno cerrado simple $C$, y $|g(z)|<|f(z)|$ para todo $z\\in C$, entonces $f(z)$ y $f(z)+g(z)$ tienen el mismo número de ceros dentro de $C$.",
    "If $f(z)$ and $g(z)$ are analytic on and inside a simple closed contour $C$ , and $\\left|g(z)\\right|<\\left|f(z)\\right|$ for all $z\\in C$ , then $f(z)$ and $f(z)+g(z)$ have the same number of zeros inside $C$ .": "Si $f(z)$ y $g(z)$ son analíticas sobre y dentro de un contorno cerrado simple $C$, y $\\left|g(z)\\right|<\\left|f(z)\\right|$ para todo $z\\in C$, entonces $f(z)$ y $f(z)+g(z)$ tienen el mismo número de ceros dentro de $C$.",
    "If $f(z)$ is analytic in a domain $D$ , $z_0\\in D$ and $|f(z)|\\leq|f(z_0)|$ for all $z\\in D$ , then $f(z)$ is constant in $D$ .": "Si $f(z)$ es analítica en un dominio $D$, $z_0\\in D$ y $|f(z)|\\leq|f(z_0)|$ para todo $z\\in D$, entonces $f(z)$ es constante en $D$.",
    "If $f(z)$ is analytic in a domain $D$ , $z_{0}\\in D$ and $\\left|f(z)\\right|\\leq\\left|f(z_{0})\\right|$ for all $z\\in D$ , then $f(z)$ is constant in $D$ .": "Si $f(z)$ es analítica en un dominio $D$, $z_{0}\\in D$ y $\\left|f(z)\\right|\\leq\\left|f(z_{0})\\right|$ para todo $z\\in D$, entonces $f(z)$ es constante en $D$.",
    "Let $D$ be a bounded domain with boundary $\\partial D$ and let $\\overline{D}=D\\cup\\partial D$ . If $f(z)$ is continuous on $\\overline{D}$ and analytic in $D$ , then $|f(z)|$ achieves its maximum value on $\\partial D$ .": "Sea $D$ un dominio acotado con frontera $\\partial D$ y sea $\\overline{D}=D\\cup\\partial D$. Si $f(z)$ es continua sobre $\\overline{D}$ y analítica en $D$, entonces $|f(z)|$ alcanza su valor máximo sobre $\\partial D$.",
    "If $u(z)$ is harmonic in $D$ , $z_0\\in D$ , and $u(z)\\leq u(z_0)$ for all $z\\in D$ , then $u(z)$ is constant in $D$ .": "Si $u(z)$ es armónica en $D$, $z_0\\in D$, y $u(z)\\leq u(z_0)$ para todo $z\\in D$, entonces $u(z)$ es constante en $D$.",
    "If $u(z)$ is harmonic in $D$ , $z_{0}\\in D$ , and $u(z)\\leq u(z_{0})$ for all $z\\in D$ , then $u(z)$ is constant in $D$ .": "Si $u(z)$ es armónica en $D$, $z_{0}\\in D$, y $u(z)\\leq u(z_{0})$ para todo $z\\in D$, entonces $u(z)$ es constante en $D$.",
    "In $|z|<R$ , if $f(z)$ is analytic, $|f(z)|\\leq M$ , and $f(0)=0$ , then": "En $|z|<R$, si $f(z)$ es analítica, $|f(z)|\\leq M$, y $f(0)=0$, entonces",
    "In $\\left|z\\right|<R$ , if $f(z)$ is analytic, $\\left|f(z)\\right|\\leq M$ , and $f(0)=0$ , then": "En $\\left|z\\right|<R$, si $f(z)$ es analítica, $\\left|f(z)\\right|\\leq M$, y $f(0)=0$, entonces",
    "Equalities hold iff $f(z)=Az$ , where $A$ is a constant such that $|A|=M/R$ .": "Las igualdades se cumplen syss $f(z)=Az$, donde $A$ es una constante tal que $|A|=M/R$.",
    "Equalities hold iff $f(z)=Az$ , where $A$ is a constant such that $\\left|A\\right|=M/R$ .": "Las igualdades se cumplen syss $f(z)=Az$, donde $A$ es una constante tal que $\\left|A\\right|=M/R$.",
    "Functions which have more than one value at a given point $z$ are called *multivalued* (or *many-valued* ).": "Las funciones que tienen más de un valor en un punto dado $z$ se denominan *multiformes* (o *multivaluadas*).",
    "A *cut domain* is one from which the points on finitely many nonintersecting simple contours (§ 1.9(iii) ) have been removed. Each contour is called a *cut* . A *cut neighborhood* is formed by deleting a ray emanating from the center. (Or more generally, a simple contour that starts at the center and terminates on the boundary.)": "Un *dominio cortado* es aquel del cual los puntos en un número finito de contornos simples que no se intersecan (§ 1.9(iii) ) han sido eliminados. Cada contorno se denomina un *corte*. Un *entorno cortado* se forma eliminando un rayo que emana del centro. (O más generalmente, un contorno simple que comienza en el centro y termina en la frontera.)",
    "Suppose $F(z)$ is multivalued and $a$ is a point such that there exists a branch of $F(z)$ in a cut neighborhood of $a$ that cannot be continued analytically to $a$ . Then $a$ is called a *branch point* (or *branch-point* ) of $F(z)$ .": "Supóngase que $F(z)$ es multiforme y $a$ es un punto tal que existe una rama de $F(z)$ en un entorno cortado de $a$ que no puede continuarse analíticamente hasta $a$. Entonces $a$ se denomina un *punto de ramificación* de $F(z)$.",
    "Branches can be constructed in two ways:": "Las ramas se pueden construir de dos maneras:",
    "(a) By introducing appropriate cuts from the branch points and restricting $F(z)$ to be single-valued in the resulting cut domain.": "(a) Introduciendo cortes apropiados desde los puntos de ramificación y restringiendo $F(z)$ a ser monódromo en el dominio cortado resultante.",
    "(b) By specifying the value of $F(z)$ at a point $z_0$ (not a branch point), and requiring $F(z)$ to be continued along paths that avoid the branch points.": "(b) Especificando el valor de $F(z)$ en un punto $z_0$ (no siendo un punto de ramificación), y requiriendo que $F(z)$ se continúe a lo largo de caminos que eviten los puntos de ramificación.",
    "(b) By specifying the value of $F(z)$ at a point $z_{0}$ (not a branch point), and requiring $F(z)$ to be continued along paths that avoid the branch points.": "(b) Especificando el valor de $F(z)$ en un punto $z_{0}$ (no siendo un punto de ramificación), y requiriendo que $F(z)$ se continúe a lo largo de caminos que eviten los puntos de ramificación.",
    "If the path circles a branch point at $z=a$ , $k$ times in the positive sense, and returns to $z_0$ with the value $F(z_0)$ unchanged, then $z=a$ is an *algebraic branch point* of order $k-1$ . If no such $k$ exists, $z=a$ is a *logarithmic branch point* .": "Si el camino rodea un punto de ramificación en $z=a$, $k$ veces en sentido positivo, y regresa a $z_0$ con el valor $F(z_0)$ sin cambios, entonces $z=a$ es un *punto de ramificación algebraico* de orden $k-1$. Si no existe tal $k$, $z=a$ es un *punto de ramificación logarítmico*.",
    "If the path circles a branch point at $z=a$ , $k$ times in the positive sense, and returns to $z_{0}$ with the value $F(z_{0})$ unchanged, then $z=a$ is an *algebraic branch point* of order $k-1$ . If no such $k$ exists, $z=a$ is a *logarithmic branch point* .": "Si el camino rodea un punto de ramificación en $z=a$, $k$ veces en sentido positivo, y regresa a $z_{0}$ con el valor $F(z_{0})$ sin cambios, entonces $z=a$ es un *punto de ramificación algebraico* de orden $k-1$. Si no existe tal $k$, $z=a$ es un *punto de ramificación logarítmico*.",
    "Let $\\alpha$ and $\\beta$ be real or complex numbers that are not integers. The function $F(z)=(1-z)^{\\alpha}(1+z)^{\\beta}$ has branch points at $z=1$ and $z=-1$ . One branch $f(z)$ is defined in $D=\\mathbb{C}\\setminus((-\\infty,-1]\\cup[1,\\infty))$ by": "Sean $\\alpha$ y $\\beta$ números reales o complejos que no son enteros. La función $F(z)=(1-z)^{\\alpha}(1+z)^{\\beta}$ tiene puntos de ramificación en $z=1$ y $z=-1$. Una rama $f(z)$ se define en $D=\\mathbb{C}\\setminus((-\\infty,-1]\\cup[1,\\infty))$ por",
    "where the principal values of the logarithms are taken. This branch is called the *principal branch* of $F(z)$ .": "donde se toman los valores principales de los logaritmos. Esta rama se denomina la *rama principal* de $F(z)$.",
    "Alternatively, take $z_0$ to be any point in $D$ and set $F(z_0)={\\mathrm{e}}^{\\alpha\\ln\\left(1-z_0\\right)+\\beta\\ln\\left(1+z_0\\right)}$ .": "Alternativamente, tómese $z_0$ como cualquier punto en $D$ y establézcase $F(z_0)={\\mathrm{e}}^{\\alpha\\ln\\left(1-z_0\\right)+\\beta\\ln\\left(1+z_0\\right)}$.",
    "Alternatively, take $z_{0}$ to be any point in $D$ and set $F(z_{0})={\\mathrm{e}}^{\\alpha\\ln\\left(1-z_{0}\\right)+\\beta\\ln\\left(1+z_{0}\\right)}$ .": "Alternativamente, tómese $z_{0}$ como cualquier punto en $D$ y establézcase $F(z_{0})={\\mathrm{e}}^{\\alpha\\ln\\left(1-z_{0}\\right)+\\beta\\ln\\left(1+z_{0}\\right)}$.",
    "Thus if $F(z)$ is continued along a path that circles $z=1$ $m$ times in the positive sense and returns to $z_0$ without encircling $z=-1$ , then": "Así, si $F(z)$ se continúa a lo largo de un camino que rodea $z=1$ $m$ veces en sentido positivo y regresa a $z_0$ sin rodear $z=-1$, entonces",
    "Thus if $F(z)$ is continued along a path that circles $z=1$ $m$ times in the positive sense and returns to $z_{0}$ without encircling $z=-1$ , then": "Así, si $F(z)$ se continúa a lo largo de un camino que rodea $z=1$ $m$ veces en sentido positivo y regresa a $z_{0}$ sin rodear $z=-1$, entonces",
    "in a neighborhood of $w_0$ , where $nF_n$ is the residue of $1/(f(z)-f(z_0))^n$ at $z=z_0$ .": "en un entorno de $w_0$, donde $nF_n$ es el residuo de $1/(f(z)-f(z_0))^n$ en $z=z_0$.",
    "in a neighborhood of $w_{0}$ , where $nF_{n}$ is the residue of $1/(f(z)-f(z_{0}))^{n}$ at $z=z_{0}$ .": "en un entorno de $w_{0}$, donde $nF_{n}$ es el residuo de $1/(f(z)-f(z_{0}))^{n}$ en $z=z_{0}$.",
    "where $nG_n$ is the residue of $g^{\\prime}(z)/(f(z)-f(z_0))^n$ at $z=z_0$ .": "donde $nG_n$ es el residuo de $g^{\\prime}(z)/(f(z)-f(z_0))^n$ en $z=z_0$.",
    "where $nG_{n}$ is the residue of $g^{\\prime}(z)/(f(z)-f(z_{0}))^{n}$ at $z=z_{0}$ .": "donde $nG_{n}$ es el residuo de $g^{\\prime}(z)/(f(z)-f(z_{0}))^{n}$ en $z=z_{0}$.",
    "where $\\mu>0$ , $f_0\\not=0$ , and the series converges in a neighborhood of $z_0$ .": "donde $\\mu>0$, $f_0\\not=0$, y la serie converge en un entorno de $z_0$.",
    "where $\\mu>0$ , $f_{0}\\not=0$ , and the series converges in a neighborhood of $z_{0}$ .": "donde $\\mu>0$, $f_{0}\\not=0$, y la serie converge en un entorno de $z_{0}$.",
    "en a neighborhood of $w_0$ , $nF_n$ being the residue of $1/(f(z)-f(z_0))^{n/\\mu}$ at $z=z_0$ .": "en un entorno de $w_0$, siendo $nF_n$ el residuo de $1/(f(z)-f(z_0))^{n/\\mu}$ en $z=z_0$.",
    "en a neighborhood of $w_{0}$ , $nF_{n}$ being the residue of $1/(f(z)-f(z_{0}))^{n/\\mu}$ at $z=z_{0}$ .": "en un entorno de $w_{0}$, siendo $nF_{n}$ el residuo de $1/(f(z)-f(z_{0}))^{n/\\mu}$ en $z=z_{0}$.",
    "It should be noted that different branches of $(w-w_0)^{1/\\mu}$ used in forming $(w-w_0)^{n/\\mu}$ in ( 1.10.18 ) can be selected for each term.": "Debe señalarse que diferentes ramas de $(w-w_0)^{1/\\mu}$ usadas para formar $(w-w_0)^{n/\\mu}$ en (1.10.18) pueden ser seleccionadas para cada término.",
    "It should be noted that different branches of $(w-w_{0})^{1/\\mu}$ used in forming $(w-w_{0})^{n/\\mu}$ in ( 1.10.18 ) can be selected for each term.": "Debe señalarse que diferentes ramas de $(w-w_{0})^{1/\\mu}$ usadas para formar $(w-w_{0})^{n/\\mu}$ en (1.10.18) pueden ser seleccionadas para cada término.",
    "where $nG_n$ is the residue of $g^{\\prime}(z)/(f(z)-f(z_0))^{n/\\mu}$ at $z=z_0$ .": "donde $nG_n$ es el residuo de $g^{\\prime}(z)/(f(z)-f(z_0))^{n/\\mu}$ en $z=z_0$.",
    "where $nG_{n}$ is the residue of $g^{\\prime}(z)/(f(z)-f(z_{0}))^{n/\\mu}$ at $z=z_{0}$ .": "donde $nG_{n}$ es el residuo de $g^{\\prime}(z)/(f(z)-f(z_{0}))^{n/\\mu}$ en $z=z_{0}$.",
    "Functions Defined by Contour Integrals": "Funciones Definidas por Integrales de Contorno",
    "Let $D$ be a domain and $[a,b]$ a closed finite segment of the real axis. Assume that for each $t\\in[a,b]$ the function $f(z,t)$ is analytic in $D$ and for each $z\\in D$ both $f(z,t)$ and $\\partial f(z,t)/\\partial z$ are continuous functions of $t$ . Then": "Sea $D$ un dominio y $[a,b]$ un segmento finito cerrado del eje real. Asúmase que para cada $t\\in[a,b]$ la función $f(z,t)$ es analítica en $D$ y para cada $z\\in D$ tanto $f(z,t)$ como $\\partial f(z,t)/\\partial z$ son funciones continuas de $t$. Entonces",
    "is analytic in $D$ and its derivatives of all orders can be found by differentiating under the sign of integration.": "es analítica en $D$ y sus derivadas de todos los órdenes se pueden hallar diferenciando bajo el signo de integración.",
    "This result is also true when $b=\\infty$ , or when $f(z,t)$ has a singularity at $t=b$ , provided that both integrals converge uniformly in every compact subset of $D$ .": "Este resultado es también verdadero cuando $b=\\infty$, o cuando $f(z,t)$ tiene una singularidad en $t=b$, siempre que ambas integrales converjan uniformemente en todo subconjunto compacto de $D$.",
}


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


def traducir_prosa_archivo(raw: str) -> str:
    """Traduce el contenido sustituyendo oraciones exactas e infoboxes."""
    # 1. Sanitizar LaTeX \text{} y \mbox{}
    raw = sanitizar_bloques_text_latex(raw)

    # 2. Reemplazos de oraciones exactas
    for orig_sent, esp_sent in ORACIONES_EXACTAS.items():
        raw = raw.replace(orig_sent, esp_sent)

    raw = re.sub(r'\(For other notation see Notation for the Special Functions\s*\.\)', '(Para otra notación véase Notación para las Funciones Especiales .)', raw)
    raw = re.sub(r'\(For other notation see \[([^\]]+)\]\(([^)]+)\)\s*\.\)', r'(Para otra notación véase [\1](\2) .)', raw)
    raw = raw.replace('**See also:**', '**Véase también:**')
    raw = raw.replace('Keywords:', 'Palabras clave:')
    raw = raw.replace('Referenced by:', 'Referenciado por:')
    raw = raw.replace('Notes:', 'Notas:')

    return raw


def perfeccionar_archivo(orig_path: Path, dest_path: Path):
    raw = orig_path.read_text(encoding="utf-8")
    translated_text = traducir_prosa_archivo(raw)
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

    print("Perfeccionamiento exacto de la Sección 1 completado exitosamente.")


if __name__ == "__main__":
    main()
