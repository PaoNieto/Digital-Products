# Notas del producto: reducir cintura y marcar abdomen

_Elegido el 23/09/2026. El ranking que lo eligió está en
`productos/fitness-mujeres/SUBNICHOS.md`._

## Precio y plata (Mercaneto, 23/09/2026)

| | |
|---|---|
| Precio | **US$27** (unos S/97) |
| Rango con sentido | US$19 a US$40 (es la banda con alumnas visibles en el nicho) |
| Queda por venta | **US$25.20** en el peor caso (tarjeta de fuera de EE. UU. con conversión); US$25.87 con tarjeta de EE. UU. |
| Mordida real | 6.7% del precio, no 2.7%: el fijo de US$0.40 pesa en un ticket chico |
| Las 10 ventas | entran US$270, quedan ≈ US$250 (unos S/900) |
| Garantía | **7 días**, sin preguntas |
| Techo por compradora | US$25.20 (unos S/91) |
| Primer retiro | con unas 21 ventas (US$514). Con 10 ventas no se retira: el wire de US$23 se lleva 9% |

- **Por qué 7 días de garantía y no 30:** el reto dura 28 días. Con 30 días, la compradora
  lo hace entero y pide la plata de vuelta.
- **Devolución:** cuesta US$1.80 además de la venta. **Contracargo:** US$27 + US$15 = US$42,
  y con 10 ventas uno solo es 10% de disputas. Pedido de devolución, se devuelve el mismo
  día.
- **Lo que cambia el precio:** con 100 visitas a la página y 0 ventas, probar US$19 antes
  de tocar el producto.
- **Arriba de US$35 la compradora espera video:** los dos productos del nicho por encima
  de ese precio son en video.
- Los números de Whop salen de `CLAUDE.md` (verificados el 21/09/2026). Tipo de cambio
  S/3.6 por dólar (supuesto).

## Los 3 huecos de la competencia (El Gato, 23/09/2026)

Desarme de las 4 ofertas que venden (Zuriworkout, Quema de Grasa Extremo, Reto Express de
Hipopresivos, Real Fit).

| Hueco | Qué hacemos |
|---|---|
| **Nadie entrega cómo medirse**, aunque las 4 prometen centímetros | Ya es el corazón del reto: "tu número de partida", medición de 9 a 9 y hoja de seguimiento |
| **La garantía es más corta que la promesa**: 3 días para un reto de 28, 7 para uno de 8 semanas, Real Fit sin garantía | Decisión pendiente de Paolo: 7 días (Mercaneto) o 30 días como argumento de venta |
| **Ninguna trae lista de compras**, y "no paso nada de hambre" es lo que más repiten las reseñas reales | Ya sumado al contenido: una hoja por semana, con lo que se consigue en un mercado de Lima |

Lo que copiamos de su plantilla: plazo en el nombre, un solo pago, entrega en área de
miembros, y el bloque "lo que ya probaste y no funcionó" en la página de venta. Lo que no
copiamos: testimonios inventados y "acceso de por vida".

Dato para el segundo escalón: Dance Fit Couple lanzó el 11/09/2026 una suscripción de
US$29/mes y adentro metió justo el kit de medición.

## La voz de la clienta (Vegeta, 23/09/2026)

De 3,246 comentarios de YouTube, reseñas de Amazon y Hotmart, y foros.

- **La palabra decide la edad.** De los 71 comentarios donde se dice la edad, **48 son
  adolescentes de 12 a 19 (68%)**, y están concentrados en los videos de "cintura de
  avispa". Los videos de "hipopresivos" y "desinflamar" tienen **0 adolescentes**. Misma
  panza, dos públicos: uno no tiene tarjeta. **Los anuncios van por "desinflamar" y
  "hipopresivos", nunca por "cintura de avispa".**
- **"Panza" es la palabra del anuncio; "abdomen", la de la página de venta.** En las
  reseñas de Hotmart nadie escribe "panza": todas escriben "abdomen".
- **Miden en centímetros, no en kilos.** 125 comentarios dan su medida en cm y varias
  aclaran "no tengo báscula". Por eso el producto mide tres puntos: cintura, abdomen y
  abdomen bajo.
- **Las dos quejas que nadie contesta bien:** el abdomen bajo y la hinchazón. La respuesta
  estándar de los foros es "déficit calórico", que no resuelve ninguna de las dos.
- **La objeción más dura, textual:** "hay muchos videos en YouTube que te pueden ayudar".
  La página de venta tiene que contestarla de frente.
- **Abandonan:** 348 comentarios arrancan un reto y solo 78 vuelven a contar algo (22%).
- **Lo que califican mal en lo que ya existe:** poca ilustración, no se entiende cómo se
  hace el ejercicio, mucha teoría, y "no pude abrir el archivo".

Frases para usar tal cual en el anuncio y en la página: "bajé 8 kilos y mi panza sigue
igual" · "no quiero bajar de peso, quiero desinflamarme" · "parezco embarazada de 4 o 5
meses" · "estoy re cuadrada" · "dejé de creer en milagros".

## Diseño (Diseñante, 23/09/2026)

La ficha completa está en `DISENO.md`. Lo que conviene que la torre de control pase a
`digimones/`:

- **Verde jade `#0E7C66` + Open Sans.** El verde salió por descarte: las 4 competidoras
  que trajo El Gato van con rojo, naranja y negro de "quema grasa", y el ángulo de este
  producto es el opuesto (no es grasa, es hinchazón y postura). Open Sans porque es
  gratis, está en Canva y es una de las 3 letras del checkout de Whop: el botón de pago
  hace juego con el PDF sin trabajo extra.
- **Las ilustraciones de ejercicios se generan con código, no con IA de imágenes.** Un
  modelo de imagen cambia de trazo en cada tirada e inventa brazos de más; con 25 dibujos
  eso se nota. `ilustraciones/generar.py` arma la silueta siempre con las mismas piezas y
  solo cambia las coordenadas de las articulaciones. Sirve para cualquier producto de
  ejercicios que venga después.
- **Esto ataca dos quejas que Vegeta encontró en lo que ya existe:** "poca ilustración, no
  se entiende cómo se hace el ejercicio" y "no pude abrir el archivo". El PDF pesa 383 KB
  y son 30 páginas: baja con datos del celular.
- **El PDF y la tapa se arman con el Chrome que ya está instalado** (HTML a PDF). Cero
  créditos, cero suscripción, cero Canva. `construir.py` rehace las 4 piezas y
  `revisar.py` avisa qué página se desborda antes de exportar.
- **Higgsfield está en plan gratis con 0 créditos** (chequeado el 23/09/2026): hoy no
  sirve para generar imágenes.
- **Hoja de 6 × 9 pulgadas, no A4**, para que se lea en el celular sin zoom.
- El número que movió una decisión: el fondo de las cajas daba 4.49 : 1 de contraste, una
  centésima por debajo del mínimo AA. Se aclaró de `#E8F2EF` a `#EDF5F2`.

Falta de diseño: las 3 imágenes de la página de Whop, y abrir el PDF en un celular de
verdad (chequeo 3 de Whoper).

### Segunda pasada, 23/09/2026

- **Las 27 ilustraciones están listas**, una por cada ejercicio de las 7 rutinas. Cada
  ejercicio del PDF es la misma fila: dibujo a la izquierda (un tercio del ancho), nombre
  y dosis a la derecha, el cómo debajo. Entran 4 por hoja.
- El PDF quedó en **38 páginas** (era 30). Entraron las tres páginas nuevas de
  `CONTENIDO.md`: los tres puntos de medición, "Hablemos del abdomen bajo" y "¿Lo estoy
  haciendo bien?".
- La hoja de seguimiento A4 ahora tiene los tres puntos (cintura, abdomen, abdomen bajo)
  para el día 1 y el día 28, y sigue entrando en una sola hoja.
- **Decisión que conviene mirar:** la página "Día 28" de `CONTENIDO.md` todavía trae la
  tabla vieja de dos números (fila día 1 / fila día 28). La maqueté con los tres puntos,
  igual que la página de partida, porque el texto dice "volvé a medirte igual que el día
  1" y dejar dos tablas distintas parecería un error del producto. Si el-panadero quiere
  la tabla vieja, se cambia en un minuto.
- Dos cosas nuevas que el generador hace solo: avisa si una flecha se sale del marco (fue
  el único error real que apareció) y rehace la hoja de contacto con las 27, así nunca
  queda vieja.

## Pendiente

- Comprador, promesa, formato e índice (el-panadero).
- Voz de la clienta: frases textuales (Vegeta).
- Desarme de las 4 ofertas que ya venden (El Gato).
- Segundo escalón: qué se le vende después del reto. Candidatos de la fila de espera:
  hipopresivos y glúteos en casa.
