---
id: msc26_calculo_multivariable
title: "Cálculo multivariable y vectorial"
pilar: "03_analisis_continuidad"
msc_code: "26-01"
tags: [multivariable, vectores, gradiente, integrales_multiples]
nivel: intermedio
updated: "2026-04-26"
status: "stable"
---

# Cálculo multivariable y vectorial

![Visualizacion de un campo vectorial rotacional](campo_vectorial.svg)

El cálculo multivariable extiende los conceptos de una variable a funciones 
de varias dimensiones $\mathbb{R}^n$. Permite modelar fenómenos físicos como 
campos de fuerza, flujo de calor y dinámica de fluidos donde las variables 
están interconectadas.

## Derivadas parciales y direccionales

A diferencia de la derivada ordinaria, la derivada parcial $f_x$ mide la tasa 
de cambio manteniendo las otras variables constantes. El **vector gradiente** 
$\nabla f$ es fundamental, ya que apunta en la dirección de máximo crecimiento 
de la función y su magnitud representa la pendiente en esa dirección. La 
derivada direccional permite calcular el cambio en cualquier dirección dada 
por un vector unitario.

## Integrales múltiples

Las integrales dobles y triples permiten calcular volúmenes, masas y centros 
de gravedad de regiones sólidas. Para regiones con simetrías, es crucial el 
**cambio de variables** mediante el Jacobiano, permitiendo pasar de 
coordenadas rectangulares a polares, cilíndricas o esféricas, simplificando 
drásticamente la complejidad algebraica de la integración.

## Teoremas vectoriales (Green, Stokes, Gauss)

Estos teoremas establecen conexiones profundas entre integrales de diferentes 
dimensiones. El Teorema de **Green** relaciona una integral de línea con una 
integral doble. El Teorema de **Stokes** generaliza esto al espacio 3D 
vinculando el flujo de un rotacional. El Teorema de la **Divergencia** (Gauss) 
relaciona el flujo neto a través de una superficie cerrada con la acumulación 
de "fuentes" o "sumideros" en el volumen interior.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $\nabla$ | Operador Nabla | operador |
| $\frac{\partial f}{\partial x}$ | Derivada parcial | operador |
| $J$ | Jacobiano | matriz |
| $\vec{F}$ | Campo vectorial | vector |
| $div \vec{F}$ | Divergencia | escalar |
| $rot \vec{F}$ | Rotacional | vector |
| $dA, dV$ | Elementos diferencial | diferencial |
