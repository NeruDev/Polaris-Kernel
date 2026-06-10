#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Escala general del gráfico
  // Ajustaremos las posiciones para dar espacio al grafo a la izquierda y la matriz a la derecha
  
  // --- GRAFO DE TRANSICIÓN DE ESTADOS ---
  
  // Definición de las posiciones de los nodos (Estados)
  let s1 = (0.0, 1.6)   // S1: Alza
  let s2 = (-2.0, -1.0) // S2: Estable
  let s3 = (2.0, -1.0)  // S3: Baja
  let r_node = 0.45     // Radio de los nodos
  
  // 1. Bucles Propios (Transición a sí mismo)
  
  // Bucle S1 (arriba)
  // Arco centrado en (0, 2.3) con radio 0.35
  arc((0.0, 2.3), start: -60deg, stop: 240deg, radius: 0.35, mark: (end: ">"), stroke: 1.2pt + rgb("#3b82f6"))
  content((0.0, 2.8), [$0.6$], size: 9pt)
  
  // Bucle S2 (izquierda)
  // Arco centrado en (-2.7, -1.0) con radio 0.35
  arc((-2.7, -1.0), start: 30deg, stop: 330deg, radius: 0.35, mark: (end: ">"), stroke: 1.2pt + rgb("#22c55e"))
  content((-3.2, -1.0), [$0.5$], size: 9pt)
  
  // Bucle S3 (derecha)
  // Arco centrado en (2.7, -1.0) con radio 0.35
  arc((2.7, -1.0), start: 150deg, stop: 450deg, radius: 0.35, mark: (end: ">"), stroke: 1.2pt + rgb("#ef4444"))
  content((3.2, -1.0), [$0.4$], size: 9pt)
  
  // 2. Aristas de Transición (Curvas Bézier con flechas)
  
  // Transición S1 -> S2 (Curva izquierda exterior)
  bezier(
    (-0.27, 1.24),  // Inicio en S1
    (-1.85, -0.6),  // Fin en S2
    (-1.0, 1.0),    // Control 1
    (-1.8, 0.2),    // Control 2
    mark: (end: ">"),
    stroke: 1.2pt + rgb("#64748b")
  )
  content((-1.5, 0.6), [$0.3$], size: 9pt, fill: white)
  
  // Transición S2 -> S1 (Curva derecha interior)
  bezier(
    (-1.6, -0.75),  // Inicio en S2
    (-0.1, 1.15),   // Fin en S1
    (-1.0, -0.2),   // Control 1
    (-0.4, 0.5),    // Control 2
    mark: (end: ">"),
    stroke: 1.2pt + rgb("#64748b")
  )
  content((-0.5, 0.1), [$0.2$], size: 9pt, fill: white)
  
  // Transición S2 -> S3 (Curva inferior exterior)
  bezier(
    (-1.55, -1.1),  // Inicio en S2
    (1.55, -1.1),   // Fin en S3
    (-0.8, -1.6),   // Control 1
    (0.8, -1.6),    // Control 2
    mark: (end: ">"),
    stroke: 1.2pt + rgb("#64748b")
  )
  content((0.0, -1.6), [$0.3$], size: 9pt, fill: white)
  
  // Transición S3 -> S2 (Curva superior interior)
  bezier(
    (1.55, -0.9),   // Inicio en S3
    (-1.55, -0.9),  // Fin en S2
    (0.8, -0.4),    // Control 1
    (-0.8, -0.4),   // Control 2
    mark: (end: ">"),
    stroke: 1.2pt + rgb("#64748b")
  )
  content((0.0, -0.25), [$0.4$], size: 9pt, fill: white)
  
  // Transición S3 -> S1 (Curva derecha exterior)
  bezier(
    (1.85, -0.6),   // Inicio en S3
    (0.27, 1.24),   // Fin en S1
    (1.8, 0.2),     // Control 1
    (1.0, 1.0),     // Control 2
    mark: (end: ">"),
    stroke: 1.2pt + rgb("#64748b")
  )
  content((1.5, 0.6), [$0.2$], size: 9pt, fill: white)
  
  // Transición S1 -> S3 (Curva izquierda interior)
  bezier(
    (0.1, 1.15),    // Inicio en S1
    (1.6, -0.75),   // Fin en S3
    (0.4, 0.5),     // Control 1
    (1.0, -0.2),    // Control 2
    mark: (end: ">"),
    stroke: 1.2pt + rgb("#64748b")
  )
  content((0.5, 0.1), [$0.1$], size: 9pt, fill: white)
  
  // 3. Dibujar los Nodos de Estados (Superpuestos para tapar las aristas que entran)
  
  // S1: Alza (Bullish)
  circle(s1, radius: r_node, fill: rgb("#eff6ff"), stroke: 2pt + rgb("#3b82f6"))
  content(s1, [
    #text(weight: "bold", size: 10pt, fill: rgb("#1e3a8a"))[$S_1$] \
    #text(size: 7.5pt, fill: rgb("#1e40af"))[Alza]
  ])
  
  // S2: Estable (Flat)
  circle(s2, radius: r_node, fill: rgb("#f0fdf4"), stroke: 2pt + rgb("#22c55e"))
  content(s2, [
    #text(weight: "bold", size: 10pt, fill: rgb("#166534"))[$S_2$] \
    #text(size: 7.5pt, fill: rgb("#15803d"))[Estable]
  ])
  
  // S3: Baja (Bearish)
  circle(s3, radius: r_node, fill: rgb("#fef2f2"), stroke: 2pt + rgb("#ef4444"))
  content(s3, [
    #text(weight: "bold", size: 10pt, fill: rgb("#991b1b"))[$S_3$] \
    #text(size: 7.5pt, fill: rgb("#b91c1c"))[Baja]
  ])
  
  // --- REPRESENTACIÓN MATRICIAL (LADO DERECHO) ---
  
  // Caja contenedora de la matriz
  rect(
    (4.0, -1.9),
    (7.8, 2.2),
    fill: rgb("#f8fafc"),
    stroke: 0.8pt + rgb("#e2e8f0"),
    radius: 4pt
  )
  
  // Título e información
  content((5.9, 1.7), text(weight: "bold", fill: rgb("#334155"), size: 10.5pt)[Matriz de Transición], anchor: "center")
  
  // Escribir la matriz de probabilidades
  content(
    (5.9, 0.0),
    [$P = mat(
      0.6, 0.3, 0.1;
      0.2, 0.5, 0.3;
      0.2, 0.4, 0.4
    )$],
    size: 13pt
  )
  
  // Glosario o detalles matemáticos
  content(
    (5.9, -1.3),
    [
      #set text(size: 7.5pt, fill: rgb("#64748b"))
      $P_(i j) = P(X_(t+1) = S_j | X_t = S_i)$ \
      Suma de cada fila $= 1.0$
    ],
    anchor: "center"
  )
})
