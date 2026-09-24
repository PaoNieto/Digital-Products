# Plana todo el día — qué abrir

Reto de 28 días para desinflamar el abdomen y marcar cintura. Se vende con Whop a US$27.

## Si querés ver el producto

| Abrí esto | Qué es |
|---|---|
| `producto/plana-todo-el-dia.pdf` | **El producto.** 38 páginas, es lo que recibe la compradora |
| `producto/portada.png` | La tapa, también sirve para la página de Whop |
| `producto/hoja-de-seguimiento.pdf` | La hoja de 1 página para imprimir o marcar en el celular |

Con esos tres alcanza. El resto es cocina.

## Si querés ver las decisiones

| Archivo | Qué contesta |
|---|---|
| `documentos/BRIEF.md` | A quién le vendemos, qué le prometemos, qué tiene adentro |
| `documentos/NOTAS.md` | Precio, garantía, lo que deja cada venta, la voz de la clienta |
| `documentos/PAUTA.md` | El plan de anuncios y de testeo en Meta, con los ganchos escritos |
| `documentos/CONTENIDO.md` | Todo el texto del PDF, en borrador |
| `documentos/DISENO.md` | Colores, letra y cómo se ve cada página |

## Si hay que rehacer el PDF

Todo lo técnico está en `taller/`. No hace falta abrirlo nunca, salvo para esto:

```
cd taller
python construir.py
```

Rehace el PDF, la tapa y la hoja, y los deja en `producto/`. Antes conviene correr
`python revisar.py`, que avisa si alguna página se está comiendo texto.

Las ilustraciones de los ejercicios se dibujan con código: `taller/ilustraciones/generar.py`.
Para verlas todas juntas, `taller/ilustraciones/muestras.png`.

## Lo que falta

- Abrir el PDF en un celular de verdad y leerlo sin agrandar.
- Las 3 imágenes para la página de venta de Whop.
- Escribir la página de venta y abrir la cuenta de Whop.
