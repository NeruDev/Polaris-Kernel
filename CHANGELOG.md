# Registro de Cambios (Changelog)

Todos los cambios notables en este proyecto serán documentados en este archivo. El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

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
