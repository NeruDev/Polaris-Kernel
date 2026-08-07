#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  let x-min = -1.0
  let x-max = 5.0
  let y-min = -1.0
  let y-max = 4.0

  // Ejes
  line((x-min, 0), (x-max, 0), mark: (end: ">"))
  line((0, y-min), (0, y-max), mark: (end: ">"))
  content((x-max + 0.3, -0.3), [$x$])
  content((-0.3, y-max + 0.3), [$y$])

  // Polinomio cúbico para ilustrar máximos y mínimos
  // f(x) = -1/3 (x-1)(x-3.5)(x+1) + 2 = -1/3(x^3 - 3.5x^2 - x + 3.5) + 2
  let f(x) = -0.3333 * (x - 1.0) * (x - 3.5) * (x + 1.0) + 1.5
  
  let curve-points = ()
  for i in range(0, 51) {
    let x = -1.0 + float(i) * 0.11
    let y = f(x)
    curve-points.push((x, y))
  }
  
  line(..curve-points, stroke: 1.5pt + blue)
  
  // Máximo local
  let x-max-loc = 2.41
  let y-max-loc = f(x-max-loc)
  circle((x-max-loc, y-max-loc), radius: 0.08, fill: red)
  line((x-max-loc - 0.7, y-max-loc), (x-max-loc + 0.7, y-max-loc), stroke: (paint: red, dash: "dashed"))
  content((x-max-loc, y-max-loc + 0.6), text(fill: red)[Máximo])

  // Mínimo local
  let x-min-loc = -0.07
  let y-min-loc = f(x-min-loc)
  circle((x-min-loc, y-min-loc), radius: 0.08, fill: green)
  line((x-min-loc - 0.7, y-min-loc), (x-min-loc + 0.7, y-min-loc), stroke: (paint: green, dash: "dashed"))
  content((x-min-loc, y-min-loc - 0.6), text(fill: green)[Mínimo])
})
