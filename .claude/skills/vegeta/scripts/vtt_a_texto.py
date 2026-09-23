#!/usr/bin/env python3
"""Convierte subtitulos automaticos de YouTube (.vtt) en texto limpio.

Saca los tiempos y las etiquetas, y borra las lineas repetidas del
subtitulo rodante (cada renglon aparece dos o tres veces en el .vtt).
Cada parrafo arranca con el minuto, para poder citar "min 0:05".

Uso:
    python vtt_a_texto.py <archivo.vtt | carpeta> [--cada 30]

Con una carpeta, convierte todos los .vtt que tenga. Escribe el .txt al
lado de cada .vtt y muestra cuantas palabras salieron.
"""
import argparse
import glob
import os
import re

TIEMPO = re.compile(r"^(\d+):(\d{2}):(\d{2})\.\d{3} --> ")
ETIQUETA = re.compile(r"<[^>]+>")


def segundos(m):
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))


def mmss(seg):
    return f"{seg // 60}:{seg % 60:02d}"


def convertir(ruta, cada):
    parrafos, actual, ultimo, inicio = [], [], None, None
    t = 0
    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            linea = linea.rstrip("\n")
            m = TIEMPO.match(linea)
            if m:
                t = segundos(m)
                continue
            if not linea.strip() or linea.startswith(("WEBVTT", "Kind:", "Language:")):
                continue
            texto = ETIQUETA.sub("", linea).strip()
            if not texto or texto == ultimo:
                continue
            ultimo = texto
            if inicio is None:
                inicio = t
            if t - inicio >= cada and actual:
                parrafos.append(f"[{mmss(inicio)}] " + " ".join(actual))
                actual, inicio = [], t
            actual.append(texto)
    if actual:
        parrafos.append(f"[{mmss(inicio or 0)}] " + " ".join(actual))
    salida = os.path.splitext(ruta)[0] + ".txt"
    with open(salida, "w", encoding="utf-8") as f:
        f.write("\n\n".join(parrafos) + "\n")
    palabras = sum(len(p.split()) - 1 for p in parrafos)
    print(f"{salida}: {palabras} palabras")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entrada")
    ap.add_argument("--cada", type=int, default=30, help="segundos por parrafo")
    a = ap.parse_args()
    rutas = (sorted(glob.glob(os.path.join(a.entrada, "*.vtt")))
             if os.path.isdir(a.entrada) else [a.entrada])
    for r in rutas:
        convertir(r, a.cada)


if __name__ == "__main__":
    main()
