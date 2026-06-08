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
  - Target: 300-500 palabras (Excluyendo YAML Frontmatter y Glosario).

## Tasks
- generar gráficas vectoriales compilando scripts Typst desde `scripts/grafics/typst_src/` exportando a `.svg` bajo el nuevo paradigma.
- orquestar y revisar flujos de CI/CD automatizados mediante GitHub Actions (`.github/workflows/pages.yml`).

## Rules
- no modificar estructura sin razón.
- mantener consistencia naming.
- delegar todo el renderizado final a Quarto y Typst.