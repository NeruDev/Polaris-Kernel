#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  // Sistema de coordenadas
  line((-4, 0), (4, 0), mark: (end: ">"), stroke: gray)
  line((0, -3), (0, 4), mark: (end: ">"), stroke: gray)
  content((4.2, 0), [$x$])
  content((0, 4.2), [$y$])
  
  // Asíntota Vertical en x = 1
  line((1, -2.5), (1, 3.5), stroke: (paint: red, dash: "dashed"), name: "AV")
  content((1.8, 3), text(fill: red)[$x = 1$ (AV)])
  
  // Asíntota Horizontal en y = 2
  line((-3.5, 2), (3.5, 2), stroke: (paint: blue, dash: "dashed"), name: "AH")
  content((-2, 2.3), text(fill: blue)[$y = 2$ (AH)])
  
  // Curva de la función f(x) = 2x / (x - 1)
  // Rama derecha
  bezier((1.2, 3.5), (3.5, 2.2), (1.5, 2.5), stroke: (paint: black, thickness: 1.5pt))
  // Rama izquierda
  bezier((-3.5, 1.8), (0.8, -2.5), (-1.5, 1.5), stroke: (paint: black, thickness: 1.5pt))
  
  content((2.5, 3), text(weight: "bold")[$f(x)$])
  
  // Explicación
  content((-2.5, -2), align(left, box(width: 4cm)[
    #text(weight: "bold")[Comportamiento Asintótico:] \
    La curva se acerca \
    infinitamente a las \
    líneas punteadas sin \
    llegar a tocarlas.
  ]))
})
