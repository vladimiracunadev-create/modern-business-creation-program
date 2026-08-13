#!/usr/bin/env python3
"""Valida la estructura del repositorio, las secciones de cada clase y los enlaces internos.

Comprueba:
  1. que los manifiestos sean coherentes entre sí (currículo, packs, contenido por clase);
  2. que exista una carpeta y un README por cada clase declarada, y ninguno de más;
  3. que cada README de clase tenga todas las secciones obligatorias;
  4. que todos los enlaces relativos de los .md apunten a archivos existentes;
  5. que las URL del catálogo de fuentes sean https.

Salida: lista de errores y código 1, o "OK" y código 0.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

RAIZ = Path(__file__).resolve().parents[1]
MANIFESTS = RAIZ / "manifests"
CURRICULUM = RAIZ / "curriculum"

SECCIONES_CLASE = [
    "## Objetivo",
    "## Resultados verificables",
    "## Conceptos clave",
    "## Desarrollo",
    "## Marco aplicable en esta parte",
    "## Flujo de trabajo",
    "## Taller guiado",
    "### Entregable",
    "## Reto",
    "### Criterio de aceptación",
    "## Errores comunes",
    "## Profesionales a considerar",
    "## Checklist Chile",
    "## Fuentes oficiales",
]

SECCIONES_PARTE = [
    "## Resultados de la parte",
    "## Marco aplicable",
    "## Riesgos característicos de esta parte",
    "## Clases",
    "## Fuentes oficiales de la parte",
]

# Enlaces markdown [texto](destino), ignorando imágenes y anclas de referencia.
ENLACE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

# Directorios que no se recorren al validar enlaces (artefactos de build o deps).
IGNORADOS = {".git", "node_modules", "site", ".venv", "__pycache__"}


def cargar(nombre: str):
    return json.loads((MANIFESTS / nombre).read_text(encoding="utf-8"))


def archivos_markdown() -> list[Path]:
    return [
        p for p in RAIZ.rglob("*.md")
        if not any(parte in IGNORADOS for parte in p.relative_to(RAIZ).parts)
    ]


def main() -> int:
    errores: list[str] = []

    curriculo = cargar("curriculum.json")
    packs = cargar("part_packs.json")
    fuentes = cargar("official_sources.json")

    contenido_clases: dict[int, dict] = {}
    for archivo in sorted((MANIFESTS / "classes").glob("*.json")):
        for entrada in json.loads(archivo.read_text(encoding="utf-8")):
            if entrada["n"] in contenido_clases:
                errores.append(f"clase {entrada['n']} duplicada en manifests/classes/")
            contenido_clases[entrada["n"]] = entrada

    # 1. Coherencia de manifiestos.
    partes_declaradas = {p["part"] for p in packs}
    partes_en_curriculo = {c["part"] for c in curriculo}
    if partes_declaradas != partes_en_curriculo:
        errores.append(
            f"partes desalineadas: packs={sorted(partes_declaradas)} "
            f"currículo={sorted(partes_en_curriculo)}"
        )
    if len(packs) != 24:
        errores.append(f"esperaba 24 packs de parte, hay {len(packs)}")

    globales = [c["global_class"] for c in curriculo]
    if globales != list(range(1, len(curriculo) + 1)):
        errores.append("la numeración global de clases no es 1..N sin saltos")
    if len(curriculo) != 336:
        errores.append(f"esperaba 336 clases en el currículo, hay {len(curriculo)}")

    sin_contenido = [n for n in globales if n not in contenido_clases]
    if sin_contenido:
        errores.append(f"clases sin contenido específico: {sin_contenido[:10]}")
    sobrantes = [n for n in contenido_clases if n not in set(globales)]
    if sobrantes:
        errores.append(f"contenido específico sin clase asociada: {sobrantes[:10]}")

    ids_fuentes = {f["id"] for f in fuentes}
    for entrada in contenido_clases.values():
        desconocidas = set(entrada.get("fuentes", [])) - ids_fuentes
        if desconocidas:
            errores.append(f"clase {entrada['n']}: fuentes desconocidas {sorted(desconocidas)}")
    for pack in packs:
        desconocidas = set(pack["fuentes"]) - ids_fuentes
        if desconocidas:
            errores.append(f"parte {pack['part']}: fuentes desconocidas {sorted(desconocidas)}")

    # 2. Estructura en disco.
    carpetas_parte = sorted(p for p in CURRICULUM.glob("part-*") if p.is_dir())
    if len(carpetas_parte) != len(packs):
        errores.append(f"hay {len(carpetas_parte)} carpetas de parte y {len(packs)} packs")

    readmes_clase = sorted(CURRICULUM.glob("part-*/class-*/README.md"))
    if len(readmes_clase) != len(curriculo):
        errores.append(
            f"hay {len(readmes_clase)} README de clase y {len(curriculo)} clases declaradas"
        )

    # 3. Secciones obligatorias.
    for readme in readmes_clase:
        texto = readme.read_text(encoding="utf-8")
        for seccion in SECCIONES_CLASE:
            if seccion not in texto:
                errores.append(f"{readme.relative_to(RAIZ).as_posix()}: falta '{seccion}'")

    for carpeta in carpetas_parte:
        readme = carpeta / "README.md"
        if not readme.exists():
            errores.append(f"{carpeta.relative_to(RAIZ).as_posix()}: falta README.md")
            continue
        texto = readme.read_text(encoding="utf-8")
        for seccion in SECCIONES_PARTE:
            if seccion not in texto:
                errores.append(f"{readme.relative_to(RAIZ).as_posix()}: falta '{seccion}'")

    # 4. Enlaces internos.
    for markdown in archivos_markdown():
        texto = markdown.read_text(encoding="utf-8")
        for destino in ENLACE.findall(texto):
            if destino.startswith(("http://", "https://", "mailto:", "#")):
                continue
            objetivo = (markdown.parent / unquote(destino.split("#", 1)[0])).resolve()
            if not objetivo.exists():
                errores.append(
                    f"{markdown.relative_to(RAIZ).as_posix()}: enlace roto -> {destino}"
                )

    # 5. Catálogo de fuentes.
    if len(fuentes) < 20:
        errores.append(f"catálogo de fuentes demasiado pequeño ({len(fuentes)})")
    for fuente in fuentes:
        if not fuente["url"].startswith("https://"):
            errores.append(f"fuente {fuente['id']}: URL no https -> {fuente['url']}")

    if errores:
        print(f"FALLÓ la validación con {len(errores)} error(es):")
        for error in errores[:60]:
            print(f"  ERROR: {error}")
        if len(errores) > 60:
            print(f"  ... y {len(errores) - 60} más")
        return 1

    print(
        f"OK: {len(curriculo)} clases en {len(packs)} partes, "
        f"{len(readmes_clase)} README validados, "
        f"{len(archivos_markdown())} archivos markdown con enlaces correctos, "
        f"{len(fuentes)} fuentes oficiales."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
