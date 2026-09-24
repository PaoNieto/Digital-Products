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


def apoyo(*pts):
    """La pared o la silla. Va del color del piso y NO cuenta para centrar la figura:
    se mueve junto con ella, asi que queda siempre donde tiene que quedar."""
    return ("apoyo", list(pts), 8, PISO, False)


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
        if tipo in ("flecha", "curva", "apoyo"):
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
        if tipo == "apoyo":
            out.append(_linea(p, a, color))
        elif tipo == "linea":
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

    # Chequeo: nada tiene que quedar fuera del marco. Las flechas son las que se
    # escapan, porque no cuentan para centrar. Avisa en vez de dibujar a medias.
    for tipo, pts, a, _c, _h in ops:
        for x, y in mov(pts):
            if not (6 <= x <= MARCO_W - 6 and 6 <= y <= MARCO_H - 6):
                _FUERA.append(f"{tipo} en ({x:.0f}, {y:.0f})")

    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {MARCO_W} {MARCO_H}" '
            f'width="{MARCO_W}" height="{MARCO_H}" role="img">' + "".join(out) + "</svg>")


_FUERA = []


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


# --- resto de la Rutina 1 ---------------------------------------------------

def exhalacion_con_cierre():
    """R1 - Exhalacion larga con cierre: al soltar el aire, la zona entre las caderas
    se cierra sola. Las dos flechas apuntan una a la otra."""
    return render([
        atras((240, 286), (292, 226), (310, 296), (340, 298)),
        atras((146, 280), (172, 256), (204, 274)),
        tronco((152, 276), (248, 279)),
        miembro((248, 279), (302, 214), (320, 294), (350, 296)),
        miembro((152, 270), (180, 252), (216, 270)),
        cuello((118, 272), (152, 276)),
        cabeza(92, 271, 190),
        flecha(200, 198, 226, 238),
        flecha(276, 198, 250, 238),
    ])


def hipopresivo_suave():
    """R1 - Hipopresivo suave: con el aire afuera, la panza se mete sola hacia arriba
    y adentro. Flecha curva, porque el movimiento entra y sube."""
    return render([
        atras((190, 150), (182, 186), (176, 218)),
        atras((190, 200), (188, 248), (186, 296), (214, 298)),
        tronco((196, 196), (196, 144)),
        miembro((196, 196), (198, 246), (198, 294), (228, 296)),
        miembro((196, 144), (206, 180), (202, 212)),
        cuello((198, 132), (196, 144)),
        cabeza(204, 108, 195),
        flecha_curva(272, 214, 268, 168, 228, 152),
    ])


def cierre_de_pie():
    """R1 - Cierre de pie: costillas abajo, coronilla al techo. Asi se camina el resto
    del dia. Flecha para arriba desde la cabeza."""
    return render([
        atras((190, 150), (186, 186), (184, 218)),
        atras((190, 200), (188, 248), (186, 296), (214, 298)),
        tronco((196, 196), (196, 144)),
        miembro((196, 196), (198, 246), (198, 294), (228, 296)),
        miembro((196, 144), (204, 182), (202, 216)),
        cuello((198, 132), (196, 144)),
        cabeza(204, 108, 195),
        flecha(254, 152, 254, 98),
    ])


# --- Rutina 2: core profundo de pie -----------------------------------------

def marcha_costillas_abajo():
    """R2 - Marcha con costillas abajo: espalda contra la pared, sube una rodilla a la
    altura de la cadera sin despegar la espalda."""
    return render([
        apoyo((164, 88), (164, 310)),
        atras((192, 200), (192, 248), (192, 296), (220, 298)),
        tronco((194, 196), (194, 144)),
        miembro((196, 194), (256, 188), (252, 244), (278, 246)),
        miembro((194, 144), (204, 180), (206, 214)),
        cuello((196, 132), (194, 144)),
        cabeza(202, 108, 195),
        flecha(300, 232, 300, 176),
    ])


def empuje_contra_la_pared():
    """R2 - Empuje contra la pared: manos apoyadas, empuja fuerte soltando el aire.
    La panza no sale."""
    return render([
        apoyo((332, 78), (332, 310)),
        atras((188, 152), (242, 160), (298, 162)),
        atras((186, 200), (186, 248), (186, 296), (214, 298)),
        tronco((190, 196), (196, 144)),
        miembro((190, 196), (194, 246), (194, 294), (224, 296)),
        miembro((196, 144), (250, 150), (306, 152)),
        cuello((200, 132), (196, 144)),
        cabeza(206, 108, 195),
        flecha(238, 204, 306, 204),
    ])


def antigiro_con_toalla():
    """R2 - Antigiro con toalla: brazos estirados adelante, alguien tira de un lado y
    vos resistis sin girar el tronco. La barra vertical es la toalla enrollada."""
    return render([
        atras((186, 154), (234, 162), (282, 164)),
        atras((186, 200), (186, 248), (186, 296), (214, 298)),
        tronco((190, 196), (194, 146)),
        miembro((190, 196), (194, 246), (194, 294), (224, 296)),
        miembro((194, 146), (242, 152), (290, 156)),
        miembro((298, 138), (298, 174)),
        cuello((198, 134), (194, 146)),
        cabeza(204, 110, 195),
        flecha(310, 210, 366, 210),
    ])


def sentadilla_a_la_silla():
    """R2 y R5 - Sentadilla a la silla: sentarse y levantarse sin manos, soltando el
    aire al subir. La silla queda atras."""
    return render([
        apoyo((120, 246), (230, 246)),
        apoyo((130, 246), (130, 316)),
        apoyo((222, 246), (222, 316)),
        apoyo((124, 246), (124, 156)),
        atras((202, 246), (244, 264), (240, 302), (268, 304)),
        atras((218, 184), (250, 208), (276, 220)),
        tronco((208, 240), (226, 178)),
        miembro((208, 240), (250, 258), (246, 298), (276, 300)),
        miembro((226, 178), (258, 202), (284, 214)),
        cuello((230, 166), (226, 178)),
        cabeza(238, 142, 195),
        flecha(322, 228, 322, 172),
    ])


def elevacion_de_talones():
    """R2 - Elevacion de talones lenta: sube a la punta de los pies en 3 segundos y
    baja en 3. El talon queda en el aire."""
    return render([
        atras((190, 150), (186, 186), (184, 218)),
        atras((190, 200), (188, 246), (190, 268), (216, 296)),
        tronco((196, 196), (196, 144)),
        miembro((196, 196), (198, 246), (200, 268), (228, 296)),
        miembro((196, 144), (204, 182), (202, 216)),
        cuello((198, 132), (196, 144)),
        cabeza(204, 108, 195),
        flecha(156, 292, 156, 238),
    ])


def estiramiento_de_flexores():
    """R2 y R6 - Estiramiento de flexores: un pie adelante en tijera, mete la cola
    hacia abajo y siente adelante de la cadera de atras."""
    return render([
        atras((194, 204), (160, 250), (136, 290), (162, 294)),
        atras((196, 152), (208, 184), (194, 206)),
        tronco((200, 200), (202, 148)),
        miembro((200, 200), (252, 244), (252, 292), (282, 294)),
        miembro((202, 148), (214, 182), (198, 204)),
        cuello((204, 136), (202, 148)),
        cabeza(210, 112, 195),
        flecha(150, 168, 150, 220),
    ])


# --- Rutina 3: cintura y oblicuos -------------------------------------------

def bicho_muerto():
    """R3 y R7 - Bicho muerto: boca arriba, estira un brazo y la pierna contraria
    soltando el aire, sin despegar la espalda del piso."""
    return render([
        atras((146, 272), (154, 226), (162, 184)),
        atras((244, 282), (246, 222), (302, 216)),
        tronco((150, 278), (250, 280)),
        miembro((250, 280), (306, 276), (356, 272), (378, 264)),
        miembro((152, 270), (120, 242), (90, 222)),
        cuello((118, 274), (150, 278)),
        cabeza(94, 276, 190),
        flecha(118, 206, 86, 186),
        flecha(336, 246, 374, 240),
    ])


def perro_pajaro():
    """R3 - Perro-pajaro: en cuatro apoyos, estira brazo y pierna contraria y aguanta
    3 segundos sin torcer la cadera."""
    return render([
        atras((286, 196), (288, 246), (290, 296)),
        atras((186, 196), (186, 246), (186, 296), (152, 292), (134, 290)),
        tronco((186, 198), (286, 194)),
        miembro((286, 192), (332, 180), (378, 170)),
        miembro((186, 198), (142, 206), (98, 214)),
        cuello((306, 164), (290, 186)),
        cabeza(330, 142, 205),
        flecha(392, 166, 420, 160),
        flecha(84, 216, 56, 220),
    ])


def giro_sentada():
    """R3 - Giro sentada, lento: espalda recta, gira el tronco despacio de un lado al
    otro. La flecha curva es el giro."""
    return render([
        atras((176, 294), (244, 268), (266, 298), (294, 300)),
        atras((184, 212), (208, 244), (238, 244)),
        tronco((180, 290), (190, 206)),
        miembro((180, 290), (250, 262), (272, 294), (300, 296)),
        miembro((190, 206), (214, 240), (246, 238)),
        cuello((194, 192), (190, 206)),
        cabeza(198, 170, 195),
        flecha_curva(128, 168, 192, 116, 252, 168),
    ])


def rodillas_al_costado():
    """R3 - Rodillas al costado: boca arriba, rodillas juntas, dejalas caer despacio a
    un lado y volve con el abdomen. La flecha curva es la caida."""
    return render([
        atras((240, 286), (292, 226), (310, 296), (340, 298)),
        atras((146, 280), (192, 268), (234, 264)),
        tronco((152, 276), (248, 279)),
        miembro((248, 279), (302, 214), (320, 294), (350, 296)),
        miembro((152, 270), (198, 260), (240, 256)),
        cuello((118, 272), (152, 276)),
        cabeza(92, 271, 190),
        flecha_curva(346, 182, 306, 132, 252, 152),
    ])


def estiramiento_de_costado():
    """R3 - Estiramiento de costado: un brazo arriba, inclinate al lado contrario y
    respira hacia esas costillas."""
    return render([
        atras((214, 152), (220, 188), (224, 220)),
        atras((192, 198), (190, 248), (188, 296), (216, 298)),
        tronco((196, 194), (222, 142)),
        miembro((196, 194), (198, 246), (198, 294), (228, 296)),
        miembro((222, 142), (244, 106), (258, 72)),
        cuello((208, 132), (216, 142)),
        cabeza(200, 110, 190),
        flecha(276, 74, 314, 98),
    ])


# --- Rutina 4: piso, cinturon interno y gluteo ------------------------------

def puente_a_una_pierna():
    """R4 - Puente a una pierna: igual que el puente, con una pierna estirada. Si es
    mucho, se queda en el anterior."""
    return render([
        atras((244, 226), (304, 234), (310, 297), (340, 299)),
        atras((140, 288), (180, 298), (214, 300)),
        tronco((152, 278), (252, 220)),
        miembro((252, 220), (306, 206), (352, 194), (374, 188)),
        miembro((148, 282), (188, 293), (224, 295)),
        cuello((120, 274), (152, 278)),
        cabeza(94, 272, 190),
        flecha(238, 182, 238, 126),
    ])


def almeja():
    """R4 - Almeja: de costado, rodillas dobladas, abri la rodilla de arriba sin mover
    la cadera. La flecha curva es la rodilla que se abre."""
    return render([
        atras((244, 264), (306, 272), (288, 306)),
        atras((150, 248), (118, 234), (94, 224)),
        tronco((152, 252), (248, 256)),
        miembro((248, 254), (310, 238), (292, 284)),
        miembro((158, 248), (196, 274), (232, 298)),
        cuello((122, 250), (152, 252)),
        cabeza(96, 246, 190),
        flecha_curva(332, 292, 372, 250, 344, 202),
    ])


def patada_atras():
    """R4 - Patada atras en cuatro apoyos: empuja el talon al techo sin arquear la
    espalda."""
    return render([
        atras((286, 196), (288, 246), (290, 296)),
        atras((186, 196), (186, 246), (186, 296), (152, 292), (134, 290)),
        tronco((186, 196), (286, 196)),
        miembro((280, 202), (282, 250), (284, 298)),
        miembro((186, 196), (142, 182), (132, 132)),
        cuello((306, 166), (290, 188)),
        cabeza(330, 144, 205),
        flecha(104, 118, 104, 70),
    ])


def plancha_antebrazos():
    """R4 - Plancha de antebrazos: cuerpo en linea, costillas abajo, respirando. La
    flecha marca lo que no se tiene que hundir: la cadera."""
    return render([
        atras((144, 246), (144, 298), (200, 302)),
        atras((244, 264), (304, 278), (354, 292), (370, 302)),
        tronco((150, 240), (250, 258)),
        miembro((250, 258), (310, 272), (360, 286), (376, 296)),
        miembro((150, 240), (150, 294), (206, 298)),
        cuello((128, 230), (150, 240)),
        cabeza(106, 222, 196),
        flecha(250, 222, 250, 170),
    ])


def postura_del_nino():
    """R4, R6 y R7 - Postura del nino con respiracion: de rodillas, sentada sobre los
    talones, frente al piso, respira hacia la espalda."""
    return render([
        atras((200, 286), (152, 300), (104, 304)),
        atras((292, 184), (262, 298), (312, 300), (332, 300)),
        tronco((300, 178), (196, 278)),
        miembro((300, 178), (268, 296), (318, 298), (338, 298)),
        cuello((176, 282), (196, 278)),
        cabeza(152, 282, 15),
        flecha(258, 146, 258, 96),
    ])


# --- Rutina 5: cardio de bajo impacto ---------------------------------------

def marcha_en_el_lugar():
    """R5 - Marcha en el lugar levantando rodillas. Sin saltos: el vecino de abajo no
    se entera."""
    return render([
        atras((188, 152), (156, 178), (134, 200)),
        atras((192, 200), (192, 248), (192, 296), (220, 298)),
        tronco((194, 196), (194, 144)),
        miembro((196, 194), (256, 186), (252, 244), (278, 246)),
        miembro((194, 144), (218, 180), (244, 170)),
        cuello((196, 132), (194, 144)),
        cabeza(202, 108, 195),
        flecha(296, 224, 296, 170),
    ])


def paso_lateral():
    """R5 - Paso lateral amplio: los pies bien separados, sin saltar."""
    return render([
        atras((192, 200), (150, 248), (134, 294), (160, 296)),
        atras((190, 150), (204, 184), (212, 212)),
        tronco((196, 196), (196, 144)),
        miembro((196, 196), (246, 246), (262, 294), (292, 296)),
        miembro((196, 144), (216, 178), (228, 206)),
        cuello((198, 132), (196, 144)),
        cabeza(204, 108, 195),
        flecha(310, 272, 368, 272),
    ])


def caminata_nariz():
    """R5 - Caminar por la casa respirando por la nariz. Si podes, cambiala por 20
    minutos de caminata afuera: es mejor y es gratis."""
    return render([
        atras((186, 150), (158, 180), (142, 204)),
        atras((186, 200), (152, 248), (132, 292), (156, 294)),
        tronco((190, 196), (192, 144)),
        miembro((190, 196), (232, 242), (250, 292), (278, 294)),
        miembro((192, 144), (222, 176), (240, 200)),
        cuello((194, 132), (192, 144)),
        cabeza(200, 108, 195),
        flecha(272, 146, 328, 146),
    ])


# --- Rutina 6: movilidad y descarga -----------------------------------------

def gato_camello():
    """R6 - Gato-camello en cuatro apoyos, 10 veces lento. La flecha marca la espalda
    que se redondea hacia arriba."""
    return render([
        atras((280, 202), (282, 250), (284, 298)),
        atras((180, 202), (180, 250), (180, 298), (148, 294), (130, 292)),
        tronco((186, 198), (236, 172), (286, 198)),
        miembro((286, 196), (288, 246), (290, 296)),
        miembro((186, 198), (186, 248), (186, 296), (152, 292), (134, 290)),
        cuello((308, 208), (288, 198)),
        cabeza(338, 216, 200),
        flecha(236, 136, 236, 86),
    ])


def rotacion_de_columna():
    """R6 - Rotacion de columna de costado, 8 por lado. El brazo de arriba se abre y
    la flecha curva marca el barrido."""
    return render([
        atras((244, 258), (306, 270), (284, 304)),
        atras((152, 246), (200, 264), (248, 274)),
        tronco((152, 250), (248, 252)),
        miembro((248, 252), (308, 264), (286, 300)),
        miembro((152, 240), (160, 196), (146, 152)),
        cuello((120, 246), (152, 250)),
        cabeza(94, 242, 190),
        flecha_curva(182, 138, 230, 116, 266, 154),
    ])


POSES = {
    # Rutina 1
    "respiracion-360": respiracion_360,
    "exhalacion-con-cierre": exhalacion_con_cierre,
    "hipopresivo-suave": hipopresivo_suave,
    "cierre-de-pie": cierre_de_pie,
    # Rutina 2
    "marcha-costillas-abajo": marcha_costillas_abajo,
    "empuje-contra-la-pared": empuje_contra_la_pared,
    "antigiro-con-toalla": antigiro_con_toalla,
    "sentadilla-a-la-silla": sentadilla_a_la_silla,
    "elevacion-de-talones": elevacion_de_talones,
    "estiramiento-de-flexores": estiramiento_de_flexores,
    # Rutina 3
    "plancha-lateral-rodillas": plancha_lateral_rodillas,
    "bicho-muerto": bicho_muerto,
    "perro-pajaro": perro_pajaro,
    "giro-sentada": giro_sentada,
    "rodillas-al-costado": rodillas_al_costado,
    "estiramiento-de-costado": estiramiento_de_costado,
    # Rutina 4
    "puente-de-gluteo": puente_de_gluteo,
    "puente-a-una-pierna": puente_a_una_pierna,
    "almeja": almeja,
    "patada-atras": patada_atras,
    "plancha-antebrazos": plancha_antebrazos,
    "postura-del-nino": postura_del_nino,
    # Rutina 5
    "marcha-en-el-lugar": marcha_en_el_lugar,
    "paso-lateral": paso_lateral,
    "caminata-nariz": caminata_nariz,
    # Rutina 6
    "gato-camello": gato_camello,
    "rotacion-de-columna": rotacion_de_columna,
}

PENDIENTES = []


def navegador():
    for ruta in (r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                 r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"):
        if os.path.exists(ruta):
            return ruta
    return shutil.which("chrome") or shutil.which("msedge")


def main():
    aqui = os.path.dirname(os.path.abspath(__file__))
    nav = navegador()
    problemas = []
    for nombre, fn in POSES.items():
        _FUERA.clear()
        contenido = fn()
        if _FUERA:
            problemas.append(f"  {nombre}: se sale del marco -> " + "; ".join(_FUERA))
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
    # hoja de contacto: se rehace sola, asi nunca queda vieja
    tarjetas = "\n".join(
        f'    <figure><img src="{n}.svg" alt=""><figcaption>{n.replace("-", " ")}</figcaption></figure>'
        for n in POSES)
    with open(os.path.join(aqui, "muestras.html"), "w", encoding="utf-8") as f:
        f.write(f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Las ilustraciones de los ejercicios</title>
<link rel="stylesheet" href="../estilo.css">
<style>
  body {{ width: 620px; padding: 20pt; }}
  h1 {{ font-size: 18pt; margin-bottom: 3pt; }}
  .nota {{ font-size: 9.5pt; color: var(--gris); margin-bottom: 14pt; line-height: 1.5; }}
  .grilla {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 12pt 10pt; }}
  figure {{ margin: 0; }}
  figure img {{ width: 100%; display: block; border-radius: 6pt; }}
  figcaption {{ font-size: 8pt; color: var(--gris); margin-top: 3pt;
                text-transform: uppercase; letter-spacing: .05em; }}
</style>
</head>
<body>
  <h1>Las {len(POSES)} ilustraciones</h1>
  <p class="nota">Mismo marco, misma linea de piso, mismos grosores, misma silueta sin
  cara. Lo unico que cambia es la pose y hacia donde apunta la flecha.<br>
  Esta hoja la arma solo <em>generar.py</em>: nunca queda vieja.</p>
  <div class="grilla">
{tarjetas}
  </div>
</body>
</html>
""")

    print(f"{len(POSES)} de {len(POSES) + len(PENDIENTES)} ilustraciones. "
          f"Faltan {len(PENDIENTES)}.")
    if problemas:
        print("\nOJO:")
        print("\n".join(problemas))
    else:
        print("Ninguna se sale del marco.")


if __name__ == "__main__":
    main()
