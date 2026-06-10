# Librerías de Typst para Gráficos, Figuras y Esquemas

Typst cuenta con un ecosistema robusto de librerías para el diseño y renderizado de gráficos vectoriales (2D y 3D), las cuales deben ser utilizadas como motor de generación estática para el proyecto Polaris Kernel, alojando sus scripts dentro de `scripts/grafics/typst_src/` y exportando a `.svg` mediante la herramienta compiladora automatizada.

A continuación, se documentan las herramientas y librerías recomendadas:

## 1. Librería Principal de Dibujo (Core)

*   **[CeTZ (Canvas for Typst)](https://typst.app/universe/package/cetz)**
    Es la librería fundacional y esencial para dibujo vectorial 2D en Typst. Está fuertemente inspirada en TikZ (de LaTeX) y proporciona una API declarativa basada en coordenadas, nodos y operaciones sobre el "Canvas". La mayoría de los paquetes especializados construyen sobre CeTZ.

## 2. Diagramas, Figuras y Graficación Especializada en 2D

Para abstracciones más directas, se utilizan paquetes construidos sobre CeTZ o diseñados para casos específicos:

*   **[Fletcher](https://typst.app/universe/package/fletcher):** La librería por excelencia para dibujar **diagramas conmutativos**, grafos, y figuras interconectadas. Ideal para esquemas algorítmicos, redes o diagramas relacionales matemáticos.
*   **[Lilaq](https://typst.app/universe/package/lilaq) / [cetz-plot](https://typst.app/universe/package/cetz-plot):** Diseñadas para la **visualización de datos científicos**. Soportan gráficos de dispersión (scatter), líneas, barras y diagramas de contorno.
*   **[Timeliney](https://typst.app/universe/package/timeliney):** Especializada en crear **Diagramas de Gantt** y líneas de tiempo temporales.
*   **[Quill](https://typst.app/universe/package/quill):** Construida para diseñar de manera limpia **circuitos cuánticos** y puertas lógicas.
*   **[Alchemist](https://typst.app/universe/package/alchemist):** Librería para renderizado de **fórmulas esqueléticas químicas** en 2D.
*   **[Digidraw](https://typst.app/universe/package/digidraw):** Herramienta para el dibujo de diagramas de tiempo (timing diagrams) usando sintaxis de WaveDrom.

## 3. Gráficos 3D y Renderizado

*   **[Plotsy-3d](https://typst.app/universe/package/plotsy-3d):** Construido sobre CeTZ para el graficado 3D matemático. Ideal para visualizar superficies matemáticas, curvas paramétricas y gradientes tridimensionales (similar a `pgfplots` 3D en LaTeX).
*   **[Larnt](https://typst.app/universe/package/larnt):** Motor de arte de líneas tridimensionales puro. Permite renderizar primitivas 3D (esferas, cilindros, cubos) a partir de proyecciones, ideal para ilustraciones topológicas o geometría euclidiana 3D.
*   **[Maquette](https://typst.app/universe/package/maquette):** Soporte avanzado para integrar modelos y mallas 3D externas (PLY, STL, OBJ) y renderizarlos directamente como imágenes 2D/vectoriales dentro del flujo de compilación.

---

### Uso en la Arquitectura de Polaris Kernel (Integración Quarto & CI/CD)

De acuerdo con **"The Trinity Rule"**, la utilización de estas librerías debe hacerse exclusivamente en archivos fuente `.typ` (alojados en la carpeta base `scripts/grafics/typst_src/`).
Los gráficos se diseñan especificando los tamaños de página dinámicos y, posteriormente, se compilan localmente a formato SVG para incrustarlos en la documentación.

Para realizar la compilación de Typst a SVG, el sistema cuenta con los siguientes scripts:
*   `scripts/grafics/compile_typst.py`:
    Escanea la carpeta `typst_src/` buscando archivos `.typ` con el patrón `folder_name___svg_stem.typ`.
    Compila automáticamente cada archivo al pilar de destino correspondiente en `src/` y lo registra en `metadata/GENERATED_ASSETS.md`.
*   `scripts/grafics/gen_jerarquia_numeros.py`:
    Script de compilación específico y manual para el gráfico de la jerarquía de los números.
    Genera el archivo SVG correspondiente bajo `src/01_fundamentos_logica/assets/`.

Bajo el nuevo paradigma, **Quarto** actúa como el orquestador principal del contenido.
Al renderizar (localmente o mediante el **flujo CI/CD en GitHub Actions** `pages.yml`), Quarto integra nativamente estos SVG e incluso puede procesar código Typst puro embebido en los `.qmd`.
La acción de GitHub publicará automáticamente el resultado utilizando `upload-pages-artifact`.

Ejemplo de plantilla de inicio (`.typ`):
```typst
#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 5pt)

#cetz.canvas({
  import cetz.draw: *
  // ... tu código de dibujo aquí ...
})
```
