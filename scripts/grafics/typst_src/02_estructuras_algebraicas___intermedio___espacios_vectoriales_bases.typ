#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)
#set text(font: "Inter", size: 10pt)

#cetz.canvas({
  import cetz.draw: *

  // Grid background
  grid((0,0), (5,5), step: 1, stroke: rgb("#ecf0f1"))
  
  // Ejes
  line((0, 0), (5.5, 0), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  line((0, 0), (0, 5.5), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  
  // Base vectores v1, v2
  line((0, 0), (2, 1), mark: (end: ">"), stroke: 2pt + rgb("#2980b9"), name: "v1")
  content((2.2, 0.8), text(fill: rgb("#2980b9"))[$bold(v)_1$])
  
  line((0, 0), (1, 3), mark: (end: ">"), stroke: 2pt + rgb("#c0392b"), name: "v2")
  content((0.8, 3.2), text(fill: rgb("#c0392b"))[$bold(v)_2$])
  
  // Vector dependiente u = 1.5*v1 + 1*v2 = (3, 1.5) + (1, 3) = (4, 4.5)
  line((0, 0), (4, 4.5), mark: (end: ">"), stroke: 2pt + rgb("#27ae60"), name: "u")
  content((4.2, 4.7), text(fill: rgb("#27ae60"))[$bold(u) = c_1 bold(v)_1 + c_2 bold(v)_2$])
  
  // Proyecciones (Paralelogramo)
  // u - v2 = (4, 4.5) - (1, 3) = (3, 1.5)
  // u - v1 = (4, 4.5) - (2, 1) = (2, 3.5)
  // Geométricamente:
  line((2, 1), (5, 2.5), stroke: (dash: "dashed", paint: rgb("#7f8c8d")))
  
  line((2, 1), (4, 4.5), stroke: (dash: "dashed", paint: rgb("#7f8c8d")))
  line((1, 3), (4, 4.5), stroke: (dash: "dashed", paint: rgb("#7f8c8d")))
})
