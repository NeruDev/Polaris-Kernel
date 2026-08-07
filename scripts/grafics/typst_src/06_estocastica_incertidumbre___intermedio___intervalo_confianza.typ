#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 15pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Escala general del gráfico
  let sx(x) = { x * 1.8 }
  let sy(y) = { y * 9.0 }
  
  // Línea de referencia vertical para la Media Poblacional Real (mu) con brecha para la etiqueta
  line(
    (sx(0), sy(-0.35)),
    (sx(0), sy(0.08)),
    stroke: (paint: rgb("#94a3b8"), thickness: 1.0pt, dash: "dashed")
  )
  line(
    (sx(0), sy(0.22)),
    (sx(0), sy(0.42)),
    stroke: (paint: rgb("#94a3b8"), thickness: 1.0pt, dash: "dashed")
  )
  content((sx(0), sy(0.44)), [$mu$], size: 11pt)
  
  // Eje X principal (y = 0)
  line(
    (sx(-4.2), sy(0)),
    (sx(4.5), sy(0)),
    mark: (end: ">"),
    stroke: 1.2pt + rgb("#475569")
  )
  
  // Etiquetas del eje X
  content((sx(4.7), sy(0)), [$z$], size: 11pt)
  
  // Definición de pasos para las regiones de densidad
  let steps = 40
  
  // 1. Región de Confianza Central [-1.96, 1.96] (Área 1 - alpha = 95%)
  let pts_conf = ((sx(-1.96), sy(0.0)),)
  for i in range(0, steps + 1) {
    let x = -1.96 + float(i) * 3.92 / float(steps)
    let y = 0.398942 * calc.exp(-0.5 * x * x)
    pts_conf.push((sx(x), sy(y)))
  }
  pts_conf.push((sx(1.96), sy(0.0)))
  line(..pts_conf, close: true, fill: rgb("#3b82f61a"), stroke: none)
  
  // 2. Región de Error / Cola Izquierda [-3.8, -1.96] (Área alpha/2 = 2.5%)
  let pts_l = ((sx(-3.8), sy(0.0)),)
  for i in range(0, steps + 1) {
    let x = -3.8 + float(i) * 1.84 / float(steps)
    let y = 0.398942 * calc.exp(-0.5 * x * x)
    pts_l.push((sx(x), sy(y)))
  }
  pts_l.push((sx(-1.96), sy(0.0)))
  line(..pts_l, close: true, fill: rgb("#ef444415"), stroke: none)
  
  // 3. Región de Error / Cola Derecha [1.96, 3.8] (Área alpha/2 = 2.5%)
  let pts_r = ((sx(1.96), sy(0.0)),)
  for i in range(0, steps + 1) {
    let x = 1.96 + float(i) * 1.84 / float(steps)
    let y = 0.398942 * calc.exp(-0.5 * x * x)
    pts_r.push((sx(x), sy(y)))
  }
  pts_r.push((sx(3.8), sy(0.0)))
  line(..pts_r, close: true, fill: rgb("#ef444415"), stroke: none)
  
  // Curva de la Distribución Muestral
  let curve_pts = ()
  let curve_steps = 100
  for i in range(0, curve_steps + 1) {
    let x = -3.8 + float(i) * 7.6 / float(curve_steps)
    let y = 0.398942 * calc.exp(-0.5 * x * x)
    curve_pts.push((sx(x), sy(y)))
  }
  line(..curve_pts, stroke: 2pt + rgb("#3b82f6"))
  
  // Valores críticos en la curva (Líneas verticales discontinuas finas)
  let y_crit = 0.398942 * calc.exp(-0.5 * 1.96 * 1.96) // ~0.058
  line((sx(-1.96), sy(0)), (sx(-1.96), sy(y_crit)), stroke: (paint: rgb("#94a3b8"), thickness: 0.8pt, dash: "dashed"))
  line((sx(1.96), sy(0)), (sx(1.96), sy(y_crit)), stroke: (paint: rgb("#94a3b8"), thickness: 0.8pt, dash: "dashed"))
  
  // Etiquetas de los valores críticos en el eje X
  content((sx(-1.96), sy(-0.05)), [$-z_(alpha/2)$], size: 9pt)
  content((sx(1.96), sy(-0.05)), [$z_(alpha/2)$], size: 9pt)
  content((sx(-1.96), sy(-0.16)), [$-1.96$], size: 8pt, fill: rgb("#475569"))
  content((sx(1.96), sy(-0.16)), [$1.96$], size: 8pt, fill: rgb("#475569"))
  
  // Etiquetas de las regiones
  rect(
    (sx(-1.5), sy(0.11)),
    (sx(1.5), sy(0.19)),
    fill: rgb("#eff6ffeb"), // Azul muy claro semi-translúcido
    stroke: 0.5pt + rgb("#bfdbfe"),
    radius: 3pt
  )
  content((sx(0), sy(0.15)), text(fill: rgb("#1e3a8a"), size: 9.5pt, weight: "bold")[Confianza ($1-alpha = 95%$)] )
  
  // Flechas y etiquetas para las colas
  line((sx(-2.5), sy(0.08)), (sx(-2.1), sy(0.02)), mark: (end: ">"), stroke: 0.8pt + rgb("#991b1b"))
  content((sx(-2.7), sy(0.1)), text(fill: rgb("#991b1b"), size: 8pt)[$alpha/2 = 2.5%$])
  
  line((sx(2.5), sy(0.08)), (sx(2.1), sy(0.02)), mark: (end: ">"), stroke: 0.8pt + rgb("#991b1b"))
  content((sx(2.7), sy(0.1)), text(fill: rgb("#991b1b"), size: 8pt)[$alpha/2 = 2.5%$])
  
  // --- REPRESENTACIÓN DEL INTERVALO DE CONFIANZA ---
  // Muestra específica con media muestral x_bar = 1.3 (desplazada a la derecha)
  let x_bar = 1.3
  let z_crit = 1.96
  let margin_err = z_crit // El margen de error equivale a z_crit en la distribución estandarizada
  let lcl = x_bar - margin_err // -0.66
  let ucl = x_bar + margin_err // 3.26
  let y_ic = -0.35 // Posición en el eje Y por debajo del gráfico (más cerca de la campana)
  
  // Dibujar el intervalo (Línea horizontal verde moderno)
  line(
    (sx(lcl), sy(y_ic)),
    (sx(ucl), sy(y_ic)),
    stroke: 2.2pt + rgb("#10b981")
  )
  
  // Corchetes de los extremos LCL y UCL
  line((sx(lcl), sy(y_ic - 0.06)), (sx(lcl), sy(y_ic + 0.06)), stroke: 2.2pt + rgb("#10b981"))
  line((sx(ucl), sy(y_ic - 0.06)), (sx(ucl), sy(y_ic + 0.06)), stroke: 2.2pt + rgb("#10b981"))
  
  // Punto central del Estimador Muestral (x_bar)
  circle(
    (sx(x_bar), sy(y_ic)),
    radius: 3pt,
    fill: rgb("#10b981"),
    stroke: 1pt + rgb("#047857")
  )
  
  // Etiquetas del Intervalo de Confianza (colocadas arriba de la barra verde, bajo el eje X)
  content((sx(x_bar), sy(y_ic + 0.12)), [$bar(x)$], size: 10pt)
  content((sx(lcl), sy(y_ic + 0.12)), [$bar(x) - E$], size: 8.5pt)
  content((sx(ucl), sy(y_ic + 0.12)), [$bar(x) + E$], size: 8.5pt)
  content((sx(lcl - 0.4), sy(y_ic)), text(fill: rgb("#047857"), size: 8.5pt, weight: "bold")[IC], anchor: "east")
  
  // Indicación del Margen de Error (E) (colocada debajo de la barra verde para no colisionar)
  // Flecha bidireccional desde x_bar hasta UCL
  line(
    (sx(x_bar), sy(y_ic - 0.16)),
    (sx(ucl), sy(y_ic - 0.16)),
    mark: (start: ">", end: ">"),
    stroke: 0.8pt + rgb("#047857")
  )
  content(
    (sx(x_bar + margin_err/2), sy(y_ic - 0.28)),
    text(fill: rgb("#047857"), size: 8.5pt)[$E = z_(alpha/2) dot frac(sigma, sqrt(n))$]
  )
  content(
    (sx(x_bar + margin_err/2), sy(y_ic - 0.40)),
    text(fill: rgb("#047857"), size: 8pt)[Margen de error]
  )
})
