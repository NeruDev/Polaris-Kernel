# Polaris Kernel (MathKernel)

[![Deploy Pages](https://github.com/NeruDev/Polaris-Kernel/actions/workflows/pages.yml/badge.svg)](https://github.com/NeruDev/Polaris-Kernel/actions/workflows/pages.yml)
[![AI-Agent Friendly](https://img.shields.io/badge/AI-Agent%20Friendly-39C5BB?style=flat-square)](GEMINI.md)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-D22128?style=flat-square)](LICENSE)
[![MSC 2020](https://img.shields.io/badge/MSC--2020-Compatible-primary?style=flat-square)](https://zbmath.org/static/msc2020.pdf)

> **Estructurando la belleza de las matemáticas para humanos y máquinas.**

Polaris Kernel es una infraestructura de conocimiento matemático de alta fidelidad. Utiliza la arquitectura Bourbaki para organizar el conocimiento en pilares atómicos, semánticos e ilustrados, optimizados para el consumo autodidacta y la integración con agentes de IA autónomos.

**Visualiza los resultados directamente en:**  
👉 [https://nerudev.github.io/Polaris-Kernel/](https://nerudev.github.io/Polaris-Kernel/)

El proyecto implementa una jerarquía modular estricta dividida en 6 pilares fundamentales, ahora renderizados mediante el **nuevo paradigma de Quarto y Typst**, y desplegados de forma automatizada y sin ramas huérfanas mediante **GitHub Actions (`pages.yml`)**:

```mermaid
graph TD
    PK[Polaris Kernel] --> P1[01 Fundamentos y Logica]
    PK --> P2[02 Estructuras Algebraicas]
    PK --> P3[03 Analisis y Continuidad]
    PK --> P4[04 Espacio y Forma]
    PK --> P5[05 Discrecion y Computacion]
    PK --> P6[06 Estocastica e Incertidumbre]

    style PK fill:#39C5BB,stroke:#fff,stroke-width:2px,color:#fff
    style P3 fill:#3498db,stroke:#fff,color:#fff
    style P4 fill:#3498db,stroke:#fff,color:#fff
```

---

## 🚀 Capacidades del Ecosistema

### 1. Enfoque "AI-Adjacent" (Adyacencia Semántica)
A diferencia de los repositorios tradicionales, Polaris Kernel aplica la **Regla de Adyacencia**:
- Cada archivo `.qmd` (teoría) o `.py` (herramientas) tiene un archivo `.json` homónimo en el mismo directorio.
- Esto permite que los agentes de IA descubran capacidades y conceptos mediante inspección de metadatos antes de procesar el código pesado.

### 2. Atomicidad Semántica (RAG-Ready)
Todo el contenido está segmentado bajo reglas estrictas para maximizar la efectividad en sistemas de **Generación Aumentada por Recuperación (RAG)**:
- **Límite:** ~300 palabras por archivo.
- **Formato:** 80 caracteres por línea (Git-friendly).
- **Estructura:** Un archivo = Un concepto independiente.

### 3. Iconografía Vectorial Nativa (Quarto & Typst)
Generación programática de activos gráficos vectoriales utilizando el nuevo paradigma y librerías nativas de **Typst** (ej. CeTZ, Fletcher, Lilaq).
Los scripts fuentes se integran a través de la compilación de Typst y Quarto, asegurando rutas relativas directas, portabilidad y alta calidad tipográfica coherente con el proyecto (documentado en [typst_graficos.md](file:///G:/REPOSITORIOS_GITHUB/POLARIS_KERNEL/docs/typst_graficos.md)).
Quarto actúa como el orquestador principal.

### 4. Computación Interactiva en Vivo (Quarto Live)
El proyecto integra la extensión oficial **Quarto Live** (ubicada en `_extensions/r-wasm/live`).
Esta extensión habilita la ejecución interactiva de código y ejercicios interactivos directamente en el navegador del usuario utilizando WebAssembly (Wasm).
*   **Motores de Ejecución**: Permite ejecutar Python (a través de Pyodide) y R (a través de webR) de forma local en el cliente estático, sin depender de servidores externos.
*   **Formatos e Integración**: Se activa en los documentos Quarto utilizando el formato `live-html` en el frontmatter del archivo `.qmd`.
*   **Uso en Python (Pyodide)**:
    Los bloques interactivos de Python se definen utilizando el motor `{pyodide}`.
    ```python
    ```{pyodide}
    import numpy as np
    print("¡Hola desde Python interactivo en el navegador!")
    ```
    ```
*   **Uso en R (webR)**:
    Los bloques interactivos de R se definen utilizando el motor `{webr}`.
    ```r
    ```{webr}
    fit <- lm(mpg ~ wt, data = mtcars)
    summary(fit)
    ```
    ```
*   **Gestión de Librerías**:
    Las librerías requeridas se pueden especificar y precargar dinámicamente desde los metadatos YAML del documento `.qmd`.
    ```yaml
    pyodide:
      packages:
        - numpy
        - matplotlib
    ```

---

## 🛠️ Flujo de Ingeniería y CI/CD

### Despliegue con GitHub Actions (`pages.yml`)
El flujo de trabajo automatizado se ha modificado. El proyecto ya no depende de la rama `gh-pages` heredada; en su lugar, la acción de GitHub empaqueta directamente la carpeta `site/` y la sube utilizando **`upload-pages-artifact`**, asegurando un despliegue transparente desde `main` manteniendo el CI/CD nativo de Polaris Kernel.

### Instalación Determinista
Optimizado para entornos Windows 11 con PowerShell:

```powershell
# Clonar con activos graficos
git lfs install
git clone git@github.com:NeruDev/Polaris-Kernel.git
cd Polaris-Kernel

# Preparar entorno
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install .
```

### Build System Orquestado
El orquestador central gestiona el ciclo de vida completo:

```powershell
# Sincronizar Metadatos -> Validar por Schema -> Renderizar (Quarto/Typst)
python scripts/build.py --verbose
```

---

## 🚦 Estándares de Calidad

| Herramienta | Rol en el Ecosistema |
| :--- | :--- |
| **Ruff** | Linter y formateador de alta velocidad. |
| **Mypy** | Verificación estática de tipos para lógica crítica. |
| **Jsonschema** | Validación formal de metadatos y taxonomía MSC. |
| **Pytest** | Garantía de integridad estructural y matemática. |

---

## 🤖 Guía para Agentes de IA

Si eres un agente de IA, lee los siguientes archivos para entender tu marco operativo:
1.  [`llms.txt`](llms.txt): Resumen técnico para descubrimiento.
2.  [`GEMINI.md`](GEMINI.md): Reglas de comportamiento y navegación.
3.  [`AGENTS.md`](AGENTS.md): Convenciones globales de nombrado y estructura.

---
**Polaris Kernel** — *The Kernel of Knowledge.*
https://nerudev.github.io/Polaris-Kernel/
