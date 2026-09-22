# Armar la vidriera en Whop — paso a paso verificado

Para Whoper. Todo lo de acá sale de la documentación de Whop, revisada el 21/09/2026,
con el link de cada paso. Los nombres de los menús cambian: si algo no está donde dice,
se busca en https://docs.whop.com y se corrige este archivo, no se adivina.

Lo que es plata (comisiones, retiro, lo que deja cada venta) **no está acá**: vive en
`CLAUDE.md` del repo.

## 0. Antes: la cuenta (la abre Mercaneto)

Al crear la cuenta en whop.com/sell, Whop pregunta cómo se va a usar. La que sirve es
**"Build & sell digital products on Whop"**: el archivo se entrega adentro de Whop. La
otra ("payment processing only") es para quien entrega por fuera.
Doc: https://docs.whop.com/launch-your-business

## 1. El producto

Dashboard > Products > Create product.

| Campo | Regla | Bloque de la página |
|---|---|---|
| Nombre | máximo 80 caracteres; descriptivo antes que ingenioso | 1, promesa |
| Titular (headline) | máximo 80 caracteres | 1, promesa |
| Imagen de banner | la hace Diseñante | — |
| Precio | pago único (one-time), en USD; el número lo fija Mercaneto | 6 |
| Apps | Files (ver punto 3) | — |
| Página del producto | foto o video + descripción | 2, 3, 4, 5, 7 |

Whop aclara que una página de producto detallada le ayuda a entender qué se vende.
Doc: https://docs.whop.com/manage-your-business/products/create-product

### Opciones avanzadas: qué se toca y qué no

| Opción | Acá | Por qué |
|---|---|---|
| Show on store page | apagada mientras se prueba; se prende con los 4 chequeos en verde | el link directo funciona igual |
| Redirect after checkout | no se toca | que el comprador caiga en la whop donde está el archivo |
| Ask questions before checkout | no | cada pregunta es un escalón más antes de pagar |
| Stock | no | escasez falsa = promesa falsa |
| Add a waitlist | no | se vende ya |
| Auto-expire access | no, para un archivo | lo compró, es suyo |
| Payment methods | los que muestre Whop por defecto; Mercaneto decide si se saca alguno | — |

Doc: https://docs.whop.com/manage-your-business/products/manage-products

## 2. El link de pago

Dashboard > Checkout links > + Create checkout link > One-time > precio.
Sin "Show on store page" es un link privado: funciona si se comparte directo.
Doc: https://docs.whop.com/payments/create-checkout-link

## 3. La entrega automática, según el formato

Default: **un solo mecanismo, la app Files**, para todo lo que sea archivo.

| Formato | Cómo se entrega | Doc |
|---|---|---|
| PDF, ebook, checklist, planilla | app Files ("templates, e-books, and digital assets") prendida en el producto | https://docs.whop.com/whop-apps/consumer-apps |
| Plantilla de Notion | Files con un PDF de 1 página que tiene el link para duplicar (default nuestro); la alternativa es la app Content, páginas estilo Notion | https://docs.whop.com/whop-apps/consumer-apps |
| Mini curso en video | app Courses: lecciones de video, texto, PDF descargable | https://docs.whop.com/supported-business-models/educational-programs |
| Comunidad | apps de Whop; en la prueba, sin acceso automático a Discord, Telegram ni TradingView (ver `CLAUDE.md`) | — |

Para ver lo que ve el comprador: en la whop, menú **Preview as** > el producto.
Doc: https://docs.whop.com/manage-your-business/products/manage-products

## 4. La bienvenida automática

Dashboard > Marketing > Support chats > **User joined** > Enable automation.
Se escribe el mensaje (acepta `recipient_name` y `whop_name`), se puede sumar imagen o
video, y la casilla de mail hace que llegue **como mensaje en Whop y como mail**.
Texto en `plantilla-pagina.md`.
Doc: https://docs.whop.com/manage-your-business/growth-marketing/automated-messaging

## 5. Garantía y términos

Dashboard > Settings > Legal. Se sube la **Return Policy** (política de devolución) con
los mismos días y la misma condición que dice la página, y se prende **Require terms and
conditions acceptance** para que el comprador marque la casilla antes de pagar. Whop dice
que esto ayuda a cortar disputas falsas.
Doc: https://docs.whop.com/manage-your-business/manage-business/legal-documents

## 6. Un link de seguimiento por canal

Dashboard > Marketing > Tracking links > + Create tracking link: nombre, whop, destino
(Checkout o Store) y plan. Mide clics, plata generada, tasa de conversión y compradores.
Uno por lugar donde se publica (bio, mensajes, cada campaña). El registro de dónde vino
cada venta lo lleva el-panadero.
Doc: https://docs.whop.com/manage-your-business/growth-marketing/tracking-links

## 7. La página de la tienda

Nombre de la whop > Design store page > Edit details: nombre, titular, descripción, logo,
galería de imágenes o video arriba, categoría.
Doc: https://docs.whop.com/supported-business-models/educational-programs

El look del checkout (color de fondo, color de botón, letra, bordes) lo elige Diseñante en
Settings > Checkout Branding.
Doc: https://docs.whop.com/manage-your-business/payment-processing/checkout-branding

## Qué pasa después de pagar (documentado)

| Momento | Qué pasa | Doc |
|---|---|---|
| Al pagar | llega "Whop Order Confirmation" desde no-reply@whop.com, con un botón para entrar a lo comprado | https://docs.whop.com/memberships-and-access/accessing-your-purchase/how-to-find-your-purchase |
| Error típico del comprador | pagó con un mail y entra con otro, y "no ve" su compra | mismo link: va al FAQ |
| Redirección | por defecto el checkout lleva a la whop (documentado para el checkout embebido; se confirma en la compra de prueba) | https://docs.whop.com/payments/checkout-embed |
| Pedido de devolución | el comprador va a Orders > Request Refund; se abre un caso y el vendedor tiene 7 días para responder o decide Whop | https://docs.whop.com/manage-your-business/manage-payments/resolution-center |
| Hacer el reembolso | Dashboard > Payments > ⋮ > Refund (lo hace Mercaneto) | https://docs.whop.com/manage-your-business/manage-payments/issuing-refunds |

## Lo que no se usa

- Sitios propios en el dominio de Whop, checkout embebido en otra web, landing aparte:
  la página se escribe en Whop.
- Prueba gratis, cuotas, lista de espera, stock: no para un archivo de entrada.
- Acceso automático a Discord, Telegram o TradingView.

## Con el conector de Whop (opcional)

Default: Paolo lo arma a mano en el panel. Son pocos campos y ve lo que hace.
Si se usa el conector:

1. `connection_status` y `accounts_list`: confirmar que el negocio es el de productos
   digitales. **Si es el de Vendí, se frena ahí.**
2. Leer la skill `whop-mcp-safety` antes de la primera escritura: cada operación lleva
   `intent` (el pedido de Paolo, textual) e `intent_id`, y las que piden confirmación
   devuelven una vista previa que Paolo aprueba antes de ejecutar.
3. Herramientas: `products_create`, `plans_create`, `checkout-configurations_create`.
4. Nunca `apps_create` ni `apps_deploy`: eso sube un sitio, y acá no hay sitio.

## No verificado todavía (se confirma con la compra de prueba)

- Qué formato acepta la descripción (negrita, listas, emojis). Se escribe en texto plano
  con líneas cortas hasta verlo.
- Medidas recomendadas de las imágenes: no están en la documentación.
- Cómo se ve y se baja el archivo de Files desde la app de celular: es el chequeo 3.
