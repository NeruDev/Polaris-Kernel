# MSC2020-Mathematics Subject Classification System

## Associate Editors of Mathematical Reviews and zbMATH

Este directorio contiene una división de [MSC_2020.tex](MSC_2020.tex) en varios archivos `.tex` por rangos de secciones `NN-XX`.
Los archivos se generaron copiando segmentos **sin modificar** del original (verificación byte-a-byte).

## Secciones principales

* **00** General and overarching topics; collections
* **01** History and biography
* **03** Mathematical logic and foundations
* **05** Combinatorics
* **06** Order, lattices, ordered algebraic structures
* **08** General algebraic systems
* **11** Number theory
* **12** Field theory and polynomials
* **13** Commutative algebra
* **14** Algebraic geometry
* **15** Linear and multilinear algebra; matrix theory
* **16** Associative rings and algebras
* **17** Nonassociative rings and algebras
* **18** Category theory; homological algebra
* **19** K-theory
* **20** Group theory and generalizations
* **22** Topological groups, Lie groups
* **26** Real functions
* **28** Measure and integration
* **30** Functions of a complex variable
* **31** Potential theory
* **32** Several complex variables and analytic spaces
* **33** Special functions
* **34** Ordinary differential equations
* **35** Partial differential equations
* **37** Dynamical systems and ergodic theory
* **39** Difference and functional equations
* **40** Sequences, series, summability
* **41** Approximations and expansions
* **42** Harmonic analysis on Euclidean spaces
* **43** Abstract harmonic analysis
* **44** Integral transforms, operational calculus
* **45** Integral equations
* **46** Functional analysis
* **47** Operator theory
* **49** Calculus of variations and optimal control; optimization
* **51** Geometry
* **52** Convex and discrete geometry
* **53** Differential geometry
* **54** General topology
* **55** Algebraic topology
* **57** Manifolds and cell complexes
* **58** Global analysis, analysis on manifolds
* **60** Probability theory and stochastic processes
* **62** Statistics
* **65** Numerical analysis
* **68** Computer science
* **70** Mechanics of particles and systems
* **74** Mechanics of deformable solids
* **76** Fluid mechanics
* **78** Optics, electromagnetic theory
* **80** Classical thermodynamics, heat transfer
* **81** Quantum theory
* **82** Statistical mechanics, structure of matter
* **83** Relativity and gravitational theory
* **85** Astronomy and astrophysics
* **86** Geophysics
* **90** Operations research, mathematical programming
* **91** Game theory, economics, social and behavioral sciences
* **92** Biology and other natural sciences
* **93** Systems theory; control
* **94** Information and communication, circuits
* **97** Mathematics education

## Archivos del Repositorio (Tex y JSON)

### Archivos LaTeX (.tex)
- [MSC_2020.tex](MSC_2020.tex): Versión completa del sistema de clasificación MSC 2020
- [MSC_frontmatter.tex](MSC_frontmatter.tex): preámbulo + introducción (antes de `00-XX`)
- [MSC_00_a_08.tex](MSC_00_a_08.tex): secciones 00, 01, 03, 05, 06, 08
- [MSC_11_a_19.tex](MSC_11_a_19.tex): secciones 11–19
- [MSC_20_a_28.tex](MSC_20_a_28.tex): secciones 20, 22, 26, 28
- [MSC_30_a_39.tex](MSC_30_a_39.tex): secciones 30, 31, 32, 33, 34, 35, 37, 39
- [MSC_40_a_49.tex](MSC_40_a_49.tex): secciones 40–47, 49
- [MSC_51_a_58.tex](MSC_51_a_58.tex): secciones 51–55, 57–58
- [MSC_60_a_68.tex](MSC_60_a_68.tex): secciones 60, 62, 65, 68
- [MSC_70_a_78.tex](MSC_70_a_78.tex): secciones 70, 74, 76, 78
- [MSC_80_a_86.tex](MSC_80_a_86.tex): secciones 80–83, 85–86
- [MSC_90_a_97.tex](MSC_90_a_97.tex): secciones 90–94, 97

### Archivos JSON (.json)
- [MSC_00_a_08.json](MSC_00_a_08.json): Metadatos para secciones 00 a 08
- [MSC_11_a_19.json](MSC_11_a_19.json): Metadatos para secciones 11 a 19
- [MSC_20_a_28.json](MSC_20_a_28.json): Metadatos para secciones 20 a 28
- [MSC_30_a_39.json](MSC_30_a_39.json): Metadatos para secciones 30 a 39
- [MSC_40_a_49.json](MSC_40_a_49.json): Metadatos para secciones 40 a 49
- [MSC_51_a_58.json](MSC_51_a_58.json): Metadatos para secciones 51 a 58
- [MSC_60_a_68.json](MSC_60_a_68.json): Metadatos para secciones 60 a 68
- [MSC_70_a_78.json](MSC_70_a_78.json): Metadatos para secciones 70 a 78
- [MSC_80_a_86.json](MSC_80_a_86.json): Metadatos para secciones 80 a 86
- [MSC_90_a_97.json](MSC_90_a_97.json): Metadatos para secciones 90 a 97
- [MSC_index.json](MSC_index.json): Índice general del sistema MSC
- [MSC_index_pillars_overlay.json](MSC_index_pillars_overlay.json): Capa de pilares para el índice
- [msc_taxonomy.all.json](msc_taxonomy.all.json): Taxonomía completa en formato JSON
- [msc_taxonomy.schema.json](msc_taxonomy.schema.json): Esquema de validación para la taxonomía JSON

---

# Sistema de scripts y metadatos (MSC2020 + MathKernel)

Este sistema permite clasificar y enriquecer notas Markdown usando la arquitectura de 6 pilares y la indexación MSC2020.

## Objetivo
1. Mantener la estructura simple de carpetas (`src/`).
2. Agregar una capa virtual de metadatos para clasificación y navegación semántica.

## Fuentes de datos
- **Índice rápido:** [MSC_index.json](MSC_index.json) (mapea códigos top-level a archivos JSON específicos).
- **Jerarquía detallada:** [MSC_00_a_08.json](MSC_00_a_08.json) y archivos hermanos.
- **Overlay de pilares:** [MSC_index_pillars_overlay.json](MSC_index_pillars_overlay.json) (mapea MSC a los 6 pilares estructurales).
- **Referencia semántica:** [MSC_2020.tex](MSC_2020.tex) (reglas de referencias cruzadas).

## Pipeline de clasificación
1. **Nivel 1 (Rápido):** Match contra el overlay para determinar el pilar primario y la sección MSC.
2. **Nivel 2 (Preciso):** Búsqueda en los archivos JSON específicos para refinar el `msc_code` y derivar `tags`.

## Scripts (Ubicación)
Los scripts se organizan en la carpeta raíz `scripts/`:
- `scripts/msc/00_generate_overlay.py`: Genera el skeleton del overlay.
- `scripts/msc/01_validate_overlay.py`: Valida el overlay.
- `scripts/msc/10_classify_note.py`: Clasifica una nota individual.
- `scripts/msc/11_classify_batch.py`: Clasifica un lote de notas.

La lógica reutilizable reside en `utils/` (MathKernel helpers).
