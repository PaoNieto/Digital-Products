#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arma el PDF de la guía de menopausia a partir de un markdown. Un solo comando:

    python productos/menopausia/pdf/armar.py              # lee productos/menopausia/contenido.md
    python productos/menopausia/pdf/armar.py muestra.md   # cualquier otro .md (sirve la muestra)

Sale en productos/menopausia/pdf/salida/ (ignorada por git):
    contenido.md  ->  grasa-abdominal-perimenopausia.pdf
    otro.md       ->  otro.pdf        (muestra.md -> muestra.pdf)
Opciones: -o ruta.pdf (otro destino)  |  --estricto (cada # siempre en página nueva: más páginas)

Necesita: playwright (usa su Chromium; si no está, Chrome o Edge) y pypdf o PyMuPDF (para
leer del PDF dónde cayó cada sección). Instalar: pip install playwright pypdf
Tarda unos 30 segundos: arma el PDF varias veces hasta que todo cae bien.

Formato del markdown que entiende:
  - Front matter arriba con `titulo` y `subtitulo`: van a la portada.
  - `# Título`  = sección nueva y entrada del índice (el índice lo arma esto, con links).
    La primera sección va en la página 2, antes del índice. Las demás empiezan página nueva
    solo si donde caen quedan menos de 65 mm libres; si no, siguen en la misma página con su
    barra y su título (así no quedan páginas casi vacías).
  - `## Subtítulo` dentro de la sección.
  - `> **Haz esto:** ...`   = caja de acción (color de acento).
  - `> **Importante:** ...` = caja de aviso (gris, sobria).
  - Tablas, listas, casillas `- [ ] texto`, **negrita**, *cursiva*, links.
  - Tabla con celdas vacías = tabla para llenar: filas altas, y cada `##` con su tabla va
    entero en una página (la hoja de seguimiento queda una semana por página).
  - Citas [1] o [1, 3]: se vuelven links a la sección `# Fuentes` (lista numerada).
  - `<!-- salto -->` en una línea sola fuerza página nueva.

Para revisarlo (PNG de cada página, prueba del pulgar y links): revisar.py
"""

import argparse
import html
import os
import re
import sys
import unicodedata
import urllib.parse
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PRODUCTO = AQUI.parent
SALIDA = AQUI / "salida"
PLANTILLA = AQUI / "plantilla.html"
ESTILO = AQUI / "estilo.css"
CONTENIDO = PRODUCTO / "contenido.md"
NOMBRE_FINAL = "grasa-abdominal-perimenopausia.pdf"
AVISO = "Esta guía es educativa y no reemplaza la consulta con tu médico."
PESO_MAXIMO_MB = 20
MINIMO_TITULO_PORTADA = 1 / 3  # el título ocupa al menos un tercio de la altura

ESTADO = {"base": AQUI, "citas": set(), "fuentes": set(), "avisos": []}


def avisar(msg):
    if msg not in ESTADO["avisos"]:
        ESTADO["avisos"].append(msg)


def esc(s, quote=True):
    return html.escape(s, quote=quote)


def quitar_acentos(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", quitar_acentos(texto_plano(s)).lower()).strip("-")
    return s or "seccion"


def texto_plano(s):
    """Título sin marcas de markdown ni citas, para el índice y el nombre del PDF."""
    s = re.sub(r"\[(\d{1,3}(?:\s*[,;–-]\s*\d{1,3})*)\](?!\()", "", s)
    s = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[*_`~]", "", s)
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------- front matter

def leer_front_matter(texto):
    m = re.match(r"^---[ \t]*\n(.*?)\n---[ \t]*(?:\n|$)", texto, re.S)
    if not m:
        return {}, texto
    bloque, resto = m.group(1), texto[m.end():]
    datos = None
    try:
        import yaml
        datos = yaml.safe_load(bloque)
    except Exception:
        datos = None
    if not isinstance(datos, dict):  # sin PyYAML o con dos puntos sin comillas: lector simple
        datos = {}
        for linea in bloque.splitlines():
            mm = re.match(r"^\s*([^:#\s][^:]*?)\s*:\s*(.*?)\s*$", linea)
            if mm:
                v = mm.group(2)
                if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                    v = v[1:-1]
                datos[mm.group(1)] = v
    limpio = {}
    for k, v in datos.items():
        limpio[quitar_acentos(str(k)).strip().lower()] = "" if v is None else str(v).strip()
    return limpio, resto


# ---------------------------------------------------------------- texto en línea

RE_URL = re.compile(r"(?<![\w/\"'=])(https?://[^\s<>\"]+[^\s<>\".,;:!?)\]])")
RE_CITA = re.compile(r"([ \t]?)\[(\d{1,3}(?:\s*[,;–-]\s*\d{1,3})*)\](?!\()")
RE_LINK = re.compile(r"\[([^\]]+)\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
RE_IMG = re.compile(r"!\[([^\]]*)\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")


def ruta_imagen(src):
    if re.match(r"^(https?:|data:|file:)", src):
        return src
    p = (ESTADO["base"] / urllib.parse.unquote(src)).resolve()
    if not p.exists():
        avisar(f"No encuentro la imagen {src}")
    return p.as_uri()


def cita(grupo):
    numeros = [int(x) for x in re.findall(r"\d+", grupo)]
    ESTADO["citas"].update(numeros)
    if len(numeros) == 1:
        return f'<sup class="cita"><a href="#fuente-{numeros[0]}">[{esc(grupo)}]</a></sup>'
    partes = re.split(r"(\d+)", grupo)
    out = "".join(f'<a href="#fuente-{int(p)}">{p}</a>' if p.isdigit() else esc(p) for p in partes)
    return f'<sup class="cita">[{out}]</sup>'


def inline(texto):
    guardado = []

    def guardar(h):
        guardado.append(h)
        return f"\x00{len(guardado) - 1}\x00"

    t = texto
    t = re.sub(r"`([^`]+)`", lambda m: guardar(f"<code>{esc(m.group(1))}</code>"), t)
    t = RE_IMG.sub(lambda m: guardar(f'<img src="{esc(ruta_imagen(m.group(2)))}" alt="{esc(m.group(1))}">'), t)
    t = RE_LINK.sub(lambda m: guardar(f'<a href="{esc(m.group(2))}">{inline(m.group(1))}</a>'), t)
    t = re.sub(r"<(https?://[^>\s]+)>", lambda m: guardar(f'<a href="{esc(m.group(1))}">{esc(m.group(1))}</a>'), t)
    t = RE_URL.sub(lambda m: guardar(f'<a href="{esc(m.group(1))}">{esc(m.group(1))}</a>'), t)
    # la cita no queda sola al principio de un renglón: el espacio de antes pasa a ser duro
    t = RE_CITA.sub(lambda m: (" " if m.group(1) else "") + guardar(cita(m.group(2))), t)
    t = esc(t, quote=False)
    t = re.sub(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"__(?=\S)(.+?)(?<=\S)__", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![*\w])\*(?=[^\s*])(.+?)(?<=[^\s*])\*(?![*\w])", r"<em>\1</em>", t)
    t = re.sub(r"(?<![_\w])_(?=\S)(.+?)(?<=\S)_(?![_\w])", r"<em>\1</em>", t)
    t = re.sub(r"~~(?=\S)(.+?)(?<=\S)~~", r"<del>\1</del>", t)
    # "4 semanas", "10 minutos": el número no queda solo al final de una línea
    t = re.sub(r"(?<![^\s(])(\d+(?:[.,]\d+)?) (?=[^\W\d_])", "\\1\u00a0", t)
    # "a", "y", "o", "e", "u" no quedan solas al final de un renglón
    t = re.sub(r"(?<![^\s(\u00a0])([aeouyAEOUY]) (?=\S)", "\\1\u00a0", t)
    t = t.replace("\x01", "<br>")
    for _ in range(10):
        nuevo = re.sub(r"\x00(\d+)\x00", lambda m: guardado[int(m.group(1))], t)
        if nuevo == t:
            break
        t = nuevo
    return t


# ---------------------------------------------------------------- bloques

RE_TITULO = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
RE_ITEM = re.compile(r"^(\s*)([-*+]|\d{1,3}[.)])\s+(.*)$")
RE_SEP_TABLA = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
RE_HR = re.compile(r"^\s{0,3}([-*_])(\s*\1){2,}\s*$")
RE_SALTO = re.compile(r"^\s*<!--\s*salto.*?-->\s*$", re.I)
RE_COMENTARIO = re.compile(r"^\s*<!--")
RE_IMAGEN_SOLA = re.compile(r'^\s*!\[([^\]]*)\]\(\s*<?([^)\s>]+)>?(?:\s+"([^"]*)")?\s*\)\s*$')
RE_CASILLA = re.compile(r"^\[([ xX])\]\s+(.*)$")
RE_ETIQUETA = re.compile(r"^\s*\*\*\s*(Haz esto|Importante)\s*(:?)\s*\*\*\s*(:?)\s*(.*)$", re.I)


def sangria(linea):
    e = linea.expandtabs(4)
    return len(e) - len(e.lstrip())


def es_tabla(lineas, i):
    return ("|" in lineas[i] and i + 1 < len(lineas)
            and "-" in lineas[i + 1] and RE_SEP_TABLA.match(lineas[i + 1]) is not None)


def es_inicio_de_bloque(lineas, i):
    l = lineas[i]
    return bool(RE_TITULO.match(l) or l.lstrip().startswith(">") or RE_HR.match(l)
                or RE_ITEM.match(l) or es_tabla(lineas, i) or RE_COMENTARIO.match(l))


def unir(lineas):
    """Une las líneas de un párrafo; dos espacios o \\ al final = salto de línea."""
    partes = []
    for k, l in enumerate(lineas):
        corte = k < len(lineas) - 1 and (l.endswith("  ") or l.rstrip().endswith("\\"))
        l = l.strip()
        if corte and l.endswith("\\"):
            l = l[:-1].rstrip()
        partes.append(l + ("\x01" if corte else ""))
    return inline(" ".join(partes).replace("\x01 ", "\x01"))


def celdas(linea):
    s = linea.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", s)]


def tabla(cabecera, separador, filas):
    alineaciones = []
    for c in celdas(separador):
        c = c.strip()
        if c.startswith(":") and c.endswith(":"):
            alineaciones.append("center")
        elif c.endswith(":"):
            alineaciones.append("right")
        else:
            alineaciones.append("")
    ancho = max([len(cabecera)] + [len(f) for f in filas])
    if any(len(f) > len(cabecera) for f in filas):
        avisar("Una tabla tiene filas con más celdas que la cabecera")

    def estilo(k):
        a = alineaciones[k] if k < len(alineaciones) else ""
        return f' style="text-align:{a}"' if a else ""

    cab = "".join(f"<th{estilo(k)}>{inline(cabecera[k]) if k < len(cabecera) else ''}</th>" for k in range(ancho))
    cuerpo = []
    for f in filas:
        f = f + [""] * (ancho - len(f))
        cuerpo.append("<tr>" + "".join(f"<td{estilo(k)}>{inline(c)}</td>" for k, c in enumerate(f)) + "</tr>")
    return f"<table><thead><tr>{cab}</tr></thead><tbody>{''.join(cuerpo)}</tbody></table>"


def caja(interior, fuentes):
    k = next((x for x, s in enumerate(interior) if s.strip()), None)
    if k is None:
        return ""
    m = RE_ETIQUETA.match(interior[k])
    if not m:
        return f'<blockquote class="cita-libre">{bloques(interior, fuentes)}</blockquote>'
    palabra, dos_puntos = m.group(1), (m.group(2) or m.group(3))
    clase = "accion" if quitar_acentos(palabra).lower().startswith("haz") else "aviso"
    resto = m.group(4)
    interior = interior[:k] + ([resto] if resto.strip() else []) + interior[k + 1:]
    etiqueta = esc(palabra + dos_puntos)
    contenido = bloques(interior, fuentes)
    if resto.strip() and contenido.startswith("<p>"):
        # "**Haz esto:** camina 10 minutos" -> la etiqueta queda en la misma línea que la frase
        contenido = f'<p><strong class="etiqueta">{etiqueta}</strong> {contenido[3:]}'
    else:
        # "**Haz esto:**" solo en su línea (por ejemplo, antes de una lista)
        contenido = f'<p class="etiqueta">{etiqueta}</p>{contenido}'
    return f'<blockquote class="{clase}">{contenido}</blockquote>'


def quitar_sangria(lineas):
    llenas = [sangria(l) for l in lineas if l.strip()]
    if not llenas:
        return []
    corte = min(llenas)
    return [l.expandtabs(4)[corte:] if l.strip() else "" for l in lineas]


def lista(lineas, i, fuentes):
    n = len(lineas)
    m = RE_ITEM.match(lineas[i])
    base = sangria(lineas[i])
    ordenada = m.group(2)[0].isdigit()
    inicio = int(re.match(r"\d+", m.group(2)).group()) if ordenada else 1
    items = []

    def es_item_propio(l):
        mm = RE_ITEM.match(l)
        return bool(mm) and sangria(l) <= base + 1 and (mm.group(2)[0].isdigit() == ordenada) and not RE_HR.match(l)

    while i < n:
        l = lineas[i]
        if es_item_propio(l):
            items.append({"texto": [RE_ITEM.match(l).group(3)], "sub": []})
            i += 1
            continue
        if not l.strip():
            j = i
            while j < n and not lineas[j].strip():
                j += 1
            if j < n and items and (es_item_propio(lineas[j]) or sangria(lineas[j]) > base + 1):
                if sangria(lineas[j]) > base + 1:
                    items[-1]["sub"].append("")
                i = j
                continue
            break
        if not items:
            break
        if sangria(l) > base + 1:
            if not items[-1]["sub"] and not RE_ITEM.match(l):
                items[-1]["texto"].append(l)          # continuación de la misma línea
            else:
                items[-1]["sub"].append(l)            # lista anidada o párrafo del ítem
            i += 1
            continue
        if not es_inicio_de_bloque(lineas, i):        # continuación perezosa
            if items[-1]["sub"]:
                items[-1]["sub"].append(l)
            else:
                items[-1]["texto"].append(l)
            i += 1
            continue
        break

    todas_casillas = not ordenada and all(RE_CASILLA.match(it["texto"][0].strip()) for it in items)
    lis = []
    for k, it in enumerate(items):
        texto = " ".join(s.strip() for s in it["texto"])
        clases = []
        mc = RE_CASILLA.match(texto)
        if mc:
            clases.append("casilla")
            if mc.group(1).lower() == "x":
                clases.append("marcada")
            texto = mc.group(2)
        atributo_id = ""
        if fuentes and ordenada:
            atributo_id = f' id="fuente-{inicio + k}"'
            ESTADO["fuentes"].add(inicio + k)
        contenido = unir([texto])
        if any(s.strip() for s in it["sub"]):
            contenido += bloques(quitar_sangria(it["sub"]), fuentes)
        clase = f' class="{" ".join(clases)}"' if clases else ""
        lis.append(f"<li{atributo_id}{clase}>{contenido}</li>")
    etiqueta = "ol" if ordenada else "ul"
    start = f' start="{inicio}"' if ordenada and inicio != 1 else ""
    clase = ' class="casillas"' if todas_casillas else ""
    return f"<{etiqueta}{start}{clase}>{''.join(lis)}</{etiqueta}>", i


def bloques(lineas, fuentes=False):
    out = []
    i, n = 0, len(lineas)
    while i < n:
        l = lineas[i]
        if not l.strip():
            i += 1
            continue
        if RE_SALTO.match(l):
            out.append('<div class="salto"></div>')
            i += 1
            continue
        if RE_COMENTARIO.match(l):
            while i < n and "-->" not in lineas[i]:
                i += 1
            i += 1
            continue
        m = RE_TITULO.match(l)
        if m:
            nivel = len(m.group(1))
            if nivel >= 3:
                avisar(f"Hay un título de nivel {nivel} (###): se muestra como texto en negrita")
                etiqueta = "h3"
            else:
                etiqueta = "h2"
            out.append(f"<{etiqueta}>{inline(m.group(2))}</{etiqueta}>")
            i += 1
            continue
        if RE_HR.match(l):
            out.append("<hr>")
            i += 1
            continue
        if l.lstrip().startswith(">"):
            j, interior = i, []
            while j < n:
                lj = lineas[j]
                if lj.lstrip().startswith(">"):
                    interior.append(re.sub(r"^\s*> ?", "", lj))
                    j += 1
                elif lj.strip() and interior and interior[-1].strip() and not es_inicio_de_bloque(lineas, j):
                    interior.append(lj)
                    j += 1
                else:
                    break
            out.append(caja(interior, fuentes))
            i = j
            continue
        if es_tabla(lineas, i):
            cabecera, separador = celdas(lineas[i]), lineas[i + 1]
            j, filas = i + 2, []
            while j < n and lineas[j].strip() and "|" in lineas[j]:
                filas.append(celdas(lineas[j]))
                j += 1
            out.append(tabla(cabecera, separador, filas))
            i = j
            continue
        if RE_ITEM.match(l):
            h, i = lista(lineas, i, fuentes)
            out.append(h)
            continue
        mi = RE_IMAGEN_SOLA.match(l)
        if mi:
            pie = f"<figcaption>{inline(mi.group(3))}</figcaption>" if mi.group(3) else ""
            out.append(f'<figure><img src="{esc(ruta_imagen(mi.group(2)))}" alt="{esc(mi.group(1))}">{pie}</figure>')
            i += 1
            continue
        j, partes = i, []
        while j < n and lineas[j].strip() and (j == i or not es_inicio_de_bloque(lineas, j)):
            partes.append(lineas[j])
            j += 1
        out.append(f"<p>{unir(partes)}</p>")
        i = j
    return "\n".join(out)


# ---------------------------------------------------------------- secciones y documento

def partir_secciones(cuerpo):
    previo, secciones, actual = [], [], None
    for l in cuerpo.split("\n"):
        m = re.match(r"^#\s+(.*?)\s*#*\s*$", l)
        if m:
            actual = {"titulo": m.group(1).strip(), "lineas": []}
            secciones.append(actual)
        elif actual is None:
            previo.append(l)
        else:
            actual["lineas"].append(l)
    return previo, secciones


def es_fuentes(titulo):
    t = quitar_acentos(texto_plano(titulo)).lower()
    return t.startswith(("fuentes", "referencias", "bibliografia"))


def html_seccion(sec, forzadas=frozenset()):
    fuentes = es_fuentes(sec["titulo"])
    cuerpo = bloques(sec["lineas"], fuentes)
    clase = "seccion fuentes" if fuentes else "seccion"
    if sec["id"] in forzadas:
        clase += " pagina-nueva"
    if "<td></td>" in cuerpo:
        # Tiene tablas para llenar (hoja de seguimiento): cada ## con su tabla y sus líneas va en
        # un bloque que no se parte entre páginas. Así queda una semana por página.
        clase += " para-llenar"
        grupos, actual = [], []
        for l in sec["lineas"]:
            if re.match(r"^##\s", l) and actual:
                grupos.append(actual)
                actual = []
            actual.append(l)
        grupos.append(actual)
        partes = []
        for k, g in enumerate(grupos):
            html_grupo = bloques(g, fuentes)
            if k > 0 or re.match(r"^##\s", next((x for x in g if x.strip()), "")):
                html_grupo = f'<div class="grupo">{html_grupo}</div>'
            partes.append(html_grupo)
        cuerpo = "\n".join(partes)
    # El id (destino del link del índice) va en la barra visible, no en la <section>: si Chrome
    # deja el borde de la sección al pie de una página y pasa el contenido a la siguiente, el
    # link igual cae donde se ve el título.
    return (f'<section class="{clase}">\n'
            f'<div class="seccion-cabeza" id="{sec["id"]}"><span class="barra"></span>'
            f'<a class="ir-indice" href="#indice">Índice</a></div>\n'
            f'<h1>{inline(sec["titulo"])}</h1>\n{cuerpo}\n</section>')


def documento(datos, previo, secciones, numeros, estricto=False, forzadas=frozenset()):
    titulo = datos.get("titulo", "")
    subtitulo = datos.get("subtitulo", "")
    htmls = [html_seccion(s, forzadas) for s in secciones]
    if any(l.strip() for l in previo):
        avisar("Hay texto antes del primer # : se pone al principio de la primera sección")
        htmls[0] = htmls[0].replace("</h1>\n", "</h1>\n" + bloques(previo) + "\n", 1)
    indice = "\n".join(
        f'    <li><a href="#{s["id"]}"><span class="t">{esc(texto_plano(s["titulo"]))}</span>'
        f'<span class="n">{numeros.get(s["id"], "00")}</span></a></li>'
        for s in secciones)
    valores = {
        "CLASE_BODY": "estricto" if estricto else "",
        "TITULO_TEXTO": esc(texto_plano(titulo)),
        "CSS": ESTILO.as_uri(),
        "TITULO": inline(titulo),
        "SUBTITULO": inline(subtitulo),
        "AVISO": esc(AVISO),
        "PRIMERA_SECCION": htmls[0],
        "INDICE": indice,
        "RESTO": "\n\n".join(htmls[1:]),
    }
    plantilla = PLANTILLA.read_text(encoding="utf-8")
    return re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: valores.get(m.group(1), m.group(0)), plantilla)


# ---------------------------------------------------------------- navegador y PDF

AJUSTAR_PORTADA = r"""
async (previo) => {
  await document.fonts.ready;
  await Promise.all([...document.fonts].map(f => f.load().catch(() => null)));
  const portada = document.querySelector('.portada');
  const t = document.getElementById('portada-titulo');
  const H = portada.clientHeight;
  // cabe = ninguna palabra se sale del ancho, nada se sale de la portada y el título no pasa de media hoja
  const cabe = () => t.scrollWidth <= t.clientWidth + 0.5
      && portada.scrollHeight <= H + 0.5
      && t.offsetHeight <= H * 0.5;
  const mayorQueCabe = () => {
    let lo = 20, hi = 96;
    for (let k = 0; k < 22; k++) {
      const mid = (lo + hi) / 2;
      t.style.fontSize = mid + 'pt';
      if (cabe()) lo = mid; else hi = mid;
    }
    lo = Math.floor(lo * 2) / 2;
    t.style.fontSize = lo + 'pt';
    return lo;
  };
  // Dos formas de cortar el título:
  //   "natural": el navegador corta donde entra.
  //   "renglones": una palabra por renglón; las palabras cortas (en, la, de, 4...) van pegadas a la
  //   siguiente. Sirve cuando una palabra larga (perimenopausia) limita el tamaño y el título
  //   queda bajo: con un renglón más llega a 1/3 de la altura sin achicar la letra.
  // Para cada forma prueba anchos de caja del 100 % al 50 %. Gana la letra más grande que llegue
  // a 1/3; si ninguna llega, la que más se acerque. No cambia ninguna palabra.
  const natural = t.innerHTML;
  let renglones = null;
  if (t.children.length === 0) {
    const palabras = t.textContent.trim().split(/ +/);
    const corta = w => w.replace(/[^\p{L}\p{N}]/gu, '').length <= 3;
    const grupos = [];
    let actual = [];
    palabras.forEach((w, k) => {
      actual.push(w);
      if (!corta(w) || k === palabras.length - 1) { grupos.push(actual.join(' ')); actual = []; }
    });
    if (grupos.length > 1) renglones = grupos;
  }
  const ponerForma = forma => {
    if (forma === 'natural' || !renglones) { t.innerHTML = natural; return; }
    t.textContent = '';
    renglones.forEach(g => {
      const s = document.createElement('span');
      s.className = 'renglon';
      s.textContent = g;
      t.appendChild(s);
    });
  };
  let mejor = previo;  // en las vueltas siguientes se reusa lo calculado en la primera
  for (const forma of (previo ? [] : (renglones ? ['natural', 'renglones'] : ['natural']))) {
    ponerForma(forma);
    for (let w = 100; w >= 50; w -= 2.5) {
      t.style.maxWidth = w + '%';
      const pt = mayorQueCabe();
      const c = { forma, w, pt, alto: t.offsetHeight / H };
      const llega = c.alto >= 1 / 3, mejorLlega = mejor && mejor.alto >= 1 / 3;
      if (!mejor || (llega && (!mejorLlega || c.pt > mejor.pt)) || (!llega && !mejorLlega && c.alto > mejor.alto)) {
        mejor = c;
      }
    }
  }
  ponerForma(mejor.forma);
  t.style.maxWidth = mejor.w + '%';
  t.style.fontSize = mejor.pt + 'pt';
  const cargadas = [...document.fonts].filter(f => f.status === 'loaded').length;
  return { pt: mejor.pt, ancho: mejor.w, forma: mejor.forma, alto: t.offsetHeight / H, cabe: cabe(), fuentes: cargadas };
}
"""


def abrir_navegador(p):
    ultimo = None
    for opciones in ({}, {"channel": "chrome"}, {"channel": "msedge"}):
        try:
            return p.chromium.launch(**opciones)
        except Exception as e:  # noqa: BLE001
            ultimo = e
    raise SystemExit(f"No pude abrir Chromium, Chrome ni Edge: {ultimo}\n"
                     "Probá: python -m playwright install chromium")


def imprimir(navegador, html_path, pdf_path, final=True, portada_previa=None):
    """final=False: vuelta de prueba, más rápida (sin marcadores ni etiquetas de accesibilidad,
    que no cambian dónde cae nada). portada_previa: el ajuste del título ya calculado."""
    pagina = navegador.new_page()
    pagina.emulate_media(media="print")
    pagina.goto(html_path.as_uri(), wait_until="load")
    previo = None
    if portada_previa:
        previo = {"forma": portada_previa["forma"], "w": portada_previa["ancho"], "pt": portada_previa["pt"]}
    portada = pagina.evaluate(AJUSTAR_PORTADA, previo)
    pagina.pdf(path=str(pdf_path), prefer_css_page_size=True, print_background=True,
               outline=final, tagged=final)
    pagina.close()
    return portada


def paginas_de_secciones(pdf_path, ids):
    """Dónde empieza cada sección, leído del PDF: {id: (página, mm libres debajo)}.
    Página 1 = portada. Los mm libres van desde el comienzo de la sección hasta el margen de abajo.
    Usa PyMuPDF si está (40 veces más rápido); si no, pypdf."""
    try:
        import pymupdf
        with pymupdf.open(str(pdf_path)) as doc:
            nombres = doc.resolve_names()
            encontradas = {}
            for clave, destino in nombres.items():
                if clave in ids and destino.get("page", -1) >= 0:
                    arriba = (destino.get("to") or (0, None))[1]
                    libre = (float(arriba) / 72 * 25.4 - MARGEN_INFERIOR_MM) if arriba is not None else 999.0
                    encontradas[clave] = (destino["page"] + 1, libre)
            return encontradas, len(doc)
    except Exception:  # noqa: BLE001  (sin PyMuPDF o versión vieja: sigue con pypdf)
        pass
    try:
        from pypdf import PdfReader
    except ImportError:
        return None
    lector = PdfReader(str(pdf_path))
    encontradas = {}
    try:
        destinos = lector.named_destinations
    except Exception:  # noqa: BLE001
        destinos = {}
    for nombre, destino in destinos.items():
        clave = urllib.parse.unquote(str(nombre).lstrip("/"))
        if clave in ids:
            try:
                pagina = lector.get_destination_page_number(destino) + 1
                arriba = destino.top
                libre = (float(arriba) / 72 * 25.4 - MARGEN_INFERIOR_MM) if arriba is not None else 999.0
                encontradas[clave] = (pagina, libre)
            except Exception:  # noqa: BLE001
                pass
    return encontradas, len(lector.pages)


def margen_inferior_mm():
    """El margen de abajo de la hoja, leído de estilo.css (así no hay que copiarlo acá)."""
    m = re.search(r"@page\s*\{[^}]*?margin:\s*([\d.]+)mm\s+([\d.]+)mm\s+([\d.]+)mm",
                  ESTILO.read_text(encoding="utf-8"))
    return float(m.group(3)) if m else 15.0


MARGEN_INFERIOR_MM = margen_inferior_mm()
LUGAR_MINIMO_MM = 65  # una sección que caería con menos lugar libre que esto empieza página nueva


# ---------------------------------------------------------------- principal

def resolver_entrada(arg):
    if not arg:
        if not CONTENIDO.exists():
            raise SystemExit(f"Todavía no existe {CONTENIDO}.\n"
                             f"Para probar: python {Path(__file__).name} muestra.md")
        return CONTENIDO
    for candidato in (Path(arg), AQUI / arg, PRODUCTO / arg):
        if candidato.exists():
            return candidato.resolve()
    raise SystemExit(f"No encuentro {arg}")


def main():
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            pass
    ap = argparse.ArgumentParser(description="Arma el PDF de la guía a partir de un markdown.")
    ap.add_argument("entrada", nargs="?", help="markdown (si no se pasa: productos/menopausia/contenido.md)")
    ap.add_argument("-o", "--salida", help="ruta del PDF (si no se pasa: pdf/salida/...)")
    ap.add_argument("--estricto", action="store_true",
                    help="cada # empieza página nueva siempre (más páginas, algunas casi vacías)")
    args = ap.parse_args()

    entrada = resolver_entrada(args.entrada)
    if args.salida:
        pdf_path = Path(args.salida).resolve()
    elif entrada.resolve() == CONTENIDO.resolve():
        pdf_path = SALIDA / NOMBRE_FINAL
    else:
        pdf_path = SALIDA / f"{entrada.stem}.pdf"
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    html_path = pdf_path.with_suffix(".html")
    ESTADO["base"] = entrada.parent

    texto = entrada.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
    datos, cuerpo = leer_front_matter(texto)
    if not datos.get("titulo"):
        avisar("Falta `titulo` en el front matter: la portada queda sin título")
    if not datos.get("subtitulo"):
        avisar("Falta `subtitulo` en el front matter")
    previo, secciones = partir_secciones(cuerpo)
    if not secciones:
        raise SystemExit("El markdown no tiene ninguna sección (# Título).")
    usados = set()
    for s in secciones:
        base = sid = "s-" + slug(s["titulo"])
        k = 2
        while sid in usados:
            sid, k = f"{base}-{k}", k + 1
        usados.add(sid)
        s["id"] = sid
    ids = [s["id"] for s in secciones]

    from playwright.sync_api import sync_playwright

    # Se arma en archivos temporales propios y recién al final reemplaza el PDF: si otro chat
    # arma o lee el mismo PDF a la vez, nadie ve un archivo a medio escribir.
    tmp_html = pdf_path.with_name(f".{pdf_path.stem}-{os.getpid()}.html")
    tmp_pdf = pdf_path.with_name(f".{pdf_path.stem}-{os.getpid()}.pdf")
    # Vueltas: arma el PDF, mira dónde cayó cada sección y corrige.
    #   1) Si una sección empieza con menos de LUGAR_MINIMO_MM libres, la manda a página nueva
    #      (de a una y en orden: mover una solo corre las que vienen después).
    #   2) Pone en el índice las páginas reales y repite hasta que no cambien.
    numeros, forzadas, portada, total_paginas = {}, set(), None, None
    with sync_playwright() as p:
        navegador = abrir_navegador(p)
        for _ in range(len(ids) + 6):
            ESTADO["citas"], ESTADO["fuentes"] = set(), set()
            tmp_html.write_text(documento(datos, previo, secciones, numeros, args.estricto, forzadas),
                                encoding="utf-8")
            portada = imprimir(navegador, tmp_html, tmp_pdf, final=False, portada_previa=portada)
            leido = paginas_de_secciones(tmp_pdf, ids)
            if leido is None:
                avisar("Falta pypdf (pip install pypdf): el índice sale sin números de página y "
                       "las secciones no se acomodan solas")
                break
            posiciones, total_paginas = leido
            if len(posiciones) < len(ids):
                avisar("No pude leer la página de todas las secciones: revisá el índice")
            if not args.estricto:
                baja = next((s for s in ids if s not in forzadas and s in posiciones
                             and posiciones[s][1] < LUGAR_MINIMO_MM), None)
                if baja:
                    forzadas.add(baja)
                    continue
            reales = {k: str(v[0]) for k, v in posiciones.items()}
            if reales == numeros:
                break
            numeros = reales
        # vuelta final, con marcadores y etiquetas de accesibilidad
        ESTADO["citas"], ESTADO["fuentes"] = set(), set()
        tmp_html.write_text(documento(datos, previo, secciones, numeros, args.estricto, forzadas),
                            encoding="utf-8")
        portada = imprimir(navegador, tmp_html, tmp_pdf, final=True, portada_previa=portada)
        leido = paginas_de_secciones(tmp_pdf, ids)
        if leido:
            posiciones, total_paginas = leido
            if {k: str(v[0]) for k, v in posiciones.items()} != numeros:
                avisar("La vuelta final no coincide con el índice: volvé a correr armar.py")
        navegador.close()

    try:
        os.replace(tmp_pdf, pdf_path)
    except PermissionError:
        otro = pdf_path.with_name(f"{pdf_path.stem}-nuevo.pdf")
        os.replace(tmp_pdf, otro)
        avisar(f"{pdf_path.name} está abierto en otro programa: el nuevo quedó como {otro.name}")
        pdf_path = otro
    try:
        os.replace(tmp_html, html_path)
    except PermissionError:
        tmp_html.unlink(missing_ok=True)

    sin_fuente = sorted(ESTADO["citas"] - ESTADO["fuentes"])
    if sin_fuente:
        avisar(f"Citas sin su fuente en la lista de # Fuentes: {', '.join(map(str, sin_fuente))}")
    peso = pdf_path.stat().st_size / 1024 / 1024
    if peso >= PESO_MAXIMO_MB:
        avisar(f"El PDF pesa {peso:.1f} MB: pasa el límite de {PESO_MAXIMO_MB} MB")
    if portada and portada["alto"] < MINIMO_TITULO_PORTADA:
        avisar(f"El título de la portada ocupa {portada['alto']:.0%} de la altura: menos de un tercio "
               "(título muy corto). Se ve bien igual, pero conviene mirarlo.")
    if portada and not portada["cabe"]:
        avisar("El título de la portada no entra ni a 20 pt: acortalo")

    print(f"PDF listo: {pdf_path}")
    print(f"  Páginas: {total_paginas or '?'}  |  Peso: {peso:.2f} MB (límite {PESO_MAXIMO_MB} MB)")
    if portada:
        print(f"  Portada: título a {portada['pt']:g} pt, corte {portada['forma']}, caja del {portada['ancho']:g}% "
              f"del ancho; ocupa el {portada['alto']:.0%} de la altura (mínimo 33%)  |  letras cargadas: {portada['fuentes']}")
    print("  Índice (* = se pasó a página nueva porque caía con poco lugar):")
    for s in secciones:
        marca = "*" if s["id"] in forzadas else " "
        print(f"    p. {numeros.get(s['id'], '?'):>3} {marca} {texto_plano(s['titulo'])}")
    if ESTADO["avisos"]:
        print("Avisos:")
        for a in ESTADO["avisos"]:
            print(f"  - {a}")


if __name__ == "__main__":
    main()
