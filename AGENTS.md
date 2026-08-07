# Project Context

## Structure
- src/: teoría en markdown / quarto (.qmd)
- scripts/: generación de gráficos (Typst y Python) y utilidades
- metadata/: JSON para IA y manifiestos de activos
- docs/: documentación técnica de librerías, Quarto, Typst y flujos de CI/CD (GitHub Actions)

## Conventions
- snake_case en archivos
- sin acentos en rutas
- markdown en español
- **Segmentación Semántica:** 
  - Una frase por línea (Semantic Line Breaks).
  - Bloques LaTeX libres de límites de línea.
  - Párrafos por unidad lógica, no por longitud física.
  - Target: 300-500 palabras (Excluyendo YAML Frontmatter y Glosario). Para demostraciones y textos matemáticos complejos, se extiende a 600-1000 palabras de prosa, excluyendo bloques de ecuaciones/matrices LaTeX.


## Tasks
- generar gráficas vectoriales compilando scripts Typst desde `scripts/grafics/typst_src/` exportando a `.svg` bajo el nuevo paradigma.
- orquestar y revisar flujos de CI/CD automatizados mediante GitHub Actions (`.github/workflows/pages.yml`).

## Rules
- no modificar estructura sin razón.
- mantener consistencia naming.
- las imágenes generadas (.svg) deben tener nombres únicos y descriptivos sin números (ej. no heredar prefijo 01_).
- delegar todo el renderizado final a Quarto y Typst.
- **Gestión de Memoria y Contexto (Ahorro de Tokens):**
  - Consultar e inspeccionar siempre en primer lugar `MEMORY.md` y `PROGRESS.md` para verificar el estado y avance del proyecto.
  - En `MEMORY.md`, registrar fecha y hora (`YYYY-MM-DD HH:MM`) por cada lección o acción relevante.
  - En `PROGRESS.md`, registrar fecha, hora y segundos (`YYYY-MM-DD HH:MM:SS`) para cada actualización del diario de trabajo.
  - Al reanudar una tarea o cuando los archivos sean extensos, consultar únicamente la última fecha/marca de tiempo para continuar la ejecución de forma eficiente y ahorrar tokens.

## Local Dataset Access (DuckDB & Parquet)
Para consultar datasets globales de referencia (`G:\DATASETS\`):
1. **Wikipedia:** `powershell.exe -Command "& 'G:\DATASETS\venv\Scripts\python.exe' 'G:\DATASETS\scripts\search_wiki.py' '<busqueda>' '<es/en>'"`
2. **Rosetta Code:** `powershell.exe -Command "& 'G:\DATASETS\venv\Scripts\python.exe' 'G:\DATASETS\scripts\search_rosetta.py' '<busqueda>'"`
3. **DLMF (Digital Library of Mathematical Functions):** `powershell.exe -Command "& 'G:\DATASETS\venv\Scripts\python.exe' 'G:\DATASETS\scripts\search_dlmf.py' '<busqueda>'"`
4. **MSC2020 (Mathematics Subject Classification):** `powershell.exe -Command "& 'G:\DATASETS\venv\Scripts\python.exe' 'G:\DATASETS\scripts\search_msc.py' '<busqueda>'"`