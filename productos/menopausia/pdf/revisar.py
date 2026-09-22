#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Revisa un PDF armado con armar.py. No toca el PDF.

    python productos/menopausia/pdf/revisar.py                      # revisa salida/grasa-abdominal-perimenopausia.pdf
    python productos/menopausia/pdf/revisar.py salida/muestra.pdf

Hace:
  1. Una PNG de cada página en salida/revision/ (para mirarlas).
  2. La prueba del pulgar: la portada en miniatura (como en la galería del celular) y la
     misma miniatura con un "pulgar" tapando la esquina de abajo a la derecha.
  3. Chequea que cada link del índice lleve a la página donde está esa sección, y que cada
     cita [n] lleve a la página de Fuentes.
  4. Tamaño de hoja, peso y letras incrustadas.

Necesita: pip install pymupdf pillow
"""

import re
import sys
import unicodedata
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SALIDA = AQUI / "salida"


def normal(s):
    s = "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s).strip().lower()


def main():
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            pass
    try:
        import pymupdf
    except ImportError:
        raise SystemExit("Falta PyMuPDF: pip install pymupdf pillow")

    arg = sys.argv[1] if len(sys.argv) > 1 else str(SALIDA / "grasa-abdominal-perimenopausia.pdf")
    pdf_path = next((c for c in (Path(arg), AQUI / arg, SALIDA / arg) if c.exists()), None)
    if not pdf_path:
        raise SystemExit(f"No encuentro {arg}")
    pdf_path = pdf_path.resolve()
    carpeta = SALIDA / "revision"
    carpeta.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    base = pdf_path.stem

    # 1. páginas (borra las PNG viejas de este mismo PDF para que no queden páginas de más)
    for vieja in carpeta.glob(f"{base}-p*.png"):
        vieja.unlink()
    for n, pagina in enumerate(doc, start=1):
        pagina.get_pixmap(dpi=110).save(carpeta / f"{base}-p{n:02d}.png")

    # 2. prueba del pulgar + hoja con todas las páginas en chico (para ver páginas medio vacías)
    miniatura = carpeta / f"{base}-portada-miniatura.png"
    doc[0].get_pixmap(dpi=24).save(miniatura)  # A5 a 24 dpi = unos 140 px de ancho
    try:
        from PIL import Image, ImageDraw
        img = Image.open(miniatura).convert("RGB")
        w, h = img.size
        dibujo = ImageDraw.Draw(img)
        dibujo.ellipse([int(w * 0.62), int(h * 0.70), int(w * 1.25), int(h * 1.25)], fill=(214, 170, 150))
        img.save(carpeta / f"{base}-portada-pulgar.png")

        columnas, ancho = 7, 180
        paginas = [Image.open(carpeta / f"{base}-p{n:02d}.png").convert("RGB") for n in range(1, len(doc) + 1)]
        alto = round(ancho * paginas[0].height / paginas[0].width)
        filas = -(-len(paginas) // columnas)
        hoja = Image.new("RGB", (columnas * (ancho + 10) + 10, filas * (alto + 10) + 10), (120, 120, 120))
        for k, pag in enumerate(paginas):
            hoja.paste(pag.resize((ancho, alto)), (10 + (k % columnas) * (ancho + 10), 10 + (k // columnas) * (alto + 10)))
        hoja.save(carpeta / f"{base}-todas.png")
    except ImportError:
        print("  (sin Pillow no hay pulgar ni hoja de todas las páginas: pip install pillow)")

    # 3. links. Chrome guarda los links internos como destinos con nombre (el id del HTML):
    #    s-...      = entrada del índice -> la página tiene que tener ese título
    #    indice     = link "Índice" de cada sección -> la página del índice
    #    fuente-N   = cita [N] -> una página de Fuentes que tenga el ítem N
    paginas_texto = [normal(p.get_text()) for p in doc]
    enlaces = []
    for n, pagina in enumerate(doc, start=1):
        for link in pagina.get_links():
            if link.get("kind") in (pymupdf.LINK_GOTO, pymupdf.LINK_NAMED) and link.get("page", -1) >= 0:
                enlaces.append((n, link, link["page"] + 1, link.get("nameddest") or ""))
    inicio_fuentes = next((d for _, _, d, nombre in enlaces if nombre.startswith("s-fuentes")), None)
    errores, revisados, citas = [], 0, 0
    for n, link, destino, nombre in enlaces:
        revisados += 1
        texto_destino = paginas_texto[destino - 1]
        if nombre == "indice":
            if "indice" not in texto_destino[:40]:
                errores.append(f"p.{n}: el link 'Índice' lleva a la p.{destino}, que no es el índice")
        elif nombre.startswith("fuente-"):
            citas += 1
            numero = nombre.split("-", 1)[1]
            if inicio_fuentes is None or destino < inicio_fuentes:
                errores.append(f"p.{n}: la cita [{numero}] lleva a la p.{destino}, antes de Fuentes")
            elif not re.search(rf"(^|\s){numero}\.\s", doc[destino - 1].get_text()):
                errores.append(f"p.{n}: la cita [{numero}] lleva a la p.{destino}, y ahí no está la fuente {numero}")
        else:
            texto = normal(doc[n - 1].get_textbox(link["from"]))
            m = re.match(r"^(.*?)\s*(\d+)$", texto)               # entrada del índice: "título  12"
            titulo, numero = (m.group(1), int(m.group(2))) if m else (texto, None)
            if numero is not None and numero != destino:
                errores.append(f"p.{n}: '{titulo}' dice p.{numero} pero el link lleva a la p.{destino}")
            elif titulo and titulo[:25] not in texto_destino:
                errores.append(f"p.{n}: '{titulo}' lleva a la p.{destino}, y ahí no está ese título")
            else:
                print(f"  ok  índice p.{n}: '{titulo}' -> p.{destino}")
    print(f"  citas [n] revisadas: {citas}")

    # 4. hoja, peso y letras
    ancho_mm = doc[0].rect.width / 72 * 25.4
    alto_mm = doc[0].rect.height / 72 * 25.4
    letras = sorted({f[3] for p in doc for f in p.get_fonts()})
    peso = pdf_path.stat().st_size / 1024 / 1024
    print(f"Hoja: {ancho_mm:.0f} x {alto_mm:.0f} mm  |  Páginas: {len(doc)}  |  Peso: {peso:.2f} MB")
    print(f"Letras incrustadas: {', '.join(letras)}")
    print(f"Links internos revisados: {revisados}  |  Errores: {len(errores)}")
    for e in errores:
        print(f"  ERROR {e}")
    print(f"PNG en: {carpeta}")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
