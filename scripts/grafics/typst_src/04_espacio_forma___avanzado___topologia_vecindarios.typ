#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Marco del Espacio Topológico X
  rect((-3.8, -2.2), (3.8, 2.2), stroke: 1pt + rgb("#7f8c8d"), fill: none)
  content((3.5, 1.9), [$X$], size: 11pt)
  
  // Conjunto A (Elipse centrada en (-0.5, 0))
  let o_a = (-0.5, 0.0)
  circle(o_a, radius: (2.2, 1.3), stroke: 1.5pt + rgb("#3498db"), fill: rgb("#3498db").lighten(92%))
  content((-2.2, 0.8), [$A$], size: 12pt)
  
  // --- Punto Interior (x) ---
  let pt_x = (-1.4, 0.2)
  circle(pt_x, radius: 2.2pt, fill: rgb("#27ae60"), stroke: 0.5pt + white)
  // Vecindario Ux completamente dentro de A (radio = 0.5)
  circle(pt_x, radius: 0.5, stroke: (paint: rgb("#27ae60"), thickness: 0.8pt, dash: "dashed"))
  content((pt_x.at(0), pt_x.at(1) + 0.15), [$x$], size: 9pt)
  content((pt_x.at(0), pt_x.at(1) - 0.75), [$U_x subset A$], size: 8pt)
  
  // --- Punto Frontera (y) ---
  // El extremo derecho de la elipse está en (-0.5 + 2.2, 0) = (1.7, 0)
  let pt_y = (1.7, 0.0)
  circle(pt_y, radius: 2.2pt, fill: rgb("#e67e22"), stroke: 0.5pt + white)
  // Vecindario Uy contiene puntos dentro y fuera (radio = 0.5)
  circle(pt_y, radius: 0.5, stroke: (paint: rgb("#e67e22"), thickness: 0.8pt, dash: "dashed"))
  content((pt_y.at(0) + 0.15, pt_y.at(1) + 0.18), [$y$], size: 9pt)
  content((pt_y.at(0) + 0.4, pt_y.at(1) - 0.7), [
    $U_y sect A != emptyset$ \
    $U_y sect A^c != emptyset$
  ], size: 7.5pt)
  
  // --- Punto Exterior (z) ---
  let pt_z = (2.4, 1.2)
  circle(pt_z, radius: 2.2pt, fill: rgb("#e74c3c"), stroke: 0.5pt + white)
  // Vecindario Uz completamente fuera de A (radio = 0.4)
  circle(pt_z, radius: 0.4, stroke: (paint: rgb("#e74c3c"), thickness: 0.8pt, dash: "dashed"))
  content((pt_z.at(0), pt_z.at(1) + 0.15), [$z$], size: 9pt)
  content((pt_z.at(0), pt_z.at(1) - 0.65), [$U_z subset A^c$], size: 8pt)
  
  // Leyenda en la esquina inferior izquierda
  content((-2.3, -1.5), [
    $x in "Int"(A)$ (Punto interior) \
    $y in partial A$ (Punto frontera) \
    $z in "Ext"(A)$ (Punto exterior)
  ], size: 8pt)
})
