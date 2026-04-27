---
id: msc05C_teoria_de_grafos
title: "Teoría de grafos"
pilar: "05_discrecion_computacion"
msc_code: "05C-01"
tags: [grafos, arboles, conectividad, redes]
nivel: intermedio
updated: "2026-04-26"
status: "stable"
---

# Teoría de grafos

![Estructura basica de un grafo no dirigido](grafos_basico.svg)

La teoría de grafos es la rama de las matemáticas que estudia las relaciones entre objetos mediante estructuras de nodos y enlaces.
Es el lenguaje universal para describir redes complejas, desde la topología de internet y los circuitos integrados hasta las interacciones sociales y las rutas logísticas.

## Definiciones y tipos de grafos

Un grafo $G = (V, E)$ está compuesto por un conjunto de **vértices** (nodos) y un conjunto de **aristas** (enlaces) que los conectan.
- **Dirigidos:** Las aristas tienen una dirección específica, representando flujos de un sentido único.
- **No dirigidos:** Las conexiones son bidireccionales por naturaleza.
- **Ponderados:** Cada arista tiene un peso o costo asociado, vital para algoritmos de optimización de rutas mínimas.
La conectividad de un grafo mide qué tan robusta es la red ante la eliminación de nodos o enlaces, una propiedad crítica en la ingeniería de sistemas distribuidos.

## Árboles y algoritmos de búsqueda

Un **árbol** es un grafo conexo que no contiene ciclos.
Esta estructura jerárquica es fundamental en informática para la organización de archivos, el análisis sintáctico y los sistemas de bases de datos.
Los algoritmos de búsqueda, como el BFS (Breadth-First Search) y el DFS (Depth-First Search), permiten recorrer estas estructuras de forma eficiente para encontrar información o verificar la existencia de caminos.
El concepto de **Árbol de Recubrimiento Mínimo** (MST) es particularmente útil para diseñar redes de bajo costo (como tendidos eléctricos) que conecten todos los puntos sin redundancias innecesarias.

## Grafos planos y coloración

Un grafo es **plano** si puede dibujarse en el papel sin que sus aristas se crucen.
Esta propiedad es esencial en el diseño de microchips y circuitos impresos.
El **Teorema de los Cuatro Colores** es un hito de este campo, estableciendo que cualquier mapa plano puede colorearse con solo cuatro colores de modo que regiones adyacentes tengan colores distintos.
Este problema de coloración se generaliza en algoritmos de asignación de recursos y programación de horarios, donde cada color representa una franja de tiempo libre de conflictos.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $G$ | Grafo | estructura |
| $V$ | Vértices | conjunto |
| $E$ | Aristas | conjunto |
| $d(v)$ | Grado | entero |
| $w$ | Peso | escalar |
| $T$ | Árbol | subgrafo |
