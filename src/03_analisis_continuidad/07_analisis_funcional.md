---
id: msc46_analisis_funcional
title: "Análisis funcional"
pilar: "03_analisis_continuidad"
msc_code: "46-01"
tags: [banach, hilbert, operadores, espacios_funcionales]
nivel: avanzado
updated: "2026-04-26"
status: "stable"
---

# Análisis funcional

![Teorema de la proyeccion ortogonal en espacios funcionales](hilbert_proyeccion.svg)

El análisis funcional es la rama del análisis que trata con espacios de funciones de dimensión infinita.
A diferencia del cálculo clásico que estudia números, esta disciplina trata a las funciones como puntos en un espacio geométrico abstracto, permitiendo resolver ecuaciones diferenciales y problemas de optimización de una complejidad superior.

## Espacios normados y métricas inducidas

Un espacio normado es un espacio vectorial donde cada elemento (función) tiene una longitud o "norma" definida.
Esta norma permite medir la distancia entre funciones, posibilitando el estudio de la convergencia de sucesiones de funciones.
Si el espacio es completo (es decir, cada sucesión de Cauchy converge a un elemento dentro del mismo espacio), se denomina **Espacio de Banach**.
Estos espacios son el escenario natural para demostrar la existencia y unicidad de soluciones en modelos físicos y financieros.

## Espacios de Hilbert y proyecciones

Un **Espacio de Hilbert** es un espacio de Banach dotado de un producto interno, lo que introduce la noción de ángulo y ortogonalidad.
El **Teorema de la Proyección Ortogonal** establece que para cualquier vector y un subespacio cerrado, existe una única "mejor aproximación".
Esta propiedad es la base de las Series de Fourier y la mecánica cuántica, donde los estados físicos se representan como vectores en espacios de Hilbert y las probabilidades se derivan de proyecciones ortogonales.

## Operadores lineales (intro)

Los operadores son funciones que mapean un espacio funcional a otro (morfismos de espacios).
El estudio de los **operadores acotados** y sus autovalores (espectro) generaliza el álgebra lineal de matrices a dimensiones infinitas.
Este marco permite entender las transformaciones integrales (como Laplace o Fourier) como simples rotaciones o estiramientos en espacios funcionales de alta dimensionalidad, unificando la visión de la física ondulatoria con el álgebra abstracta.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $\mathcal{H}$ | Espacio Hilbert | estructura |
| $\| \cdot \|$ | Norma | función |
| $\langle \cdot, \cdot \rangle$ | Producto interno | función |
| $T$ | Operador lineal | mapeo |
| $\lambda$ | Autovalor | escalar |
| $L^2$ | Espacio funciones | conjunto |
| $\perp$ | Ortogonalidad | relación |
