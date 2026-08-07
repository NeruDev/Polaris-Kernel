# Pilar 02: Estructuras Algebraicas - Registro de Activos Gráficos

Este documento describe el estándar utilizado para la generación de imágenes y gráficos dentro de este pilar, así como los parámetros clave de los scripts origen para facilitar su futuro mantenimiento y escalabilidad.

## Formato y Configuración General

- **Motor de Renderizado:** Typst (v0.15.1)
- **Librería de Dibujo:** `@preview/cetz:0.3.2` (o superior)
- **Formato de Salida:** Scalable Vector Graphics (`.svg`)
- **Directorio de Fuentes:** `scripts/grafics/typst_src/`
- **Prefijo de Archivos:** `02_estructuras_algebraicas___`

Todos los gráficos se diseñan bajo el entorno de `cetz.canvas()`.

---

## Gráficos del Pilar 2 y sus Parámetros Clave

A continuación se detallan los gráficos pertenecientes a este pilar y las variables o enfoques principales que rigen sus scripts `.typ`:

### 1. Diagrama Conmutativo (`diagrama_conmutativo.svg`)
Dibuja un diagrama categórico entre objetos A, B y C mostrando morfismos $f, g$ y su composición.
- **Estructura:** Nodos de texto y conexiones relativas.
- **Parámetros a ajustar:**
  - `content((x, y), [$A$], name: "A")`: Coordenadas absolutas de los objetos. Si el diagrama requiere más objetos (D, E), simplemente agrega nuevas coordenadas en el plano.
  - `line("A.east", "B.west", ...)`: Las flechas usan anclajes cardinales. Cambiar las direcciones si los nodos se mueven.
  - `arc(..., start, delta, radius)`: Controla el arco curvo central que indica la conmutatividad.

### 2. Ecuaciones y Desigualdades (`ecuaciones_y_desigualdades.svg`)
Ilustra el punto de intersección de un sistema de ecuaciones lineales de $2 \times 2$.
- **Estructura:** Trazado de líneas rectas y proyecciones punteadas sobre ejes Cartesianos.
- **Parámetros a ajustar:**
  - `line((x1, y1), (x2, y2))`: Define las coordenadas de inicio y fin de las rectas numéricas limitando con los ejes.
  - `circle((x, y), radius)`: Señala el punto de intersección exacto. Modificar si cambian las ecuaciones del modelo.

### 3. Espacios Vectoriales y Bases (`espacios_vectoriales_bases.svg`)
Muestra cómo dos vectores base ($v_1, v_2$) construyen un vector resultante $u$ mediante combinaciones lineales.
- **Estructura:** Rejilla (`grid`) de fondo y vectores como líneas con `mark: (end: ">")`.
- **Parámetros a ajustar:**
  - `grid((0,0), (x, y))`: Expande o reduce la cuadrícula del plano.
  - Puntos finales de los vectores `v1`, `v2` y `u`: Modificar directamente las coordenadas en los comandos `line()`. Si el espacio cambia, actualizar correspondientemente las proyecciones (líneas punteadas).

### 4. Jerarquía de Estructuras (`jerarquia_estructuras.svg`)
Un diagrama de flujo vertical que traza la especialización desde un Grupo hasta un Campo/Cuerpo.
- **Estructura:** Cajas redondeadas apiladas en el eje $y$, conectadas por flechas descendentes.
- **Parámetros a ajustar:**
  - `rect((x1, y1), (x2, y2), ..style-box(...))`: Las coordenadas delimitan la altura y anchura del contenedor del texto. Si se agrega un nuevo nodo, usar una nueva ventana en el eje $y$ negativo.
  - `style-box`: Variable local para inyectar configuración unificada de estilo, incluyendo el color (`fill`).

### 5. Polinomios y Factorización (`polinomios_y_factorizacion.svg`)
Dibuja el comportamiento continuo de un polinomio cruzando por sus raíces.
- **Estructura:** Uso intensivo de curvas Bezier interconectadas.
- **Parámetros a ajustar:**
  - `bezier((start), (end), (control))`: Si se requieren nuevas formas del polinomio, los puntos de control modifican la curvatura.
  - `circle(..., fill: red)`: Posiciones específicas en $y=0$ donde el polinomio cruza el eje.

### 6. Transformación Lineal (`transformacion_lineal.svg`)
Contrasta visualmente una cuadrícula estándar (dominio) contra una cuadrícula cizallada (codominio).
- **Estructura:** Dos grupos de dibujo (`group({ ... })`) separados por una traslación.
- **Parámetros a ajustar:**
  - `translate((x, y))`: Controla la separación entre el plano original y el transformado.
  - Generación de rejillas iterando en un rango (`for x in range(...)`). En el plano transformado, las coordenadas dependen directamente de las transformaciones matriciales (ej. $x' = x + y$). Si se cambia la matriz de transformación, ajustar estas ecuaciones del bloque `for`.
