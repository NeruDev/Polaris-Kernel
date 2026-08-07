#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Ejes cartesianos en 2D
  line((-3.2, 0), (3.2, 0), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  line((0, -3.2), (0, 3.2), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  content((3.4, 0), [$x$], size: 9pt)
  content((0, 3.4), [$y$], size: 9pt)
  
  // Bucle para dibujar de forma dinámica las flechas del campo rotacional
  // F(x, y) = (-y, x)
  for x in range(-2, 3) {
    for y in range(-2, 3) {
      // Omitir el origen donde el vector es nulo
      if x == 0 and y == 0 {
        continue
      }
      
      let px = float(x)
      let py = float(y)
      
      // Vector de dirección de rotación
      let vx = -py
      let vy = px
      
      // Distancia al origen (radio)
      let r = calc.sqrt(px * px + py * py)
      
      // Normalizar y escalar para la visualización del campo
      let vx_esc = (vx / r) * 0.5
      let vy_esc = (vy / r) * 0.5
      
      // Centrar la flecha en la coordenada de la cuadrícula
      let start_x = px - vx_esc / 2
      let start_y = py - vy_esc / 2
      let end_x = px + vx_esc / 2
      let end_y = py + vy_esc / 2
      
      // Color de las flechas según la magnitud (calor/velocidad)
      let color = rgb("#3498db") // Azul para velocidad baja (cerca del origen)
      if r > 2.0 {
        color = rgb("#e74c3c") // Rojo para velocidad alta (exterior)
      } else if r > 1.0 {
        color = rgb("#39C5BB") // Turquesa Miku para velocidad intermedia
      }
      
      line((start_x, start_y), (end_x, end_y), mark: (end: ">"), stroke: 1.2pt + color)
    }
  }
  
  // Etiqueta del campo vectorial
  content((1.8, 2.7), [$arrow(F)(x,y) = (-y, x)$], size: 9pt)
  content((-1.8, -2.7), [$"rot" arrow(F) = 2 arrow(k)$], size: 9pt)
})
