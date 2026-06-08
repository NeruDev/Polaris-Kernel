# Documentación de Utilidades (`utils/`)

Esta carpeta engloba las herramientas modulares auxiliares utilizadas por los orquestadores principales para tareas compartidas como manejo de rutas, renderizado y consola.

## Archivos y Funciones Principales

### `links.py`
Encargado de auditar la validez de los enlaces internos en la documentación HTML.
* `detect_broken_internal_links(generated_pages)`: Rastrea y reporta enlaces dentro de los archivos generados que apuntan a rutas u hojas HTML inexistentes.

### `logging.py`
Centraliza la impresión de mensajes estandarizados por consola.
* `log_info(msg)`: Imprime un mensaje estándar con etiqueta `[INFO]`.
* `log_warn(msg)`: Imprime un mensaje de advertencia enviado al flujo de error `stderr` con la etiqueta `[WARN]`.
* `log_error(msg)`: Imprime un mensaje de error crítico al `stderr` con la etiqueta `[ERROR]`.

### `markdown.py`
Proporcionaba la capa original de renderizado avanzado de Markdown a HTML (actualmente Quarto lidera este flujo).
* `convert_md_to_html(md_text, asset_prefix)`: Convierte el texto `.md` a HTML validado e implementa reglas regex para corregir extensiones `.md` vinculadas a `.html`.

### `pathing.py`
Administra lógicas avanzadas de rutas.
* `get_relative_html_path(md_path, base_dir)`: Transforma la ruta original de Markdown en su equivalente HTML relativo para la web.
* `compute_depth(rel_path)`: Calcula niveles de profundidad recursiva dentro del árbol de directorios.
* `build_relative_prefix(depth)`: Genera prefijos iterativos de retroceso direccional (`../`) basados en la profundidad calculada para enlaces relativos cruzados.
