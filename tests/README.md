# Documentación de Pruebas Unitarias (`tests/`)

Este directorio contiene las pruebas automatizadas (vía `pytest`) que aseguran la estabilidad y coherencia arquitectónica de Polaris Kernel.

## Archivos y Funciones Principales

### `conftest.py`
Configuración global de fixtures para las pruebas. Provee herramientas y entornos de pruebas limpios y controlados.
* `repo_root()`: Fixture que devuelve un objeto `Path` apuntando a la raíz real del repositorio.
* `sandbox_project(tmp_path)`: Crea un repositorio temporal ("sandbox") emulando la arquitectura completa de los 6 pilares, archivos MD simulados y estructura básica del Kernel.

### `test_structure.py`
Valida la integridad de la estructura organizativa de directorios y pilares del proyecto.
* `test_six_pillars_exist(repo_root)`: Verifica que existan exactamente los 6 pilares de la arquitectura Bourbaki bajo la carpeta `src/`.
* `test_root_directories_exist(repo_root)`: Valida la existencia de las carpetas core del proyecto (`scripts`, `utils`, `metadata`, `tests`).

### `test_validators.py`
Pruebas para comprobar la robustez de las reglas de validación (codificación y sintaxis).
* `test_utf8_validation_positive(tmp_path)`: Comprueba que el validador acepte archivos guardados en UTF-8 correcto.
* `test_utf8_validation_negative(tmp_path)`: Comprueba que el validador lance un error ante codificaciones incorrectas (ej. latin-1).
* `test_math_syntax_balanced()`: Verifica que el escáner apruebe archivos con fórmulas matemáticas de LaTeX balanceadas (`$..$`).
* `test_math_syntax_unbalanced()`: Asegura que se detecten etiquetas matemáticas sin su correspondiente cierre.

## Flujo de Trabajo de Pruebas

El entorno de pruebas de Polaris Kernel opera bajo `pytest` y utiliza fixtures globales para simular y validar las condiciones del proyecto sin afectar el directorio activo.
1. **Aislamiento y Fixtures:** `conftest.py` proporciona repositorios simulados ("sandboxes") para garantizar que las pruebas de estructura y validación corran en un entorno predecible y seguro.
2. **Verificación Arquitectónica:** `test_structure.py` se ejecuta para afirmar que la taxonomía base (los 6 pilares de Bourbaki) y los directorios fundamentales de utilidades/scripts se mantienen intactos.
3. **Auditoría de Validadores:** `test_validators.py` somete las reglas de codificación UTF-8, balance de ecuaciones en LaTeX y validación semántica a escenarios de estrés (casos positivos y negativos), asegurando la robustez de las herramientas de integración continua.

## Conexión entre Directorios

* **Hacia `scripts/` y `utils/`:** Los tests importan directamente las funciones lógicas desde `scripts/` y `utils/` para evaluarlas. Por ejemplo, se evalúa el validador UTF-8 o el chequeo de fórmulas, originados en los orquestadores y utilidades.
* **Hacia `src/`:** Las reglas arquitectónicas que evalúa `tests/` son aplicadas directamente a la integridad de los pilares estructurales en `src/`.

## Manejo de Datos (Data Handling)

* En el contexto de pruebas, los datos se manejan mediante archivos temporales instanciados por los fixtures (`tmp_path`). 
* No se alteran los metadatos JSON ni los archivos YAML/QMD reales; en su lugar, se inyectan strings en memoria o se crean árboles de carpetas volátiles que replican la estructura de Polaris Kernel.
