# Plan de Escalabilidad y Registro de Avance: Polaris Kernel

***
**Versión:** 1.0  
**Estado:** `Activo y En Progreso`  
**Estándar de Nomenclatura:** MSC 2020  
**Última Actualización:** 2026-07-22  
***

## 1. Propósito y Modelo de Escalabilidad

Este documento establece la hoja de ruta integral para el crecimiento modular y ordenado del contenido matemático en **Polaris Kernel**, siguiendo las directrices de arquitectura técnica estipuladas en [ARQUITECTURE.md](ARQUITECTURE.md).

La prioridad estratégica del proyecto radica en **garantizar una cobertura sólida y completa de los conceptos básicos y fundamentales** dentro de los 6 pilares de Bourbaki. Esto previene vacíos conceptuales antes de abordar temas de abstracción formal avanzada.

```mermaid
graph TD
    subgraph Escalabilidad_Faseada[Estrategia de Crecimiento Progresivo]
        Fase1[Fase 1: Fundamentos Completada]
        Fase2[Fase 2: Enriquecimiento Intro (Activa)]
        Fase3[Fase 3: Teoremas Intermedios/Avanzados]
    end

    Fase1 -->|Requisito de Cobertura Completa| Fase2
    Fase2 -->|Consolidación Nivel Básico| Fase3
```

---

## 2. Principios de Integración y Calidad (IA-Ready)

Cualquier nuevo tema incorporado a Polaris Kernel debe cumplir de manera estricta con las siguientes reglas arquitectónicas:

1. **Adyacencia Semántica (.json adyacente):** Todo archivo `.qmd` en `src/` debe poseer su par descriptivo `.json` en el mismo directorio.
2. **Atomicidad Semántica:** De 300 a 500 palabras de prosa pura por archivo `.qmd` (excluyendo YAML frontmatter y la sección "Glosario de variables").
3. **Saltos de Línea Semánticos (Semantic Line Breaks):** Redacción de una oración completa por línea. Las ecuaciones LaTeX de bloque (`$$...$$`) están exentas del límite de longitud.
4. **Glosario de Variables en Tabla:** Para mantener homogeneidad de parseo, el glosario final debe presentarse estrictamente como una tabla Markdown de tres columnas (`Símbolo`, `Descripción`, `Tipo`).
5. **Exactitud de Metadatos y Carpetas:** Los archivos `.json` deben definir explícitamente el `"nivel"`, y la triada (JSON, QMD, SVG) debe crearse/moverse a su respectiva subcarpeta (`intro/`, `intermedio/`, etc.) para asegurar la clasificación de dificultad.
6. **Trinidad de Activos Gráficos:**
   - Código fuente gráfico Typst en `scripts/grafics/typst_src/<pilar>___<dificultad>___<nombre_sin_numeros>.typ`
   - Gráfico SVG exportado en el directorio correspondiente de `src/<pilar>/<dificultad>/<nombre_sin_numeros>.svg`
   - Registro del activo en `metadata/GENERATED_ASSETS.md`
   - *(Importante: El `<nombre_sin_numeros>` no debe heredar el prefijo `01_` del archivo `.qmd` para evitar confusión con los archivos teóricos).*
7. **Validación del Pipeline de Construcción:** Ejecución obligatoria de `python scripts/build.py` (o `quarto render`) para asegurar integridad.

---

## 3. Matriz de Progreso por Pilar

La siguiente tabla consolida el estado actual del contenido y el avance en la cobertura de conceptos básicos para cada pilar:

| Pilar | Archivos Actuales | Cobertura Actual | Estado Fase 1 | Progreso Fase 2 (Intro) |
| :--- | :---: | :--- | :---: | :---: |
| **01. Fundamentos y Lógica** | 8 | Aritmética, conjuntos, lógica proposicional básica y demostraciones. | Completado | 0% (Pendiente) |
| **02. Estructuras Algebraicas** | 8 | Álgebra elemental, matrices, anillos y categorías. | Completado | 0% (Pendiente) |
| **03. Análisis y Continuidad** | 11 | Límites, derivada, integral, EDs, análisis funcional, transcendentes. | Completado | 0% (Pendiente) |
| **04. Espacio y Forma** | 8 | Geometría euclidiana, trigonometría, analítica, topología, diferencial. | Completado | 0% (Pendiente) |
| **05. Discreción y Computación** | 8 | Combinatoria, grafos, teoría de números, métodos numéricos. | Completado | 0% (Pendiente) |
| **06. Estocástica e Incertidumbre** | 8 | Estadística descriptiva, probabilidad, inferencia, entropía. | Completado | 0% (Pendiente) |

---

## 4. Plan Detallado de Escalabilidad por Pilar

### 4.1 Pilar 01: Fundamentos y Lógica (`src/01_fundamentos_logica/`)

* **Estado Actual:** Contiene aritmética básica, sistemas numéricos, tablas de verdad, teoría intuitiva de conjuntos, métodos de demostración y relaciones de equivalencia.
* **Temas Prioritarios Fase 1 (Conceptos Básicos Faltantes):**

| ID / Archivo `.qmd` | Código MSC | Título del Módulo | Estado |
| :--- | :--- | :--- | :---: |
| `01_aritmetica_propiedades.qmd` | 11-01 | Aritmética: Propiedades de las Operaciones | Completado |
| `01_sistemas_numericos.qmd` | 11-01 | Sistemas Numéricos | Completado |
| `02_logica_matematica.qmd` | 03B05 | Lógica Matemática | Completado |
| `03_teoria_conjuntos.qmd` | 03E05 | Teoría de Conjuntos | Completado |
| `04_metodos_demostracion.qmd` | 03-01 | Métodos de Demostración | Completado |
| `05_relaciones_equivalencia.qmd` | 03E02 | Relaciones de Equivalencia | Completado |
| `06_funciones_y_mapeos.qmd` | 03E05 | Funciones e Inyectividad/Sobreyectividad/Biyectividad | Pendiente |
| `07_logica_predicados_inferencia.qmd` | 03B10 | Lógica de Predicados y Reglas Formales de Inferencia | Pendiente |

---

### 4.2 Pilar 02: Estructuras Algebraicas (`src/02_estructuras_algebraicas/`)

* **Estado Actual:** Cubre expresiones elementales, álgebra lineal matricial, grupos, anillos/cuerpos y categorías.
* **Temas Prioritarios Fase 1 (Conceptos Básicos Faltantes):**

| ID / Archivo `.qmd` | Código MSC | Título del Módulo | Estado |
| :--- | :--- | :--- | :---: |
| `01_algebra_elemental.qmd` | 12-01 | Álgebra Elemental y Productos Notables | Completado |
| `02_algebra_lineal.qmd` | 15A03 | Álgebra Lineal: Vectores y Matrices | Completado |
| `03_algebra_abstracta.qmd` | 20-01 | Álgebra Abstracta: Grupos | Completado |
| `04_teoria_de_categorias.qmd` | 18A05 | Teoría de Categorías | Completado |
| `05_teoria_anillos_cuerpos.qmd` | 13-01 | Teoría de Anillos y Cuerpos | Completado |
| `06_ecuaciones_y_desigualdades.qmd` | 12D05 | Ecuaciones, Inecuaciones y Sistemas Lineales | Pendiente |
| `07_polinomios_y_factorizacion.qmd` | 12D10 | Polinomios, Raíces y Teorema Fundamental del Álgebra | Pendiente |
| `08_espacios_vectoriales_bases.qmd` | 15A04 | Espacios Vectoriales, Bases y Dimensión | Pendiente |

---

### 4.3 Pilar 03: Análisis y Continuidad (`src/03_analisis_continuidad/`)

* **Estado Actual:** Cubre límites ($\varepsilon-\delta$), derivación, integración de Riemann, multivariable, ecuaciones diferenciales, sucesiones/series, análisis de Lebesgue y Hilbert.
* **Temas Prioritarios Fase 1 (Conceptos Básicos Faltantes):**

| ID / Archivo `.qmd` | Código MSC | Título del Módulo | Estado |
| :--- | :--- | :--- | :---: |
| `01_funciones_y_limites.qmd` | 26A03 | Funciones y Límites | Completado |
| `02_calculo_diferencial.qmd` | 26A24 | Cálculo Diferencial | Completado |
| `03_calculo_integral.qmd` | 26A42 | Cálculo Integral | Completado |
| `04_calculo_multivariable.qmd` | 26B05 | Cálculo Multivariable | Completado |
| `05_ecuaciones_diferenciales.qmd` | 34A01 | Ecuaciones Diferenciales Ordinarias | Completado |
| `06_analisis_avanzado.qmd` | 28A05 | Análisis Avanzado: Medida e Integración | Completado |
| `07_analisis_funcional.qmd` | 46-01 | Análisis Funcional | Completado |
| `08_sucesiones_y_series.qmd` | 40-01 | Sucesiones y Series | Completado |
| `09_funciones_transcendentes.qmd` | 26A09 | Funciones Exponenciales, Logarítmicas y Trigonométricas | Completado |
| `10_tecnicas_integracion.qmd` | 26A06 | Técnicas de Integración Práctica | Completado |
| `11_aplicaciones_calculo.qmd` | 26A07 | Aplicaciones del Cálculo: Optimización y Áreas | Completado |

---

### 4.4 Pilar 04: Espacio y Forma (`src/04_espacio_forma/`)

* **Estado Actual:** Geometría euclidiana bidimensional, trigonometría básica, geometría analítica cónica, topología, geometría diferencial y geometrías no euclidianas.
* **Temas Prioritarios Fase 1 (Conceptos Básicos Faltantes):**

| ID / Archivo `.qmd` | Código MSC | Título del Módulo | Estado |
| :--- | :--- | :--- | :---: |
| `01_geometria_euclidiana.qmd` | 51M04 | Geometría Euclidiana | Completado |
| `02_trigonometria.qmd` | 51M05 | Trigonometría Elemental | Completado |
| `03_geometria_analitica.qmd` | 51N20 | Geometría Analítica | Completado |
| `04_topologia.qmd` | 54-01 | Topología General | Completado |
| `05_geometria_diferencial.qmd` | 53A04 | Geometría Diferencial | Completado |
| `06_geometria_no_euclidiana.qmd` | 51M10 | Geometría No Euclidiana | Completado |
| `07_geometria_espacio_3d.qmd` | 51N15 | Geometría Analítica en $\mathbb{R}^3$ (Rectas, Planos y Vectores) | Completado |
| `08_identidades_ecuaciones_trigonometricas.qmd` | 51M05 | Identidades y Ecuaciones Trigonométricas Avanzadas | Completado |

---

### 4.5 Pilar 05: Discreción y Computación (`src/05_discrecion_computacion/`)

* **Estado Actual:** Combinatoria, teoría de grafos, divisibilidad y números primos, métodos numéricos (Newton-Raphson) y autómatas finitos.
* **Temas Prioritarios Fase 1 (Conceptos Básicos Faltantes):**

| ID / Archivo `.qmd` | Código MSC | Título del Módulo | Estado |
| :--- | :--- | :--- | :---: |
| `01_combinatoria.qmd` | 05A05 | Combinatoria Elemental | Completado |
| `02_teoria_de_grafos.qmd` | 05C05 | Teoría de Grafos | Completado |
| `03_teoria_de_numeros.qmd` | 11A05 | Teoría de Números | Completado |
| `04_metodos_numericos.qmd` | 65-01 | Métodos Numéricos | Completado |
| `05_teoria_automatas.qmd` | 68Q45 | Teoría de Autómatas | Completado |
| `06_relaciones_recurrencia.qmd` | 05A15 | Relaciones de Recurrencia y Funciones Generatrices | Completado |
| `07_analisis_complejidad.qmd` | 68Q25 | Análisis de Complejidad Algorítmica ($O, \Omega, \Theta$) | Completado |
| `08_aritmetica_modular_aplicada.qmd` | 11A07 | Aritmética Modular, Euclides Extendido y RSA | Completado |

---

### 4.6 Pilar 06: Estocástica e Incertidumbre (`src/06_estocastica_incertidumbre/`)

* **Estado Actual:** Estadística descriptiva, axiomas de probabilidad y Bayes, estadística inferencial, cadenas de Markov y teoría de la información.
* **Temas Prioritarios Fase 1 (Conceptos Básicos Faltantes):**

| ID / Archivo `.qmd` | Código MSC | Título del Módulo | Estado |
| :--- | :--- | :--- | :---: |
| `01_estadistica_descriptiva.qmd` | 62-01 | Estadística Descriptiva | Completado |
| `02_teoria_de_probabilidad.qmd` | 60A05 | Teoría de Probabilidad | Completado |
| `03_estadistica_inferencial.qmd` | 62F03 | Estadística Inferencial | Completado |
| `04_modelos_estocasticos.qmd` | 60J10 | Modelos Estocásticos | Completado |
| `05_teoria_informacion.qmd` | 94A17 | Teoría de la Información | Completado |
| `06_distribuciones_probabilidad.qmd` | 60E05 | Variables Aleatorias y Distribuciones Estándar | Completado |
| `07_regresion_y_correlacion.qmd` | 62J05 | Regresión Lineal Simple y Correlación de Pearson | Completado |
| `08_teoremas_limite.qmd` | 60F05 | Teorema del Límite Central y Leyes de Grandes Números | Completado |

---

## 5. Plan de Escalabilidad Fase 2 (Enriquecimiento Nivel 'Intro')

Con la Fase 1 completa y la estructura de carpetas de dificultad implementada (intro, intermedio, avanzado, abstracto), la **Fase 2** consiste en asegurar una base masiva de material introductorio. Se crearán nuevos módulos nivel `intro` para fortalecer el piso pedagógico en cada pilar.

### Nuevos Módulos Propuestos (Carpeta `intro/`)

| Pilar | Archivo `.qmd` Propuesto | Código MSC | Título del Módulo (Concepto Base) | Estado |
| :--- | :--- | :--- | :--- | :---: |
| **01 Fundamentos** | `08_falacias_logicas.qmd` | 03B05 | Falacias Lógicas y Errores de Argumentación | Completado |
| **02 Estructuras** | `05_sistemas_lineales_2x2.qmd` | 15A06 | Sistemas de Ecuaciones Lineales Básicos (2x2) | Completado |
| **03 Análisis** | `08_precalculo_asintotas.qmd` | 26A03 | Precálculo: Asíntotas y Comportamiento Final | Completado |
| **04 Espacio** | `05_poligonos_perimetros.qmd` | 51M04 | Geometría Plana: Polígonos, Perímetros y Áreas | Completado |
| **06 Estocástica** | `05_medidas_tendencia.qmd` | 62-01 | Medidas de Tendencia Central y Dispersión | Completado |

> **Recordatorio Fase 2:** Todos estos archivos deben colocarse dentro de la carpeta `intro/` de sus respectivos pilares. Asegurarse de que el `nivel: intro` está seteado en el JSON y que la sección del **Glosario de variables** se implementa como tabla estricta.

---

## 6. Protocolo de Registro y Actualización del Avance

Para mantener este registro actualizado durante el desarrollo de la hoja de ruta:

1. **Creación del Módulo:** Al generar los archivos `.qmd` y `.json`, cambiar el estado en la tabla correspondiente de este documento de `Pendiente` a `En Desarrollo`.
2. **Generación del Gráfico Typst:** Crear el script de gráfico en `scripts/grafics/typst_src/<pilar>/<nombre>.typ` y compilarlo a `.svg`.
3. **Verificación de Integridad:** Ejecutar `python scripts/build.py --verbose`.
4. **Cierre de Tarea:** Una vez validado sin errores por Quarto y el linter, actualizar el estado a `Completado` y recalcular el porcentaje global del pilar en la **Sección 3**.
