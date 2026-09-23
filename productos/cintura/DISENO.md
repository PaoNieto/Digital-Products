# Diseño de "Plana todo el día"

_Diseñante, 23/09/2026. La camiseta del equipo: poco y siempre igual._
_El archivo que manda es `estilo.css`. Este documento lo explica; no lo repite._

## La ficha: 2 colores, 1 letra, 3 tamaños

| Qué | Decisión | Dónde se usa |
|---|---|---|
| **Color 1 — tinta** | `#1A1A1A` | todo el texto y la flecha de las ilustraciones |
| **Color 2 — acento** | `#0E7C66` (verde jade) | títulos, cajas, siluetas, y el **botón del checkout de Whop** |
| Fondo | blanco `#FFFFFF` | siempre |
| Letra | **Open Sans** (400, 600, 700) | una sola, en todo |
| Título | 26 pt negrita, en acento | uno por página |
| Subtítulo | 15 pt semi-negrita, en gris | la bajada del título |
| Texto | 12.5 pt, interlineado 1.62 | el cuerpo |

Tres aclaraciones honestas:

- **El acento tiene dos versiones aguadas**, no son colores nuevos: `#93C3B7` (el lado
  lejano del cuerpo en las ilustraciones) y `#EDF5F2` (fondo de cajas y de ilustraciones).
  Es el mismo verde con más agua, como un café cortado.
- **Hay un cuarto tamaño, 8.5 pt**, y solo para el número de página, las etiquetas de
  tabla y las notas al pie. Nunca para algo que haya que leer entero.
- **Las tablas van a 11 pt.** En una hoja de 6 × 9 pulgadas, 12.5 pt en tabla obliga a
  partir palabras.

### Por qué este verde y no otro

Las 4 competidoras que trajo El Gato juegan al "quema grasa": rojo, naranja y negro. El
verde jade dice lo contrario, que es justo el ángulo del producto: esto no es grasa, es
hinchazón y postura. Y no es el rosa fucsia de fitness femenino, que es el default del
que conviene escaparse.

Contraste medido (mínimo WCAG AA: 4.5 a 1 para texto):

| Combinación | Contraste |
|---|---|
| Tinta sobre blanco | 17.4 : 1 |
| Acento sobre blanco, y blanco sobre acento (la tapa) | 5.13 : 1 |
| Acento sobre el fondo de caja | 4.63 : 1 |
| Gris de servicio `#5C6B67` sobre blanco | 5.59 : 1 |

El fondo de caja empezó en `#E8F2EF` y daba **4.49 : 1**: raspaba el mínimo por una
centésima. Se aclaró a `#EDF5F2`. Ese es el número que movió la decisión.

## Cómo se ve una página tipo

Hoja de **6 × 9 pulgadas** (tipo libro, no A4). En el celular una hoja chica se lee sin
zoom; una A4 obliga a agrandar. Márgenes: 1.6 cm a los lados, 1.6 arriba, 1.9 abajo.

```
┌──────────────────────────────┐
│ RUTINA 4 · 12 MINUTOS        │ ← etiqueta de sección, 8.5 pt, en acento
│ ──────────────────────────── │
│                              │
│ Piso: cinturón interno       │ ← título, 26 pt, acento
│ y glúteo                     │
│ El glúteo dormido es medio   │ ← bajada, 15 pt, gris
│ problema de postura...       │
│                              │
│     ┌──────────────────┐     │ ← ilustración: 76% del ancho, centrada
│     │   [silueta]      │     │
│     └──────────────────┘     │
│     pie de la ilustración    │
│                              │
│ Puente de glúteo ······  15  │ ← nombre en negrita · dosis en acento
│ Boca arriba, pies apoyados.  │ ← el cómo, 11 pt, debajo
│                              │
│ Puente a una pierna ·· 8 x 2 │
│ Igual, con una pierna...     │
│                       Pág. 13│
└──────────────────────────────┘
```

Reglas de la página: **una columna**, **una idea por página**, título arriba siempre,
número de página siempre, y un único estilo de caja destacada (fondo aguado + barra de
acento a la izquierda).

## El estilo de las 25 ilustraciones

Una sola línea visual, y no la dibuja un modelo de imagen: la dibuja
`ilustraciones/generar.py`. **Un generador de imágenes cambia de trazo en cada tirada e
inventa brazos de más.** Acá la figura se arma siempre con las mismas piezas y lo único
que cambia son las coordenadas de las articulaciones. Molde de galletas, no un dibujante
distinto cada vez.

| Regla | Detalle |
|---|---|
| Marco | 440 × 300 siempre, esquinas redondeadas, fondo `#EDF5F2` |
| Piso | una línea gris verdosa, **siempre a la misma altura** en las 25 |
| Encuadre | la figura se centra sola y se apoya en el piso: ninguna queda torcida |
| Cuerpo | silueta plana en acento, **sin cara**, sin ropa, sin músculos; pelo recogido |
| Profundidad | el brazo y la pierna del fondo, en el acento aguado `#93C3B7` |
| Separación | lo que está adelante lleva un halo del color del fondo: un brazo nunca se funde con el tronco |
| Flecha | negra, gruesa. **Recta = a dónde va el movimiento.** Curva = solo para girar |
| Vista | siempre de perfil, mirando a la derecha |
| Prohibido | fotos, caras, gestos, sombras, degradados, texto adentro del dibujo |

**Muestras hechas: 3 de 25** (respiración 360, puente de glúteo, plancha lateral de
rodillas). Ver `ilustraciones/muestras.png`. Las otras 22 salen copiando un bloque de
`POSES` y cambiando coordenadas; están listadas en `PENDIENTES` dentro del script.

## Lo que no se hace, nunca

- Sellos de "más vendido", "número 1", estrellas o cantidad de alumnas: **no hay ventas
  todavía**. Un sello inventado trae devoluciones, y las devoluciones cuestan la cuenta.
- Fotos de cuerpos reales, de stock o generadas. Ni antes y después.
- Emoji. Degradados violeta y azul de "IA genérica". Una quinta tipografía.

## Los archivos

| Archivo | Qué es |
|---|---|
| `estilo.css` | **la ficha, de verdad.** Un color o un tamaño se cambia acá y cambia en las tres piezas |
| `portada.html` → `portada.png` | la tapa, 1200 × 1800 (6 × 9 pulgadas a 200 ppp) |
| `plana-todo-el-dia.html` → `.pdf` | el reto: **30 páginas**, hoja de 6 × 9, índice con links, 3 ilustraciones |
| `hoja-de-seguimiento.html` → `.pdf` | la hoja de 1 página en A4, para imprimir |
| `ilustraciones/generar.py` | el molde de las 25 siluetas |
| `tipografia/` | Open Sans (licencia SIL Open Font, gratis para uso comercial) |
| `construir.py` | rehace las 4 piezas: `python construir.py` |
| `revisar.py` | avisa qué páginas se desbordarían: `python revisar.py`. **Correrlo cada vez que se toca el contenido** |

Todo se arma con el Chrome que ya está instalado. Cero créditos, cero suscripciones, cero
Canva. La tapa del PDF es la misma imagen que `portada.png`: no hay dos versiones que se
puedan desincronizar.

## Pendiente

- Las 22 ilustraciones que faltan.
- Las 3 imágenes de la página de Whop (banner 16:9 + 2 vistas de adentro). No estaban en
  este pedido.
- Abrir el PDF en un celular de verdad y leerlo sin zoom: es el chequeo 3 de Whoper y
  todavía no se hizo. Lo hace Paolo.
- Poner `#0E7C66` en el botón del checkout: Whop → Settings → Checkout Branding, con letra
  `open_sans` (es una de las 3 que ofrece Whop, por eso se eligió).
