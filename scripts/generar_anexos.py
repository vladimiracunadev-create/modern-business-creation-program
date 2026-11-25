#!/usr/bin/env python3
"""Genera figuras, navegación, índice y tabla del README de los anexos desde `manifests/anexos.json`.

Los anexos (`annexes/*.md`) se redactan a mano. Del manifiesto salen: sus figuras SVG (mismo motor que
los modelos mentales de las clases), el bloque de navegación y «En 60 segundos» de cada anexo, el cierre
«Para seguir leyendo», el índice `annexes/README.md` y la tabla del README principal.

    python scripts/generar_anexos.py          # escribe todo
    python scripts/generar_anexos.py --check  # falla si algo no coincide con el manifiesto
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from svg_modelos import dibujar_figura  # noqa: E402

MANIFIESTO = RAIZ / "manifests" / "anexos.json"
SALIDA = RAIZ / "annexes" / "img"

ACENTOS_GRUPO = {
    "personas": "#2E8B57", "sociedades-personas": "#2563EB", "sociedades-capital": "#7C3AED",
    "especial": "#C2410C", "otras": "#0F766E", "tramites": "#374151", "estrategia": "#B45309",
}
GRUPOS = {
    "personas": "Sin sociedad", "sociedades-personas": "Sociedades de personas",
    "sociedades-capital": "Sociedades de capital", "especial": "Régimen especial",
    "otras": "Otras formas", "tramites": "Trámites e instituciones",
    "estrategia": "Decisiones estratégicas",
}

FILAS_MATRIZ = [
    ("01", "Persona natural", "1", "Ilimitada: todos sus bienes", "No aplica (inicio de actividades en el SII)", "Probar un negocio o ejercer una profesión"),
    ("02", "EIRL", "1 persona natural", "Limitada al patrimonio de la empresa, con cinco excepciones", "Sí", "Negocio individual estable"),
    ("03", "Sociedad limitada", "2 a 50", "Limitada a los aportes", "Sí", "Pymes y empresas familiares cerradas"),
    ("04", "Colectiva comercial", "2 o más", "Solidaria e ilimitada", "Sí", "Casos muy particulares; derecho supletorio"),
    ("05", "Comandita", "Gestores y comanditarios", "Gestores ilimitada; comanditarios hasta su aporte", "Sí", "Poco usada; capital pasivo con un gestor"),
    ("06", "SpA", "1 o más", "Limitada a los aportes", "Sí", "Startups y pymes con inversionistas"),
    ("07", "Anónima cerrada", "Varios", "Limitada a los aportes", "Sí", "Empresas medianas con gobierno institucional"),
    ("08", "Anónima abierta", "Público", "Limitada a los aportes", "No (se inscribe en el Registro de Valores)", "Captar capital en el mercado"),
    ("09", "Cooperativa", "5 o más", "Limitada a las cuotas", "No (junta constitutiva y escritura)", "Socios que son también usuarios o trabajadores"),
    ("10", "Garantía recíproca", "Accionistas beneficiarios", "Limitada a los aportes", "Sí (la S.A.G.R.)", "Afianzar a pymes sin garantías"),
    ("11", "Sociedad civil", "2 o más", "A prorrata, no solidaria", "No", "Actividades no mercantiles"),
    ("12", "Asociación o fundación", "Asociados o fundador", "De la entidad, sin reparto de utilidades", "No (Registro Nacional)", "Fines sociales, culturales o comunitarios"),
    ("14", "Sucursal extranjera", "La matriz extranjera", "Ilimitada de la matriz", "No (protocolización y extracto)", "Operar en Chile sin crear una filial"),
]
RUTAS = [
    ("Voy a partir solo y con poco riesgo", "01, luego 02 si el riesgo crece"),
    ("Quiero limitar mi responsabilidad siendo único dueño", "02 o 06"),
    ("Tengo uno o varios socios y puede entrar inversión", "06; compara con 03 y 07"),
    ("Somos pocos, nos conocemos y no habrá inversión", "03"),
    ("Mi proyecto es social, cultural o comunitario", "12; si el reparto es por uso, 09"),
    ("Una empresa extranjera quiere operar en Chile", "14 o una filial (06 o 07)"),
    ("Ya elegí el tipo y quiero constituirla", "15, 16 y 17"),
    ("Soy pyme y busco trámites más simples", "13, 17 y 16"),
    ("Necesito una dirección: oficina virtual, coworking, casa o local", "18, luego 16 y 17"),
    ("Tengo socios y quiero acordar reglas antes de un conflicto", "19, con 03, 06 o 07"),
    ("Quiero transformar, fusionar, dividir, vender o cerrar mi empresa", "20, luego 16 y 15"),
    ("No puedo pagar mis deudas y necesito entender mis opciones", "21 y la guía de crisis; abogado de insolvencia"),
]

NAV_INICIO = "<!-- anexos:nav-inicio -->"
NAV_FIN = "<!-- anexos:nav-fin -->"
CIERRE_INICIO = "<!-- anexos:cierre-inicio -->"
CIERRE_FIN = "<!-- anexos:cierre-fin -->"
TABLA_INICIO = "<!-- anexos:tabla-inicio -->"
TABLA_FIN = "<!-- anexos:tabla-fin -->"


def cargar() -> list[dict]:
    return json.loads(MANIFIESTO.read_text(encoding="utf-8"))


def leer(ruta: Path) -> str:
    return ruta.read_text(encoding="utf-8").replace("\r\n", "\n")


def archivos_por_numero() -> dict[int, Path]:
    return {int(p.name[:2]): p for p in (RAIZ / "annexes").glob("[0-9][0-9]-*.md")}


def esperados() -> dict[Path, str]:
    salida: dict[Path, str] = {}
    for anexo in cargar():
        acento = ACENTOS_GRUPO[anexo["grupo"]]
        for k, fig in enumerate(anexo["figuras"], start=1):
            rotulo = f"Anexo {anexo['n']:02d} · {anexo['titulo']}"
            salida[SALIDA / f"{anexo['slug']}-{k}.svg"] = dibujar_figura(anexo["n"], rotulo, acento, fig)
    return salida


def barra(anexos: list, i: int, archivos: dict) -> str:
    ant = anexos[i - 1] if i > 0 else None
    sig = anexos[i + 1] if i < len(anexos) - 1 else None
    izq = f"[← {ant['n']:02d}. {ant['titulo']}]({archivos[ant['n']].name})" if ant else "—"
    der = f"[{sig['n']:02d}. {sig['titulo']} →]({archivos[sig['n']].name})" if sig else "—"
    return f"{izq} · [Índice de anexos](README.md) · {der}"


def bloque_inicio(anexos: list, i: int, archivos: dict) -> str:
    puntos = "\n".join(f"- {x}" for x in anexos[i]["resumen"])
    return (f"{NAV_INICIO}\n\n**Navegación:** {barra(anexos, i, archivos)}\n\n"
            f"## En 60 segundos\n\n{puntos}\n\n{NAV_FIN}")


def bloque_cierre(anexos: list, i: int, archivos: dict) -> str:
    titulos = {x["n"]: x["titulo"] for x in anexos}
    rel = "\n".join(f"- [Anexo {n:02d}. {titulos[n]}]({archivos[n].name}): {motivo}."
                    for n, motivo in anexos[i]["relacionados"])
    return (f"{CIERRE_INICIO}\n\n## Para seguir leyendo\n\n{rel}\n\n"
            f"**Navegación:** {barra(anexos, i, archivos)}\n\n{CIERRE_FIN}")


def reemplazar(texto: str, ini: str, fin: str, bloque: str, tras_aviso: bool) -> str:
    patron = re.compile(re.escape(ini) + r".*?" + re.escape(fin), re.S)
    if patron.search(texto):
        return patron.sub(lambda _m: bloque, texto, count=1)
    if not tras_aviso:
        return texto.rstrip("\n") + "\n\n" + bloque + "\n"
    m = re.search(r"\n(?:> [^\n]*\n)+", texto)
    pos = m.end() if m else texto.index("\n") + 1
    return texto[:pos] + "\n" + bloque + "\n" + texto[pos:]


def textos_anexos() -> dict[Path, str]:
    anexos = cargar()
    archivos = archivos_por_numero()
    salida: dict[Path, str] = {}
    for i, a in enumerate(anexos):
        ruta = archivos[a["n"]]
        txt = leer(ruta)
        txt = reemplazar(txt, NAV_INICIO, NAV_FIN, bloque_inicio(anexos, i, archivos), True)
        txt = reemplazar(txt, CIERRE_INICIO, CIERRE_FIN, bloque_cierre(anexos, i, archivos), False)
        salida[ruta] = txt
    return salida


def palabras(txt: str) -> int:
    return len(re.findall(r"\w+", txt))


def texto_indice(textos: dict[Path, str]) -> str:
    anexos = cargar()
    archivos = archivos_por_numero()
    filas = []
    for a in anexos:
        w = f"{palabras(textos[archivos[a['n']]]):,}".replace(",", ".")
        filas.append(f"| {a['n']:02d} | [{a['titulo']}]({archivos[a['n']].name}) | {a['descripcion']} | {GRUPOS[a['grupo']]} | {w} |")
    matriz = "\n".join("| " + " | ".join(f) + " |" for f in FILAS_MATRIZ)
    rutas = "\n".join(f"| {q} | {r} |" for q, r in RUTAS)
    indice = "\n".join(filas)
    return f"""# Anexos: tipos de empresa, Empresa en un Día, SII y municipalidades

Los anexos profundizan lo que las clases solo pueden introducir. Cada uno tiene **más de 5.000
palabras**, un resumen «En 60 segundos», figuras SVG propias, fuentes con enlace oficial, una lista de
verificación «antes de construir», preguntas frecuentes y enlaces para seguir con el anexo siguiente sin
volver a este índice. Son material educativo, no asesoría legal ni tributaria: confirma cada dato en la
fuente citada y en el texto vigente de la ley.

## Cómo leer un anexo

1. **En 60 segundos:** cinco ideas para decidir si el anexo te interesa.
2. **Ficha rápida, historia, marco legal y constitución:** de dónde viene y qué exige la ley.
3. **Capital, gobierno, responsabilidad y tributación:** el corazón de la decisión.
4. **Antes de construir:** lista de verificación y un caso trabajado.
5. **Preguntas frecuentes, fuentes y «Para seguir leyendo»:** respuestas cortas con el artículo que las respalda.

## ¿Por dónde empiezo?

| Si tu situación es… | Lee… |
|---|---|
{rutas}

## Índice

| N.º | Anexo | Qué encontrarás | Grupo | Palabras |
|---:|---|---|---|---:|
{indice}

## Matriz comparativa de las formas jurídicas

| Anexo | Forma | Dueños | Responsabilidad | Registro en línea (Ley 20.659) | Uso típico |
|---|---|---|---|---|---|
{matriz}

El Estatuto Pyme (anexo 13) no es una forma jurídica: se superpone a cualquiera según el tamaño de la
empresa.

## Lo que dice y lo que no dice este material

- Cita artículos que se leyeron en el texto de la Biblioteca del Congreso Nacional (fecha de consulta
  en cada anexo). Cuando un texto remite a un artículo derogado o a una unidad histórica, lo señala.
- Los números de los ejemplos son **ilustrativos**.
- No incluye tarifas de notarías, aranceles ni plazos de terceros: cambian y deben consultarse en la
  fuente.
- No existe en Chile, a la fecha de consulta, una ley de sociedades de beneficio e interés colectivo
  (BIC); por eso no hay un anexo sobre ese tipo.
"""


def texto_tabla_readme() -> str:
    archivos = archivos_por_numero()
    filas = "\n".join(f"| {a['n']:02d} | [{a['titulo']}](annexes/{archivos[a['n']].name}) | {a['descripcion']} |"
                      for a in cargar())
    return f"{TABLA_INICIO}\n| N.º | Anexo | Qué encontrarás |\n|---:|---|---|\n{filas}\n{TABLA_FIN}"


def texto_readme() -> str:
    txt = leer(RAIZ / "README.md")
    bloque = texto_tabla_readme()
    patron = re.compile(re.escape(TABLA_INICIO) + r".*?" + re.escape(TABLA_FIN), re.S)
    if patron.search(txt):
        return patron.sub(lambda _m: bloque, txt, count=1)
    viejo = re.compile(r"\| N\.º \| Anexo \|\n\|---:\|---\|\n(?:\| \d\d \|[^\n]*\n)+")
    if not viejo.search(txt):
        raise SystemExit("No se encontró la tabla de anexos del README principal.")
    return viejo.sub(lambda _m: bloque + "\n", txt, count=1)


def main() -> int:
    pendientes = esperados()
    anexos = textos_anexos()
    indice, readme = texto_indice(anexos), texto_readme()
    if "--check" in sys.argv:
        malos = [
            p.relative_to(RAIZ).as_posix() for p, svg in pendientes.items()
            if not p.exists() or p.read_text(encoding="utf-8") != svg
        ]
        malos += [r.relative_to(RAIZ).as_posix() for r, txt in anexos.items() if leer(r) != txt]
        if leer(RAIZ / "annexes" / "README.md") != indice:
            malos.append("annexes/README.md")
        if leer(RAIZ / "README.md") != readme:
            malos.append("README.md")
        sobrantes = [
            p.relative_to(RAIZ).as_posix() for p in SALIDA.glob("*.svg") if p not in pendientes
        ] if SALIDA.exists() else []
        if malos or sobrantes:
            print(f"FALLÓ: {len(malos)} archivo(s) desincronizado(s), {len(sobrantes)} sobrante(s).")
            for m in (malos + sobrantes)[:20]:
                print(f"  - {m}")
            return 1
        print(f"OK: {len(pendientes)} figuras, navegación, índice y tabla del README sincronizados con el manifiesto")
        return 0
    SALIDA.mkdir(parents=True, exist_ok=True)
    for p, svg in pendientes.items():
        p.write_text(svg, encoding="utf-8", newline="\n")
    for ruta, txt in anexos.items():
        ruta.write_text(txt, encoding="utf-8", newline="\n")
    (RAIZ / "annexes" / "README.md").write_text(indice, encoding="utf-8", newline="\n")
    (RAIZ / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    print(f"OK: {len(pendientes)} figuras, navegación, índice y tabla del README generados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
