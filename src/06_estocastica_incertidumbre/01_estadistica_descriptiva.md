---
id: msc62_estadistica_descriptiva
title: "Estadística descriptiva"
pilar: "06_estocastica_incertidumbre"
msc_code: "62-01"
tags: [estadistica, datos, medidas, tendencia]
nivel: intro
updated: "2026-05-24"
status: "stable"
---

# Estadística descriptiva

![Histograma de frecuencias](histograma_ejemplo.svg)


![Grafico de barras para analisis de datos](estadistica_barras.svg)

La estadística descriptiva es una disciplina esencial que se encarga de recolectar, organizar, visualizar y resumir conjuntos de datos empíricos.
A diferencia de la estadística inferencial, su propósito principal no es formular conclusiones matemáticas generalizadas sobre una población, sino detallar y presentar exhaustivamente las características observables de la muestra analizada.
Constituye el primer paso fundamental en cualquier análisis de ciencia de datos moderno, revelando la estructura oculta detrás de la información bruta.

## Medidas de tendencia central

Estas métricas estadísticas resumen y localizan el centroide numérico en torno al cual se agrupan las observaciones del conjunto de datos.
- **Media ($\mu$):** Es el promedio aritmético tradicional que se obtiene al sumar todos los valores y dividir el resultado entre el tamaño total de la muestra.
- **Mediana:** Representa el valor posicional central que divide exactamente a la mitad la distribución de datos una vez que estos han sido ordenados de menor a mayor magnitud.
- **Moda:** Identifica el valor o categoría que exhibe la mayor frecuencia absoluta de aparición dentro del conjunto de datos.

## Medidas de dispersión

La tendencia central por sí sola es insuficiente para describir los datos, por lo que se requiere medir el nivel de propagación o variabilidad.
- **Varianza ($\sigma^2$):** Es el promedio de las diferencias cuadráticas que existen entre cada dato individual y la media aritmética del conjunto.
- **Desviación estándar ($\sigma$):** Se calcula como la raíz cuadrada positiva de la varianza.
Esta medida es especialmente intuitiva en el análisis práctico porque comparte exactamente las mismas unidades de medida originales que los datos recolectados.
- **Rango:** Constituye la diferencia matemática directa entre el valor máximo observado y el valor mínimo presente en la distribución.
- **Rango intercuartílico (IQR):** Mide la dispersión del cincuenta por ciento central de los datos, calculándose como la diferencia entre el tercer y el primer cuartil, lo cual ofrece gran robustez ante valores atípicos.

## Medidas de forma

Para comprender la geometría y el perfil de la distribución empírica, se emplean estadísticos analíticos superiores que evalúan su comportamiento en relación a la curva normal ideal.
- **Asimetría (Skewness):** Cuantifica la falta de simetría estructural de la distribución de los datos alrededor de su media aritmética.
Una distribución con asimetría positiva posee una cola larga que se extiende hacia los valores más altos a la derecha, mientras que una asimetría negativa indica lo contrario.
- **Curtosis:** Mide el peso o la concentración estadística que existe en las colas de la distribución en comparación con su centro.
Una curtosis elevada (leptocúrtica) sugiere la presencia frecuente de datos atípicos extremos, un aspecto crítico en el modelado de riesgos financieros y fiabilidad de sistemas.

## Distribuciones de frecuencia

La organización categórica de los datos es la base de las distribuciones de frecuencia empíricas.
Consiste en la agrupación estructurada de las observaciones en intervalos de clase, registrando la cantidad de incidencias absolutas y relativas en cada segmento.
Estos datos se visualizan predominantemente mediante histogramas o diagramas de caja (boxplots).
Dichas representaciones gráficas son imprescindibles porque permiten a los analistas discernir visualmente de inmediato la distribución subyacente, evidenciando posibles bimodalidades, sesgos marcados o la presencia de errores sistemáticos en la medición de la muestra original.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $N$ | Tamaño población | entero |
| $n$ | Tamaño muestra | entero |
| $\mu$ | Media poblacional | escalar |
| $\bar{x}$ | Media muestral | escalar |
| $\sigma^2$ | Varianza | escalar |
| $\sigma$ | Desviación estándar | escalar |
| $\sum$ | Sumatoria | operador |