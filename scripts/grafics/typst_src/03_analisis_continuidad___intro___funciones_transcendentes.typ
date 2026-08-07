#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  // Configuracion del grafico
  let x-min = -3.0
  let x-max = 3.0
  let y-min = -3.0
  let y-max = 4.0

  // Ejes
  line((x-min, 0), (x-max, 0), mark: (end: ">"), name: "x-axis")
  line((0, y-min), (0, y-max), mark: (end: ">"), name: "y-axis")
  content((x-max + 0.3, -0.3), [$x$])
  content((-0.3, y-max + 0.3), [$y$])

  // Grafica de e^x
  let exp-points = ()
  for i in range(0, 61) {
    let x = -3.0 + float(i) * 0.1
    let y = calc.exp(x)
    if y <= y-max {
      exp-points.push((x, y))
    }
  }
  line(..exp-points, stroke: 1.5pt + blue, name: "exp-curve")
  content((1.8, 3.5), text(fill: blue)[$y = e^x$])

  // Grafica de ln(x)
  let ln-points = ()
  for i in range(1, 61) {
    let x = 0.05 + float(i) * 0.05
    let y = calc.ln(x)
    if y >= y-min and x <= x-max {
      ln-points.push((x, y))
    }
  }
  line(..ln-points, stroke: 1.5pt + red, name: "ln-curve")
  content((3.0, 1.2), text(fill: red)[$y = ln(x)$])

  // Identidad y=x
  line((y-min, y-min), (y-max - 1.0, y-max - 1.0), stroke: (paint: gray, dash: "dashed"), name: "identity-curve")
  content((3.6, 3.2), text(fill: gray)[$y = x$])
})
