---
id: msc51_trigonometria
title: "Trigonometría Fundamental"
pilar: "04_espacio_forma"
msc_code: "51-01"
tags: [trigonometria, identidad, triangulos, ondas]
nivel: intro
updated: "2026-04-26"
status: "stable"
---

# Trigonometría Fundamental

![Comparativa de funciones seno y coseno](graficas_seno_coseno.svg)


![Comparativa de funciones trigonométricas](grafica_seno_coseno.svg)

La trigonometría es el estudio de las relaciones entre los ángulos y los lados de los triángulos.
Más allá de los triángulos, esta disciplina proporciona las funciones periódicas necesarias para modelar ondas, vibraciones y ciclos en la naturaleza y la tecnología.

## Razones y círculo unitario

Las razones trigonométricas (seno, coseno y tangente) se definen originalmente en un triángulo rectángulo.
Para un ángulo $\theta$:
- **$\sin \theta$:** Cateto opuesto / hipotenusa.
- **$\cos \theta$:** Cateto adyacente / hipotenusa.
- **$\tan \theta$:** Cateto opuesto / cateto adyacente.
El **Círculo Unitario** generaliza estas funciones para cualquier ángulo real, donde las coordenadas de un punto en el círculo de radio 1 son $(\cos \theta, \sin \theta)$.
Esta perspectiva circular permite entender la periodicidad y el comportamiento oscilatorio de las funciones.

## Identidades trigonométricas

Las identidades son igualdades que se cumplen para cualquier valor del ángulo.
La identidad fundamental es la **Identidad Pitagórica**:
$$\sin^2 \theta + \cos^2 \theta = 1$$
Otras identidades importantes permiten calcular funciones de suma de ángulos, ángulos dobles y relaciones recíprocas (secante, cosecante, cotangente).
Estas leyes son fundamentales para simplificar expresiones en cálculo integral y para la resolución de ecuaciones en el dominio de la frecuencia (Análisis de Fourier).

## Ley de senos y cosenos

Para resolver triángulos que no son rectángulos (triángulos oblicuángulos), se utilizan las leyes de senos y cosenos.
- **Ley de Senos:** $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$. Es útil cuando se conocen dos ángulos y un lado.
- **Ley de Cosenos:** $c^2 = a^2 + b^2 - 2ab \cos C$. Es una generalización del teorema de Pitágoras para cualquier ángulo.
Estas leyes permiten triangular posiciones en navegación y geodesia, siendo la base tecnológica de los sistemas de posicionamiento global (GPS).

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $\theta$ | Ángulo | variable |
| $\sin, \cos$ | Funciones base | función |
| $\tan$ | Tangente | función |
| $r$ | Radio vector | escalar |
| $\pi$ | Constante pi | constante |
| $A, B, C$ | Ángulos internos | escalar |