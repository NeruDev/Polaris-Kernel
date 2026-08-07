#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  let x-min = 0.0
  let x-max = 5.0
  let y-min = 0.0
  let y-max = 5.0

  // Ejes
  line((x-min, 0.0), (x-max, 0.0), mark: (end: ">"))
  line((0.0, y-min), (0.0, y-max), mark: (end: ">"))
  content((x-max + 0.3, -0.3), [$X$])
  content((-0.3, y-max + 0.3), [$Y$])

  // Puntos de datos (dispersión)
  let data = (
    (0.5, 1.2), (1.0, 1.8), (1.2, 1.5), (1.8, 2.5), 
    (2.1, 2.1), (2.5, 2.8), (2.8, 2.4), (3.2, 3.5),
    (3.5, 3.1), (4.0, 3.8), (4.2, 4.3), (4.5, 3.9)
  )

  for p in data {
    circle(p, radius: 0.05, fill: rgb("#34495e"))
  }

  // Recta de regresión: y = 0.8x + 0.6 (aprox)
  let line-fn(x) = 0.75 * x + 0.7
  
  let line-pts = ((0.2, line-fn(0.2)), (4.8, line-fn(4.8)))
  line(..line-pts, stroke: 1.5pt + rgb("#e74c3c"))
  
  content((4.5, 2.0), text(fill: rgb("#e74c3c"))[$hat(y) = beta_0 + beta_1 x$])

  // Dibujar un residuo ilustrativo
  let rp = data.at(7) // (3.2, 3.5)
  let r_pred = line-fn(rp.at(0))
  line(rp, (rp.at(0), r_pred), stroke: (paint: gray, dash: "dashed"))
  content((rp.at(0) - 0.5, (rp.at(1) + r_pred) / 2.0), text(size: 8pt)[Residuo])
})
