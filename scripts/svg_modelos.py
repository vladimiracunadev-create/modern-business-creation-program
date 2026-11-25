#!/usr/bin/env python3
"""Motor de modelos mentales en SVG para las clases del programa.

Cada clase declara en `manifests/visuales/` un arquetipo (matriz, embudo, ciclo,
balanza, línea de tiempo, árbol de decisión…) y sus datos. Este módulo dibuja
el SVG con la biblioteca estándar: sin dependencias, determinista y con el
mismo resultado en cada ejecución, de modo que `generar_clases.py --check`
pueda comparar el archivo publicado con lo que dicen los manifiestos.

Principios de diseño:
  - Un arquetipo por idea, no un diagrama único con palabras cambiadas.
  - Fondo propio claro: el SVG se ve igual en tema claro y oscuro.
  - Texto real (no trazos), con <title> y <desc>, para lectores de pantalla.
  - El color de acento identifica la etapa del programa.
"""

from __future__ import annotations

import math
import textwrap
from html import escape

ANCHO, ALTO = 760, 440
TINTA, TENUE, LINEA, FONDO = "#1F2937", "#6B7280", "#CBD5E1", "#FBFAF7"
FUENTE = "system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif"

ACENTOS = {
    1: "#2E8B57", 2: "#2563EB", 3: "#7C3AED", 4: "#C2410C", 5: "#0F766E", 6: "#374151",
}


def _mezcla(hex_color: str, factor: float) -> str:
    """Mezcla el color con blanco: factor 0 = blanco, 1 = color puro."""
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
    return "#%02X%02X%02X" % tuple(round(255 + (c - 255) * factor) for c in (r, g, b))


def esc(texto: object) -> str:
    return escape(str(texto), quote=True)


def envolver(texto: str, ancho: int) -> list[str]:
    return textwrap.wrap(str(texto), width=max(ancho, 6), break_long_words=False) or [""]


def texto(x, y, lineas, tam=14, ancla="middle", color=TINTA, peso="400", interlineado=1.28, cursiva=False):
    if isinstance(lineas, str):
        lineas = [lineas]
    estilo = ' font-style="italic"' if cursiva else ""
    partes = [
        f'<text x="{x:.1f}" y="{y:.1f}" font-size="{tam}" text-anchor="{ancla}" fill="{color}" '
        f'font-weight="{peso}"{estilo}>'
    ]
    for i, linea in enumerate(lineas):
        dy = 0 if i == 0 else tam * interlineado
        partes.append(f'<tspan x="{x:.1f}" dy="{dy:.1f}">{esc(linea)}</tspan>')
    partes.append("</text>")
    return "".join(partes)


def texto_centrado_vertical(x, cy, lineas, tam=14, **kw):
    n = len(lineas)
    alto = (n - 1) * tam * kw.get("interlineado", 1.28)
    return texto(x, cy - alto / 2 + tam * 0.35, lineas, tam=tam, **kw)


def caja(x, y, w, h, relleno, borde=None, rx=10, grosor=1.5):
    b = f' stroke="{borde}" stroke-width="{grosor}"' if borde else ""
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{relleno}"{b}/>'


def linea(x1, y1, x2, y2, color=TENUE, grosor=1.6, flecha=False, punteada=False):
    extra = ' marker-end="url(#fl)"' if flecha else ""
    punto = ' stroke-dasharray="5 4"' if punteada else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" '
            f'stroke-width="{grosor}"{punto}{extra}/>')


def marco(numero: int, parte_titulo: str, titulo: str, descripcion: str, acento: str, cuerpo: str) -> str:
    claro, medio = _mezcla(acento, 0.12), _mezcla(acento, 0.35)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ANCHO} {ALTO}" width="{ANCHO}" '
        f'height="{ALTO}" role="img" aria-labelledby="t d" font-family="{FUENTE}">'
        f'<title id="t">{esc(titulo)}</title><desc id="d">{esc(descripcion)}</desc>'
        f'<defs><marker id="fl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
        f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{TENUE}"/></marker>'
        f'<marker id="fa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
        f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{acento}"/></marker></defs>'
        f'<rect width="{ANCHO}" height="{ALTO}" rx="16" fill="{FONDO}" stroke="{LINEA}"/>'
        f'<rect x="0" y="0" width="{ANCHO}" height="8" rx="4" fill="{acento}"/>'
        f'{texto(32, 44, titulo, tam=20, ancla="start", peso="700")}'
        f'{texto(32, 66, f"Clase {numero} · {parte_titulo}", tam=12, ancla="start", color=TENUE)}'
        f'<line x1="32" y1="76" x2="{ANCHO - 32}" y2="76" stroke="{LINEA}"/>'
        f'{cuerpo}'
        f'<circle cx="{ANCHO - 40}" cy="40" r="14" fill="{claro}" stroke="{medio}"/>'
        f'<text x="{ANCHO - 40}" y="45" font-size="13" text-anchor="middle" fill="{acento}" '
        f'font-weight="700">{numero}</text>'
        f'</svg>\n'
    )


# --------------------------------------------------------------------------- arquetipos
# Todos reciben (datos, acento) y devuelven los elementos que van bajo la cabecera.

def matriz(d, ac):
    x0, y0, w, h = 150, 96, 520, 290
    cw, ch = w / 2, h / 2
    colores = [_mezcla(ac, 0.22), _mezcla(ac, 0.10), "#EEF0F3", _mezcla("#F59E0B", 0.18)]
    pos = [(0, 0), (1, 0), (0, 1), (1, 1)]
    salida = []
    for (cx, cy), (nombre, consejo), color in zip(pos, d["cuadrantes"], colores):
        salida.append(caja(x0 + cx * cw, y0 + cy * ch, cw, ch, color, "#FFFFFF", rx=6, grosor=3))
        nl = envolver(nombre, 27)
        salida.append(texto(x0 + cx * cw + 14, y0 + cy * ch + 28, nl, tam=15, ancla="start", peso="700"))
        salida.append(texto(x0 + cx * cw + 14, y0 + cy * ch + 28 + 18 * len(nl) + 6, envolver(consejo, 34), tam=12, ancla="start", color=TENUE))
    salida.append(linea(x0 - 10, y0 + h + 10, x0 + w + 6, y0 + h + 10, TINTA, 1.8, True))
    salida.append(linea(x0 - 10, y0 + h + 10, x0 - 10, y0 - 4, TINTA, 1.8, True))
    salida.append(texto(x0 + w / 2, y0 + h + 34, d["x"], tam=13, peso="600"))
    salida.append(f'<g transform="translate(88 {y0 + h / 2}) rotate(-90)">{texto(0, 0, d["y"], tam=13, peso="600")}</g>')
    salida.append(texto(x0, y0 + h + 34, "bajo", tam=11, ancla="start", color=TENUE))
    salida.append(texto(x0 + w, y0 + h + 34, "alto", tam=11, ancla="end", color=TENUE))
    if d.get("punto"):
        px, py, et = d["punto"][:3]
        izq = len(d["punto"]) > 3
        cx, cy = x0 + px * w, y0 + (1 - py) * h
        salida.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="9" fill="{ac}" stroke="#FFFFFF" stroke-width="3"/>')
        if izq:
            salida.append(texto(cx - 16, cy - 12, et, tam=13, ancla="end", peso="700", color=ac))
        else:
            salida.append(texto(cx + 16, cy + 5, et, tam=13, ancla="start", peso="700", color=ac))
    return "".join(salida)


def embudo(d, ac):
    etapas = d["etapas"]
    n = len(etapas)
    top, alto_barra, sep = 100, min(52, 290 / n - 8), 8
    salida = []
    for i, (nombre, valor, frac) in enumerate(etapas):
        ancho = 170 + 350 * frac
        x = 300 - ancho / 2
        y = top + i * (alto_barra + sep)
        salida.append(caja(x, y, ancho, alto_barra, _mezcla(ac, 0.25 + 0.6 * (i / max(n - 1, 1))), None, rx=8))
        nl = envolver(nombre, max(int((ancho - 16) / 7.6), 8))
        salida.append(texto_centrado_vertical(x + ancho / 2, y + alto_barra / 2 + 1, nl, tam=13 if len(nl) > 1 else 14, peso="700", color="#FFFFFF" if i > n / 2 else TINTA))
        salida.append(texto(596, y + alto_barra / 2 + 5, valor, tam=14, ancla="start", peso="700", color=ac))
        if i:
            previa = etapas[i - 1][2]
            pasa = round(frac / previa * 100) if previa else 0
            salida.append(texto(668, y + alto_barra / 2 + 5, f"pasa {pasa} %", tam=12, ancla="start", color=TENUE))
    if d.get("cuello") is not None:
        i = d["cuello"]
        y = top + i * (alto_barra + sep)
        salida.append(f'<rect x="30" y="{y - 4}" width="720" height="{alto_barra + 8}" rx="12" fill="none" stroke="#DC2626" stroke-width="2.4" stroke-dasharray="6 4"/>')
        salida.append(texto(742, y - 8, "cuello", tam=11, ancla="end", peso="700", color="#DC2626"))
    return "".join(salida)


def ciclo(d, ac):
    pasos = d["pasos"]
    n = len(pasos)
    cx, cy, r = 380, 252, 128
    salida = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{_mezcla(ac, .35)}" stroke-width="3" stroke-dasharray="3 7"/>']
    centros = []
    for i in range(n):
        ang = -math.pi / 2 + 2 * math.pi * i / n
        centros.append((cx + r * 1.45 * math.cos(ang), cy + r * math.sin(ang)))
    for i, (x, y) in enumerate(centros):
        sx, sy = centros[(i + 1) % n]
        mx, my = (x + sx) / 2, (y + sy) / 2
        vx, vy = mx - cx, my - cy
        norma = math.hypot(vx, vy) or 1
        qx, qy = mx + vx / norma * 24, my + vy / norma * 24
        salida.append(f'<path d="M{x:.1f},{y:.1f} Q{qx:.1f},{qy:.1f} {sx:.1f},{sy:.1f}" fill="none" stroke="{ac}" stroke-width="2.2" marker-end="url(#fa)" opacity=".75"/>')
    for i, ((x, y), paso) in enumerate(zip(centros, pasos)):
        lineas = envolver(paso, 17)
        ancho = max(len(l) for l in lineas) * 7.6 + 28
        alto = len(lineas) * 17 + 18
        salida.append(caja(x - ancho / 2, y - alto / 2, ancho, alto, "#FFFFFF", ac, rx=12, grosor=2))
        salida.append(texto_centrado_vertical(x, y, lineas, tam=13, peso="600"))
        salida.append(f'<circle cx="{x - ancho / 2 + 2}" cy="{y - alto / 2 + 2}" r="10" fill="{ac}"/>')
        salida.append(f'<text x="{x - ancho / 2 + 2}" y="{y - alto / 2 + 6}" font-size="11" text-anchor="middle" fill="#FFF" font-weight="700">{i + 1}</text>')
    salida.append(texto_centrado_vertical(cx, cy, envolver(d.get("centro", ""), 16), tam=14, peso="700", color=ac))
    return "".join(salida)


def escalera(d, ac):
    niveles = d["niveles"]
    n = len(niveles)
    ancho = (ANCHO - 90) / n
    salida = []
    for i, (nombre, detalle) in enumerate(niveles):
        alto = 120 + i * (170 / max(n - 1, 1))
        x, y = 40 + i * ancho, 400 - alto
        salida.append(caja(x, y, ancho - 8, alto, _mezcla(ac, 0.10 + 0.5 * i / max(n - 1, 1)), None, rx=10))
        salida.append(texto(x + 14, y + 28, f"{i + 1}", tam=22, ancla="start", peso="800", color=ac))
        salida.append(texto(x + 14, y + 52, envolver(nombre, int(ancho / 8.6)), tam=14, ancla="start", peso="700"))
        salida.append(texto(x + 14, y + 52 + 18 * len(envolver(nombre, int(ancho / 8.6))) + 6, envolver(detalle, int(ancho / 7.4)), tam=12, ancla="start", color=TENUE))
    salida.append(linea(48, 412, ANCHO - 40, 412, ac, 2.4, True))
    salida.append(texto(ANCHO - 44, 430, d.get("eje", "madurez"), tam=11, ancla="end", color=TENUE))
    return "".join(salida)


def balanza(d, ac):
    (tz, iz), (td, idd) = d["izq"], d["der"]
    salida = []
    for x, titulo, items, color in ((40, tz, iz, "#F59E0B"), (404, td, idd, ac)):
        salida.append(caja(x, 96, 316, 214, _mezcla(color, 0.12), color, rx=14, grosor=2))
        salida.append(texto(x + 20, 134, envolver(titulo, 34), tam=16, ancla="start", peso="700", color=color if color != "#F59E0B" else "#B45309"))
        y = 168
        for it in items:
            ls = envolver(it, 40)
            salida.append(f'<circle cx="{x + 24}" cy="{y - 4}" r="3.4" fill="{color}"/>')
            salida.append(texto(x + 38, y, ls, tam=13, ancla="start"))
            y += 18 * len(ls) + 10
    salida.append(f'<circle cx="380" cy="203" r="22" fill="{TINTA}"/>')
    salida.append(texto(380, 208, "vs", tam=15, peso="800", color="#FFFFFF"))
    salida.append(caja(40, 326, 680, 90, "#FFFFFF", TINTA, rx=12, grosor=1.6))
    salida.append(texto(60, 350, "Criterio de decisión", tam=11, ancla="start", color=TENUE, peso="700"))
    salida.append(texto(60, 376, envolver(d["criterio"], 84)[:2], tam=15, ancla="start", peso="700"))
    return "".join(salida)


def tiempo(d, ac):
    hitos = d["hitos"]
    n = len(hitos)
    y0 = 244
    salida = [linea(50, y0, ANCHO - 50, y0, ac, 4)]
    paso = (ANCHO - 220) / max(n - 1, 1)
    for i, (cuando, que) in enumerate(hitos):
        x = 110 + i * paso
        arriba = i % 2 == 0
        resaltado = d.get("hito") == i
        salida.append(f'<circle cx="{x:.1f}" cy="{y0}" r="{13 if resaltado else 9}" fill="{ac if resaltado else "#FFFFFF"}" stroke="{ac}" stroke-width="3"/>')
        ls = envolver(que, max(int(min(paso, 170) / 7.2), 14))
        if arriba:
            salida.append(linea(x, y0 - 14, x, y0 - 46, LINEA, 1.5))
            salida.append(texto(x, y0 - 58 - 16 * (len(ls) - 1) - 18, cuando, tam=15, peso="800", color=ac))
            salida.append(texto(x, y0 - 58 - 16 * (len(ls) - 1), ls, tam=12.5))
        else:
            salida.append(linea(x, y0 + 14, x, y0 + 46, LINEA, 1.5))
            salida.append(texto(x, y0 + 68, cuando, tam=15, peso="800", color=ac))
            salida.append(texto(x, y0 + 88, ls, tam=12.5))
    if d.get("bajada"):
        salida.append(texto(ANCHO / 2, 420, d["bajada"], tam=12, color=TENUE, cursiva=True))
    return "".join(salida)


def capas(d, ac):
    capas_ = d["capas"]
    n = len(capas_)
    alto = min(64, 290 / n - 6)
    salida = []
    for i, (nombre, detalle) in enumerate(capas_):
        y = 100 + i * (alto + 6)
        ancho = 300 + i * (200 / max(n - 1, 1))
        x = 290 - ancho / 2
        fuerte = i / max(n - 1, 1) > 0.5
        salida.append(caja(x, y, ancho, alto, _mezcla(ac, 0.18 + 0.62 * i / max(n - 1, 1)), None, rx=10))
        salida.append(texto(290, y + alto / 2 + 5, nombre, tam=15, peso="800", color="#FFFFFF" if fuerte else TINTA))
        ls = envolver(detalle, 26)
        salida.append(texto(560, y + alto / 2 - (len(ls) - 1) * 7 + 4, ls, tam=12.5, ancla="start"))
        salida.append(linea(x + ancho + 6, y + alto / 2, 552, y + alto / 2, LINEA, 1.2, False, True))
    return "".join(salida)


def _hoja(x, y, texto_, ac, ancho=150):
    ls = envolver(texto_, int(ancho / 7.4))
    alto = len(ls) * 16 + 20
    return (caja(x - ancho / 2, y, ancho, alto, _mezcla(ac, 0.16), ac, rx=10, grosor=1.6)
            + texto_centrado_vertical(x, y + alto / 2, ls, tam=12.5, peso="600"), alto)


def arbol(d, ac):
    salida = []
    pregunta = d["q"]

    def hojas(nodo):
        return 1 if isinstance(nodo, str) else hojas(nodo["si"]) + hojas(nodo["no"])

    total = hojas(d)
    ancho_hoja = (ANCHO - 70) / total
    contador = [0]

    def colocar(nodo, nivel):
        """Devuelve x del nodo y dibuja su subárbol."""
        y = 112 + nivel * 112
        if isinstance(nodo, str):
            x = 35 + ancho_hoja * (contador[0] + 0.5)
            contador[0] += 1
            html, _ = _hoja(x, y, nodo, ac, min(ancho_hoja - 12, 190))
            salida.append(html)
            return x, y
        xs, ys = colocar(nodo["si"], nivel + 1)
        xn, yn = colocar(nodo["no"], nivel + 1)
        x = (xs + xn) / 2
        ls = envolver(nodo["q"], 26)
        ancho = max(len(l) for l in ls) * 7.4 + 30
        alto = len(ls) * 16 + 18
        for destino, etiqueta, color in ((xs, "sí", "#16A34A"), (xn, "no", "#DC2626")):
            salida.append(linea(x, y + alto, destino, y + 112 - 2, color, 1.8, True))
            salida.append(texto((x + destino) / 2 + (-12 if etiqueta == "sí" else 12), (y + alto + y + 112) / 2 - 2, etiqueta, tam=12.5, peso="800", color=color))
        salida.append(f'<path d="M{x - ancho / 2 + 14},{y} h{ancho - 28} a14,14 0 0 1 14,14 v{alto - 28} a14,14 0 0 1 -14,14 h-{ancho - 28} a14,14 0 0 1 -14,-14 v-{alto - 28} a14,14 0 0 1 14,-14z" fill="#FFFFFF" stroke="{ac}" stroke-width="2.2"/>')
        salida.append(texto_centrado_vertical(x, y + alto / 2, ls, tam=13, peso="700"))
        return x, y

    colocar(d, 0)
    return "".join(salida)


def actores(d, ac):
    lista = d["actores"]
    n = len(lista)
    cx, cy = 380, 262
    salida = []
    puntos = []
    for i in range(n):
        ang = -math.pi / 2 + 2 * math.pi * i / n
        puntos.append((cx + 255 * math.cos(ang), cy + 132 * math.sin(ang)))
    for (x, y), (_, _) in zip(puntos, lista):
        salida.append(linea(cx, cy, x, y, _mezcla(ac, 0.45), 2))
    centro = envolver(d["centro"], 14)
    salida.append(f'<ellipse cx="{cx}" cy="{cy}" rx="78" ry="46" fill="{ac}"/>')
    salida.append(texto_centrado_vertical(cx, cy, centro, tam=14, peso="800", color="#FFFFFF"))
    for (x, y), (nombre, relacion) in zip(puntos, lista):
        rl = envolver(relacion, 24)
        ancho = 176
        alto = 26 + len(rl) * 14
        salida.append(caja(x - ancho / 2, y - alto / 2, ancho, alto, "#FFFFFF", ac, rx=12, grosor=1.8))
        salida.append(texto(x, y - alto / 2 + 19, nombre, tam=13.5, peso="800", color=ac))
        salida.append(texto(x, y - alto / 2 + 35, rl, tam=11.5, color=TENUE))
    return "".join(salida)


def _ejes(x0, y0, w, h, etiqueta_x, etiqueta_y, ac):
    return [
        linea(x0, y0 + h, x0 + w + 8, y0 + h, TINTA, 1.8, True),
        linea(x0, y0 + h, x0, y0 - 8, TINTA, 1.8, True),
        texto(x0 + w / 2, y0 + h + 32, etiqueta_x, tam=13, peso="600"),
        f'<g transform="translate({x0 - 30} {y0 + h / 2}) rotate(-90)">{texto(0, 0, etiqueta_y, tam=13, peso="600")}</g>',
    ]


def curva(d, ac):
    x0, y0, w, h = 96, 100, 560, 262
    tipo = d["tipo"]
    salida = _ejes(x0, y0, w, h, d["x"], d["y"], ac)

    def trazar(f, color, grosor=3.4, puntos=60, punteada=False):
        pts = [(x0 + w * i / puntos, y0 + h - h * f(i / puntos)) for i in range(puntos + 1)]
        trazo = "M" + " L".join(f"{px:.1f},{py:.1f}" for px, py in pts)
        extra = ' stroke-dasharray="7 5"' if punteada else ""
        return f'<path d="{trazo}" fill="none" stroke="{color}" stroke-width="{grosor}" stroke-linecap="round"{extra}/>'

    def marcar(t, f, etiqueta, dx=16, dy=-14, color=None):
        color = color or ac
        px, py = x0 + w * t, y0 + h - h * f(t)
        salida.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="8" fill="{color}" stroke="#FFFFFF" stroke-width="3"/>')
        salida.append(texto(px + dx, py + dy, envolver(etiqueta, 24), tam=13, ancla="start" if dx > 0 else "end", peso="700", color=color))

    if tipo == "saturacion":
        f = lambda t: 1 - math.exp(-3.4 * t)
        salida.append(trazar(f, ac))
        marcar(0.62, f, d["punto"], dx=14, dy=34)
        salida.append(f'<rect x="{x0 + w * .62:.1f}" y="{y0}" width="{w * .38:.1f}" height="{h}" fill="#F59E0B" opacity=".10"/>')
        salida.append(texto(x0 + w * .81, y0 + 24, envolver(d.get("zona", ""), 20), tam=12, peso="700", color="#B45309"))
    elif tipo == "convexa":
        f = lambda t: 0.08 + 0.9 * t ** 2.4
        salida.append(trazar(f, ac))
        marcar(0.66, f, d["punto"], dx=-14, dy=-34)
        salida.append(f'<rect x="{x0 + w * .66:.1f}" y="{y0}" width="{w * .34:.1f}" height="{h}" fill="#DC2626" opacity=".08"/>')
        salida.append(texto(x0 + w * .83, y0 + 24, envolver(d.get("zona", ""), 18), tam=12, peso="700", color="#B91C1C"))
    elif tipo == "equilibrio":
        ingreso = lambda t: 0.98 * t
        costo = lambda t: 0.28 + 0.38 * t
        salida.append(trazar(costo, "#6B7280", punteada=True))
        salida.append(trazar(ingreso, ac))
        t = 0.28 / (0.98 - 0.38)
        marcar(t, ingreso, d["punto"], dx=16, dy=30)
        salida.append(texto(x0 + w * .86, y0 + h - h * ingreso(.86) - 12, d.get("serie1", "Ingresos"), tam=12.5, peso="700", color=ac))
        salida.append(texto(x0 + w * .86, y0 + h - h * costo(.86) + 24, d.get("serie2", "Costos"), tam=12.5, peso="700", color=TENUE))
        salida.append(texto(x0 + w * .12, y0 + h - 18, d.get("zona", "pérdida"), tam=12, peso="700", color="#B91C1C"))
        salida.append(texto(x0 + w * .86, y0 + 28, "ganancia", tam=12, peso="700", color="#15803D"))
    elif tipo == "acumulacion":
        activo = lambda t: min(0.06 + 0.92 * t ** 1.5, 0.98)
        campana = lambda t: 0.06 + 0.5 * math.exp(-(((t - 0.12) / 0.09) ** 2)) + 0.03 * math.exp(-t * 2)
        salida.append(trazar(campana, "#F59E0B", punteada=True))
        salida.append(trazar(activo, ac))
        salida.append(texto(x0 + w * .88, y0 + h - h * activo(.88) - 14, d.get("serie1", "Activo"), tam=12.5, peso="700", color=ac, ancla="end"))
        salida.append(texto(x0 + w * .2, y0 + h - h * .45, d.get("serie2", "Campaña"), tam=12.5, peso="700", color="#B45309", ancla="start"))
        marcar(0.58, activo, d["punto"], dx=16, dy=36)
    elif tipo == "s":
        f = lambda t: 1 / (1 + math.exp(-10 * (t - 0.5)))
        salida.append(trazar(f, ac))
        marcar(0.5, f, d["punto"], dx=16, dy=24)
    elif tipo == "u":
        f = lambda t: 0.18 + 1.9 * (t - 0.5) ** 2
        salida.append(trazar(f, ac))
        marcar(0.5, f, d["punto"], dx=0, dy=-24)
    elif tipo == "pico":
        f = lambda t: max(0.1, 0.96 - 3.2 * (t - 0.46) ** 2)
        salida.append(trazar(f, ac))
        marcar(0.46, f, d["punto"], dx=0, dy=-24)
        salida.append(texto(x0 + w * .08, y0 + h - 14, d.get("zona", ""), tam=12, ancla="start", color=TENUE))
    elif tipo == "decaimiento":
        f = lambda t: 0.05 + 0.9 * math.exp(-3.2 * t)
        salida.append(trazar(f, ac))
        marcar(0.2, f, d["punto"], dx=16, dy=-14)
    return "".join(salida)


def semaforo(d, ac):
    colores = {"verde": "#16A34A", "amarillo": "#F59E0B", "rojo": "#DC2626"}
    fondo = {"verde": "#ECFDF3", "amarillo": "#FEF6E3", "rojo": "#FDECEC"}
    salida = [texto(40, 104, d.get("indicador", ""), tam=13, ancla="start", color=TENUE, peso="700")]
    y = 118
    for color, rango, accion in d["bandas"]:
        salida.append(caja(40, y, 680, 82, fondo[color], colores[color], rx=14, grosor=2))
        salida.append(f'<circle cx="86" cy="{y + 41}" r="22" fill="{colores[color]}"/>')
        lr = envolver(rango, 24)
        salida.append(texto(130, y + 32 - (len(lr) - 1) * 9, lr, tam=15.5, ancla="start", peso="800"))
        salida.append(texto(130, y + 62, color.upper(), tam=11, ancla="start", color=colores[color], peso="800"))
        la = envolver(accion, 40)
        salida.append(texto(430, y + 38 - (len(la) - 1) * 8, la, tam=13.5, ancla="start"))
        y += 94
    return "".join(salida)


def barras(d, ac):
    serie = d["serie"]
    n = len(serie)
    x0, y0, w, h = 90, 106, 600, 244
    maximo = max(abs(v) for _, v in serie) or 1
    ancho = w / n
    salida = [linea(x0, y0 + h, x0 + w, y0 + h, TINTA, 1.8)]
    for i, (nombre, valor) in enumerate(serie):
        alto = h * 0.82 * abs(valor) / maximo
        x = x0 + i * ancho + ancho * 0.18
        y = y0 + h - alto
        destacado = d.get("destacar") == i
        color = ac if destacado else _mezcla(ac, 0.35)
        salida.append(caja(x, y, ancho * 0.64, alto, color, None, rx=8))
        salida.append(texto(x + ancho * 0.32, y - 10, f"{valor:g}{d.get('unidad', '')}", tam=14, peso="800", color=ac if destacado else TENUE))
        salida.append(texto(x + ancho * 0.32, y0 + h + 24, envolver(nombre, int(ancho / 7.4)), tam=12.5))
    if d.get("nota"):
        salida.append(caja(40, 384, 680, 46, "#FFFFFF", LINEA, rx=10, grosor=1.2))
        salida.append(texto(56, 404, envolver(d["nota"], 104)[:2], tam=12.5, ancla="start", color=TENUE))
    salida.append(texto(x0 - 8, y0 - 6, d.get("eje", ""), tam=12, ancla="start", color=TENUE, peso="700"))
    return "".join(salida)


def flujo(d, ac):
    pasos = d["pasos"]
    n = len(pasos)
    gate = d.get("compuerta")
    hueco = 44
    ancho = (ANCHO - 70 - hueco * (n - 1)) / n
    y, alto = 160, 118
    salida = []
    xs = []
    for i, paso in enumerate(pasos):
        x = 35 + i * (ancho + hueco)
        xs.append(x)
        ls = envolver(paso, max(int(ancho / 7.0), 8))
        salida.append(caja(x, y, ancho, alto, "#FFFFFF", ac, rx=12, grosor=2))
        salida.append(f'<circle cx="{x + 16}" cy="{y}" r="12" fill="{ac}"/>')
        salida.append(f'<text x="{x + 16}" y="{y + 4.5}" font-size="12" text-anchor="middle" fill="#FFF" font-weight="800">{i + 1}</text>')
        salida.append(texto_centrado_vertical(x + ancho / 2, y + alto / 2 + 4, ls, tam=12.5, peso="600"))
        if i:
            salida.append(linea(x - hueco + 4, y + alto / 2, x - 3, y + alto / 2, ac, 2.2, True))
    if gate:
        gx = xs[gate["despues"]] + ancho + hueco / 2
        gy = y + alto / 2
        salida.append(f'<path d="M{gx},{gy - 16} l12,16 l-12,16 l-12,-16z" fill="#FEF6E3" stroke="#F59E0B" stroke-width="2"/>')
        salida.append(texto(gx, y - 18, gate["pregunta"], tam=12.5, peso="800", color="#B45309"))
    if d.get("retorno"):
        salida.append(f'<path d="M{xs[-1] + ancho / 2},{y + alto} v34 H{xs[0] + ancho / 2} v-34" fill="none" stroke="{TENUE}" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#fl)"/>')
        salida.append(texto(ANCHO / 2, y + alto + 62, d["retorno"], tam=12.5, color=TENUE, cursiva=True))
    return "".join(salida)


def venn(d, ac):
    nombres = d["circulos"]
    cx, cy, r = 380, 232, 92
    pos = [(cx - 52, cy - 34), (cx + 52, cy - 34), (cx, cy + 44)]
    colores = [ac, "#F59E0B", "#0EA5E9"]
    salida = []
    for (x, y), c in zip(pos, colores):
        salida.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" fill-opacity=".22" stroke="{c}" stroke-width="2.4"/>')
    etiquetas = [(cx - 158, cy - 104, "end"), (cx + 158, cy - 104, "start"), (cx, cy + 162, "middle")]
    for (x, y, a), nombre, c in zip(etiquetas, nombres, colores):
        salida.append(texto(x, y, envolver(nombre, 18), tam=15, ancla=a, peso="800", color=c if c != "#F59E0B" else "#B45309"))
    salida.append(texto_centrado_vertical(cx, cy - 8, envolver(d["centro"], 10), tam=12.5, peso="800"))
    if d.get("nota"):
        salida.append(texto(ANCHO - 36, 410, envolver(d["nota"], 40), tam=11.5, ancla="end", color=TENUE))
    return "".join(salida)


ARQUETIPOS = {
    "matriz": matriz, "embudo": embudo, "ciclo": ciclo, "escalera": escalera, "balanza": balanza,
    "tiempo": tiempo, "capas": capas, "arbol": arbol, "actores": actores, "curva": curva,
    "semaforo": semaforo, "barras": barras, "flujo": flujo, "venn": venn,
}


def dibujar(numero: int, parte_titulo: str, etapa: int, visual: dict) -> str:
    """Renderiza el SVG de una clase a partir de su especificación."""
    arquetipo = ARQUETIPOS[visual["tipo"]]
    acento = ACENTOS[etapa]
    cuerpo = arquetipo(visual["datos"], acento)
    return marco(numero, parte_titulo, visual["titulo"], visual["alt"], acento, cuerpo)
