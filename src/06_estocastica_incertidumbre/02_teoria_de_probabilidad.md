---
id: msc60_teoria_de_probabilidad
title: "Teoría de probabilidad"
pilar: "06_estocastica_incertidumbre"
msc_code: "60-01"
tags: [probabilidad, azar, bayes, aleatoria]
nivel: intro
updated: "2026-04-26"
status: "stable"
---

# Teoría de probabilidad

![Visualizacion de la campana de Gauss](distribucion_normal.svg)

La teoría de probabilidad es el marco matemático que permite cuantificar la incertidumbre y modelar fenómenos donde el azar desempeña un papel determinante.
Desde el diseño de experimentos hasta la inteligencia artificial, esta disciplina proporciona las leyes que rigen los eventos aleatorios y su comportamiento a largo plazo.

## Axiomas de probabilidad

La probabilidad moderna se fundamenta en los axiomas de Kolmogórov, que definen una medida de probabilidad sobre un espacio muestral.
1. La probabilidad de cualquier evento es un número no negativo: $P(A) \geq 0$.
2. La probabilidad del espacio muestral completo es la unidad: $P(S) = 1$.
3. Para eventos mutuamente excluyentes, la probabilidad de la unión es la suma de sus probabilidades individuales.
Estas reglas simples permiten derivar teoremas complejos que aseguran la consistencia lógica de cualquier modelo estocástico, estableciendo que la probabilidad total siempre se conserva.

## Probabilidad condicional y teorema de Bayes

La probabilidad condicional mide la verosimilitud de un evento $A$ dado que ya ha ocurrido otro evento $B$.
Se define como $P(A|B) = P(A \cap B) / P(B)$, asumiendo que $P(B) > 0$.
Esta noción es la base del **Teorema de Bayes**, una herramienta fundamental para actualizar nuestras creencias a medida que obtenemos nueva evidencia.
Bayes permite invertir la condicionalidad, calculando la probabilidad de una causa dada una consecuencia observada.
Este razonamiento es el motor detrás de los clasificadores modernos y los sistemas de filtrado de información.

## Variables aleatorias discretas y continuas

Una variable aleatoria es una función que asigna un valor numérico al resultado de un experimento aleatorio.
- **Discretas:** Toman valores aislados, como el resultado de lanzar un dado. Se describen mediante funciones de masa de probabilidad.
- **Continuas:** Pueden tomar cualquier valor dentro de un intervalo real, como la estatura de una persona o el tiempo de espera.
Para las variables continuas, utilizamos funciones de densidad de probabilidad ($f(x)$), donde la probabilidad de un intervalo se calcula mediante la integral del área bajo la curva.
La **Distribución Normal** es el ejemplo más importante debido al Teorema del Límite Central, que afirma que la suma de muchas variables independientes tiende a seguir esta forma acampanada.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $P(A)$ | Probabilidad | escalar |
| $E[X]$ | Esperanza | escalar |
| $\sigma^2$ | Varianza | escalar |
| $f(x)$ | Densidad | función |
| $\Omega$ | Espacio muestral | conjunto |
| $A \cap B$ | Intersección | evento |
