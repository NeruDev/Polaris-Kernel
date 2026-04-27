---
id: msc26_funciones_y_limites
title: "Funciones y Límites"
pilar: "03_analisis_continuidad"
msc_code: "26-XX"
tags: [funciones, limites, sucesiones, continuidad]
nivel: intro
updated: "2026-04-26"
status: "stable"
---

# Funciones y Límites

![Definición visual de límite de una función](limite_concepto.svg)


## Tipos de funciones y composición

*(Pendiente de expansión detallada sobre funciones base)*

## Sucesiones y series

*(Pendiente de expansión detallada)*

## Límites y continuidad

### Concepto de Límite

El **límite** de $f(x)$ cuando $x$ tiende a $a$ es $L$ si los valores de $f(x)$ se aproximan arbitrariamente a $L$ cuando $x$ se aproxima a $a$ (sin ser igual a $a$).

$$\lim_{x \to a} f(x) = L$$

### Definición Formal (Épsilon-Delta)

$$\lim_{x \to a} f(x) = L$$
si y solo si: para todo $\varepsilon > 0$, existe un $\delta > 0$ tal que:
$$0 < \lvert x - a \rvert < \delta \Rightarrow \lvert f(x) - L \rvert < \varepsilon$$

### Límites Laterales

El límite existe si y solo si ambos límites laterales existen y son iguales:
$$\lim_{x \to a} f(x) = L \quad \Leftrightarrow \quad \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = L$$

### Técnicas de Evaluación y Formas Indeterminadas

Cuando la sustitución directa produce formas como $\frac{0}{0}$ o $\frac{\infty}{\infty}$, se utilizan técnicas como:
- **Factorización** y cancelación.
- **Racionalización** (multiplicación por el conjugado).
- **Límites trigonométricos fundamentales**: $\lim_{x \to 0} \frac{\sin x}{x} = 1$.

### Continuidad

Una función $f$ es **continua en $a$** si cumple tres condiciones:
1. $f(a)$ está definida.
2. $\lim_{x \to a} f(x)$ existe.
3. $\lim_{x \to a} f(x) = f(a)$.

#### Tipos de Discontinuidad
- **Removible**: El límite existe pero el punto no o es diferente.
- **Salto**: Los límites laterales existen pero son diferentes.
- **Infinita**: Al menos un límite lateral es $\pm\infty$ (asíntota vertical).

### Teorema del Valor Intermedio (TVI)
Si $f$ es continua en $[a, b]$ y $k$ es cualquier valor entre $f(a)$ y $f(b)$, entonces existe al menos un $c \in (a, b)$ tal que $f(c) = k$.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $L$ | Valor del límite | escalar |
| $\varepsilon$ | Error en el rango | constante |
| $\delta$ | Margen en el dominio | constante |
| $x \to a$ | Tendencia de $x$ | relación |
