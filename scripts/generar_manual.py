#!/usr/bin/env python3
"""Compila el manual del programa en PDF a partir del Markdown canónico.

Produce el manual integral con las 336 clases y, opcionalmente, un PDF por parte.
Usa reportlab: no depende de un navegador ni de binarios externos, así que corre
igual en Windows y en el runner de CI.

Los diagramas mermaid no se rasterizan —eso exigiría Node y un navegador— sino que
se transcriben como esquema de texto legible, indicando dónde verlos renderizados.

Uso:
  python scripts/generar_manual.py                 # manual integral
  python scripts/generar_manual.py --partes        # además, un PDF por parte
  python scripts/generar_manual.py --check         # valida sin escribir
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

RAIZ = Path(__file__).resolve().parents[1]
# El PDF se emite en output/ y no en site/: el generador del sitio borra site/
# completo en cada build y se llevaría el manual por delante.
SALIDA = RAIZ / "output" / "pdf"
MANIFIESTO = SALIDA / "manual-manifest.json"

TITULO = "Modern Business Creation Program"
SUBTITULO = "Crear y operar una empresa real en Chile"

AZUL = colors.HexColor("#0b62d0")
GRIS = colors.HexColor("#5a6572")
BORDE = colors.HexColor("#dfe4ea")
FONDO = colors.HexColor("#f5f7fa")

# Los emoji de los encabezados no existen en las fuentes base de reportlab y se
# imprimirían como cuadros negros; se retiran solo para el PDF.
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿️←-⇿⬀-⯿]")
ENLACE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
NEGRITA = re.compile(r"\*\*([^*]+)\*\*")
CURSIVA = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")
CODIGO = re.compile(r"`([^`]+)`")
HTML_BR = re.compile(r"<br\s*/?>")


NODO = re.compile(r'^([A-Za-z0-9_]+)\s*[\[\{\(]{1,2}"?(.*?)"?[\]\}\)]{1,2}\s*$')
ARISTA = re.compile(
    r'^(.+?)\s*-[-.]?->\s*(?:\|\s*"?(.*?)"?\s*\|)?\s*(.+?)$'
)


def mermaid_a_texto(fuente: str) -> list[str]:
    """Traduce un diagrama mermaid a un esquema de texto legible.

    Volcar la sintaxis mermaid en el PDF produce ruido —`<br/>`, corchetes, ids—
    y se desborda del margen. Aquí se resuelven los identificadores a sus
    etiquetas y cada arista se imprime como `origen → destino`.
    """
    etiquetas: dict[str, str] = {}
    aristas: list[tuple[str, str, str]] = []
    grupos: list[str] = []

    def texto_nodo(bruto: str) -> str:
        bruto = bruto.strip()
        coincidencia = NODO.match(bruto)
        if coincidencia:
            identificador, etiqueta_nodo = coincidencia.groups()
            etiqueta_limpia = HTML_BR.sub(" · ", etiqueta_nodo).strip()
            etiquetas[identificador] = etiqueta_limpia
            return etiqueta_limpia
        return " + ".join(
            etiquetas.get(parte.strip(), parte.strip())
            for parte in bruto.split("&")
        )

    for linea in fuente.split("\n"):
        despojada = linea.strip()
        if not despojada or despojada.startswith(("flowchart", "graph", "end", "%%")):
            continue
        if despojada.startswith("subgraph"):
            nombre = re.sub(r'^subgraph\s+\w*\s*\[?"?|"?\]?$', "", despojada).strip()
            if nombre:
                grupos.append(nombre)
            continue
        arista = ARISTA.match(despojada)
        if arista:
            origen, condicion, destino = arista.groups()
            aristas.append((texto_nodo(origen), condicion or "", texto_nodo(destino)))
            continue
        texto_nodo(despojada)

    lineas = [f"Bloques: {' · '.join(grupos)}"] if grupos else []
    for origen, condicion, destino in aristas:
        flecha = f" --[{condicion}]-> " if condicion else " -> "
        lineas.append(f"{origen}{flecha}{destino}")
    return lineas or ["(diagrama sin aristas)"]


def limpiar(texto: str) -> str:
    """Convierte Markdown en línea al subconjunto de marcado que acepta reportlab."""
    texto = EMOJI.sub("", texto)
    texto = ENLACE.sub(r"\1", texto)
    texto = texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # El salto se restituye después del escape: si se convirtiera antes, la
    # propia etiqueta <br/> quedaría escapada y se imprimiría como texto.
    texto = re.sub(r"&lt;br\s*/?&gt;", "<br/>", texto)
    texto = NEGRITA.sub(r"<b>\1</b>", texto)
    texto = CURSIVA.sub(r"<i>\1</i>", texto)
    texto = CODIGO.sub(r'<font face="Courier" size="8.5">\1</font>', texto)
    return texto.strip()


def estilos() -> dict:
    base = getSampleStyleSheet()
    return {
        "portada_titulo": ParagraphStyle(
            "PortadaTitulo", parent=base["Title"], fontSize=28, leading=34,
            textColor=AZUL, alignment=TA_CENTER, spaceAfter=6),
        "portada_sub": ParagraphStyle(
            "PortadaSub", parent=base["Normal"], fontSize=13, leading=18,
            textColor=GRIS, alignment=TA_CENTER, spaceAfter=24),
        "h1": ParagraphStyle(
            "H1", parent=base["Heading1"], fontSize=18, leading=22, textColor=AZUL,
            spaceBefore=10, spaceAfter=8),
        "h2": ParagraphStyle(
            "H2", parent=base["Heading2"], fontSize=12.5, leading=16,
            textColor=colors.HexColor("#12181f"), spaceBefore=10, spaceAfter=4),
        "h3": ParagraphStyle(
            "H3", parent=base["Heading3"], fontSize=10.5, leading=14,
            textColor=GRIS, spaceBefore=8, spaceAfter=3),
        "cuerpo": ParagraphStyle(
            "Cuerpo", parent=base["BodyText"], fontSize=9.3, leading=13.4,
            alignment=TA_JUSTIFY, spaceAfter=5),
        "meta": ParagraphStyle(
            "Meta", parent=base["BodyText"], fontSize=8.2, leading=11,
            textColor=GRIS, spaceAfter=6),
        "lista": ParagraphStyle(
            "Lista", parent=base["BodyText"], fontSize=9.3, leading=13,
            leftIndent=10, bulletIndent=2, spaceAfter=2),
        "cita": ParagraphStyle(
            "Cita", parent=base["BodyText"], fontSize=8.8, leading=12.4,
            leftIndent=10, textColor=GRIS, spaceAfter=6,
            borderPadding=(4, 4, 4, 6), backColor=FONDO),
        "codigo": ParagraphStyle(
            "Codigo", parent=base["Code"], fontSize=7.4, leading=9.4,
            textColor=GRIS, leftIndent=8),
        "diagrama": ParagraphStyle(
            "Diagrama", parent=base["BodyText"], fontSize=8.2, leading=11.5,
            leftIndent=10, spaceAfter=1.5, textColor=colors.HexColor("#12181f"),
            backColor=FONDO, borderPadding=(2, 4, 2, 6)),
        "titulo_indice": ParagraphStyle(
            "TituloIndice", parent=base["Heading1"], fontSize=18, leading=22,
            textColor=AZUL, spaceBefore=10, spaceAfter=8),
        "toc1": ParagraphStyle("Toc1", parent=base["Normal"], fontSize=9,
                               leading=12.5, spaceBefore=1, textColor=AZUL),
        "toc2": ParagraphStyle("Toc2", parent=base["Normal"], fontSize=8.6,
                               leading=11.6, leftIndent=14, textColor=GRIS),
    }


class Documento(BaseDocTemplate):
    """Plantilla con numeración, encabezado corrido y marcadores para el índice."""

    def __init__(self, ruta: Path, titulo: str, **kwargs):
        super().__init__(str(ruta), pagesize=A4, title=titulo, author="Vladimir Acuña",
                         subject=SUBTITULO, **kwargs)
        marco = Frame(20 * mm, 18 * mm, A4[0] - 40 * mm, A4[1] - 38 * mm, id="cuerpo")
        self.addPageTemplates([
            PageTemplate(id="portada", frames=[marco]),
            PageTemplate(id="normal", frames=[marco], onPage=self._decorar),
        ])
        self.titulo_corrido = titulo

    def _decorar(self, canvas, doc) -> None:
        canvas.saveState()
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(GRIS)
        canvas.drawString(20 * mm, A4[1] - 13 * mm, self.titulo_corrido)
        canvas.drawRightString(A4[0] - 20 * mm, A4[1] - 13 * mm, "Fecha base normativa: 07-08-2026")
        canvas.setStrokeColor(BORDE)
        canvas.line(20 * mm, A4[1] - 15 * mm, A4[0] - 20 * mm, A4[1] - 15 * mm)
        canvas.line(20 * mm, 15 * mm, A4[0] - 20 * mm, 15 * mm)
        canvas.drawCentredString(A4[0] / 2, 10 * mm, str(doc.page))
        canvas.restoreState()

    def afterFlowable(self, flowable) -> None:
        # Solo entran al índice los títulos de parte y de clase. Indexar también
        # las secciones internas produciría más de 4.000 entradas y un índice de
        # 120 páginas para un manual de 350 páginas de contenido por parte.
        if isinstance(flowable, Paragraph) and flowable.style.name == "H1":
            self.notify("TOCEntry", (0, flowable.getPlainText(), self.page))


def tabla(filas: list[list[str]], est: dict) -> Table:
    datos = [[Paragraph(limpiar(celda), est["meta"]) for celda in fila] for fila in filas]
    ancho = A4[0] - 40 * mm
    columnas = len(filas[0])
    tabla_pdf = Table(datos, colWidths=[ancho / columnas] * columnas, repeatRows=1)
    tabla_pdf.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, BORDE),
        ("BACKGROUND", (0, 0), (-1, 0), FONDO),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return tabla_pdf


def convertir(markdown: str, est: dict, nivel_titulo: str = "h1") -> list:
    """Traduce un README a flowables de reportlab."""
    flujo: list = []
    lineas = markdown.split("\n")
    indice = 0
    buffer_tabla: list[list[str]] = []

    def volcar_tabla() -> None:
        nonlocal buffer_tabla
        if buffer_tabla:
            flujo.append(Spacer(1, 3))
            flujo.append(tabla(buffer_tabla, est))
            flujo.append(Spacer(1, 5))
            buffer_tabla = []

    while indice < len(lineas):
        linea = lineas[indice].rstrip()
        despojada = linea.strip()

        if despojada.startswith("```"):
            volcar_tabla()
            lenguaje = despojada[3:].strip().lower()
            cuerpo: list[str] = []
            indice += 1
            while indice < len(lineas) and not lineas[indice].strip().startswith("```"):
                cuerpo.append(lineas[indice])
                indice += 1
            indice += 1
            if lenguaje == "mermaid":
                flujo.append(Paragraph(
                    "<b>Diagrama</b> — esquema de razonamiento. La versión renderizada está en "
                    "el repositorio y en el sitio del programa.", est["meta"]))
                for paso in mermaid_a_texto(EMOJI.sub("", "\n".join(cuerpo))):
                    flujo.append(Paragraph(limpiar(paso), est["diagrama"]))
            else:
                flujo.append(Preformatted("\n".join(cuerpo), est["codigo"]))
            flujo.append(Spacer(1, 4))
            continue

        if not despojada:
            volcar_tabla()
            indice += 1
            continue

        if despojada.startswith("|"):
            celdas = [c.strip() for c in despojada.strip("|").split("|")]
            if not re.match(r"^[\s:|-]+$", despojada.strip("|")):
                buffer_tabla.append(celdas)
            indice += 1
            continue
        volcar_tabla()

        encabezado = re.match(r"^(#{1,6})\s+(.*)$", despojada)
        if encabezado:
            profundidad, texto = len(encabezado.group(1)), limpiar(encabezado.group(2))
            if profundidad == 1:
                parrafo = Paragraph(texto, est[nivel_titulo])
            elif profundidad == 2:
                parrafo = Paragraph(texto, est["h2"])
            else:
                parrafo = Paragraph(texto, est["h3"])
            flujo.append(parrafo)
            indice += 1
            continue

        if despojada.startswith(">"):
            cita: list[str] = []
            while indice < len(lineas) and lineas[indice].strip().startswith(">"):
                fragmento = lineas[indice].strip().lstrip(">").strip()
                if not re.match(r"^\[!\w+\]$", fragmento):
                    cita.append(fragmento)
                indice += 1
            if any(cita):
                flujo.append(Paragraph(limpiar(" ".join(cita)), est["cita"]))
            continue

        if re.match(r"^[-*+]\s+|^\d+[.)]\s+", despojada):
            contenido = re.sub(r"^[-*+]\s+|^\d+[.)]\s+", "", despojada)
            marca = "•"
            casilla = re.match(r"^\[([ xX])\]\s*(.*)$", contenido)
            if casilla:
                marca = "☑" if casilla.group(1).lower() == "x" else "☐"
                contenido = casilla.group(2)
            flujo.append(Paragraph(limpiar(contenido), est["lista"],
                                   bulletText=marca if marca == "•" else "-"))
            indice += 1
            continue

        if set(despojada) <= {"-"} and len(despojada) >= 3:
            flujo.append(Spacer(1, 6))
            indice += 1
            continue

        parrafo_txt: list[str] = []
        while indice < len(lineas) and lineas[indice].strip() and not re.match(
                r"^(#{1,6}\s|>|\||```|[-*+]\s|\d+[.)]\s|---)", lineas[indice].strip()):
            parrafo_txt.append(lineas[indice].strip())
            indice += 1
        if parrafo_txt:
            flujo.append(Paragraph(limpiar(" ".join(parrafo_txt)), est["cuerpo"]))

    volcar_tabla()
    return flujo


def portada(est: dict, titulo: str, subtitulo: str, datos: list[tuple[str, str]]) -> list:
    flujo = [Spacer(1, 55 * mm),
             Paragraph(titulo, est["portada_titulo"]),
             Paragraph(subtitulo, est["portada_sub"]),
             Spacer(1, 8 * mm)]
    filas = [[clave, valor] for clave, valor in datos]
    cuadro = Table(filas, colWidths=[55 * mm, 75 * mm], hAlign="CENTER")
    cuadro.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, BORDE),
        ("BACKGROUND", (0, 0), (0, -1), FONDO),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ]))
    flujo.append(cuadro)
    flujo.append(Spacer(1, 12 * mm))
    flujo.append(Paragraph(
        "Material educativo y de ingeniería empresarial. No reemplaza asesoría legal, tributaria, "
        "contable, laboral, sanitaria, financiera ni regulatoria para un caso concreto. Antes de "
        "ejecutar un trámite hay que verificar la fuente oficial vigente.", est["meta"]))
    flujo.append(NextPageTemplate("normal"))
    flujo.append(PageBreak())
    return flujo


def leer(ruta: Path) -> str:
    return ruta.read_text(encoding="utf-8")


def partes_ordenadas() -> list[Path]:
    return sorted((RAIZ / "curriculum").glob("part-*"), key=lambda p: p.name)


def clases_de(parte: Path) -> list[Path]:
    return sorted(parte.glob("class-*"), key=lambda p: p.name)


def construir_manual(est: dict, solo_parte: Path | None = None) -> tuple[Path, int]:
    curriculo = json.loads((RAIZ / "manifests" / "curriculum.json").read_text(encoding="utf-8"))
    version = (RAIZ / "VERSION").read_text(encoding="utf-8").strip()

    if solo_parte:
        partes = [solo_parte]
        numero = int(solo_parte.name.split("-")[1])
        titulo_doc = f"Parte {numero:02d} — {[c for c in curriculo if c['part'] == numero][0]['part_title']}"
        destino = SALIDA / "partes" / f"manual-{solo_parte.name}.pdf"
        total_clases = len(clases_de(solo_parte))
    else:
        partes = partes_ordenadas()
        titulo_doc = TITULO
        destino = SALIDA / f"modern-business-creation-program-manual-v{version}.pdf"
        total_clases = len(curriculo)

    destino.parent.mkdir(parents=True, exist_ok=True)
    documento = Documento(destino, titulo_doc)

    flujo = portada(est, titulo_doc, SUBTITULO, [
        ["Versión", version],
        ["Partes", str(len(partes))],
        ["Clases", str(total_clases)],
        ["Jurisdicción", "Chile-first"],
        ["Fecha base normativa", "07-08-2026"],
        ["Licencia", "MIT"],
    ])

    indice = TableOfContents()
    indice.levelStyles = [est["toc1"], est["toc2"]]
    # El propio encabezado del índice usa un estilo aparte para no autoindexarse.
    flujo += [Paragraph("Índice", est["titulo_indice"]), indice, PageBreak()]

    if not solo_parte:
        for nombre in ("README.md", "CURRICULUM.md"):
            flujo += convertir(leer(RAIZ / nombre), est)
            flujo.append(PageBreak())

    for parte in partes:
        flujo += convertir(leer(parte / "README.md"), est)
        flujo.append(PageBreak())
        for clase in clases_de(parte):
            flujo += convertir(leer(clase / "README.md"), est)
            flujo.append(PageBreak())

    if not solo_parte:
        flujo += convertir(leer(RAIZ / "docs" / "19_GLOSSARY.md"), est)

    documento.multiBuild(flujo)
    return destino, documento.page


PAGINAS_MINIMAS = 1200


def verificar() -> int:
    """Abre el PDF emitido y comprueba que tenga portada y extensión razonables.

    Un build en verde no prueba que el artefacto sirva: reportlab produce un PDF
    válido aunque el contenido llegue vacío. Aquí se lee el archivo de vuelta.
    """
    from pypdf import PdfReader

    version = (RAIZ / "VERSION").read_text(encoding="utf-8").strip()
    ruta = SALIDA / f"modern-business-creation-program-manual-v{version}.pdf"
    if not ruta.exists():
        print(f"ERROR: no existe {ruta.relative_to(RAIZ)}")
        return 1

    lector = PdfReader(str(ruta))
    paginas = len(lector.pages)
    portada_txt = lector.pages[0].extract_text() or ""
    problemas = []
    if paginas < PAGINAS_MINIMAS:
        problemas.append(f"solo {paginas} páginas, se esperaban al menos {PAGINAS_MINIMAS}")
    if TITULO not in portada_txt.replace("\n", " ").replace("  ", " "):
        problemas.append("la portada no contiene el título del programa")
    if version not in portada_txt:
        problemas.append(f"la portada no declara la versión {version}")

    if problemas:
        print("FALLÓ la verificación del manual:")
        for problema in problemas:
            print(f"  ERROR: {problema}")
        return 1

    print(f"OK: {ruta.name} · {paginas} páginas · "
          f"{ruta.stat().st_size / 1_048_576:.1f} MB · portada y versión correctas.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--partes", action="store_true", help="genera además un PDF por parte")
    parser.add_argument("--check", action="store_true", help="valida sin escribir en disco")
    parser.add_argument("--verificar", action="store_true",
                        help="abre el PDF ya generado y comprueba portada y extensión")
    args = parser.parse_args()

    if args.verificar:
        return verificar()

    if args.check:
        faltan = [p.name for p in partes_ordenadas() if not (p / "README.md").exists()]
        if faltan:
            print(f"ERROR: partes sin README: {faltan}")
            return 1
        print(f"OK: {len(partes_ordenadas())} partes y "
              f"{sum(len(clases_de(p)) for p in partes_ordenadas())} clases listas para compilar.")
        return 0

    est = estilos()
    generados = []

    ruta, paginas = construir_manual(est)
    generados.append({"archivo": ruta.relative_to(RAIZ).as_posix(), "paginas": paginas,
                      "bytes": ruta.stat().st_size,
                      "sha256": hashlib.sha256(ruta.read_bytes()).hexdigest()})
    print(f"OK: {ruta.relative_to(RAIZ)} · {paginas} páginas · "
          f"{ruta.stat().st_size / 1_048_576:.1f} MB")

    if args.partes:
        for parte in partes_ordenadas():
            ruta_parte, paginas_parte = construir_manual(est, parte)
            generados.append({"archivo": ruta_parte.relative_to(RAIZ).as_posix(),
                              "paginas": paginas_parte, "bytes": ruta_parte.stat().st_size,
                              "sha256": hashlib.sha256(ruta_parte.read_bytes()).hexdigest()})
            print(f"  {ruta_parte.name} · {paginas_parte} páginas")

    MANIFIESTO.write_text(json.dumps(generados, ensure_ascii=False, indent=2) + "\n",
                          encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
