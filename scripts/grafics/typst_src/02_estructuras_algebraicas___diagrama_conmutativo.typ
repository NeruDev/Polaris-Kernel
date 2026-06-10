#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Definicion de los objetos (Nodos) de la categoria
  content((0, 2.2), [$A$], name: "A", size: 14pt)
  content((3.5, 2.2), [$B$], name: "B", size: 14pt)
  content((1.75, 0.2), [$C$], name: "C", size: 14pt)
  
  // Morfismo f: A -> B
  // Usamos anclajes de nodo en CeTZ para que las flechas no toquen el texto
  line("A.east", "B.west", mark: (end: ">"), stroke: 1.5pt + rgb("#2c3e50"), name: "f")
  content((1.75, 2.5), [$f$], size: 10pt)
  
  // Morfismo g: B -> C
  line("B.south-west", "C.north-east", mark: (end: ">"), stroke: 1.5pt + rgb("#2c3e50"), name: "g")
  content((2.9, 1.2), [$g$], size: 10pt)
  
  // Morfismo composicion: g o f: A -> C (Resaltado en color turquesa Miku)
  line("A.south-east", "C.north-west", mark: (end: ">"), stroke: 1.5pt + rgb("#39C5BB"), name: "g_o_f")
  content((0.5, 1.2), [$g compose f$], size: 10pt)
  
  // Indicador de conmutatividad en el centro del diagrama
  content((1.75, 1.4), [conmuta], size: 8pt)
  
  // Pequeña flecha curva indicando la dirección de conmutación
  arc((1.75, 1.6), start: 220deg, delta: 100deg, radius: 0.2, stroke: 0.8pt + rgb("#7f8c8d"), mark: (end: ">"))
})
