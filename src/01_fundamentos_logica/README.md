---
id: "msc00_readme"
title: "README"
pilar: "01_fundamentos_logica"
msc_code: "00-00"
status: "draft"
---
# Pilar 01: Fundamentos y Lógica - Registro de Activos Gráficos

Este documento describe el estándar utilizado para la generación de imágenes y gráficos dentro de este pilar, así como los parámetros clave de los scripts origen para facilitar su futuro mantenimiento y escalabilidad.

## Formato y Configuración General

- **Motor de Renderizado:** Typst (v0.15.1)
- **Librería de Dibujo:** `@preview/cetz:0.3.2` (o superior)
- **Formato de Salida:** Scalable Vector Graphics (`.svg`)
- **Directorio de Fuentes:** `scripts/grafics/typst_src/`
- **Prefijo de Archivos:** `01_fundamentos_logica___`

Las imágenes de este pilar están diseñadas utilizando el lienzo de `cetz` (`#cetz.canvas`), el cual permite posicionar elementos usando un sistema de coordenadas cartesiano `(x, y)`. Se fomenta el uso de colores de la paleta oficial y trazados consistentes.

---

## Gráficos del Pilar 1 y sus Parámetros Clave

A continuación se detallan los gráficos pertenecientes a este pilar y las variables o enfoques principales que rigen sus scripts `.typ`:

### 1. Funciones y Mapeos (`funciones_y_mapeos.svg`)
Ilustra las relaciones inyectiva, sobreyectiva y biyectiva mediante conjuntos (diagramas de Venn).
- **Estructura:** Se posicionan 3 bloques principales (Inyectiva, Sobreyectiva, Biyectiva) a lo largo del eje X.
- **Parámetros a ajustar:**
  - `circle(..., radius: (rx, ry))`: Controla la forma elíptica de los conjuntos.
Si se requieren más elementos, incrementa el valor de `ry`.
  - `content((x, y), [texto])`: Posiciona los elementos dentro de los conjuntos.
Asegúrate de modificar `y` espaciadamente para evitar superposiciones.
  - `line("origen.east", "destino.west", mark: (end: ">"))`: Dibuja las flechas de mapeo anclándose automáticamente a los bordes de los nodos nombrados.

### 2. Inducción Matemática (`induccion_matematica.svg`)
Representa el principio de inducción mediante un efecto dominó, ilustrando el caso base y el paso inductivo.
- **Estructura:** Utiliza bloques `group({ ... })` para aislar las transformaciones de cada ficha de dominó individual.
- **Parámetros a ajustar:**
  - `translate((x, 0))`: Define la posición horizontal de la ficha en la línea de tiempo.
Incrementa `x` para separar más las fichas.
  - `rotate(angulo)`: Controla la inclinación de la ficha (ej. `-25deg` para una ficha cayendo, `0deg` para una en reposo).
  - `rect((-0.2, 0), (0.2, 1.8))`: Modifica el ancho y alto estandarizado de todas las fichas.

### 3. Lógica de Predicados e Inferencia (`logica_predicados_inferencia.svg`)
Dibuja un Árbol de Derivación Formal (Modus Ponens y Adición).
- **Estructura:** Uso de anclas (anchors) de posicionamiento semántico mediante nombres de nodos.
- **Parámetros a ajustar:**
  - `rect((x1, y1), (x2, y2), name: "Nombre")`: Define el tamaño y posición de las cajas de premisas/conclusiones.
Amplía estas coordenadas si el texto interior se desborda.
  - `line("NodoA.south", "NodoB.north")`: La conexión de flechas es relativa (sur a norte). Si cambias los nodos de posición, las flechas se adaptarán automáticamente sin necesidad de re-calcular coordenadas cartesianas.

---
*Nota: Para recompilar cualquier gráfico tras modificar sus parámetros, utiliza el comando `typst compile "ruta/al/script.typ" "ruta/al/output.svg"` desde la raíz del proyecto.*
