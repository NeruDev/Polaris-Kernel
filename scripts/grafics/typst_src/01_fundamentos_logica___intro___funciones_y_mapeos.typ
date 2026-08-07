#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)
#set text(font: "Inter", size: 10pt)

#cetz.canvas({
  import cetz.draw: *

  // Inyectiva
  content((0, 4), [*Inyectiva*])
  circle((-1, 2), radius: (0.8, 1.5), name: "A1", stroke: 1pt + rgb("#bdc3c7"))
  circle((1, 2), radius: (0.8, 1.5), name: "B1", stroke: 1pt + rgb("#bdc3c7"))
  
  content((-1, 3), [a], name: "a1")
  content((-1, 2), [b], name: "b1")
  content((-1, 1), [c], name: "c1")
  
  content((1, 3.2), [1], name: "n1")
  content((1, 2.4), [2], name: "n2")
  content((1, 1.6), [3], name: "n3")
  content((1, 0.8), [4], name: "n4")
  
  line("a1.east", "n1.west", mark: (end: ">"))
  line("b1.east", "n3.west", mark: (end: ">"))
  line("c1.east", "n2.west", mark: (end: ">"))

  // Sobreyectiva
  content((4, 4), [*Sobreyectiva*])
  circle((3, 2), radius: (0.8, 1.5), name: "A2", stroke: 1pt + rgb("#bdc3c7"))
  circle((5, 2), radius: (0.8, 1.2), name: "B2", stroke: 1pt + rgb("#bdc3c7"))
  
  content((3, 3), [a], name: "a2")
  content((3, 2.2), [b], name: "b2")
  content((3, 1.4), [c], name: "c2")
  content((3, 0.6), [d], name: "d2")
  
  content((5, 2.8), [1], name: "m1")
  content((5, 2), [2], name: "m2")
  content((5, 1.2), [3], name: "m3")
  
  line("a2.east", "m1.west", mark: (end: ">"))
  line("b2.east", "m2.west", mark: (end: ">"))
  line("c2.east", "m3.west", mark: (end: ">"))
  line("d2.east", "m3.west", mark: (end: ">"))

  // Biyectiva
  content((8, 4), [*Biyectiva*])
  circle((7, 2), radius: (0.8, 1.5), name: "A3", stroke: 1pt + rgb("#bdc3c7"))
  circle((9, 2), radius: (0.8, 1.5), name: "B3", stroke: 1pt + rgb("#bdc3c7"))
  
  content((7, 3), [a], name: "a3")
  content((7, 2), [b], name: "b3")
  content((7, 1), [c], name: "c3")
  
  content((9, 3), [1], name: "k1")
  content((9, 2), [2], name: "k2")
  content((9, 1), [3], name: "k3")
  
  line("a3.east", "k2.west", mark: (end: ">"))
  line("b3.east", "k1.west", mark: (end: ">"))
  line("c3.east", "k3.west", mark: (end: ">"))
})
