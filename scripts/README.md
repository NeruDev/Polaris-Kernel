# Documentación de Scripts (`scripts/`)

Este directorio contiene los scripts y orquestadores principales para la construcción, generación de gráficos, procesamiento de metadatos y traducción técnica de Polaris Kernel.

## Orquestación y Compilación Principal

### `build.py`
Orquestador unificado de construcción y validación del proyecto. Delega la compilación a Quarto y constituye el punto de entrada para la integración continua (CI/CD mediante GitHub Actions).
* `parse_args()`: Procesa los argumentos de línea de comandos.
* `validate_project(...)`: Valida la integridad de archivos, codificaciones UTF-8 y esquemas JSON.
* `run_assets(...)`: Invoca la generación masiva de gráficos.
* `run_site(...)`: Ejecuta `quarto render` para construir el sitio web final.

### `config.py`
Define configuraciones y rutas estáticas centralizadas.
* `Paths (clase)`: Administra las rutas críticas del proyecto relativas a la raíz.
* `BuildConfig (clase)`: Configura parámetros de compilación, banderas de advertencia y verbosidad.

## Gráficos Vectoriales (`grafics/` y `generate_assets.py`)

### `generate_assets.py`
Orquestador de generación gráfica que escanea y ejecuta scripts en lote.

### `grafics/` (Subdirectorio de Gráficos Typst)
Especializado en la compilación de diagramas vectoriales bajo el nuevo paradigma basado en Typst:
* `compile_typst.py`: Compilador automatizado de archivos Typst a SVG en lote que actualiza el registro en `metadata/GENERATED_ASSETS.md`.
* `typst_src/`: Directorio que alberga los archivos fuente `.typ` de los diagramas.

### `automate_image_linking.py` y `fix_orphaned_images.py`
* `automate_image_linking.py`: Vincula automáticamente las imágenes SVG generadas en los archivos de teoría (`src/`) basándose en IDs o etiquetas.
* `fix_orphaned_images.py`: Detecta y soluciona enlaces a imágenes SVG desasociadas o huérfanas.

## Procesamiento y Traducción de la DLMF (`docs/DLMF-markdown-main/`)

### Sanitización y Verificación Matemática
* `sanitizar_dlmf.py`: Corrige macros LaTeX no estándares (`\ifrac`, `\NVar`, `\cfracstyle`, entidades HTML) para garantizar compatibilidad con KaTeX/MathJax.
* `verificar_dlmf.py`: Audita masivamente las expresiones matemáticas en busca de inconsistencias o errores de sintaxis.

### Motores de Traducción Modular
* `inicializar_traduccion_dlmf.py`: Genera las tablas de contenido traducidas (`toc_es.md` y `toc_full_es.md`).
* `glosario_matematico.py`: Contiene el glosario terminológico estandarizado en español técnico.
* `traducir_dlmf.py`, `traducir_prosa_completa.py`, `traducir_oraciones_dlmf.py`, `traducir_seccion_profunda.py`: Automatizan la traducción modular de la prosa explicativa manteniendo intactas el 100% de las expresiones LaTeX.
* `verificar_traduccion_dlmf.py` y `auditar_prosa_ingles.py`: Verifican la calidad del texto traducido y confirman la preservación de fórmulas.

### Extracción y Refinamiento de Metadatos DLMF
* `generar_indices_dlmf.py`: Genera `DLMF_indice_simplificado.json`, `DLMF_indice_completo.json` y la estructura inicial de los 36 capítulos en `metadata/DLMF_data/`.
* `extraer_contenido_dlmf.py`: Parsea los 872 archivos Markdown extraendo formulas LaTeX, palabras clave y tablas hacia los archivos JSON.
* `auditar_extraccion_dlmf.py`: Realiza auditoría de tipos de datos e integridad estructural.
* `refinar_metadata_dlmf.py`: Depura arreglos vacíos y limpia palabras clave conceptuales puras.

## Gestión de Taxonomía MSC2020

### `update_taxonomy_pillars.py`
Actualiza la taxonomía base MSC2020 cruzando datos con el overlay de los 6 Pilares de Bourbaki en `msc_taxonomy.all.json`.

## Flujo de Trabajo y Conexiones

* **Hacia `utils/`:** Depende de utilidades de rutas (`utils/pathing.py`), enlaces (`utils/links.py`), parseo (`utils/markdown.py`) y registro (`utils/logging.py`).
* **Hacia `src/`:** Procesa, valida, traduce e inyecta gráficos en las notas teóricas de `src/`.
* **Hacia `metadata/`:** Lee y actualiza los índices JSON, la taxonomía MSC y el manifiesto de activos.
* **Hacia `tests/`:** El comportamiento y robustez de estos scripts son validados por la suite de pruebas unitarias.
