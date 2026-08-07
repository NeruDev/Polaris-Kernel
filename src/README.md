---
id: "msc00_readme"
title: "README"
pilar: "01_fundamentos_logica"
msc_code: "00-00"
status: "draft"
---
# Contenido Teórico y Pilares de Conocimiento (`src/`)

Este directorio constituye el núcleo teórico y pedagógico de Polaris Kernel.
Alberga los módulos conceptuales redactados en Quarto Markdown (`.qmd`) y Markdown (`.md`), estructurados rigurosamente bajo la taxonomía de los 6 Pilares de Bourbaki.

## Propósito y Funciones en el Repositorio

El directorio `src/` almacena la prosa explicativa, demostraciones matemáticas y recursos gráficos del repositorio.
Sirve como la fuente primaria de contenido que el orquestador `scripts/build.py` compila mediante Quarto para generar la plataforma estática final.
Además, aloja los archivos SVG vectoriales generados mediante la integración con Typst.

---

## Plan Maestro de Volcado e Integración DLMF $\rightarrow$ `src/`

Para incorporar la *Digital Library of Mathematical Functions* (NIST DLMF) con el máximo rigor pedagógico y matemático, se ha diseñado un plan de volcado estructurado a partir de los índices [`metadata/DLMF_data/DLMF_indice_simplificado.json`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/metadata/DLMF_data/DLMF_indice_simplificado.json) y [`metadata/DLMF_data/DLMF_indice_completo.json`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/metadata/DLMF_data/DLMF_indice_completo.json).

### Estrategia de Clasificación y Rigor Matemático

Cada capítulo de la DLMF se subdivide internamente en 5 bloques semánticos estandarizados:
1. **Definiciones y Construcción Axiomática:** Ecuaciones diferenciales generadoras, representaciones en serie de potencias o integrales de contorno.
2. **Identidades y Relaciones de Recurrencia:** Fórmulas de tres términos, relaciones Wronskianas y derivadas de orden arbitrario.
3. **Comportamiento Asintótico y Polos:** Expansiones para grandes argumentos u órdenes, regiones de convergencia y estructuras de ramificación.
4. **Clasificación de Fórmulas y Simetrías:** Propiedades de paridad, transformaciones de grupo y ceros de las funciones.
5. **Representación Gráfica e Interactividad:** Diagramas vectoriales en Typst bajo la Regla de la Trinidad e hipervínculos hacia el dataset DuckDB.

---

## Distribución de los 36 Capítulos DLMF por Pilar de Bourbaki

### 🏛️ Pilar 01: Fundamentos y Lógica (`src/01_fundamentos_logica/`)

Este pilar recibe los métodos analíticos algebraicos básicos que sustentan la construcción formal de funciones.

* [`src/01_fundamentos_logica/avanzado/09_metodos_algebraicos_analiticos.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/01_fundamentos_logica/avanzado/09_metodos_algebraicos_analiticos.qmd):
  - **Origen DLMF:** Capítulo 1 (*Algebraic and Analytic Methods*).
  - **Código MSC2020:** `00A05`, `12Dxx`, `26Axx`.
  - **Explicación pedagógica:** Introduce las desigualdades fundamentales, sistemas polinomiales, teoremas de continuidad analítica y expansiones en series.
  - **Rigor y Fórmulas:** Incorpora la fórmula del resto de Taylor, desigualdades de Cauchy-Schwarz y el principio de prolongación analítica.
  $$\sum_{k=0}^{n} a_k x^k = 0, \quad |f(z)| \le M$$

---

### 🏛️ Pilar 02: Estructuras Algebraicas (`src/02_estructuras_algebraicas/`)

Alberga los polinomios con propiedades algebraicas de grupos, simetrías de momento angular y funciones sobre matrices.

* [`src/02_estructuras_algebraicas/intermedio/09_polinomios_bernoulli_euler.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/02_estructuras_algebraicas/intermedio/09_polinomios_bernoulli_euler.qmd):
  - **Origen DLMF:** Capítulo 24 (*Bernoulli and Euler Polynomials*).
  - **Código MSC2020:** `11B68`, `33E20`.
  - **Explicación pedagógica:** Examina la estructura algebraica de las funciones generatrices de números de Bernoulli y Euler.
  - **Rigor y Fórmulas:** Analiza las fórmulas de suma de potencias de Euler-Maclaurin y las relaciones de paridad polinomial.
  $$\frac{t e^{xt}}{e^t - 1} = \sum_{n=0}^{\infty} B_n(x) \frac{t^n}{n!}$$

* [`src/02_estructuras_algebraicas/avanzado/10_simbolos_acoplamiento_angular.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/02_estructuras_algebraicas/avanzado/10_simbolos_acoplamiento_angular.qmd):
  - **Origen DLMF:** Capítulo 34 (*3j, 6j, 9j Symbols*).
  - **Código MSC2020:** `22E70`, `81R05`.
  - **Explicación pedagógica:** Desarrolla la teoría de coeficientes de Clebsch-Gordan y simetrías de grupos Lie $SU(2)$ y $SO(3)$.
  - **Rigor y Fórmulas:** Formula las identidades de ortogonalidad y relocalización de fase en acoplamientos espinoriales.
  $$\begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix}$$

* [`src/02_estructuras_algebraicas/abstracto/11_funciones_argumento_matricial.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/02_estructuras_algebraicas/abstracto/11_funciones_argumento_matricial.qmd):
  - **Origen DLMF:** Capítulo 35 (*Functions of Matrix Argument*).
  - **Código MSC2020:** `15A15`, `33C99`.
  - **Explicación pedagógica:** Estudiar funciones hipergeométricas y Gamma definidas sobre álgebras de matrices simétricas e hipercomplejas.
  - **Rigor y Fórmulas:** Introduce la transformada de Laplaciano matricial y polinomios de Zonal sobre espectros propios.
  $$\Gamma_m(a) = \int_{A > 0} \operatorname{etr}(-A) (\det A)^{a - \frac{m+1}{2}} dA$$

---

### 🏛️ Pilar 03: Análisis y Continuidad (`src/03_analisis_continuidad/`)

Contiene la mayor parte de las funciones trascendentes de la física matemática y ecuaciones diferenciales clásicas.

* [`src/03_analisis_continuidad/intro/09_funciones_elementales_trascendentes.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/intro/09_funciones_elementales_trascendentes.qmd):
  - **Origen DLMF:** Capítulo 4 (*Elementary Functions*).
  - **Código MSC2020:** `33B10`.
  - **Explicación pedagógica:** Análisis riguroso de logaritmos complejos, ramas de cortes y funciones exponenciales.
  - **Rigor y Fórmulas:** Expone las fórmulas de Euler, inversas trigonométricas y puntos de ramificación en el plano complejo.

* [`src/03_analisis_continuidad/intermedio/13_funcion_gamma_psi.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/intermedio/13_funcion_gamma_psi.qmd):
  - **Origen DLMF:** Capítulo 5 (*Gamma Function*).
  - **Código MSC2020:** `33B15`.
  - **Explicación pedagógica:** La función Gamma de Euler, función Digamma $\psi(z)$ y la constante de Euler-Mascheroni.
  - **Rigor y Fórmulas:** Integra la fórmula de reflexión de Euler, la duplicación de Legendre y la aproximación de Stirling.
  $$\Gamma(z) \Gamma(1-z) = \frac{\pi}{\sin(\pi z)}$$

* [`src/03_analisis_continuidad/intermedio/14_integrales_exponenciales_trigonometricas.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/intermedio/14_integrales_exponenciales_trigonometricas.qmd):
  - **Origen DLMF:** Capítulo 6 (*Exponential, Logarithmic, Sine, and Cosine Integrals*).
  - **Código MSC2020:** `33B20`.
  - **Explicación pedagógica:** Integrales trascendentes $E_n(z)$, $\operatorname{Li}(z)$, $\operatorname{Si}(z)$ y $\operatorname{Ci}(z)$.
  - **Rigor y Fórmulas:** Desarrolla expansiones continuas y soluciones de problemas de difusión conductiva.

* [`src/03_analisis_continuidad/intermedio/15_funciones_error_fresnel_dawson.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/intermedio/15_funciones_error_fresnel_dawson.qmd):
  - **Origen DLMF:** Capítulo 7 (*Error Functions, Dawson’s and Fresnel Integrals*).
  - **Código MSC2020:** `33B20`, `33C10`.
  - **Explicación pedagógica:** Estudio de la función $\operatorname{erf}(z)$, $\operatorname{erfc}(z)$, integrales de Fresnel $C(z), S(z)$ y la integral de Dawson.
  - **Rigor y Fórmulas:** Relaciona las integrales de difracción de ondas electromagnéticas y procesos gaussianos.
  $$\operatorname{erf}(z) = \frac{2}{\sqrt{\pi}} \int_0^z e^{-t^2} dt$$

* [`src/03_analisis_continuidad/avanzado/16_funcion_gamma_incompleta.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/avanzado/16_funcion_gamma_incompleta.qmd):
  - **Origen DLMF:** Capítulo 8 (*Incomplete Gamma and Related Functions*).
  - **Código MSC2020:** `33B20`.
  - **Explicación pedagógica:** Funciones Gamma incompletas $\gamma(a,z)$ y $\Gamma(a,z)$ con integrales de Beta incompletas.
  - **Rigor y Fórmulas:** Proporciona expansiones en fracciones continuas de Cauer y distribuciones acumuladas.

* [`src/03_analisis_continuidad/avanzado/17_funciones_airy.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/avanzado/17_funciones_airy.qmd):
  - **Origen DLMF:** Capítulo 9 (*Airy and Related Functions*).
  - **Código MSC2020:** `33C10`, `34E20`.
  - **Explicación pedagógica:** Funciones $\operatorname{Ai}(z)$ y $\operatorname{Bi}(z)$ como soluciones del problema de punto de retorno diferencial.
  - **Rigor y Fórmulas:** Demuestra el comportamiento en el régimen subyacente de la aproximación WKB.
  $$\frac{d^2 w}{dz^2} - z w = 0$$

* [`src/03_analisis_continuidad/intermedio/18_funciones_bessel.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/intermedio/18_funciones_bessel.qmd):
  - **Origen DLMF:** Capítulo 10 (*Bessel Functions*).
  - **Código MSC2020:** `33C10`.
  - **Explicación pedagógica:** Funciones cilíndricas $J_\nu(z)$, $Y_\nu(z)$, Hankel $H_\nu^{(1)}, H_\nu^{(2)}$ y modadas $I_\nu, K_\nu$.
  - **Rigor y Fórmulas:** Desarrolla relaciones de recurrencia de tres términos, ceros y ortogonalidad en discos.
  $$z^2 \frac{d^2 w}{dz^2} + z \frac{dw}{dz} + (z^2 - \nu^2)w = 0$$

* [`src/03_analisis_continuidad/avanzado/19_funciones_struve.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/avanzado/19_funciones_struve.qmd):
  - **Origen DLMF:** Capítulo 11 (*Struve and Related Functions*).
  - **Código MSC2020:** `33C10`.
  - **Explicación pedagógica:** Funciones $\mathbf{H}_\nu(z)$ y $\mathbf{L}_\nu(z)$ para ecuaciones diferenciales no homogéneas de Bessel.
  - **Rigor y Fórmulas:** Establece integrales de fuentes acústicas y expansiones en términos de funciones de Bessel.

* [`src/03_analisis_continuidad/avanzado/20_funciones_cilindro_parabolico.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/avanzado/20_funciones_cilindro_parabolico.qmd):
  - **Origen DLMF:** Capítulo 12 (*Parabolic Cylinder Functions*).
  - **Código MSC2020:** `33C15`.
  - **Explicación pedagógica:** Funciones $U(a,z)$ y $V(a,z)$ asociadas a pozos de potencial armónico cuántico.
  - **Rigor y Fórmulas:** Deduce la cuantización de niveles de energía y funciones propias de Weber.

* [`src/03_analisis_continuidad/avanzado/21_funciones_hipergeometricas_confluentes.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/avanzado/21_funciones_hipergeometricas_confluentes.qmd):
  - **Origen DLMF:** Capítulo 13 (*Confluent Hypergeometric Functions*).
  - **Código MSC2020:** `33C15`.
  - **Explicación pedagógica:** Funciones de Kummer $M(a,b,z)$ y Tricomi $U(a,b,z)$.
  - **Rigor y Fórmulas:** Deduce las relaciones de confluencia a partir del límite de la serie de Gauss.
  $$z \frac{d^2 w}{dz^2} + (b-z)\frac{dw}{dz} - a w = 0$$

* [`src/03_analisis_continuidad/intermedio/22_funciones_legendre.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/intermedio/22_funciones_legendre.qmd):
  - **Origen DLMF:** Capítulo 14 (*Legendre and Related Functions*).
  - **Código MSC2020:** `33C45`, `33C05`.
  - **Explicación pedagógica:** Polinomios $P_n(x)$ y funciones asociadas de Legendre $P_\mu^\nu(z), Q_\mu^\nu(z)$.
  - **Rigor y Fórmulas:** Define armónicos esféricos en coordenadas multivariables y desarrollo del potencial gravitatorio.

* [`src/03_analisis_continuidad/intermedio/23_funcion_hipergeometrica_gauss.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/intermedio/23_funcion_hipergeometrica_gauss.qmd):
  - **Origen DLMF:** Capítulo 15 (*Hypergeometric Function*).
  - **Código MSC2020:** `33C05`.
  - **Explicación pedagógica:** La serie de Gauss ${}_2F_1(a,b;c;z)$ y soluciones a la ecuación diferencial lineal de segundo orden con 3 singularidades regulares.
  - **Rigor y Fórmulas:** Deduce las 24 soluciones de Kummer y transformaciones de Pfaff.
  $${}_2F_1(a,b;c;z) = \sum_{n=0}^{\infty} \frac{(a)_n (b)_n}{(c)_n} \frac{z^n}{n!}$$

* [`src/03_analisis_continuidad/abstracto/24_hipergeometricas_generalizadas_meijer_g.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/abstracto/24_hipergeometricas_generalizadas_meijer_g.qmd):
  - **Origen DLMF:** Capítulo 16 (*Generalized Hypergeometric Functions and Meijer G-Function*).
  - **Código MSC2020:** `33C20`, `33C60`.
  - **Explicación pedagógica:** Series ${}_pF_q$ y la función $G$ de Meijer como integrador unificador de funciones especiales.
  - **Rigor y Fórmulas:** Describe integrales de Mellin-Barnes y contornos de integración en el plano complejo.

* [`src/03_analisis_continuidad/abstracto/25_funciones_q_hipergeometricas.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/abstracto/25_funciones_q_hipergeometricas.qmd):
  - **Origen DLMF:** Capítulo 17 (*q-Hypergeometric and Related Functions*).
  - **Código MSC2020:** `33D15`.
  - **Explicación pedagógica:** Análogos $q$-discretos, factorial de Pochhammer $q$-desplazado y series de Heine.
  - **Rigor y Fórmulas:** Formula identidades de Rogers-Ramanujan y funciones $q$-Gamma.

* [`src/03_analisis_continuidad/intermedio/26_polinomios_ortogonales_clasicos.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/intermedio/26_polinomios_ortogonales_clasicos.qmd):
  - **Origen DLMF:** Capítulo 18 (*Orthogonal Polynomials*).
  - **Código MSC2020:** `33C45`, `42C05`.
  - **Explicación pedagógica:** Familia de Askey: Polinomios de Jacobi, Laguerre, Hermite, Gegenbauer y Chebyshev.
  - **Rigor y Fórmulas:** Formula la relación de recurrencia de tres términos de Favard y la fórmula de Rodrigues.

* [`src/03_analisis_continuidad/intermedio/27_integrales_elipticas.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/intermedio/27_integrales_elipticas.qmd):
  - **Origen DLMF:** Capítulo 19 (*Elliptic Integrals*).
  - **Código MSC2020:** `33E05`.
  - **Explicación pedagógica:** Integrales elípticas incompletas y completas de Legendre $F(k,\phi), E(k,\phi), \Pi(n,k,\phi)$ y simétricas de Carlson.
  - **Rigor y Fórmulas:** Muestra transformaciones de Landen y aplicaciones en péndulos complejos.

* [`src/03_analisis_continuidad/avanzado/28_funciones_theta_jacobi.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/avanzado/28_funciones_theta_jacobi.qmd):
  - **Origen DLMF:** Capítulo 20 (*Theta Functions*).
  - **Código MSC2020:** `14K25`, `33E05`.
  - **Explicación pedagógica:** Las cuatro funciones Theta de Jacobi $\theta_1, \theta_2, \theta_3, \theta_4$ y su cuasi-periodicidad.
  - **Rigor y Fórmulas:** Expone las identidades triplicadas de Jacobi y la ecuación del calor.

* [`src/03_analisis_continuidad/abstracto/29_funciones_theta_multidimensionales.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/abstracto/29_funciones_theta_multidimensionales.qmd):
  - **Origen DLMF:** Capítulo 21 (*Multidimensional Theta Functions*).
  - **Código MSC2020:** `14K25`, `32G20`.
  - **Explicación pedagógica:** Funciones Theta sobre variedades abelianas y matrices de Riemann de género $g$.
  - **Rigor y Fórmulas:** Formula las relaciones de reciprocidad de Riemann y formas automórficas.

* [`src/03_analisis_continuidad/intermedio/30_funciones_elipticas_jacobi.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/intermedio/30_funciones_elipticas_jacobi.qmd):
  - **Origen DLMF:** Capítulo 22 (*Jacobian Elliptic Functions*).
  - **Código MSC2020:** `33E05`.
  - **Explicación pedagógica:** Las doce funciones elípticas de Jacobi $\operatorname{sn}(u,k), \operatorname{cn}(u,k), \operatorname{dn}(u,k)$.
  - **Rigor y Fórmulas:** Demuestra la doble periodicidad en el plano complejo y sumas de adición.

* [`src/03_analisis_continuidad/avanzado/31_funciones_elipticas_weierstrass_modulares.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/avanzado/31_funciones_elipticas_weierstrass_modulares.qmd):
  - **Origen DLMF:** Capítulo 23 (*Weierstrass Elliptic and Modular Functions*).
  - **Código MSC2020:** `11F11`, `33E05`.
  - **Explicación pedagógica:** Función $\wp(z)$ de Weierstrass, invariantes $g_2, g_3$ y discriminante modular $\Delta(\tau)$.
  - **Rigor y Fórmulas:** Formula la ecuación diferencial cúbica $\wp'^2 = 4\wp^3 - g_2\wp - g_3$.

* [`src/03_analisis_continuidad/avanzado/32_funcion_zeta_riemann.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/avanzado/32_funcion_zeta_riemann.qmd):
  - **Origen DLMF:** Capítulo 25 (*Zeta and Related Functions*).
  - **Código MSC2020:** `11M06`, `11M35`.
  - **Explicación pedagógica:** Función $\zeta(s)$ de Riemann, funciones $L$ de Dirichlet, Hurwitz y Polilogaritmos.
  - **Rigor y Fórmulas:** Analiza la ecuación funcional de Riemann y el producto de Euler.
  $$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_{p \text{ primo}} \frac{1}{1 - p^{-s}}$$

* [`src/03_analisis_continuidad/avanzado/33_funciones_mathieu_ecuacion_hill.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/avanzado/33_funciones_mathieu_ecuacion_hill.qmd):
  - **Origen DLMF:** Capítulo 28 (*Mathieu Functions and Hill’s Equation*).
  - **Código MSC2020:** `33E10`, `34B30`.
  - **Explicación pedagógica:** Ecuación diferencial de Mathieu para sistemas elípticos armónicos y teoría de Floquet.
  - **Rigor y Fórmulas:** Determina zonas de estabilidad e inestabilidad (diagramas de Ince-Strutt).

* [`src/03_analisis_continuidad/abstracto/34_funciones_lame.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/abstracto/34_funciones_lame.qmd):
  - **Origen DLMF:** Capítulo 29 (*Lamé Functions*).
  - **Código MSC2020:** `33E10`.
  - **Explicación pedagógica:** Ecuación de Lamé resultante de la separación de variables de Laplace en coordenadas elipsoidales.
  - **Rigor y Fórmulas:** Construye armónicos elipsoidales y curvas espectrales.

* [`src/03_analisis_continuidad/avanzado/35_funciones_onda_esferoidales.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/avanzado/35_funciones_onda_esferoidales.qmd):
  - **Origen DLMF:** Capítulo 30 (*Spheroidal Wave Functions*).
  - **Código MSC2020:** `33E10`, `35Q60`.
  - **Explicación pedagógica:** Funciones angulares y radiales esferoidales prolatas y oblatas.
  - **Rigor y Fórmulas:** Aplica la dispersión de ondas sobre esferoides de revolución.

* [`src/03_analisis_continuidad/abstracto/36_funciones_heun.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/abstracto/36_funciones_heun.qmd):
  - **Origen DLMF:** Capítulo 31 (*Heun Functions*).
  - **Código MSC2020:** `33E30`, `34M35`.
  - **Explicación pedagógica:** Ecuación de Heun con 4 puntos singulares regulares y sus confluencias.
  - **Rigor y Fórmulas:** Expone las soluciones locales Frobenius y relaciones de transición.

* [`src/03_analisis_continuidad/abstracto/37_trascendentes_painleve.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/abstracto/37_trascendentes_painleve.qmd):
  - **Origen DLMF:** Capítulo 32 (*Painlevé Transcendents*).
  - **Código MSC2020:** `34M55`, `33E30`.
  - **Explicación pedagógica:** Las seis ecuaciones diferenciales no lineales de Painlevé $\text{P}_{\text{I}}$ a $\text{P}_{\text{VI}}$ exentas de puntos críticos móviles.
  - **Rigor y Fórmulas:** Muestra su par de Lax y conexiones con matrices aleatorias.

* [`src/03_analisis_continuidad/avanzado/38_funciones_coulomb.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/avanzado/38_funciones_coulomb.qmd):
  - **Origen DLMF:** Capítulo 33 (*Coulomb Functions*).
  - **Código MSC2020:** `33C15`, `81V45`.
  - **Explicación pedagógica:** Funciones de onda libre de Coulomb $F_L(\eta,\rho)$ y $G_L(\eta,\rho)$ para dispersión nuclear.
  - **Rigor y Fórmulas:** Establece desfases de Coulomb y límites de acoplamiento de carga.

* [`src/03_analisis_continuidad/abstracto/39_integrales_puntos_ensilladura_coalescentes.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/03_analisis_continuidad/abstracto/39_integrales_puntos_ensilladura_coalescentes.qmd):
  - **Origen DLMF:** Capítulo 36 (*Integrals with Coalescing Saddles*).
  - **Código MSC2020:** `41A60`, `58K05`.
  - **Explicación pedagógica:** Método de la fase estacionaria y aproximaciones de ensilladura en presencia de catástrofes.
  - **Rigor y Fórmulas:** Modela expansiones de tipo Airy y Pearcey unificadas.

---

### 🏛️ Pilar 04: Espacio y Forma (`src/04_espacio_forma/`)

* [`src/04_espacio_forma/avanzado/09_geometria_variedades_elipticas.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/04_espacio_forma/avanzado/09_geometria_variedades_elipticas.qmd):
  - **Origen DLMF:** Secciones geométricas de Capítulos 19-23.
  - **Código MSC2020:** `14H52`, `32G15`.
  - **Explicación pedagógica:** Superficies de Riemann de género 1, toros complejos y geometría del espacio modular.
  - **Rigor y Fórmulas:** Integra métricas de Poincaré y retículos en el plano complejo.

---

### 🏛️ Pilar 05: Discreción y Computación (`src/05_discrecion_computacion/`)

* [`src/05_discrecion_computacion/intermedio/09_metodos_numericos_funciones_especiales.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/05_discrecion_computacion/intermedio/09_metodos_numericos_funciones_especiales.qmd):
  - **Origen DLMF:** Capítulo 3 (*Numerical Methods*).
  - **Código MSC2020:** `65D20`, `65D05`.
  - **Explicación pedagógica:** Algoritmos de recurrencia hacia atrás (Olver, Miller) y cuadratura de Gauss.
  - **Rigor y Fórmulas:** Evalúa la acumulación de error de redondeo e inestabilidad numérica.

* [`src/05_discrecion_computacion/intermedio/10_analisis_combinatorio_avanzado.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/05_discrecion_computacion/intermedio/10_analisis_combinatorio_avanzado.qmd):
  - **Origen DLMF:** Capítulo 26 (*Combinatorial Analysis*).
  - **Código MSC2020:** `05A15`, `05A19`.
  - **Explicación pedagógica:** Coeficientes binomiales, números de Stirling, particiones de enteros y permutatrones.
  - **Rigor y Fórmulas:** Identidades de Vandermonde y funciones generatrices combinatorias.

* [`src/05_discrecion_computacion/avanzado/11_funciones_teoria_numeros.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/05_discrecion_computacion/avanzado/11_funciones_teoria_numeros.qmd):
  - **Origen DLMF:** Capítulo 27 (*Functions of Number Theory*).
  - **Código MSC2020:** `11A25`, `11N37`.
  - **Explicación pedagógica:** Función $\phi$ de Euler, función de Möbius $\mu(n)$, suma de divisores $\sigma(n)$ y primos.
  - **Rigor y Fórmulas:** Inversión de Möbius y producto de convolución de Dirichlet.

---

### 🏛️ Pilar 06: Estocástica e Incertidumbre (`src/06_estocastica_incertidumbre/`)

* [`src/06_estocastica_incertidumbre/intermedio/09_distribuciones_funciones_especiales.qmd`](file:///G:/REPOSITORIOS%20GITHUB/POLARIS%20KERNEL/src/06_estocastica_incertidumbre/intermedio/09_distribuciones_funciones_especiales.qmd):
  - **Origen DLMF:** Secciones aplicadas de Capítulos 7 y 8.
  - **Código MSC2020:** `60E05`, `62E15`.
  - **Explicación pedagógica:** Uso de la función de error e integrales Gamma incompletas en distribuciones Gaussianas, Chi-cuadrado y Student.
  - **Rigor y Fórmulas:** Deduce colas de probabilidad y densidad de variables aleatorias compuestas.

---

## Directrices de Calidad, Nomenclatura y Formato

1. **Clasificación por Dificultad Relativa Perferida (MSC2020):**
   - Cada archivo se ubica estrictamente dentro de su correspondiente subcarpeta de dificultad (`intro/`, `intermedio/`, `avanzado/`, `abstracto/`).
   - El nivel pedagógico se determina evaluando la complejidad conceptual y la taxonomía del estándar **MSC2020**:
     - **`intro/`:** Conceptos básicos, funciones elementales y métodos analíticos primarios.
     - **`intermedio/`:** Funciones especiales clásicas (Gamma, Bessel, Legendre, Polinomios Ortogonales, Integrales Elípticas).
     - **`avanzado/`:** Aproximaciones asintóticas, funciones de Mathieu, Airy, Zeta de Riemann, Theta y Ecuaciones de Hill.
     - **`abstracto/`:** Funciones de argumento matricial, $q$-series, G de Meijer, trascendentes de Painlevé y simetrías $3j, 6j, 9j$.

2. **Nomenclatura y Contenido 100% en Español:**
   - Todos los nombres de archivos Markdown/Quarto (`.qmd`) se escriben en **español nativo** y en formato `snake_case` (sin acentos ni caracteres especiales en rutas).
   - Los títulos de capítulos, secciones, explicaciones pedagógicas y notas se redactan completamente en español técnico de alta fidelidad.

3. **Frontmatter YAML Obligatorio para Quarto:**
   - Todo archivo `.qmd` generado debe incluir el encabezado YAML estructurado para su correcta compilación en el sitio web mediante **Quarto**:
   ```yaml
   ---
   id: "33C10"
   title: "Funciones de Bessel"
   pilar: "03_analisis_continuidad"
   msc_code: "33C10"
   difficulty: "intermedio"
   tags:
     - funciones_bessel
     - funciones_especiales
     - analisis_continuidad
   ---
   ```

4. **Segmentación Semántica (*Semantic Line Breaks*):**
   - La prosa explicativa respeta la regla de exactamente una oración por línea para optimizar el procesamiento por agentes de IA.
   - Las ecuaciones matemáticas en bloque (`$$ ... $$`) permanecen exentas de límites de longitud para resguardar la continuidad del razonamiento.

5. **Adyacencia JSON (ADR-002):**
   - Cada archivo `.qmd` generado poseerá su contraparte `.json` homónima con la metainformación estructurada requerida por la arquitectura.

