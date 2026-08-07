# Documentación de Pruebas Unitarias (`tests/`)

Este directorio contiene las pruebas automatizadas (vía `pytest`) que aseguran la estabilidad y coherencia arquitectónica de Polaris Kernel.

## Archivos y Funciones Principales

### [`conftest.py`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/tests/conftest.py)
Configuración global de fixtures para las pruebas.
Provee entornos de prueba aislados y reproducibles.
* `repo_root()`: Fixture que devuelve la ruta absoluta (`Path`) a la raíz del repositorio.
* `sandbox_project(tmp_path)`: Crea un repositorio temporal simulando la estructura completa de los 6 pilares de Bourbaki y la configuración base del Kernel.

### [`test_structure.py`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/tests/test_structure.py)
Valida la integridad de la estructura organizativa de directorios y pilares del proyecto.
* `test_six_pillars_exist(repo_root)`: Comprueba la existencia de los 6 pilares de la arquitectura en `src/`.
* `test_root_directories_exist(repo_root)`: Valida que existan las carpetas core (`scripts`, `utils`, `metadata`, `tests`, `docs`).

### [`test_validators.py`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/tests/test_validators.py)
Pruebas para comprobar la robustez de las reglas de validación de codificación y sintaxis.
* `test_utf8_validation_positive(tmp_path)`: Comprueba que el validador acepte archivos en formato UTF-8 correcto.
* `test_utf8_validation_negative(tmp_path)`: Asegura que se detecten y rechacen codificaciones incorrectas (ej. latin-1).
* `test_math_syntax_balanced()`: Verifica la aprobación de documentos con fórmulas LaTeX balanceadas (`$...$`).
* `test_math_syntax_unbalanced()`: Confirma la detección de etiquetas matemáticas sin cierre.

## Flujo de Trabajo de Pruebas

El entorno de pruebas opera mediante `pytest` empleando fixtures globales para simular escenarios sin alterar el repositorio real.
1. **Aislamiento:** `conftest.py` instancia directorios temporales ("sandboxes") para ejecutar pruebas en entornos limpios.
2. **Verificación de Estructura:** `test_structure.py` confirma el mantenimiento de los 6 pilares y directorios fundamentales.
3. **Auditoría de Validadores:** `test_validators.py` somete a prueba las reglas de codificación y sintaxis matemática.

## Relación con otros Directorios

* **Con `scripts/` y `utils/`:** Evalúa directamente las funciones de validación, renderizado y análisis importadas desde estas carpetas.
* **Con `src/`:** Garantiza la adherencia a la taxonomía estructural de los pilares.
* **Con `docs/`:** Asegura el cumplimiento de los criterios arquitectónicos documentados.
