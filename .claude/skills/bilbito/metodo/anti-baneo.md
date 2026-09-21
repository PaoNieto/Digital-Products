# Anti-baneo y políticas para infoproductos

**La regla que manda sobre todas las demás: las políticas de Meta y de TikTok ganan sobre cualquier número.**
Si una táctica mejora un resultado pero pone en riesgo la cuenta o cruza una política, no se hace. Entre
"cumple pero rinde menos" y "rinde más pero es zona gris", siempre lo que cumple. Perder la cuenta cuesta más
que cualquier campaña.

**Las políticas cambian seguido.** Todo lo de abajo está armado el 21/09/2026 y es un resumen, no la fuente.
Antes de cada lanzamiento se releen las oficiales; si algo cambió, se corrige este archivo.

## Fuentes oficiales

| Qué | Dónde |
|---|---|
| Normas de publicidad de Meta (el contenido del anuncio) | https://transparency.meta.com/policies/ad-standards/ y https://www.facebook.com/policies/ads/ |
| Cuenta restringida o deshabilitada (Meta) | https://www.facebook.com/business/help/422289316306981 |
| Restricciones de publicidad (Meta) | https://www.facebook.com/business/help/975570072950669 |
| Límites de uso de la API de Meta | https://developers.facebook.com/docs/marketing-api/overview/rate-limiting/ |
| Políticas de publicidad de TikTok | https://ads.tiktok.com/help/ (sección Advertising Policies) |
| Whop Ads: qué se permite y qué no | https://docs.whop.com/manage-your-business/growth-marketing/ads |

---

## Los tres niveles

Meta puede cerrar cosas en tres lugares independientes. Cuidar uno no salva a los otros: es como tener tres
puertas con tres llaves distintas.

### Nivel 1: la herramienta o la API

Acá se cae la herramienta que opera los anuncios.

- **Agente de IA operando anuncios: el riesgo más nuevo.** Evidencia de campo que cuenta Claudio Conde: cuentas
  publicitarias baneadas de por vida por dos errores. Uno, operar con una app de Meta para desarrolladores sin
  verificar, en borrador. Dos, ráfagas: pedirle a un agente "analizá todos mis anuncios, creá 20 campañas y
  duplicá presupuestos" son unas 800 peticiones en un minuto, y Meta lo lee como automatización abusiva.
- Si algún día se usa la API de Meta directo: frenar al 80% de la cuota (Meta la informa en el encabezado
  `X-Business-Use-Case-Usage`; al 100% corta con el error 17 unos 5 minutos), nunca ráfagas, reintentos cada
  vez más espaciados, y la app aprobada para producción antes de operar en serio.
- **Regla de Bilbito:** ningún cambio en campañas sin el OK de Paolo, y de a uno (también lo pide el método:
  un cambio por vez). Las herramientas de Whop para anuncios piden vista previa y confirmación antes de crear,
  editar o pausar: se respeta siempre, nunca se saltea.

### Nivel 2: la cuenta publicitaria (contenido y calidad)

Acá se cae la cuenta que paga los anuncios. Es responsabilidad directa de Bilbito.

- Anuncios que rompen las normas de publicidad. **Cada copy y cada creativo pasa la lista de chequeo de abajo
  antes de publicarse.**
- Página que no cumple lo que dice el anuncio, que redirige, o que promete cosas raras. La página de Whop la
  arma Whoper: si el anuncio promete algo, la página lo tiene que cumplir.
- Muchas quejas o comentarios negativos sobre los anuncios.
- Muchos anuncios rechazados en poco tiempo: la cuenta queda marcada como de baja calidad. Por eso se arranca
  con pocos anuncios limpios, no con 30 al borde.
- Devoluciones: un anuncio que promete de más trae compradores que piden la plata de vuelta. En Whop la tasa de
  devoluciones pone en riesgo la cuenta de la tienda (ver `CLAUDE.md`). Sobreprometer quema dos cuentas a la vez.

### Nivel 3: identidad (perfil, página, negocio)

Lo más traicionero: se dispara por señales de seguridad o de fraude.

- Método de pago que falla o que se cambia seguido: parece fraude. Uno solo, estable.
- Perfil personal recién creado que arranca a pautar: señal roja. Se usa el perfil de Paolo, con antigüedad.
- Página vacía: tener 5 a 8 publicaciones reales antes de pautar.
- Doble factor en el perfil y un administrador de respaldo, para que perder un acceso no sea perderlo todo.
- **Trampa mortal:** si te restringen, **no** abrir una cuenta o un negocio nuevo, **no** borrar nada y **no**
  cambiar el método de pago. Meta lo lee como querer esquivar la sanción y la extiende a todo. Se apela desde
  la calidad de la cuenta (Account Quality, pedir revisión), máximo unas 3 veces, y **nunca se manda la misma
  apelación dos veces**: primero se entiende el motivo real y se cambia el enfoque.

### Con Whop Ads cambia una parte

Con Whop Ads, la cuenta publicitaria es de la agencia de Whop y tu página de Facebook e Instagram se conecta
por inicio de sesión. Entonces:

- El nivel 3 de la cuenta publicitaria lo comparte Whop, pero **tu perfil y tu página siguen siendo tuyos**:
  si los restringen, aplica la misma trampa mortal.
- Whop hace sus propios chequeos antes de lanzar. Según su documentación, no permite: promesas de ingresos
  falsas o que no se pueden verificar, testimonios falsos, contenido adulto, ofertas engañosas o con pinta de
  estafa. Dice que permite "la mayoría de los productos de información".
- Lo que Whop dice de su cuenta (nivel alto ante Meta, menos rechazos, sin tope de gasto) es "no verificado".
  Un chequeo de Whop aprobado **no** reemplaza leer las normas de Meta.

## Candados antes del primer anuncio

Se hacen enteros antes de gastar el primer sol, y recién después de la compuerta de 10 de 10.

1. Perfil personal de Paolo con antigüedad, con doble factor y un administrador de respaldo.
2. Página de Facebook e Instagram con 5 a 8 publicaciones reales (el contenido lo hace el-panadero).
   Nunca comprar seguidores para que no parezca vacía.
3. Si se usa una cuenta propia de Meta en vez de Whop Ads: verificar el negocio desde el día 1.
4. Un solo método de pago, estable.
5. Arrancar bajo: la plata por conjunto del `SKILL.md` y el total anotado en `CLAUDE.md`, no más.
6. La página de venta en Whop cumple todo lo que dice el anuncio (lo chequea Whoper).
7. La compra de prueba de Paolo se hace y se reembolsa el mismo día. Sirve para ver que la compra llega a los
   reportes. No cuenta como venta.

---

## Políticas para infoproductos: las zonas rojas

A re-chequear contra las fuentes oficiales antes de cada lanzamiento.

| Tema | Qué dice la política (resumen al 21/09/2026) | Qué hace Bilbito |
|---|---|---|
| Promesas de ingresos | Prohibidas las promesas de plata fácil o de resultados económicos engañosos. Es la violación más común del rubro | Cero cifras de ingresos, cero multiplicadores ("de 300 a 3 mil", "ganá 5 veces más"), cero paneles de ventas en el anuncio. Solo tiempo, orden, claridad |
| Salud y bienestar | Bajar de peso, dietas, suplementos y procedimientos estéticos: solo a mayores de 18. Prohibido el antes y después del cuerpo y hacer sentir mal a alguien con su cuerpo | Si el nicho toca salud o peso, avisarle a el-panadero antes de que se elija: es la zona más estrecha |
| Salud: medición | Meta limita desde 2025 (al menos en EE. UU.) que los negocios que clasifica como salud y bienestar optimicen a eventos como Compra. No verificado para el caso de Paolo | Si el nicho es de salud, confirmar antes del test que se puede optimizar a Compra |
| Atributos personales | El anuncio no puede afirmar ni insinuar algo de quien lo mira: salud, plata, deudas, religión, orientación, etc. | "¿Tenés deudas?" no; "Cómo ordenan sus deudas los que [X]" sí. Tercera persona |
| Antes y después | Prohibido en salud y cuerpo; engañoso si muestra resultados improbables | Solo con cosas (planilla desordenada contra ordenada). Nunca cuerpo ni plata |
| Testimonios y reseñas | Tienen que ser reales; los inventados son engaño | Solo testimonios reales con permiso. "4.9 de 5" solo si es el promedio real |
| Escasez y urgencia | Engañosa si no es verdad | "Sube mañana" solo si sube mañana. Un archivo no se agota: "quedan 5 cupos" no va |
| Categorías especiales | Empleo, crédito, vivienda y temas sociales o políticos exigen declarar la categoría; la segmentación queda limitada | Si el producto es, por ejemplo, para conseguir trabajo, se declara la categoría de empleo |
| Edad | Varias categorías exigen 18+ | 18+ siempre, aunque el tema no lo pida: el que paga con tarjeta es adulto y te ahorra un rechazo |
| IA realista | TikTok pide etiquetar el contenido generado con IA que parece real; Meta lo pide en temas sociales y políticos y etiqueta por su cuenta | Personaje o voz hechos con IA: etiquetar. Si además da consejos de salud, no usarlo |
| Engagement falso | Comprar seguidores, likes o comentarios viola las políticas | Nunca |

TikTok tiene sus propias reglas y suele ser igual o más estricto en peso y en promesas de plata (no
verificado): se leen sus políticas antes de gastar un sol ahí.

## Lista de chequeo antes de publicar cada anuncio

Si alguna respuesta es "sí", el anuncio no sale.

1. ¿Promete plata, ingresos o un resultado económico, aunque sea insinuado?
2. ¿Afirma algo de quien lo mira ("vos tenés", "vos sufrís")?
3. ¿Muestra un antes y después del cuerpo, o de plata?
4. ¿Toca salud, peso o apariencia sin estar dirigido a 18+?
5. ¿Usa un testimonio, una reseña o un "4.9 de 5" que no es real?
6. ¿Usa una urgencia o una escasez que no es verdad?
7. ¿Promete algo que la página de Whop no cumple?
8. ¿Tiene una persona o voz hecha con IA que parece real y no está etiquetada?
9. ¿El producto cae en empleo, crédito o vivienda y no se declaró la categoría especial?

Y una pregunta final: si un desconocido lo compra y lo lee, ¿se siente estafado? Si la respuesta es "un poco", no sale.
