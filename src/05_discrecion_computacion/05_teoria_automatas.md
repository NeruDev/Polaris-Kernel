---
id: msc68_teoria_automatas
title: "Teoría de Autómatas y Lenguajes Formales"
pilar: "05_discrecion_computacion"
msc_code: "68-XX"
tags: [automatas, turing, lenguajes, chomsky]
nivel: avanzado
updated: "2026-05-24"
status: "stable"
---

# Teoría de Autómatas y Lenguajes Formales

La teoría de autómatas constituye la fundamentación matemática rigurosa sobre la cual se erigen las ciencias de la computación modernas.
Esta disciplina abstracta estudia el comportamiento conceptual de las máquinas computacionales teóricas y la íntima relación que estas mantienen con los diversos tipos de lenguajes formales.
A través del modelado de problemas mediante transiciones de estados discretos, permite establecer de forma inequívoca qué tipos de problemas lógicos son inherentemente computables y cuáles no lo son.

## Autómatas Finitos y Expresiones Regulares

El modelo computacional matemático más elemental y restrictivo es el denominado autómata finito.
Un autómata finito consta estrictamente de un conjunto predeterminado y finito de estados internos y una función matemática de transición que dictamina fehacientemente cómo el sistema debe cambiar de estado tras leer cada símbolo de entrada.
Estos autómatas simples carecen de memoria auxiliar profunda, lo que significa que su poder descriptivo se limita de forma exclusiva a reconocer patrones cíclicos secuenciales.
Los lenguajes matemáticos que estos autómatas son capaces de procesar y reconocer se conocen como lenguajes regulares, los cuales coinciden exactamente con aquellos patrones que pueden ser descritos analíticamente a través de expresiones regulares sintácticas.

## Jerarquía de Chomsky

El insigne lingüista y pensador Noam Chomsky propuso una clasificación estructural estratificada de las gramáticas formales que generó un profundo impacto teórico tanto en la lingüística estructural como en la naciente informática.
Esta jerarquía ascendente clasifica a los lenguajes en cuatro niveles concéntricos de complejidad generativa creciente: regulares, libres de contexto, sensibles al contexto y estructurados recursivamente enumerables.
Cada uno de estos niveles lingüísticos abstractos corresponde biyectivamente a una clase específica de máquina teórica que posee capacidades de memoria gradualmente superiores.
Por ejemplo, los lenguajes libres de contexto, que componen el esqueleto de la gran mayoría de los lenguajes de programación modernos, exigen imperativamente el uso de un autómata de pila o *pushdown automaton*, capaz de almacenar símbolos en una memoria secuencial de tipo LIFO (Last In, First Out).

## Máquinas de Turing y Computabilidad Universal

En la cúspide indiscutible del poder de procesamiento teórico reside la icónica máquina inventada por Alan Turing.
A diferencia de los modelos más primitivos, una máquina de Turing teórica está equipada con una cinta de almacenamiento infinita sobre la cual posee la capacidad de avanzar libremente, leer datos y escribir nueva información sin ningún tipo de restricción de tiempo.
La tesis fundamental de Church-Turing postula audazmente que cualquier algoritmo efectivo y computable que un ser humano pueda concebir lógicamente puede ser invariablemente simulado por una de estas máquinas elementales.
Consecuentemente, las máquinas de Turing delimitan de forma categórica y permanente la frontera conceptual extrema entre lo que es matemáticamente decidible y lo que escapa a los dominios del procesamiento algorítmico algorítmico, como ocurre célebremente con el irresoluble problema de la parada.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $Q$ | Conjunto de estados | conjunto |
| $\Sigma$ | Alfabeto de símbolos | conjunto |
| $\delta$ | Función de transición | función |
| $q_0$ | Estado inicial | elemento |
| $F$ | Conjunto de estados finales | conjunto |
