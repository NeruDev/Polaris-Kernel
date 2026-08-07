#import "@preview/cetz:0.3.2"

#set page(width: auto, height: auto, margin: 10pt)

#cetz.canvas({
  import cetz.draw: *
  
  // Configuración de estilos globales para las cajas de las estructuras
  let style-box(fill-color) = (
    fill: fill-color,
    stroke: 1.5pt + rgb("#2c3e50"),
    radius: 3pt
  )

  // ---------------------------------------------------------------------------
  // NODO 1: GRUPO
  // ---------------------------------------------------------------------------
  rect((-3, 5), (3, 6.2), ..style-box(rgb("#39C5BB").lighten(80%)), name: "grupo")
  content("grupo", [
    *Grupo* $(G, \cdot)$ \
    #set text(size: 7pt)
    1. Clausura | 2. Asociatividad | 3. Neutro | 4. Inverso
  ])

  // Flecha 1 -> 2
  line((0, 5), (0, 3.8), mark: (end: ">"), stroke: 1.5pt + rgb("#7f8c8d"))
  content((1.2, 4.4), [Abeliano \ (+ Conmutatividad)], size: 7pt, fill: white)

  // ---------------------------------------------------------------------------
  // NODO 2: GRUPO ABELIANO
  // ---------------------------------------------------------------------------
  rect((-3, 2.5), (3, 3.7), ..style-box(rgb("#39C5BB").lighten(60%)), name: "abeliano")
  content("abeliano", [
    *Grupo Abeliano* $(G, +)$ \
    #set text(size: 7pt)
    Axiomas de Grupo + Conmutatividad: $a + b = b + a$
  ])

  // Flecha 2 -> 3
  line((0, 2.5), (0, 1.3), mark: (end: ">"), stroke: 1.5pt + rgb("#7f8c8d"))
  content((1.8, 1.9), [Segunda operacion $(dot)$ \ (+ Distributividad)], size: 7pt, fill: white)

  // ---------------------------------------------------------------------------
  // NODO 3: ANILLO
  // ---------------------------------------------------------------------------
  rect((-3, 0), (3, 1.2), ..style-box(rgb("#3498db").lighten(70%)), name: "anillo")
  content("anillo", [
    *Anillo* $(R, +, dot)$ \
    #set text(size: 7pt)
    1. $(R, +)$ es Grupo Abeliano \
    2. $(R, dot)$ es Semigrupo (Clausura, Asociatividad)
  ])

  // Flecha 3 -> 4
  line((0, 0), (0, -1.2), mark: (end: ">"), stroke: 1.5pt + rgb("#7f8c8d"))
  content((1.8, -0.6), [Conmutatividad en $(dot)$ \ y Elemento Unidad (1)], size: 7pt, fill: white)

  // ---------------------------------------------------------------------------
  // NODO 4: ANILLO CONMUTATIVO UNITARIO
  // ---------------------------------------------------------------------------
  rect((-3, -2.5), (3, -1.3), ..style-box(rgb("#3498db").lighten(50%)), name: "anillo_unitario")
  content("anillo_unitario", [
    *Anillo Conmutativo Unitario* \
    #set text(size: 7pt)
    $(R, dot)$ es Monoide Conmutativo: $a dot b = b dot a$ y $exists 1$
  ])

  // Flecha 4 -> 5
  line((0, -2.5), (0, -3.7), mark: (end: ">"), stroke: 1.5pt + rgb("#7f8c8d"))
  content((1.8, -3.1), [Todo elemento no nulo \ posee inverso multiplicativo], size: 7pt, fill: white)

  // ---------------------------------------------------------------------------
  // NODO 5: CAMPO / CUERPO
  // ---------------------------------------------------------------------------
  rect((-3, -5), (3, -3.8), ..style-box(rgb("#e74c3c").lighten(70%)), name: "campo")
  content("campo", [
    *Campo (Cuerpo)* $(K, +, dot)$ \
    #set text(size: 7pt)
    1. $(K, +)$ y $(K - {0}, dot)$ son Grupos Abelianos \
    2. Ejemplos: $QQ$, $RR$, $CC$
  ])
})
