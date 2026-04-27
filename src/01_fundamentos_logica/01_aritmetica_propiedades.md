---
id: msc11_sistemas_numericos_propiedades
title: "Aritmética: Propiedades de las Operaciones"
pilar: "01_fundamentos_logica"
msc_code: "11-01"
tags: [aritmetica, propiedades, axiomas, pemdas]
nivel: intro
updated: "2026-04-26"
status: "stable"
---

# Aritmética: Propiedades de las Operaciones

![Diagrama de Venn de tres conjuntos](conjuntos_triple_venn.svg)

Las propiedades aritméticas definen el comportamiento de las operaciones básicas en los sistemas numéricos.
Estos axiomas estructurales aseguran que la manipulación algebraica sea consistente y predecible, independientemente de la magnitud de los valores involucrados.

## Operaciones fundamentales

La suma y la multiplicación son las operaciones binarias primarias.
La resta y la división se definen formalmente como las operaciones inversas de estas.
La consistencia de estas operaciones se apoya en propiedades que permiten reordenar y agrupar términos para facilitar el cálculo mental y el procesamiento algorítmico.

### Propiedades de la suma y multiplicación

| Propiedad | Suma | Multiplicación |
|-----------|------|----------------|
| **Conmutativa** | $a + b = b + a$ | $a \cdot b = b \cdot a$ |
| **Asociativa** | $(a + b) + c = a + (b + c)$ | $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ |
| **Elemento neutro** | $a + 0 = a$ | $a \cdot 1 = a$ |
| **Elemento inverso** | $a + (-a) = 0$ | $a \cdot (1/a) = 1$ |

La **Propiedad Distributiva** es el puente entre ambas operaciones, permitiendo expandir o factorizar expresiones: $a \cdot (b + c) = a \cdot b + a \cdot c$.
Este axioma es la base de casi todas las simplificaciones de ecuaciones en matemáticas avanzadas.

## Jerarquía de operaciones (PEMDAS)

Para evitar la ambigüedad en expresiones que contienen múltiples operaciones, se aplica la convención PEMDAS.
El orden estricto de ejecución es:
1. **P**aréntesis y otros símbolos de agrupación.
2. **E**xponentes y raíces.
3. **M**ultiplicación y **D**ivisión (de izquierda a derecha).
4. **A**dición y **S**ustracción (de izquierda a derecha).
Seguir este orden es crítico en la programación de computadoras y en la resolución de problemas de ingeniería para garantizar resultados reproducibles y libres de errores lógicos.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $a, b, c$ | Términos reales | escalar |
| $+$ | Operador suma | binario |
| $\cdot$ | Operador producto | binario |
| $0$ | Identidad aditiva | constante |
| $1$ | Identidad multiplicativa | constante |
| $( )$ | Agrupación | delimitador |
