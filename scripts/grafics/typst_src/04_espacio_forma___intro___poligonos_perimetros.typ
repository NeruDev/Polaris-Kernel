#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  // Dibujo de un polígono regular (Pentágono)
  // Vértices del pentágono inscrito en un círculo de radio 2
  let r = 2
  let v1 = (0, r)
  let v2 = (r * calc.cos(18deg), r * calc.sin(18deg))
  let v3 = (r * calc.cos(-54deg), r * calc.sin(-54deg))
  let v4 = (-r * calc.cos(-54deg), r * calc.sin(-54deg))
  let v5 = (-r * calc.cos(18deg), r * calc.sin(18deg))
  
  // Dibujar el polígono relleno
  line(v1, v2, v3, v4, v5, close: true, fill: rgb(200, 255, 200, 150), stroke: (paint: green.darken(20%), thickness: 1.5pt), name: "Pentagono")
  
  // Etiquetas de los lados (L)
  content((1.2, 1.4), [$L$])
  content((1.9, -0.6), [$L$])
  content((0, -2.2), [$L$])
  content((-1.9, -0.6), [$L$])
  content((-1.2, 1.4), [$L$])
  
  // Centro y Apotema (a)
  circle((0,0), radius: 0.05, fill: black)
  line((0,0), (0, -r * calc.sin(54deg)), stroke: (paint: blue, dash: "dashed"))
  content((-0.2, -0.8), text(fill: blue)[$a$])
  
  // Texto interior: Área
  content((0, 0.5), text(weight: "bold", size: 12pt)[Área])
  
  // Fórmulas
  content((4, 0), align(left, box(width: 4cm)[
    #text(weight: "bold")[Pentágono Regular] \ \
    Perímetro ($P$): \
    $P = 5 dot L$ \ \
    Área ($A$): \
    $A = (P dot a) / 2$
  ]))
})
