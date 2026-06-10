#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Ejes cartesianos
  line((-3.2, 0), (4.2, 0), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  line((0, -3.2), (0, 3.2), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  content((4.4, 0), [$x$], size: 9pt)
  content((0, 3.4), [$y$], size: 9pt)
  
  // Campo de pendientes de la EDO dy/dx = x - y
  // Cuadrícula de puntos
  for xi in range(-14, 18) {
    for yi in range(-12, 13) {
      let x = float(xi) * 0.25
      let y = float(yi) * 0.25
      
      // Omitir puntos que salgan del área de interés principal
      if x < -3.0 or x > 3.8 or y < -2.8 or y > 2.8 {
        continue
      }
      
      let m = x - y
      
      // Vector director unitario
      let length = calc.sqrt(1 + m * m)
      let dx = 1.0 / length
      let dy = m / length
      
      // Longitud del segmento
      let L = 0.16
      let start_x = x - (dx * L / 2)
      let start_y = y - (dy * L / 2)
      let end_x = x + (dx * L / 2)
      let end_y = y + (dy * L / 2)
      
      // Color degradado elegante según la magnitud de la pendiente
      let val = calc.min(5.0, calc.abs(m)) / 5.0
      let c = rgb(
        int(127 + val * 60),
        int(140 - val * 40),
        int(141 - val * 20)
      )
      
      line((start_x, start_y), (end_x, end_y), stroke: 0.8pt + c)
    }
  }
  
  // --- Solución 1 (C = 2.0, superior) ---
  // y(x) = x - 1 + 2 * exp(-x)
  let points1 = ()
  for xi in range(-12, 36) {
    let x = float(xi) * 0.1
    let y = x - 1.0 + 2.0 * calc.exp(-x)
    if y >= -3.0 and y <= 3.0 {
      points1.push((x, y))
    }
  }
  line(..points1, stroke: 1.8pt + rgb("#e74c3c"), name: "sol1")
  content((1.2, 1.8), [$y(x) = x - 1 + 2e^{-x}$], size: 8pt, fill: white)
  
  // --- Solución 2 (C = -1.2, inferior) ---
  // y(x) = x - 1 - 1.2 * exp(-x)
  let points2 = ()
  for xi in range(-5, 36) {
    let x = float(xi) * 0.1
    let y = x - 1.0 - 1.2 * calc.exp(-x)
    if y >= -3.0 and y <= 3.0 {
      points2.push((x, y))
    }
  }
  line(..points2, stroke: 1.8pt + rgb("#3498db"), name: "sol2")
  content((1.6, -0.2), [$y(x) = x - 1 - 1.2e^{-x}$], size: 8pt, fill: white)
  
  // --- Solución Particular Asintótica (C = 0) ---
  // y(x) = x - 1 (recta atrayente)
  line((-2.0, -3.0), (3.8, 2.8), stroke: (paint: rgb("#27ae60"), thickness: 1.5pt, dash: "dashed"), name: "sol3")
  content((3.3, 1.9), [$y(x) = x - 1$], size: 8pt, fill: white)
  
  // Etiquetas del gráfico
  content((-1.8, 2.5), [$frac(d y, d x) = x - y$], size: 10pt)
})
