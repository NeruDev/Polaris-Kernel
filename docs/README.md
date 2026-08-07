# Documentación Técnica (`docs/`)

Este directorio centraliza la documentación técnica, las especificaciones arquitectónicas, las guías de diseño gráfico y las fuentes de referencia matemática de Polaris Kernel.

## Propósito y Funciones en el Repositorio

El directorio `docs/` sirve como la fuente de especificaciones y estándares técnicos para desarrolladores y agentes IA.
Define cómo se compila la teoría en `src/`, cómo operan los scripts de `scripts/` y de qué manera se orquestan las herramientas de renderizado Quarto y Typst.
Además, alberga la base documental de referencia de funciones matemáticas especiales.

## Archivos y Subdirectorios

### Documentación de Arquitectura y Diseño
* [`ARQUITECTURE.md`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/docs/ARQUITECTURE.md): Especificación principal de la arquitectura FileSystem-as-Memory, los 6 pilares estructurales y el pipeline de compilación.
* [`escalabilidad_del_proyecto.md`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/docs/escalabilidad_del_proyecto.md): Estrategia y principios de diseño para garantizar la escalabilidad modular del kernel matemático.
* [`project_structure.json`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/docs/project_structure.json) y [`project_structure.jsonc`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/docs/project_structure.jsonc): Definiciones estructuradas de la topología de carpetas y componentes del proyecto.

### Guías de Renderizado y Gráficos
* [`plan_quarto_typst.md`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/docs/plan_quarto_typst.md): Plan de integración del pipeline que coordina Typst para gráficos vectoriales y Quarto para la publicación del sitio estático.
* [`typst_graficos.md`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/docs/typst_graficos.md): Guía de desarrollo y estándares de estilo para la creación de diagramas y esquemas vectoriales mediante Typst.
* [`quarto_live.md`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/docs/quarto_live.md): Documentación sobre la integración de componentes interactivos y ejecutabilidad en vivo mediante Quarto Live.

### Auditoría y Registro de Activos
* [`GENERATED_ASSETS.md`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/docs/GENERATED_ASSETS.md): Manifiesto de activos gráficos compilados que mapea scripts Typst con sus archivos SVG e identificadores.
* [`correcciones.md`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/docs/correcciones.md): Registro de planes de sanitización matemática, corrección de sintaxis y normativas KaTeX/MathJax.

### Repositorios de Referencia Matemática
* `DLMF-markdown-main/`: Colección estructurada en Markdown de la Digital Library of Mathematical Functions (DLMF) del NIST, dividida en 36 capítulos de funciones especiales.

## Relación con otros Directorios

* **Con `src/`:** Proporciona los estándares pedagógicos y gráficos aplicados en la redacción de notas y temas matemáticos.
* **Con `scripts/`:** Describe el comportamiento esperado que deben automatizar los orquestadores como `build.py` y `compile_typst.py`.
* **Con `metadata/`:** Define el flujo de la "Regla de la Trinidad" para mantener sincronizados los registros de metadatos y gráficos.
