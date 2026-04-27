---
id: msc11_sistemas_numericos_reales
title: "Sistemas Numéricos: Conjuntos Reales"
pilar: "01_fundamentos_logica"
msc_code: "11-01"
tags: [numeros, conjuntos, reales]
nivel: intro
updated: "2026-04-26"
status: "stable"
---

# Sistemas Numéricos: Conjuntos Reales

![Representacion de la recta real y conjuntos](sistemas_numericos_recta.svg)

La aritmética es la base sobre la cual se edifica toda la estructura matemática.
Dominar sus conceptos fundamentales es un requisito esencial para el éxito en disciplinas más complejas como el álgebra, el cálculo diferencial y las matemáticas superiores aplicadas a la ingeniería.

## Naturales y enteros

### Números naturales $\mathbb{N}$
$$\mathbb{N} = \{1, 2, 3, 4, 5, \ldots\}$$
Los números naturales son aquellos utilizados primordialmente para contar elementos de un conjunto.
Desde un punto de vista algebraico, este conjunto es cerrado bajo las operaciones de suma y multiplicación, lo que significa que el resultado siempre pertenece a $\mathbb{N}$.
Sin embargo, no es cerrado bajo la resta o la división, ya que operaciones como $3 - 5$ o $1 / 2$ no producen resultados naturales.
Es importante notar que algunos autores modernos incluyen el número cero dentro de este conjunto, denotándolo como $\mathbb{N}_0$.

### Números enteros $\mathbb{Z}$
$$\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}$$
El conjunto de los números enteros extiende a los naturales incorporando los números negativos y el elemento neutro aditivo, el cero.
Esta extensión permite que el conjunto sea cerrado bajo la resta, resolviendo la limitación de los naturales.
En el contexto de la teoría de anillos, $\mathbb{Z}$ es el ejemplo prototípico de un anillo conmutativo con unidad, donde se preservan propiedades críticas como la divisibilidad y la existencia de números primos.

## Racionales e irracionales

### Números racionales $\mathbb{Q}$
$$\mathbb{Q} = \left\{ \frac{p}{q} : p, q \in \mathbb{Z}, q \neq 0 \right\}$$
Un número racional es cualquier valor que puede expresarse como el cociente de dos números enteros, siempre que el denominador sea distinto de cero.
Este conjunto incluye tanto a las fracciones simples como a los números decimales exactos y decimales periódicos.
A diferencia de los enteros, los racionales forman un cuerpo o campo, ya que son cerrados bajo las cuatro operaciones aritméticas elementales, exceptuando la división por cero.

### Números irracionales $\mathbb{I}$
Los números irracionales son aquellos que no pueden ser representados como una razón entre dos enteros.
Su expresión decimal se caracteriza por ser infinita y no presentar ningún patrón de repetición o periodicidad.
Ejemplos fundamentales de este conjunto incluyen la constante pi $\pi$, el número de Euler $e$ y raíces de números no cuadrados como $\sqrt{2}$.
La existencia de estos números fue un hito histórico que rompió con la concepción pitagórica de que todo en el universo podía explicarse mediante razones de números enteros.

### Números reales $\mathbb{R}$
$$\mathbb{R} = \mathbb{Q} \cup \mathbb{I}$$
El conjunto de los números reales nace de la unión de los racionales y los irracionales.
Representan la totalidad de los puntos que componen la recta numérica continua.
Una propiedad definitoria de los reales es la completitud, que garantiza que no existen "huecos" en la recta, permitiendo el desarrollo riguroso del análisis matemático y el concepto de límite.

## Jerarquía de conjuntos
La relación de inclusión entre estos conjuntos define la estructura jerárquica de los sistemas numéricos:
$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$

## Glosario de variables

| Símbolo | Nombre | Tipo | Unidad |
| --- | --- | --- | --- |
| $\pi$ | Constante pi | constante | rad |
| $e$ | Número de Euler | constante | escalar |
| $\mathbb{N}$ | Conjunto Naturales | conjunto | N/A |
| $\mathbb{Z}$ | Conjunto Enteros | conjunto | N/A |
| $\mathbb{Q}$ | Conjunto Racionales | conjunto | N/A |
| $\mathbb{R}$ | Conjunto Reales | conjunto | N/A |
