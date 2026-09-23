# Diseño — "Durar más, el plan de 21 días"

_Diseñante, 23/09/2026. Para maquetar en Canva a partir de `CONTENIDO.md`._
_La portada se puede ver ya: abrí `PORTADA.html` en el navegador._

---

## 0. Título: uno solo, decidido

| Dónde | Texto |
|---|---|
| Nombre del producto | **Durar más — el plan de 21 días** |
| Portada (arriba, chico) | EL PLAN DE 21 DÍAS |
| Portada (gigante) | **DURAR MÁS** |
| Portada (abajo) | Entrenamiento de control. Sin pastillas. |
| Página de venta y archivo | Para el que termina antes de lo que quiere. Sin pastillas. |
| Nombre del archivo | `durar-mas-plan-21-dias.pdf` |

**Por qué el subtítulo de la portada es más corto que el de la página.** La portada vive
en el celular del comprador. "Termina antes de lo que quiere" es la única línea que
alguien podría leer por encima del hombro. En la página de venta esa frase es el gancho y
se queda; en la tapa se guarda. La tapa es la caja del remedio, no el prospecto.

El texto de venta es de Whoper. Si él cambia la frase de la página, la portada no se
toca: la de la tapa ya está elegida por discreción, no por gusto.

---

## 1. La portada

### El concepto en tres líneas

Arriba el título enorme en dos renglones. Abajo, diez barras de un medidor: nueve apagadas
y **una sola encendida, la 7**. Debajo de esa barra, un 7 en cobre.

Es el mapa del capítulo 4 convertido en imagen. El que compra y después abre el PDF
reconoce el dibujo: la tapa y la herramienta central son la misma cosa.

### Por qué es discreta

De lejos parece un medidor de sonido o una app de entrenamiento. Sin cuerpos, sin pareja,
sin pastillas, sin rojo de farmacia, sin la palabra del diagnóstico. Un amigo que mira de
costado ve un libro de disciplina.

### Los dos colores exactos

| Rol | Hex | Dónde va |
|---|---|---|
| **Tinta** | `#12161C` | fondo de la portada, y texto del PDF sobre blanco |
| **Cobre** | `#AD6015` | acento sobre blanco: títulos de tabla, cajas, números de ejercicio, botón del checkout |
| Cobre claro | `#E0954A` | el mismo cobre aclarado, **solo** sobre el fondo oscuro (portada y banner) |
| Blanco | `#FFFFFF` | fondo del PDF |
| Caja | `#F8F2EC` | fondo de las cajas "ojo con esto" (es el cobre al 8%) |
| Línea | `#E3E1DD` | filas de tabla, pie de página |

Contraste, ya chequeado: blanco sobre cobre `#AD6015` da **4,7 a 1** (pasa AA, sirve para
el botón del checkout). Cobre claro `#E0954A` sobre tinta da **7,4 a 1**. Si querés
verificarlo: https://webaim.org/resources/contrastchecker/

**Por qué cobre y no otro.** Rojo es farmacia. Azul es clínica. Verde es suplemento de
hombre (la mitad de la competencia lo usa). Violeta degradado es "hecho con IA". El cobre
es gimnasio, cuero, disciplina: caliente y adulto sin gritar.

### La letra

**Open Sans**, una sola familia. ExtraBold para el título de tapa, Bold para títulos,
Regular para texto. Está en Canva gratis y es una de las tres letras del checkout de Whop,
así que el PDF y la página de pago van a parecer del mismo negocio.

### Medidas de la portada

| Qué | Valor |
|---|---|
| Lienzo | 1800 × 2700 px (= 6 × 9 pulgadas a 300 dpi) |
| Margen lateral | 216 px (7,2 % del ancho) |
| Kicker "EL PLAN DE 21 DÍAS" | 63 px, Bold, espaciado entre letras +4,5, cobre claro |
| Raya bajo el kicker | 192 × 9 px, cobre claro |
| Título DURAR / MÁS | 384 px, ExtraBold, blanco, espaciado −2 |
| Medidor | 10 barras de 90 px de ancho, 54 px de separación, base a 2280 px del borde superior |
| Barras 1 a 6 | blanco al 20 % |
| **Barra 7** | cobre claro `#E0954A`, sólida, la más alta que se ve |
| Barras 8, 9, 10 | blanco al 9 %: siguen subiendo pero se apagan |
| El "7" | 108 px ExtraBold, cobre claro, centrado bajo la barra |
| Pie | 66 px Semibold, blanco al 78 % |

Las alturas exactas de cada barra están en `PORTADA.html` (multiplicá por 3 los valores
del SVG para pasarlos a px del lienzo de 1800).

### La prueba del pulgar

En `PORTADA.html` está la misma tapa a 300, 150 y 80 px. A 80 px ya no se lee el pie y no
importa: se sigue leyendo DURAR MÁS y se sigue viendo la barra naranja. Eso es aprobar.

---

## 2. El sistema visual del PDF

### La hoja

| Qué | Valor | Por qué |
|---|---|---|
| Tamaño | **152 × 229 mm** (6 × 9 pulgadas) | más alta que A5, llena mejor la pantalla del celular |
| Margen izquierdo y derecho | 16 mm | columna de texto de 120 mm, unas 55 letras por línea |
| Margen superior | 18 mm |  |
| Margen inferior | 20 mm | deja aire para el pie y el número |
| Columnas | **una**, siempre | |

### Los tres tamaños de letra. No hay un cuarto

| Nivel | Tamaño | Peso | Color | Interlineado |
|---|---|---|---|---|
| Título de capítulo | **26 pt** | ExtraBold | tinta | 1,15 |
| Subtítulo (los `###` de `CONTENIDO.md`) | **15 pt** | Bold | tinta | 1,3 |
| Texto | **12,5 pt** | Regular | tinta | **1,6** (= 20 pt) |

Única excepción: el **pie de página**, 9 pt. No es un tamaño de texto, es mobiliario.

Espacio entre párrafos: 5 mm. Antes de un subtítulo: 9 mm. Nunca sangría: o sangría o
espacio, las dos juntas nunca.

### Cómo empieza cada capítulo

1. Un **chip** de cobre arriba a la izquierda: `CAP. 5` — rectángulo de esquinas de 2 mm,
   borde cobre de 1 pt, sin relleno, letra 9,5 pt Bold cobre.
2. El título a 26 pt, tinta, debajo.
3. Una raya cobre de 40 × 3 mm bajo el título.
4. El texto arranca 12 mm después.

En la página de apertura de capítulo no va pie ni número de página.

### El pie de página

Raya de 0,5 pt `#E3E1DD` a lo ancho de la columna. Debajo: a la izquierda el nombre corto
del capítulo en 9 pt gris `#8A8782`; a la derecha el número de página en 9 pt Bold cobre.

### Las cajas de "ojo con esto"

**Un solo modelo, tres etiquetas.** Nunca se inventa una cuarta.

| Etiqueta | Para qué |
|---|---|
| `HAZ ESTO` | la acción del día |
| `OJO CON ESTO` | el error que arruina el ejercicio |
| `EN UNA LÍNEA` | el resumen de la página |

Cómo se dibuja:

- Ancho: los 120 mm de la columna. Alto: el que pida el texto.
- Fondo `#F8F2EC`, esquinas de 3 mm.
- **Barra de 4 pt de cobre `#AD6015` pegada al borde izquierdo**, de arriba abajo.
- Relleno interno: 10 mm por lado.
- Etiqueta arriba: 10 pt Bold cobre, MAYÚSCULAS, espaciado entre letras +1,5.
- Texto de la caja: 12,5 pt tinta, el mismo del cuerpo.
- Nunca dos cajas seguidas y nunca más de una por página.

### Las tablas

- **Ninguna línea vertical.** Solo horizontales.
- Fila de encabezado: fondo cobre `#AD6015`, texto blanco 11 pt Bold, MAYÚSCULAS,
  espaciado +0,5. Alto 9 mm.
- Filas: fondo blanco, línea inferior de 0,5 pt `#E3E1DD`, alto mínimo 9 mm, texto 11,5 pt.
- Relleno: 4 mm arriba y abajo, 4 mm a los costados.
- Tablas de 6 filas o más: filas alternadas en `#F7F6F4` (muy suave) para no perderse.
- **Fila destacada** (el nivel 7 del mapa, la semana que importa): fondo `#F8F2EC` y texto
  en cobre Bold.
- Primera columna siempre en Bold: es la que se busca con el dedo.

La tabla "alarga / apura" del capítulo 13 y la del test del capítulo 3 son las candidatas
a captura de pantalla. Van solas en su página, con el título arriba y nada más alrededor,
para que sirvan recortadas.

### Los números de los ejercicios

Los pasos numerados (capítulo 5, 6 y 11) se dibujan así:

- **Círculo de cobre lleno, 8 mm de diámetro**, con el número adentro en blanco 12 pt
  ExtraBold, centrado.
- El círculo se alinea con la altura de la primera línea del texto, no con su centro.
- El texto arranca a 13 mm del borde izquierdo del círculo.
- Entre paso y paso: 6 mm.
- En el freno de 20 segundos (capítulo 11), a la derecha de cada paso va una **píldora de
  segundos**: rectángulo de esquinas redondas, relleno `#F8F2EC`, texto cobre 10 pt Bold,
  `2 s` `5 s` `3 s` `5 s` `5 s`. Los cinco números suman 20 y eso tiene que verse.

### Los códigos del calendario

`K1` `K2` `K3` `PS` `R` `KI` se escriben siempre como chip: borde cobre de 1 pt, sin
relleno, esquinas de 2 mm, letra 9,5 pt Bold cobre, relleno interno de 2 mm. Se usan igual
en el calendario, en la hoja de registro y adentro del texto.

### Las pestañas de las tres páginas que se vuelven a abrir

Los capítulos 4 (el mapa), 11 (el freno) y 14 (el calendario) son a los que el lector
vuelve. Cada uno lleva una **pestaña de cobre pegada al borde derecho**: rectángulo de
4 × 30 mm, sin margen, a tres alturas distintas (60 mm, 110 mm y 160 mm desde arriba).

Cuando pasás el dedo rápido por el PDF en el celular, las tres pestañas aparecen a
distinta altura y las encontrás sin índice. Es el mismo truco de las agendas de papel.

### Imágenes

Ninguna foto de persona. Solo el gráfico del mapa, el calendario, la hoja de registro y
los chips. Todo se dibuja con rectángulos y texto: cero stock, cero IA, cero créditos
gastados.

---

## 3. El gráfico del mapa del 1 al 10 (capítulo 4, página entera)

Está dibujado en `PORTADA.html`, panel 3. Es el corazón del producto: si Paolo solo hace
una página bien, es esta.

### La idea que lo hace distinto

**Las bandas no miden lo mismo.** Del 1 al 5 son anchas, del 8 al 10 son finitas. El
dibujo enseña solo la regla 2 del capítulo: entre el 8 y el 9 casi no hay nada. No hace
falta leer el párrafo para entenderlo.

Y el color sube de blanco a cobre a negro: abajo hay luz, en el 7 está la raya, arriba se
cierra el túnel.

### Medidas, en mm sobre la hoja de 152 × 229

- Barra vertical de **26 mm de ancho**, de 135 mm de alto, arrancando a 30 mm del borde
  izquierdo. El 1 abajo, el 10 arriba.

| Nivel | Alto de la banda | Relleno | Número |
|---|---|---|---|
| 1 | 18 mm | `#F2F0ED` | tinta, 12 pt Bold |
| 2 | 18 mm | `#EFEDE9` | tinta |
| 3 | 18 mm | `#EBE8E4` | tinta |
| 4 | 16 mm | `#E8E5E0` | tinta |
| 5 | 16 mm | `#E4E1DC` | tinta |
| 6 | 14 mm | `#DEDAD4` | tinta |
| **7** | **14 mm** | **`#AD6015`** | **blanco, 17 pt ExtraBold** |
| 8 | 9 mm | `#2D3138` | blanco |
| 9 | 7 mm | `#1D2128` | blanco, 10 pt |
| 10 | 5 mm | `#12161C` | blanco, 9 pt |

- **Lengüeta de cobre** de 6 × 8 mm pegada al lado izquierdo de la banda 7: es lo que
  saca al 7 de la fila y lo convierte en "la línea".
- A la derecha de la barra, a 12 mm, la columna de etiquetas en 10 pt gris `#55585E`,
  cada una centrada con su banda. La del 7 va en dos renglones: **`AQUÍ FRENAS.`** en
  13 pt ExtraBold cobre, y debajo "Se siente que va en serio. Todavía es tuyo." en 9,5 pt.
- **Línea punteada** de 1 pt tinta, guion de 5 y hueco de 5, cruzando toda la página en la
  frontera entre el 8 y el 9. Es el punto sin retorno.
- Debajo de todo, una raya `#E3E1DD` y el pie en 11 pt Bold cobre:
  _"Los últimos escalones son más cortos. Ahí está toda la trampa."_

### La versión chica

Los capítulos 5, 11 y 13 repiten el mapa como recuadro: la misma barra **sin etiquetas y
sin números**, de 8 mm de ancho por 60 mm de alto, en el margen derecho, con un `7` en
cobre al lado de la banda naranja. Se arma una vez, se agrupa y se copia.

---

## 4. El calendario y la hoja de registro

### 4a. La hoja para marcar (capítulo 14, página entera)

Es la página que se guarda en el carrete de fotos. Todo lo que hay que hacer en 21 días,
en una sola pantalla.

**Grilla de 3 columnas × 7 filas.** Cada columna es una semana.

| Qué | Valor |
|---|---|
| Celda | 36 mm de ancho × 22 mm de alto |
| Separación | 4 mm (3 × 36 + 2 × 4 = 116 mm, entra en los 120 de la columna) |
| Borde de la celda | 1 pt `#E3E1DD`, esquinas de 2 mm, fondo blanco |
| Número del día | arriba a la izquierda, 15 pt ExtraBold tinta |
| **Casilla para marcar** | arriba a la derecha, cuadrado de **6 × 6 mm**, borde 1,2 pt tinta, esquinas de 1 mm, vacío |
| Códigos | al medio, chips de cobre: `K1` `PS` |
| Minutos | abajo, 9 pt gris: `20 min` |
| Días con sesión (PS) | barra de cobre de 2 mm pegada arriba de la celda |

**Por qué la casilla mide 6 mm:** es el mínimo que se puede tocar con el dedo o tildar con
una lapicera sin errar. Más chica se convierte en adorno.

Encabezado de cada columna: barra de cobre de todo el ancho, 8 mm de alto, texto blanco
10 pt Bold en mayúsculas: `SEMANA 1 · CONOCER EL CUERPO`, `SEMANA 2 · CONTROL BAJO
PRESIÓN`, `SEMANA 3 · LLEVARLO A LA CAMA`.

Abajo de la grilla, las dos reglas del calendario en una caja `OJO CON ESTO`.

**Se exporta además como PNG suelto** (1200 × 1800 px) para que el comprador lo baje al
celular sin abrir el PDF. Canva puede: seleccionar solo esa página al descargar.

### 4b. El detalle día por día (2 páginas)

Las tablas de `CONTENIDO.md` tal cual, con el modelo de tabla de arriba, alto de fila
12 mm, tres columnas: `DÍA` (12 mm) · `QUÉ HACES` (88 mm) · `MIN` (20 mm). Los códigos
dentro de la columna del medio van como chips.

- Página A: semana 1 y semana 2.
- Página B: semana 3 y las dos reglas.

### 4c. La hoja de registro (capítulo 18, 3 páginas, una por semana)

Una página por semana, idénticas, tituladas `SEMANA 1`, `SEMANA 2`, `SEMANA 3`. Tres
páginas y no una porque se llena tres veces, no una sola.

Anchos de columna sobre los 120 mm:

| Columna | Ancho | Cómo se llena |
|---|---|---|
| Día | 12 mm | ya impreso: 1 a 7 |
| ¿Hice el Kegel? | 16 mm | **cuadrado de 5 mm** centrado |
| Sesión | 16 mm | **cuadrado de 5 mm** centrado |
| Número máximo sin frenar | 20 mm | línea punteada cobre al 30 % |
| Ciclos | 16 mm | línea punteada cobre al 30 % |
| Nota | 40 mm | línea punteada cobre al 30 % |

- Alto de fila: **9 mm**. Es lo mínimo para escribir a mano sin pisarse.
- Las celdas para llenar **nunca van vacías del todo**: o tienen el cuadrado o tienen la
  línea punteada. Una celda en blanco no se lee como "escribí acá".
- Debajo de la tabla, el cierre de la semana: las tres preguntas, cada una con tres
  círculos de 5 mm para rellenar, etiquetados `Sí` · `A veces` · `No`.

---

## 5. Cómo armarlo en Canva, paso a paso

**Antes de empezar:** son unas 4 horas la primera vez. No se pule más que eso. Publicado y
prolijo le gana a perfecto y guardado.

1. **Crear el diseño.** Canva → Crear un diseño → Tamaño personalizado → **152 × 229 mm**.
   Nombre: `Durar mas - plan de 21 dias`.

2. **Cargar la paleta una sola vez.** Dibujá un rectángulo cualquiera, abrí el selector de
   color, tocá el `+` y tipeá los seis códigos: `12161C`, `AD6015`, `E0954A`, `F8F2EC`,
   `E3E1DD`, `FFFFFF`. Quedan en "Colores del documento" y ya no se tipean más. Borrá el
   rectángulo.

3. **Fijar las guías.** Archivo → Configuración → Agregar guías → Personalizado. Márgenes
   16 mm a los lados, 18 arriba, 20 abajo.

4. **Armar la página de prueba con los tres estilos de texto.** Tres cuadros: 26 ExtraBold,
   15 Bold, 12,5 Regular con interlineado 1,6. Se copian de ahí toda la vida. Esta página
   se borra al final.

5. **Armar cuatro páginas maestras y recién después escribir.** (a) apertura de capítulo,
   (b) página de texto, (c) página de tabla, (d) página de gráfico. Después es duplicar y
   reemplazar, no dibujar de nuevo.

6. **El pie de página.** Canva no numera solo en este tipo de diseño: armá el pie una vez
   (raya + nombre + número), agrupalo, copialo en todas las páginas y editá el dígito. Son
   unos 10 minutos para 28 páginas. Que sea aburrido no lo hace opcional.

7. **El mapa del 1 al 10.** Diez rectángulos apilados: dibujá uno, copiá diez veces,
   ponéles el alto de la tabla del punto 3 (Posición → alto, en mm), alineá todos a la
   izquierda y usá "Organizar" para que queden pegados sin hueco. Coloreá. Después
   agregá la lengüeta de la banda 7 y las etiquetas. Agrupá todo: lo vas a copiar tres
   veces más en versión chica.

8. **Los chips.** Un rectángulo redondeado, sin relleno, borde cobre de 1 pt, con el texto
   encima. Agrupalo. Copiar y pegar en todos lados cambiando las letras.

9. **La grilla del calendario.** Armá **una** celda completa (borde, número, casilla,
   chips, minutos), agrupala, duplicala 6 veces hacia abajo, alineá con "Organizar", y
   después duplicá la columna entera dos veces al costado.

10. **El índice con links.** Escribí las 18 líneas, seleccioná cada una y Ctrl+K →
    "Páginas de este diseño" → elegí la página. Probalo tocándolo en el celular: si el
    link no salta, el índice no sirve.

11. **Las tres pestañas.** Rectángulo de 4 × 30 mm en cobre, pegado al borde derecho
    (posición X = 148 mm), en las páginas del mapa, del freno y del calendario, a 60, 110
    y 160 mm de altura.

12. **Exportar.** Compartir → Descargar → **PDF estándar** (nunca "PDF para imprimir": pesa
    el triple y no aporta nada en pantalla). Nombre: `durar-mas-plan-21-dias.pdf`. Tiene
    que pesar menos de 20 MB.

13. **Las piezas sueltas.** Descargá como PNG, seleccionando solo esas páginas: la portada
    (para la galería de Whop), el calendario y la hoja de registro.

14. **La portada en grande y el banner.** Diseño nuevo de 1800 × 2700 px para la portada
    sola, y otro de 1920 × 1080 px para el banner de Whop: el mismo medidor pero acostado,
    el título a la izquierda y la barra 7 a la derecha, con lo importante en el centro por
    si Whop recorta.

15. **La prueba final.** Mandate el PDF por WhatsApp a vos mismo, abrilo en el celular y
    sin hacer zoom: ¿se lee el texto? ¿saltan los links del índice? ¿se ven las tres
    pestañas al pasar el dedo? Si algo falla ahí, falla para todos.

---

## 6. El plan de páginas: 28

| # | Qué va |
|---|---|
| 1 | Portada |
| 2 | Índice con links |
| 3 | Cap. 1 · Cómo usar esta guía — **es el "empezá acá"** |
| 4 | Cap. 2 · Motivos 1 y 2 |
| 5 | Cap. 2 · Motivo 3 + los tres se arreglan con lo mismo |
| 6 | Cap. 3 · El test, los 10 con casilla |
| 7 | Cap. 3 · Cómo se lee (tabla) |
| 8 | **Cap. 4 · El mapa del 1 al 10, página entera** · pestaña |
| 9 | Cap. 4 · Las dos reglas + calibración del día 2 |
| 10 | Cap. 5 · Parar y seguir, los 7 pasos numerados |
| 11 | Cap. 5 · Series, frecuencia, los 3 niveles y el error |
| 12 | Cap. 6 · La técnica del apretón |
| 13 | Cap. 7 · Encontrar el músculo, las 3 formas |
| 14 | Cap. 7 · Cómo saber que va bien + Kegel inverso |
| 15 | Cap. 8 · La rutina de 3 semanas (tabla) |
| 16 | Cap. 9 · Los 5 errores |
| 17 | Cap. 10 · Respiración 4 y 6 |
| 18 | **Cap. 11 · El freno de 20 segundos** + caja "lo que no funciona" · pestaña |
| 19 | Cap. 12 · Por qué la primera vez es la peor |
| 20 | Cap. 12 · El plan de la noche + ordenar la noche + los 3 frenos |
| 21 | Cap. 12 · Las dos frases + si igual pasa + ensayo mental |
| 22 | Cap. 13 · Alarga / apura (tabla) + los 3 movimientos |
| 23 | **Cap. 14 · La hoja para marcar, 21 casillas** · pestaña |
| 24 | Cap. 14 · Semana 1 y 2 en detalle |
| 25 | Cap. 14 · Semana 3 + las dos reglas |
| 26 | Cap. 15 · Qué esperar semana a semana + cap. 16 resumido en tabla |
| 27 | Cap. 17 · Después del día 21 |
| 28 | Cap. 18 · Hoja de registro, semana 1 |
| +2 | Hoja de registro semanas 2 y 3 |

Da 28 más las dos hojas de registro repetidas: **30 páginas**. Si alguna queda apretada al
maquetar, se parte en dos y son 31. La regla que manda no es el número de páginas, es una
idea por página.

---

## 7. Revisión final: las 5 preguntas

| Pregunta | Respuesta |
|---|---|
| ¿Se entiende en un segundo, en el celular? | Sí: DURAR MÁS y una barra encendida |
| ¿Usa solo lo que dice la ficha? | Sí: dos colores, Open Sans, tres tamaños |
| ¿Hay algo inventado? | No: cero sellos, cero "más vendido", cero estrellas, cero testimonios, cero cifras. Todo lo que se dibuja existe adentro del PDF |
| ¿El texto es el de Whoper? | Todavía no escribió. El de la tapa queda propuesto y él lo confirma o lo cambia |
| ¿Llevó más de una tarde? | El diseño está decidido. Armarlo son ~4 horas |

---

## 8. Para la torre de control

Cuando esta carpeta se lea desde el chat central, lo que corresponde pasar a
`digimones/diseno.md` (no está creado todavía) es la ficha de estilo:

```
Producto: Durar más — el plan de 21 días
Comprador: hombre de 20 a 35 que termina antes de lo que quiere
Color de texto: #12161C (grafito)
Color de acento: #AD6015 (cobre) — es el del botón del checkout
Acento aclarado, solo sobre fondo oscuro: #E0954A
Fondo: blanco. Caja: #F8F2EC. Línea: #E3E1DD
Letra: Open Sans (ExtraBold, Bold, Regular)
Tamaños: título 26 · subtítulo 15 · texto 12,5 (interlineado 1,6)
Hoja del PDF: 152 × 229 mm, márgenes 16/16/18/20
Decidido el: 23/09/2026
```

Dos cosas aprendidas que sirven para el próximo producto y no están en el método:

1. **En un nicho donde el comprador se esconde, la tapa dice menos que la página de
   venta.** El subtítulo largo vende; el corto se puede tener en el celular. Vale la pena
   tener las dos versiones desde el principio.
2. **El gráfico central conviene que sea la portada.** Acá el mapa del 1 al 10 es la tapa,
   el ícono y la herramienta. Una sola idea dibujada tres veces vale más que tres dibujos.
