#!/usr/bin/env python3
"""Genera el currículo completo a partir de los manifiestos.

Fuentes de verdad:
  manifests/curriculum.json        -> qué clases existen y cómo se llaman
  manifests/part_packs.json        -> marco normativo y riesgos por parte (24)
  manifests/part_content.json      -> narrativa, diagrama y lecturas por parte (24)
  manifests/classes/*.json         -> contenido operativo por clase (336)
  manifests/pedagogia/*.json       -> propósito, desarrollo y preguntas por clase (336)
  manifests/official_sources.json  -> catálogo de fuentes con qué dice y cómo leerla

Salida:
  curriculum/part-NN-<slug>/class-NN-<slug>/README.md
  curriculum/part-NN-<slug>/README.md
  CURRICULUM.md
  docs/19_GLOSSARY.md

Uso:
  python scripts/generar_clases.py            # escribe
  python scripts/generar_clases.py --check    # falla si algo está desactualizado
"""

from __future__ import annotations

import argparse
import json
import re
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


def etiqueta(texto: str, ancho: int = 34) -> str:
    """Prepara un texto para usarlo como etiqueta de nodo mermaid.

    Mermaid rompe con comillas dobles dentro de una etiqueta entrecomillada y no
    corta líneas solo, así que aquí se sustituyen las comillas y se inserta el
    salto explícito `<br/>` cada `ancho` caracteres aproximados.
    """
    texto = texto.replace('"', "'").replace("\n", " ").strip()
    palabras, lineas, actual = texto.split(), [], ""
    for palabra in palabras:
        if len(actual) + len(palabra) + 1 > ancho and actual:
            lineas.append(actual)
            actual = palabra
        else:
            actual = f"{actual} {palabra}".strip()
    if actual:
        lineas.append(actual)
    return "<br/>".join(lineas)


def cargar_json(ruta: Path):
    return json.loads(ruta.read_text(encoding="utf-8"))


def cargar_carpeta(carpeta: Path, clave: str = "n") -> dict:
    datos = {}
    for archivo in sorted(carpeta.glob("*.json")):
        for entrada in cargar_json(archivo):
            datos[entrada[clave]] = entrada
    return datos


def cargar_datos():
    curriculo = cargar_json(MANIFESTS / "curriculum.json")
    packs = {p["part"]: p for p in cargar_json(MANIFESTS / "part_packs.json")}
    for extra in cargar_json(MANIFESTS / "part_content.json"):
        packs[extra["part"]].update(extra)
    fuentes = {f["id"]: f for f in cargar_json(MANIFESTS / "official_sources.json")}

    especificas = cargar_carpeta(MANIFESTS / "classes")
    pedagogia = cargar_carpeta(MANIFESTS / "pedagogia")
    for numero, entrada in pedagogia.items():
        if numero in especificas:
            especificas[numero].update(entrada)

    faltantes = [
        c["global_class"] for c in curriculo
        if c["global_class"] not in especificas or "proposito" not in especificas[c["global_class"]]
    ]
    if faltantes:
        raise SystemExit(f"ERROR: sin contenido completo las clases {faltantes[:10]}")
    return curriculo, packs, fuentes, especificas


def ruta_parte(parte: int, titulo: str) -> Path:
    return CURRICULUM / f"part-{parte:02d}-{slug(titulo)}"


def ruta_clase(clase: dict) -> Path:
    carpeta = ruta_parte(clase["part"], clase["part_title"])
    return carpeta / f"class-{clase['class']:02d}-{slug(clase['title'])}"


def bloque_fuentes(ids: list[str], fuentes: dict) -> str:
    """Renderiza las fuentes explicando qué dicen y cómo leerlas.

    Enlazar una fuente sin explicarla obliga a quien estudia a descubrir por su
    cuenta qué parte del sitio importa; por eso cada entrada trae el contenido y
    la instrucción de lectura.
    """
    bloques = []
    for identificador in ids:
        fuente = fuentes.get(identificador)
        if fuente is None:
            raise SystemExit(f"ERROR: fuente desconocida '{identificador}'")
        bloques.append(
            f"**{fuente['entity']} — {fuente['topic']}**  \n"
            f"<{fuente['url']}> · verificado {fuente['verificado']}\n\n"
            f"- *Qué contiene:* {fuente['que_dice']}\n"
            f"- *Cómo leerla:* {fuente['como_leerla']}"
        )
    return "\n\n".join(bloques)


def diagrama_clase(clase: dict, spec: dict) -> str:
    """Construye el diagrama de razonamiento propio de la clase.

    No es decorativo: los nodos salen de los cuatro conceptos, la decisión y el
    entregable de esta clase concreta, así que dos clases nunca producen el mismo
    diagrama.
    """
    conceptos = [c[0] for c in spec["conceptos"]]
    nodos = "\n".join(
        f'    C --> A{i}["{etiqueta(termino, 26)}"]' for i, termino in enumerate(conceptos, 1)
    )
    union = " & ".join(f"A{i}" for i in range(1, len(conceptos) + 1))
    return f"""```mermaid
flowchart TB
    C["Contexto del caso<br/>actividad · escala · comuna"]
{nodos}
    {union} --> D{{{{"{etiqueta(spec['decision'], 30)}"}}}}
    D --> E["Entregable<br/>{etiqueta(spec['entregable'], 30)}"]
    E --> V{{"¿Cumple el criterio<br/>de aceptación?"}}
    V -->|sí| S["Evidencia archivada<br/>y clase siguiente"]
    V -->|no| C
```"""


def render_clase(clase: dict, pack: dict, spec: dict, fuentes: dict,
                 anterior: dict | None, siguiente: dict | None) -> str:
    numero = clase["global_class"]
    total_parte = pack["_total_clases"]
    ids_fuentes = spec.get("fuentes") or pack["fuentes"][:3]

    conceptos = "\n".join(
        f"| **{termino}** | {definicion.capitalize()}. |" for termino, definicion in spec["conceptos"]
    )
    marco = "\n".join(f"- {item}" for item in pack["marco"])
    errores_clase = "\n".join(f"- {e.capitalize()}." for e in spec["errores"])
    errores_parte = "\n".join(f"- {e.capitalize()}." for e in pack["riesgos"][:2])
    criterios = "\n".join(f"- [ ] {c}" for c in spec["criterios"])
    preguntas = "\n".join(f"{i}. {p}" for i, p in enumerate(spec["preguntas"], 1))
    profesionales = ", ".join(pack["profesionales"])
    autoridades = ", ".join(pack["autoridades"])

    if anterior:
        celda_anterior = (
            f"[← {anterior['global_class']:03d} · {anterior['title']}]"
            f"(../{ruta_clase(anterior).name}/README.md)"
        )
    else:
        celda_anterior = "**Inicio de la parte**"

    if siguiente:
        destino = (
            f"../{ruta_clase(siguiente).name}/README.md"
            if siguiente["part"] == clase["part"]
            else f"../../{ruta_parte(siguiente['part'], siguiente['part_title']).name}/{ruta_clase(siguiente).name}/README.md"
        )
        celda_siguiente = f"[{siguiente['global_class']:03d} · {siguiente['title']} →]({destino})"
    else:
        celda_siguiente = "**Fin del programa**"

    return f"""# Clase {numero:03d} — {clase['title']}

> **Parte {clase['part']:02d} · {pack['titulo']}** — clase {clase['class']} de {total_parte}

**Estado de evidencia:** `{pack['estado']}` · **Jurisdicción:** Chile-first · **Fecha base normativa:** {FECHA_BASE}<br>
**Decisión que habilita:** {spec['decision']}<br>
**Entregable:** {spec['entregable']}

## 🎯 Propósito

{spec['proposito']}

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —{spec['decision']}— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
{conceptos}

## 🗺️ Flujo de razonamiento

{diagrama_clase(clase, spec)}

## 📖 Desarrollo

### 1. El fondo del asunto

{spec['desarrollo']}

### 2. Cómo se traduce en la práctica

{spec['desarrollo2']}

### 3. Marco aplicable y quién interviene

{marco}

**Autoridades o contrapartes involucradas:** {autoridades}.
**Profesionales de apoyo:** {profesionales}. La participación concreta depende del riesgo, del
tamaño de la empresa y de la actividad económica.

## 🧪 Taller guiado

Aplica esta clase a **una** de las siguientes líneas de negocio y repite después el ejercicio con
una segunda línea de carga regulatoria distinta:

| Línea | Carga regulatoria |
|---|---|
| SaaS B2B con IA | media |
| Servicios profesionales | baja |
| E-commerce D2C | media |
| Alimentos o foodtech | alta |
| Exportación de servicios | media |
| Fintech regulada | alta |
| Construcción o servicios técnicos | alta |

**Secuencia de trabajo:**

1. Delimita el contexto: actividad económica, escala, comuna y etapa de la empresa.
2. Reúne los antecedentes que la decisión exige y anota la fecha de cada fuente.
3. Identifica las alternativas reales, incluida la de no hacer nada.
4. Evalúa el impacto en mercado, caja, personas, regulación y operación.
5. Toma la decisión y regístrala con sus supuestos.
6. Produce el entregable.
7. Contrástalo contra el criterio de aceptación.
8. Anota lo que requiere validación profesional y programa su revisión.

### 📦 Entregable

{spec['entregable'].capitalize()}.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

{criterios}
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

{errores_clase}

**Característicos de la parte {clase['part']:02d}:**

{errores_parte}

## 🇨🇱 Checklist Chile

- [ ] ¿existe norma o autoridad específica para esta materia?
- [ ] ¿la fuente consultada está vigente a la fecha de ejecución?
- [ ] ¿se activa algún trámite ante el SII?
- [ ] ¿se activa algún requisito municipal o sectorial?
- [ ] ¿afecta a consumidores o al tratamiento de datos personales?
- [ ] ¿afecta a trabajadores o a la seguridad y salud en el trabajo?
- [ ] ¿afecta a impuestos, contabilidad o caja?
- [ ] ¿afecta a contratos o a propiedad intelectual?
- [ ] ¿requiere renovación, reporte periódico o revalidación?

## ❓ Preguntas de comprobación

{preguntas}

## 🔗 Fuentes oficiales

{bloque_fuentes(ids_fuentes, fuentes)}

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| {celda_anterior} | [Parte {clase['part']:02d}](../README.md) · [Programa](../../../README.md) | {celda_siguiente} |
"""


def render_parte(pack: dict, clases: list[dict], especificas: dict, fuentes: dict,
                 anterior: dict | None, siguiente: dict | None) -> str:
    rango = f"{clases[0]['global_class']:03d}–{clases[-1]['global_class']:03d}"
    resultados = "\n".join(f"{i}. **{r[0].upper()}{r[1:]}**." for i, r in enumerate(pack["resultados"], 1))
    marco = "\n".join(f"- {item}" for item in pack["marco"])
    riesgos = "\n".join(f"- {r.capitalize()}." for r in pack["riesgos"])
    lecturas = "\n".join(f"- {item}" for item in pack["lecturas"])
    indice = "\n".join(
        f"| {c['class']:02d} | {c['global_class']:03d} | "
        f"[{c['title']}]({ruta_clase(c).name}/README.md) | "
        f"{especificas[c['global_class']]['decision']} |"
        for c in clases
    )

    # Glosario de la parte: los 56 conceptos de sus clases, sin repetir término.
    glosario: dict[str, str] = {}
    for c in clases:
        for termino, definicion in especificas[c["global_class"]]["conceptos"]:
            glosario.setdefault(termino, definicion)
    filas_glosario = "\n".join(
        f"| **{t}** | {d.capitalize()}. |" for t, d in sorted(glosario.items(), key=lambda x: x[0].lower())
    )

    nav_anterior = (
        f"[← Parte {anterior['part']:02d} · {anterior['titulo']}]"
        f"(../{ruta_parte(anterior['part'], anterior['titulo']).name}/README.md)"
        if anterior else "**Primera parte**"
    )
    nav_siguiente = (
        f"[Parte {siguiente['part']:02d} · {siguiente['titulo']} →]"
        f"(../{ruta_parte(siguiente['part'], siguiente['titulo']).name}/README.md)"
        if siguiente else "**Última parte**"
    )

    return f"""# Parte {pack['part']:02d} — {pack['titulo']}

> *{pack['lema']}*

**Estado de evidencia:** `{pack['estado']}` · **Clases:** {len(clases)} ({rango}) · **Fecha base normativa:** {FECHA_BASE}<br>
**Conceptos definidos en esta parte:** {len(glosario)}

## 🎯 De qué trata esta parte

{pack['narrativa']}

## 📚 Resultados de la parte

Al terminar esta parte podrás:

{resultados}

## 🗺️ Mapa de la parte

{pack['diagrama_render']}

## ⚖️ Marco aplicable

{marco}

**Autoridades o contrapartes:** {", ".join(pack['autoridades'])}.
**Profesionales de apoyo:** {", ".join(pack['profesionales'])}.

## ⚠️ Riesgos característicos

{riesgos}

## 📘 Las {len(clases)} clases

| # | Global | Clase | Decisión que habilita |
|---:|---:|---|---|
{indice}

## 🔤 Glosario de la parte

| Concepto | Definición operacional |
|---|---|
{filas_glosario}

## 🔗 Cómo se conecta

{pack['conexiones']}

## 📖 Pauta bibliográfica

{lecturas}

## 🏛️ Fuentes oficiales de la parte

{bloque_fuentes(pack['fuentes'], fuentes)}

---

| Anterior | Índice | Siguiente |
|---|---|---|
| {nav_anterior} | [Currículo](../../CURRICULUM.md) · [Programa](../../README.md) | {nav_siguiente} |
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
            f"| `{pack['estado']}` | {pack['lema']} |"
        )
    tabla = "\n".join(filas)
    return f"""# Currículo — {len(curriculo)} clases en {len(packs)} partes

Cada parte tiene su propio README con narrativa, mapa visual, marco normativo, glosario propio y
el índice de sus clases. Cada clase es una carpeta con un `README.md` autocontenido que incluye
diagrama de razonamiento, desarrollo, taller, criterio de aceptación y fuentes explicadas.

## 🗺️ Recorrido completo

```mermaid
flowchart LR
    subgraph F1["Fundamentos y mercado · 01-04"]
        P1["01 Fundamentos"] --> P2["02 Validación"] --> P3["03 Modelos"] --> P4["04 Estrategia"]
    end
    subgraph F2["Constitución y finanzas · 05-09"]
        P5["05 Societario"] --> P6["06 Constitución"] --> P7["07 SII"] --> P8["08 Contabilidad"] --> P9["09 Finanzas"]
    end
    subgraph F3["Marco legal y personas · 10-12"]
        P10["10 Contratos"] --> P11["11 Consumidor y datos"] --> P12["12 Personas"]
    end
    subgraph F4["Operación y crecimiento · 13-20"]
        P13["13 Operaciones"] --> P14["14 Ventas"] --> P15["15 Tecnología"] --> P16["16 Financiamiento"]
        P16 --> P17["17 Permisos"] --> P18["18 Comercio exterior"] --> P19["19 Compliance"] --> P20["20 Escalamiento"]
    end
    subgraph F5["Crisis, salida y práctica · 21-24"]
        P21["21 Crisis"] --> P22["22 Venta y cierre"] --> P23["23 Casos 2026"] --> P24["24 Capstone"]
    end
    F1 --> F2 --> F3 --> F4 --> F5
```

## 📘 Las {len(packs)} partes

| # | Parte | Clases | Rango | Estado | Idea central |
|---:|---|---:|---|---|---|
{tabla}

## 🏷️ Estados de evidencia

| Estado | Significado |
|---|---|
| `VERIFICADO-FUENTE` | Referido a fuente oficial primaria o institucional |
| `GUIA-PRACTICA` | Síntesis educativa que debe adaptarse al caso concreto |
| `SECTORIAL` | Aplica solo si la actividad cae en ese sector |
| `DINAMICO` | Tasa, plazo, convocatoria o norma en transición que debe revisarse a la fecha de ejecución |

---

[← Inicio](README.md) · [Glosario maestro](docs/19_GLOSSARY.md) · [Estado verificable](STATUS.md)
"""


def render_glosario(curriculo: list[dict], packs: dict, especificas: dict) -> str:
    """Glosario maestro construido desde los conceptos de las 336 clases."""
    entradas: dict[str, dict] = {}
    for clase in curriculo:
        spec = especificas[clase["global_class"]]
        for termino, definicion in spec["conceptos"]:
            registro = entradas.setdefault(
                termino, {"definicion": definicion, "clases": [], "partes": set()}
            )
            registro["clases"].append(clase)
            registro["partes"].add(clase["part"])

    por_letra: dict[str, list] = {}
    for termino in sorted(entradas, key=lambda t: (unicodedata.normalize("NFKD", t.lower()), t)):
        inicial = unicodedata.normalize("NFKD", termino[0].upper())[0]
        por_letra.setdefault(inicial, []).append(termino)

    indice = " · ".join(f"[{letra}](#{letra.lower()})" for letra in sorted(por_letra))

    secciones = []
    for letra in sorted(por_letra):
        filas = []
        for termino in por_letra[letra]:
            registro = entradas[termino]
            primera = registro["clases"][0]
            ruta = (
                f"../curriculum/{ruta_parte(primera['part'], primera['part_title']).name}/"
                f"{ruta_clase(primera).name}/README.md"
            )
            referencia = f"[{primera['global_class']:03d}]({ruta})"
            otras = len(registro["clases"]) - 1
            if otras:
                referencia += f" +{otras}"
            filas.append(
                f"| **{termino}** | {registro['definicion'].capitalize()}. | {referencia} |"
            )
        secciones.append(
            f"### {letra}\n\n| Concepto | Definición operacional | Clase |\n|---|---|---|\n"
            + "\n".join(filas)
        )

    cuerpo = "\n\n".join(secciones)
    partes_glosario = "\n".join(
        f"| {p:02d} | [{packs[p]['titulo']}]"
        f"(../curriculum/{ruta_parte(p, packs[p]['titulo']).name}/README.md#-glosario-de-la-parte) |"
        for p in sorted(packs)
    )

    return f"""# Glosario maestro

{len(entradas)} conceptos con definición operacional, extraídos de las {len(curriculo)} clases del
programa. Este archivo **se genera**: cada término proviene de la tabla «Conceptos centrales» de
la clase donde se introduce, de modo que la definición del glosario y la de la clase nunca
divergen.

La columna **Clase** enlaza a la clase donde el concepto se introduce; `+n` indica en cuántas
clases adicionales vuelve a aparecer.

**Índice alfabético:** {indice}

## Términos

{cuerpo}

## Glosarios por parte

Cada parte reúne además los conceptos de sus propias clases:

| # | Parte |
|---:|---|
{partes_glosario}

---

[← Inicio](../README.md) · [Currículo](../CURRICULUM.md) · [Catálogo de fuentes](16_OFFICIAL_SOURCE_CATALOG.md)
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="no escribe; falla si hay archivos desactualizados")
    args = parser.parse_args()

    curriculo, packs, fuentes, especificas = cargar_datos()
    for parte, pack in packs.items():
        pack["_total_clases"] = sum(1 for c in curriculo if c["part"] == parte)
        pack["diagrama_render"] = "```mermaid\n" + pack["diagrama"] + "\n```"

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
        pendientes.append((
            ruta_parte(parte, pack["titulo"]) / "README.md",
            render_parte(pack, clases, especificas, fuentes,
                         packs.get(parte - 1), packs.get(parte + 1)),
        ))

    pendientes.append((RAIZ / "CURRICULUM.md", render_curriculum(curriculo, packs)))
    pendientes.append((RAIZ / "docs" / "19_GLOSSARY.md",
                       render_glosario(curriculo, packs, especificas)))

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
