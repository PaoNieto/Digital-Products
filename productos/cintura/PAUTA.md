# Pauta: PLANA TODO EL DÍA

_Bilbito (pauta), 23/09/2026. Plan en papel, no orden de lanzamiento._

**Nombre del producto (elegido por Paolo, 23/09/2026):**
**PLANA TODO EL DÍA** — Reto de 28 días para desinflamar el abdomen y marcar cintura.
10 min al día, sin dieta, sin equipo.

Se retiran "Abdomen Desinflamado" y "Cintura de 9 a 9". La promesa no cambia: que la
cintura mida lo mismo a las 9 de la noche que a las 9 de la mañana.

**Cómo se escribe el nombre en un anuncio.** En pantalla va siempre completo y en dos
renglones, el reto abajo del nombre:

> **PLANA TODO EL DÍA**
> Reto de 28 días · 10 min al día · sin dieta · sin equipo

Y una advertencia de política que viene con el nombre, en la sección 7: la palabra
"plana" es marca, no promesa. Nunca se conjuga hacia quien mira ("vas a quedar plana",
"quedá plana en 28 días") y nunca aparece encima de un cuerpo.

## Lo primero: la compuerta está cerrada

`CLAUDE.md` marca **0 de 10 ventas a desconocidos**. Hasta que diga 10 de 10, **no se
gasta un sol acá**. Este archivo se escribe ahora para que el día 1 no se improvise, no
para prender nada.

Por qué no se saltea: con 0 ventas no sabés si falla el anuncio, la página o la oferta. Y
el dato que hace legible esta prueba —cuántas de cada 100 visitas compran— sale de las 10
ventas orgánicas, no de Meta.

> Lo que abre esta compuerta: la línea "Ventas a desconocidos: 10 de 10" en `CLAUDE.md`.

**Dos cosas que faltan además de las ventas:**

| Falta | Quién | Por qué bloquea |
|---|---|---|
| Anuncios activos del nicho en la Biblioteca de anuncios de Meta | El Gato | `digimones/mercado.md` dice que la Biblioteca no se abrió. El método es **modelar, no inventar**: los primeros creativos deberían copiar el esqueleto de lo que ya corre hace 3+ días. Los 10 ganchos de abajo salen del producto y de la compradora, no de un ganador espiado. Es la debilidad conocida de este plan |
| Confirmar que Meta deja optimizar a **Compra** | Bilbito, al abrir la cuenta | Meta limita desde 2025 (al menos en EE. UU.) que los negocios que clasifica como salud y bienestar optimicen a Compra. **No verificado para Paolo.** Si está bloqueado, el plan B es optimizar a *Iniciar pago* y leer las compras en Whop |

---

## Los números base

| Qué | Valor | De dónde |
|---|---|---|
| Precio | US$27 | `NOTAS.md` |
| Deja cada venta (peor caso) | **US$25.20** | `NOTAS.md` / `CLAUDE.md` |
| Techo por compradora | **US$25.20** (S/93) | Mercaneto |
| Presupuesto de la prueba | **S/1,000 ≈ US$270** | `CLAUDE.md` |
| Punto de empate de la prueba | **11 ventas** (270 ÷ 25.20 = 10.7) | cuenta |

Tipo de cambio de trabajo: **S/3.7 por dólar** (supuesto; `NOTAS.md` usa S/3.6 para el
precio, la diferencia no cambia ninguna decisión).

### El techo por visita: la única cuenta que manda

```
costo por visita (CPV)  <  lo que deja cada visita (RPV)  →  el anuncio paga solo
```

| Si compran… | Techo del CPV | En soles |
|---|---|---|
| 1 de cada 100 (1%) | **US$0.25** | S/0.93 |
| 2 de cada 100 (2%) | **US$0.50** | S/1.86 |
| 3 de cada 100 (3%) | **US$0.76** | S/2.81 |

Las tres tasas son **supuestos** hasta que Whop muestre la real. Objetivo de trabajo:
**CPV por debajo de US$0.25**, que aguanta incluso si solo compra 1 de cada 100.

CPV no es CPC. El CPC es lo que cuesta el clic; el CPV, lo que cuesta una visita que sí
cargó la página. La diferencia se evapora en silencio.

---

## 1. La estructura de la prueba

**Dónde:** Meta (Facebook e Instagram) desde **Whop Ads**, en el panel de Whop. Whop
registra la compra en su servidor y se la pasa a Meta: no hay pixel que instalar.
Lo que cambia esta decisión: que Whop Ads rechace la categoría (fitness/salud) o que las
10 ventas orgánicas hayan salido de TikTok.

| Qué | Cómo |
|---|---|
| Objetivo | Ventas · conversión en sitio web · evento **Compra** |
| Presupuesto | **ABO**: una canilla por maceta. Presupuesto a nivel conjunto, el de campaña apagado |
| Conjuntos | **4**, uno por creativo. 1 anuncio por conjunto |
| Fotos y videos | **Nunca en el mismo conjunto.** Tanda 1: 2 conjuntos de imagen + 2 de video |
| Plata por conjunto | **US$8 por día** (S/30) |
| Gasto diario | **US$32** (S/118) |
| Puja | La que más resultados trae (volumen). Tope de costo recién para escalar |
| Arranque | 00:00 del día siguiente. Sin fecha de fin: se apaga a mano |
| Segmentación | Ver sección 6. Audiencia automática **apagada** |
| Ubicaciones | Automáticas **sí** (ahí Meta busca el clic barato). Mejoras creativas con IA **apagadas todas** |
| Nombres | Campaña `testeo - 2026-XX-XX - cintura` · conjunto `XX-XX - creativo 1` |

### Por qué 4 conjuntos a US$8 y no 6 a US$6.50

Porque la regla de corte dice que **antes de gastar cerca del techo (US$25.20) no se
decide nada**, y a US$8 por día un conjunto llega a US$24 —el 95% del techo— exactamente
a las 72 horas. Con US$6.50 harían falta 4 días para tener derecho a matarlo, y la prueba
no aguanta esa espera. 4 conjuntos son menos tiros, pero cada tiro se puede leer.

### Cómo se reparten los US$270

| Bloque | Días | Gasto | Acumulado |
|---|---|---|---|
| Tanda 1: 4 creativos nuevos | D1 a D3 | US$96 (S/355) | US$96 |
| Tanda 2: sobrevivientes + relevos | D4 a D6 | US$96 (S/355) | US$192 |
| Colchón para desfasajes y el domingo | D7 | hasta US$8 | US$200 |
| **Reserva intocable** | D8 a D14 | **US$70 (S/260)** | US$270 |

**La reserva no está presupuestada: se gana.** Solo se toca si en la semana 1 apareció un
ganador, y se usa viernes a domingo, que es cuando el ticket bajo compra por impulso.
Si no hubo ganador, los US$70 no se gastan: se diagnostica.

**Dato duro que hay que aceptar:** S/1,000 no compra 14 días de prueba. Compra entre 6 y 8
días de lectura limpia. La semana 2 se financia con ventas o no existe.

---

## 2. Reglas de corte y de escalado

### El interruptor general (se anota en `CLAUDE.md` antes de gastar)

| Se apaga TODO el test si… | Por qué |
|---|---|
| Se gastaron **US$100 (S/370)** y no hubo **ni un pago iniciado** en Whop | Son 4 presupuestos de compradora enteros. Si nadie ni siquiera abrió el cobro, el problema está arriba del anuncio: es la oferta o la página |
| Se gastaron **US$50 (S/185)** y hay **menos de 100 visitas** | El CPV está sobre US$0.50. A ese precio harían falta 3 de cada 100 comprando: no da |

### Corte por creativo, según el reloj

El embudo se lee de arriba hacia abajo, y el reloj también: a las 12 horas se mata por
falla de arriba (nadie clickea), no por falla de abajo (nadie compra).

| Momento | Gastó | Se apaga si… | No se toca si… |
|---|---|---|---|
| **12 h** (D1 mediodía) | ~US$4 | Más de 500 impresiones y **cero clics en el enlace**, o CTR bajo **0.5%** | Tiene clics aunque no haya ventas: es muy pronto |
| **48 h** | ~US$16 | CTR bajo **1%** (la mitad del piso de Bilbao) | La carga de página está bajo 70%: eso no es del anuncio, es de la página → Whoper y Diseñante |
| **72 h** (D3 noche) | **~US$24 = 95% del techo** | Sin ventas **ni pagos iniciados** → apagar, sin apego | — |
| **72 h** | ~US$24 | Vendió 1 al costo del techo → **changüí de US$1 a 2** (S/4 a 7). Si gasta eso sin vender, apagar | — |
| **72 h** | ~US$24 | Vendió con costo **muy por debajo** del techo → **dejar correr** y mirar todos los días | — |
| Cualquier día | — | Vende pero se encarece → **tirón de oreja**: bajar 30% el presupuesto. Si al otro día mejora, se vuelve a subir | — |

Un test nunca dura más de 72 horas. De 10 creativos suelen quedar 2 o 3.

### Escalar

| Señal | Qué se hace |
|---|---|
| 3 o 4 ventas bajo el techo en 7 días | "Buena pinta": se prueba **un fin de semana** con la reserva de US$70 |
| 6 ventas bajo el techo | Aceptable: +15% de presupuesto por día, solo viernes a domingo |
| 10 ventas o más bajo el techo | Ganador confiable: se escala en serio |
| Costo por compradora bajo **US$15** (60% del techo, supuesto de trabajo) con 3+ ventas | Se abre la canilla antes de esperar los 7 días |
| Subió el presupuesto y al otro día no vendió | **No se vuelve a subir** hasta que mejore |

Tres candados:

1. **Nunca se escala lo que no ganó en el test.** Ni por corazonada, ni por likes.
2. **La plata del escalado sale de las ventas, no de los S/1,000.** Los S/1,000 compran el
   dato del CPV; las ventas compran el volumen.
3. Con estos números Meta **no va a salir de la fase de aprendizaje** (pide unas 50 compras
   por semana por conjunto). Esta prueba no escala: mide.

---

## 3. Qué mirar y en qué orden

El embudo es una manguera: se busca dónde se tranca el agua. Arreglar donde no está el
freno es tirar tiempo. Una cosa por vez, de arriba hacia abajo.

| # | Métrica | Esperado | Si falla, significa | Quién lo arregla |
|---|---|---|---|---|
| 1 | **Entrega** (¿gastó el presupuesto?) | Gasta sus US$8 | Gastó menos del 50%: público muy chico, puja mal puesta o anuncio en revisión | Bilbito |
| 2 | **CPM** | Sin umbral. Se anota el del día 1 como **línea base propia de Paolo** | Sube 50% sobre esa línea: fatiga del creativo o público saturado | Bilbito |
| 3 | **Hook rate** (repro. de 3 s ÷ impresiones, solo video) | **más de 50%** (Bilbao, no verificado) | Los primeros 3 segundos no frenan el dedo. Se cambian **solo** los primeros 3 segundos, el resto del guion queda | Bilbito |
| 4 | **CTR del enlace** | **2 a 3%**; ganador más de 3% | Bajo 1%: gusta pero no da motivo para entrar. Falta el llamado o la promesa es vaga | Bilbito |
| 5 | **Carga de página** (visitas ÷ clics) | **más de 70%** (ideal 85 a 95%) | Pagaste clics que nunca vieron la página. Casi siempre son imágenes pesadas | Whoper y Diseñante |
| 6 | **CPV** (gasto ÷ visitas) | **bajo US$0.25** | Arriba de US$0.50 la oferta no paga a ninguna tasa realista. Es más fácil bajar el CPV que subir la conversión: primero el creativo | Bilbito |
| 7 | **Pagos iniciados ÷ visitas** | Sin umbral. Línea base propia | 100+ visitas y **cero** pagos iniciados: la página no cierra o el precio asusta | Whoper y Mercaneto |
| 8 | **Compras ÷ visitas** (dato de **Whop**) | **2.5 a 3%** (Conde: 2%+) | Llegan visitas, no compran: promesa, prueba, o la página no cumple lo que prometió el anuncio | Whoper |
| 9 | **Compras ÷ pagos iniciados** | Sin umbral | Muchos pagos iniciados y pocas compras: se traba en el cobro (checkout, FAQ, garantía) | Whoper y Mercaneto |
| 10 | **Costo por compradora vs techo** | **bajo US$25.20** | Arriba del techo, cada venta pierde plata | Mercaneto y Bilbito |

**El panel de Meta exagera las compras.** La fuente dura son las ventas que registra Whop.
Un estudio con 663 experimentos reales en Facebook encontró que la atribución habitual
sobreestima el efecto de los anuncios varias veces.

### La cadena, con un ejemplo aritmético

Solo para ver cómo encajan los eslabones. **El CPM de US$5 es un supuesto sin verificar
para Perú y LatAm hispano**: el día 1 se reemplaza por el real y se rehace la cuenta.

| Eslabón | Cuenta | Resultado |
|---|---|---|
| Gasto del día | — | US$32 |
| Impresiones | 32 ÷ 5 × 1,000 | 6,400 |
| Clics en el enlace (CTR 2%) | 6,400 × 0.02 | 128 |
| Visitas (carga 75%) | 128 × 0.75 | 96 |
| **CPV** | 32 ÷ 96 | **US$0.33** |
| Compras (conversión 2.5%) | 96 × 0.025 | 2.4 |
| **Costo por compradora** | 32 ÷ 2.4 | **US$13.3** — bajo el techo |

Si el CPM real sale el doble, el CPV se va a US$0.66 y la prueba muere ahí: se rehacen los
creativos, no la página.

---

## 4. Diez ganchos, listos para usar

Reglas que cumplen los diez: nada de antes y después del cuerpo, nada que le señale el
cuerpo a quien mira (tercera persona o el objeto, nunca "tu panza"), cero promesa de peso
o de kilos, cero "detox". Todos se producen con imagen generada, texto en pantalla o
animación simple. **Carrusel no entra: rinde mal.**

| # | Gancho literal (primeros 3 s o titular) | Formato | Por qué puede funcionar |
|---|---|---|---|
| 1 | **"9:00 a.m.: cierra. 9:00 p.m.: no cierra. El mismo jean."** | Video de texto: dos imágenes generadas del mismo jean sobre la misma silla, luz de mañana y luz de noche | Es la escena exacta de la compradora, contada con un objeto y no con un cuerpo. La brecha entre las dos fotos la abre el anuncio y la cierra el producto |
| 2 | **"El error que comete casi toda la que hace abdominales para marcar cintura."** | Imagen: diagrama de línea de las dos capas del abdomen, con un título grande | Familia "error de mercado": ataca la creencia, no a la persona. Y el diagrama del mecanismo no lo tiene nadie en el nicho |
| 3 | **"El abdomen tiene dos capas. Los abdominales entrenan la que se ve. La que aprieta es la otra."** | Animación simple: dos anillos concéntricos que se iluminan uno por vez | Mecanismo con nombre propio. Explica en 5 segundos por qué lo que ya hizo no le sirvió, sin decirle que hizo algo mal |
| 4 | **"Ni té, ni faja, ni saltarse la cena."** | Animación simple: tres objetos ilustrados que se tachan uno a uno | Diferenciación por negación ("no es X, no es Y: es Z"). Nombra lo que ya probó sin señalarla. Ojo: se tacha el objeto, nunca se dice "detox funciona/no funciona" como claim de salud |
| 5 | **"Mientras unas suman abdominales, otras están entrenando la capa de adentro."** | Video de texto sobre imagen generada de una colchoneta enrollada | Comparación con el par: mueve sin acusar. Es de las familias más limpias de política |
| 6 | **"28 días. Dos números. Una cinta métrica."** | Imagen: cinta métrica de costura y una hoja con dos casilleros vacíos | Es el hueco de la competencia: las 4 ofertas del nicho prometen centímetros y **ninguna entrega cómo medirse**. Convierte una promesa vaga en algo que ella verifica sola |
| 7 | **"La panza de las 6 de la tarde empieza a las 9 de la mañana, en la silla."** | Video de texto: imagen generada de un escritorio con la pantalla baja, luego la pantalla a la altura de los ojos | Reencuadra la causa hacia algo que ella reconoce (8 horas sentada) y que no es su culpa ni su cuerpo |
| 8 | **"Sin saltos. El vecino de abajo no se entera."** | Imagen: ilustración de un departamento con una colchoneta en el living | Objeción real de la compradora que vive en departamento. Humor suave, cero cuerpo, y filtra a la que odia el cardio de saltos |
| 9 | **"Tiene una rutina de 6 minutos para el día que no da la vida."** | Video de texto: un reloj marcando 23:10 | Vende la terminación, que es el miedo verdadero. La semana 3 es donde abandonan: el anuncio promete el permiso de no abandonar |
| 10 | **"No es grasa. La grasa no aparece en 12 horas."** | Video de texto sobre fondo plano, tipografía grande | Re-hook puro convertido en hook: desarma la culpa en una frase y obliga a quedarse a escuchar qué sí es. Frase textual del producto, así que la página cumple lo que el anuncio dice |

**Cómo se usan:** los 10 no salen juntos. Salen 4 en la tanda 1 (los que menos se parecen
entre sí: **1, 4, 6 y 3**), y los relevos en la tanda 2. Más de un creativo por ángulo,
y el segundo de un ángulo tiene que ser visualmente distinto del primero.

**Dónde va el nombre.** Ninguno de los 10 ganchos abre con el nombre: el gancho es el
problema de ella, no la marca. **PLANA TODO EL DÍA** entra recién en el cierre, sobre la
portada, con el "Reto de 28 días" abajo. Es la regla de Bilbao de "primero el resultado,
después la venta". Se prueba el nombre como titular recién cuando haya un creativo que ya
vende, y como variación de ese, nunca como el primer tiro.

---

## 5. Tres guiones completos

Estructura fija de Bilbao: hook → re-hook → producto → beneficios → qué trae → cómo se usa
→ testimonio → llamado. **El paso de testimonio se saltea: todavía no hay alumnas y
inventar uno es la línea que no se cruza.** Entre guion y guion solo cambian hook y
re-hook; lo demás se repite a propósito.

### Guion A · "El jean de las 9" (22 s, video de texto, sin voz)

| Seg. | Qué se ve | Texto en pantalla |
|---|---|---|
| 0-2 | Imagen generada: jean doblado sobre el respaldo de una silla de oficina, luz de mañana | **9:00 a.m. — cierra** |
| 2-4 | Misma silla, mismo jean, luz de tarde | **9:00 p.m. — no cierra** |
| 4-7 | Fondo plano | No es grasa. La grasa no aparece en 12 horas |
| 7-10 | Fondo plano | Es aire, digestión y una pared abdominal que no sostiene |
| 10-14 | Portada del PDF entrando desde abajo | **PLANA TODO EL DÍA** · Reto de 28 días. Entrena la capa de adentro: la que aprieta como faja |
| 14-17 | Cuatro íconos de línea apareciendo | Sin dieta · sin saltos · sin equipo · 10 min por día |
| 17-19 | Hoja de seguimiento y cinta métrica | 28 fichas + 7 rutinas + hoja de seguimiento |
| 19-22 | Portada quieta | Te medís el día 1 y el día 28. **Link abajo. Garantía de 7 días** |

Producción: 3 imágenes generadas (jean mañana, jean noche, departamento), la portada de
Diseñante, texto en pantalla y música sin letra. Ningún cuerpo en cuadro.

### Guion B · "Las dos capas" (18 s, animación simple)

| Seg. | Qué se ve | Texto en pantalla |
|---|---|---|
| 0-3 | Dibujo de línea: corte de la cintura visto desde arriba, dos anillos concéntricos, ambos grises | **El abdomen tiene dos capas** |
| 3-6 | Se ilumina el anillo **exterior** | La de afuera es la que se ve. Es la que trabajan los abdominales |
| 6-9 | Se ilumina el anillo **interior** | La de adentro es un cinturón. Es la que decide cuánto sale la panza en reposo |
| 9-12 | Exterior grueso, interior parpadeando débil | Años de abdominales inflan una con la otra dormida |
| 12-15 | El anillo interior se cierra y aprieta | El reto de 28 días entrena la de adentro. Por eso el primer ejercicio es respirar |
| 15-18 | Portada del PDF | 10 minutos al día · 28 días · **Link abajo** |

Producción: un solo gráfico vectorial animado con opacidad y escala. Es el creativo más
barato de los tres y el más difícil de rechazar: no hay cuerpo, no hay promesa de peso.

### Guion C · "Lo que ya probaste" (28 s, imágenes generadas + voz en off neutra)

| Seg. | Qué se ve | Voz en off / texto |
|---|---|---|
| 0-3 | Tres objetos sobre una mesa de madera, se tachan uno a uno: taza de infusión, faja doblada, plato vacío | "Té. Faja. Saltarse la cena." |
| 3-6 | Los tres tachados | "Duran unas horas y después vuelve. Y no es por falta de fuerza de voluntad." |
| 6-10 | Diagrama de línea de los 3 motivos, apareciendo | "Lo que se hincha durante el día no es grasa: es el intestino, la postura y una faja interna dormida." |
| 10-15 | Portada del PDF + páginas pasando | "Plana todo el día. Reto de 28 días: siete rutinas de 10 minutos que entrenan la capa de adentro." |
| 15-20 | Hoja de seguimiento, calendario, lista de compras | "28 fichas día por día, hoja de seguimiento y la lista de compras de la semana." |
| 20-24 | Cinta métrica y un reloj marcando 9:00 | "Te medís a las 9 de la mañana y a las 9 de la noche. El día 28 volvés a medir la diferencia." |
| 24-28 | Portada quieta | "Un pago. Garantía de 7 días. Está en el link." |

**Regla de la voz:** si la voz es generada con IA y suena a persona real, se etiqueta como
contenido generado con IA. Y no puede presentarse como alguien (nada de "soy entrenadora",
nada de credenciales): una voz que narra un producto, no una persona que da consejo de
salud. Si esto complica, **la salida limpia es texto en pantalla y música**, como en los
guiones A y B.

---

## 6. Los públicos y en qué orden

**Tanda 1 no testea públicos: testea creativos.** El público queda **idéntico en los 4
conjuntos**. Un cambio por vez, o no se sabe qué funcionó.

### Público base (P0), constante en la tanda 1

| Campo | Valor |
|---|---|
| Países | **Perú, Ecuador, Chile, Colombia, México** |
| Idioma | Español |
| Edad | **18+** (obligatorio, aunque el tema no lo pida: ahorra un rechazo) |
| Género | Abierto |
| Intereses | **Ninguno.** Con US$8 por día un público de intereses no junta datos |
| Audiencia automática | **Apagada**, para que el 18+ sea firme |

Por qué un bloque amplio y no un país: se arranca por región y se poda con el desglose
por país, que es la mecánica de Bilbao. **Afuera de entrada: Argentina y Venezuela**
(moneda y poder de compra; Bilbao midió Argentina dejando US$0.10 por visita — no
verificado).

### Tanda 2: con el creativo ganador fijo, se rota el público

| Orden | Público | Por qué en ese lugar |
|---|---|---|
| 1 | P0 (control) | Sin control no hay comparación |
| 2 | Mismo bloque, **solo mujeres 25 a 45** | Mitad de las impresiones del P0 van a gente que no va a comprar nunca. Con presupuesto chico eso pesa |
| 3 | **México solo** | Es el mercado hispano con más volumen y tarjeta del bloque |
| 4 | **Hispanos en EE. UU.** (español, ubicación EE. UU.) | Clic más caro, pero es donde más deja cada visita según Bilbao (no verificado). Se prueba último porque puede comerse el presupuesto rápido |

### Lo que NO se prueba en esta ronda

| Qué | Por qué |
|---|---|
| **España** | El producto habla peruano: la lista de compras nombra camote, vainita, jurel y hierbaluisa. Antes de comprar tráfico español hay que neutralizar esa hoja (eso lo decide el-panadero) |
| Retargeting | Necesita volumen. No antes de ~1,000 visitas |
| Públicos similares (lookalike) | Necesitan una lista de compradoras. Con 10 ventas no alcanza |

> Lo que cambiaría el orden: si el desglose por país de la tanda 1 muestra que México
> deja más del doble por visita que el resto, México pasa a ser el control.

---

## 7. Anti-baneo

Las políticas de Meta ganan sobre cualquier número. **Todo esto es un resumen al
23/09/2026 y se relee contra las fuentes oficiales antes de prender** (los links están en
`.claude/skills/bilbito/metodo/anti-baneo.md`).

Este producto cae en **salud y peso**: es la zona más estrecha que hay, junto con plata.

### Palabras que disparan rechazo, y cómo se dice lo mismo

| No se escribe | Se escribe |
|---|---|
| bajar de peso · adelgazar · perder kilos · quemar grasa | que la cintura mida lo mismo a las 9 de la noche que a las 9 de la mañana |
| barriga · rollitos · panza chata | que la ropa marque cintura y no panza |
| **"vas a quedar plana" · "quedá plana en 28 días"** (el nombre conjugado hacia quien mira) | **PLANA TODO EL DÍA** como nombre en pantalla, y al lado qué significa: la cintura mide lo mismo a las 9 de la noche que a las 9 de la mañana |
| **tu** panza se hincha · **vos** tenés hinchazón | la panza de las 6 de la tarde · lo que se hincha durante el día |
| detox · desintoxicar · eliminar toxinas | qué alimentos hinchan más y con qué cambiarlos |
| elimina la hinchazón · cura · trata · corrige | entrena la capa profunda del abdomen |
| resultados garantizados · resultados en 7 días | 28 días, dos medidas y garantía de 7 días (es verdad, se puede decir) |
| sin esfuerzo · sin hacer nada | 10 minutos por día, sin saltos y sin equipo |
| diástasis · piso pélvico · posparto | (nada: ese no es este comprador y es condición médica) |
| antes y después | el mismo jean a dos horas del día · la hoja de seguimiento vacía y llena |

La regla madre del lenguaje: **hablar del fenómeno o del objeto, nunca de quien mira.**
Meta prohíbe afirmar o insinuar algo de la persona que ve el anuncio.

### El nombre nuevo: "plana" es marca, no promesa

El nombre **PLANA TODO EL DÍA** es fuerte para vender y queda a un paso de la zona roja de
salud y peso. No está prohibido: no es un antes y después, no promete kilos y no afirma
nada de quien mira. Pero se usa con tres candados, y se relee esta sección si aparece el
primer rechazo.

| Candado | Por qué |
|---|---|
| Se escribe **siempre en mayúsculas y como nombre**, nunca conjugado hacia la persona | "PLANA TODO EL DÍA" es una marca; "vas a quedar plana" es una promesa de resultado corporal dirigida a quien mira, y ahí empieza el problema |
| **Nunca sobre un cuerpo.** Va sobre la portada, sobre fondo plano o sobre un objeto | Nombre + torso en la misma imagen es exactamente lo que Meta lee como imagen corporal idealizada |
| **Siempre acompañado de qué significa** en el mismo cuadro: la cintura mide lo mismo a las 9 de la noche que a las 9 de la mañana | Convierte una promesa de forma del cuerpo en un resultado medible con cinta métrica, que además la página de Whop cumple |

> El número que cambia esto: **2 rechazos seguidos** de anuncios que traen el nombre en el
> titular. Ahí el nombre baja al cuerpo del texto y el titular pasa a ser la promesa de
> las 9 a las 9. El nombre del producto en Whop no se toca: solo el titular del anuncio.

### Imágenes que disparan rechazo, y qué se usa

| Nunca | Sí |
|---|---|
| Torsos, abdómenes desnudos, primeros planos de panza, bikinis, ropa interior | Ropa sin cuerpo: un jean sobre una silla |
| Pellizcar la grasa, manos midiendo cintura sobre piel | Cinta métrica sola, sobre una mesa |
| Comparación lado a lado de dos cuerpos | Comparación lado a lado de dos **relojes** o dos hojas |
| Balanza con números | La hoja de seguimiento con los dos números escritos |
| Flechas o círculos señalando una parte del cuerpo | Diagrama de línea del abdomen en corte, esquemático, nada realista |
| Gente comiendo "mal" | El plato de 3 partes, ilustrado |
| Personajes de IA fotorrealistas dando consejo de salud | Ilustración, objetos, tipografía |

### Antes de publicar cada anuncio: 9 preguntas. Si alguna da "sí", no sale

1. ¿Promete plata o un resultado económico?
2. ¿Afirma algo de quien mira ("vos tenés", "vos sufrís")?
3. ¿Muestra un antes y después del cuerpo?
4. ¿Toca peso o apariencia sin estar en 18+?
5. ¿Usa un testimonio o un "4.9 de 5" que no es real? **Acá no hay ninguno real: no se usa.**
6. ¿Usa una urgencia o escasez falsa? Un PDF no se agota: "quedan 5 cupos" nunca.
7. ¿Promete algo que la página de Whop no cumple?
8. ¿Tiene una persona o voz de IA que parece real y no está etiquetada?
9. ¿Cae en empleo, crédito o vivienda? (Acá no.)

Y la última: si una desconocida lo compra y lo lee, ¿se siente estafada? Si es "un poco",
no sale.

### Cómo se prepara la cuenta antes de prender

| # | Qué | Quién | Cuándo |
|---|---|---|---|
| 1 | Perfil personal de Paolo con antigüedad, **doble factor** y un administrador de respaldo | Paolo | Semana previa |
| 2 | Página de Facebook e Instagram de la marca con **5 a 8 publicaciones reales**, publicadas de a poco durante 1 o 2 semanas. Nunca comprar seguidores | el-panadero | 2 semanas antes |
| 3 | **Un solo método de pago, estable.** Cambiarlo seguido parece fraude | Paolo | Antes de D1 |
| 4 | Cuenta de Whop abierta y con KYC hecho, producto publicado, checkout probado | Mercaneto y Whoper | Antes de D1 |
| 5 | **Compra de prueba** de Paolo, reembolsada el mismo día. Sirve para ver que la compra aparece en los reportes. **No cuenta como venta** | Paolo | D-1 |
| 6 | **Pixel:** con Whop Ads no se instala nada — Whop registra la compra en su servidor y se la pasa a Meta. Se verifica con la compra de prueba, no se supone | Bilbito | D-1 |
| 7 | **Dominio:** la página vive en Whop. Si algún día se conecta un dominio propio, hay que verificarlo. Con Whop Ads la verificación la tiene Whop — **no verificado**, se confirma al abrir la cuenta | Bilbito | D-1 |
| 8 | Confirmar que se puede **optimizar a Compra** (restricción de salud y bienestar de Meta desde 2025, no verificada para Paolo). Plan B: optimizar a *Iniciar pago* | Bilbito | D-1 |
| 9 | La página de Whop cumple **todo** lo que dicen los anuncios: el jean, los 10 minutos, los 28 días, la garantía de 7 días | Whoper | D-1 |

### Lo que NO se hace, pase lo que pase

- **Calentar la cuenta no existe** como función oficial de Meta. Lo que sí baja el riesgo:
  arrancar con **4 anuncios limpios** y no con 20 al borde, y dejar correr 24 h antes de
  tocar nada. Muchos rechazos seguidos marcan la cuenta como de baja calidad.
- **Ninguna ráfaga de cambios.** Un agente que dispara 800 peticiones en un minuto se lee
  como automatización abusiva y hay cuentas baneadas de por vida por eso. Ningún cambio en
  campañas sin el OK de Paolo, y de a uno. Las herramientas de Whop piden confirmación:
  se respeta siempre.
- **Si restringen la cuenta:** no abrir otra, no borrar nada, no cambiar el método de pago.
  Meta lo lee como esquivar la sanción y la extiende a todo. Se apela desde Calidad de la
  cuenta, máximo unas 3 veces, y **nunca la misma apelación dos veces**.

---

## 8. Calendario de las 2 primeras semanas

Todo esto arranca el día después de que `CLAUDE.md` diga 10 de 10.

### Semana previa (sin gasto en anuncios)

| Día | Qué |
|---|---|
| D-14 a D-8 | Página de FB e IG con 5 a 8 publicaciones reales, de a una (el-panadero) |
| D-7 | El Gato trae 5 a 10 anuncios activos del nicho con 3+ días corriendo. Se comparan contra los 10 ganchos: el que se parezca a un ganador sube de prioridad |
| D-5 | Se producen los 4 creativos de la tanda 1 (ganchos 1, 4, 6 y 3). Generar imágenes gasta créditos: **solo con el OK de Paolo** |
| D-3 | Los 4 pasan la lista de 9 preguntas. El que no pasa, se reescribe |
| D-2 | Cuenta de Whop lista, producto publicado, página revisada contra lo que prometen los anuncios |
| D-1 | Compra de prueba y reembolso el mismo día. Se confirma que aparece en los reportes. Se confirma que se puede optimizar a Compra. Se carga la campaña **programada a las 00:00** y el interruptor general se anota en `CLAUDE.md` |

### Semana 1: la tanda de creativos

| Día | Gasto | Qué se hace |
|---|---|---|
| **D1** 00:00 | US$32 | Arrancan los 4 conjuntos a US$8 |
| **D1** 12:00 | — | Primera revisión. **Solo se apaga** el conjunto con 500+ impresiones y cero clics, o CTR bajo 0.5%. Se anota el **CPM del día 1**: es la línea base de Paolo para siempre |
| **D1** noche | — | Se anotan CTR, carga de página y CPV de cada conjunto. Nada más se toca |
| **D2** | US$32 | No se toca nada. Se mira y se anota |
| **D3** mañana | US$32 | Revisión de 48 h: se apaga el que tenga CTR bajo 1%. Si la **carga** está bajo 70% en todos, el problema es la página: aviso a Whoper y Diseñante, y **no se apaga ningún anuncio por eso** |
| **D3** noche | — | **La decisión grande.** Cada conjunto gastó ~US$24 = 95% del techo. Se aplica la tabla de corte de la sección 2. Se producen los relevos para los que murieron |
| **D4** | US$32 | Arranca la tanda 2: sobrevivientes + relevos, siempre 4 conjuntos a US$8. Imágenes y videos **nunca** en el mismo conjunto |
| **D5** | US$32 | No se toca. Chequeo del interruptor general: ¿se pasaron los US$100 sin un solo pago iniciado? |
| **D6** | US$32 | Revisión de 48 h de la tanda 2, misma regla |
| **D7** (domingo) | hasta US$8 | Cierre de semana. Acumulado ≈ US$200 (S/740). Se escribe el veredicto |

**Veredicto del D7, tres caminos:**

| Si… | Semana 2 |
|---|---|
| Hay 3 o más ventas bajo el techo | **Camino A: probar el ganador un fin de semana** |
| Hay visitas a CPV bajo US$0.25 pero 0 o 1 venta | **Camino B: el freno está abajo del anuncio** |
| El CPV quedó sobre US$0.50 | **Camino C: el freno está en el anuncio** |

### Semana 2, camino A (hubo ganador) — se usa la reserva de US$70

| Día | Gasto | Qué |
|---|---|---|
| D8 a D11 (lu a ju) | US$0 | **Todo apagado.** Se producen 4 variaciones del ganador (mismo guion, otro fondo, otro primer segundo) y se anota el costo por compradora real |
| D12 (viernes) | ~US$24 | Se prende el ganador solo, a US$24 en un conjunto |
| D13 (sábado) | ~US$27 | Si vendió el viernes bajo el techo: **+15%**. Si no vendió, no se sube |
| D14 (domingo) | ~US$19 | Se cierra la reserva. Veredicto final y número real de Paolo: **cuánto le cuesta una compradora** |

### Semana 2, camino B (hay visitas baratas y no compran)

| Día | Gasto | Qué |
|---|---|---|
| D8 | US$0 | Todo apagado. El anuncio anda: el problema está en la página, la oferta o el precio |
| D8 a D10 | US$0 | Whoper revisa la página y el checkout; Mercaneto revisa el precio. `NOTAS.md`: con 100 visitas y 0 ventas, se prueba **US$19** antes de tocar el producto. **Un cambio por vez** |
| D11 a D13 | ~US$24/día | Se vuelve a prender el **mismo** conjunto ganador, sin tocar el creativo, contra la página corregida. Mínimo 3 días: un cambio de página no se juzga en un día |
| D14 | — | Se compara la conversión de página contra la de la semana 1 |

### Semana 2, camino C (el CPV nunca bajó)

| Día | Gasto | Qué |
|---|---|---|
| D8 | US$0 | Todo apagado. **No se cambia de nicho: se diagnostica** |
| D8 a D11 | US$0 | 4 creativos nuevos con ángulos que no se probaron (ganchos 7, 8, 9 y 10), y esta vez **modelados** sobre lo que El Gato encontró corriendo |
| D12 a D14 | ~US$23/día | Se gasta la reserva en esos 4, a US$6 por conjunto, con la misma regla de corte |
| D14 | — | Si el CPV sigue sobre US$0.50 con 8 creativos distintos, el problema no es el creativo: es el precio o la promesa. Vuelve a Mercaneto y a el-panadero |

---

## Resumen en cinco líneas

1. **Hoy no se prende nada:** 0 de 10 ventas a desconocidos.
2. ABO, 4 conjuntos, US$8 por día cada uno, 3 días por tanda. US$200 de test y US$70 de
   reserva que se gana.
3. El número que manda: **CPV bajo US$0.25**. El techo absoluto: **US$25.20 por compradora**.
4. Se apaga todo si se gastan **US$100 sin un solo pago iniciado**.
5. Faltan dos cosas antes del día 1: los anuncios activos del nicho que tiene que traer
   **El Gato**, y confirmar que Meta deja **optimizar a Compra** en un producto de salud.
