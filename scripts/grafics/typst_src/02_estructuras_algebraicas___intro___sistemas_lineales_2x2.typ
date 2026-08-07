#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  // Sistema de coordenadas y ejes
  line((-4, 0), (4, 0), mark: (end: ">"), stroke: gray)
  line((0, -3), (0, 4), mark: (end: ">"), stroke: gray)
  content((4.2, 0), [$x$])
  content((0, 4.2), [$y$])
  
  // Recta 1: y = x + 1 => x - y = -1
  line((-3, -2), (3, 4), stroke: blue, name: "L1")
  content((2.5, 4), text(fill: blue, size: 10pt)[$L_1: y = x + 1$])
  
  // Recta 2: y = -2x + 4 => 2x + y = 4
  line((-0.5, 5), (3.5, -3), stroke: red, name: "L2")
  content((3.5, -2.5), text(fill: red, size: 10pt)[$L_2: y = -2x + 4$])
  
  // Punto de intersección: x+1 = -2x+4 => 3x = 3 => x = 1, y = 2
  circle((1, 2), radius: 0.1, fill: black)
  content((1.8, 2), text(weight: "bold")[$P(1, 2)$])
  
  // Líneas punteadas hacia los ejes
  line((1, 2), (1, 0), stroke: (dash: "dashed", paint: gray))
  line((1, 2), (0, 2), stroke: (dash: "dashed", paint: gray))
  content((1, -0.3), [$1$])
  content((-0.3, 2), [$2$])
  
  // Explicación
  content((4, -3), align(left, box(width: 5cm)[
    #text(weight: "bold")[Solución Única:] \
    Intersección de $L_1$ y $L_2$ \
    representa el vector solución \
    del sistema de ecuaciones.
  ]))
})
