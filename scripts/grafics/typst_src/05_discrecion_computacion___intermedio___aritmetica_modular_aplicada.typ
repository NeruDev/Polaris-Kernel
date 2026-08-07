#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  let r = 3.5
  let origin = (0.0, 0.0)

  // Círculo base
  circle(origin, radius: r, stroke: 2pt + rgb("#2c3e50"), fill: rgb("#ecf0f1"))
  
  let mod-val = 12
  
  // Dibujar números y marcas del reloj modular
  for i in range(0, mod-val) {
    // Calcular angulo. El 0 arriba, direccion manecillas de reloj
    let angle = 90deg - float(i) * 360deg / float(mod-val)
    
    // Posicion para los textos
    let tx = (r - 0.6) * calc.cos(angle)
    let ty = (r - 0.6) * calc.sin(angle)
    
    // Posicion para las marcas
    let mx1 = r * calc.cos(angle)
    let my1 = r * calc.sin(angle)
    let mx2 = (r - 0.3) * calc.cos(angle)
    let my2 = (r - 0.3) * calc.sin(angle)
    
    line((mx1, my1), (mx2, my2), stroke: 1.5pt + rgb("#34495e"))
    content((tx, ty), text(weight: "bold", size: 12pt)[$#i$])
  }
  
  // Flecha circular interna para indicar dirección del avance
  arc(origin, start: 45deg, stop: -45deg, radius: 1.8, mark: (end: ">"), stroke: 1.5pt + rgb("#e74c3c"))
  content((2.4, 0.0), text(fill: rgb("#e74c3c"), size: 10pt)[$+1 (mod 12)$])
  
  // Indicador central
  circle(origin, radius: 0.1, fill: rgb("#34495e"))
  // Una flecha apuntando a un numero (e.g., 5)
  let hand-angle = 90deg - 5.0 * 360deg / 12.0
  line(origin, ((r - 1.2) * calc.cos(hand-angle), (r - 1.2) * calc.sin(hand-angle)), mark: (end: ">"), stroke: 2pt + rgb("#2980b9"))
})
