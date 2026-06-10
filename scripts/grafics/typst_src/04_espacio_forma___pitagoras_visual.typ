#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Coordenadas del triángulo rectángulo
  let pA = (0, 3)  // Vértice superior
  let pB = (0, 0)  // Vértice ángulo recto
  let pC = (4, 0)  // Vértice derecho
  
  // Coordenadas del cuadrado A (sobre lado vertical a = 3)
  let sqA_1 = (0, 0)
  let sqA_2 = (-3, 0)
  let sqA_3 = (-3, 3)
  let sqA_4 = (0, 3)
  
  // Coordenadas del cuadrado B (sobre lado horizontal b = 4)
  let sqB_1 = (0, 0)
  let sqB_2 = (0, -4)
  let sqB_3 = (4, -4)
  let sqB_4 = (4, 0)
  
  // Coordenadas del cuadrado C (sobre hipotenusa c = 5)
  let sqC_1 = (4, 0)
  let sqC_2 = (0, 3)
  let sqC_3 = (3, 7)
  let sqC_4 = (7, 4)
  
  // Dibujar Cuadrado A (a^2)
  line(sqA_1, sqA_2, sqA_3, sqA_4, close: true,
    fill: rgb("#39C5BB").lighten(85%),
    stroke: 1.5pt + rgb("#39C5BB")
  )
  content((-1.5, 1.5), [$a^2$], size: 12pt)
  
  // Dibujar Cuadrado B (b^2)
  line(sqB_1, sqB_2, sqB_3, sqB_4, close: true,
    fill: rgb("#3498db").lighten(85%),
    stroke: 1.5pt + rgb("#3498db")
  )
  content((2, -2), [$b^2$], size: 12pt)
  
  // Dibujar Cuadrado C (c^2)
  line(sqC_1, sqC_2, sqC_3, sqC_4, close: true,
    fill: rgb("#e74c3c").lighten(85%),
    stroke: 1.5pt + rgb("#e74c3c")
  )
  content((3.5, 3.5), [$c^2$], size: 14pt)
  
  // Dibujar Triángulo Central (relleno suave para contraste)
  line(pA, pB, pC, close: true,
    fill: rgb("#2c3e50").lighten(90%),
    stroke: 1.5pt + rgb("#2c3e50")
  )
  
  // Símbolo de Ángulo Recto
  line((0.3, 0), (0.3, 0.3), (0, 0.3), stroke: 1pt + rgb("#7f8c8d"))
  
  // Etiquetas de los lados
  content((0.2, 1.5), [$a$], size: 10pt)
  content((2, 0.25), [$b$], size: 10pt)
  content((1.8, 1.7), [$c$], size: 10pt)
  
  // Fórmula del Teorema de Pitágoras
  content((5.5, -2), [
    $a^2 + b^2 = c^2$
  ], size: 14pt)
})
