#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Ejes cartesianos
  line((-0.5, 0), (5.5, 0), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  line((0, -0.5), (0, 4.2), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  content((5.7, 0), [$x$], size: 9pt)
  content((0, 4.4), [$y$], size: 9pt)
  
  // Parámetros de intervalos
  let a = 1.0
  let b = 4.6
  
  // --- Área Real Bajo la Curva (Sombreado en Turquesa traslúcido) ---
  // Aproximación poligonal de la curva para el sombreado de fondo
  line(
    (1.0, 0), (1.0, 1.3), (1.3, 1.6), (1.6, 1.9), (1.9, 2.2), 
    (2.2, 2.45), (2.5, 2.65), (2.8, 2.8), (3.1, 2.92), (3.4, 3.02), 
    (3.7, 3.1), (4.0, 3.18), (4.3, 3.24), (4.6, 3.3), (4.6, 0),
    close: true,
    fill: rgb("#39C5BB").lighten(85%),
    stroke: none
  )

  // --- Sumas de Riemann (Rectángulos de Aproximación en Azul) ---
  // R1: [1.0, 1.9], Altura f(1.9) = 2.2
  rect((1.0, 0), (1.9, 2.2), fill: rgb("#3498db").lighten(80%), stroke: 0.8pt + rgb("#3498db"))
  
  // R2: [1.9, 2.8], Altura f(2.8) = 2.8
  rect((1.9, 0), (2.8, 2.8), fill: rgb("#3498db").lighten(80%), stroke: 0.8pt + rgb("#3498db"))
  
  // R3: [2.8, 3.7], Altura f(3.7) = 3.1
  rect((2.8, 0), (3.7, 3.1), fill: rgb("#3498db").lighten(80%), stroke: 0.8pt + rgb("#3498db"))
  
  // R4: [3.7, 4.6], Altura f(4.6) = 3.3
  rect((3.7, 0), (4.6, 3.3), fill: rgb("#3498db").lighten(80%), stroke: 0.8pt + rgb("#3498db"))

  // --- Trazado de la Curva Continua f(x) ---
  bezier((0.5, 0.8), (5.0, 3.4), (2.0, 2.5), (3.8, 3.2), stroke: 1.5pt + rgb("#2c3e50"), name: "f")
  content((4.8, 3.55), [$f(x)$], size: 9pt)
  
  // --- Líneas de Proyección de Extremos a y b ---
  line((a, 0), (a, 1.3), stroke: (paint: rgb("#7f8c8d"), thickness: 0.8pt, dash: "dashed"))
  line((b, 0), (b, 3.3), stroke: (paint: rgb("#7f8c8d"), thickness: 0.8pt, dash: "dashed"))

  // --- Indicadores y Acotaciones ---
  // Corchete indicador de ancho de base Delta x en R1
  line((1.0, -0.12), (1.0, -0.05), stroke: 1pt + rgb("#2c3e50"))
  line((1.9, -0.12), (1.9, -0.05), stroke: 1pt + rgb("#2c3e50"))
  line((1.0, -0.08), (1.9, -0.08), stroke: 1pt + rgb("#2c3e50"))
  content((1.45, -0.28), [$Delta x$], size: 8pt)
  
  // --- Etiquetas de los Ejes ---
  content((a, -0.4), [$a = x_0$], size: 9pt)
  content((1.9, -0.4), [$x_1$], size: 8pt)
  content((2.8, -0.4), [$x_2$], size: 8pt)
  content((3.7, -0.4), [$x_3$], size: 8pt)
  content((b, -0.4), [$b = x_n$], size: 9pt)
  
  // Leyenda en la gráfica
  content((2.8, 3.7), [Area $approx sum_(i=1)^n f(x_i) Delta x$], size: 8pt)
})
