#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // ==========================================
  // LADO IZQUIERDO: ELIPSE (Centro en x = -3)
  // ==========================================
  
  let o1 = (-3.0, 0.0)
  
  // Ejes cartesianos locales
  line((-5.2, 0), (-0.8, 0), mark: (end: ">"), stroke: 0.8pt + rgb("#7f8c8d"))
  line((-3, -2.0), (-3, 2.0), mark: (end: ">"), stroke: 0.8pt + rgb("#7f8c8d"))
  content((-0.6, 0), [$x$], size: 9pt)
  content((-3, 2.2), [$y$], size: 9pt)
  
  // Dibujar Elipse (a = 1.8, b = 1.1)
  circle(o1, radius: (1.8, 1.1), stroke: 1.8pt + rgb("#3498db"), fill: rgb("#3498db").lighten(92%))
  
  // Semiejes indicados
  line(o1, (-1.2, 0), stroke: 1.2pt + rgb("#2c3e50"))
  content((-2.1, 0.25), [$a$], size: 9pt)
  line(o1, (-3, 1.1), stroke: 1.2pt + rgb("#2c3e50"))
  content((-3.25, 0.55), [$b$], size: 9pt)
  
  // Focos de la elipse
  // c = sqrt(1.8^2 - 1.1^2) = sqrt(3.24 - 1.21) = sqrt(2.03) ≈ 1.42
  let c_val = 1.4248
  circle((-3.0 - c_val, 0), radius: 2.2pt, fill: rgb("#e74c3c"), stroke: 0.5pt + white)
  circle((-3.0 + c_val, 0), radius: 2.2pt, fill: rgb("#e74c3c"), stroke: 0.5pt + white)
  content((-3.0 - c_val, -0.3), [$F_1$], size: 8pt)
  content((-3.0 + c_val, -0.3), [$F_2$], size: 8pt)
  
  // Centro
  circle(o1, radius: 1.8pt, fill: rgb("#2c3e50"))
  
  // Ecuación de la Elipse
  content((-3.0, -2.4), [$frac(x^2, a^2) + frac(y^2, b^2) = 1$], size: 11pt)
  content((-3.0, 2.7), [Elipse], size: 12pt, name: "title_elipse")
  
  // ==========================================
  // LADO DERECHO: PARÁBOLA (Centro en x = 3)
  // ==========================================
  
  let o2 = (3.0, 0.0)
  
  // Ejes cartesianos locales
  line((0.8, 0), (5.2, 0), mark: (end: ">"), stroke: 0.8pt + rgb("#7f8c8d"))
  line((3, -2.0), (3, 2.0), mark: (end: ">"), stroke: 0.8pt + rgb("#7f8c8d"))
  content((5.4, 0), [$x$], size: 9pt)
  content((3, 2.2), [$y$], size: 9pt)
  
  // Curva de la Parábola y = 0.5*x^2 - 0.8
  let para_pts = ()
  for i in range(-18, 19) {
    let xl = float(i) * 0.1
    let yl = 0.5 * xl * xl - 0.8
    para_pts.push((3.0 + xl, yl))
  }
  line(..para_pts, stroke: 1.8pt + rgb("#27ae60"))
  
  // Vértice V(0, -0.8) local -> (3, -0.8) global
  circle((3.0, -0.8), radius: 2.2pt, fill: rgb("#2c3e50"))
  content((3.3, -0.9), [$V$], size: 8pt)
  
  // Foco F(0, -0.3) local -> (3, -0.3) global (dado que p = 1/(4*0.5) = 0.5)
  circle((3.0, -0.3), radius: 2.2pt, fill: rgb("#e74c3c"), stroke: 0.5pt + white)
  content((3.3, -0.25), [$F$], size: 8pt)
  
  // Directriz y = -1.3 local -> y = -1.3 global
  line((1.2, -1.3), (4.8, -1.3), stroke: (paint: rgb("#e67e22"), thickness: 1.2pt, dash: "dashed"))
  content((4.2, -1.55), [Directriz], size: 8pt)
  
  // Ecuación de la Parábola
  content((3.0, -2.4), [$x^2 = 4p y$], size: 11pt)
  content((3.0, 2.7), [Parábola], size: 12pt, name: "title_parabola")
})
