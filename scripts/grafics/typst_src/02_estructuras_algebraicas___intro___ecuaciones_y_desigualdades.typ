#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)
#set text(font: "Inter", size: 10pt)

#cetz.canvas({
  import cetz.draw: *

  // Ejes
  line((-1, 0), (5, 0), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  line((0, -1), (0, 4), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  content((5.2, 0), [$x$])
  content((0, 4.2), [$y$])

  // Línea 1: y = 2x - 1 (Puntos: (0,-1) a (2.5, 4))
  line((0, -1), (2.5, 4), stroke: 1.5pt + rgb("#3498db"), name: "L1")
  content((2.8, 3.8), text(fill: rgb("#3498db"))[$y = 2x - 1$])

  // Línea 2: y = -x + 5 (Puntos: (1, 4) a (5, 0))
  line((1, 4), (5, 0), stroke: 1.5pt + rgb("#e74c3c"), name: "L2")
  content((4.5, 1.2), text(fill: rgb("#e74c3c"))[$y = -x + 5$])

  // Intersección en (2, 3)
  circle((2, 3), radius: 0.1, fill: rgb("#2c3e50"))
  content((1.2, 3), [$(2, 3)$])
  
  // Proyecciones
  line((2, 0), (2, 3), stroke: (dash: "dashed", paint: rgb("#bdc3c7")))
  line((0, 3), (2, 3), stroke: (dash: "dashed", paint: rgb("#bdc3c7")))
  content((2, -0.3), [$2$])
  content((-0.3, 3), [$3$])
})
