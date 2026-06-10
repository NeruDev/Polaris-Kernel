#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Función para obtener propiedades del número
  let get-properties(n) = {
    let primos = (2, 3, 5, 7, 11, 13, 17, 19, 23)
    if primos.contains(n) {
      return (is-primo: true, div-min: n)
    }
    
    if calc.even(n) {
      return (is-primo: false, div-min: 2)
    }
    if calc.rem(n, 3) == 0 {
      return (is-primo: false, div-min: 3)
    }
    if calc.rem(n, 5) == 0 {
      return (is-primo: false, div-min: 5)
    }
    return (is-primo: false, div-min: 7)
  }
  
  // --- Cuadrícula de la Criba (Números del 2 al 26, desplazada a la izquierda) ---
  for f in range(0, 5) {
    for c in range(0, 5) {
      let n = 2 + c + f * 5
      let x = float(c) * 1.1 - 3.0
      let y = 2.2 - float(f) * 1.1
      
      let prop = get-properties(n)
      
      if prop.is-primo {
        // Primo
        circle((x, y), radius: 0.42, fill: rgb("#39C5BB").lighten(85%), stroke: 1.5pt + rgb("#39C5BB"))
        content((x, y), [*#str(n)*], size: 10pt)
      } else {
        // Compuesto (atenuado y tachado)
        content((x, y), str(n), size: 10pt)
        
        let stroke-color = rgb("#7f8c8d")
        if prop.div-min == 2 {
          stroke-color = rgb("#3498db")
        } else if prop.div-min == 3 {
          stroke-color = rgb("#e67e22")
        } else if prop.div-min == 5 {
          stroke-color = rgb("#e74c3c")
        }
        
        let d = 0.26
        line((x - d, y - d), (x + d, y + d), stroke: 1.2pt + stroke-color)
      }
    }
  }
  
  // --- Leyenda Vertical a la Derecha (Con la simbología exacta de las líneas de la criba) ---
  let leg_x = 2.1
  
  // Elemento Primo
  circle((leg_x + 0.3, 1.2), radius: 0.20, fill: rgb("#39C5BB").lighten(85%), stroke: 1.2pt + rgb("#39C5BB"))
  content((leg_x + 0.7, 1.2), [Número Primo], size: 8pt, anchor: "west")
  
  // Elemento Compuesto divisor 2
  circle((leg_x + 0.3, 0.4), radius: 0.20, stroke: 0.5pt + rgb("#bdc3c7"), fill: none)
  line((leg_x + 0.3 - 0.13, 0.4 - 0.13), (leg_x + 0.3 + 0.13, 0.4 + 0.13), stroke: 1.2pt + rgb("#3498db"))
  content((leg_x + 0.7, 0.4), [Divisible entre 2], size: 8pt, anchor: "west")
  
  // Elemento Compuesto divisor 3
  circle((leg_x + 0.3, -0.4), radius: 0.20, stroke: 0.5pt + rgb("#bdc3c7"), fill: none)
  line((leg_x + 0.3 - 0.13, -0.4 - 0.13), (leg_x + 0.3 + 0.13, -0.4 + 0.13), stroke: 1.2pt + rgb("#e67e22"))
  content((leg_x + 0.7, -0.4), [Divisible entre 3], size: 8pt, anchor: "west")
  
  // Elemento Compuesto divisor 5
  circle((leg_x + 0.3, -1.2), radius: 0.20, stroke: 0.5pt + rgb("#bdc3c7"), fill: none)
  line((leg_x + 0.3 - 0.13, -1.2 - 0.13), (leg_x + 0.3 + 0.13, -1.2 + 0.13), stroke: 1.2pt + rgb("#e74c3c"))
  content((leg_x + 0.7, -1.2), [Divisible entre 5], size: 8pt, anchor: "west")
  
  // Nota aclaratoria al final, debajo de la criba
  content((-0.8, -3.1), [
    $p_i$ es primo. Los compuestos son tachados por su factor primo mínimo.
  ], size: 7.5pt)
})
