#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Ejes cartesianos
  line((-3.8, 0), (7.0, 0), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  line((0, -1.5), (0, 1.5), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  content((7.2, 0), [$theta$], size: 10pt)
  content((0, 1.65), [$y$], size: 10pt)
  
  // Líneas de límite y = 1 y y = -1
  line((-3.6, 1), (6.6, 1), stroke: (paint: rgb("#bdc3c7"), thickness: 0.8pt, dash: "dashed"))
  line((-3.6, -1), (6.6, -1), stroke: (paint: rgb("#bdc3c7"), thickness: 0.8pt, dash: "dashed"))
  
  // Marcas en el eje Y
  line((-0.08, 1), (0.08, 1), stroke: 1pt + rgb("#7f8c8d"))
  content((-0.3, 1), [$1$], size: 8pt)
  line((-0.08, -1), (0.08, -1), stroke: 1pt + rgb("#7f8c8d"))
  content((-0.3, -1), [$-1$], size: 8pt)
  
  // Marcas y etiquetas especiales en el eje X
  let ticks = (
    (-3.1416, [$-pi$]),
    (-1.5708, [$-pi/2$]),
    (1.5708, [$pi/2$]),
    (3.1416, [$pi$]),
    (4.7124, [$3pi/2$]),
    (6.2832, [$2pi$])
  )
  
  for (val, label) in ticks {
    line((val, -0.08), (val, 0.08), stroke: 1pt + rgb("#7f8c8d"))
    content((val, -0.35), label, size: 8pt)
  }
  
  // Curva de la función Seno: y = sin(x)
  let sin_pts = ()
  for i in range(-50, 96) {
    let x = float(i) * 0.07
    let y = calc.sin(x)
    sin_pts.push((x, y))
  }
  line(..sin_pts, stroke: 2pt + rgb("#3498db"), name: "sin_line")
  
  // Curva de la función Coseno: y = cos(x)
  let cos_pts = ()
  for i in range(-50, 96) {
    let x = float(i) * 0.07
    let y = calc.cos(x)
    cos_pts.push((x, y))
  }
  line(..cos_pts, stroke: 2pt + rgb("#e74c3c"), name: "cos_line")
  
  // Etiquetas sobre las curvas
  content((1.9, 0.7), [$y = sin(theta)$], size: 9pt, fill: white)
  content((3.8, -0.7), [$y = cos(theta)$], size: 9pt, fill: white)
})
