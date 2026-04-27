---
id: msc08_algebra_abstracta
title: "Álgebra abstracta"
pilar: "02_estructuras_algebraicas"
msc_code: "08-01"
tags: [grupos, anillos, campos, estructuras]
nivel: avanzado
updated: "2026-04-26"
status: "stable"
---

# Álgebra abstracta

![Jerarquia de Monoides, Grupos, Anillos y Campos](jerarquia_estructuras.svg)

El álgebra abstracta estudia las estructuras algebraicas por sí mismas, 
prescindiendo de la naturaleza de los elementos. Se enfoca en las propiedades 
de las operaciones y las leyes que las rigen.

## Teoría de grupos

Un grupo es un conjunto G con una operación $*$ que cumple:
1. **Asociatividad:** $(a*b)*c = a*(b*c)$.
2. **Elemento neutro:** Existe $e$ tal que $a*e = a$.
3. **Elemento inverso:** Existe $a^{-1}$ tal que $a*a^{-1} = e$.
Si además es conmutativo, se llama grupo abeliano.

## Teoría de anillos

Un anillo es una estructura con dos operaciones (suma y producto). Debe ser 
un grupo abeliano bajo la suma y cumplir la asociatividad y distributividad 
bajo el producto. Ejemplos comunes son los números enteros $\mathbb{Z}$ y 
los polinomios.

## Campos y extensiones de Galois

Un campo es un anillo donde todo elemento no nulo tiene inverso multiplicativo. 
La teoría de Galois estudia las raíces de los polinomios y sus simetrías, 
siendo fundamental para demostrar la imposibilidad de resolver ecuaciones de 
quinto grado por radicales.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $(G, *)$ | Grupo | estructura |
| $e$ | Neutro | constante |
| $\mathbb{F}$ | Campo | estructura |
| $\phi$ | Homomorfismo | función |
