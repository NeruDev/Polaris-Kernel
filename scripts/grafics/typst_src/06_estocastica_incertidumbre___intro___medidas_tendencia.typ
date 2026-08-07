#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  // Sistema de ejes
  line((0, 0), (6, 0), mark: (end: ">"), stroke: gray)
  line((0, 0), (0, 3), mark: (end: ">"), stroke: gray)
  content((6.2, 0), [$x$])
  content((0, 3.2), [$f(x)$])
  
  // Dibujar una curva asimétrica (Distribución Sesgada a la Derecha)
  bezier((0.5, 0), (5.5, 0.2), (1.5, 4), stroke: (paint: black, thickness: 1.5pt))
  
  // Posición Moda (punto más alto)
  line((1.1, 0), (1.1, 2.1), stroke: (paint: red, dash: "dashed"))
  content((1.1, -0.3), text(fill: red, size: 8pt)[Moda])
  
  // Posición Mediana (divide el área 50/50)
  line((1.7, 0), (1.7, 1.8), stroke: (paint: blue, dash: "dashed"))
  content((1.7, -0.7), text(fill: blue, size: 8pt)[Mediana])
  
  // Posición Media (centro de masa, arrastrada por el sesgo)
  line((2.3, 0), (2.3, 1.4), stroke: (paint: green.darken(20%), dash: "dashed"))
  content((2.3, -1.1), text(fill: green.darken(20%), size: 8pt)[Media])
  
  // Explicación
  content((3.5, 2.5), align(left, box(width: 4cm)[
    #text(weight: "bold", size: 10pt)[Sesgo Positivo] \
    En distribuciones asimétricas, \
    los valores extremos arrastran \
    la Media hacia la cola, \
    mientras la Mediana se resiste.
  ]))
})
