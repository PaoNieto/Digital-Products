#!/usr/bin/env python3
"""Analiza un video de YouTube sin transcripcion.

Saca metadatos, descripcion, capitulos, miniatura y hojas de capturas del
storyboard con el minuto marcado en cada cuadro, listas para mirar con `view`.

Uso:
    pip install yt-dlp pillow --break-system-packages
    python storyboard.py <url_de_youtube> <carpeta_salida> [--hojas-por-imagen 3]

Salida en <carpeta_salida>:
    resumen.txt     titulo, canal, suscriptores, fecha, vistas, likes,
                    comentarios, duracion, descripcion y capitulos
    info.json       todo lo que devolvio yt-dlp
    miniatura.jpg
    hoja_01.jpg...  capturas del video (la primera empieza con la miniatura)
"""
import argparse
import json
import os
import ssl
import subprocess
import sys
import urllib.request

from PIL import Image, ImageDraw, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
# Clientes de YouTube que hoy devuelven metadatos y storyboard desde este entorno.
CLIENTES = ["web_safari", "mweb"]
CTX = ssl._create_unverified_context()  # el proxy del entorno usa certificado propio


def info_video(url):
    for cliente in CLIENTES:
        cmd = ["yt-dlp", "--no-check-certificates",
               "--extractor-args", f"youtube:player_client={cliente}",
               "--ignore-no-formats-error", "--skip-download", "-J", url]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        if r.returncode == 0 and r.stdout.strip():
            try:
                return json.loads(r.stdout)
            except json.JSONDecodeError:
                continue
    sys.exit("YouTube bloqueo todos los clientes. Reintentar en unos minutos; "
             "la alternativa es Apify, solo con permiso de Paolo.")


def bajar(url, destino):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for _ in range(3):
        try:
            with urllib.request.urlopen(req, context=CTX, timeout=30) as resp:
                data = resp.read()
            with open(destino, "wb") as f:
                f.write(data)
            return True
        except Exception:
            continue
    return False


def mmss(seg):
    seg = int(seg)
    return f"{seg // 60}:{seg % 60:02d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("salida")
    ap.add_argument("--hojas-por-imagen", type=int, default=3)
    a = ap.parse_args()
    os.makedirs(a.salida, exist_ok=True)

    d = info_video(a.url)
    json.dump(d, open(os.path.join(a.salida, "info.json"), "w"), ensure_ascii=False)

    lineas = [
        f"TITULO: {d.get('title')}",
        f"CANAL: {d.get('channel')} ({d.get('channel_follower_count')} suscriptores)",
        f"PUBLICADO: {d.get('upload_date')} | VISTAS: {d.get('view_count')} | "
        f"LIKES: {d.get('like_count')} | COMENTARIOS: {d.get('comment_count')}",
        f"DURACION: {d.get('duration_string')}",
        "", "=== DESCRIPCION ===", d.get("description") or "", "", "=== CAPITULOS ===",
    ]
    for c in d.get("chapters") or []:
        lineas.append(f"{mmss(c['start_time'])} {c['title']}")
    open(os.path.join(a.salida, "resumen.txt"), "w").write("\n".join(lineas))

    miniatura = os.path.join(a.salida, "miniatura.jpg")
    vid = d.get("id")
    if not bajar(f"https://i.ytimg.com/vi/{vid}/maxresdefault.jpg", miniatura):
        bajar(d.get("thumbnail", ""), miniatura)

    sb = [f for f in d.get("formats", []) if f.get("format_id") == "sb0"]
    if not sb:
        print("\n".join(lineas[:5]))
        sys.exit("Sin storyboard: solo quedan miniatura y descripcion.")
    sb = sb[0]
    fps = sb.get("fps") or 0.1
    filas, cols = sb.get("rows", 3), sb.get("columns", 3)
    paso = 1 / fps

    hojas = []
    for i, frag in enumerate(sb.get("fragments", [])):
        ruta = os.path.join(a.salida, f"_frag{i:02d}.jpg")
        if not bajar(frag["url"], ruta):
            continue
        try:
            im = Image.open(ruta)
            im.load()
            im = im.convert("RGB")
        except Exception:
            continue
        w, h = im.size
        cw, ch = w // cols, (h // filas if h >= filas * 90 else 180)
        dib = ImageDraw.Draw(im)
        for k in range(filas * cols):
            r, c = divmod(k, cols)
            if r * ch >= h:
                break
            t = (i * filas * cols + k) * paso
            x, y = c * cw, r * ch
            dib.rectangle([x, y, x + 44, y + 14], fill=(0, 0, 0))
            dib.text((x + 3, y + 1), mmss(t), fill=(255, 255, 0))
        hojas.append(im.resize((960, int(960 * h / w))) if w != 960 else im)
        os.remove(ruta)

    grupos = []
    if os.path.exists(miniatura):
        mini = Image.open(miniatura).convert("RGB").resize((960, 540))
        grupos.append([mini] + hojas[: a.hojas_por_imagen - 1])
        resto = hojas[a.hojas_por_imagen - 1:]
    else:
        resto = hojas
    for j in range(0, len(resto), a.hojas_por_imagen):
        grupos.append(resto[j: j + a.hojas_por_imagen])

    for n, ims in enumerate(grupos, 1):
        alto = sum(im.size[1] for im in ims)
        lienzo = Image.new("RGB", (960, alto))
        y = 0
        for im in ims:
            lienzo.paste(im, (0, y))
            y += im.size[1]
        lienzo.save(os.path.join(a.salida, f"hoja_{n:02d}.jpg"), quality=90)

    print("\n".join(lineas[:5]))
    print(f"\n{len(grupos)} hojas de capturas en {a.salida} (una captura cada {paso:.1f} s)")


if __name__ == "__main__":
    main()
