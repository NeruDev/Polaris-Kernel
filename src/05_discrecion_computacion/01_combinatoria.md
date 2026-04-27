---
id: msc05_combinatoria
title: "Combinatoria"
pilar: "05_discrecion_computacion"
msc_code: "05-01"
tags: [conteo, permutaciones, combinaciones, binomio]
nivel: intro
updated: "2026-04-26"
status: "stable"
---

# Combinatoria

![Diagrama de arbol para principios de conteo](combinatoria_arbol.svg)

La combinatoria es el arte de contar y organizar estructuras discretas sin necesidad de enumerarlas una por una.
Es una rama esencial para la informática, la probabilidad y la optimización, proporcionando los métodos para determinar la viabilidad de algoritmos y el tamaño de espacios de búsqueda.

## Principios fundamentales de conteo

El **Principio Aditivo** establece que si una tarea puede realizarse de $n$ maneras y otra de $m$ maneras, y ambas son mutuamente excluyentes, entonces hay $n+m$ formas de realizar una de ellas.
Por otro lado, el **Principio Multiplicativo** indica que si una tarea tiene $n$ opciones y otra tiene $m$ opciones independientes, existen $n \times m$ formas de realizar ambas secuencialmente.
Estos dos pilares permiten descomponer problemas de conteo masivos en unidades manejables, representables a menudo mediante diagramas de árbol de decisiones.

## Permutaciones y combinaciones

Las **permutaciones** se utilizan cuando el orden de los elementos es relevante.
Si tenemos $n$ objetos y queremos organizar $k$ de ellos, el número de formas posibles es $P(n, k) = n! / (n-k)!$.
En contraste, las **combinaciones** se emplean cuando el orden no importa, como al seleccionar un comité o una mano de cartas.
La fórmula para combinaciones es $C(n, k) = n! / (k!(n-k)!)$, también conocida como el coeficiente binomial.
Dominar la diferencia entre orden y selección es crítico para evitar el sobreconteo en problemas estadísticos.

## Teorema del binomio

El teorema del binomio describe la expansión algebraica de las potencias de un binomio $(a + b)^n$.
Establece que los coeficientes de los términos de la expansión son precisamente las combinaciones $C(n, k)$.
Esta conexión profunda vincula el álgebra polinomial con la combinatoria de conteo, permitiendo resolver identidades matemáticas complejas y calcular probabilidades en experimentos de Bernoulli (éxito/fracaso).
El Triángulo de Pascal es la representación visual de estos coeficientes, donde cada entrada es la suma de las dos superiores, demostrando la naturaleza recursiva de las estructuras combinatorias.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $n!$ | Factorial | operación |
| $P(n, k)$ | Permutaciones | función |
| $C(n, k)$ | Combinaciones | función |
| $\binom{n}{k}$ | Coef. Binomial | función |
| $a, b$ | Términos binomio | escalar |
