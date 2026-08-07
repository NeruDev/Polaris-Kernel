# Registro de Cambios (Changelog)

Todos los cambios notables en este proyecto serán documentados en este archivo. El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [2.2.0] - 2026-08-06

### Añadido
- Documentación completa y estandarizada mediante `README.md` en todos los directorios del repositorio ([`docs/README.md`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/docs/README.md), [`src/README.md`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/README.md), [`metadata/README.md`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/metadata/README.md), [`scripts/README.md`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/scripts/README.md), [`tests/README.md`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/tests/README.md) y [`utils/README.md`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/utils/README.md)).
- Inclusión del subdirectorio de datos estructurados de la DLMF (Digital Library of Mathematical Functions, NIST) en [`metadata/DLMF_data/`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/metadata/DLMF_data/), abarcando índices simplificados, completos, datos por capítulo y reportes de auditoría de extracción/metadatos.
- Suite de scripts de sanitización, traducción modular, verificación matemática KaTeX/MathJax e hipervínculos para la base de conocimientos DLMF.

### Cambiado
- Actualización de [`tests/test_structure.py`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/tests/test_structure.py) para autorizar la presencia de `README.md` dentro de `src/` manteniendo la validación estricta de nombres `snake_case`.
- Actualización del archivo de versión del proyecto en `pyproject.toml` a `v2.2.0`.

## [2.1.1] - 2026-07-22
### Arquitectura y Refactorización
- **Nomenclatura Semántica:** Los archivos dentro de `src/` han sido renombrados bajo una nueva política de arquitectura (documentada en `ARQUITECTURE.md`). Sus prefijos (ej. `01_`, `02_`) ahora respetan estrictamente el **orden de complejidad relativa** pedagógica determinado por sus metadatos (intro, intermedio, avanzado, abstracto), abandonando el orden alfabético estático.
- Se refactorizaron en lote los archivos `.qmd`, `.json`, scripts de generación `.typ` y los correspondientes compilados `.svg` garantizando que los orquestadores dinámicos no rompan sus referencias.
- Generación de archivos `README.md` específicos por pilar indicando la manipulación de variables de Typst.

## [2.1.0] - 2026-07-22

### Añadido
- Finalización de la **Fase 1 (Conceptos Básicos)** para los 6 Pilares de Polaris Kernel, logrando el 100% de cobertura planificada.
- Integración de 11 nuevos gráficos generados por Typst (v0.15.1) utilizando la librería `@preview/cetz:0.3.3`.
- Completado el Pilar 03 con 3 nuevos módulos: funciones transcendentes, técnicas de integración y aplicaciones del cálculo.
- Completado el Pilar 04 con 2 nuevos módulos: geometría en el espacio 3D e identidades trigonométricas avanzadas.
- Completado el Pilar 05 con 3 nuevos módulos: relaciones de recurrencia, análisis de complejidad y aritmética modular.
- Completado el Pilar 06 con 3 nuevos módulos: variables aleatorias y distribuciones, regresión y correlación, y teoremas límite (TLC).

### Cambiado
- El manifiesto `docs/escalabilidad_del_proyecto.md` y el registro de activos `metadata/GENERATED_ASSETS.md` fueron actualizados acorde a las nuevas adiciones.
- Actualización en el listado del árbol de directorios `docs/project_structure.json`.

## [2.0.0] - 2026-06-09

### Añadido
- Soporte dinámico para tema claro y tema oscuro en el mismo archivo `miku-dark.scss` mediante la variable `$theme-layout`.
- Interruptor de tema personalizado (Sol y Luna) interactivo y animado con efecto de rotación de rayos solares en modo claro.
- Leyenda estructurada de cambio de tema ("tema:" arriba, icono al centro y nombre del tema actual abajo) flotante en la esquina superior derecha.

### Cambiado
- Configuración global de temas en `_quarto.yml` para compilar ambos temas simultáneamente con la personalización unificada de Hatsune Miku.
- Ajuste de contraste y paletas de colores en tablas, callouts y bloques de código para legibilidad óptima en el tema claro de Miku.

## [1.0.0] - 2026-04-26 (Lanzamiento Inicial)

### Añadido
- Arquitectura Bourbaki implementada con 6 pilares en `src/`.
- Suite de 29 documentos atómicos de teoría matemática.
- Biblioteca de activos gráficos SVG vinculados al 100%.
- Sistema de construcción (Build System) orquestado por `build.py`.
- Capa de Inteligencia con Metadatos Adyacentes JSON.
- Validación formal mediante JSON Schemas y taxonomía MSC.
- Configuración de CI/CD para despliegue automático en GitHub Pages.
- Documentación técnica avanzada (`ARQUITECTURE.md`, `llms.txt`, `GEMINI.md`).

### Cambiado
- Migración de contenido legado a estructura atómica de 300 palabras.
- Estandarización de paleta de colores para gráficos didácticos.

### Seguridad
- Implementación de validación estricta UTF-8 y sintaxis LaTeX.
- Configuración de Git LFS para protección de activos pesados.

---
*Polaris Kernel: Versión estable v2.0.0.*
