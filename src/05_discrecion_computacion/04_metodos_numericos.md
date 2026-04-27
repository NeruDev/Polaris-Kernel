---
id: msc65_metodos_numericos
title: "Métodos Numéricos: Raíces y Aproximación"
pilar: "05_discrecion_computacion"
msc_code: "65-01"
tags: [numerico, raices, aproximacion, errores, iteracion]
nivel: intermedio
updated: "2026-04-26"
status: "stable"
---

# Métodos Numéricos: Raíces y Aproximación

![Visualizacion del metodo de biseccion](metodos_numericos_raices.svg)

Los métodos numéricos son técnicas que permiten formular problemas matemáticos para que puedan resolverse mediante operaciones aritméticas.
Son fundamentales en la era de la computación, permitiendo hallar soluciones aproximadas pero suficientemente precisas a problemas que carecen de una solución analítica exacta.

## Aproximación y análisis de errores

Toda aproximación numérica conlleva una discrepancia respecto al valor real.
El **error absoluto** mide la diferencia directa, mientras que el **error relativo** normaliza esta diferencia respecto a la magnitud de la solución.
Identificar las fuentes de error (truncamiento por series finitas o redondeo por límites de hardware) es crítico para garantizar la estabilidad de los algoritmos y evitar la divergencia en simulaciones de largo plazo.

## Resolución de sistemas no lineales

Hallar las raíces de una ecuación $f(x) = 0$ es un desafío recurrente.
- **Métodos Cerrados:** Como la **Bisección**, garantizan la convergencia si se conoce un intervalo donde la función cambia de signo.
- **Métodos Abiertos:** Como **Newton-Raphson**, utilizan la derivada local para acelerar la búsqueda mediante la fórmula $x_{n+1} = x_n - f(x_n)/f'(x_n)$.
Aunque los métodos abiertos son más veloces, requieren una buena aproximación inicial para no divergir hacia soluciones erróneas.

## Integración y derivación numérica

Cuando una función es difícil de integrar analíticamente o solo se dispone de datos puntuales, se recurre a la integración numérica.
La **Regla del Trapecio** y la **Regla de Simpson** aproximan el área bajo la curva mediante polinomios de bajo grado.
Para la derivación, se utilizan diferencias finitas (hacia adelante, atrás o centradas), basándose en la expansión de la Serie de Taylor para estimar la tasa de cambio con un error controlado.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $x^*$ | Raíz exacta | escalar |
| $\varepsilon$ | Tolerancia | constante |
| $e_n$ | Error relativo | escalar |
| $h$ | Paso de malla | escalar |
| $f(x)$ | Función objetivo | función |
| $J$ | Jacobiano | matriz |
| $\int_Q$ | Integral num. | operador |
| $\Delta x$ | Incremento | diferencial |
| $P_n(x)$ | Polinomio aprox. | función |
