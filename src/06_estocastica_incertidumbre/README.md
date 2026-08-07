# Pilar 06: Estocástica e Incertidumbre - Registro de Activos Gráficos

Este documento describe el estándar utilizado para la generación de imágenes y gráficos dentro de este pilar, así como los parámetros clave de los scripts origen para facilitar su futuro mantenimiento y escalabilidad.

## Formato y Configuración General

- **Motor de Renderizado:** Typst (v0.15.1)
- **Librería de Dibujo:** `@preview/cetz:0.3.3`
- **Formato de Salida:** Scalable Vector Graphics (`.svg`)
- **Directorio de Fuentes:** `scripts/grafics/typst_src/`
- **Prefijo de Archivos:** `06_estocastica_incertidumbre___`

Los gráficos en este pilar (Probabilidad y Estadística) se caracterizan por presentar campanas de Gauss (Normales), puntos de dispersión aleatorios generados matemáticamente y visualizaciones de flujo de probabilidades (cadenas de Markov y diagramas de árbol bayesianos).

---

## Gráficos del Pilar 6 y sus Parámetros Clave

### 1. Variables Aleatorias y Esperanza (`esperanza_varianza.svg`)
Ilustración del centro de gravedad (valor esperado) de una distribución de probabilidad discreta o continua.
- **Parámetros:** La palanca o balanza tiene puntos de masa (probabilidades). Las coordenadas `circle()` en $y=0$ deben equilibrarse con el triángulo (fulcro) ubicado exactamente en $E[X]$.

### 2. Distribuciones Fundamentales (`distribuciones_probabilidad.svg`)
Campana de Gauss clásica $N(\mu, \sigma^2)$.
- **Parámetros:** Uso explícito de la ecuación `calc.exp(-x*x / 2.0) / calc.sqrt(2.0 * calc.pi)` evaluada de $[-4, 4]$ en iteraciones. El área rellena bajo la curva (e.g. varianza de $\pm 1 \sigma$ cubriendo $68.2\%$) utiliza `close: true` y polígonos cerrados sobre el eje $X$.

### 3. Procesos Estocásticos (`cadenas_markov.svg`)
Autómata de estados de probabilidades de transición con la suma de cada salida igual a 1.
- **Parámetros:** Grafo dirigido con estados `(S1, S2, ...)`. Se usan bucles iterativos o flechas curvas `arc()` para transiciones sobre un mismo estado (recurrencia $P_{ii}$).

### 4. Lógica Bayesiana (`inferencia_bayesiana.svg`)
Diagramas de árbol (probabilidad condicional y Total) o espacio muestral particionado (Diagrama de Venn segmentado).
- **Parámetros:** Si se usa formato de árbol, ajustar márgenes $X, Y$ de los nodos. Si se usan conjuntos rectangulares particionados, ajustar la posición de las fronteras (split) que define $P(A|B)$.

### 5. Estadística Inferencial (`regresion_y_correlacion.svg`)
Nube de puntos de dispersión (Scatter plot) y la recta de Mínimos Cuadrados (Regresión Lineal Simple).
- **Parámetros:** La matriz o lista estática de coordenadas (Ej. `data = ((0.5, 1.2), (1.0, 1.8), ...)`). Para recalcular la línea de regresión $\hat{y} = \beta_0 + \beta_1 x$, se actualizan directamente los coeficientes de la ecuación `line-fn(x)` dibujada sobre los límites del eje $X$.

### 6. Convergencia Estocástica (`teoremas_limite.svg`)
Teorema del Límite Central, mostrando cómo distribuciones superpuestas se aproximan a la Normal conforme $n \to \infty$.
- **Parámetros:** Formas base como rectángulos (uniforme, $n=1$), triángulos ($n=2$) y la campana suave superpuestos. El control visual se logra mediante variaciones en la opacidad del relleno (`fill: rgb(..., 50)`).

### 7. Combinatoria (`combinatoria_permutacion.svg`)
Diagramas de urnas y bolas, o arreglos jerárquicos simples.
- **Parámetros:** Colocación iterada de símbolos o círculos coloreados usando contadores en Tipst.
