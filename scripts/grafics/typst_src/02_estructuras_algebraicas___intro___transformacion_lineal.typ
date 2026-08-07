#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *
  
  // ---------------------------------------------------------------------------
  // 1. ESPACIO ORIGINAL (DOMINIO V)
  // ---------------------------------------------------------------------------
  group({
    translate((0, 0))
    
    // Cuadrícula de fondo
    for x in range(-2, 3) {
      line((x, -2), (x, 2), stroke: 0.5pt + rgb("#e0e0e0"))
    }
    for y in range(-2, 3) {
      line((-2, y), (2, y), stroke: 0.5pt + rgb("#e0e0e0"))
    }
    
    // Ejes cartesianos
    line((-2.2, 0), (2.2, 0), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
    line((0, -2.2), (0, 2.2), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
    content((2.4, 0), [$x$], size: 8pt)
    content((0, 2.4), [$y$], size: 8pt)
    
    // Área unitaria original (cuadrado)
    rect((0, 0), (1, 1), fill: rgb("#39C5BB").lighten(70%), stroke: 0.5pt + rgb("#39C5BB").darken(20%))
    
    // Vectores base canónicos
    line((0, 0), (1, 0), mark: (end: ">"), stroke: 1.8pt + rgb("#3498db")) // e_1
    line((0, 0), (0, 1), mark: (end: ">"), stroke: 1.8pt + rgb("#e74c3c")) // e_2
    
    // Etiquetas de los vectores base
    content((0.5, -0.3), [$e_1$], size: 9pt)
    content((-0.3, 0.5), [$e_2$], size: 9pt)
    
    content((0, -2.6), [Espacio Original $V$ (Dominio)], size: 10pt)
  })
  
  // ---------------------------------------------------------------------------
  // ARCO / FLECHA DE TRANSFORMACIÓN LINEAL
  // ---------------------------------------------------------------------------
  group({
    translate((3.0, 0))
    line((0, 0.2), (1.6, 0.2), mark: (end: ">"), stroke: 2pt + rgb("#7f8c8d"))
    content((0.8, 0.7), [$T(x) = A x$], size: 9pt)
    content((0.8, -0.6), [$A = mat(1, 1; 0, 1)$], size: 8pt)
  })

  // ---------------------------------------------------------------------------
  // 2. ESPACIO TRANSFORMADO (CODOMINIO W)
  // ---------------------------------------------------------------------------
  group({
    translate((6.5, 0))
    
    // Cuadrícula transformada (cizallada: x' = x + y, y' = y)
    // Líneas horizontales (siguen siendo y = c)
    for y in range(-2, 3) {
      line((-2 + y, y), (2 + y, y), stroke: 0.5pt + rgb("#e0e0e0"))
    }
    // Líneas verticales (se inclinan: x' = c + y)
    for x in range(-2, 3) {
      line((x - 2, -2), (x + 2, 2), stroke: 0.5pt + rgb("#e0e0e0"))
    }
    
    // Ejes cartesianos transformados
    line((-2.2, 0), (2.2, 0), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
    line((0, -2.2), (0, 2.2), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
    content((2.4, 0), [$x'$], size: 8pt)
    content((0, 2.4), [$y'$], size: 8pt)
    
    // Área unitaria transformada (paralelogramo)
    line((0, 0), (1, 0), (2, 1), (1, 1), close: true, fill: rgb("#39C5BB").lighten(70%), stroke: 0.5pt + rgb("#39C5BB").darken(20%))
    
    // Vectores transformados T(e_1) y T(e_2)
    line((0, 0), (1, 0), mark: (end: ">"), stroke: 1.8pt + rgb("#3498db")) // T(e_1) = (1, 0)
    line((0, 0), (1, 1), mark: (end: ">"), stroke: 1.8pt + rgb("#e74c3c")) // T(e_2) = (1, 1)
    
    // Etiquetas de los vectores transformados
    content((0.5, -0.3), [$T(e_1)$], size: 9pt)
    content((0.6, 0.9), [$T(e_2)$], size: 9pt)
    
    content((0.8, -2.6), [Espacio Transformado $W$], size: 10pt)
  })
})
