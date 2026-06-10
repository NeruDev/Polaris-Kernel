#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Ejes cartesianos
  line((-0.5, 0), (5.5, 0), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  line((0, -0.5), (0, 4.2), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  content((5.7, 0), [$x$], size: 9pt)
  content((0, 4.4), [$y$], size: 9pt)
  
  // Dibujar la curva f(x) usando bezier suave
  bezier((0.5, 0.8), (5.0, 3.8), (2.0, 2.2), (4.0, 2.8), stroke: 1.5pt + rgb("#2c3e50"), name: "f")
  content((4.8, 3.9), [$f(x)$], size: 9pt)
  
  // Parametros estáticos de épsilon y delta para posicionar elementos
  let a = 3.0
  let L = 2.5
  
  let delta = 0.6
  let epsilon = 0.4
  
  let x1 = a - delta
  let x2 = a + delta
  
  let y_a = L
  let y_x1 = 2.15
  let y_x2 = 2.85
  
  let y_ep_down = L - epsilon
  let y_ep_up = L + epsilon
  
  // --- Bandas de Tolerancia ---
  // Relleno traslúcido para la tolerancia épsilon (Eje Y)
  rect((0, y_ep_down), (5.0, y_ep_up), fill: rgb("#e74c3c").lighten(90%), stroke: none)
  // Relleno traslúcido para el entorno delta (Eje X)
  rect((x1, 0), (x2, 4.0), fill: rgb("#3498db").lighten(92%), stroke: none)
  
  // --- Líneas de Proyección ---
  // Proyección central (a, L)
  line((a, 0), (a, y_a), stroke: (paint: rgb("#7f8c8d"), thickness: 1pt, dash: "dashed"))
  line((0, y_a), (a, y_a), stroke: (paint: rgb("#7f8c8d"), thickness: 1pt, dash: "dashed"))
  
  // Proyecciones laterales
  line((x1, 0), (x1, y_x1), stroke: (paint: rgb("#7f8c8d"), thickness: 0.8pt, dash: "dotted"))
  line((0, y_x1), (x1, y_x1), stroke: (paint: rgb("#7f8c8d"), thickness: 0.8pt, dash: "dotted"))
  
  line((x2, 0), (x2, y_x2), stroke: (paint: rgb("#7f8c8d"), thickness: 0.8pt, dash: "dotted"))
  line((0, y_x2), (x2, y_x2), stroke: (paint: rgb("#7f8c8d"), thickness: 0.8pt, dash: "dotted"))
  
  // Marcadores de puntos en la curva
  circle((a, y_a), radius: 2.5pt, fill: rgb("#2980b9"), stroke: 1pt + white)
  circle((x1, y_x1), radius: 2pt, fill: rgb("#7f8c8d"), stroke: 0.5pt + white)
  circle((x2, y_x2), radius: 2pt, fill: rgb("#7f8c8d"), stroke: 0.5pt + white)
  
  // --- Corchetes e Intervalos ---
  // Intervalo delta en el eje X
  line((x1, -0.15), (x1, -0.05), stroke: 1.2pt + rgb("#3498db"))
  line((x2, -0.15), (x2, -0.05), stroke: 1.2pt + rgb("#3498db"))
  line((x1, -0.1), (x2, -0.1), stroke: 1.2pt + rgb("#3498db"))
  
  // Intervalo épsilon en el eje Y
  line((-0.15, y_ep_down), (-0.05, y_ep_down), stroke: 1.2pt + rgb("#e74c3c"))
  line((-0.15, y_ep_up), (-0.05, y_ep_up), stroke: 1.2pt + rgb("#e74c3c"))
  line((-0.1, y_ep_down), (-0.1, y_ep_up), stroke: 1.2pt + rgb("#e74c3c"))
  
  // --- Etiquetas de texto ---
  // Eje X
  content((a, -0.4), [$a$], size: 9pt)
  content((x1 - 0.1, -0.4), [$a-delta$], size: 8pt)
  content((x2 + 0.1, -0.4), [$a+delta$], size: 8pt)
  content((a, -0.75), [entorno de $delta$], size: 7pt)
  
  // Eje Y
  content((-0.3, L), [$L$], size: 9pt)
  content((-0.5, y_ep_down), [$L-epsilon$], size: 8pt)
  content((-0.5, y_ep_up), [$L+epsilon$], size: 8pt)
  content((-1.2, L), [tolerancia $epsilon$], size: 7pt)
})
