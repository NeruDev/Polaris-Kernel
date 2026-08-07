---
id: "msc00_readme"
title: "README"
pilar: "05_discrecion_computacion"
msc_code: "00-00"
status: "draft"
---
# Pilar 05: Discreción y Computación - Registro de Activos Gráficos

Este documento describe el estándar utilizado para la generación de imágenes y gráficos dentro de este pilar, así como los parámetros clave de los scripts origen para facilitar su futuro mantenimiento y escalabilidad.

## Formato y Configuración General

- **Motor de Renderizado:** Typst (v0.15.1)
- **Librería de Dibujo:** `@preview/cetz:0.3.3`
- **Formato de Salida:** Scalable Vector Graphics (`.svg`)
- **Directorio de Fuentes:** `scripts/grafics/typst_src/`
- **Prefijo de Archivos:** `05_discrecion_computacion___`

Para este pilar, especializado en informática teórica y matemáticas discretas, predomina el uso de grafos, árboles jerárquicos y trazados temporales (asintóticos).

---

## Gráficos del Pilar 5 y sus Parámetros Clave

### 1. Teoría de Grafos (`grafos_conceptos.svg`)
Ilustración de nodos conectados por aristas dirigidas/no dirigidas (vértices y relaciones).
- **Parámetros:** La matriz de adyacencia visual se construye posicionando los nodos.
Las aristas deben anclarse a los centros o bordes perimetrales de los nodos.
Para grafos ponderados, agregar `content()` en el punto medio geométrico de las líneas.

### 2. Autómatas y Computación
- **`automata_estados_finitos.svg`**: Máquina de estados (DFA/NFA) con transiciones.
  - Ajustes de `arc(...)` y `bezier()` entre nodos circulares (`circle()`) garantizan que las aristas de ida y vuelta no colisionen.
- **`teoria_computacion_turing.svg`**: Modelo esquemático de una cinta infinita y la cabeza de lectura/escritura de una Máquina de Turing. 

### 3. Criptografía y Aritmética Modular
- **`aritmetica_modular_aplicada.svg`**: Un reloj circular modular.
  - **Parámetros:** `mod-val = 12` controla las particiones.
Si se cambia, los grados del bucle y los textos se adaptan solos.
El radio base `r = 3.5` da suficiente margen a las etiquetas perimetrales.
- **`criptografia_rsa_flujo.svg`**: Diagrama de flujo de cifrado asimétrico (llaves públicas/privadas). Basado fuertemente en bloques de texto posicionados con alineación central (`rect()` más flechas interconectadas).

### 4. Algoritmos y Complejidad
- **`analisis_complejidad.svg`**: Curvas asintóticas Big-O (e.g. $O(n)$, $O(\log n)$, $O(2^n)$).
  - **Parámetros:** Cada clase de complejidad está graficada mediante ecuaciones de `calc`. Para $2^n$, se requiere control estricto de truncamiento en el eje $y$ (`y-max`) para que no rompa el diseño del lienzo debido al crecimiento exponencial.
- **`relaciones_recurrencia.svg`**: Árbol de recursión (Master Theorem, ej.
MergeSort $T(n/2)$).
  - **Parámetros:** Amplia separación en las ramas `(x, y)` para los niveles del árbol.
Los nodos hijos `l1`, `r1`, `l2` abren en un ancho considerable para que las etiquetas no colapsen en niveles más profundos.
