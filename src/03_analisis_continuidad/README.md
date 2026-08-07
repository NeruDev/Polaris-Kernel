---
id: "msc00_readme"
title: "README"
pilar: "03_analisis_continuidad"
msc_code: "00-00"
status: "draft"
---
# Pilar 03: Análisis y Continuidad - Registro de Activos Gráficos

Este documento describe el estándar utilizado para la generación de imágenes y gráficos dentro de este pilar, así como los parámetros clave de los scripts origen para facilitar su futuro mantenimiento y escalabilidad.

## Formato y Configuración General

- **Motor de Renderizado:** Typst (v0.15.1)
- **Librería de Dibujo:** `@preview/cetz:0.3.3`
- **Formato de Salida:** Scalable Vector Graphics (`.svg`)
- **Directorio de Fuentes:** `scripts/grafics/typst_src/`
- **Prefijo de Archivos:** `03_analisis_continuidad___`

Todos los gráficos se diseñan bajo el entorno de `cetz.canvas()`. Se promueve el uso de bucles (`for`) para calcular dinámicamente curvas matemáticas complejas sin necesidad de importar archivos externos.

---

## Gráficos del Pilar 3 y sus Parámetros Clave

### 1. Conceptos Básicos (Límite, Derivada, Integral)
- **`limite_concepto.svg`**: Muestra la aproximación asintótica.
Ajustar las flechas de acercamiento (límite por izquierda y derecha) usando las coordenadas de `line(..., mark: (end: ">"))`.
- **`derivada_concepto.svg`**: Muestra la pendiente de la recta tangente.
Si se altera la función base, asegurarse de recalcular y rotar la línea recta tangente en el punto de interés.
- **`integral_area.svg`**: Usa la propiedad `close: true` y `fill` en una ruta conformada por múltiples puntos de la curva para simular la región bajo el área.

### 2. Campos Vectoriales y Direccionales (EDOs y Análisis Multivariable)
- **`campo_vectorial.svg` / `edo_campo_direcciones.svg`**: 
  - **Estructura:** Se genera utilizando bucles anidados `for x in range(...)` y `for y in range(...)` para calcular la pendiente / vector en cada punto de la cuadrícula.
  - **Parámetros:** La longitud de los vectores (normalización) y la densidad de la rejilla.
Ajustar el paso del rango si el campo se ve demasiado sobrecargado.

### 3. Funciones Trascendentes (`funciones_transcendentes.svg`)
- Representación de $y=e^x$ y $y=\ln(x)$ y su simetría con $y=x$.
- **Parámetros:** Los rangos del ciclo `for` limitan el crecimiento explosivo de la función exponencial `calc.exp()`. Utilizar condiciones lógicas `if y <= y-max` para truncar los puntos y que no desborden el lienzo de renderizado.

### 4. Técnicas de Integración (`tecnicas_integracion.svg`)
- Similar al área de la integral pero con un enfoque en fronteras definidas $a$ y $b$.
- **Parámetros:** Modificar directamente los límites $x=1.0$ y $x=3.0$ o en las líneas verticales delimitadoras (`line((1.0, 0.0), ...)`).

### 5. Aplicaciones del Cálculo (`aplicaciones_calculo.svg`)
- Rastreo visual de los puntos Máximo y Mínimo Locales en una función cúbica.
- **Parámetros:** Las coordenadas calculadas manualmente para los puntos críticos (ej. $x_{max}=2.41, x_{min}=-0.07$). Si cambias el polinomio $f(x)$, deberás encontrar sus nuevas raíces derivadas para ubicar las anclas `circle` correctamente.

### 6. Análisis Funcional (`hilbert_proyeccion.svg`)
- Geometría de espacios abstractos y proyecciones ortogonales sobre subespacios.
- **Parámetros:** Usa proyecciones vectoriales visuales (líneas punteadas `dash: "dashed"`) para crear la ilusión de ortogonalidad (ángulo recto) frente al subespacio base.
