---
id: msc54_topologia
title: "Topología"
pilar: "04_espacio_forma"
msc_code: "54-01"
tags: [topologia, metricas, continuidad]
nivel: avanzado
updated: "2026-04-26"
status: "stable"
---

# Topología

![Puntos interiores y vecindarios](topologia_vecindarios.svg)


![Equivalencia entre una dona y una taza](topologia_homeomorfismo.svg)

La topología es el estudio de las propiedades de las figuras que permanecen 
invariantes ante deformaciones continuas (estiramientos o torsiones, pero 
sin romper ni pegar). Es conocida como la "geometría de la plastilina".

## Espacios métricos

Un espacio métrico es un conjunto dotado de una función de distancia $d(x,y)$. 
Permite definir conceptos como vecindarios, convergencia de sucesiones y 
conjuntos abiertos de forma rigurosa. Es la base para generalizar el cálculo 
a dimensiones infinitas.

## Continuidad topológica

En topología, una función $f$ es continua si la preimagen de cada conjunto 
abierto es abierta. Esta definición es más general que la del cálculo ($\varepsilon-\delta$) 
y permite estudiar la continuidad en espacios donde no hay una noción de 
distancia clara.

## Compacidad y conexión

- **Compacidad:** Generaliza la noción de finitud; un conjunto es compacto si 
todo recubrimiento abierto tiene un subrecubrimiento finito.
- **Conexión:** Un espacio es conexo si no puede dividirse en dos conjuntos 
abiertos disjuntos no vacíos; representa la idea de "una sola pieza".

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $\tau$ | Topología | colección |
| $d(x,y)$ | Distancia | función |
| $U$ | Conjunto abierto | conjunto |
| $\bar{A}$ | Clausura de A | conjunto |