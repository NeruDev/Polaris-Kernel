#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Coordenadas de los vértices
  let v1 = (0.0, 1.8)
  let v2 = (-2.0, 0.3)
  let v3 = (-1.2, -1.5)
  let v4 = (1.2, -1.5)
  let v5 = (2.0, 0.3)
  
  // --- Dibujar Aristas (Edges) ---
  
  // Aristas normales (no dirigidas)
  line(v1, v2, stroke: 1.5pt + rgb("#2c3e50"))
  line(v2, v3, stroke: 1.5pt + rgb("#2c3e50"))
  line(v5, v1, stroke: 1.5pt + rgb("#2c3e50"))
  
  // Arista ponderada (v3 a v4)
  line(v3, v4, stroke: 1.5pt + rgb("#2c3e50"), name: "e_pond")
  content((0.0, -1.5), [$w = 7$], size: 8pt, fill: white)
  
  // Arista dirigida (v4 a v5)
  line(v4, v5, mark: (end: ">"), stroke: 1.5pt + rgb("#2c3e50"))
  content((1.8, -0.6), [$e_4$], size: 8pt, fill: white)
  
  // Camino resaltado (v1 a v3 a v5) en color rojo/coral
  line(v1, v3, stroke: 2.2pt + rgb("#e74c3c"), name: "e_cam1")
  line(v3, v5, stroke: 2.2pt + rgb("#e74c3c"), name: "e_cam2")
  
  // Arista central diagonal
  line(v2, v5, stroke: 1.2pt + rgb("#bdc3c7"))
  
  // --- Dibujar Vértices (Vertices) ---
  let draw_node(pos, label) = {
    circle(pos, radius: 0.38, fill: rgb("#3498db").lighten(85%), stroke: 1.8pt + rgb("#3498db"))
    content(pos, label, size: 10pt)
  }
  
  draw_node(v1, [$v_1$])
  draw_node(v2, [$v_2$])
  draw_node(v3, [$v_3$])
  draw_node(v4, [$v_4$])
  draw_node(v5, [$v_5$])
  
  // Leyenda o información del Grafo G = (V, E)
  content((-3.0, -2.4), [
    $G = (V, E)$ \
    $V = {v_1, v_2, v_3, v_4, v_5\}$ \
    $E = {e_1, e_2, e_3, e_4, e_5, e_6, e_7\}$
  ], size: 8.5pt)
  
  // Nota sobre el camino resaltado
  content((2.8, -2.4), [
    $text("Camino resaltado: ") v_1 -> v_3 -> v_5$ \
    $text("Arista con peso: ") w(e_3) = 7$ \
    $text("Arista dirigida: ") e_4 = (v_4, v_5)$
  ], size: 8.5pt)
})
