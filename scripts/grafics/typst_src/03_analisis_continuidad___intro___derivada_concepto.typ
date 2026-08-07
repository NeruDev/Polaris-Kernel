#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Ejes cartesianos
  line((-0.5, 0), (5.5, 0), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  line((0, -0.5), (0, 4.2), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  content((5.7, 0), [$x$], size: 9pt)
  content((0, 4.4), [$y$], size: 9pt)
  
  // Curva de la función f(x)
  bezier((0.5, 0.6), (5.0, 3.5), (2.0, 2.3), (3.8, 3.2), stroke: 1.5pt + rgb("#2c3e50"), name: "f")
  content((4.8, 3.6), [$f(x)$], size: 9pt)
  
  // Puntos definidos
  let a = 1.8
  let h = 1.6
  let a_h = a + h
  
  let fa = 1.76 // f(a) aproximado
  let fah = 2.72 // f(a+h) aproximado
  
  // --- Recta Secante (Pasa por (a, fa) y (a+h, fah)) ---
  // Ecuación aproximada de la secante: y - fa = m * (x - a)
  // m = (2.72 - 1.76) / 1.6 = 0.96 / 1.6 = 0.6
  // y = 0.6*(x - 1.8) + 1.76 = 0.6*x + 0.68
  line((0.3, 0.86), (4.8, 3.56), stroke: (paint: rgb("#3498db"), thickness: 1.2pt, dash: "dashed"), name: "secante")
  content((4.7, 3.8), [Secante (pendiente $frac(Delta y, h)$)], size: 7pt, fill: white)
  
  // --- Recta Tangente en (a, fa) ---
  // Ecuación de la tangente (pendiente aproximada en a = 1.8 es m_t = 0.8)
  // y - 1.76 = 0.8 * (x - 1.8) => y = 0.8*x + 0.32
  line((0.5, 0.72), (4.5, 3.92), stroke: 1.5pt + rgb("#39C5BB"), name: "tangente")
  content((4.4, 4.15), [Tangente (pendiente $f'(a)$)], size: 7pt, fill: white)
  
  // --- Triángulo de Incrementos (Secante) ---
  // Cateto horizontal (h) de (a, fa) a (a+h, fa)
  line((a, fa), (a_h, fa), stroke: (paint: rgb("#e67e22"), thickness: 1.2pt), name: "cat_h")
  content((a + h/2, fa - 0.25), [$h$], size: 9pt)
  
  // Cateto vertical (Delta y) de (a+h, fa) a (a+h, fah)
  line((a_h, fa), (a_h, fah), stroke: (paint: rgb("#e67e22"), thickness: 1.2pt), name: "cat_v")
  content((a_h + 0.5, fa + (fah - fa)/2), [$Delta y = f(a+h) - f(a)$], size: 8pt)
  
  // --- Líneas de Proyección de los Ejes ---
  // Para el punto a
  line((a, 0), (a, fa), stroke: (paint: rgb("#7f8c8d"), thickness: 0.8pt, dash: "dotted"))
  line((0, fa), (a, fa), stroke: (paint: rgb("#7f8c8d"), thickness: 0.8pt, dash: "dotted"))
  
  // Para el punto a+h
  line((a_h, 0), (a_h, fah), stroke: (paint: rgb("#7f8c8d"), thickness: 0.8pt, dash: "dotted"))
  line((0, fah), (a_h, fah), stroke: (paint: rgb("#7f8c8d"), thickness: 0.8pt, dash: "dotted"))
  
  // Puntos geométricos de intersección (P y Q)
  circle((a, fa), radius: 2.5pt, fill: rgb("#39C5BB"), stroke: 1pt + white) // Punto de tangencia P
  circle((a_h, fah), radius: 2pt, fill: rgb("#3498db"), stroke: 0.8pt + white) // Punto secante Q
  
  // --- Etiquetas de los Ejes ---
  content((a, -0.35), [$a$], size: 9pt)
  content((a_h, -0.35), [$a+h$], size: 9pt)
  content((-0.3, fa), [$f(a)$], size: 9pt)
  content((-0.5, fah), [$f(a+h)$], size: 9pt)
})
