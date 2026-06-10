#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Ejes cartesianos locales (Eje Y extendido hacia abajo para dar espacio a las barras)
  line((-0.5, 0), (8.2, 0), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  line((0, -2.8), (0, 2.1), mark: (end: ">"), stroke: 1pt + rgb("#7f8c8d"))
  content((8.4, 0), [$x$], size: 10pt)
  content((0, 2.3), [$y$], size: 10pt)
  
  // Definición de la función matemática: f(x)
  let f_val(x) = {
    let dx = x - 4.4
    return dx * 0.25 + dx * dx * dx * 0.0125
  }
  
  // Dibujar Curva de la función f(x)
  let pts = ()
  for i in range(8, 77) {
    let x = float(i) * 0.1
    pts.push((x, f_val(x)))
  }
  line(..pts, stroke: 1.8pt + rgb("#2c3e50"), name: "f_curve")
  content((7.6, 1.45), [$f(x)$], size: 9pt)
  
  // Raíz exacta x* = 4.4
  let rx = 4.4
  circle((rx, 0), radius: 1.8pt, fill: rgb("#e74c3c"))
  
  // --- Paso 0: Intervalo Inicial [a0, b0] ---
  let a0 = 1.2
  let b0 = 7.2
  let fa0 = f_val(a0)
  let fb0 = f_val(b0)
  
  // Proyecciones verticales discontinuas discretas
  line((a0, 0), (a0, fa0), stroke: (paint: rgb("#bdc3c7"), thickness: 0.6pt, dash: "dotted"))
  line((b0, 0), (b0, fb0), stroke: (paint: rgb("#bdc3c7"), thickness: 0.6pt, dash: "dotted"))
  
  // Marcadores de puntos sobre la curva
  circle((a0, fa0), radius: 1.8pt, fill: rgb("#7f8c8d"))
  circle((b0, fb0), radius: 1.8pt, fill: rgb("#7f8c8d"))
  
  // --- Paso 1: Primera partición p1 = 4.2 ---
  let p1 = 4.2
  let fp1 = f_val(p1)
  line((p1, 0), (p1, fp1), stroke: (paint: rgb("#3498db"), thickness: 0.8pt, dash: "dashed"))
  circle((p1, fp1), radius: 1.8pt, fill: rgb("#3498db"))
  
  // --- Paso 2: Segunda partición p2 = 5.7 ---
  let p2 = 5.7
  let fp2 = f_val(p2)
  line((p2, 0), (p2, fp2), stroke: (paint: rgb("#27ae60"), thickness: 0.8pt, dash: "dashed"))
  circle((p2, fp2), radius: 1.8pt, fill: rgb("#27ae60"))
  
  // --- Etiquetas en el eje X ---
  content((a0, -0.35), [$a_0$], size: 8pt)
  content((p1 - 0.25, -0.35), [$p_1$], size: 8pt)
  content((rx + 0.25, -0.35), [$x^*$], size: 8pt)
  content((p2, -0.35), [$p_2$], size: 8pt)
  content((b0, -0.35), [$b_0$], size: 8pt)
  
  // --- Barras de Intervalos Sucesivos (Espaciado vertical ampliado) ---
  let bar_y0 = -1.6
  let bar_y1 = -2.0
  let bar_y2 = -2.5
  
  // Barra 0: [a0, b0]
  line((a0, bar_y0), (b0, bar_y0), stroke: 2.2pt + rgb("#bdc3c7"))
  content((a0 - 0.35, bar_y0), [$I_0$], size: 7.5pt)
  
  // Barra 1: [p1, b0]
  line((p1, bar_y1), (b0, bar_y1), stroke: 2.2pt + rgb("#3498db"))
  content((p1 - 0.35, bar_y1), [$I_1$], size: 7.5pt)
  
  // Barra 2: [p1, p2]
  line((p1, bar_y2), (p2, bar_y2), stroke: 2.2pt + rgb("#27ae60"))
  content((p1 - 0.35, bar_y2), [$I_2$], size: 7.5pt)
  
  // ==========================================
  // LEYENDA DEL ALGORITMO (Lado Derecho, leg_x = 8.8, mayor interlineado)
  // ==========================================
  let leg_x = 8.8
  
  // Marco contenedor para la leyenda (Ampliado verticalmente para mayor interlineado)
  rect((leg_x, -2.1), (leg_x + 3.4, 2.1), radius: 4pt, fill: rgb("#f8f9fa"), stroke: 0.8pt + rgb("#e2e2e2"))
  content((leg_x + 1.7, 1.80), [*Iteraciones Bisección*], size: 9pt)
  
  // Iteración 0
  content((leg_x + 0.2, 1.35), [Intervalo inicial $I_0 = [a_0, b_0]$], size: 7.5pt, anchor: "west")
  content((leg_x + 0.4, 0.95), [$f(a_0) < 0, quad f(b_0) > 0$], size: 7.5pt, anchor: "west")
  
  // Iteración 1
  content((leg_x + 0.2, 0.35), [Punto medio $p_1 = frac(a_0 + b_0, 2)$], size: 7.5pt, anchor: "west")
  content((leg_x + 0.4, -0.05), [$f(p_1) < 0 quad arrow quad I_1 = [p_1, b_0]$], size: 7.5pt, anchor: "west")
  
  // Iteración 2
  content((leg_x + 0.2, -0.65), [Punto medio $p_2 = frac(p_1 + b_0, 2)$], size: 7.5pt, anchor: "west")
  content((leg_x + 0.4, -1.05), [$f(p_2) > 0 quad arrow quad I_2 = [p_1, p_2]$], size: 7.5pt, anchor: "west")
  
  // Criterio de parada / acotamiento
  content((leg_x + 0.2, -1.55), [Acotamiento final de la raíz:], size: 7.5pt, anchor: "west")
  content((leg_x + 0.4, -1.95), [$x^* in I_2 = [p_1, p_2]$], size: 7.5pt, anchor: "west")
})
