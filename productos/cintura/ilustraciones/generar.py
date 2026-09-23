# -*- coding: utf-8 -*-
"""
Generador de las ilustraciones de ejercicios de "Plana todo el dia".

Por que un script y no un generador de imagenes con IA:
las ~25 ilustraciones tienen que ser LA MISMA mano. Un modelo de imagen cambia de
trazo, de grosor y de proporciones en cada tirada, e inventa brazos y piernas de mas.
Aca la figura se arma siempre con las mismas piezas (cabeza, cuello, tronco, brazo,
pierna), los mismos grosores y los mismos colores: lo unico que cambia entre un
ejercicio y otro son las coordenadas de las articulaciones. Es un molde de galletas,
no un dibujante distinto cada vez.

Tres cosas hacen que la serie se vea pareja sin pensarla:
  1. El marco es siempre 440 x 300 y la linea de piso siempre esta en el mismo alto.
  2. La figura se centra sola: se calcula su caja y se la apoya en el piso, al medio.
  3. Lo que esta adelante lleva un halo del color del fondo, para que un brazo nunca
     se funda con el tronco.

Como agregar un ejercicio nuevo:
  1. Copiar un bloque de POSES y cambiar las coordenadas de las articulaciones.
  2. Correr: python generar.py
  3. Sale el .svg y el .png (usa el Chrome o el Edge que ya esta instalado).
"""

import math
import os
import shutil
import subprocess

# --- Ficha de estilo (ver DISENO.md). No se cambia aca sin cambiar DISENO.md. ---
ACENTO = "#0E7C66"          # color 2 de la ficha: el cuerpo
ACENTO_LEJOS = "#93C3B7"    # el mismo acento aguado: brazo y pierna del lado de atras
FONDO = "#EDF5F2"           # el mismo acento muy aguado: fondo del recuadro y halos
PISO = "#BCD3CC"            # la linea de piso o de pared
TINTA = "#1A1A1A"           # color 1 de la ficha: solo la flecha del movimiento

MARCO_W, MARCO_H = 440, 300
PISO_Y = 252          # la linea de piso cae siempre en el mismo alto
MARGEN = 26
G_TRONCO = 40         # grosor del tronco
G_CUELLO = 21
G_MIEMBRO = 22        # brazos y piernas del lado cercano
G_LEJOS = 20          # brazos y piernas del lado lejano
R_CABEZA = 27
R_MONIO = 13
G_FLECHA = 9
HALO = 11             # cuanto sobresale el halo del color del fondo


# --- piezas: se declaran como datos, el dibujo viene despues -----------------

def tronco(*pts):    return ("linea", list(pts), G_TRONCO, ACENTO, True)
def cuello(*pts):    return ("linea", list(pts), G_CUELLO, ACENTO, False)
def miembro(*pts):   return ("linea", list(pts), G_MIEMBRO, ACENTO, True)
def atras(*pts):     return ("linea", list(pts), G_LEJOS, ACENTO_LEJOS, False)
def cabeza(x, y, monio=200): return ("cabeza", [(x, y)], monio, ACENTO, False)
def flecha(x1, y1, x2, y2):  return ("flecha", [(x1, y1), (x2, y2)], 0, TINTA, False)
def flecha_curva(x1, y1, cx, cy, x2, y2):
    return ("curva", [(x1, y1), (cx, cy), (x2, y2)], 0, TINTA, False)


def _d(pts):
    return " ".join(("M" if i == 0 else "L") + f"{x:.1f} {y:.1f}" for i, (x, y) in enumerate(pts))


def _linea(pts, ancho, color):
    return (f'<path d="{_d(pts)}" fill="none" stroke="{color}" stroke-width="{ancho}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def _punta(x, y, ang, color, extra=0):
    L, A = 26 + extra, 12 + extra
    p2 = (x - L * math.cos(ang) + A * math.sin(ang), y - L * math.sin(ang) - A * math.cos(ang))
    p3 = (x - L * math.cos(ang) - A * math.sin(ang), y - L * math.sin(ang) + A * math.cos(ang))
    pts = " ".join(f"{px:.1f},{py:.1f}" for px, py in ((x, y), p2, p3))
    return f'<polygon points="{pts}" fill="{color}" stroke="{color}" stroke-width="2" stroke-linejoin="round"/>'


def _caja(ops):
    """Caja que ocupa el cuerpo, contando el grosor del trazo. Las flechas no cuentan."""
    xs, ys = [], []
    for tipo, pts, a, _c, _h in ops:
        if tipo in ("flecha", "curva"):
            continue
        r = R_CABEZA + R_MONIO if tipo == "cabeza" else a / 2
        for x, y in pts:
            xs += [x - r, x + r]
            ys += [y - r, y + r]
    return min(xs), min(ys), max(xs), max(ys)


def render(ops, con_piso=True):
    x0, _y0, x1, y1 = _caja(ops)
    dx = (MARCO_W - (x1 - x0)) / 2 - x0
    dy = PISO_Y - y1
    mov = lambda pts: [(x + dx, y + dy) for x, y in pts]

    out = [f'<rect width="{MARCO_W}" height="{MARCO_H}" rx="26" fill="{FONDO}"/>']
    if con_piso:
        out.append(_linea([(MARGEN, PISO_Y + 4), (MARCO_W - MARGEN, PISO_Y + 4)], 7, PISO))

    for tipo, pts, a, color, halo in ops:
        p = mov(pts)
        if tipo == "linea":
            if halo:
                out.append(_linea(p, a + HALO, FONDO))
            out.append(_linea(p, a, color))
        elif tipo == "cabeza":
            (cx, cy), ang = p[0], math.radians(a)
            mx = cx + math.cos(ang) * (R_CABEZA + R_MONIO - 15)
            my = cy + math.sin(ang) * (R_CABEZA + R_MONIO - 15)
            out.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="{R_MONIO}" fill="{color}"/>')
            out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{R_CABEZA}" fill="{color}"/>')
        elif tipo == "flecha":
            (ax, ay), (bx, by) = p
            ang = math.atan2(by - ay, bx - ax)
            cx, cy = bx - 18 * math.cos(ang), by - 18 * math.sin(ang)
            out.append(_linea([(ax, ay), (cx, cy)], G_FLECHA + HALO, FONDO))
            out.append(_punta(bx, by, ang, FONDO, HALO / 2))
            out.append(_linea([(ax, ay), (cx, cy)], G_FLECHA, color))
            out.append(_punta(bx, by, ang, color))
        elif tipo == "curva":
            (ax, ay), (qx, qy), (bx, by) = p
            ang = math.atan2(by - qy, bx - qx)
            cx, cy = bx - 18 * math.cos(ang), by - 18 * math.sin(ang)
            arco = f"M{ax:.1f} {ay:.1f} Q{qx:.1f} {qy:.1f} {cx:.1f} {cy:.1f}"
            for w, col in ((G_FLECHA + HALO, FONDO), (G_FLECHA, color)):
                out.append(f'<path d="{arco}" fill="none" stroke="{col}" stroke-width="{w}" '
                           f'stroke-linecap="round"/>')
                if col == FONDO:
                    out.append(_punta(bx, by, ang, FONDO, HALO / 2))
            out.append(_punta(bx, by, ang, color))

    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {MARCO_W} {MARCO_H}" '
            f'width="{MARCO_W}" height="{MARCO_H}" role="img">' + "".join(out) + "</svg>")


# ---------------------------------------------------------------------------
# LAS POSES. Siempre de perfil, mirando a la derecha.
# Orden de dibujo: lado de atras, tronco, lado de adelante, cuello, cabeza, flecha.
# ---------------------------------------------------------------------------

def respiracion_360():
    """R1 - Respiracion 360 acostada: las costillas se abren hacia las manos."""
    return render([
        atras((240, 286), (292, 226), (310, 296), (340, 298)),
        atras((146, 280), (166, 240), (200, 268)),
        tronco((152, 276), (248, 279)),
        miembro((248, 279), (302, 214), (320, 294), (350, 296)),
        miembro((152, 267), (176, 244), (210, 262)),
        cuello((118, 272), (152, 276)),
        cabeza(92, 271, 190),
        flecha(204, 232, 158, 180),
        flecha(226, 232, 272, 180),
    ])


def puente_de_gluteo():
    """R4 - Puente de gluteo: la cadera sube soltando el aire."""
    return render([
        atras((244, 228), (304, 236), (310, 297), (340, 299)),
        atras((140, 288), (180, 298), (214, 300)),
        tronco((152, 278), (252, 220)),
        miembro((252, 220), (314, 228), (320, 295), (350, 297)),
        miembro((148, 282), (188, 293), (224, 295)),
        cuello((120, 274), (152, 278)),
        cabeza(94, 272, 190),
        flecha(258, 186, 258, 128),
    ])


def plancha_lateral_rodillas():
    """R3 - Plancha lateral de rodillas: la cadera sube hasta quedar en linea."""
    return render([
        atras((150, 240), (150, 302), (208, 306)),
        atras((260, 286), (304, 310), (248, 316), (226, 316)),
        tronco((146, 232), (268, 278)),
        miembro((268, 278), (310, 302), (252, 308), (230, 308)),
        miembro((152, 222), (196, 216), (240, 246)),
        cuello((122, 222), (146, 232)),
        cabeza(98, 216, 196),
        flecha(302, 250, 302, 192),
    ])


POSES = {
    "respiracion-360": respiracion_360,
    "puente-de-gluteo": puente_de_gluteo,
    "plancha-lateral-rodillas": plancha_lateral_rodillas,
}

# Los 22 que faltan salen del mismo molde: se copia un bloque de arriba y se cambian
# las coordenadas. Ninguno necesita una herramienta nueva.
PENDIENTES = [
    "marcha-costillas-abajo", "empuje-contra-la-pared", "antigiro-con-toalla",
    "sentadilla-a-la-silla", "elevacion-de-talones", "estiramiento-de-flexores",
    "bicho-muerto", "perro-pajaro", "giro-sentada", "rodillas-al-costado",
    "estiramiento-de-costado", "puente-a-una-pierna", "almeja", "patada-atras",
    "plancha-antebrazos", "postura-del-nino", "paso-lateral", "gato-camello",
    "rotacion-de-columna", "exhalacion-con-cierre", "hipopresivo-suave",
    "cierre-de-pie",
]


def navegador():
    for ruta in (r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                 r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"):
        if os.path.exists(ruta):
            return ruta
    return shutil.which("chrome") or shutil.which("msedge")


def main():
    aqui = os.path.dirname(os.path.abspath(__file__))
    nav = navegador()
    for nombre, fn in POSES.items():
        contenido = fn()
        with open(os.path.join(aqui, nombre + ".svg"), "w", encoding="utf-8") as f:
            f.write(contenido)
        if nav:
            html = os.path.join(aqui, "_tmp.html")
            grande = contenido.replace(f'width="{MARCO_W}" height="{MARCO_H}"',
                                       f'width="{MARCO_W*2}" height="{MARCO_H*2}"')
            with open(html, "w", encoding="utf-8") as f:
                f.write('<html><body style="margin:0">' + grande + "</body></html>")
            subprocess.run([nav, "--headless", "--disable-gpu", "--hide-scrollbars",
                            f"--window-size={MARCO_W*2},{MARCO_H*2}",
                            "--screenshot=" + os.path.join(aqui, nombre + ".png"),
                            "file:///" + html.replace("\\", "/")],
                           capture_output=True, timeout=120)
            os.remove(html)
        print("listo:", nombre)
    print(f"\n{len(POSES)} de {len(POSES) + len(PENDIENTES)} ilustraciones. Faltan {len(PENDIENTES)}.")


if __name__ == "__main__":
    main()
