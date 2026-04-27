---
id: msc62_estadistica_inferencial
title: "Estadística inferencial"
pilar: "06_estocastica_incertidumbre"
msc_code: "62-01"
tags: [inferencia, hipotesis, intervalos, significancia]
nivel: intermedio
updated: "2026-04-26"
status: "stable"
---

# Estadística inferencial

![Visualizacion del margen de error y nivel de confianza](intervalo_confianza.svg)

La estadística inferencial es la rama que permite extraer conclusiones sobre una población a partir del análisis de una muestra representativa.
Mediante el uso de modelos de probabilidad, esta disciplina cuantifica la incertidumbre de las estimaciones y proporciona un marco riguroso para la toma de decisiones basada en evidencia.

## Distribuciones muestrales

Una distribución muestral es la distribución de probabilidad de un estadístico (como la media) calculado a partir de múltiples muestras de una población.
El **Teorema del Límite Central** es el núcleo de la inferencia: establece que la media de una muestra de tamaño suficiente tiende a seguir una distribución normal, independientemente de la forma original de la población.
Esta propiedad asombrosa permite aplicar métodos paramétricos incluso cuando los datos originales son complejos o desconocidos, facilitando el cálculo de errores estándar y márgenes de error precisos.

## Estimación por intervalos

La estimación puntual rara vez coincide con el parámetro poblacional real.
Por ello, utilizamos **Intervalos de Confianza**, que proporcionan un rango de valores en el cual esperamos encontrar el parámetro con un cierto nivel de probabilidad (ej. 95%).
El ancho del intervalo depende de la variabilidad de los datos y del tamaño de la muestra; a mayor muestra, mayor es la precisión de la estimación.
Este concepto es vital en encuestas de opinión, control de calidad y experimentos científicos, donde reportar un rango de incertidumbre es más honesto y útil que un valor único.

## Pruebas de hipótesis

Las pruebas de hipótesis permiten evaluar afirmaciones sobre una población de forma objetiva.
El proceso comienza con una Hipótesis Nula ($H_0$), que representa el "status quo", y una Hipótesis Alternativa ($H_1$).
Calculamos un **p-valor**, que mide la probabilidad de observar los datos obtenidos si la hipótesis nula fuera cierta.
Si el p-valor es menor que un nivel de significancia prefijado ($\alpha$), rechazamos la hipótesis nula.
Este rigor procedimental es la base del método científico moderno, protegiéndonos contra el sesgo de confirmación y el descubrimiento de patrones que son simples coincidencias del azar.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $\mu$ | Media poblacional | escalar |
| $\bar{x}$ | Media muestral | escalar |
| $\sigma$ | Desviación estándar | escalar |
| $\alpha$ | Significancia | escalar |
| $p$ | p-valor | escalar |
| $H_0$ | Hipótesis nula | enunciado |
| $Z$ | Estadístico Z | escalar |
