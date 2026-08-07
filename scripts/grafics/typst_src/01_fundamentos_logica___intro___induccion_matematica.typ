#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Dibujar el suelo sobre el que descansan las fichas
  line((-1, 0), (9, 0), stroke: 1.5pt + rgb("#bdc3c7"))
  
  // Ficha 1: Caso Base P(1) - Cayendo e iniciando la reaccion
  group({
    translate((0, 0))
    rotate(-25deg)
    rect((-0.2, 0), (0.2, 1.8), fill: rgb("#39C5BB"), stroke: 1pt + rgb("#2c3e50"), radius: 1pt)
  })
  
  // Flecha de fuerza inicial (Base de la Induccion)
  line((-1.2, 1.2), (-0.4, 0.9), mark: (end: ">"), stroke: 1.5pt + rgb("#e67e22"))
  content((-1.5, 1.4), [Base P(1)], size: 8pt)

  // Ficha 2: P(2) - Inclinada por el empuje
  group({
    translate((1.0, 0))
    rotate(-15deg)
    rect((-0.2, 0), (0.2, 1.8), fill: rgb("#39C5BB"), stroke: 1.5pt + rgb("#2c3e50"), radius: 1pt)
  })

  // Ficha 3: P(3) - Levemente inclinada
  group({
    translate((2.0, 0))
    rotate(-5deg)
    rect((-0.2, 0), (0.2, 1.8), fill: rgb("#39C5BB"), stroke: 1.5pt + rgb("#2c3e50"), radius: 1pt)
  })

  // Puntos suspensivos (Representando el paso de transicion intermedia)
  content((3.3, 0.9), [...], size: 14pt)

  // Ficha k: Hipotesis Inductiva P(k)
  group({
    translate((4.8, 0))
    rotate(-12deg)
    rect((-0.2, 0), (0.2, 1.8), fill: rgb("#3498db"), stroke: 1.5pt + rgb("#2c3e50"), radius: 1pt)
  })

  // Ficha k+1: Tesis Inductiva P(k+1) - A punto de ser golpeada
  group({
    translate((5.8, 0))
    rotate(0deg)
    rect((-0.2, 0), (0.2, 1.8), fill: rgb("#e74c3c"), stroke: 1.5pt + rgb("#2c3e50"), radius: 1pt)
  })
  
  // Ficha k+2: Fichas subsiguientes en reposo
  group({
    translate((6.8, 0))
    rotate(0deg)
    rect((-0.2, 0), (0.2, 1.8), fill: rgb("#95a5a6"), stroke: 1.5pt + rgb("#7f8c8d"), radius: 1pt)
  })

  // Etiquetas de la base de datos de los pasos
  content((0.0, -0.3), [P(1)], size: 9pt)
  content((0.9, -0.3), [P(2)], size: 9pt)
  content((1.9, -0.3), [P(3)], size: 9pt)
  content((4.7, -0.3), [P(k)], size: 9pt)
  content((5.8, -0.3), [P(k+1)], size: 9pt)

  // Arco y texto indicando el paso inductivo P(k) => P(k+1)
  content((5.25, 2.3), [Paso inductivo: P(k) => P(k+1)], size: 8pt)
  line((4.7, 2.0), (5.8, 2.0), mark: (end: ">"), stroke: 1pt + rgb("#34495e"))
})
