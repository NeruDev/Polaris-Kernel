# MEMORY - Lecciones Aprendidas y Conocimiento del Sistema

## Arquitectura FileSystem-as-Memory

Este repositorio adopta el patrón de arquitectura de agentes FileSystem-as-Memory.
La división de responsabilidades se distribuye de la siguiente manera:
- `AGENTS.md` y `GEMINI.md`: Reglas estáticas del sistema, directivas de desarrollo y convenciones.
- `MEMORY.md`: Conocimiento acumulado, decisiones de diseño, lecciones aprendidas y peculiaridades del código.
- `PROGRESS.md`: Registro en tiempo real del trabajo actual, tareas pendientes y estado de ejecución.

## Peculiaridades Descubiertas en el Código y Datos

- **[2026-08-05 15:22] Biblioteca DLMF (`docs/DLMF-markdown-main/`)**:
  Contiene una conversión a Markdown de la Digital Library of Mathematical Functions del NIST.
  Presenta macros LaTeX no estándares como `\*`, `\ifrac`, `\NVar` y `\cfracstyle` que requieren sanitización antes de su renderizado.
  Incluye entidades HTML como `&amp;` dentro de bloques LaTeX de matrices que rompen el parser de KaTeX/MathJax.

- **[2026-08-05 15:22] Convenciones de Archivos e Imágenes**:
  Todo nombre de archivo en el repositorio debe seguir la convención `snake_case`.
  Las imágenes generadas SVG deben tener nombres descriptivos únicos y sin prefijos numéricos herederos (ej. evitar `01_`).
  La regla de la Trinidad debe mantenerse: script Typst en `scripts/grafics/typst_src/` $\rightarrow$ activo SVG en `src/` $\rightarrow$ registro en `metadata/GENERATED_ASSETS.md`.

- **[2026-08-05 15:25] Lectura Prioritaria y Estampas de Tiempo para Ahorro de Tokens**:
  Los agentes deben leer `MEMORY.md` y `PROGRESS.md` antes que cualquier otro archivo para comprobar el estado.
  Cada entrada de `MEMORY.md` incluye fecha y hora (`YYYY-MM-DD HH:MM`).
  Cada entrada de `PROGRESS.md` incluye fecha, hora y segundos (`YYYY-MM-DD HH:MM:SS`).
  Se debe consultar la estampa más reciente para reanudar el trabajo sin cargar historiales innecesarios.

- **[2026-08-05 15:33] Sanitización Automática DLMF y Verificación KaTeX/MathJax**:
  Se crearon dos scripts: `scripts/sanitizar_dlmf.py` para corregir macros no estándares (`\ifrac`, `\NVar`, `\cfracstyle`, `\*`, `\mskip`, `\pvint`, entidades HTML) y `scripts/verificar_dlmf.py` para auditar la validez KaTeX/MathJax.
  Se procesaron exitosamente los 935 archivos de `docs/DLMF-markdown-main/`, evaluando 56,567 expresiones matemáticas sin perder contenido ni estructura.

- **[2026-08-05 15:44] Traducción Modular DLMF y Repositorio en Español**:
  Se creó el repositorio de traducción en `docs/DLMF_markdown_traduccion/markdown/` incluyendo `toc_es.md` y `toc_full_es.md`.
  Se desarrollaron los scripts `scripts/inicializar_traduccion_dlmf.py`, `scripts/glosario_matematico.py`, `scripts/traducir_dlmf.py` y `scripts/verificar_traduccion_dlmf.py` para la traducción modular conservando 100% de la sintaxis LaTeX.
  Se auditaron y tradujeron los 934 archivos del repositorio (incluyendo los 36 capítulos, tablas de contenido y la sección de índices `idx/`), preservando intactas las 56,567 expresiones matemáticas.

- **[2026-08-05 15:52] Traducción Integral de Prosa Intermedia y Metadatos**:
  Se perfeccionó el script `scripts/traducir_prosa_completa.py` para procesar y traducir la prosa explicativa restante, metadatos de infoboxes (`Keywords`, `Referenced by`, `Notes`), títulos de secciones e hipervínculos en todo `docs/DLMF_markdown_traduccion/markdown/`.
  Se aplicó traducción de oraciones completas garantizando fluidez en español académico nativo y manteniendo 100% protegidas las expresiones matemáticas KaTeX/MathJax.

- [2026-08-05 16:25] **Macros LaTeX en Modo Texto y Priorización de Oraciones Compuestas**:
  - En motores KaTeX/MathJax (utilizados por la extensión Markdown Preview Enhancer de VS Code), escribir macros matemáticas dentro de bloques `\text{...}` (como `\text{(or \infty)}`) provoca fallos fatales de renderizado. La forma sintácticamente válida y compatible es aislar los símbolos matemáticos de la prosa: `\text{(o }\infty\text{)}`.
  - Al realizar traducciones de prosa explicativa, los reemplazos de palabras individuales cortas (ej. `cut`, `branch`, `zero`) nunca deben ejecutarse antes que las expresiones matemáticas compuestas (ej. `cut domain` $\rightarrow$ `dominio cortado`, `branch point` $\rightarrow$ `punto de ramificación`), ya que alteran los términos intermedios impidiendo la coincidencia del patrón completo.

- **[2026-08-05 16:40] Generación de Índices JSON y Estructura Modular DLMF (`metadata/DLMF_data/`)**:
  Se creó el script `scripts/generar_indices_dlmf.py` para construir de manera automatizada los índices generales y la serie completa de archivos JSON de capítulos.
  Se generó `DLMF_indice_simplificado.json` a partir de `toc.md` y `DLMF_indice_completo.json` (así como su alias `DLMF_indice completo.json`) a partir de `toc_full.md`.
  Se crearon los 36 archivos JSON correspondientes a las secciones/capítulos de DLMF con placeholders estructurados para contenido, fórmulas LaTeX, gráficos Typst y referencias cruzadas.

- **[2026-08-05 16:45] Extracción Masiva y Auditoría Automatizada DLMF (`metadata/DLMF_data/`)**:
  Se desarrollaron dos scripts: `scripts/extraer_contenido_dlmf.py` para la extracción estructurada de los 872 archivos markdown de `docs/DLMF-markdown-main/` hacia los 36 archivos JSON de sección, y `scripts/auditar_extraccion_dlmf.py` para auditar la integridad y los tipos de datos.
  Se lograron extraer exitosamente 10,480 fórmulas LaTeX, 7,544 palabras clave, 7,753 referencias cruzadas y 155 tablas de datos con 100% de cumplimiento de tipos y 0 errores.
  Se generó el reporte oficial de auditoría en `metadata/DLMF_data/AUDITORIA_EXTRACCION.json`.

- **[2026-08-05 16:54] Refinamiento Fino y Depuración de Metadatos DLMF (`metadata/DLMF_data/`)**:
  Se desarrolló el script `scripts/refinar_metadata_dlmf.py` para erradicar arreglos vacíos redundantes (`simbolos: []`, `abramowitz_stegun: []`, etc.) en favor de un esquema dinámico de campos presentes.
  Se corrigió el parser de palabras clave para procesar enlaces Markdown complejos (evitando fragmentaciones arbitrarias como `[matrix`), indexando 3,116 palabras clave conceptuales puras.
  Se auditaron y validaron 10,480 fórmulas LaTeX verificando la integridad de sintaxis, sanitización de macros KaTeX y balance de llaves, generando el informe `metadata/DLMF_data/AUDITORIA_METADATOS.json`.

- **[2026-08-05 15:22] Estándar Pedagógico y Formato**:
  Se aplica la segmentación semántica (*Semantic Line Breaks*): exactamente una oración por línea.
  Los bloques LaTeX en línea o independientes (`$$...$$`) están exentos de límites de longitud de línea.
  El idioma obligatorio para la prosa y la documentación es español.

- **[2026-08-06 20:00] Documentación y Estandarización de Directorios**:
  Se incorporó `docs/README.md` detallando las guías arquitectónicas, integración Quarto/Typst y repositorio DLMF.
  Se creó `src/README.md` explicando los 6 pilares de Bourbaki.
  Se actualizaron los `README.md` de `metadata/`, `scripts/`, `tests/` y `utils/` incorporando las adiciones recientes (DLMF, gráficos Typst, taxonomía MSC).
  Se ajustó `tests/test_structure.py` para permitir la existencia de `README.md` dentro de `src/` sin romper la verificación de nombres snake_case.

- **[2026-08-06 21:00] Formalización Arquitectónica de la Triada de Datos (ADR-008)**:
  Se formalizó la arquitectura de tres capas para datasets extensos y densos (DLMF y MSC2020):
  1. Capa 1 (`docs/`): Fuente original en Markdown para maquetación y renderizado en Quarto.
  2. Capa 2 (`metadata/`): Estructura adyacente JSON para metadatos, esquemas e inspección por IA.
  3. Capa 3 (`G:\DATASETS\`): Datasets Parquet e índices DuckDB FTS (BM25) para búsquedas de alta velocidad en RAG.
  Se actualizaron los mapas del sistema `docs/project_structure.json`, `docs/project_structure.jsonc` y el `README.md` de la raíz.

- **[2026-08-06 21:05] Planificación Modular de Volcado DLMF a los 6 Pilares (`src/README.md`)**:
  Se mapearon los 36 capítulos de la DLMF NIST desde `metadata/DLMF_data/` hacia los 6 Pilares de Bourbaki en `src/`.
  Se establecieron 5 subdivisiones estructurales por documento (Definiciones, Identidades, Asintótica, Simetrías y Gráficos Typst) respaldando el rigor formal con fórmulas LaTeX clave y clasificación de códigos MSC2020.

- **[2026-08-06 21:08] Directivas de Nomenclatura, Dificultad MSC2020 y Frontmatter YAML**:
  Se incorporaron reglas estrictas al plan en `src/README.md`:
  1. Clasificación en `intro/`, `intermedio/`, `avanzado/`, `abstracto/` según la complejidad percibida basada en el índice MSC2020.
  2. Nombres de archivos y títulos 100% en español nativo bajo convención `snake_case`.
  3. Encabezado Frontmatter YAML obligatorio para compilación y renderizado en Quarto.

- **[2026-08-06 21:22] Automatización Iterativa del Volcado DLMF**:
  Se desarrolló `scripts/build_dlmf_qmd.py` para mapear de manera automática el corpus JSON extraído (`metadata/DLMF_data/`) hacia el esquema conceptual de los 6 Pilares de Bourbaki en `src/`.
  **Lecciones Aprendidas**:
  - Emplear librerías como `deep-translator` dentro del flujo automatizado agiliza enormemente la traducción del vocabulario técnico conservando la indemnidad del código `snake_case` que valida la suite `pytest`.
  - Las ecuaciones y símbolos LaTeX que se insertan algorítmicamente desde JSON hacia `.qmd` deben siempre envolverse explícitamente en delimitadores de bloque (`$$ ... $$`) para evitar el colapso del parser KaTeX/MathJax en el renderizado final de Quarto.








