#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Definición del origen
  let origin = (0, 0)
  
  // Definición del paralelogramo para el plano M (Subespacio cerrado)
  let pA = (-3.2, -1.2)
  let pB = (1.5, -0.9)
  let pC = (3.5, 0.8)
  let pD = (-1.2, 0.5)
  
  // Dibujar el plano M
  line(pA, pB, pC, pD, close: true,
    fill: rgb("#3498db").lighten(88%), 
    stroke: 1.5pt + rgb("#2980b9")
  )
  
  // Etiqueta del subespacio M
  content((2.8, 0.3), [$M$], size: 10pt)
  
  // Vector de proyección p = P_M(f) sobre el plano M
  let p_proj = (1.8, 0.1)
  line(origin, p_proj, mark: (end: ">"), stroke: 1.8pt + rgb("#27ae60"), name: "p")
  content((1.0, -0.25), [$p = P_M(f)$], size: 9pt)
  
  // Vector f (fuera del plano M)
  let f_vec = (1.8, 2.3)
  line(origin, f_vec, mark: (end: ">"), stroke: 2pt + rgb("#2c3e50"), name: "f")
  content((0.7, 1.4), [$f$], size: 10pt)
  
  // Vector de error f - p (perpendicular a M)
  line(p_proj, f_vec, stroke: (paint: rgb("#e74c3c"), thickness: 1.5pt, dash: "dashed"), name: "err")
  content((2.4, 1.2), [$f - P_M(f)$], size: 9pt)
  
  // Símbolo de ángulo recto en perspectiva
  let d = 0.18
  let length_p = calc.sqrt(1.8 * 1.8 + 0.1 * 0.1)
  let norm_p_x = 1.8 / length_p
  let norm_p_y = 0.1 / length_p
  
  let p1 = (p_proj.at(0) - d * norm_p_x, p_proj.at(1) - d * norm_p_y)
  let p2 = (p1.at(0), p1.at(1) + d)
  let p3 = (p_proj.at(0), p_proj.at(1) + d)
  
  line(p1, p2, p3, stroke: 1pt + rgb("#7f8c8d"))
  
  // Otro vector genérico w en M
  let w_vec = (-1.5, -0.6)
  line(origin, w_vec, mark: (end: ">"), stroke: 1.2pt + rgb("#7f8c8d"), name: "w")
  content((-1.2, -0.85), [$w$], size: 9pt)
  
  // Distancia de f a w (hipotenusa)
  line(w_vec, f_vec, stroke: (paint: rgb("#95a5a6"), thickness: 1pt, dash: "dotted"))
  
  // Etiqueta del Espacio de Hilbert completo
  content((-2.8, 2.0), [$cal(H)$], size: 12pt)
  
  // Nota matemática / Teorema de la mejor aproximación
  content((-1.6, 1.6), [
    $ (f - P_M (f)) perp M $
    $ ||f - P_M (f)|| < ||f - w|| $
    $ forall w != P_M (f) $
  ], size: 8pt)
})
