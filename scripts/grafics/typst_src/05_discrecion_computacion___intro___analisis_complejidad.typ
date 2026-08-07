#import "@preview/cetz:0.3.3"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *

  let x-min = 0.0
  let x-max = 5.0
  let y-min = 0.0
  let y-max = 5.0

  // Ejes
  line((x-min, 0.0), (x-max, 0.0), mark: (end: ">"))
  line((0.0, y-min), (0.0, y-max), mark: (end: ">"))
  content((x-max + 0.6, -0.3), [$n$ (Tamaño)])
  content((-0.3, y-max + 0.6), [$O$ (Tiempo)])

  // Curvas de complejidad
  
  // O(1)
  line((0.0, 0.5), (5.0, 0.5), stroke: 1.5pt + rgb("#2ecc71"))
  content((6.0, 0.5), text(fill: rgb("#2ecc71"))[$O(1)$])
  
  // O(log n)
  let log_pts = ()
  for i in range(1, 51) {
    let x = float(i) * 0.1
    let y = 0.5 + calc.ln(x + 1.0) * 0.6
    log_pts.push((x, y))
  }
  line(..log_pts, stroke: 1.5pt + rgb("#3498db"))
  content((6.0, 1.6), text(fill: rgb("#3498db"))[$O(log n)$])
  
  // O(n)
  line((0.0, 0.0), (5.0, 3.5), stroke: 1.5pt + rgb("#f1c40f"))
  content((6.0, 3.5), text(fill: rgb("#f1c40f"))[$O(n)$])
  
  // O(n log n)
  let nlog_pts = ()
  for i in range(0, 51) {
    let x = float(i) * 0.1
    let y = x * calc.ln(x + 2.0) * 0.4
    if y <= y-max {
      nlog_pts.push((x, y))
    }
  }
  line(..nlog_pts, stroke: 1.5pt + rgb("#e67e22"))
  content((6.0, 4.3), text(fill: rgb("#e67e22"))[$O(n log n)$])
  
  // O(n^2)
  let n2_pts = ()
  for i in range(0, 51) {
    let x = float(i) * 0.1
    let y = x * x * 0.6
    if y <= y-max {
      n2_pts.push((x, y))
    }
  }
  line(..n2_pts, stroke: 1.5pt + rgb("#e74c3c"))
  content((3.3, 5.5), text(fill: rgb("#e74c3c"))[$O(n^2)$])
  
  // O(2^n)
  let exp_pts = ()
  for i in range(0, 51) {
    let x = float(i) * 0.1
    let y = (calc.pow(2.0, x) - 1.0) * 0.5
    if y <= y-max {
      exp_pts.push((x, y))
    }
  }
  line(..exp_pts, stroke: 1.5pt + rgb("#8e44ad"))
  content((2.2, 5.5), text(fill: rgb("#8e44ad"))[$O(2^n)$])
})
