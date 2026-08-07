#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  let x-min = -3.0
  let x-max = 3.0
  let y-min = 0.0
  let y-max = 1.0

  // Ejes
  line((x-min, 0.0), (x-max, 0.0), mark: (end: ">"))
  line((0.0, y-min), (0.0, y-max), mark: (end: ">"))
  
  // Dibujar distribución original n=1 (Uniforme)
  // Rango -1.732 a 1.732 (varianza 1)
  let bound = 1.732
  let h = 1.0 / (2.0 * bound) // approx 0.288
  line((-bound, 0.0), (-bound, h), (bound, h), (bound, 0.0), stroke: 1pt + gray, fill: rgb(150, 150, 150, 50))
  content((1.8, h + 0.1), text(fill: gray)[$n=1$])

  // Dibujar Normal objetivo (n->infty)
  let normal-pdf(x) = calc.exp(-x*x / 2.0) / calc.sqrt(2.0 * calc.pi)
  let curve-pts = ()
  for i in range(0, 61) {
    let x = -3.0 + float(i) * 0.1
    curve-pts.push((x, normal-pdf(x)))
  }
  line(..curve-pts, stroke: 1.5pt + blue)
  content((2.4, 0.5), text(fill: blue)[$n -> oo$ ($N(0,1)$)])
  
  // Aproximación n=2 (Triangular)
  line((-2.45, 0.0), (0.0, 0.408), (2.45, 0.0), stroke: 1pt + rgb("#e67e22"), fill: rgb(230, 126, 34, 40))
  content((-2.0, 0.35), text(fill: rgb("#e67e22"))[$n=2$])
})
