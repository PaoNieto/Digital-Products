# -*- coding: utf-8 -*-
"""
Arma las piezas finales del producto "Plana todo el dia" a partir de los HTML.

  python construir.py

Sale:
  portada.png                      la tapa, 1200 x 1800 (6 x 9 pulgadas a 200 ppp)
  plana-todo-el-dia.pdf            el PDF del reto, hoja de 6 x 9 pulgadas
  hoja-de-seguimiento.pdf          la hoja de 1 pagina, A4, para imprimir
  ilustraciones/muestras.png       las 3 ilustraciones juntas, para mirarlas de una

Usa el Chrome (o el Edge) que ya esta instalado. No instala nada ni gasta creditos.
"""

import os
import shutil
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))


def navegador():
    for ruta in (r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                 r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"):
        if os.path.exists(ruta):
            return ruta
    hallado = shutil.which("chrome") or shutil.which("msedge") or shutil.which("chromium")
    if not hallado:
        sys.exit("No encontre Chrome ni Edge. Instala uno y volve a correr.")
    return hallado


NAV = navegador()


def url(nombre):
    return "file:///" + os.path.join(AQUI, nombre).replace("\\", "/")


def correr(args):
    r = subprocess.run([NAV, "--headless", "--disable-gpu", "--hide-scrollbars",
                        "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
                        "--virtual-time-budget=6000"] + args,
                       capture_output=True, timeout=300)
    if r.returncode != 0:
        print(r.stderr.decode("utf-8", "ignore")[-800:])


def captura(html, png, ancho, alto, escala=2):
    correr([f"--window-size={ancho},{alto}", f"--force-device-scale-factor={escala}",
            "--screenshot=" + os.path.join(AQUI, png), url(html)])
    print("imagen:", png)


def pdf(html, salida):
    correr(["--print-to-pdf=" + os.path.join(AQUI, salida), "--print-to-pdf-no-header", url(html)])
    print("pdf:   ", salida)


if __name__ == "__main__":
    captura("portada.html", "portada.png", 600, 900)
    captura("ilustraciones/muestras.html", "ilustraciones/muestras.png", 520, 1290)
    pdf("plana-todo-el-dia.html", "plana-todo-el-dia.pdf")
    pdf("hoja-de-seguimiento.html", "hoja-de-seguimiento.pdf")
    print("\nListo. Abri el PDF en el celular antes de publicarlo.")
