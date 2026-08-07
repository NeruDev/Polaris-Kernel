#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  let r = 2.0
  let origin = (0.0, 0.0)

  // Ejes
  line((-3.0, 0.0), (3.0, 0.0), mark: (end: ">"), stroke: gray)
  line((0.0, -3.0), (0.0, 3.0), mark: (end: ">"), stroke: gray)
  content((3.3, -0.3), [$x$])
  content((-0.3, 3.3), [$y$])

  // Círculo
  circle(origin, radius: r, stroke: 1.5pt + blue)

  // Ángulo theta
  let theta = 35deg
  let p1 = (r * calc.cos(theta), r * calc.sin(theta))
  line(origin, p1, stroke: 1pt + black)
  circle(p1, radius: 0.05, fill: red)
  content((p1.at(0) + 0.7, p1.at(1) + 0.7), [$(cos theta, sin theta)$])
  
  // Arco para theta
  arc(origin, start: 0deg, stop: theta, radius: 0.5, stroke: 1.5pt + red)
  content((0.9, 0.35), text(fill: red)[$theta$])

  // Triángulo rectángulo
  line(p1, (p1.at(0), 0.0), stroke: (paint: gray, dash: "dashed"))
  line(origin, (p1.at(0), 0.0), stroke: (paint: gray, dash: "dashed"))

  // Ángulo negativo -theta
  let p2 = (r * calc.cos(-theta), r * calc.sin(-theta))
  line(origin, p2, stroke: 1pt + black)
  circle(p2, radius: 0.05, fill: green)
  content((p2.at(0) + 0.7, p2.at(1) - 0.6), [$(cos(-theta), sin(-theta))$])
  
  // Arco para -theta
  arc(origin, start: 0deg, stop: -theta, radius: 0.4, stroke: 1.5pt + green)
  content((0.8, -0.3), text(fill: green)[$-theta$])
  
  line(p2, (p2.at(0), 0.0), stroke: (paint: gray, dash: "dashed"))
})
