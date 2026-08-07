#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)
#set text(font: "Inter", size: 10pt)

#cetz.canvas({
  import cetz.draw: *

  content((2, 3.5), [*Árbol de Derivación Formal*])

  // Nodos
  rect((0, 2), (1.8, 2.8), name: "P1", fill: rgb("#f0f8ff"), stroke: 1pt + rgb("#bdc3c7"))
  content("P1", [Premisa 1: $P => Q$])

  rect((2.2, 2), (4.0, 2.8), name: "P2", fill: rgb("#f0f8ff"), stroke: 1pt + rgb("#bdc3c7"))
  content("P2", [Premisa 2: $P$])

  rect((1, 0.5), (3, 1.3), name: "MP", fill: rgb("#e8f4f8"), stroke: 1pt + rgb("#0074d9"))
  content("MP", [$Q$ (Modus Ponens)])

  rect((0.5, -1), (3.5, -0.2), name: "Concl", fill: rgb("#eef9ea"), stroke: 1pt + rgb("#2ecc40"))
  content("Concl", [Conclusión: $Q or R$])

  // Flechas
  line("P1.south", "MP.north", mark: (end: ">"))
  line("P2.south", "MP.north", mark: (end: ">"))
  line("MP.south", "Concl.north", mark: (end: ">"))
  
  content((2.8, -0.1), [Adición], size: 8pt)
})
