# Diseño: guía de grasa abdominal en la perimenopausia

_Diseñante (diseño), 22/09/2026. Plantilla de `.claude/skills/disenante/metodo/reglas-de-diseno.md`._

## Ficha de estilo

```
Comprador: mujer de 45 a 55, Latinoamérica, que come y se mueve igual que siempre pero desde
           la perimenopausia le crece la panza y no entiende por qué. Lee en el celular.
Color de texto: #1A1A1A (casi negro)
Color de acento: #A8432A (terracota; es también el del botón del checkout de Whop)
Fondo: blanco
Letra: Open Sans, negrita para títulos y normal para texto
       (título de portada: Open Sans Condensed ExtraBold, la versión angosta de la misma familia)
Tamaños: título 22 pt · subtítulo 15 pt · texto 12 pt
         (chica, solo para número de página, citas y aviso: 9.5 pt; lista de Fuentes: 9 pt)
Decidido el: 22/09/2026
```

Los grises (#666666 para el número de página, #F3F3F3 de fondo de la caja "Importante") y el
tinte #F7EEEC (el acento al 9 % sobre blanco, fondo de la caja "Haz esto") son el texto y el
acento aclarados: no cuentan como colores nuevos.

## Por qué terracota

- Es cálido y adulto: habla a una mujer de 50, no a una adolescente. No es el rosa chicle ni el
  violeta o azul de "hecho con IA".
- Remite a comida y a tierra (barro cocido): va con un plan de comer, moverse y dormir, no con
  una clínica.
- **Sin verificar:** El Gato no trajo todavía los colores de la competencia (`digimones/mercado.md`
  no tiene ese dato). Si en la Biblioteca de anuncios el anunciante más grande de "menopausia" usa
  terracota o naranja ladrillo, se cambia el acento para no parecer copia.

## Contraste medido (fórmula WCAG, la misma de webaim.org/resources/contrastchecker)

| Combinación | Relación | Mínimo (AA, texto chico) |
|---|---|---|
| Texto blanco sobre el acento #A8432A (portada, botón) | **6.00 a 1** | 4.5 a 1 |
| Acento #A8432A sobre blanco (links, citas, números) | 6.00 a 1 | 4.5 a 1 |
| Acento sobre el tinte #F7EEEC (etiqueta "Haz esto:") | 5.25 a 1 | 4.5 a 1 |
| Texto #1A1A1A sobre blanco | 17.40 a 1 | 4.5 a 1 |
| Texto #1A1A1A sobre el tinte #F7EEEC | 15.25 a 1 | 4.5 a 1 |
| Gris #666666 sobre blanco (número de página) | 5.74 a 1 | 4.5 a 1 |

## Portada: boceto en 3 líneas

1. Arriba a la izquierda, un calendario con una marca, dibujado en SVG blanco ("plan para
   seguir y marcar"). Sin imágenes hechas con IA.
2. Al medio, el título del front matter en blanco, Open Sans Condensed ExtraBold, enorme: sale
   en 4 renglones (Grasa / abdominal / en la / perimenopausia), a 50 pt, y ocupa el 34 % de la
   altura. Debajo, una rayita blanca y el subtítulo.
3. Al pie, chico: "Esta guía es educativa y no reemplaza la consulta con tu médico." Todo sobre
   fondo terracota lleno. Sin autor, sellos, estrellas ni números.

Prueba del pulgar (miniatura de unos 140 px con el pulgar tapando la esquina de abajo a la
derecha): el título se lee entero, y el pulgar solo tapa el subtítulo y el aviso. **Pasa.**

El tamaño del título lo calcula `armar.py`: la palabra "perimenopausia" es la que manda. Con la
letra normal el título ocupaba el 21 % de la altura; con la versión angosta, el 26 %; con la
angosta y un renglón por palabra llega al 34 %.

## Hoja y páginas

| Qué | Valor |
|---|---|
| Hoja | A5 (148 × 210 mm), una columna |
| Márgenes | 13 mm arriba y a los costados, 15 mm abajo |
| Interlineado | 1.4 |
| Página 1 | portada |
| Página 2 | "Empieza aquí", el primer paso, en menos de 5 minutos (chequeo 4 de Whoper) |
| Página 3 | índice con links que se tocan y el número de página de cada sección |
| Secciones (`#`) | empiezan página nueva solo si donde caen quedan menos de 65 mm libres; si no, siguen en la misma página con su barra terracota y su título. Cada sección tiene arriba un link "Índice" para volver |
| Hoja de seguimiento | una semana por página: título, tabla para llenar y líneas, siempre juntos |
| Cajas | "Haz esto": fondo tinte y barra terracota. "Importante": fondo gris y barra casi negra |
| Número de página | abajo al centro, en todas menos la portada |
| Peso | 0.41 MB (límite 20 MB) |
| Nombre | `grasa-abdominal-perimenopausia.pdf` |

Por qué el índice va en la página 3 y no en la 2: la compradora abre el PDF y lo primero que ve
es el paso 1, que hace en 5 minutos. El índice va justo después.

Por qué no todas las secciones empiezan página nueva: son 20 secciones y unas 5.500 palabras.
Con cada `#` en página nueva el PDF da **43 páginas**, y en 9 la última hoja de la sección queda
con menos de un tercio escrito. Dejando que sigan seguidas cuando hay lugar da **34 páginas**
sin cortar texto. `armar.py --estricto` vuelve a la regla de siempre página nueva.

## Cómo se arma

```
python productos/menopausia/pdf/armar.py                 # contenido.md -> pdf/salida/grasa-abdominal-perimenopausia.pdf
python productos/menopausia/pdf/revisar.py               # PNG de cada página, pulgar y links, en pdf/salida/revision/
python productos/menopausia/pdf/armar.py muestra.md      # la muestra, para probar cambios de diseño
```

| Archivo | Qué es |
|---|---|
| `pdf/armar.py` | lee el markdown y arma el PDF (tarda unos 30 s: lo arma varias veces hasta que todo cae bien) |
| `pdf/revisar.py` | revisa el PDF armado: no lo cambia |
| `pdf/plantilla.html` | portada, índice y el lugar de cada sección |
| `pdf/estilo.css` | la ficha de estilo hecha código: colores, letra, tamaños, márgenes |
| `pdf/fuentes/` | Open Sans (licencia OFL, `OFL.txt`), incrustada en el PDF |
| `pdf/muestra.md` | contenido de relleno con todos los elementos del formato |
| `pdf/salida/` | lo que se genera; ignorado por git (el producto final vive en Whop) |

Necesita: `pip install playwright pypdf` (y el Chromium de playwright, o Chrome o Edge).
Con `pymupdf` instalado arma más rápido y `revisar.py` funciona.

## Lo que cambiaría este diseño

- **Letra:** 12 pt en A5, en un celular a lo ancho, se ve como texto de unos 11 px. Se lee sin
  zoom, pero justo. Si Paolo lo abre en su celular y le cuesta, se sube a 13 pt (una línea en
  `estilo.css`): da 39 páginas (medido el 22/09/2026), 5 más que la meta de 34.
- **Acento:** si la competencia más grande usa terracota (dato de El Gato, pendiente).

## Pendiente

- Abrirlo en un celular real sin zoom y tocar 2 links del índice (chequeo 3 de Whoper).
- Imágenes de la página de Whop (portada en 16:9 y 2 o 3 páginas reales de adentro): cuando
  Whoper arme la página.
- Dibujos de los 6 ejercicios: después del 80 %.
