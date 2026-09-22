# Whop: la parte de la plata

Lo que dicen los docs de Whop sobre devoluciones, disputas, retiros y KYC. Verificado en docs.whop.com el 21/09/2026. Si pasaron meses, se re-chequea.

**Acá no hay montos.** Comisión, costo de retiro y cualquier tarifa en dólares van a la sección Whop del `CLAUDE.md` del repo, que es la única copia. Si hace falta un monto que no está ahí, se busca en docs.whop.com/fees y se agrega al `CLAUDE.md`, no acá.

## Devoluciones

| Dato | Fuente |
|---|---|
| Al devolver, se le paga al comprador el total que pagó, aunque la comisión haya achicado lo que te llegó. Devolver no tiene costo extra | https://docs.whop.com/manage-your-business/manage-payments/issuing-refunds |
| Tres formas de devolver: desde el perfil del cliente, desde Payments o aceptando el caso en el Resolution Center. Whop la procesa al instante | https://docs.whop.com/manage-your-business/manage-payments/issuing-refunds |
| Si no hay saldo para devolver, hay que cargar plata (Balances → Top up) | https://docs.whop.com/manage-your-business/manage-payments/issuing-refunds |
| Con retiros automáticos se puede dejar un saldo mínimo; Whop sugiere que alcance para al menos 2 devoluciones al precio típico. Con retiros manuales, el colchón se cuida a mano | https://docs.whop.com/manage-your-business/manage-payments/issuing-refunds |
| Hay auto-reembolso por debajo de un monto (Resolution Center → Auto respond) | https://docs.whop.com/manage-your-business/manage-payments/issuing-refunds |

## Resolution Center

| Dato | Fuente |
|---|---|
| El comprador abre un caso; vos tenés 7 días para aceptar, negar o pedir más info. Si no contestás, decide el equipo de Whop | https://docs.whop.com/manage-your-business/manage-payments/resolution-center |
| La mayoría de las disputas pasan porque el comprador no sabía que podía pedirte la plata a vos. Cada caso resuelto ahí es una disputa que no pasa | https://docs.whop.com/trust-and-safety/account-health/managing-dispute-rates |

## Disputas (contracargos)

| Dato | Fuente |
|---|---|
| Una devolución cuesta una venta. Una disputa cuesta la venta, una tarifa fija y un golpe a la tasa de disputas | https://docs.whop.com/trust-and-safety/account-health/managing-dispute-rates |
| Las devoluciones no cuentan para la tasa de disputas: son lo contrario | https://docs.whop.com/trust-and-safety/account-health/managing-dispute-rates |
| La línea que miran las redes de tarjetas es 1.5% de pagos con disputa. Estados: Healthy, At risk, Critical; con pocos pagos muestra "Low data" | https://docs.whop.com/trust-and-safety/account-health/payment-health |
| Pasarse de la línea tiene consecuencias. El panel lista los controles de la cuenta (reserva, umbrales de auto-reembolso, demora en liberar la plata, comisiones); se aflojan solos cuando la tasa baja | https://docs.whop.com/trust-and-safety/account-health/payment-health |
| Cuando entra una disputa, Whop descuenta del saldo el monto y la tarifa al instante | https://docs.whop.com/manage-your-business/manage-payments/manage-disputes |
| Se contesta en el Dispute fighter en 7 a 21 días; el banco decide en 2 a 3 meses. Sin respuesta antes del plazo, se pierde sola | https://docs.whop.com/manage-your-business/manage-payments/manage-disputes |
| Whop sube solo parte de la prueba (mail, fecha de compra, registro de acceso, si aceptó términos y política) | https://docs.whop.com/manage-your-business/manage-payments/manage-disputes |
| Si ya es contracargo completo, no se puede devolver | https://docs.whop.com/manage-your-business/manage-payments/manage-disputes |
| Si retiraste todo y llega una disputa o devolución, el saldo queda negativo | https://docs.whop.com/trust-and-safety/account-health/managing-dispute-rates |
| Nombre en el resumen de tarjeta poco claro → el comprador no lo reconoce y reporta fraude. Se cambia en la configuración | https://docs.whop.com/trust-and-safety/account-health/managing-dispute-rates |
| Frenar las ventas no baja la tasa enseguida: las disputas llegan atrasadas | https://docs.whop.com/trust-and-safety/account-health/managing-dispute-rates |

## Documentos legales

| Dato | Fuente |
|---|---|
| Se suben en Dashboard → Settings → Legal: Terms of Service, Privacy Policy, Return Policy, EULA | https://docs.whop.com/manage-your-business/manage-business/legal-documents |
| En Options se prende "Require terms and conditions acceptance": el comprador tiene que tildar que acepta antes de pagar | https://docs.whop.com/manage-your-business/manage-business/legal-documents |
| Si no subiste política de devolución, en una disputa Whop presenta la de la plataforma | https://docs.whop.com/api-reference/beta/disputes/dispute |

## Retiros y KYC

| Dato | Fuente |
|---|---|
| Para retirar: Balances → Set up Whop Payments → elegir país (define la moneda del retiro) → KYC: datos, banco y documento | https://docs.whop.com/manage-your-business/manage-payouts/set-up-payouts |
| La verificación de identidad es obligatoria antes de retirar | https://docs.whop.com/sdk/elements/verify-element |
| Fuera de EE. UU., la cuenta tiene que aceptar la moneda del país registrado. Whop convierte a moneda local aunque se cobre en dólares; a una cuenta en dólares en un país con otra moneda no llega | https://docs.whop.com/manage-your-business/manage-payouts/payout-methods |
| El país del retiro se puede cambiar después (Payouts → tres puntos → Change payout country) | https://docs.whop.com/manage-your-business/manage-payouts/payout-methods |
| Hay un monto mínimo para retirar (ver la página) | https://docs.whop.com/manage-your-business/manage-payouts/set-up-payouts |
| La plata de una venta queda disponible en 1 a 4 días hábiles; el retiro tarda hasta 10 días hábiles | https://docs.whop.com/manage-your-business/manage-payouts/troubleshoot-payouts |
| Si un retiro falla, vuelve al saldo. Causa común: la cuenta no está en la moneda local | https://docs.whop.com/manage-your-business/manage-payouts/troubleshoot-payouts |
| Algunos retiros pasan por revisión manual de cumplimiento; ahí no aparece la opción instantánea | https://docs.whop.com/manage-your-business/manage-payouts/payout-methods |

## Afiliados

| Dato | Fuente |
|---|---|
| Whop prende por default los afiliados globales: cualquier afiliado de su red puede promocionar el producto y se lleva una comisión por venta, sin que hagas nada | https://docs.whop.com/affiliates/setup-global |
| Se cambia por producto en Marketing → Affiliates | https://docs.whop.com/affiliates/setup-global |

## Lo que NO está verificado

- **W-8BEN o formulario de impuestos**: no aparece en docs.whop.com (búsqueda del 21/09/2026). Si el panel lo pide al abrir la cuenta, se completa y se anota acá qué pidió.
- **Costo del retiro a banco local de Perú**: los docs dicen que varía por país. Se ve recién al abrir la cuenta y elegir Perú; va al `CLAUDE.md`.
- **Cuánto tarda el KYC**: sin dato.
