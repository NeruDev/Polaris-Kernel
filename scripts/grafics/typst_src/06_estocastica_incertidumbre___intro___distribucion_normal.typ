#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Escala general del gráfico
  let sx(x) = { x * 1.8 }
  let sy(y) = { y * 11.0 }
  
  // Rejilla de fondo horizontal (sutil)
  for y in (0.1, 0.2, 0.3, 0.4) {
    line(
      (sx(-4.0), sy(y)),
      (sx(4.0), sy(y)),
      stroke: 0.5pt + rgb("#e2e8f0")
    )
  }
  
  // Ejes cartesianos
  line(
    (sx(-4.2), sy(0)),
    (sx(4.5), sy(0)),
    mark: (end: ">"),
    stroke: 1.2pt + rgb("#475569")
  )
  line(
    (sx(0), sy(-0.02)),
    (sx(0), sy(0.45)),
    mark: (end: ">"),
    stroke: 1.2pt + rgb("#475569")
  )
  
  // Etiquetas de los ejes
  content((sx(4.7), sy(0)), [$z$], size: 11pt)
  content((sx(0), sy(0.47)), [$f(z)$], size: 11pt)
  
  // Definición de las regiones para colorear la regla empírica (68-95-99.7)
  let steps = 30
  
  // 1. Región [-1, 1] (~68.27%)
  let pts1 = ((sx(-1.0), sy(0.0)),)
  for i in range(0, steps + 1) {
    let x = -1.0 + float(i) * 2.0 / float(steps)
    let y = 0.398942 * calc.exp(-0.5 * x * x)
    pts1.push((sx(x), sy(y)))
  }
  pts1.push((sx(1.0), sy(0.0)))
  line(..pts1, close: true, fill: rgb("#3b82f63a"), stroke: none)
  
  // 2. Región [-2, -1] y [1, 2] (~13.59% cada una)
  let pts2l = ((sx(-2.0), sy(0.0)),)
  for i in range(0, steps + 1) {
    let x = -2.0 + float(i) * 1.0 / float(steps)
    let y = 0.398942 * calc.exp(-0.5 * x * x)
    pts2l.push((sx(x), sy(y)))
  }
  pts2l.push((sx(-1.0), sy(0.0)))
  line(..pts2l, close: true, fill: rgb("#3b82f620"), stroke: none)
  
  let pts2r = ((sx(1.0), sy(0.0)),)
  for i in range(0, steps + 1) {
    let x = 1.0 + float(i) * 1.0 / float(steps)
    let y = 0.398942 * calc.exp(-0.5 * x * x)
    pts2r.push((sx(x), sy(y)))
  }
  pts2r.push((sx(2.0), sy(0.0)))
  line(..pts2r, close: true, fill: rgb("#3b82f620"), stroke: none)
  
  // 3. Región [-3, -2] y [2, 3] (~2.14% cada una)
  let pts3l = ((sx(-3.0), sy(0.0)),)
  for i in range(0, steps + 1) {
    let x = -3.0 + float(i) * 1.0 / float(steps)
    let y = 0.398942 * calc.exp(-0.5 * x * x)
    pts3l.push((sx(x), sy(y)))
  }
  pts3l.push((sx(-2.0), sy(0.0)))
  line(..pts3l, close: true, fill: rgb("#3b82f60e"), stroke: none)
  
  let pts3r = ((sx(2.0), sy(0.0)),)
  for i in range(0, steps + 1) {
    let x = 2.0 + float(i) * 1.0 / float(steps)
    let y = 0.398942 * calc.exp(-0.5 * x * x)
    pts3r.push((sx(x), sy(y)))
  }
  pts3r.push((sx(3.0), sy(0.0)))
  line(..pts3r, close: true, fill: rgb("#3b82f60e"), stroke: none)
  
  // Curva de la Distribución Normal Estándar f(x) = (1/sqrt(2pi)) * e^(-x^2/2)
  let curve_pts = ()
  let curve_steps = 120
  for i in range(0, curve_steps + 1) {
    let x = -4.0 + float(i) * 8.0 / float(curve_steps)
    let y = 0.398942 * calc.exp(-0.5 * x * x)
    curve_pts.push((sx(x), sy(y)))
  }
  line(..curve_pts, stroke: 2.2pt + rgb("#2563eb"), name: "normal_curve")
  
  // Líneas verticales indicando las desviaciones estándar
  // Media (x=0)
  line(
    (sx(0), sy(0)),
    (sx(0), sy(0.3989)),
    stroke: (paint: rgb("#475569"), thickness: 1.0pt, dash: "dashed")
  )
  
  // +/- 1 Desviación estándar (x = 1, -1)
  let y_1s = 0.398942 * calc.exp(-0.5)
  line((sx(1), sy(0)), (sx(1), sy(y_1s)), stroke: (paint: rgb("#94a3b8"), thickness: 0.8pt, dash: "dotted"))
  line((sx(-1), sy(0)), (sx(-1), sy(y_1s)), stroke: (paint: rgb("#94a3b8"), thickness: 0.8pt, dash: "dotted"))
  
  // +/- 2 Desviaciones estándar (x = 2, -2)
  let y_2s = 0.398942 * calc.exp(-2.0)
  line((sx(2), sy(0)), (sx(2), sy(y_2s)), stroke: (paint: rgb("#94a3b8"), thickness: 0.8pt, dash: "dotted"))
  line((sx(-2), sy(0)), (sx(-2), sy(y_2s)), stroke: (paint: rgb("#94a3b8"), thickness: 0.8pt, dash: "dotted"))
  
  // +/- 3 Desviaciones estándar (x = 3, -3)
  let y_3s = 0.398942 * calc.exp(-4.5)
  line((sx(3), sy(0)), (sx(3), sy(y_3s)), stroke: (paint: rgb("#94a3b8"), thickness: 0.8pt, dash: "dotted"))
  line((sx(-3), sy(0)), (sx(-3), sy(y_3s)), stroke: (paint: rgb("#94a3b8"), thickness: 0.8pt, dash: "dotted"))
  
  // Marcas en el eje X con texto matemático
  let ticks_x = (
    (-3, [$-3sigma$]),
    (-2, [$-2sigma$]),
    (-1, [$-sigma$]),
    (0, [$mu$]),
    (1, [$sigma$]),
    (2, [$2sigma$]),
    (3, [$3sigma$])
  )
  
  for (x, label) in ticks_x {
    line((sx(x), sy(-0.008)), (sx(x), sy(0.008)), stroke: 1pt + rgb("#475569"))
    content(
      (sx(x), sy(-0.035)),
      text(fill: rgb("#334155"), size: 9pt)[#label]
    )
  }
  
  // Marcas en el eje Y
  for y in (0.1, 0.2, 0.3, 0.4) {
    line((sx(-0.08), sy(y)), (sx(0.08), sy(y)), stroke: 1pt + rgb("#475569"))
    content(
      (sx(-0.35), sy(y)),
      text(fill: rgb("#475569"), size: 8pt)[#str(y)]
    )
  }
  
  // Etiquetas del porcentaje de la regla empírica
  // Centro [ -1, 1 ] (~68.27%)
  content(
    (sx(0), sy(0.13)),
    text(fill: rgb("#1e3a8a"), size: 10pt, weight: "bold")[68.27%]
  )
  
  // Lados [ -2, -1 ] y [ 1, 2 ] (~13.59% cada uno)
  content(
    (sx(1.5), sy(0.05)),
    text(fill: rgb("#1e3a8a"), size: 8pt, weight: "semibold")[13.59%]
  )
  content(
    (sx(-1.5), sy(0.05)),
    text(fill: rgb("#1e3a8a"), size: 8pt, weight: "semibold")[13.59%]
  )
  
  // Extremos [ -3, -2 ] y [ 2, 3 ] (~2.14% cada uno)
  content(
    (sx(2.5), sy(0.018)),
    text(fill: rgb("#1e3a8a"), size: 7.5pt)[2.14%]
  )
  content(
    (sx(-2.5), sy(0.018)),
    text(fill: rgb("#1e3a8a"), size: 7.5pt)[2.14%]
  )
  
  // Colas externas [ x < -3 ] y [ x > 3 ] (~0.13% cada una)
  content(
    (sx(3.4), sy(0.008)),
    text(fill: rgb("#1e3a8a"), size: 6.5pt)[0.13%]
  )
  content(
    (sx(-3.4), sy(0.008)),
    text(fill: rgb("#1e3a8a"), size: 6.5pt)[0.13%]
  )
  
  // Anotación de la fórmula matemática en la esquina superior derecha
  rect(
    (sx(1.2), sy(0.28)),
    (sx(3.9), sy(0.42)),
    fill: rgb("#ffffffea"),
    stroke: 0.8pt + rgb("#cbd5e1"),
    radius: 3pt
  )
  content(
    (sx(2.55), sy(0.35)),
    [$f(x) = frac(1, sigma sqrt(2 pi)) e^(- frac(1, 2) (frac(x - mu, sigma))^2$],
    size: 9.5pt
  )
})
