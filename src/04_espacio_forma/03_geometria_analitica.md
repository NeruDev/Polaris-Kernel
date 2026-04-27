---
id: msc51_geometria_analitica
title: "Geometría analítica"
pilar: "04_espacio_forma"
msc_code: "51-01"
tags: [analitica, conicas, coordenadas]
nivel: intro
updated: "2026-04-26"
status: "stable"
---

# Geometría analítica

![Representacion de elipse y parabola](conicas_analitica.svg)

La geometría analítica es la rama de las matemáticas que vincula el álgebra con la geometría mediante el uso de un sistema de coordenadas.
Esta potente herramienta permite representar figuras geométricas mediante ecuaciones algebraicas, facilitando el análisis de sus propiedades mediante el cálculo numérico y simbólico.

## Sistema de coordenadas y vectores

El marco de referencia fundamental es el sistema de coordenadas cartesianas, definido por ejes ortogonales que se intersectan en el origen.
En el plano $\mathbb{R}^2$, cada punto queda unívocamente determinado por un par ordenado $(x, y)$.
Los vectores en este sistema se representan como flechas con magnitud y dirección, siendo cruciales para describir traslaciones y fuerzas físicas.
La distancia entre dos puntos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$ se deriva del teorema de Pitágoras:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

## La recta y el plano

Una recta en el plano puede describirse mediante una ecuación lineal de primer orden.
La forma más común es la ecuación punto-pendiente:
$$y - y_1 = m(x - x_1)$$
Donde $m$ representa la pendiente o inclinación de la recta respecto al eje horizontal.
En el espacio tridimensional $\mathbb{R}^3$, la recta requiere de ecuaciones paramétricas, mientras que el plano se define mediante una ecuación lineal en tres variables de la forma $Ax + By + Cz + D = 0$.

## Cónicas y superficies cuádricas

Las cónicas son figuras que resultan de la intersección de un plano con un cono circular recto.
Dependiendo del ángulo de inclinación del plano, se obtienen cuatro formas fundamentales:
1. **Circunferencia:** Intersección perpendicular al eje del cono.
2. **Elipse:** Intersección en ángulo oblicuo que cierra la curva.
3. **Parábola:** Intersección paralela a una generatriz del cono.
4. **Hipérbola:** Intersección que corta ambas hojas del cono.

Cada una de estas curvas tiene una ecuación característica de segundo grado.
Por ejemplo, la elipse centrada en el origen se rige por:
$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$
Estas curvas no solo son curiosidades geométricas, sino que modelan fenómenos naturales críticos como las órbitas planetarias (elipses) y la trayectoria de proyectiles (parábolas).

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $m$ | Pendiente | escalar |
| $(x, y)$ | Coordenadas | par ordenado |
| $d$ | Distancia | escalar |
| $a, b$ | Semiejes | constante |
| $\vec{v}$ | Vector | estructura |
