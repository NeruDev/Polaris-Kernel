---
id: msc26_calculo_diferencial
title: "Cálculo Diferencial"
pilar: "03_analisis_continuidad"
msc_code: "26-XX"
tags: [derivadas, optimizacion, diferencial]
nivel: intro
updated: "2026-04-26"
status: "stable"
---

# Cálculo Diferencial

![Recta tangente y pendiente $f'(a)$](derivada_concepto.svg)


## Concepto de derivada

### Definición por Límite

La **derivada** de $f(x)$ en $x = a$ es la tasa de cambio instantánea de la función:
$$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$

Geométricamente, $f'(a)$ es la **pendiente** de la recta tangente a la gráfica de $f$ en el punto $(a, f(a))$.

### Interpretación Física
Si $s(t)$ es la función de posición, entonces:
- $v(t) = s'(t)$ es la **velocidad instantánea**.
- $a(t) = v'(t) = s''(t)$ es la **aceleración**.

## Reglas de derivación

| Regla | Fórmula |
| --- | --- |
| **Constante** | $\frac{d}{dx}[c] = 0$ |
| **Suma** | $(f \pm g)' = f' \pm g'$ |
| **Producto** | $(f \cdot g)' = f'g + fg'$ |
| **Cociente** | $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$ |
| **Cadena** | $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$ |

### Derivadas de funciones elementales
- $\frac{d}{dx}[x^n] = nx^{n-1}$
- $\frac{d}{dx}[e^x] = e^x$
- $\frac{d}{dx}[\ln x] = \frac{1}{x}$
- $\frac{d}{dx}[\sin x] = \cos x$
- $\frac{d}{dx}[\cos x] = -\sin x$

## Optimización y análisis de curvas

*(Pendiente de expansión sobre máximos, mínimos y puntos de inflexión)*

### Derivación Implícita y Logarítmica
Se utilizan cuando $y$ no está despejada o cuando la función es de la forma $f(x)^{g(x)}$.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $f'(x)$ | Primera derivada | función |
| $f''(x)$ | Segunda derivada | función |
| $\frac{dy}{dx}$ | Notación de Leibniz | operador |
| $h$ | Incremento infinitesimal | variable |