#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  // Falacia: Afirmación del Consecuente (P -> Q, Q, por lo tanto P)
  // Se representa como conjuntos donde P está dentro de Q, pero estar en Q no garantiza estar en P.
  
  // Conjunto Q (Consecuente)
  circle((0,0), radius: 3, fill: rgb(200, 220, 255, 100), stroke: blue)
  content((0, 2.3), text(fill: blue, weight: "bold", size: 14pt)[Conjunto $Q$ (Consecuente)])
  
  // Conjunto P (Antecedente)
  circle((-0.5, -0.5), radius: 1.5, fill: rgb(150, 255, 150, 150), stroke: green)
  content((-0.5, -0.5), text(fill: green.darken(20%), weight: "bold", size: 12pt)[Conjunto $P$ (Antecedente)])
  
  // Elemento x en Q pero no en P
  circle((1.5, -0.5), radius: 0.1, fill: red)
  content((2.2, -0.5), text(fill: red, weight: "bold")[Elemento $x$])
  
  // Explicación textual a un lado
  content((6, 0), align(left, box(width: 6cm)[
    #text(weight: "bold", size: 14pt)[Afirmación del Consecuente] \ \
    Premisa 1: Si llueve ($P$), entonces el suelo se moja ($Q$). \
    Premisa 2: El suelo está mojado ($x \\in Q$). \
    Conclusión Falaz: Por lo tanto, llovió ($x \\in P$). \ \
    #text(fill: red, size: 10pt)[(Falso: Alguien pudo regar el jardín. Estar en $Q$ no implica estar en $P$)]
  ]))
  
  // Línea separadora
  line((4, -3), (4, 3), stroke: (dash: "dashed", paint: gray))
})
