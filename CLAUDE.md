# Digital-Products — Paolo Nieto

## Qué es y qué no es

Negocio de productos digitales: vender archivos (PDF, plantillas, packs) o acceso pago
a desconocidos por internet, cobrando en dólares desde Lima.

**No es Vendí** (la app de fotos de producto con IA para PyMEs). Otro negocio, otras
cuentas. Acá no entra ni un número de Vendí: ni S/39, ni catálogo, ni Mercado Pago, ni
costo por crédito, ni su CAC.

| | Vendí | Acá |
|---|---|---|
| Costo por unidad vendida | créditos de IA por imagen | cero |
| Margen bruto | ~40% | ~90% (solo comisión) |
| Qué limita el crecimiento | costo de generar | conseguir tráfico |

## Whop: decidido, no se discute

Whop es la pasarela de pagos **y** la tienda. Está cerrado. **Prohibido proponer
alternativas** (Gumroad, Etsy, Stan Store, Hotmart, Payhip, Lemon Squeezy, Mercado Pago,
Shopify, ninguna) salvo que Paolo lo pida con esas palabras. Si aparecen en un video o en
research, son registro de lo que hace otra gente, nunca sugerencia para él.

Números verificados en docs.whop.com/fees el 21/09/2026 — si pasaron meses, re-chequear
antes de usarlos. **Este archivo es la única copia de estos números: los demás archivos
lo apuntan, no lo copian.**

- Comisión: **2.7% + US$0.30**. +1.5% si la tarjeta es de fuera de EE. UU., +1% si hay
  conversión de moneda. Además, por venta: **US$0.07 antifraude** y **US$0.03** si el
  checkout pide verificación 3DS.
- De un PDF de US$27 quedan **US$25.20 a 25.90**.
- El recargo de +3% por acceso automático a Discord, Telegram o TradingView **ya no
  figura** en las tarifas oficiales. Se confirma al abrir la cuenta.
- Contracargo (el comprador reclama al banco): **US$15 cada uno**, y alerta temprana
  US$29. La línea de las tarjetas es **1.5%** de pagos con contracargo.
- Retiro: **US$23 por transferencia internacional (wire)**; **banco local de Perú:
  "varía por país", sin verificar** — se ve recién al abrir la cuenta y elegir Perú.
  Cripto: 5% + US$1. Mínimo de retiro: US$10.
- Whop paga en la moneda del país: a un banco peruano llega **en soles, a una cuenta en
  soles**. Una cuenta en dólares en Perú hace rebotar el retiro.

Tres reglas caras:

1. Acumular antes de retirar. Por wire, un retiro de US$100 se come el 23%. Si el banco
   local de Perú sale barato, esta regla se afloja.
2. Mirar los **contracargos**, no las devoluciones. Las devoluciones no cuentan en la
   tasa; los contracargos sí, y pasado 1.5% Whop retiene plata y cobra más. Devolver
   rápido sale más barato que un contracargo. Con 10 ventas, uno solo ya es 10%.
3. Lo que sí hace perder la cuenta es vender algo prohibido: promesas de ingresos o de
   salud sin sustento, o prometer "acceso de por vida".

**Toda cuenta se hace sobre lo que DEJA la venta (~US$25), nunca sobre el precio de
lista.** Eso también es el techo de lo que puede costar conseguir un comprador.

## Prioridad #0: todavía no hay producto

Paolo no eligió nicho, ni comprador, ni formato. Cero productos, cero ventas, cero
audiencia. **Hasta que eso esté definido no se construye nada**: ni PDF, ni página, ni
anuncios, ni automatizaciones.

Primero la calle, después el pan: el cuello de botella nunca es hacer el producto (la
IA lo arma en una tarde), es conseguir compradores. Es la lección de Vendí — el pan
salió bueno y nadie pasó por la puerta.

Orden obligatorio: **a quién le vendo → por dónde me ve → qué le vendo → a cuánto →
10 ventas a desconocidos → recién ahí pauta.**

Primer hito, no la meta grande: **10 ventas a desconocidos** en 2 a 4 semanas con S/1,000
de prueba. La prueba no compra ventas, compra el dato de cuánto cuesta un comprador.

Regla antiautogol: la compra de prueba que hace Paolo para verificar el checkout **se
reembolsa el mismo día y NO cuenta** en las 10. En Vendí la única venta histórica fue
probablemente de su propia cuenta y eso contaminó el veredicto durante meses.

## Cómo responderle

- Corto. Titular primero, contexto después. Tablas y números antes que párrafos.
- **Una recomendación, no un menú.** Si hay un default razonable, decidilo y explicalo
  en una línea. "Depende" sin decidir no sirve.
- Español coloquial, **en fácil, con analogías**. Cero emoji, cero relleno.
- Todo veredicto viene con el número que lo cambiaría de opinión.
- Nunca inventar ventas, precios ni métricas. Lo que sale de un video de YouTube es
  "no verificado" hasta ver de dónde sale; los supuestos se marcan inline ("si compran
  2 de cada 100, supuesto").
- Plata en dos monedas cuando aplica a Paolo (US$100 a 300 / unos S/350 a 1,100).
- Si el pedido salta pasos del orden de arriba, decirlo y volver al paso que falta.

## Qué se escribe en el repo

Sí: este archivo, `CONTEXTO.md` (el por qué de cada decisión), notas de nicho y
comprador, lo que aprenden los digimones en `digimones/` (el equipo en `DIGIMONES.md`,
videos en `videos.md`, otras fuentes en `fuentes.md`, ofertas de la competencia en
`mercado.md`, publicaciones en `publicaciones.md`), y borradores de producto y de copy.

No: el producto final (vive en Whop), claves ni credenciales, capturas con datos
personales, y nada de Vendí.

Regla: **un número que se compara vive una sola vez en el repo.** Si ya está acá, los
demás archivos lo apuntan, no lo copian.

## Digimones: se nutren solos — OBLIGATORIO en cada sesión

`digimones/` es lo que van aprendiendo los agentes de este negocio. Quién es quién está
en `digimones/DIGIMONES.md`.
Antes de cerrar cada sesión, **sin esperar a que Paolo lo pida**, se guarda ahí lo nuevo
que haya aparecido sobre productos digitales, y se hace commit:

| Si apareció... | Va a |
|---|---|
| Un video analizado | una fila en el tablero y un apartado en `digimones/videos.md` |
| Una fuente leída (estudio, docs, artículo, libro, foro), con link y fecha | `digimones/fuentes.md`, en el tema que corresponda |
| Una oferta, precio o anuncio de la competencia visto, con fecha | `digimones/mercado.md`, una fila por observación |
| Un dato de Whop verificado (comisión, retiro, cómo se entrega) | este archivo, sección Whop, no `digimones/` |
| Nicho, comprador, formato, precio o canal decidido | "Estado actual" de este archivo |

Lo que no entra: nada de Vendí, nichos que todavía no se decidieron, ni números de
creadores sin marcar "no verificado". Si en la sesión no se aprendió nada nuevo, no se
toca nada.

## Estado actual — actualizar cuando cambie

_Última actualización: 21/09/2026_

- Nicho: **sin definir**
- Comprador concreto (nombre y problema en una frase): **sin definir**
- Formato del producto: **sin definir** (pensando en PDF, ebook o plantilla de Notion)
- Precio: **sin definir**
- Canal elegido (uno solo): **sin definir**
- Cuenta de Whop: **sin abrir**
- Productos publicados: **0** · Ventas a desconocidos: **0 de 10**
- Cobrado: **US$0** · acumulado sin retirar: **US$0**
- Pauta: **apagada** (compuerta: 10 ventas)
- Próximo paso: elegir un comprador con nombre y su problema en una frase
