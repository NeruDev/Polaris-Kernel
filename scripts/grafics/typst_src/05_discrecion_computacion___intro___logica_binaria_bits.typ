#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  // Operación a nivel de bits: AND
  
  // Tabla de verdad AND visual
  content((0, 3), text(weight: "bold", size: 14pt)[Compuerta Lógica: AND (Conjunción)])
  
  // Bits de entrada 1
  content((-3, 1), box(fill: rgb(200, 200, 255), outset: 5pt)[Bit $A = 1$])
  // Bits de entrada 2
  content((-3, -1), box(fill: rgb(200, 200, 255), outset: 5pt)[Bit $B = 0$])
  
  // Cables de entrada
  line((-2, 1), (0, 0.5), stroke: (paint: gray, thickness: 2pt))
  line((-2, -1), (0, -0.5), stroke: (paint: gray, thickness: 2pt))
  
  // Símbolo de la compuerta AND
  arc((0, -1), start: -90deg, stop: 90deg, radius: 1, fill: rgb(255, 230, 150), stroke: (paint: orange, thickness: 2pt))
  line((0, 1), (0, -1), stroke: (paint: orange, thickness: 2pt))
  content((0.5, 0), text(weight: "bold")[AND])
  
  // Cable de salida
  line((1, 0), (3, 0), stroke: (paint: gray, thickness: 2pt))
  
  // Bit de salida
  content((4.2, 0), box(fill: rgb(255, 200, 200), outset: 5pt)[Salida = $0$])
  
  // Explicación de la regla
  content((0, -2.5), align(center)[
    #text(style: "italic")[La salida es $1$ única y exclusivamente si ambos bits de entrada son $1$.]
  ])
})
