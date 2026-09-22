# Biblioteca de anuncios y funnel hacking — paso a paso

Para El Gato. Verificado el 21/09/2026 en la ayuda de Meta
(https://www.facebook.com/help/259468828226154): la Biblioteca es pública y gratis, se
busca en https://www.facebook.com/ads/library, muestra los anuncios **activos** de
cualquier tipo, y solo los de política y temas sociales muestran gasto, alcance y
anuncios inactivos. En la Unión Europea y el Reino Unido hay opciones distintas.
Los nombres de los botones cambian seguido: si algo no aparece donde dice acá, se
busca y se anota el cambio, no se inventa.

## 1. Keywords (antes de abrir la Biblioteca)

Salen de la frase del comprador de el-panadero ("enfermera del turno noche que no puede
dormir de día"). 5 a 10 por comprador, en el idioma del comprador:

| Tipo | Ejemplo (ilustrativo) |
|---|---|
| El dolor, en sus palabras | "no puedo dormir de día" |
| El resultado | "dormir 7 horas turno noche" |
| El formato | "guía", "plantilla", "ebook", "curso", "checklist" |
| Quién es | "enfermera", "night shift nurse" |

Bola de nieve (el truco de Santi Bilbao, que usaba ChatGPT para esto; acá lo hace
Claude): de cada anuncio que encontrás se sacan las palabras que usa el anunciante y
se vuelve a buscar con ellas.

## 2. Buscar

1. Abrir https://www.facebook.com/ads/library
2. País: el del comprador. Si el comprador es de cualquier lado, "Todos".
3. Categoría: todos los anuncios (no la de política).
4. Escribir la keyword y buscar.
5. Filtros si hacen falta: idioma, plataforma, tipo de medio, fechas.

## 3. Leer cada anuncio

| Dato | Dónde se ve | Cómo se usa |
|---|---|---|
| Fecha en que empezó a circular | en la tarjeta del anuncio | días corriendo = hoy − esa fecha |
| Creativos activos del anunciante | entrar al anunciante dentro de la Biblioteca y contar sus anuncios activos | 7 o más = está escalando |
| Varias versiones del mismo anuncio | aviso en la tarjeta | cuenta como un creativo con variantes, no como 7 |
| Link de destino | botón del anuncio | ahí empieza el funnel hacking |

Qué **no** muestra la Biblioteca en anuncios comerciales: cuánto gastan, cuántos lo
vieron, cuánto venden. Cualquier número de ese tipo sale de otra herramienta y es
"no verificado".

## 4. Funnel hacking (sin pagar)

1. Clic en el anuncio → página de venta. Anotar promesa, formato, qué incluye, prueba,
   garantía (días y dónde está dicha).
2. Botón de compra → checkout. Anotar precio, moneda, si hay bump (casilla "sumá X por
   US$Y") y si hay suscripción escondida.
3. No se completa el pago. Si el-panadero necesita ver el producto por dentro, lo pide y
   Paolo decide si lo compra (es plata de la prueba).
4. Si la página menciona upsell o "siguiente paso" (curso, comunidad, acompañamiento),
   se anota como backend con el precio que se vea. Si no se ve, va vacío.

## 5. La fila (en `digimones/mercado.md` del repo)

Una fila por observación. Nunca se pisa una fila vieja: el historial es el dato.

| Fecha | Comprador candidato | Anunciante | Qué vende | Precio visto | Promesa (textual, solo registro) | Garantía | Backend | Días corriendo (el más viejo) | Creativos activos | Link | Señal |
|---|---|---|---|---|---|---|---|---|---|---|---|

Si un dato no se vio, la celda va vacía. No se estima.

## 6. El veredicto (formato fijo)

```
¿Ya se paga? — comprador: <frase de el-panadero>
Veredicto: ya se paga / señal débil / no se sabe
Evidencia: <N> anunciantes; el más viejo corre hace <X> días; el más grande tiene <Y>
creativos activos (Biblioteca, dd/mm/aaaa).
Lo que lo cambia: <el número; ej. "si en 2 semanas ninguno sigue activo, baja a señal débil">
```

Umbrales (ver SKILL.md): menos de 3 días no cuenta; 3+ días = pasó la prueba; 7+
creativos activos = escalando; "ya se paga" pide 2 anunciantes distintos con señal
fuerte (supuesto nuestro).

## Errores que se repiten

| Error | Por qué está mal |
|---|---|
| Celebrar "no hay competencia" | Casi siempre significa que nadie encontró cómo cobrarle a ese comprador |
| Contar anuncios de 1 día | Son pruebas; la mayoría se apaga |
| Tomar el panel de ingresos de un creador como dato | No verificado, siempre |
| Copiar texto, imágenes o promesas | Se modela la estructura, se escribe de cero |
| Mezclar países | Un anuncio en EE. UU. no prueba hambre en Perú, ni al revés |
| Proponer la plataforma donde vende el competidor | Es registro de lo que hace otra gente; acá solo Whop |
