---
id: msc53_geometria_diferencial
title: "Geometría diferencial"
pilar: "04_espacio_forma"
msc_code: "53-01"
tags: [variedades, curvas, curvatura, frenet]
nivel: avanzado
updated: "2026-04-26"
status: "stable"
---

# Geometría diferencial

![Triedro de Frenet en una helice 3D](geometria_diferencial_frenet)

La geometría diferencial es la disciplina que utiliza las herramientas del cálculo diferencial e integral para estudiar las propiedades locales y globales de las formas geométricas.
A diferencia de la geometría clásica, esta rama se enfoca en la curvatura, la torsión y las propiedades que pueden variar suavemente punto a punto.

## Curvas parametrizadas

Una curva se define mediante una función vectorial $\gamma(t)$ que mapea un intervalo de tiempo al espacio euclidiano.
El estudio de estas curvas se basa en el **Triedro de Frenet-Serret**, un conjunto de tres vectores unitarios ortogonales (Tangente, Normal y Binormal) que acompañan al punto móvil.
La **curvatura** $\kappa$ mide cuánto se desvía la curva de ser una línea recta, mientras que la **torsión** $\tau$ mide cuánto se aleja de estar contenida en un plano.
Estas dos funciones escalares determinan unívocamente la forma de la curva en el espacio tridimensional.

## Superficies y formas fundamentales

Una superficie en el espacio se analiza localmente mediante su **Plano Tangente**.
Este plano representa la mejor aproximación lineal de la superficie en la vecindad de un punto.
Para describir la métrica intrínseca y la curvatura de la superficie, se utilizan las **Formas Fundamentales**.
La Primera Forma Fundamental permite calcular longitudes de arco y áreas sobre la superficie, mientras que la Segunda Forma Fundamental mide cómo la superficie se dobla dentro del espacio ambiente.
Esto da lugar al concepto de **Curvatura de Gauss**, una propiedad intrínseca que no cambia si la superficie se dobla sin estirarse (Teorema Egregium).

## Variedades (introducción)

El concepto de variedad (manifold) generaliza la noción de curva y superficie a dimensiones superiores y espacios abstractos.
Una variedad es un espacio que localmente se comporta como el espacio euclidiano $\mathbb{R}^n$, permitiendo el desarrollo del cálculo diferencial en su superficie.
Este marco es fundamental en la física moderna, especialmente en la Relatividad General, donde el universo se modela como una variedad de cuatro dimensiones cuya curvatura representa la gravedad.
El estudio de las variedades requiere de herramientas avanzadas como el cálculo tensorial y la noción de conexión para comparar vectores en diferentes puntos.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $\gamma(t)$ | Trayectoria | vector |
| $\kappa$ | Curvatura | escalar |
| $\tau$ | Torsión | escalar |
| $\vec{T}, \vec{N}, \vec{B}$ | Triedro Frenet | vector |
| $g_{ij}$ | Métrica | tensor |
| $K$ | Curvatura Gauss | escalar |
