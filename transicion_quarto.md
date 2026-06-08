# Plan de Transición a Quarto y Typst

Este documento detalla el plan gradual para migrar la arquitectura del repositorio al paradigma de renderizado con Quarto y Typst, basándose en la propuesta inicial y garantizando la compatibilidad con la infraestructura actual del proyecto.

## Fases de la Transición

### Etapa 1: Adaptación de Metadatos y Archivos Base
- [x] **Revisión de scripts de Python:** Primero, revisar y adaptar los scripts de Python para que en el futuro generen los metadatos adecuados directamente en su sección correspondiente (después de la reservada para Quarto). Utilizar los ejemplos de la carpeta `notes` referenciada en la arquitectura de origen para ver cuáles son los campos estándar a estandarizar (ej. `title`, `date`, `author`, `description`, `categories`).
- [x] Renombrar archivos de contenido (teoría) de `.md` a `.qmd` para habilitar el motor nativo de Quarto.
- [x] Mantener el directorio `src/` como la fuente principal de los archivos, configurando Quarto para que los consuma desde allí.
- [x] Refactorizar el Front-Matter YAML de cada archivo separando los metadatos en dos bloques:
  - Primero, los metadatos estándar de Quarto.
  - Segundo, los metadatos de la estructura de scripts actual (ej. `id`, `pilar`).
  - Añadir comentarios adecuados en el YAML indicando a qué sección pertenece cada bloque y qué describen.
- [x] **Auditoría y Documentación:** Debido a la complejidad de la tarea, documentar exhaustivamente los avances y modificaciones de esta etapa en `README.md`, `docs/ARCHITECTURE.md`, `docs/project_structure.jsonc` y demás archivos que permitan llevar una auditoría clara.

### Etapa 2: Configuración del Proyecto Quarto
- [x] Crear el archivo central de configuración `_quarto.yml` en la raíz del proyecto, orquestando el proyecto de tipo `website` (o `book` si aplica) y el menú lateral/navegación a partir de `src/`.
- [x] Integrar el archivo de estilos principal en la configuración de salida HTML en `_quarto.yml`.
- [x] **Auditoría y Documentación:** Debido a la complejidad de la tarea, documentar exhaustivamente los avances y modificaciones de esta etapa en `README.md`, `docs/ARCHITECTURE.md`, `docs/project_structure.jsonc` y demás archivos que permitan llevar una auditoría clara.

### Etapa 3: Generación de Gráficos con Typst
- [x] Emplear Typst nativamente desde dentro de los documentos `.qmd` para la generación de la gran mayoría de gráficos y figuras tridimensionales, aprovechando su sintaxis clara y su renderizado eficiente.
- [x] Dejar los scripts de generación de imágenes en `scripts/grafics` únicamente como alternativa para casos excepcionales o especialmente complejos.
- [x] **Restricción Importante:** Los scripts de gráficos en `scripts/grafics` NO deben ejecutarse en cada renderización (ni local ni remota). Ya que GitHub Actions renderiza automáticamente cada vez que se sube un avance a GitHub Pages, ejecutar estos scripts aumentaría el número de imágenes y el peso del repositorio de forma innecesaria. Su ejecución será estrictamente manual bajo demanda.
- [x] **Auditoría y Documentación:** Debido a la complejidad de la tarea, documentar exhaustivamente los avances y modificaciones de esta etapa en `README.md`, `docs/ARCHITECTURE.md`, `docs/project_structure.jsonc` y demás archivos que permitan llevar una auditoría clara.

### Etapa 4: Integración con la Automatización de Python (Python Build)
- [x] Modificar `scripts/build.py` para que funja como **orquestador (wrapper)**. En lugar de generar HTML estático por su cuenta, preparará el entorno y luego invocará la compilación de Quarto (`quarto render`).
- [x] Asegurarse de que el pipeline genere y deposite la salida consolidada en la carpeta esperada (ej. `site`).
- [x] **Auditoría y Documentación:** Debido a la complejidad de la tarea, documentar exhaustivamente los avances y modificaciones de esta etapa en `README.md`, `docs/ARCHITECTURE.md`, `docs/project_structure.jsonc` y demás archivos que permitan llevar una auditoría clara.

### Etapa 5: Adaptación del Flujo de GitHub Actions (CI/CD)
- [x] Mantener el flujo moderno basado en artefactos del repositorio actual (`upload-pages-artifact` y `deploy-pages`) en el archivo `pages.yml`.
- [x] Instalar la dependencia de Quarto CLI dentro del workflow.
- [x] Modificar el trabajo de compilación en `pages.yml` para ejecutar el build (vía `scripts/build.py` como wrapper) y subir la carpeta de salida (ej. `site`) como artefacto de GitHub Pages. **No** se adoptará la rama `gh-pages`.
- [x] **Auditoría y Documentación:** Debido a la complejidad de la tarea, documentar exhaustivamente los avances y modificaciones de esta etapa en `README.md`, `docs/ARCHITECTURE.md`, `docs/project_structure.jsonc` y demás archivos que permitan llevar una auditoría clara.

---

## Registro de Conflictos y Decisiones de Arquitectura

### 1. Despliegue en GitHub Pages (Artefactos vs Ramas)
**Conflicto:** Propuestas anteriores sugerían usar una rama separada `gh-pages` con la acción de Quarto. Sin embargo, el repositorio actual ya usa el método moderno de subir la carpeta construida mediante artefactos.
**Decisión:** **Se mantendrá el flujo actual de artefactos** en `pages.yml`. Se integrará Quarto CLI en la acción de compilación y se seguirá subiendo la carpeta de compilación (`site/`) vía `upload-pages-artifact`, evitando crear ramas huérfanas o dobles ejecuciones.

### 2. Estructura de Directorios Base (`src/` vs `notes/`)
**Conflicto:** Quarto frecuentemente asume una estructura tipo libro en carpetas separadas (como `notes/`), pero el proyecto tiene como fuente de verdad indiscutible la carpeta `src/`.
**Decisión:** Se rechaza cualquier cambio de directorio. Se mantendrá inmutable `src/` como el origen del contenido. El archivo de configuración `_quarto.yml` deberá apuntar a los documentos existentes en `src/`.

### 3. Preservación y Separación del Front-Matter Obligatorio
**Conflicto:** El motor Quarto exige metadatos estándar, mientras que el proyecto obliga (vía `GEMINI.md`) la presencia de variables estructurales como `id` (MSC standard) y `pilar`.
**Decisión:** Los metadatos coexistirán de forma organizada. El bloque YAML se estructurará colocando los atributos de Quarto en la parte superior, separados por los atributos obligatorios del repositorio mediante comentarios (`#`). Esto asegura que el parser de Quarto procese lo suyo y los scripts de validación de Python mantengan integridad sin conflictos.

### 4. Roles del `build.py` vs Quarto
**Conflicto:** El script actual `scripts/build.py` es responsable de construir el sitio. Al integrar Quarto, este asume la renderización completa.
**Decisión:** Se mantiene la recomendación de adaptar `scripts/build.py` a su nuevo rol como **wrapper**. Se encargará de lanzar `quarto render`, validando o moviendo previamente los directorios necesarios.

### 5. Renderizado de Gráficos y Multiplicación de Archivos
**Conflicto:** Ejecutar scripts de generación de imágenes (`scripts/grafics`) en cada actualización de GitHub Actions ralentizaría el pipeline y multiplicaría innecesariamente la cantidad de archivos binarios/imágenes en el historial del repositorio.
**Decisión:** La generación gráfica estándar y en 3D será absorbida por la tecnología **Typst** embebida en los documentos, gracias a su limpieza semántica. Los scripts en Python de la carpeta `scripts/grafics` quedarán como respaldo para casos altamente complejos y se les aplicará una restricción estricta para **no ejecutarse de forma automática** durante el ciclo de CI/CD.
