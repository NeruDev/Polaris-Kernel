# Plan de Sanitización y Correcciones de Caracteres Especiales DLMF

## Introducción

Este documento establece el plan integral de sanitización para los archivos en formato Markdown provenientes de la biblioteca matemática DLMF (NIST Digital Library of Mathematical Functions).
Tras revisar la documentación original en `docs/DLMF-markdown-main/README.md` y explorar la estructura de los contenidos, se han identificado diversas macros LaTeX no estándares y entidades HTML escapadas.
Estas peculiaridades causan fallos de visualización y errores de sintaxis en motores de renderizado Markdown y LaTeX como Quarto, KaTeX y MathJax.

## Tabla de Caracteres y Macros Especiales a Corregir

| Elemento Original | Significado / Contexto | Problema de Renderizado | Acción de Sanitización Propuesta |
|---|---|---|---|
| `\*` | Multiplicación semántica invisible en DLMF | Se interpreta como asterisco escapado o causa fallos en bloques math | Eliminar o sustituir por espacio fino `\,` o `\cdot` según el contexto |
| `\ifrac{a}{b}` | Fracción en línea (*inline fraction*) | Macro de LaTeX no estándar no reconocida por KaTeX/MathJax | Convertir a `a/b` o a `\frac{a}{b}`, o definir la macro globalmente |
| `\NVar{a}` | Variable nueva (*New Variable*) sin significado especial en infoboxes | Comando no estándar no soportado por motores web | Extraer el argumento `a` o definir `\newcommand{\NVar}[1]{#1}` |
| `\cfracstyle{d}` | Estilo visual de fracciones continuas en la sección 1.12 | Comando no estándar no soportado | Eliminar la macro o reemplazar por `\displaystyle` |
| `\mskip` (ej. `\mskip-3.0mu`) | Espaciado sintáctico en LaTeX | Incompatible con KaTeX | Sustituir por `\mspace{-3mu}` o `\mspace{3mu}` |
| `\pvint` | Valor principal de Cauchy para integrales | Simbolo no nativo en KaTeX/MathJax | Sustituir por `\fint` o agregar macro de soporte |
| `&amp;` | Entidad HTML dentro de matrices LaTeX (ej. `vmatrix`) | Rompe la delimitación de columnas en matrices LaTeX | Convertir a carácter literal `&` |
| `&lt;` / `&gt;` | Entidades HTML en bloques de ecuaciones matemáticas | Rompe la sintaxis matemática de desigualdades | Convertir a `<` y `>` respectivamente |

## Plan de Acción para la Sanitización

1. **Creación de Script de Limpieza (`scripts/sanitizar_dlmf.py`)**:
   Implementar un script en Python para procesar de manera automatizada los archivos Markdown situados en `docs/DLMF-markdown-main/markdown/`.
   Aplicar expresiones regulares para corregir las macros y entidades HTML de forma consistente.

2. **Definición de Macros Globales en Quarto / MathJax**:
   Configurar macros fallback en el sistema para mantener la compatibilidad en caso de preservar comandos originales.
   Asegurar que el motor Quarto pueda procesar expresiones matemáticas sin arrojar advertencias de compilación.

3. **Validación y Verificación de Sintaxis**:
   Ejecutar pruebas automatizadas para comprobar que ningún bloque LaTeX contenga sintaxis corrupta tras el procesamiento.
   Verificar el renderizado final mediante el proceso de build del proyecto.
