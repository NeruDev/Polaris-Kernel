#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Ejes de proyección 3D a 2D
  let px = (1.5, -0.35)
  let py = (-0.9, -0.55)
  let pz = (0.0, 1.3)
  
  // Función de proyección
  let proj(u, v, w) = (
    u * px.at(0) + v * py.at(0) + w * pz.at(0),
    u * px.at(1) + v * py.at(1) + w * pz.at(1)
  )
  
  // Definimos la superficie z(u, v) = -0.12 * (u^2 + v^2)
  // Dibujamos la malla de la superficie (wireframe)
  let grid_steps = 8
  let min_val = -1.5
  let max_val = 1.5
  
  // Dibujamos líneas de u constante (variando v)
  for i in range(0, grid_steps + 1) {
    let u = min_val + (max_val - min_val) * float(i) / float(grid_steps)
    let pts = ()
    for j in range(0, 21) {
      let v = min_val + (max_val - min_val) * float(j) / 20.0
      let w = -0.12 * (u*u + v*v)
      pts.push(proj(u, v, w))
    }
    line(..pts, stroke: 0.6pt + rgb("#bdc3c7"))
  }
  
  // Dibujamos líneas de v constante (variando u)
  for j in range(0, grid_steps + 1) {
    let v = min_val + (max_val - min_val) * float(j) / float(grid_steps)
    let pts = ()
    for i in range(0, 21) {
      let u = min_val + (max_val - min_val) * float(i) / 20.0
      let w = -0.12 * (u*u + v*v)
      pts.push(proj(u, v, w))
    }
    line(..pts, stroke: 0.6pt + rgb("#bdc3c7"))
  }
  
  // Punto de tangencia p en (0, 0, 0)
  let p_zero = proj(0, 0, 0)
  
  // Dibujamos el plano tangente (en w = 0)
  let pt_size = 1.2
  let v1 = proj(-pt_size, -pt_size, 0)
  let v2 = proj(pt_size, -pt_size, 0)
  let v3 = proj(pt_size, pt_size, 0)
  let v4 = proj(-pt_size, pt_size, 0)
  
  line(v1, v2, v3, v4, close: true, 
    fill: rgb("#e67e22").lighten(85%), 
    stroke: 1.5pt + rgb("#d35400")
  )
  
  // Vectores tangentes en el plano
  let t_u = proj(0.8, 0, 0)
  let t_v = proj(0, 0.8, 0)
  line(p_zero, t_u, mark: (end: ">"), stroke: 1.5pt + rgb("#2980b9"))
  line(p_zero, t_v, mark: (end: ">"), stroke: 1.5pt + rgb("#27ae60"))
  content((t_u.at(0) + 0.15, t_u.at(1) - 0.1), [$v_1$], size: 8pt)
  content((t_v.at(0) - 0.15, t_v.at(1) - 0.1), [$v_2$], size: 8pt)
  
  // Vector normal n
  let normal = proj(0, 0, 1.2)
  line(p_zero, normal, mark: (end: ">"), stroke: 1.8pt + rgb("#e74c3c"))
  content((normal.at(0) + 0.22, normal.at(1)), [$arrow(n)$], size: 9pt)
  
  // Punto p
  circle(p_zero, radius: 2.2pt, fill: rgb("#2c3e50"))
  content((p_zero.at(0) - 0.2, p_zero.at(1) + 0.15), [$p$], size: 9pt)
  
  // Etiquetas generales
  content((v3.at(0) + 0.4, v3.at(1) + 0.2), [$T_p M$], size: 10pt)
  let p_m = proj(-1.4, -1.4, -0.12 * 2.88)
  content((p_m.at(0), p_m.at(1) - 0.35), [$M$], size: 11pt)
})
