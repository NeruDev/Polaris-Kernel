# Documentación de Scripts (`scripts/`)

Este directorio contiene los scripts y orquestadores principales para la construcción, generación de gráficos y manejo de la configuración del proyecto Polaris Kernel.

## Archivos y Funciones Principales

### `automate_image_linking.py`
Script para vinculación automática de imágenes en los archivos de teoría (Markdown/Quarto). Busca coincidencias y actualiza el contenido con los gráficos generados.
* `parse_assets_record(record_path)`: Analiza el archivo `GENERATED_ASSETS.md` para obtener la lista de activos registrados.
* `get_md_files(src_dir)`: Obtiene metadatos e IDs de todos los archivos MD/QMD en la carpeta de teoría.
* `link_assets()`: Compara y vincula automáticamente las imágenes correspondientes en los archivos de teoría basándose en sus IDs o tags.

### `build.py`
Orquestador unificado de construcción y validación. Delega la compilación a Quarto y es el punto de entrada para el CI/CD (`pages.yml`).
* `parse_args()`: Procesa los argumentos de la línea de comandos para el build.
* `validate_project(...)`: Valida la integridad de archivos, codificaciones y esquemas JSON.
* `run_assets(...)`: Llama a `generate_assets.py` si se activa la generación gráfica manual.
* `run_site(...)`: Invoca a `quarto render` para construir el sitio web.
* `run_build()`: Función principal que coordina el flujo de sincronización, validación y renderizado.

### `config.py`
Define configuraciones y estructuras de rutas estáticas.
* `Paths (clase)`: Centraliza todas las rutas críticas del proyecto y define el método `from_project_root()`.
* `BuildConfig (clase)`: Almacena parámetros de compilación como banderas de advertencias y verbosidad.

### `generate_assets.py`
Orquestador de generación de gráficos.
Mantiene retrocompatibilidad con Python/Matplotlib y coordina la ejecución de generadores `.py`.
* `run_graphic_script(script_path)`: Ejecuta de manera segura un único script generador.
* `orchestrate_assets()`: Escanea el directorio de scripts gráficos y los ejecuta en lote, proporcionando un reporte final.

### `grafics/` (Subdirectorio Gráfico)
Contiene scripts especializados en la generación de activos gráficos en el nuevo paradigma basado en Typst.
* `compile_typst.py`: Compilador automatizado de archivos Typst a SVG en lote que actualiza el registro en `metadata/GENERATED_ASSETS.md`.
* `gen_jerarquia_numeros.py`: Script para compilar el gráfico `jerarquia_numeros.typ` usando Typst.
* `typst_src/`: Directorio donde se almacenan las plantillas y archivos fuente `.typ`.

### `update_taxonomy_pillars.py`
Actualiza dinámicamente la taxonomía base MSC cruzando datos con los pilares estructurales.
* `update_taxonomy()`: Carga el overlay, mapea los códigos MSC hacia pilares principales y secundarios, y sobrescribe `msc_taxonomy.all.json`.

## Flujo de Trabajo y Orquestación

El flujo principal está dirigido por `build.py`, el cual coordina las validaciones y el proceso de renderizado:
1. **Sincronización de Metadatos:** Se invoca `MetadataAgent` (en `scripts/io/metadata_agent.py`) para leer el frontmatter YAML de los archivos `.qmd`/`.md` y actualizar/generar los archivos `.json` adyacentes (ADR-002).
2. **Validación:** Se ejecutan verificaciones de sintaxis matemática, codificación UTF-8, y estructura semántica (Semantic Line Breaks) en todo el repositorio. Las alertas se recopilan mediante la clase `ErrorCollector`.
3. **Vinculación de Activos (Opcional):** `automate_image_linking.py` puede usarse para inyectar enlaces a imágenes SVG generadas en el texto de los archivos fuente, respetando los bloques de frontmatter YAML.
4. **Generación de Activos (Opcional):** Si se habilita, `generate_assets.py` orquesta la compilación masiva de gráficos vectoriales (principalmente Typst hacia SVG).
5. **Renderizado Quarto:** `build.py` invoca el comando `quarto render` para construir el sitio estático final bajo el directorio `site/`.
6. **Auditoría de Enlaces:** Finalmente, se revisan los enlaces internos rotos en el directorio `site/` utilizando las utilidades.

## Conexión entre Directorios

* **Hacia `utils/`:** Los scripts de orquestación dependen fundamentalmente del directorio de utilidades. Extraen constantes de rutas higiénicas (`utils/pathing.py`), utilizan funciones compartidas de renderizado/auditoría (`utils/links.py`, `utils/markdown.py`), y centralizan los mensajes de consola (`utils/logging.py`).
* **Hacia `src/` y `metadata/`:** `scripts/` actúa sobre el pilar teórico (`src/`). Extrae su información, parsea el frontmatter YAML, compila scripts de gráficos hacia activos en `src/`, y actualiza el registro en `metadata/`.
* **Hacia `tests/`:** Las reglas de integridad y el comportamiento esperado del pipeline en `scripts/` se verifican mediante las pruebas unitarias y de integración contenidas en el directorio de pruebas.

## Manejo de Datos (Data Handling)

* **Formatos Principales:** El sistema opera principalmente con archivos Markdown (`.md`) y Quarto Markdown (`.qmd`) como fuente de verdad teórica.
* **Metadatos (ADR-002):** Existe una sincronización obligatoria entre el YAML frontmatter de los documentos y archivos JSON adyacentes ("Adyacencia Semántica"). Esto es facilitado por el `MetadataAgent`.
* **Generación Vectorial:** Los scripts fuente de Typst se compilan a SVG, que luego son vinculados y presentados a través del sitio estático sin comprometer binarios pesados en el repositorio de código.
* **Reportes de Error:** Durante el proceso de construcción, las advertencias y errores no interrumpen de inmediato (salvo errores críticos) sino que se acumulan en un objeto central, evaluando al final contra el umbral configurado (`config.strict`).
