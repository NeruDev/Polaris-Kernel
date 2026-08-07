#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  let x-min = -0.5
  let x-max = 4.5
  let y-min = -0.5
  let y-max = 3.5

  // Ejes
  line((x-min, 0), (x-max, 0), mark: (end: ">"))
  line((0, y-min), (0, y-max), mark: (end: ">"))
  content((x-max + 0.3, -0.3), [$x$])
  content((-0.3, y-max + 0.3), [$y$])

  // Curva: f(x) = 0.5 * x * sin(x) + 1.5
  let curve-points = ()
  for i in range(0, 41) {
    let x = float(i) * 0.1
    let y = 0.5 * x * calc.sin(x * 1rad) + 1.5
    curve-points.push((x, y))
  }
  
  // Rellenar area bajo la curva
  let area-points = ((1.0, 0.0),)
  for i in range(10, 31) {
    let x = float(i) * 0.1
    let y = 0.5 * x * calc.sin(x * 1rad) + 1.5
    area-points.push((x, y))
  }
  area-points.push((3.0, 0.0))
  
  line(..area-points, close: true, fill: rgb(0, 150, 255, 50), stroke: none)

  // Dibujar curva
  line(..curve-points, stroke: 1.5pt + blue)
  
  // Limites de integracion
  line((1.0, 0.0), (1.0, 0.5 * 1.0 * calc.sin(1rad) + 1.5), stroke: (paint: gray, dash: "dashed"))
  line((3.0, 0.0), (3.0, 0.5 * 3.0 * calc.sin(3rad) + 1.5), stroke: (paint: gray, dash: "dashed"))
  content((1.0, -0.3), [$a$])
  content((3.0, -0.3), [$b$])
  content((2.0, 0.7), [$integral_a^b f(x) d x$])
  content((3.8, 2.8), text(fill: blue)[$y = f(x)$])
})
