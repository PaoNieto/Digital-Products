# Digimones — el equipo de productos digitales

Los agentes de este negocio. Son a Digital-Products lo que los minions son a Vendí: otro
equipo, otras cuentas. Ningún digimon usa números de Vendí y ningún minion trabaja acá.

_Última actualización: 23/09/2026_

## Regla de nombre

Al nombrar un digimon, siempre **nombre + rol entre paréntesis**: `Mercaneto (cuentas)`.
Los nombres los eligió Paolo. En claude.ai, Diseñante figura como `disenante` (sin ñ).

## El equipo

| Digimon | Rol | Qué hace | Cuándo entra | Viene de |
|---|---|---|---|---|
| **el-panadero** | producto | Es el jefe. Decide a quién se le vende, qué problema se resuelve y qué formato se hace. Por ahora también lleva el canal orgánico | Siempre, es el primero | — |
| **Vegeta** | investigación | Analiza videos y canales de YouTube (con transcripción), fuentes y creadores, y guarda todo en esta carpeta | Cuando hay algo para investigar | Willy |
| **El Gato** | espía | Espía anuncios y ofertas de la competencia. Si un anuncio lleva mucho tiempo corriendo, es prueba de que ya se paga | Al validar una idea | Adsioso |
| **Mercaneto** | cuentas | Precio, validación, lo que deja cada venta, garantía, devoluciones y contracargos, cuenta de Whop y retiros | Al poner precio o hacer cuentas | El Comerciante |
| **Whoper** | vidriera | Escribe la página de venta dentro de Whop, arma el checkout y la entrega, y hace los 4 chequeos antes de publicar | Con producto y precio definidos | Frontero |
| **Diseñante** | diseño | Portada, maquetado del PDF o ebook, look de la plantilla de Notion, miniaturas | Con producto definido | Davinci |
| **Bilbito** | pauta | Anuncios pagados con el método de Santi Bilbao: testeo, escalado y anti-baneo | Recién después de 10 ventas a desconocidos | Metapod |
| **Bibliomon** | bibliografía | Busca información de cualquier tema en cualquier circunstancia para detallar y respaldar el contenido de un producto, con fuente, link y fecha de cada dato | Al escribir o revisar el contenido de un producto | — |

## Compuertas

1. Nada se construye hasta que haya un comprador con nombre y su problema en una frase.
2. Bilbito no gasta un sol hasta que `CLAUDE.md` marque 10 de 10 ventas a desconocidos.
3. Cuentas y números de Whop: solo en `CLAUDE.md`. Ningún digimon los copia.

## Dónde vive cada cosa

- **El manual de cada digimon** vive en este repo, en `.claude/skills/<nombre>/`, y su
  ficha para lanzarlo en `.claude/agents/<nombre>.md`. En Claude Code, dentro de este
  repo, ya funcionan. Para usarlos también en claude.ai se sube el zip de cada uno en
  Settings → Capabilities → Skills; si cambia un manual, se rearma su zip.
- **Lo que aprenden** vive en esta carpeta, y crece solo por la regla de `CLAUDE.md`:

| Archivo | Qué guarda | Quién lo llena |
|---|---|---|
| `DIGIMONES.md` | este equipo | se actualiza cuando cambia un rol o entra un digimon |
| `videos.md` | videos y canales analizados | Vegeta |
| `fuentes.md` | estudios, documentación, artículos y libros, por tema | Vegeta |
| `mercado.md` | ofertas, precios y anuncios de la competencia, con fecha | El Gato (se crea con la primera observación) |
| `publicaciones.md` | cada publicación propia y de dónde vino cada venta | el-panadero (se crea con la primera publicación) |
| `productos/<producto>/BIBLIOGRAFIA.md` | cada dato del contenido del producto con su fuente | Bibliomon |

## Huecos del equipo

- Nadie tiene todavía el canal orgánico como tarea única: lo lleva el-panadero hasta que
  haga falta un digimon para eso.
