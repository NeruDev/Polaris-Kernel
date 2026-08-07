# Documentación de Utilidades (`utils/`)

Esta carpeta engloba las herramientas modulares auxiliares utilizadas por los orquestadores principales para tareas compartidas como manejo de rutas, renderizado y logging de consola.

## Archivos y Funciones Principales

### [`links.py`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/utils/links.py)
Encargado de auditar la validez de los enlaces internos en la documentación HTML generada.
* `detect_broken_internal_links(generated_pages)`: Rastrea y reporta enlaces rotos o referencias a páginas u hojas HTML inexistentes.

### [`logging.py`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/utils/logging.py)
Centraliza la impresión de mensajes estandarizados por consola.
* `log_info(msg)`: Imprime mensajes informativos con la etiqueta `[INFO]`.
* `log_warn(msg)`: Imprime advertencias dirigidas al flujo de error `stderr` con la etiqueta `[WARN]`.
* `log_error(msg)`: Imprime errores críticos en `stderr` con la etiqueta `[ERROR]`.

### [`markdown.py`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/utils/markdown.py)
Proporciona utilidades para el análisis y renderizado de contenido Markdown.
* `convert_md_to_html(md_text, asset_prefix)`: Convierte texto Markdown a HTML y ajusta enlaces con extensiones relativas.

### [`pathing.py`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/utils/pathing.py)
Administra lógicas avanzadas de resolución e higiene de rutas.
* `get_relative_html_path(md_path, base_dir)`: Transforma la ruta original de un documento Markdown a su ruta equivalente HTML.
* `compute_depth(rel_path)`: Calcula el nivel de profundidad dentro del árbol de directorios.
* `build_relative_prefix(depth)`: Genera prefijos de retroceso direccional (`../`) para enlaces cruzados entre carpetas.

## Flujo de Trabajo y Funcionalidad

El directorio `utils/` opera como una biblioteca interna proveedora de servicios comunes.
1. **Resolución de Rutas:** Módulos como `pathing.py` calculan profundidades y normalizan rutas garantizando convenciones sin espacios ni acentos.
2. **Validación:** `markdown.py` asiste en la verificación de reglas semánticas en documentos Markdown.
3. **Auditoría Post-Build:** Tras el renderizado con Quarto, `links.py` escanea la salida para detectar hipervínculos rotos e imágenes faltantes.
4. **Logging Consistente:** Todo mensaje en consola utiliza `logging.py` para mantener un formato unificado.

## Relación con otros Directorios

* **Desde `scripts/`:** Las utilidades son consumidas por orquestadores como `build.py` y `automate_image_linking.py`.
* **Desde `tests/`:** Las pruebas unitarias invocan directamente las funciones utilitarias para verificar su corrección.
