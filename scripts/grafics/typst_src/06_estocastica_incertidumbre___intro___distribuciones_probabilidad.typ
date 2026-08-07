#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  let x-min = -4.0
  let x-max = 4.0
  let y-min = 0.0
  let y-max = 0.5

  // Ejes
  line((x-min, 0.0), (x-max, 0.0), mark: (end: ">"))
  line((0.0, y-min), (0.0, y-max), mark: (end: ">"))
  content((x-max + 0.3, -0.05), [$z$])
  content((-0.2, y-max + 0.05), [$f(z)$])

  // Normal pdf function
  let normal-pdf(x) = calc.exp(-x*x / 2.0) / calc.sqrt(2.0 * calc.pi)

  // Curva Normal Estándar
  let curve-pts = ()
  for i in range(0, 81) {
    let x = -4.0 + float(i) * 0.1
    curve-pts.push((x, normal-pdf(x)))
  }

  // Rellenar área [-1, 1]
  let area-pts = ((-1.0, 0.0),)
  for i in range(0, 21) {
    let x = -1.0 + float(i) * 0.1
    area-pts.push((x, normal-pdf(x)))
  }
  area-pts.push((1.0, 0.0))
  
  line(..area-pts, close: true, fill: rgb(0, 150, 255, 60), stroke: none)

  // Dibujar curva
  line(..curve-pts, stroke: 1.5pt + blue)
  
  // Marcas en sigma
  line((-1.0, 0.0), (-1.0, normal-pdf(-1.0)), stroke: (paint: gray, dash: "dashed"))
  line((1.0, 0.0), (1.0, normal-pdf(1.0)), stroke: (paint: gray, dash: "dashed"))
  
  content((-1.0, -0.1), [$-sigma$])
  content((1.0, -0.1), [$+sigma$])
  content((0.0, 0.2), text(fill: blue)[$68.2\%$])
})
