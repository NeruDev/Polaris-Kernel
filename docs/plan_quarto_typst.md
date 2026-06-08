---
id: 'plan_quarto_typst'
title: 'Plan de Migración a Quarto y Typst'
pilar: 'docs'
tags: ['arquitectura', 'quarto', 'typst', 'renderizado']
---

# Plan de Migración: Renderizado en Quarto y Visualización en Typst

Este documento detalla la viabilidad y los retos técnicos para migrar el sistema de renderizado actual de Polaris Kernel hacia una arquitectura basada en Quarto, utilizando Typst para el diseño de gráficos matemáticos y la composición tipográfica de alta fidelidad.

## 1. Descripción del Cambio Propuesto

El sistema evolucionará de un generador estático personalizado (basado en la librería `markdown` de Python y MathJax) hacia el framework **Quarto**. 
Quarto actuará como el orquestador de compilación para los documentos científicos, ejecutando las lógicas programáticas (vía Jupyter/ipykernel) para generar gráficos, y delegando el motor de renderizado y visualización final a **Typst**. Esta transición garantizará una presentación matemática impecable en la página web, optimizando tiempos de compilación respecto a LaTeX y modernizando la estética visual del kernel.

## 2. Análisis de Viabilidad

La transición es **altamente viable** gracias a la preparación modular del proyecto actual:

- **Estructura Compatible:** Los archivos fuente actuales ya son Markdown con YAML frontmatter, formato que Quarto consume de forma nativa.
- **Preparación del Entorno:** El entorno virtual (`venv`) ya fue instrumentado con las herramientas necesarias (`typst` e `ipykernel`), habilitando la ejecución directa del código de Python a través de Quarto y la compilación de activos.
- **Ecosistema Tipográfico:** Typst soporta la incrustación nativa de activos `.svg` generados previamente por `matplotlib`, facilitando una migración híbrida inicial sin romper gráficos existentes.

## 3. Retos Técnicos y Estrategia de Migración

Para consolidar la transformación del contenido a representaciones Typst dentro de Quarto, se deben afrontar los siguientes desafíos arquitectónicos:

### 3.1 Transición de Sintaxis Matemática (LaTeX a Typst)
- **El Reto:** Polaris Kernel posee abundante notación matemática escrita en sintaxis LaTeX/MathJax (ej. entornos `\begin{aligned}`). Quarto utiliza Pandoc, que convierte automáticamente mucho del LaTeX a Typst, pero las macros avanzadas y alineaciones condicionales a menudo fallan o requieren intervención.
- **La Estrategia:** Adoptar un enfoque progresivo. Configurar conversiones iniciales y revisar manualmente las fórmulas que fallen, adoptando eventualmente la sintaxis limpia de Typst de forma nativa en la base documental para ganar eficiencia en parsing.

### 3.2 Refactorización del Build System (`scripts/build.py`)
- **El Reto:** Actualmente, la función `run_site()` realiza la conversión MD a HTML "a mano" usando la extensión `jinja2` y `markdown`.
- **La Estrategia:** El sistema de construcción debe delegar la capa de visualización al CLI de Quarto. El script `build.py` se limitará a la validación de integridad (`MetadataAgent`), la inyección de pre-procesamiento y finalmente llamará a un subprocess de `quarto render` hacia el directorio de salida final (`site/`).

### 3.3 Preservación de la "Regla de Adyacencia" y Entornos RAG
- **El Reto:** Quarto inyecta metadatos dinámicos y crea directorios de soporte ocultos (como `_quarto_files`) que pueden contaminar el escaneo estructurado y añadir "ruido" para los LLMs.
- **La Estrategia:** Implementar un archivo de configuración unificado `_quarto.yml` que enjaule estrictamente los artefactos de compilación. Los scripts de `MetadataAgent` deberán ser modificados para ignorar carpetas generadas automáticamente y seguir enfocándose en la teoría pura (`src/`).

### 3.4 El Flujo de Activos Gráficos (La "Regla de la Trinidad")
- **El Reto:** La arquitectura impone que todo SVG provenga de `scripts/grafics/`. Si Quarto puede ejecutar bloques interactivos (`.qmd`) y Typst puede renderizar formas de forma nativa, la abstracción del script Python externo puede quedar obsoleta para gráficos simples.
- **La Estrategia:** Permitir una excepción arquitectónica: los gráficos complejos seguirán siendo gestionados por scripts de Python aislados, mientras que los diseños esquemáticos y fórmulas ilustradas migrarán a código Typst puro incrustado de manera determinista dentro del contenido teórico.
