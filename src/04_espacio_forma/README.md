---
id: "msc00_readme"
title: "README"
pilar: "04_espacio_forma"
msc_code: "00-00"
status: "draft"
---
# Pilar 04: Espacio y Forma - Registro de Activos Gráficos

Este documento describe el estándar utilizado para la generación de imágenes y gráficos dentro de este pilar, así como los parámetros clave de los scripts origen para facilitar su futuro mantenimiento y escalabilidad.

## Formato y Configuración General

- **Motor de Renderizado:** Typst (v0.15.1)
- **Librería de Dibujo:** `@preview/cetz:0.3.3`
- **Formato de Salida:** Scalable Vector Graphics (`.svg`)
- **Directorio de Fuentes:** `scripts/grafics/typst_src/`
- **Prefijo de Archivos:** `04_espacio_forma___`

Para este pilar, que representa el estudio de la geometría, el uso de las formas primitivas (`circle`, `arc`, `rect`) combinadas con ejes direccionales 2D y 3D es el núcleo central del diseño de las ilustraciones.

---

## Gráficos del Pilar 4 y sus Parámetros Clave

### 1. Geometría Euclidiana (`pitagoras_visual.svg`)
Demostración visual del Teorema de Pitágoras mediante áreas de cuadrados.
- **Parámetros:** La longitud de los catetos $a, b$ dicta los lados de los cuadrados adjuntos `rect()`. Ajustar las posiciones y rotaciones de los cuadrados laterales si se modifica el triángulo rectángulo central.

### 2. Trigonometría Analítica
- **`graficas_seno_coseno.svg`**: Curvas ondulatorias desfasadas.
Modificar la frecuencia o amplitud multiplicando los factores dentro de `calc.sin()` en los ciclos de generación de puntos.
- **`identidades_ecuaciones_trigonometricas.svg`**: Circunferencia unitaria con ángulos positivo y negativo (simetría).
  - Parámetros: `theta = 35deg`. Cambiar este valor actualizará automáticamente la posición de las líneas, pero requerirá ajuste manual de las posiciones de texto (mediante offsets escalares) para evitar empalmes en la nueva posición del arco.

### 3. Geometría Analítica y Espacio 3D
- **`conicas_analitica.svg`**: Ilustra una elipse o cónica.
Usa `circle(..., radius: (rx, ry))` para manejar las excentricidades.
- **`geometria_espacio_3d.svg`**: Emula un entorno isométrico/3D sobre un lienzo 2D.
  - Se utilizan vectores directores base (`x-dir`, `y-dir`, `z-dir`) con componentes calculados (como `0.866, -0.5`).
  - Todo se escala multiplicando por `scale-ax`. Para rotar la perspectiva, se deben cambiar las componentes $x, y$ de los vectores directores base.

### 4. Topología (`topologia_vecindarios.svg`)
Conceptos abstractos de vecindades de puntos y conjuntos abiertos/cerrados.
- **Parámetros:** Los contornos de vecindades pueden dibujarse utilizando líneas curvas de Bezier o círculos difuminados usando opacidades (`fill: rgb(R, G, B, Alfa)`).

### 5. Geometría Diferencial
- **`geometria_variedad_tangente.svg` / `geometria_diferencial_frenet.svg`**:
  - Dibujan curvas espaciales complejas (ej. hélices) y vectores ortonormales en un punto móvil (T, N, B - triedro de Frenet).
  - **Parámetros:** Las coordenadas del triedro cambian según la posición en la curva paramétrica.
Mantener la ortogonalidad usando vectores directores simulados visualmente en 2D isomórfico.
