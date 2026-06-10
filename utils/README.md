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

## Flujo de Trabajo y Funcionalidad

El directorio `utils/` no se ejecuta de manera independiente, sino que funciona como una biblioteca interna estandarizada, proveedora de servicios comunes.
1. **Rutas y Nomenclaturas:** Módulos como `pathing.py` ofrecen cálculos de profundidad y normalización, asegurando que Polaris Kernel mantenga convenciones limpias sin acentos ni espacios (Higiene de Rutas).
2. **Validación y Renderizado:** `markdown.py` provee las reglas para validar los saltos de línea semánticos ("Semantic Line Breaks") dentro de los documentos QMD/MD.
3. **Auditoría Post-Build:** Tras el renderizado con Quarto, `links.py` escanea recursivamente el directorio de salida (ej. `site/`) parseando el HTML para detectar hipervínculos rotos y dependencias de activos (`href`, `src`) faltantes, levantando alarmas.
4. **Consola:** Todo intercambio de información a la terminal pasa por `logging.py`, manteniendo el formato `[INFO]`, `[WARN]`, `[ERROR]`.

## Conexión entre Directorios

* **Desde `scripts/`:** Las herramientas en `utils/` son consumidas intensivamente por el pipeline de construcción de `scripts/build.py` y el motor de enlace `scripts/automate_image_linking.py`.
* **Desde `tests/`:** Las pruebas unitarias invocan directamente las funciones utilitarias para verificar su precisión matemática y lógicas de parseo en entornos simulados.

## Manejo de Datos (Data Handling)

* **Abstracción de Rutas:** Evita referencias a rutas absolutas "quemadas" (hardcoded) en código mediante las utilidades estandarizadas.
* **Parseo HTML:** Emplea herramientas como `BeautifulSoup` en la post-compilación para navegar por el árbol DOM de los documentos HTML generados y auditar el sistema de enlaces internos y las referencias a SVGs, garantizando un manejo robusto de los datos y rutas entre documentos.
