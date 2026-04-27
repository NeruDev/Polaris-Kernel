---
id: msc11_teoria_de_numeros
title: "Teoría de Números y Divisibilidad"
pilar: "05_discrecion_computacion"
msc_code: "11-01"
tags: [divisibilidad, primos, modular, aritmetica]
nivel: intermedio
updated: "2026-04-26"
status: "stable"
---

# Teoría de Números y Divisibilidad

![Representacion esquematica de numeros primos](primos_criba.svg)

La teoría de números es el estudio de las propiedades de los números enteros, a menudo referida como "la reina de las matemáticas".
Aunque sus planteamientos son frecuentemente sencillos de entender, su resolución ha requerido el desarrollo de las herramientas más sofisticadas del álgebra y el análisis.

## Divisibilidad y números primos

Se dice que un entero $a$ divide a $b$ ($a \mid b$) si el residuo de la división es cero.
Los **números primos** son los bloques de construcción fundamentales de este sistema, definidos como enteros mayores que 1 cuyos únicos divisores son ellos mismos y la unidad.
El **Teorema Fundamental de la Aritmética** garantiza que todo entero positivo puede descomponerse en un producto único de factores primos.
Esta propiedad es la base de la criptografía moderna, ya que factorizar números extremadamente grandes en sus primos constituyentes es un problema computacionalmente difícil.

## Aritmética modular y congruencias

La aritmética modular, o "aritmética del reloj", se ocupa de los residuos de las operaciones respecto a un módulo fijo $m$.
Decimos que $a \equiv b \pmod{m}$ si $m$ divide a la diferencia $a - b$.
Este sistema es cíclico y preserva las operaciones de suma y multiplicación, lo que lo hace ideal para el diseño de algoritmos informáticos y la verificación de errores.
El Pequeño Teorema de Fermat y el Teorema Chino del Residuo son herramientas avanzadas en este campo que permiten resolver complejos sistemas de congruencias lineales.

## Ecuaciones diofánticas

Son ecuaciones donde se buscan exclusivamente soluciones enteras.
El ejemplo más famoso es el Último Teorema de Fermat, que afirma que la ecuación $x^n + y^n = z^n$ no tiene soluciones enteras no nulas para $n > 2$.
La resolución de estas ecuaciones a menudo involucra el **Algoritmo de Euclides** para hallar el Máximo Común Divisor (MCD).
El algoritmo es eficiente y fundamental para simplificar fracciones y resolver identidades de Bézout, estableciendo una conexión directa entre la geometría de los números y la eficiencia algorítmica.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $a \mid b$ | Divisibilidad | relación |
| $\equiv$ | Congruencia | relación |
| $p$ | Número primo | entero |
| $m$ | Módulo | entero |
| $\text{MCD}$ | Máximo Común Divisor | función |
| $\text{MCM}$ | Mínimo Común Múltiplo | función |
