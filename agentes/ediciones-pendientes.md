# Ediciones pendientes en los agentes de la cuenta

Los agentes `el-panadero`, `el-comerciante` y `metapod` viven en la **cuenta** de Paolo,
no en este repo. En disco están en un directorio `synced/`, que es una copia bajada del
servidor: **editar el archivo local no sirve, la próxima sincronización lo pisa.**

Estas ediciones se hacen en **claude.ai → Settings → Capabilities → Skills → \<agente\>**.

`el-pregonero` no está en esta lista: vive en este repo (`.claude/skills/el-pregonero/`),
versionado en git, y no hay nada que sincronizar.

---

## 1. el-panadero — URGENTE, hoy contradice el CLAUDE.md

Dos líneas vivas mandan a plataformas prohibidas. Hasta que se arreglen, el agente
titular de esta rama recomienda salir de Whop.

### 1a. Borrar la fila de Gumroad de "Números base"

En la tabla de comisiones, borrar la fila entera de Gumroad (era la línea 71).
**No se corrige: se borra.** Los números de Whop viven solo en el `CLAUDE.md` del repo.
Dejar en su lugar:

```
Las comisiones, el costo de retiro y lo que deja cada venta viven en el CLAUDE.md
del repo Digital-Products. Se leen de ahí, no se copian acá.
```

### 1b. Reescribir la sección "Frontera con los otros agentes"

Hoy dice textual, en la última línea: *"**Integral** entra si se cobra con Mercado Pago
o Shopify **en vez de Whop**."* Es la puerta de salida de Whop, escrita adentro del
agente titular. Reemplazar la sección completa (eran las líneas 107-112) por:

```markdown
## Frontera con los otros agentes

- **el-comerciante** decide precio y validación (Office Hours), y es el único que hace
  cuentas: comisión, retiro, devoluciones y el setup de la cuenta de Whop. El Panadero
  le trae formatos y precios vistos en el mercado.
- **el-pregonero** trae la gente y escribe la página de venta: canal, gancho, guiones,
  cadencia, DM, portada y miniaturas. El Panadero elige el comprador; el Pregonero
  escribe las palabras para ese comprador.
- **metapod** decide la pauta paga, y recién después de 10 ventas a desconocidos.
  Riesgo a pasarle: Meta restringe anuncios de infoproductos que prometen resultados.

Cobro: **solo Whop**. Cualquier otra pasarela que aparezca en un video o en research es
registro de lo que hace otra gente, nunca una opción para Paolo.
```

Willy, Davinci e Integral salen de la sección: son de Vendí.

### 1c. Marcar las dos filas de la tabla de formatos que obligan plataforma

- "Clipart hecho con IA en Etsy" → agregar **"exige Etsy: NO aplica acá"**.
- "Comunidad paga" → agregar **"ojo: el acceso automático a Discord/Telegram cuesta
  +3% en Whop; entregar el acceso a mano"**.

### 1d. Bajar la tabla de los US$15,000 y sacarla de la description

La tabla "cuánto hay que vender para US$15,000 al mes" no se borra (sirve para
"¿cuánto puedo ganar?"), pero:

- Se mueve **abajo** de la prueba de las 10 ventas.
- Se encabeza con: *"Esto no es la meta de este trimestre. El hito es 10 ventas a
  desconocidos."*
- Se saca de la `description` la frase "la cuenta para llegar a US$15k al mes".

### 1e. Sumar a la description los gatillos que hoy faltan

Sin esto hay preguntas típicas que no despiertan a nadie:

- **Formatos que se cayeron:** `curso, mini curso, membresía, taller`
- **Entrega** (hoy sin dueño): `entrega, cómo le llega el archivo, el archivo no abre, peso del archivo`
- **Derechos** (hoy sin dueño): `derechos, licencia, me lo copian, piratería, puedo vender lo que hizo la IA`

### 1f. Lo que NO hay que sacar de la description

Los críticos pidieron sacar `Gumroad, Etsy, Stan Store, Hotmart` de los gatillos.
**Recomendación contraria: dejarlos.** Son el gatillo que hace que el Panadero despierte
si Paolo se cruza una y pregunta qué es. El peligro nunca fue la palabra en el gatillo:
era el contenido que las ofrecía como opción, y eso lo arreglan 1a y 1b.

---

## 2. el-comerciante — agregar un modo, no reescribir

El archivo es Vendí de punta a punta (S/39, Mercado Pago, costo por crédito). **No se
reescribe.** Se agrega una sección al tope, arriba de todo:

```markdown
## Modo productos digitales

Si la conversación es del negocio de productos digitales (repo Digital-Products),
este modo gana y las secciones de Vendí de abajo NO aplican: nada de S/39, catálogo,
Mercado Pago ni costo por crédito.

- Estado: 0 productos, 0 ventas, 0 audiencia, nicho sin definir.
- No hay costo variable por unidad: el margen es ~90%, solo comisión.
- Los números de Whop (comisión, retiro, lo que deja cada venta) y el estado real
  viven en el CLAUDE.md del repo. Se leen de ahí, no se copian acá.
- El techo de lo que puede costar conseguir un comprador es lo que deja la venta.
- Sos el único que hace cuentas de esta rama: comisión, retiro, devoluciones,
  contracargos, y si hay garantía y de cuántos días (el-pregonero solo la redacta).

### Setup de Whop — checklist, sos el dueño

1. Abrir la cuenta.
2. Crear el producto.
3. Subir el archivo.
4. Probar que la entrega automática llega.
5. Configurar la política de devolución en el panel.
6. Firmar el W-8BEN (cobrar en dólares desde Perú).

No activar acceso automático a Discord, Telegram ni TradingView: cuesta +3%.
```

Sumar a la `description`: `comisión, cuánto me queda, retiro, transferencia, cripto,
devolución, reembolso, contracargo, acceso automático a Discord o Telegram, W-8BEN,
cobrar en dólares`.

---

## 3. metapod — una compuerta, y NO recortarle la description

### 3a. La compuerta, adentro de su propio archivo

Va al tope, **arriba del "VEREDICTO VIGENTE"** (era la línea 28). Tiene que estar dentro
de metapod: una regla escrita en el archivo del vecino no lo frena, porque cuando metapod
se activa no leyó esos archivos.

```markdown
## Compuerta — negocio de productos digitales

No se prende un peso de pauta hasta que el CLAUDE.md del repo Digital-Products marque
10 de 10 ventas a desconocidos. El techo de CAC lo dicta el-comerciante leyendo ese
archivo — no lo calculo acá.

Si el pedido es orgánico (gancho, guion, portada, miniatura, cadencia, contenido que
no se paga), no es mío: es de el-pregonero. Salgo y lo digo.

El veredicto vigente y los números de abajo son DE VENDÍ. No aplican a esta rama.
```

### 3b. La description: agregar una cláusula, no borrar palabras

El crítico de colisiones pidió sacarle `hooks y guiones`, `copy y ángulos` y `creativos`.
**No conviene: eso deja a Vendí sin nadie que escriba un anuncio.** El costo de romper
Vendí es más alto que la colisión.

En su lugar, agregar al final de la `description`:

```
En el negocio de productos digitales metapod es SOLO lo pagado (anuncios, pauta,
presupuesto, públicos, Pixel, CAC por canal, baneo): los ganchos, guiones, portadas
y la página de venta orgánicos son de el-pregonero.
```

---

## 4. Los cinco de Vendí — opcional, una línea cada uno

`willy`, `integral`, `hawkeye`, `davinci` y `frontero` se activan solos con palabras de
este negocio ("checkout de Whop", "probemos el link", "este video", "la portada",
"armemos la página").

**Dentro de este repo no hace falta arreglarlos:** el `CLAUDE.md` se carga solo y ya trae
los desempates. Esto importa cuando Paolo habla de productos digitales **en claude.ai sin
el repo abierto**, donde ese archivo no existe.

Si se hace, es una cláusula de alcance al final de cada `description`:

| Agente | Cláusula |
|---|---|
| willy | `Solo el mercado de fotografía de producto con IA (Vendí). Los videos y precios de productos digitales son de el-panadero.` |
| integral | `Solo Vendí: Mercado Pago, Shopify, Clerk, Vercel, DNS. El cobro en Whop no es mío.` |
| hawkeye | `Solo la app de Vendí. En productos digitales la prueba de antes de publicar es de el-pregonero.` |
| davinci | `Solo Cuaderno v2 de Vendí. Portadas de producto y miniaturas de productos digitales son de el-pregonero.` |
| frontero | `Solo la app de Vendí. La página de venta de productos digitales se escribe en Whop, no se programa.` |

---

## Orden de ejecución

1. **Hoy, media hora:** 1a y 1b de el-panadero. Son las dos que hoy mandan a plataformas
   prohibidas — sin esto, el titular de la rama trabaja contra la decisión de Whop.
2. Cuando haya nicho elegido: el resto de el-panadero (1c a 1e) y el modo de
   el-comerciante.
3. Cuando se acerque la venta 10: la compuerta de metapod.
4. Nunca urgente: los cinco de Vendí.

## Cómo se prueba que quedó bien

Chat nuevo, sin nombrar al agente, y ver quién despierta:

| Frase de prueba | Tiene que despertar |
|---|---|
| "¿dónde publico el PDF?" | el-panadero, y decir Whop |
| "dame un gancho para el short" | el-pregonero, no metapod |
| "¿a cuánto lo vendo?" | el-comerciante |
| "¿prendo anuncios?" | metapod, y frenar por la compuerta |
| "¿cómo le llega el archivo al que compra?" | el-panadero |
