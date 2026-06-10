#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Ejes de proyección 3D a 2D
  let px = (1.4, -0.3)
  let py = (-0.8, -0.5)
  let pz = (0.0, 1.2)
  
  // Función de proyección
  let proj(u, v, w) = (
    u * px.at(0) + v * py.at(0) + w * pz.at(0),
    u * px.at(1) + v * py.at(1) + w * pz.at(1)
  )
  
  let R = 1.6
  let c = 0.22
  let z_min = -1.0
  let t_max = 9.0
  let z_max = c * t_max - 1.0
  
  // --- Cilindro de Referencia (Trazos finos para profundidad) ---
  let base_inf = ()
  for i in range(0, 41) {
    let t = float(i) * 2.0 * calc.pi / 40.0
    base_inf.push(proj(R * calc.cos(t), R * calc.sin(t), z_min))
  }
  line(..base_inf, stroke: (paint: rgb("#bdc3c7"), thickness: 0.6pt, dash: "dashed"))
  
  let base_sup = ()
  for i in range(0, 41) {
    let t = float(i) * 2.0 * calc.pi / 40.0
    base_sup.push(proj(R * calc.cos(t), R * calc.sin(t), z_max))
  }
  line(..base_sup, stroke: (paint: rgb("#bdc3c7"), thickness: 0.6pt, dash: "dashed"))
  
  // Generatrices del cilindro
  line(proj(R, 0, z_min), proj(R, 0, z_max), stroke: (paint: rgb("#bdc3c7"), thickness: 0.6pt, dash: "dashed"))
  line(proj(-R, 0, z_min), proj(-R, 0, z_max), stroke: (paint: rgb("#bdc3c7"), thickness: 0.6pt, dash: "dashed"))
  
  // --- Curva Hélice 3D ---
  let helice_pts = ()
  let n_points = 80
  for i in range(0, n_points + 1) {
    let t = t_max * float(i) / float(n_points)
    let x = R * calc.cos(t)
    let y = R * calc.sin(t)
    let z = c * t - 1.0
    helice_pts.push(proj(x, y, z))
  }
  line(..helice_pts, stroke: 1.8pt + rgb("#2c3e50"))
  
  // --- Cálculo del Triedro de Frenet en t0 ---
  let t0 = 4.4 // Punto visible de la hélice
  let p_x = R * calc.cos(t0)
  let p_y = R * calc.sin(t0)
  let p_z = c * t0 - 1.0
  let p_pos = proj(p_x, p_y, p_z)
  
  // Vector Tangente T
  let tx = -R * calc.sin(t0)
  let ty = R * calc.cos(t0)
  let tz = c
  let t_len = calc.sqrt(tx*tx + ty*ty + tz*tz)
  let Tx = tx / t_len
  let Ty = ty / t_len
  let Tz = tz / t_len
  let T_pos = proj(p_x + Tx * 1.1, p_y + Ty * 1.1, p_z + Tz * 1.1)
  
  // Vector Normal N (apunta hacia el eje z del cilindro)
  let Nx = -calc.cos(t0)
  let Ny = -calc.sin(t0)
  let Nz = 0.0
  let N_pos = proj(p_x + Nx * 1.1, p_y + Ny * 1.1, p_z + Nz * 1.1)
  
  // Vector Binormal B (T x N)
  let Bx = -Tz * Ny
  let By = Tz * Nx
  let Bz = Tx * Ny - Ty * Nx
  let b_len = calc.sqrt(Bx*Bx + By*By + Bz*Bz)
  let Bx_u = Bx / b_len
  let By_u = By / b_len
  let Bz_u = Bz / b_len
  let B_pos = proj(p_x + Bx_u * 1.1, p_y + By_u * 1.1, p_z + Bz_u * 1.1)
  
  // Dibujar vectores del Triedro
  line(p_pos, T_pos, mark: (end: ">"), stroke: 2pt + rgb("#27ae60")) // Tangente T
  line(p_pos, N_pos, mark: (end: ">"), stroke: 2pt + rgb("#3498db")) // Normal N
  line(p_pos, B_pos, mark: (end: ">"), stroke: 2pt + rgb("#e74c3c")) // Binormal B
  
  // Marcador del punto p
  circle(p_pos, radius: 2.2pt, fill: rgb("#2c3e50"))
  
  // Etiquetas del Triedro de Frenet
  content((T_pos.at(0) - 0.1, T_pos.at(1) + 0.18), [$arrow(T)$], size: 9pt)
  content((N_pos.at(0) + 0.15, N_pos.at(1) - 0.1), [$arrow(N)$], size: 9pt)
  content((B_pos.at(0) - 0.15, B_pos.at(1) + 0.1), [$arrow(B)$], size: 9pt)
  
  // Eje del cilindro (eje z de la hélice)
  line(proj(0, 0, z_min), proj(0, 0, z_max), stroke: 0.8pt + rgb("#7f8c8d"))
  let p_z_max = proj(0, 0, z_max)
  content((p_z_max.at(0), p_z_max.at(1) + 0.2), [$z$], size: 9pt)
})
