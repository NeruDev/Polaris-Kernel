---
id: msc18_teoria_de_categorias
title: "Teoría de categorías"
pilar: "02_estructuras_algebraicas"
msc_code: "18-01"
tags: [categorias, functores, morfismos, abstraccion]
nivel: abstracto
updated: "2026-04-26"
status: "stable"
---

# Teoría de Categorías

![Morfismos f, g y su composicion en una categoria](diagrama_conmutativo.svg)

La teoría de categorías es el nivel más alto de abstracción en las matemáticas. 
No se preocupa por los elementos individuales de un conjunto, sino por las 
relaciones y transformaciones entre estructuras. Es, en esencia, la 
"matemática de las matemáticas".

## Objetos, morfismos y composición

Una categoría $\mathcal{C}$ consiste en una colección de **objetos** ($A, B, C$) 
y una colección de **morfismos** (flechas) entre ellos. Para cada par de 
morfismos $f: A \to B$ y $g: B \to C$, debe existir un morfismo composición 
$g \circ f: A \to C$ que sea asociativo. Además, cada objeto debe tener un 
morfismo identidad $1_A$ que actúe como neutro en la composición.

## Functores y transformaciones naturales

Los **functores** son los morfismos de las categorías. Un functor $F: \mathcal{C} \to \mathcal{D}$ 
mapea objetos a objetos y morfismos a morfismos, preservando la estructura de 
composición e identidad. Las **transformaciones naturales** van un paso más 
allá, mapeando un functor a otro functor, permitiendo comparar diferentes 
maneras de transformar categorías.

## Productos, coproductos y límites

Estas construcciones universales permiten definir objetos mediante sus 
propiedades de relación. Un **producto** de $A$ y $B$ es un objeto junto con 
proyecciones que cumplen una propiedad universal: cualquier otro objeto con 
mismo mapeo debe factorizarse a través del producto. El **límite** generaliza 
esta noción a diagramas complejos, capturando la esencia de la convergencia y 
la consistencia estructural.

## Equivalencias y adjunciones

Las **adjunciones** son una de las herramientas más potentes. 
Representan una relación de "casi equivalencia" entre dos functores en 
direcciones opuestas. Establecen que resolver un problema en una categoría 
$\mathcal{C}$ es equivalente a resolverlo en $\mathcal{D}$ tras aplicar una 
transformación específica, lo que unifica conceptos de álgebra, topología y 
lógica computacional.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $\mathcal{C}$ | Categoría | estructura |
| $f, g$ | Morfismos | flecha |
| $\circ$ | Composición | operador |
| $F$ | Functor | mapeo |
| $\eta$ | Transf. Natural | mapeo |
| $\cong$ | Isomorfismo | relación |
| $1_A$ | Identidad | morfismo |
| $\dashv$ | Adjuncion | relación |
