# Arquitectura del Repositorio de Matemáticas: Von Neumann MathKernel

Este repositorio no está diseñado como un curso tradicional ni como una colección lineal de apuntes. Su objetivo es más ambicioso: construir un sistema estructurado de conocimiento matemático que pueda escalar desde aritmética básica hasta áreas avanzadas como topología, análisis funcional o teoría de categorías, sin perder coherencia ni navegabilidad.

La organización clásica por “materias escolares” (álgebra, cálculo, geometría, etc.) resulta insuficiente a medida que el contenido crece. Ese enfoque asume un recorrido lineal y compartimentado que rara vez refleja cómo funciona realmente la matemática. En la práctica, los conceptos no viven en silos: se interconectan, se reutilizan y evolucionan formando una red densa de dependencias y relaciones.

Por esta razón, este repositorio adopta un enfoque estructural en lugar de curricular. El contenido se organiza en torno a **pilares conceptuales** que agrupan áreas según la naturaleza de los objetos que estudian (estructuras, cambio, espacio, discreción, incertidumbre, fundamentos). Esta clasificación se inspira parcialmente en sistemas formales como el estándar de clasificación matemática (MSC), pero se simplifica para mantener claridad y usabilidad.

Sin embargo, la estructura de carpetas se mantiene deliberadamente plana y limitada. La complejidad no se delega en la jerarquía de directorios, sino en los **metadatos**. Cada documento es una unidad atómica de conocimiento que incluye información estructurada sobre:
- prerrequisitos conceptuales  
- relaciones con otros temas  
- clasificación temática (tags y MSC)  
- nivel de abstracción y complejidad  

Esto permite reconstruir múltiples formas de navegación sin imponer una única ruta rígida. En lugar de “rutas de aprendizaje” lineales, el sistema permite generar **rutas lógicas semánticas**, es decir, recorridos dinámicos basados en dependencias reales entre conceptos.

El repositorio está diseñado desde el inicio para ser procesado por herramientas automatizadas. Scripts en Python se encargan de:
- validar la consistencia de metadatos  
- construir grafos de conocimiento  
- generar índices por pilar  
- alimentar la navegación de la página web  

De esta forma, se separan claramente dos responsabilidades:
- **estructura simple (carpetas)** → fácil de mantener  
- **estructura compleja (metadatos + scripts)** → poderosa y escalable  

El resultado es un sistema que no solo organiza contenido, sino que permite explorarlo como una red de conocimiento interconectado, adaptable tanto para humanos como para sistemas automatizados (búsqueda avanzada, RAG, visualización de grafos, etc.).

En resumen, este repositorio no pretende enseñar matemáticas como una secuencia fija, sino representarlas como lo que realmente son: una arquitectura de ideas profundamente conectadas.

La arquitectura propuesta está diseñada para ser compatible con:
- humanos (navegación simple, convenciones estables, lectura directa)
- sistemas de IA (segmentación consistente, metadatos explícitos, recuperación tipo RAG)

La organización del contenido sigue un enfoque inspirado en el grupo de matemáticos **Nicolas Bourbaki**: prioriza **estructuras** y relaciones entre conceptos por encima de una secuencia lineal por “materias”.

Para indexación y nomenclatura temática se utiliza el estándar **Mathematics Subject Classification (MSC)** (versión **MSC 2020**) publicado por la **American Mathematical Society (AMS)**. El MSC se usa para clasificar y buscar; no dicta la estructura de carpetas.

---

## 0) Contexto histórico (Nicolas Bourbaki)

**Nicolas Bourbaki** es el seudónimo colectivo de un grupo de matemáticos (principalmente franceses) fundado en la década de 1930. Su proyecto influyó en la manera moderna de presentar matemáticas: axiomas claros, definiciones precisas y desarrollo por **estructuras** (algebraicas, topológicas, analíticas) con un lenguaje común.

Este repositorio toma esa idea como guía editorial: mantener una estructura de archivos simple y estable, y mover la complejidad a (1) relaciones entre documentos y (2) metadatos.

---

## Parte I — Arquitectura para humanos (didáctica basada en pilares)

Esta parte define la estructura base del repositorio: pilares, división de carpetas y reglas de organización pensadas para lectura y edición humana. Las convenciones de metadatos y automatización se agrupan en la Parte II.

---

## 0.1) Estructura Funcional del Repositorio (Root)

Para mantener una separación clara entre el conocimiento, las herramientas de procesamiento y la visualización, el repositorio se organiza en los siguientes directorios raíz:

- **`src/`**: Carpeta principal de contenido. Contiene los 6 pilares estructurales en formato Markdown. Es la única carpeta donde se edita el conocimiento matemático.
- **`scripts/`**: Contiene los puntos de entrada (entry points) de la lógica del sistema. Aquí residen los scripts ejecutables para validación, generación de índices y procesamiento.
- **`utils/`**: Funciones modulares y herramientas compartidas de Python. Contiene lógica reutilizable para el manejo de archivos, parsing de metadatos y utilidades comunes.
- **`tests/`**: Pruebas automáticas (unitarias e integración). Garantiza que los scripts y utilidades funcionen correctamente antes de cada despliegue.
- **`docs/`**: Documentación técnica del repositorio. Guías para desarrolladores, manuales de uso de scripts y especificaciones de la arquitectura (separado del contenido matemático).
- **`site_src/`**: Plantillas, estilos (CSS) y archivos de configuración para la generación del sitio web (GitHub Pages).
- **`site/`**: Carpeta de salida generada automáticamente. Contiene los archivos finales (HTML/JS) listos para ser servidos.
- **`metadata/`**: Archivos de soporte taxonómico (como el MSC 2020) y esquemas de validación.

---

## 1) Regla de Oro: 3 Niveles Exactos

Para mantener un sistema escalable y fácil de navegar por humanos e IA, el repositorio se define con **tres niveles**:

1. **Nivel 1 (directorios raíz):** 6 pilares estructurales.
2. **Nivel 2 (documentos atómicos):** archivos Markdown (`.md`) dentro de cada pilar.
3. **Nivel 3 (alcance interno):** secciones `##` dentro de cada documento.

No se crean subcarpetas dentro de un pilar. La granularidad se controla con:
- el tamaño de los documentos (atómicos)
- el orden de lectura (prefijos `01_`, `02_`, …)
- los metadatos (prerrequisitos, tags, MSC)

---

## 2) Convenciones de Nombres

### 2.1 Directorios (Nivel 1)

- Formato: `NN_nombre_con_guion_bajo`
- Ejemplo: `03_analisis_continuidad`

### 2.2 Documentos (Nivel 2)

- Formato: `NN_nombre_del_documento.md`
- Los prefijos numéricos indican un **orden sugerido** (no obligatorio) y ayudan a “capas de abstracción”.

### 2.3 Secciones (Nivel 3)

- Las secciones `##` representan subtemas.
- Regla práctica: si una sección crece demasiado, se convierte en un documento atómico nuevo.

---

## 3) Los 6 Pilares (Nivel 1)

Los pilares se definen por la naturaleza de lo que estudian:

1. **01_fundamentos_logica** — lenguaje, reglas, demostración, conjuntos.
2. **02_estructuras_algebraicas** — operaciones y estructuras (lineal y abstracta).
3. **03_analisis_continuidad** — límite, infinito, cambio, aproximación.
4. **04_espacio_forma** — geometría, espacio, cercanía, topología.
5. **05_discrecion_computacion** — finito, conteo, grafos, algoritmos, métodos numéricos.
6. **06_estocastica_incertidumbre** — azar, estadística, modelos estocásticos.

---

## 4) Estructura Propuesta (Nivel 1 → Nivel 2 → Nivel 3)

La siguiente estructura traduce el esquema de tus notas a:
- carpetas (pilares)
- documentos atómicos (archivos `.md`)
- secciones internas `##`

> Nota: Los títulos de sección se muestran en español “legible”; internamente puedes conservar el identificador `snake_case` en los metadatos si lo deseas.

```text
01_fundamentos_logica/
	01_sistemas_numericos.md
	02_logica_matematica.md
	03_teoria_conjuntos.md
	04_metodos_demostracion.md

02_estructuras_algebraicas/
	01_algebra_elemental.md
	02_algebra_lineal.md
	03_algebra_abstracta.md
	04_teoria_de_categorias.md        (sugerido)

03_analisis_continuidad/
	01_funciones_y_limites.md
	02_calculo_diferencial.md
	03_calculo_integral.md
	04_calculo_multivariable.md
	05_ecuaciones_diferenciales.md
	06_analisis_avanzado.md
	07_analisis_funcional.md          (sugerido)

04_espacio_forma/
	01_geometria_euclidiana.md
	02_trigonometria.md
	03_geometria_analitica.md
	04_topologia.md
	05_geometria_diferencial.md       (sugerido)

05_discrecion_computacion/
	01_combinatoria.md
	02_teoria_de_grafos.md
	03_teoria_de_numeros.md
	04_metodos_numericos.md

06_estocastica_incertidumbre/
	01_estadistica_descriptiva.md
	02_teoria_de_probabilidad.md
	03_estadistica_inferencial.md
	04_modelos_estocasticos.md
```

### 4.1 Detalle por pilar: documentos y secciones

#### 01_fundamentos_logica

**01_sistemas_numericos.md**
- `## Naturales y enteros`
- `## Racionales e irracionales`
- `## Números complejos`

**02_logica_matematica.md**
- `## Lógica proposicional`
- `## Cuantificadores y predicados`
- `## Lógica de primer orden`

**03_teoria_conjuntos.md**
- `## Axiomas básicos`
- `## Operaciones entre conjuntos`
- `## Cardinalidad e infinito`

**04_metodos_demostracion.md**
- `## Inducción matemática`
- `## Reducción al absurdo`
- `## Demostración directa y contraposición`

#### 02_estructuras_algebraicas

**01_algebra_elemental.md**
- `## Expresiones y polinomios`
- `## Ecuaciones e inecuaciones`
- `## Fracciones parciales`

**02_algebra_lineal.md**
- `## Sistemas de ecuaciones`
- `## Matrices y determinantes`
- `## Espacios vectoriales`
- `## Transformaciones lineales`

**03_algebra_abstracta.md**
- `## Teoría de grupos`
- `## Teoría de anillos`
- `## Campos y extensiones de Galois`

**04_teoria_de_categorias.md (sugerido)**
- `## Objetos, morfismos y composición`
- `## Functores y transformaciones naturales`
- `## Productos, coproductos y límites`
- `## Equivalencias y adjunciones (intro)`

#### 03_analisis_continuidad

**01_funciones_y_limites.md**
- `## Tipos de funciones y composición`
- `## Sucesiones y series`
- `## Límites y continuidad`

**02_calculo_diferencial.md**
- `## Concepto de derivada`
- `## Reglas de derivación`
- `## Optimización y análisis de curvas`

**03_calculo_integral.md**
- `## Integral indefinida y definida`
- `## Teorema fundamental del cálculo`
- `## Técnicas de integración`

**04_calculo_multivariable.md**
- `## Derivadas parciales y direccionales`
- `## Integrales múltiples`
- `## Teoremas vectoriales (Green, Stokes, Gauss)`

**05_ecuaciones_diferenciales.md**
- `## EDO de primer orden`
- `## EDO de orden superior`
- `## Transformada de Laplace`

**06_analisis_avanzado.md**
- `## Introducción al análisis real`
- `## Funciones de variable compleja`

**07_analisis_funcional.md (sugerido)**
- `## Espacios normados y métricas inducidas`
- `## Espacios de Banach y teoremas básicos`
- `## Espacios de Hilbert y proyecciones`
- `## Operadores lineales (intro)`

#### 04_espacio_forma

**01_geometria_euclidiana.md**
- `## Axiomas y postulados`
- `## Semejanza y congruencia`
- `## Geometría del espacio 3D`

**02_trigonometria.md**
- `## Razones y círculo unitario`
- `## Identidades trigonométricas`
- `## Ley de senos y cosenos`

**03_geometria_analitica.md**
- `## Sistema de coordenadas y vectores`
- `## La recta y el plano`
- `## Cónicas y superficies cuádricas`

**04_topologia.md**
- `## Espacios métricos`
- `## Continuidad topológica`
- `## Compacidad y conexión`

**05_geometria_diferencial.md (sugerido)**
- `## Curvas parametrizadas`
- `## Superficies y formas fundamentales (intro)`
- `## Variedades (introducción)`

#### 05_discrecion_computacion

**01_combinatoria.md**
- `## Principios fundamentales de conteo`
- `## Permutaciones y combinaciones`
- `## Teorema del binomio`

**02_teoria_de_grafos.md**
- `## Definiciones y tipos de grafos`
- `## Árboles y algoritmos de búsqueda`
- `## Grafos planos y coloración`

**03_teoria_de_numeros.md**
- `## Divisibilidad y números primos`
- `## Aritmética modular y congruencias`
- `## Ecuaciones diofánticas`

**04_metodos_numericos.md**
- `## Aproximación y análisis de errores`
- `## Resolución de sistemas no lineales`
- `## Integración y derivación numérica`

#### 06_estocastica_incertidumbre

**01_estadistica_descriptiva.md**
- `## Medidas de tendencia central`
- `## Medidas de dispersión`
- `## Distribuciones de frecuencia`

**02_teoria_de_probabilidad.md**
- `## Axiomas de probabilidad`
- `## Probabilidad condicional y teorema de Bayes`
- `## Variables aleatorias discretas y continuas`

**03_estadistica_inferencial.md**
- `## Distribuciones muestrales`
- `## Estimación por intervalos`
- `## Pruebas de hipótesis`

**04_modelos_estocasticos.md**
- `## Cadenas de Markov`
- `## Procesos de Poisson`

---

## 6) Regla de Escalabilidad (Bourbaki)

Criterio editorial (humano): decidir en qué pilar “vive” un tema nuevo.

### 6.1 (Bourbaki) ¿Dónde cae un tema nuevo?

Hazte una sola pregunta:

- ¿Estudia **operaciones y propiedades algebraicas**? → `02_estructuras_algebraicas`
- ¿Estudia **límite, aproximación, infinito, cambio**? → `03_analisis_continuidad`
- ¿Estudia **espacio, forma, cercanía, continuidad topológica**? → `04_espacio_forma`
- ¿Estudia **conteo finito, grafos, algoritmos, métodos computacionales**? → `05_discrecion_computacion`
- ¿Estudia **azar, incertidumbre, inferencia**? → `06_estocastica_incertidumbre`
- ¿Define **lenguaje, demostración, conjuntos, fundamentos**? → `01_fundamentos_logica`

---

## Parte II — Arquitectura para IA (metadatos + automatización)

Esta parte define las convenciones que permiten indexación (MSC), validación automática, segmentación estable y generación de navegación.

---

## 7) Observaciones y Mejoras Recomendadas

### 7.1 Observaciones (fortalezas y riesgos)

- **Fortaleza:** los pilares preservan “localidad semántica”: temas relacionados viven juntos, y los documentos se ordenan por madurez.
- **Fortaleza:** los metadatos desacoplan el crecimiento del contenido de la complejidad de carpetas.
- **Riesgo:** si los `id` no son estables o consistentes, se rompe el grafo de prerrequisitos.
- **Riesgo:** sin una convención de “tamaño objetivo” por documento, algunos `.md` crecerán demasiado.

### 7.2 Mejoras implementables (sin cambiar la arquitectura)

1. **Plantilla única de documento**
	 - Crear un `template.md` (o `TEMPLATE.md`) con el frontmatter YAML mínimo + secciones sugeridas (Definiciones, Teoremas, Ejemplos, Ejercicios, Errores comunes, Referencias).

2. **Índice automático / vistas**
	 - Un script (Python u otro) podría leer frontmatter y generar:
		 - un `INDEX.md` global por pilar
		 - una “ruta” por prerrequisitos (grafo)
		 - listas por `tags` o por `msc_code`

3. **Convención editorial por niveles**
	 - Usar `nivel: intro|intermedio|avanzado|abstracto` de forma consistente para filtrar rutas.

4. **Estandarizar prerrequisitos**
	 - Recomendación: `prerrequisitos` siempre referencian `id` (no rutas) y se mantiene un glosario de IDs.

5. **Integración con IA/RAG**
	 - Mantener fragmentación estable: encabezados `##` claros y consistentes, para facilitar chunking.
	 - Añadir en cada documento una sección `## Prerrequisitos (mapa)` generada o mantenida manualmente.

---

## 8) Checklist para Agregar un Tema Nuevo

1. Elegir pilar canónico (regla de escalabilidad).
2. Crear documento atómico nuevo con prefijo numérico.
3. Escribir frontmatter YAML (`id`, `title`, `pilar`; opcionalmente `msc_code`, `prerrequisitos`, `tags`).
4. Definir alcance con secciones `##`.
5. Si es híbrido, agregar `pilares` secundarios + `prerrequisitos`.

---

## 9) Reglas de Robustez para Metadatos y Escalabilidad

Para garantizar que el sistema pueda crecer indefinidamente sin degradarse, se establecen las siguientes reglas obligatorias.

---

### 9.0 Metadatos (YAML) para Indexación y Navegación (IA/RAG)

La idea es que el sistema de archivos permanezca simple (6 pilares, sin subcarpetas), mientras que los **metadatos** permitan:

- reconstruir rutas de aprendizaje (prerrequisitos)
- ubicar temas híbridos (pertenencias múltiples)
- indexar por MSC 2020 (búsqueda universal)
- generar “vistas” (por tags, por nivel, por prerequisitos)

#### 9.0.1 Frontmatter mínimo recomendado

Cada documento atómico debe iniciar con un frontmatter:

```yaml
---
id: calculo_integral
title: "Cálculo integral"
pilar: "03_analisis_continuidad"
msc_code: "26-XX"   # opcional; MSC 2020 aproximado / inicial
tags: [calculo, integrales]
nivel: intro         # intro | intermedio | avanzado | abstracto (opcional)
prerrequisitos: [limites_definicion, derivada_basica]
updated: "2026-04-15"
status: "draft"     # draft | stable | wip (opcional)
---
```

#### 9.0.2 Campos y significado

- `id` (requerido): identificador estable en `snake_case`. No debe depender del nombre del archivo, del orden (`NN_`) ni de la ubicación en carpetas.
- `title` (requerido): título legible.
- `pilar` (requerido): **un** pilar canónico (uno de los 6).
- `msc_code` (opcional): código MSC 2020 (puede ser general `xx-XX` al inicio).
- `prerrequisitos` (opcional): lista de `id` de otros documentos.
- `tags` (opcional): lista corta de palabras clave.
- `nivel` (opcional): `intro` | `intermedio` | `avanzado` | `abstracto`.
- `updated`, `status` (opcional): control editorial.

#### 9.0.3 Temas “híbridos” (sin romper los 6 pilares)

Cuando un tema use varios dominios (ej. optimización), se asigna:

- un `pilar` canónico (donde “vive” el documento)
- una lista `pilares` secundaria (para pertenencias cruzadas)

Ejemplo:

```yaml
---
id: optimizacion_descenso_gradiente
title: "Optimización por descenso de gradiente"
pilar: "05_discrecion_computacion"
pilares: ["03_analisis_continuidad", "02_estructuras_algebraicas"]
prerrequisitos: [calculo_multivariable, algebra_lineal]
tags: [optimizacion, gradiente]
msc_code: "49-XX"
---
```

Regla práctica: si un tema híbrido se vuelve enorme, no se crea una carpeta nueva; se crean **documentos atómicos adicionales** y se conectan por metadatos.

#### 9.0.4 (MSC 2020) ¿Cómo se indexa para búsqueda universal?

El MSC no manda en la estructura de carpetas; manda en la **indexación**.

- Al inicio, usa códigos generales (`18-XX`, `26-XX`, etc.)
- Con el tiempo, refina a códigos más específicos cuando el contenido lo amerite

---

### 9.1 Política de Identificadores Únicos (UID) de Alta Robustez

Para garantizar que el repositorio crezca hasta miles de documentos sin colisiones y sin romper las referencias de prerrequisitos, se establece el siguiente estándar para el campo `id`:

#### 9.1.1 Regla del Espacio de Nombres (MSC Namespace)
El `id` NO debe ser puramente semántico. Debe incluir un prefijo basado en la clasificación numérica del **MSC 2020** que se encuentra en `metadata/`.

**Formato:** `msc[codigo]_[nombre_en_snake_case]`

- **Nivel General (Sección):** `msc26_calculo_integral`
- **Nivel Específico (Subsección):** `msc26A_integral_riemann`
- **Nivel Atómico (Ítem):** `msc26A42_integrales_singulares`

#### 9.1.2 Ventajas de este sistema:
1. **Eliminación de homónimos:** Evita colisiones entre términos que significan cosas distintas en áreas diferentes (ej: `msc62_distribucion_normal` vs `msc53_vector_normal`).
2. **Localidad Semántica:** Los IDs de temas relacionados quedan agrupados alfabéticamente en los metadatos.
3. **Independencia de Ruta:** Si mueves un archivo de pilar (ej. de "Análisis" a "Fundamentos"), el ID se mantiene idéntico porque su "apellido" matemático (MSC) no cambia.

#### 9.1.3 Regla de Oro: Inmutabilidad del ID
- **El ID es sagrado:** Una vez que un documento es publicado y referenciado como `prerrequisito` por otro, su `id` **nunca debe cambiar**.
- Si el título del tema cambia (ej. de "Integral" a "Teoría de la Integración"), el `id` original se mantiene para no romper el grafo de conocimiento.
- Si un tema se divide en dos, el `id` original debe permanecer para el concepto más general o introductorio.

#### 9.1.4 Restricciones Técnicas
- **Caracteres:** Solo minúsculas (a-z), números (0-9) y guiones bajos (_).
- **Prohibido:** Espacios, acentos, mayúsculas o caracteres especiales.
- **Longitud:** Máximo 50 caracteres (para mantener legibilidad en scripts de grafos).

---

### 9.2 Validación Automática de Integridad

El sistema debe contar con un script en `scripts/msc/` que realice las siguientes comprobaciones en cada "commit":

1. **Unicidad Global:** No pueden existir dos archivos con el mismo `id` en todo el repositorio.
2. **Existencia de Referencias:** Todos los IDs listados en `prerrequisitos` deben existir como un `id` válido en otro archivo.
3. **Consistencia MSC:** El prefijo del `id` debe ser coherente con el campo `msc_code` del YAML.

---

### 9.2 Prerrequisitos (`prerrequisitos`) validados

- Siempre referencian `id`, nunca rutas.

```yaml
prerrequisitos: [limites_definicion, derivada_basica]
```

#### Reglas obligatorias

- Todos los `id` referenciados deben existir.
- No se permiten ciclos (A → B → A).
- Debe existir un script de validación automática.

#### Recomendación

- Validar el grafo completo en cada build (CI).

---

### 9.3 Control de `tags`

- Lista controlada o normalizada.

#### Problema a evitar

```
calculo, cálculo, calc, integrales, integral
```

#### Solución

- Definir un vocabulario base (`tags.json`).
- O normalización automática en scripts.

#### Reglas

- minúsculas
- sin acentos
- evitar sinónimos redundantes

---

### 9.4 Campo `nivel` estandarizado

Valores permitidos:

```yaml
nivel: intro  # intro | intermedio | avanzado | abstracto
```

#### Regla

- No inventar nuevos niveles arbitrarios.
- Usar consistentemente para filtrado y rutas semánticas.

---

### 9.5 Campos recomendados adicionales

```yaml
complexity: baja  # baja | media | alta
dependencias_conceptuales: []
```

---

## 10) Reglas de Segmentación de Contenido (Markdown)

El control de tamaño evita tanto documentos inmanejables como fragmentación inútil.

---

### 10.1 Longitud por línea

- Máximo: 80–100 caracteres por línea.
- Objetivo: legibilidad y compatibilidad con diff.

---

### 10.2 Tamaño total del documento

#### Reglas base

- Mínimo: 300 palabras.
- Óptimo: 500–1500 palabras.
- Máximo recomendado: 2000 palabras.

#### Excepciones

- Temas complejos pueden exceder 2000 palabras SOLO si:
  - están claramente estructurados
  - no se pueden dividir sin romper coherencia

---

### 10.3 Segmentación por párrafos

- Cada párrafo: 3–6 líneas promedio.
- Evitar:
  - bloques de texto largos
  - listas excesivas sin contexto

---

### 10.4 Regla de división

Dividir documento cuando:

- una sección `##` supera ~300–500 palabras
- el documento cubre más de un concepto central

---

### 10.5 Regla anti-microarchivo

NO crear archivos si:

- contienen <300 palabras
- no representan un concepto independiente

#### Regla

> Si no puede vivir solo semánticamente, no merece un archivo.

---

## 11) Generación de Índices y Navegación

Dado que no hay subcarpetas profundas, la navegación debe generarse automáticamente.

---

### 11.1 Índice por pilar

Cada pilar debe tener un archivo:

INDEX.md

Generado automáticamente con:

- lista de documentos
- orden sugerido (`NN_`)
- título (`title`)
- nivel (`nivel`)

---

### 11.2 Sidebar (navegación web)

La página web debe incluir:

- navegación por pilares
- lista de documentos por pilar
- filtrado por:
  - nivel
  - tags

#### Implementación

- generada vía script (Python)
- basada en frontmatter YAML

---

### 11.3 Ruta lógica semántica

Se reemplaza la “ruta de aprendizaje” tradicional por una estructura basada en relaciones conceptuales.

#### Definición

> Unión de conceptos según dependencia, no según orden lineal.

Se construye usando:

- `prerrequisitos`
- `tags`
- `pilares` secundarios

#### Resultado

- grafo navegable de conceptos
- múltiples caminos válidos (no lineales)

---

### 11.4 Generación automática

Un script debe ser capaz de generar:

- índices (`INDEX.md`)
- sidebar (JSON/YAML para frontend)
- grafo de dependencias
- rutas semánticas

---

## 12) Regla Fundamental de Escalabilidad

> La complejidad vive en metadatos y scripts, no en la estructura de carpetas.

Si esta regla se rompe:

- el sistema deja de escalar
- la navegación se degrada
- el mantenimiento se vuelve costoso

Si se respeta:

- el repositorio puede crecer indefinidamente
- la estructura permanece simple
- la recuperación de información mejora con el tiempo

