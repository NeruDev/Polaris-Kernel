#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Escala general del gráfico
  // Multiplicaremos x por 1.2 e y por 0.8 para ajustar el aspecto
  let sx(x) = { x * 1.1 }
  let sy(y) = { y * 0.8 }
  
  // Rejilla de fondo horizontal (sutil)
  for y in (2, 4, 6, 8) {
    line(
      (sx(-0.5), sy(y)),
      (sx(10.5), sy(y)),
      stroke: 0.5pt + rgb("#e2e8f0")
    )
  }
  
  // Ejes cartesianos
  line(
    (sx(-0.5), sy(0)),
    (sx(11.0), sy(0)),
    mark: (end: ">"),
    stroke: 1.2pt + rgb("#475569")
  )
  line(
    (sx(0), sy(-0.2)),
    (sx(0), sy(9.0)),
    mark: (end: ">"),
    stroke: 1.2pt + rgb("#475569")
  )
  
  // Etiquetas de los ejes
  content((sx(11.2), sy(0)), [$x$], size: 11pt)
  content((sx(0), sy(9.3)), [$f(x)$], size: 11pt)
  
  // Datos del histograma (intervalo_min, intervalo_max, frecuencia)
  let bins = (
    (0, 1, 0.8),
    (1, 2, 2.5),
    (2, 3, 5.5),
    (3, 4, 7.2),
    (4, 5, 6.8),
    (5, 6, 5.0),
    (6, 7, 3.5),
    (7, 8, 2.0),
    (8, 9, 1.0),
    (9, 10, 0.5)
  )
  
  // Dibujar barras del histograma
  for (x_min, x_max, h) in bins {
    rect(
      (sx(x_min), sy(0)),
      (sx(x_max), sy(h)),
      fill: rgb("#3b82f633"), // Azul translúcido moderno
      stroke: 1pt + rgb("#2563eb") // Borde azul
    )
  }
  
  // Marcas en el eje X
  for x in range(0, 11) {
    line(
      (sx(x), sy(-0.1)),
      (sx(x), sy(0.1)),
      stroke: 1pt + rgb("#475569")
    )
    content(
      (sx(x), sy(-0.4)),
      text(fill: rgb("#475569"), size: 9pt)[#x]
    )
  }
  
  // Marcas en el eje Y
  for y in (2, 4, 6, 8) {
    line(
      (sx(-0.1), sy(y)),
      (sx(0.1), sy(y)),
      stroke: 1pt + rgb("#475569")
    )
    content(
      (sx(-0.4), sy(y)),
      text(fill: rgb("#475569"), size: 9pt)[#y]
    )
  }
  
  // Curva de densidad teórica ajustada (Normal Sesgada / Gamma aproximada)
  // f(x) = A * x^3 * e^(-0.8 * x)
  let density_pts = ()
  let steps = 100
  for i in range(0, steps + 1) {
    let x = float(i) * 10.0 / float(steps)
    // Evitar desbordamiento o valores raros en 0
    let y = 0.0
    if x > 0 {
      y = 2.85 * calc.pow(x, 3) * calc.exp(-0.8 * x)
    }
    density_pts.push((sx(x), sy(y)))
  }
  line(
    ..density_pts,
    stroke: 2.2pt + rgb("#ea580c"), // Naranja rojizo moderno
    name: "density"
  )
  
  // Líneas de tendencia central (Moda, Mediana, Media)
  // Moda = 3.75 (pico de la curva)
  // Mediana = 4.35
  // Media = 5.0
  
  let x_moda = 3.75
  let y_moda = 2.85 * calc.pow(x_moda, 3) * calc.exp(-0.8 * x_moda)
  
  let x_mediana = 4.35
  let y_mediana = 2.85 * calc.pow(x_mediana, 3) * calc.exp(-0.8 * x_mediana)
  
  let x_media = 5.0
  let y_media = 2.85 * calc.pow(x_media, 3) * calc.exp(-0.8 * x_media)
  
  // Moda (Línea discontinua verde)
  line(
    (sx(x_moda), sy(0)),
    (sx(x_moda), sy(y_moda)),
    stroke: (paint: rgb("#10b981"), thickness: 1.2pt, dash: "dashed")
  )
  
  // Mediana (Línea discontinua azul)
  line(
    (sx(x_mediana), sy(0)),
    (sx(x_mediana), sy(y_mediana)),
    stroke: (paint: rgb("#06b6d4"), thickness: 1.2pt, dash: "dashed")
  )
  
  // Media (Línea discontinua roja)
  line(
    (sx(x_media), sy(0)),
    (sx(x_media), sy(y_media)),
    stroke: (paint: rgb("#ef4444"), thickness: 1.2pt, dash: "dashed")
  )
  
  // Etiquetas sobre los ejes para las medidas (arriba de la curva)
  content(
    (sx(x_moda), sy(y_moda + 0.3)),
    text(fill: rgb("#047857"), size: 8pt, weight: "bold")[Moda]
  )
  content(
    (sx(x_mediana), sy(y_mediana + 0.6)),
    text(fill: rgb("#0e7490"), size: 8pt, weight: "bold")[Mediana]
  )
  content(
    (sx(x_media), sy(y_media + 0.9)),
    text(fill: rgb("#b91c1c"), size: 8pt, weight: "bold")[Media]
  )
  
  // Leyenda en la esquina superior derecha
  let lx = 7.5
  let ly = 6.0
  
  rect(
    (sx(lx), sy(ly)),
    (sx(lx + 3.0), sy(ly + 2.5)),
    fill: rgb("#ffffffea"),
    stroke: 0.8pt + rgb("#cbd5e1"),
    radius: 2pt
  )
  
  // Densidad
  line(
    (sx(lx + 0.3), sy(ly + 1.9)),
    (sx(lx + 0.9), sy(ly + 1.9)),
    stroke: 2pt + rgb("#ea580c")
  )
  content(
    (sx(lx + 1.1), sy(ly + 1.9)),
    text(size: 8pt, weight: "medium")[Densidad],
    anchor: "west"
  )
  
  // Moda
  line(
    (sx(lx + 0.3), sy(ly + 1.4)),
    (sx(lx + 0.9), sy(ly + 1.4)),
    stroke: (paint: rgb("#10b981"), thickness: 1.5pt, dash: "dashed")
  )
  content(
    (sx(lx + 1.1), sy(ly + 1.4)),
    text(size: 8pt)[Moda (Mo)],
    anchor: "west"
  )
  
  // Mediana
  line(
    (sx(lx + 0.3), sy(ly + 0.9)),
    (sx(lx + 0.9), sy(ly + 0.9)),
    stroke: (paint: rgb("#06b6d4"), thickness: 1.5pt, dash: "dashed")
  )
  content(
    (sx(lx + 1.1), sy(ly + 0.9)),
    text(size: 8pt)[Mediana (Me)],
    anchor: "west"
  )
  
  // Media
  line(
    (sx(lx + 0.3), sy(ly + 0.4)),
    (sx(lx + 0.9), sy(ly + 0.4)),
    stroke: (paint: rgb("#ef4444"), thickness: 1.5pt, dash: "dashed")
  )
  content(
    (sx(lx + 1.1), sy(ly + 0.4)),
    text(size: 8pt)[Media ($mu$)],
    anchor: "west"
  )
})
