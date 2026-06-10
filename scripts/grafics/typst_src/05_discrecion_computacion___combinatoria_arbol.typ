#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Nodo Raíz
  let n_root = (-3.5, 0.0)
  
  // Nodos Nivel 1
  let n_A = (-1.0, 1.5)
  let n_B = (-1.0, -1.5)
  
  // Nodos Nivel 2 (Hojas de A)
  let n_A1 = (1.8, 2.2)
  let n_A2 = (1.8, 1.5)
  let n_A3 = (1.8, 0.8)
  
  // Nodos Nivel 2 (Hojas de B)
  let n_B1 = (1.8, -0.8)
  let n_B2 = (1.8, -1.5)
  let n_B3 = (1.8, -2.2)
  
  // --- Dibujar Conexiones Nivel 0 -> Nivel 1 ---
  line(n_root, n_A, stroke: 1.2pt + rgb("#7f8c8d"))
  line(n_root, n_B, stroke: 1.2pt + rgb("#7f8c8d"))
  
  // --- Dibujar Conexiones Nivel 1 -> Nivel 2 ---
  line(n_A, n_A1, stroke: 1.0pt + rgb("#bdc3c7"))
  line(n_A, n_A2, stroke: 1.0pt + rgb("#bdc3c7"))
  line(n_A, n_A3, stroke: 1.0pt + rgb("#bdc3c7"))
  
  line(n_B, n_B1, stroke: 1.0pt + rgb("#bdc3c7"))
  line(n_B, n_B2, stroke: 1.0pt + rgb("#bdc3c7"))
  line(n_B, n_B3, stroke: 1.0pt + rgb("#bdc3c7"))
  
  // --- Etiquetas en las Conexiones ---
  content((-2.3, 0.95), [Paso 1: $A$], size: 8pt, fill: white)
  content((-2.3, -0.95), [Paso 1: $B$], size: 8pt, fill: white)
  
  content((0.4, 1.95), [Paso 2: $1$], size: 7pt, fill: white)
  content((0.4, 1.5), [Paso 2: $2$], size: 7pt, fill: white)
  content((0.4, 1.05), [Paso 2: $3$], size: 7pt, fill: white)
  
  content((0.4, -1.05), [Paso 2: $1$], size: 7pt, fill: white)
  content((0.4, -1.5), [Paso 2: $2$], size: 7pt, fill: white)
  content((0.4, -1.95), [Paso 2: $3$], size: 7pt, fill: white)
  
  // --- Dibujar Nodos Estilizados ---
  
  // Nodo Raíz (Inicio)
  rect((-4.4, -0.35), (-2.6, 0.35), radius: 3pt, fill: rgb("#2c3e50"), stroke: 1pt + rgb("#2c3e50"))
  content(n_root, [Inicio], size: 9pt, text-color: white)
  
  // Nodos Nivel 1 (A, B)
  circle(n_A, radius: 0.35, fill: rgb("#3498db").lighten(85%), stroke: 1.5pt + rgb("#3498db"))
  content(n_A, [$A$], size: 10pt)
  
  circle(n_B, radius: 0.35, fill: rgb("#3498db").lighten(85%), stroke: 1.5pt + rgb("#3498db"))
  content(n_B, [$B$], size: 10pt)
  
  // Nodos Nivel 2 (1, 2, 3)
  let draw_leaf(pos, label) = {
    circle(pos, radius: 0.25, fill: rgb("#27ae60").lighten(88%), stroke: 1.2pt + rgb("#27ae60"))
    content(pos, label, size: 9pt)
  }
  draw_leaf(n_A1, [$1$])
  draw_leaf(n_A2, [$2$])
  draw_leaf(n_A3, [$3$])
  
  draw_leaf(n_B1, [$1$])
  draw_leaf(n_B2, [$2$])
  draw_leaf(n_B3, [$3$])
  
  // --- Hojas de Resultados Finales ---
  let draw_result(pos, text) = {
    content((pos.at(0) + 1.2, pos.at(1)), text, size: 9pt, fill: rgb("#f8f9fa"))
  }
  draw_result(n_A1, [Resultado: $(A, 1)$])
  draw_result(n_A2, [Resultado: $(A, 2)$])
  draw_result(n_A3, [Resultado: $(A, 3)$])
  
  draw_result(n_B1, [Resultado: $(B, 1)$])
  draw_result(n_B2, [Resultado: $(B, 2)$])
  draw_result(n_B3, [Resultado: $(B, 3)$])
  
  // Leyenda del Principio Multiplicativo
  content((-1.0, -2.9), [
    $ text("Principio Multiplicativo: ") n_1 times n_2 = 2 times 3 = 6 " resultados" $
  ], size: 10pt)
})
