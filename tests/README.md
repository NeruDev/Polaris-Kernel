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
