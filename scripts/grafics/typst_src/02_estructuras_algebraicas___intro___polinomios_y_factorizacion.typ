#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)
#set text(font: "Inter", size: 10pt)

#cetz.canvas({
  import cetz.draw: *

  // Ejes
  line((-3, 0), (4, 0), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  line((0, -2), (0, 3), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  
  // Dibujar curva P(x) = (x+2)(x-1)(x-3) aproximadamente (Bezier)
  bezier((-2, 0), (1, 0), (-1, 4), stroke: 1.5pt + rgb("#8e44ad"))
  bezier((1, 0), (3, 0), (2, -3), stroke: 1.5pt + rgb("#8e44ad"))
  bezier((3, 0), (3.5, 2), (3.2, 1), stroke: 1.5pt + rgb("#8e44ad"))
  bezier((-2, 0), (-2.5, -2), (-2.2, -1), stroke: 1.5pt + rgb("#8e44ad"))

  // Raíces
  circle((-2, 0), radius: 0.1, fill: rgb("#c0392b"))
  content((-2, -0.4), [$x_1$])
  
  circle((1, 0), radius: 0.1, fill: rgb("#c0392b"))
  content((1, 0.4), [$x_2$])
  
  circle((3, 0), radius: 0.1, fill: rgb("#c0392b"))
  content((3, 0.4), [$x_3$])
  
  content((2, 2.5), text(fill: rgb("#8e44ad"))[$P(x)$])
})
