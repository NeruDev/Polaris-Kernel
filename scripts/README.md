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
Orquestador de generación de gráficos. Mantiene retrocompatibilidad con Python/Matplotlib y coordina la actualización masiva de SVG.
* `run_graphic_script(script_path)`: Ejecuta de manera segura un único script generador.
* `orchestrate_assets()`: Escanea el directorio de scripts gráficos y los ejecuta en lote, proporcionando un reporte final.

### `templates.py`
Define y aplica estilos visuales unificados para gráficos históricos creados con Matplotlib.
* `get_colors()`: Retorna el diccionario con la paleta de colores oficial del proyecto.
* `setup_style()`: Configura globalmente los parámetros (`rcParams`) de Matplotlib usando esta paleta.

### `update_taxonomy_pillars.py`
Actualiza dinámicamente la taxonomía base MSC cruzando datos con los pilares estructurales.
* `update_taxonomy()`: Carga el overlay, mapea los códigos MSC hacia pilares principales y secundarios, y sobrescribe `msc_taxonomy.all.json`.
