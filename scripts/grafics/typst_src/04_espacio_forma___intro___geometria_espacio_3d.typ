#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  let origin = (0.0, 0.0)
  
  let x-dir = (-0.866, -0.5) 
  let y-dir = (0.866, -0.5)  
  let z-dir = (0.0, 1.0)     

  let scale-ax = 3.0

  // Ejes
  line(origin, (x-dir.at(0) * scale-ax, x-dir.at(1) * scale-ax), mark: (end: ">"), stroke: gray)
  line(origin, (y-dir.at(0) * scale-ax, y-dir.at(1) * scale-ax), mark: (end: ">"), stroke: gray)
  line(origin, (z-dir.at(0) * scale-ax, z-dir.at(1) * scale-ax), mark: (end: ">"), stroke: gray)
  
  content((x-dir.at(0) * scale-ax - 0.4, x-dir.at(1) * scale-ax - 0.4), [$x$])
  content((y-dir.at(0) * scale-ax + 0.4, y-dir.at(1) * scale-ax - 0.4), [$y$])
  content((z-dir.at(0) * scale-ax, z-dir.at(1) * scale-ax + 0.4), [$z$])

  // Plano
  let p-x = (x-dir.at(0) * 2.0, x-dir.at(1) * 2.0)
  let p-y = (y-dir.at(0) * 2.0, y-dir.at(1) * 2.0)
  let p-z = (z-dir.at(0) * 2.0, z-dir.at(1) * 2.0)

  line(p-x, p-y, p-z, close: true, fill: rgb(0, 150, 255, 60), stroke: 1pt + blue)
  
  // Vector Normal
  let center = ((p-x.at(0) + p-y.at(0) + p-z.at(0))/3.0, (p-x.at(1) + p-y.at(1) + p-z.at(1))/3.0)
  let normal = (center.at(0) + 1.0, center.at(1) + 1.5)
  
  line(center, normal, mark: (end: ">"), stroke: 1.5pt + red)
  content((normal.at(0) + 0.4, normal.at(1) + 0.4), text(fill: red)[$n$])

  // Puntos
  circle(p-x, radius: 0.05, fill: black)
  circle(p-y, radius: 0.05, fill: black)
  circle(p-z, radius: 0.05, fill: black)
})
