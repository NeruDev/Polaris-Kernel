# Sistema de Clasificación y Metadatos (`metadata/`)

Este directorio contiene los esquemas, índices y conjuntos de metadatos estructurados que impulsan el sistema de clasificación de Polaris Kernel.
Permite vincular las notas teóricas de `src/` con el estándar internacional Mathematics Subject Classification (MSC2020) y la base de conocimiento DLMF (Digital Library of Mathematical Functions).

## Estructura de Datos y Fuentes Principales

### Taxonomía e Índices MSC2020
* **[MSC_2020.tex](MSC_2020.tex):** Fuente primaria completa en LaTeX del sistema de clasificación MSC2020 (zbMATH / Mathematical Reviews).
* **[MSC_index.json](MSC_index.json):** Índice principal para mapear códigos de nivel superior hacia los archivos de rango específico.
* **[MSC_index_pillars_overlay.json](MSC_index_pillars_overlay.json):** Capa de superposición que asocia los códigos MSC2020 con los 6 Pilares de Bourbaki.
* **Archivos por Rango (`MSC_NN_a_XX.json` y `MSC_NN_a_XX.tex`):** División por secciones temáticas del estándar MSC2020.
* **[msc_taxonomy.all.json](msc_taxonomy.all.json):** Arbol taxonómico consolidado para consulta y validación rápida.

### Datos de Referencia DLMF (`DLMF_data/`)
Subdirectorio que contiene la extracción estructurada en JSON de los 36 capítulos de la Digital Library of Mathematical Functions del NIST:
* **`DLMF_indice_simplificado.json`:** Índice simplificado de capítulos y secciones de DLMF.
* **`DLMF_indice_completo.json`:** Índice jerárquico detallado con referencias cruzadas.
* **Archivos por Sección (`1_Algebraic_and_Analytic_Methods.json` a `36_...json`):** Datos estructurados que incluyen fórmulas LaTeX, palabras clave conceptuales y tablas.
* **`AUDITORIA_EXTRACCION.json` y `AUDITORIA_METADATOS.json`:** Reportes automatizados de integridad, tipado estricto y auditoría sintáctica KaTeX.

### Registro de Activos Gráficos
* **[GENERATED_ASSETS.md](GENERATED_ASSETS.md):** Registro oficial de activos gráficos vectoriales (SVG) que cumple con la Regla de la Trinidad: relaciona el script Typst fuente (`scripts/grafics/typst_src/`), el gráfico SVG en `src/` y su entrada de metadatos.

### Esquemas de Validación (`schemas/`)
* Contiene esquemas JSON Schema para validar la estructura de la taxonomía y la integridad de los datos del proyecto.

## Pipeline de Clasificación

1. **Nivel 1 (Rápido):** Coincidencia con el overlay (`MSC_index_pillars_overlay.json`) para determinar el pilar principal y la sección MSC.
2. **Nivel 2 (Preciso):** Búsqueda en los archivos JSON específicos de sección para refinar el `msc_code` y derivar etiquetas (`tags`).

## Scripts Relacionados (`scripts/`)

Los scripts para la gestión de metadatos residen en `scripts/`:
* `scripts/update_taxonomy_pillars.py`: Actualiza la taxonomía sincronizando con el overlay.
* `scripts/generar_indices_dlmf.py`: Genera los índices estructurales de DLMF.
* `scripts/extraer_contenido_dlmf.py` y `scripts/refinar_metadata_dlmf.py`: Procesan y depuran los metadatos de DLMF.

## Relación con otros Directorios

* **Con `src/`:** Proporciona los metadatos YAML frontmatter e identidades MSC requeridos por cada documento teórico.
* **Con `scripts/`:** Es consumido y actualizado por los orquestadores de compilación y extracción.
* **Con `utils/`:** Utiliza helpers para validar esquemas JSON y mantener la coherencia de datos.
