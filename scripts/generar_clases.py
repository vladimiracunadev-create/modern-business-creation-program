#!/usr/bin/env python3
"""Genera el currículo completo a partir de los manifiestos.

Fuentes de verdad:
  manifests/curriculum.json        -> qué clases existen y cómo se llaman
  manifests/part_packs.json        -> conocimiento de dominio por parte (24)
  manifests/classes/*.json         -> contenido específico por clase (336)
  manifests/official_sources.json  -> catálogo de fuentes oficiales

Salida:
  curriculum/part-NN-<slug>/class-NN-<slug>/README.md
  curriculum/part-NN-<slug>/README.md
  CURRICULUM.md

Uso:
  python scripts/generar_clases.py            # escribe
  python scripts/generar_clases.py --check    # falla si algo está desactualizado
"""

from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
MANIFESTS = RAIZ / "manifests"
CURRICULUM = RAIZ / "curriculum"

FECHA_BASE = "07-08-2026"

# Reemplazos previos a la normalización Unicode: la descomposición NFKD no
# separa estos caracteres, así que hay que mapearlos a mano o desaparecen.
TRANSLITERACION = {"ñ": "n", "Ñ": "n", "ü": "u", "Ü": "u"}


def slug(texto: str) -> str:
    """Convierte un título a slug ASCII estable, igual al usado en el repo."""
    for origen, destino in TRANSLITERACION.items():
        texto = texto.replace(origen, destino)
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    salida = []
    for caracter in texto.lower():
        if caracter.isalnum():
            salida.append(caracter)
        elif salida and salida[-1] != "-":
            salida.append("-")
    return "".join(salida).strip("-")


def cargar_json(ruta: Path):
    return json.loads(ruta.read_text(encoding="utf-8"))


def cargar_datos():
    curriculo = cargar_json(MANIFESTS / "curriculum.json")
    packs = {p["part"]: p for p in cargar_json(MANIFESTS / "part_packs.json")}
    fuentes = {f["id"]: f for f in cargar_json(MANIFESTS / "official_sources.json")}

    especificas = {}
    for archivo in sorted((MANIFESTS / "classes").glob("*.json")):
        for entrada in cargar_json(archivo):
            especificas[entrada["n"]] = entrada

    faltantes = [c["global_class"] for c in curriculo if c["global_class"] not in especificas]
    if faltantes:
        raise SystemExit(f"ERROR: sin contenido específico las clases {faltantes[:10]}")
    return curriculo, packs, fuentes, especificas


def ruta_parte(parte: int, titulo: str) -> Path:
    return CURRICULUM / f"part-{parte:02d}-{slug(titulo)}"


def ruta_clase(clase: dict) -> Path:
    carpeta = ruta_parte(clase["part"], clase["part_title"])
    return carpeta / f"class-{clase['class']:02d}-{slug(clase['title'])}"


def bloque_fuentes(ids: list[str], fuentes: dict) -> str:
    lineas = []
    for identificador in ids:
        fuente = fuentes.get(identificador)
        if fuente is None:
            raise SystemExit(f"ERROR: fuente desconocida '{identificador}'")
        lineas.append(f"- **{fuente['entity']}** — {fuente['topic']}: <{fuente['url']}>")
    return "\n".join(lineas)


def render_clase(clase: dict, pack: dict, spec: dict, fuentes: dict,
                 anterior: dict | None, siguiente: dict | None) -> str:
    numero = clase["global_class"]
    total_parte = pack["_total_clases"]
    ids_fuentes = spec.get("fuentes") or pack["fuentes"][:3]

    conceptos = "\n".join(
        f"| **{termino}** | {definicion} |" for termino, definicion in spec["conceptos"]
    )
    marco = "\n".join(f"- {item}" for item in pack["marco"])
    errores_clase = "\n".join(f"- {e}" for e in spec["errores"])
    errores_parte = "\n".join(f"- {e}" for e in pack["riesgos"][:2])
    criterios = "\n".join(f"- [ ] {c}" for c in spec["criterios"])
    profesionales = ", ".join(pack["profesionales"])
    autoridades = ", ".join(pack["autoridades"])

    nav = []
    if anterior:
        nav.append(
            f"[← {anterior['global_class']:03d}. {anterior['title']}]"
            f"(../{ruta_clase(anterior).name}/README.md)"
        )
    nav.append("[Índice de la parte](../README.md)")
    if siguiente:
        destino = (
            f"../{ruta_clase(siguiente).name}/README.md"
            if siguiente["part"] == clase["part"]
            else f"../../{ruta_parte(siguiente['part'], siguiente['part_title']).name}/{ruta_clase(siguiente).name}/README.md"
        )
        nav.append(f"[{siguiente['global_class']:03d}. {siguiente['title']} →]({destino})")

    return f"""# Clase {numero:03d} — {clase['title']}

> **Parte {clase['part']:02d} · {clase['part_title']}** — clase {clase['class']} de {total_parte}
> Estado: `{pack['estado']}` · Jurisdicción: **Chile-first** · Fecha base normativa: **{FECHA_BASE}**

## Objetivo

Comprender **{clase['title'].lower()}** dentro del sistema de creación y operación de una empresa,
y quedar en condiciones de tomar la decisión que esta clase habilita:
*{spec['decision']}*.

## Resultados verificables

Al finalizar, quien estudia esta clase puede:

1. definir los conceptos de la tabla siguiente sin recurrir a una definición memorizada;
2. explicar cómo esta materia condiciona a las demás partes del programa;
3. tomar la decisión declarada arriba y justificarla por escrito;
4. producir el entregable de la clase con criterio de aceptación verificable;
5. identificar qué dato es estable y cuál es dinámico y requiere revalidación en la fuente.

## Conceptos clave

| Concepto | Definición operacional |
|---|---|
{conceptos}

## Desarrollo

{spec['desarrollo']}

## Marco aplicable en esta parte

{marco}

**Autoridades o contrapartes involucradas:** {autoridades}.

## Flujo de trabajo

1. Delimitar el contexto: actividad económica, escala, comuna y etapa de la empresa.
2. Reunir los antecedentes que la decisión exige y verificar su fecha.
3. Identificar las alternativas reales, incluida la de no hacer nada.
4. Evaluar el impacto en mercado, caja, personas, regulación y operación.
5. Tomar la decisión y dejarla registrada con sus supuestos.
6. Ejecutar o simular el flujo hasta producir el entregable.
7. Contrastar el resultado contra el criterio de aceptación.
8. Anotar lo que requiere validación profesional y programar su revisión.

## Taller guiado

Aplicar esta clase a **una** de las siguientes líneas de negocio, y repetir el ejercicio con una
segunda línea de carga regulatoria distinta:

- SaaS B2B con IA;
- servicios profesionales;
- e-commerce D2C;
- alimentos o foodtech;
- exportación de servicios;
- fintech regulada;
- construcción o servicios técnicos.

### Entregable

{spec['entregable'].capitalize()}.

El documento debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable,
riesgos identificados y próximos pasos.

## Reto

Resolver la misma materia para una segunda línea de negocio con distinta carga regulatoria,
y explicar por escrito **qué cambió y por qué**.

### Criterio de aceptación

{criterios}
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## Errores comunes

{errores_clase}
{errores_parte}

## Profesionales a considerar

{profesionales.capitalize()}. La participación concreta depende del riesgo, el tamaño de la
empresa y la actividad económica; este material no reemplaza esa asesoría.

## Checklist Chile

- [ ] ¿existe norma o autoridad específica para esta materia?
- [ ] ¿la fuente consultada está vigente a la fecha de ejecución?
- [ ] ¿se activa algún trámite ante el SII?
- [ ] ¿se activa algún requisito municipal o sectorial?
- [ ] ¿afecta a consumidores o al tratamiento de datos personales?
- [ ] ¿afecta a trabajadores o a la seguridad y salud en el trabajo?
- [ ] ¿afecta a impuestos, contabilidad o caja?
- [ ] ¿afecta a contratos o a propiedad intelectual?
- [ ] ¿requiere renovación, reporte periódico o revalidación?

## Fuentes oficiales

{bloque_fuentes(ids_fuentes, fuentes)}

Lecturas complementarias: [`docs/15_BOOKS_AND_LEARNING_PATH.md`](../../../docs/15_BOOKS_AND_LEARNING_PATH.md)
y [`docs/16_OFFICIAL_SOURCE_CATALOG.md`](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

{" · ".join(nav)}
"""


def render_parte(pack: dict, clases: list[dict], fuentes: dict) -> str:
    resultados = "\n".join(f"{i}. {r};" for i, r in enumerate(pack["resultados"], 1))
    marco = "\n".join(f"- {item}" for item in pack["marco"])
    riesgos = "\n".join(f"- {r}" for r in pack["riesgos"])
    indice = "\n".join(
        f"| {c['class']:02d} | {c['global_class']:03d} | [{c['title']}]({ruta_clase(c).name}/README.md) |"
        for c in clases
    )
    rango = f"{clases[0]['global_class']:03d}–{clases[-1]['global_class']:03d}"
    return f"""# Parte {pack['part']:02d} — {pack['titulo']}

> Estado: `{pack['estado']}` · {len(clases)} clases ({rango}) · Fecha base normativa: **{FECHA_BASE}**

{pack['resumen']}

## Resultados de la parte

Al terminar esta parte, quien estudia puede:

{resultados}

## Marco aplicable

{marco}

**Autoridades o contrapartes:** {", ".join(pack['autoridades'])}.
**Profesionales de apoyo:** {", ".join(pack['profesionales'])}.

## Riesgos característicos de esta parte

{riesgos}

## Clases

| # | Global | Clase |
|---:|---:|---|
{indice}

## Fuentes oficiales de la parte

{bloque_fuentes(pack['fuentes'], fuentes)}

---

[← Volver al currículo completo](../../CURRICULUM.md) · [Inicio](../../README.md)
"""


def render_curriculum(curriculo: list[dict], packs: dict) -> str:
    filas = []
    for parte in sorted(packs):
        pack = packs[parte]
        clases = [c for c in curriculo if c["part"] == parte]
        filas.append(
            f"| {parte:02d} | [{pack['titulo']}]"
            f"(curriculum/{ruta_parte(parte, pack['titulo']).name}/README.md) "
            f"| {len(clases)} | {clases[0]['global_class']:03d}–{clases[-1]['global_class']:03d} "
            f"| `{pack['estado']}` |"
        )
    tabla = "\n".join(filas)
    return f"""# Currículo — {len(curriculo)} clases en {len(packs)} partes

Cada parte tiene su propio README con narrativa, marco normativo, riesgos característicos y el
índice de sus clases. Cada clase es una carpeta con un `README.md` autocontenido.

| # | Parte | Clases | Rango | Estado |
|---:|---|---:|---|---|
{tabla}

## Estados de evidencia

| Estado | Significado |
|---|---|
| `VERIFICADO-FUENTE` | Referido a fuente oficial primaria o institucional |
| `GUIA-PRACTICA` | Síntesis educativa que debe adaptarse al caso concreto |
| `SECTORIAL` | Aplica solo si la actividad cae en ese sector |
| `DINAMICO` | Tasa, plazo, convocatoria o norma en transición que debe revisarse a la fecha de ejecución |

---

[← Inicio](README.md)
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="no escribe; falla si hay archivos desactualizados")
    args = parser.parse_args()

    curriculo, packs, fuentes, especificas = cargar_datos()
    for parte, pack in packs.items():
        pack["_total_clases"] = sum(1 for c in curriculo if c["part"] == parte)

    pendientes: list[tuple[Path, str]] = []

    for indice, clase in enumerate(curriculo):
        anterior = curriculo[indice - 1] if indice else None
        siguiente = curriculo[indice + 1] if indice + 1 < len(curriculo) else None
        # El enlace "anterior" solo se dibuja dentro de la misma parte: cruzarlo
        # produciría una ruta relativa que rompe al cambiar de carpeta padre.
        if anterior and anterior["part"] != clase["part"]:
            anterior = None
        contenido = render_clase(
            clase, packs[clase["part"]], especificas[clase["global_class"]],
            fuentes, anterior, siguiente,
        )
        pendientes.append((ruta_clase(clase) / "README.md", contenido))

    for parte, pack in packs.items():
        clases = [c for c in curriculo if c["part"] == parte]
        pendientes.append((ruta_parte(parte, pack["titulo"]) / "README.md",
                           render_parte(pack, clases, fuentes)))

    pendientes.append((RAIZ / "CURRICULUM.md", render_curriculum(curriculo, packs)))

    # Carpetas de clase que ya no corresponden a ninguna entrada del manifiesto:
    # aparecen al renombrar una clase y dejarían READMEs huérfanos en el sitio.
    esperadas = {ruta_clase(c) for c in curriculo}
    huerfanas = sorted(
        p for p in CURRICULUM.glob("part-*/class-*") if p.is_dir() and p not in esperadas
    )

    desactualizados = []
    for ruta, contenido in pendientes:
        actual = ruta.read_text(encoding="utf-8") if ruta.exists() else None
        if actual == contenido:
            continue
        desactualizados.append(ruta.relative_to(RAIZ).as_posix())
        if not args.check:
            ruta.parent.mkdir(parents=True, exist_ok=True)
            ruta.write_text(contenido, encoding="utf-8")

    if args.check:
        problemas = desactualizados + [f"huérfana: {p.relative_to(RAIZ).as_posix()}" for p in huerfanas]
        if problemas:
            print("ERROR: el currículo no está sincronizado con los manifiestos:")
            for ruta in problemas[:20]:
                print(f"  - {ruta}")
            if len(problemas) > 20:
                print(f"  ... y {len(problemas) - 20} más")
            print("Ejecuta: python scripts/generar_clases.py")
            return 1
        print(f"OK: {len(pendientes)} archivos sincronizados con los manifiestos")
        return 0

    for carpeta in huerfanas:
        for archivo in sorted(carpeta.rglob("*"), reverse=True):
            archivo.unlink() if archivo.is_file() else archivo.rmdir()
        carpeta.rmdir()
        print(f"  eliminada carpeta huérfana: {carpeta.relative_to(RAIZ).as_posix()}")

    print(f"OK: {len(pendientes)} archivos generados ({len(desactualizados)} actualizados)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
