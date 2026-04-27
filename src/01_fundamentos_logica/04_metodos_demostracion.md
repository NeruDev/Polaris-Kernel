---
id: msc03_metodos_demostracion
title: "Métodos de demostración"
pilar: "01_fundamentos_logica"
msc_code: "03-01"
tags: [demostracion, induccion]
nivel: intro
updated: "2026-04-26"
status: "stable"
---

# Métodos de demostración

![Metafora del domino para el principio de induccion](induccion_domino.svg)

Una demostración es una secuencia lógica de argumentos que establece la verdad 
de una proposición. En matemáticas, nada se acepta sin una prueba rigurosa 
basada en axiomas y teoremas previamente demostrados.

## Inducción matemática

Se usa para demostrar propiedades sobre los números naturales. Consta de dos 
pasos:
1. **Base:** Probar que la propiedad se cumple para $n = 1$.
2. **Paso Inductivo:** Supone que se cumple para $k$ y demuestra que entonces se 
cumple para $k+1$. Si ambos pasos son válidos, se cumple para todo $n$.

## Reducción al absurdo

Este método (también llamado *reductio ad absurdum*) consiste en suponer que la 
proposición que queremos demostrar es falsa. Si esto conduce a una contradicción 
lógica evidente, entonces la proposición original debe ser necesariamente 
verdadera.

## Demostración directa y contraposición

- **Directa:** Parte de las premisas P y llega a la conclusión Q mediante pasos 
lógicos sucesivos ($P \rightarrow Q$).
- **Contraposición:** En lugar de probar $P \rightarrow Q$, se demuestra que 
$\neg Q \rightarrow \neg P$, lo cual es lógicamente equivalente.

## Glosario de variables

| Símbolo | Nombre | Tipo |
| --- | --- | --- |
| $n$ | Variable natural | escalar |
| $\neg$ | Negación | conectivo |
| $\rightarrow$ | Implicación | relación |
| $\qed$ | Q.E.D. | marcador |
