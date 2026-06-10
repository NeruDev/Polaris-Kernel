---
id: 'quarto_live_guide'
title: 'Guia de Computacion Interactiva con Quarto Live'
pilar: 'docs'
tags: ['quarto', 'live', 'wasm', 'pyodide', 'webr']
---

# Guia de Computacion Interactiva con Quarto Live

## 1. Introduccion y Proposito

Quarto Live es una extension oficial de Quarto diseñada para habilitar ejecucion interactiva de codigo y evaluacion en vivo en el navegador.
Utiliza tecnologia WebAssembly (Wasm) para ejecutar motores cientificos completos del lado del cliente.
Esto elimina la necesidad de contar con servidores externos o dependencias complejas como servidores Shiny o backends de Jupyter en ejecucion continua.

En Polaris Kernel, esta capacidad se utiliza para complementar la teoria matematica con simulaciones interactivas, consolas de prueba de algoritmos y cuestionarios de evaluacion dinamica.

---

## 2. Tecnologias de Soporte

La extension implementa dos motores fundamentales basados en WebAssembly:

### 2.1 Pyodide (Python en Wasm)
*   **Funcionamiento**: Pyodide compila el interprete de CPython a WebAssembly.
*   **Ecosistema**: Permite el uso directo en el navegador de librerias cientificas de primer nivel como NumPy, SciPy, Matplotlib y Pandas.
*   **Uso en el Kernel**: Ideal para modelado numerico, visualizacion de graficas en 2D/3D (Matplotlib) y ejecucion de metodos numericos.

### 2.2 webR (R en Wasm)
*   **Funcionamiento**: webR compila el motor estadistico de R en WebAssembly.
*   **Ecosistema**: Habilita la ejecucion de scripts en R y la carga de paquetes del repositorio CRAN.
*   **Uso en el Kernel**: Utilizado principalmente en simulaciones de probabilidad, estadistica descriptiva y modelado estocastico.

---

## 3. Configuracion y Activacion

Para habilitar Quarto Live en un documento de teoria del repositorio, se deben configurar las siguientes directivas en el frontmatter de Quarto:

```yaml
---
title: "Teorema Central del Limite"
format: live-html
engine: knitr
---
```

> [!IMPORTANT]
> Es sumamente importante utilizar el formato `live-html` en lugar de `html` estandar para activar los scripts del runtime interactivo.
> Si se utiliza el motor `knitr` bajo ciertas configuraciones locales, se debe incluir la directiva de inclusion en la primera linea util del documento:
> `{{< include ./_extensions/r-wasm/live/_knitr.qmd >}}`

---

## 4. Estructura de Celdas de Codigo

### 4.1 Consola Interactiva Basica (Python/Pyodide)
Para crear un editor interactivo donde el lector pueda experimentar y ejecutar codigo Python, utiliza el identificador de motor `{pyodide}` en la declaracion del bloque de codigo.
Por ejemplo:

```python
# Ejemplo de bloque interactivo (usa la etiqueta {pyodide})
import numpy as np
matriz = np.array([[1, 2], [3, 4]])
print(np.linalg.det(matriz))
```

### 4.2 Consola Interactiva Basica (R/webR)
De manera equivalente, para R se utiliza el identificador de motor `{webr}` en la declaracion del bloque de codigo:

```r
# Ejemplo de bloque interactivo (usa la etiqueta {webr})
summary(cars)
```

---

## 5. Ejercicios y Calificacion en Vivo

Quarto Live soporta la definicion de bloques de ejercicios con pistas (hints) y comprobaciones automaticas de soluciones.

### 5.1 Definicion de un Ejercicio
Para crear un ejercicio interactivo, se añade la opcion `ex` o `exercise` a la celda declarada con el motor interactivo:

```python
# Celda de configuracion de ejercicio (setup)
#| setup: true
# Codigo oculto de preparacion de variables
```

```python
# Celda del ejercicio para el estudiante (Usa la etiqueta {pyodide})
#| exercise: mi_ejercicio
# Instruccion: Completa la funcion para retornar la traza de la matriz
def traza(matriz):
    pass
```

### 5.2 Pistas (Hints)
Las pistas se colocan en una celda dedicada que comparte el nombre del ejercicio añadiendo el sufijo `-hint`:

```python
# Celda de pista (Usa la etiqueta {pyodide})
#| exercise: mi_ejercicio-hint
#| eval: false
# Pista: Puedes usar numpy para calcular la traza de forma directa.
```

### 5.3 Solucion y Verificacion
Para proveer la solucion y ejecutar la evaluacion automatica (grading), se usa el sufijo `-solution`:

```python
# Celda de solucion (Usa la etiqueta {pyodide})
#| exercise: mi_ejercicio-solution
#| eval: false
def traza(matriz):
    import numpy as np
    return np.trace(matriz)
```

---

## 6. Gestion de Paquetes y Dependencias

Es posible configurar que paquetes de Python o R deben cargarse de forma anticipada cuando el documento se inicializa en el navegador del usuario.
Esto reduce los tiempos de espera interactivos posteriores.

### 6.1 Declaracion en el Frontmatter YAML
```yaml
pyodide:
  packages:
    - numpy
    - matplotlib
    - pandas
```

De igual forma para R:
```yaml
webr:
  packages:
    - ggplot2
    - dplyr
```

---

## 7. Directrices de Despliegue en GitHub Pages

Al compilar el sitio estatico final, el pipeline de CI/CD del repositorio (`pages.yml`) procesa los archivos `.qmd` interactivos con la CLI de Quarto.
Dado que Quarto Live opera en el lado del cliente (Client-Side), el directorio compilado final `site/` no requiere un servidor dinamico ni contenedores Docker.
El sitio web estatico desplegado a traves de GitHub Pages servira de manera directa los archivos Javascript (`live-runtime.js`) y WebAssembly de forma instantanea al navegador del usuario final.
