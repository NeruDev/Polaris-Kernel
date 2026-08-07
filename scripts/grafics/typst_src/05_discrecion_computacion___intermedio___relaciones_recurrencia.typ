#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Nodos del arbol
  let n-root = (0.0, 4.0)
  let n-l1 = (-2.5, 2.0)
  let n-r1 = (2.5, 2.0)
  
  let n-l2 = (-3.5, 0.0)
  let n-r2 = (-1.5, 0.0)
  
  let n-l3 = (1.5, 0.0)
  let n-r3 = (3.5, 0.0)

  // Lineas de conexion
  line(n-root, n-l1, stroke: 1pt + black)
  line(n-root, n-r1, stroke: 1pt + black)
  
  line(n-l1, n-l2, stroke: 1pt + black)
  line(n-l1, n-r2, stroke: 1pt + black)
  
  line(n-r1, n-l3, stroke: 1pt + black)
  line(n-r1, n-r3, stroke: 1pt + black)
  
  // Dibujar circulos y textos
  let draw-node(pos, text-str) = {
    circle(pos, radius: 0.5, fill: rgb(0, 150, 255, 60), stroke: 1.5pt + blue)
    content(pos, text-str)
  }

  draw-node(n-root, [$T(n)$])
  draw-node(n-l1, [$T(n/2)$])
  draw-node(n-r1, [$T(n/2)$])
  
  draw-node(n-l2, [$T(n/4)$])
  draw-node(n-r2, [$T(n/4)$])
  draw-node(n-l3, [$T(n/4)$])
  draw-node(n-r3, [$T(n/4)$])
  
  // Indicar continuacion
  content((0.0, -1.2), [$. . .$], size: 14pt)
})
