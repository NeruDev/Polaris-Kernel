#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 5pt)

#cetz.canvas({
  import cetz.draw: *

  // R
  circle((0, 0), radius: 4, name: "R", fill: rgb("E6F2FF"), stroke: (paint: rgb("0066CC"), thickness: 1pt))
  content((0, 3.2), [$bb(R)$ Reales])
  
  // Q
  circle((0, -0.5), radius: 3, name: "Q", fill: rgb("CCE5FF"), stroke: (paint: rgb("0055AA"), thickness: 1pt))
  content((0, 1.8), [$bb(Q)$ Racionales])

  // Z
  circle((0, -1), radius: 2, name: "Z", fill: rgb("99CCFF"), stroke: (paint: rgb("004488"), thickness: 1pt))
  content((0, 0.4), [$bb(Z)$ Enteros])

  // N
  circle((0, -1.5), radius: 1, name: "N", fill: rgb("66B2FF"), stroke: (paint: rgb("003366"), thickness: 1pt))
  content((0, -1.5), [$bb(N)$ Naturales])
})
