# Cómo analizar YouTube: un video o un canal entero

Dos capas, siempre en este orden: primero se saca todo con comandos (datos, guion, capturas), después se piensa. Como en una autopsia: primero se pesa y se mide, después se opina.

## Qué se puede sacar

| Qué | Con qué | PC de Paolo | claude.ai o nube |
|---|---|---|---|
| Título, canal, suscriptores, fecha, vistas, likes, comentarios, duración, descripción, capítulos, miniatura | `scripts/storyboard.py` | Sí | Casi siempre sí |
| Capturas cada 5 a 10 segundos, con el minuto marcado | `scripts/storyboard.py` | Sí | Sí |
| Guion hablado (subtítulos automáticos) | `yt-dlp --write-auto-subs` + `scripts/vtt_a_texto.py` | Sí, probado el 21/09/2026 desde IP de casa | Casi siempre bloqueado (pide token o da error 429) |
| Tono, música, lo que se oye sin palabras | Nada | No | No |

Si no hay guion, el apartado lleva la línea **"Falta el guion hablado"**. Apify lo saca, pero solo con aprobación explícita de Paolo: gasta créditos.

## Preparar la PC (una vez por sesión)

En la PC de Paolo `yt-dlp` está instalado, pero su `.exe` no está en el PATH, y Python en Windows escribe los archivos en un formato que se cae con los emoji de las descripciones. Dos arreglos, sin tocar los scripts:

| | Bash | PowerShell |
|---|---|---|
| `yt-dlp` en el PATH | `export PATH="$PATH:/c/Users/Usuario/AppData/Roaming/Python/Python314/Scripts"` | `$env:PATH += ";$env:APPDATA\Python\Python314\Scripts"` |
| Archivos en UTF-8 | `export PYTHONUTF8=1` | `$env:PYTHONUTF8 = "1"` |

- Sin el primero, `storyboard.py` no encuentra `yt-dlp`. Los comandos sueltos también andan como `python -m yt_dlp`.
- Sin el segundo, `storyboard.py` se cae con `UnicodeEncodeError` al guardar `info.json`.
- El aviso "No supported JavaScript runtime" se ignora: el 21/09/2026 anduvo igual.
- Si empieza a fallar todo, primero `pip install -U yt-dlp`: YouTube cambia seguido.
- En claude.ai: `pip install yt-dlp pillow --break-system-packages`.
- Carpeta de trabajo **fuera del repo**, una por video o canal: `/tmp/vegeta/<id>` en Bash (`%TEMP%\vegeta\<id>` en Windows). Guiones y capturas son borrador y no se suben.

## Un video

1. **Datos y capturas.** `python scripts/storyboard.py <url> <carpeta>` → `resumen.txt`, `info.json`, `miniatura.jpg` y `hoja_01.jpg`, `hoja_02.jpg`...
2. **Guion.**

   ```
   python -m yt_dlp --skip-download --write-auto-subs --sub-langs "en-orig,es-orig,pt-orig" --sub-format vtt -o "<carpeta>/%(upload_date)s__%(id)s.%(ext)s" --sleep-requests 1 <url>
   python scripts/vtt_a_texto.py <carpeta>
   ```

   Sale un `.txt` con un párrafo cada 30 segundos, cada uno con su minuto (`[1:02] ...`). El `*-orig` son las palabras reales; `en` o `es` sin `-orig` pueden ser traducción automática.
   - Si no aparece ningún `.vtt`: probar `--write-subs --sub-langs "en,es"` (subtítulos cargados a mano).
   - Si YouTube bloquea (429, "Sign in to confirm you're not a bot", archivo vacío): esperar unos minutos y un reintento con `--sleep-requests 3`. Si sigue, se sigue sin guion y se escribe "Falta el guion hablado".
3. **Descripción.** Leé `resumen.txt`: la descripción y los capítulos traen los links de sus productos, afiliados y patrocinadores.
4. **Guion entero.** Un video se lee a mano. Anotá: el gancho literal de los primeros 30 segundos, el minuto en que aparece la oferta, cómo dice que consigue compradores, y cada número de ingresos o alumnos (va a "No verificado").
5. **Capturas.** Mirá las hojas en orden; la primera trae la miniatura, que es el gancho visual. Cruzá lo que se ve (paneles, pantallas de venta, precios) con lo que dice.
6. **Precios.** Revisá los links con `curl -skL -A "Mozilla/5.0"`: Gumroad (meta `product:price:amount`), Skool (precio y miembros en el texto), cursos "gratis" (quién los paga). `curl -skI` muestra a dónde redirige un link de afiliado. Cada precio con la fecha de la consulta.
7. **Armar el apartado** con los campos de "Qué trae cada dossier" del `SKILL.md`.

## Un canal entero

Default, sin preguntar: si el canal tiene hasta 100 videos, se transcriben todos; si tiene más, los de los últimos 12 meses más los 10 con más vistas. Un canal de 350 videos se mapea entero en minutos y 250 guiones bajan en una tarde, en segundo plano.

1. **Mapa del canal.**

   ```
   python -m yt_dlp --flat-playlist --print "%(id)s|%(view_count)s|%(duration)s|%(title)s" "https://www.youtube.com/@<handle>/videos" > <carpeta>/canal.txt
   ```

   Lo mismo con `/shorts` y `/streams` si los tiene. El handle real está en `uploader_url` del `info.json` de cualquier video suyo: no lo adivines.
2. **Guiones y descripciones de la muestra.**

   ```
   python -m yt_dlp --skip-download --write-auto-subs --sub-langs "en-orig,es-orig,pt-orig" --sub-format vtt --write-description --match-filter "upload_date >= AAAAMMDD" -o "<carpeta>/%(upload_date)s__%(id)s.%(ext)s" --ignore-errors --quiet --sleep-requests 1 "https://www.youtube.com/@<handle>/videos"
   ```

   Para los 10 con más vistas que queden afuera: sus links en `lista.txt` y el mismo comando con `-a lista.txt` en vez del canal y sin `--match-filter`. Con más de 30 videos, corrélo en segundo plano.
3. **Limpiar.** `python scripts/vtt_a_texto.py <carpeta>` convierte todos los `.vtt` de la carpeta.
4. **Minar.** Cien mil palabras no se leen a mano:
   - En cuántos videos aparece cada concepto: `grep -il "skool" <carpeta>/*.txt | wc -l`. Probá con precio, curso, comunidad, afiliado, email, regalo, garantía, anuncios, Whop, Gumroad, Skool, Stan.
   - Cómo lo dice: `grep -ioh ".\{0,80\}skool.\{0,80\}" <carpeta>/*.txt | head`.
   - Su negocio real: `grep -ohE "https?://[^ )]+" <carpeta>/*.description | sort | uniq -c | sort -rn | head -30`. Los links que más repite son lo que vende.
   - Leé enteros solo los videos firma: los 5 con más vistas y los que venden su oferta.
5. **Números del canal.** Vistas **mediana** (no promedio: un viral lo infla), cuántos son shorts (menos de 60 segundos), videos por mes (la fecha sale del nombre de cada archivo), top 10 por vistas.
6. **Armar el dossier** con `metodo/dossier-canal.md`.

Trampas de `yt-dlp` que ya costaron tiempo:

- `--print` fuerza modo simulación: combinado con `--write-auto-subs` no baja nada. Una pasada para el mapa, otra para los guiones.
- `--flat-playlist` no trae fechas (sale `NA`) y redondea las vistas (11000). Fechas exactas: del nombre de archivo de la segunda pasada. Vistas exactas: `storyboard.py` o `-J` del video.
- `--break-match-filter` corta en la entrada del canal. Usá solo `--match-filter`.
- El título del mapa puede venir traducido automáticamente; el real está en la metadata completa.
- La página de un video puede leer "147 mil suscriptores" como 147. Los suscriptores de los canales chicos (menos de 100k) se verifican en el canal: `python -m yt_dlp --flat-playlist --playlist-items 1 -J "https://www.youtube.com/@<handle>/videos"`.

## Demanda de una búsqueda

Es la fila de "Demanda en YouTube" de `digimones/mercado.md`: mediana de vistas de los 12 primeros videos, cuántos son de los últimos 12 meses y quién domina.

```
python -m yt_dlp --skip-download --extractor-args "youtube:lang=es" --print "%(id)s|%(view_count)s|%(upload_date)s|%(duration)s|%(channel_follower_count)s|%(channel)s|%(uploader_id)s|%(title)s" "ytsearch12:<búsqueda>" > <carpeta>/r_<n>.txt
```

- Tarda unos 70 segundos por búsqueda. Con `--flat-playlist` es más rápido, pero no trae fechas.
- "Quién domina": qué canal se lleva más vistas de las 12 y si hay canales chicos (menos de 100k suscriptores) con videos que pegan. Canal chico que pega = se puede entrar sin ser gigante.
- Autocompletado (sirve para encontrar subnichos): `https://suggestqueries-clients6.youtube.com/complete/search?client=youtube&hl=es&gl=pe&ds=yt&q=<búsqueda>`. Probar también prefijos cortos.

## Dónde se guarda

El único lugar es `digimones/` del repo Digital-Products (`C:\Users\Usuario\Digital Products\Digital-Products`). No se escribe en el doc viejo de Claude Docs (quedó congelado al 19/09/2026) ni en la memoria de Vendí.

### Un video → `digimones/videos.md`

- Leé el archivo antes de escribir: si Paolo editó algo, sus palabras ganan.
- Una fila al final del tablero, con el número de video que sigue.
- Apartado "Video N" antes de "Lo que se repite en todos": título con la idea central, una línea con los datos del canal, paso a paso, gancho (literal con minuto, o visual), "Cómo gana plata el creador", "No verificado", "Falta el guion hablado" si corresponde, y el link.
- El link en "Fuentes"; el creador en "Cómo ganan los que enseñan" si es nuevo; el conteo del encabezado ("N videos de M creadores") al día; y "Limitaciones del análisis" corregida si cambió (por ejemplo, este video sí tiene guion).

### Un canal → sección "Canales" de `digimones/videos.md`

- La primera vez se crea la sección "## Canales" antes de "Lo que se repite en todos", con un tablero chico: `| Canal | Mapeados / transcritos | Qué enseña | Cómo consigue compradores | Consultado |`. Sin precios en ese tablero: viven en el apartado.
- Debajo, un apartado por canal con el formato de `metodo/dossier-canal.md`.
- Si un video de ese canal se analiza a fondo, además va al tablero principal como "Video N".

### Otra fuente → `digimones/fuentes.md`

Si no existe, se crea con este esqueleto:

```
# Otras fuentes

Todo lo que no es un video de YouTube: páginas de venta, tiendas, hilos, reseñas, notas.
Mismas reglas que videos.md: es registro de lo que hace otra gente, los números de los
creadores son "no verificado", cada precio lleva fecha, y las comisiones de Whop viven
solo en el CLAUDE.md.

## Tablero

| # | Fuente | Tipo | Revisada | Qué dice o vende | Precio visto |
|---|---|---|---|---|---|

## Detalle por fuente

### Fuente 1. <idea central>

- Link:
- Qué es:
- Lo que dice (el dolor con las palabras de quien lo escribe):
- Precios (moneda y fecha):
- No verificado:
```

### Con el repo o sin el repo

- **Con el repo (Claude Code):** commit en una rama propia (nunca directo en `main`), push, y avisá el link.
- **Sin el repo (claude.ai):** entregá la fila y el apartado como un archivo `.md` con el mismo formato, para que Paolo lo pase a Claude Code.

## Reglas de formato

- Números con coma para miles y punto para decimales (US$341,000; US$18.99).
- Fechas en día/mes/año.
- Un número que se compara vive una sola vez: los precios del formato en el tablero; las métricas del canal y los precios del creador en su apartado. Las comisiones de Whop no se copian: viven en el `CLAUDE.md`.
- Plataformas que no son Whop se anotan como "lo que usa el creador", nunca como opción.
- Nada de nichos candidatos de Paolo: eso va al `CLAUDE.md` cuando se decida.
- Del guion, al repo van solo citas cortas con minuto. El guion completo queda en la carpeta de trabajo.
- Al terminar, una línea en el chat y "mandame el siguiente". Sin conclusiones hasta que Paolo pida cruzar todo.

## Señales de humo que ya aparecieron

- Paneles de ingresos sin origen. Fijate de qué plataforma son (un panel de Stripe no es Etsy) y dividí ingresos por ventas para ver si el precio cuadra con lo que dice vender.
- "Valor" ancla de cursos gratis (US$1,997, US$4,000).
- Curso "gratis" que se activa comprando una herramienta, como Wix: el creador gana con la herramienta.
- Estimaciones de terceros (Alura, Similarweb) presentadas como ventas.
- Testimonios que solo están en la propia página del creador.
- Con guion, una más: el número que dice hablando y no muestra en pantalla.

## Límites

Solo contenido público: nada detrás de un login ni de un pago, y respetando las reglas de cada plataforma.