---
id: msc26_calculo_integral
title: "Cálculo Integral"
pilar: "03_analisis_continuidad"
msc_code: "26-XX"
tags: [integrales, antiderivada, area]
nivel: intro
updated: "2026-04-26"
status: "stable"
---

# Cálculo Integral

![Área bajo la curva y sumas de Riemann](integral_area.svg)


## Antiderivada e Integral Indefinida

### Concepto de Antiderivada

Una función $F(x)$ es una **antiderivada** de $f(x)$ si $F'(x) = f(x)$. La integral indefinida representa el conjunto de todas las antiderivadas:
$$\int f(x) \, dx = F(x) + C$$
donde $C$ es la **constante de integración**.

### Reglas básicas
- **Potencia**: $\int x^n \, dx = \frac{x^{n+1}}{n+1} + C$ (para $n \neq -1$).
- **Logarítmica**: $\int \frac{1}{x} \, dx = \ln|x| + C$.
- **Exponencial**: $\int e^x \, dx = e^x + C$.
- **Trigonométricas**: $\int \sin x \, dx = -\cos x + C$ y $\int \cos x \, dx = \sin x + C$.

## Teorema Fundamental del Cálculo

Establece la conexión entre la derivación y la integración.

### Primera parte
Si $f$ es continua en $[a, b]$, la función $g(x) = \int_a^x f(t) \, dt$ es continua en $[a, b]$ y diferenciable en $(a, b)$, y $g'(x) = f(x)$.

### Segunda parte (Evaluación)
$$\int_a^b f(x) \, dx = F(b) - F(a)$$
donde $F$ es cualquier antiderivada de $f$.

## Técnicas de integración

*(Pendiente de expansión detallada)*
- **Sustitución** (Cambio de variable).
- **Integración por partes**.
- **Fracciones parciales**.
- **Sustitución trigonométrica**.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $\int$ | Símbolo de integral | operador |
| $C$ | Constante de integración | constante |
| $F(x)$ | Función primitiva | función |
| $dx$ | Diferencial de x | diferencial |