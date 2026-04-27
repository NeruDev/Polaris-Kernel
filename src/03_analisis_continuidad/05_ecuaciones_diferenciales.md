---
id: msc34_ecuaciones_diferenciales
title: "Ecuaciones diferenciales ordinarias (EDO)"
pilar: "03_analisis_continuidad"
msc_code: "34-01"
tags: [edo, laplace, primer_orden, superior]
nivel: intermedio
updated: "2026-04-26"
status: "stable"
---

# Ecuaciones diferenciales ordinarias (EDO)

![Campo de pendientes para una EDO de primer orden](edo_campo_direcciones.svg)

Una ecuación diferencial es una relación entre una función desconocida y sus 
derivadas. Son el lenguaje natural de la física, la biología y la ingeniería 
para describir cómo cambian los sistemas en el tiempo o el espacio.

## EDO de primer orden

Involucran solo la primera derivada $y'$. Existen métodos clásicos de resolución:
- **Separables:** $\frac{dy}{dx} = g(x)h(y)$. Se resuelven integrando cada lado.
- **Lineales:** $y' + P(x)y = Q(x)$. Requieren el uso de un **factor integrante** 
$\mu(x) = e^{\int P(x)dx}$.
- **Exactas:** Basadas en el diferencial total de una función de estado.
- **Bernoulli:** Ecuaciones no lineales que se pueden linealizar mediante 
una sustitución adecuada.

## EDO de orden superior

Las ecuaciones de segundo orden o mayor describen sistemas con inercia o 
aceleración. Las **EDO lineales con coeficientes constantes** son las más 
comunes; se resuelven hallando la solución homogénea mediante la ecuación 
característica y una solución particular basada en el término fuente $g(x)$.

## Transformada de Laplace

Es una herramienta integral que convierte una ecuación diferencial (dominio 
del tiempo) en una ecuación algebraica (dominio de la frecuencia). Es 
especialmente útil para resolver sistemas con entradas discontinuas o 
impulsivas (funciones de Heaviside y Delta de Dirac), simplificando el 
tratamiento de las condiciones iniciales.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $y(t)$ | Función incógnita | función |
| $y'$ | Derivada (cambio) | tasa |
| $\mu(x)$ | Factor integrante | función |
| $\mathcal{L}$ | Transformada Laplace | operador |
| $s$ | Frecuencia compleja | escalar |
| $k$ | Constante decaimiento | escalar |
