---
id: msc15_algebra_lineal
title: "Álgebra Lineal: Matrices y Espacios Vectoriales"
pilar: "02_estructuras_algebraicas"
msc_code: "15-XX"
tags: [matrices, vectores, lineal, algebra]
nivel: intro
updated: "2026-04-26"
status: "stable"
---

# Álgebra Lineal: Matrices y Espacios Vectoriales

![Visualización de multiplicación de matrices](operaciones_matrices.svg)


![Representación de base canónica R3](espacio_vectorial_base.svg)


![Efecto de una matriz sobre el espacio](transformacion_lineal.svg)


El álgebra lineal es el estudio de vectores, espacios vectoriales y transformaciones lineales. Es una herramienta fundamental en física, ingeniería e informática.

## Sistemas de ecuaciones

Un sistema de ecuaciones lineales puede representarse en forma matricial como $Ax = b$. Se resuelve comúnmente mediante la **Eliminación de Gauss-Jordan**.

## Matrices y determinantes

### Definición de Matriz
Una **matriz** es un arreglo rectangular de números organizados en filas y columnas.
$$A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$$

### Operaciones Básicas
- **Suma**: $A + B$ (elemento a elemento, mismas dimensiones).
- **Multiplicación por escalar**: $cA$.
- **Producto de matrices**: El producto $AB$ solo es posible si el número de columnas de $A$ es igual al de filas de $B$.

### Determinantes
El determinante de una matriz cuadrada indica si es invertible.
- Para $2 \times 2$: $\det(A) = ad - bc$.
- Si $\det(A) \neq 0$, la matriz es **no singular** (invertible).

### Matriz Inversa y Transpuesta
- **Transpuesta ($A^T$)**: Se intercambian filas por columnas.
- **Inversa ($A^{-1}$)**: Matriz tal que $AA^{-1} = I$.

## Espacios vectoriales

Un **espacio vectorial** es un conjunto de elementos (vectores) cerrados bajo la suma y la multiplicación por un escalar, cumpliendo 10 axiomas fundamentales.

### Conceptos Clave
- **Combinación lineal**: $v = c_1v_1 + c_2v_2 + \dots + c_nv_n$.
- **Independencia lineal**: Un conjunto de vectores es independiente si ninguno puede escribirse como combinación de los otros.
- **Base**: Conjunto de vectores linealmente independientes que generan todo el espacio.

## Transformaciones lineales

*(Pendiente de expansión detallada)*

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $A, B$ | Matrices | estructura |
| $v, w$ | Vectores | estructura |
| $\det$ | Determinante | función |
| $I$ | Matriz Identidad | constante |
| $c$ | Escalar | variable |