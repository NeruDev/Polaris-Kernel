# Contribuyendo a Polaris Kernel

¡Gracias por tu interés en mejorar este sistema de conocimiento! Polaris Kernel es un proyecto de alta ingeniería y esperamos que todas las contribuciones (humanas o de IA) sigan estos estándares.

## 1. El Estándar Bourbaki
Todas las aportaciones teóricas deben clasificarse en uno de los 6 pilares definidos en `ARQUITECTURE.md`. Si un tema no encaja claramente, abre una consulta antes de crear el archivo.

## 2. Reglas de Oro del Contenido
Para maximizar la efectividad del sistema RAG (IA):
- **Atomicidad:** Máximo 300-400 palabras por archivo Markdown.
- **Formato:** 80 caracteres por línea.
- **Párrafos:** Máximo 6 líneas.
- **Metadatos:** Cada `.md` debe empezar con YAML frontmatter válido según `metadata/schemas/content.schema.json`.

## 3. Flujo de Trabajo
1.  **Crea el contenido** en la carpeta de pilar correspondiente dentro de `src/`.
2.  **Genera los activos** necesarios usando scripts de Python en `scripts/grafics/`.
3.  **Ejecuta el Build Local:**
    ```powershell
    python scripts/build.py --verbose
    ```
4.  **Verifica la Calidad:** Asegúrate de que `ruff` y `pytest` pasen sin errores.

## 4. Convenciones de Código
- Usamos **Python 3.11+**.
- Prohibido el uso de **emojis** en scripts y logs.
- Toda operación de archivos debe usar `pathlib`.
- Mantén la **Regla de Adyacencia**: Archivo fuente + Archivo JSON en el mismo nivel.

## 5. Estándar de Commits
Adoptamos **Conventional Commits**. Los mensajes deben seguir el formato `<tipo>: <descripcion>`:
- `feat`: Nuevos pilares, temas o graficos.
- `fix`: Correccion de formulas o errores en scripts.
- `docs`: Cambios en la documentacion.
- `build`: Modificaciones en build.py o dependencias.
- `ci`: Cambios en workflows de GitHub Actions.

---
Al contribuir, aceptas que tu trabajo será licenciado bajo la licencia Apache 2.0 del proyecto.
