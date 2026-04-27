---
id: msc60_modelos_estocasticos
title: "Modelos estocásticos"
pilar: "06_estocastica_incertidumbre"
msc_code: "60-01"
tags: [markov, poisson, procesos, tiempo]
nivel: avanzado
updated: "2026-04-26"
status: "stable"
---

# Modelos estocásticos

![Diagrama de transicion de estados de una cadena de Markov](markov_estados.svg)

Los modelos estocásticos estudian sistemas que evolucionan de forma aleatoria a lo largo del tiempo o el espacio.
A diferencia de los modelos deterministas, estos capturan la variabilidad inherente a los sistemas dinámicos, permitiendo predecir comportamientos promedio y estados de equilibrio en entornos de alta incertidumbre.

## Cadenas de Markov

Una cadena de Markov es un proceso estocástico donde el futuro depende exclusivamente del estado presente y no de la historia pasada (propiedad de falta de memoria o Markoviana).
Se modelan mediante **Matrices de Transición**, que indican la probabilidad de saltar de un estado a otro en un solo paso.
Estas estructuras son la base de los algoritmos de búsqueda (como el PageRank de Google), el modelado de mercados financieros y el procesamiento del lenguaje natural, donde la secuencia de palabras se rige por probabilidades de transición condicionadas.
El análisis de largo plazo permite identificar el "Estado Estacionario", que es la configuración hacia la cual tiende el sistema sin importar su punto de partida.

## Procesos de Poisson

El proceso de Poisson modela la llegada de eventos independientes en un intervalo continuo de tiempo o espacio.
Se caracteriza por una tasa de llegada ($\lambda$) constante y es la base de la teoría de colas y el análisis de fiabilidad.
Propiedades críticas incluyen que el tiempo entre eventos sucesivos sigue una distribución exponencial, lo que refuerza la noción de eventos que ocurren al azar y sin coordinación.
Este modelo es vital para dimensionar servidores de red, diseñar salas de urgencias en hospitales y predecir fallos en componentes industriales, permitiendo optimizar el uso de recursos ante una demanda impredecible.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $X_t$ | Estado en tiempo t | variable |
| $P$ | Matriz transición | matriz |
| $\pi$ | Vector estacionario | vector |
| $\lambda$ | Tasa de llegada | escalar |
| $N(t)$ | Conteo de eventos | entero |
| $\tau$ | Tiempo inter-arribo | escalar |
