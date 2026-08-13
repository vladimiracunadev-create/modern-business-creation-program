#!/usr/bin/env python3
"""Genera el sitio estático HTML que se publica en GitHub Pages.

Convierte todo el Markdown del repositorio a HTML autocontenido en `site/`, con
navegación lateral, buscador de clases en cliente y tema claro/oscuro. No requiere
dependencias externas: incluye un conversor Markdown mínimo, suficiente para el
subconjunto que este repositorio usa (encabezados, listas, tablas, citas, código,
enlaces, énfasis y casillas de verificación).

Uso:
  python scripts/generar_sitio.py            # genera site/
  python scripts/generar_sitio.py --check    # solo valida que compile, sin escribir
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SALIDA = RAIZ / "site"

TITULO = "Modern Business Creation Program"
SUBTITULO = "Chile-first · idea → constitución → operación → crecimiento → crisis → salida"
REPO = "https://github.com/vladimiracunadev-create/modern-business-creation-program"

# Directorios cuyo Markdown se publica, en el orden en que aparecen en el menú.
SECCIONES = [
    ("docs", "Manuales transversales"),
    ("case-studies", "Casos de líneas de negocio"),
    ("templates", "Plantillas"),
    ("curriculum", "Currículo"),
]

IGNORADOS = {".git", "node_modules", "site", ".venv", "__pycache__", "scripts"}

# Carpetas que el sitio publica con su propio index.html.
PUBLICADOS = {carpeta for carpeta, _ in SECCIONES}

# El manual se compila aparte con scripts/generar_manual.py; el sitio se genera
# igual sin él, solo que sin la sección de descargas.
MANUALES = RAIZ / "output" / "pdf"
HAY_MANUAL = MANUALES.exists() and any(MANUALES.glob("*.pdf"))
HAY_PARTES = (MANUALES / "partes").exists() and any((MANUALES / "partes").glob("*.pdf"))


# --------------------------------------------------------------------------- #
# Conversor Markdown mínimo
# --------------------------------------------------------------------------- #

EN_LINEA = [
    (re.compile(r"`([^`]+)`"), lambda m: f"<code>{html.escape(m.group(1))}</code>"),
    (re.compile(r"\*\*([^*]+)\*\*"), r"<strong>\1</strong>"),
    (re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)"), r"<em>\1</em>"),
    (re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)"), r'<img src="\2" alt="\1">'),
    (re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)"), r'<a href="\2">\1</a>'),
    (re.compile(r"<((?:https?|mailto):[^>\s]+)>"), r'<a href="\1">\1</a>'),
]

# Marcadores usados para proteger el código en línea mientras se escapa el resto.
CENTINELA = "\x00{}\x00"


def en_linea(texto: str) -> str:
    """Aplica formato en línea escapando el HTML del contenido original."""
    fragmentos: list[str] = []

    def guardar(match: re.Match) -> str:
        fragmentos.append(f"<code>{html.escape(match.group(1))}</code>")
        return CENTINELA.format(len(fragmentos) - 1)

    texto = re.sub(r"`([^`]+)`", guardar, texto)
    texto = html.escape(texto, quote=False)
    # Los README usan <br> en las cabeceras de metadatos; se restituye tras el
    # escape para no publicarlo como texto literal.
    texto = re.sub(r"&lt;br\s*/?&gt;", "<br>", texto)
    for patron, reemplazo in EN_LINEA[1:]:
        texto = patron.sub(reemplazo, texto)
    for indice, fragmento in enumerate(fragmentos):
        texto = texto.replace(CENTINELA.format(indice), fragmento)
    return texto


# Enlace markdown admitiendo un nivel de anidamiento en el texto, que es lo que
# necesitan los badges de la portada: [![alt](imagen)](destino).
ENLACE_MD = re.compile(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(([^)\s]+)\)")


def convertir_enlaces(texto: str, carpeta: Path) -> str:
    """Adapta los enlaces del Markdown al sitio.

    Los `.md` pasan a `.html`. Los enlaces relativos a archivos que el sitio no
    publica —LICENSE, VERSION, los CSV de `templates/`, los JSON de `manifests/`—
    se redirigen al repositorio, porque dentro del sitio darían 404.
    """
    def reescribir(match: re.Match) -> str:
        texto_enlace, destino = match.group(1), match.group(2)
        if destino.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        ruta, _, ancla = destino.partition("#")
        sufijo = f"#{ancla}" if ancla else ""
        if ruta.endswith(".md"):
            # Los README se publican como index.html de su carpeta, igual que en
            # el generador: enlazarlos como README.html daría 404.
            if ruta.endswith("README.md"):
                return f"[{texto_enlace}]({ruta[:-9]}index.html{sufijo})"
            return f"[{texto_enlace}]({ruta[:-3]}.html{sufijo})"
        if not ruta:
            return match.group(0)
        objetivo = (carpeta / ruta.rstrip("/")).resolve()
        if objetivo.is_dir():
            # Solo las carpetas que el sitio publica tienen index.html; el resto
            # (scripts/, manifests/) se enlazan al árbol del repositorio.
            try:
                seccion = objetivo.relative_to(RAIZ).parts[0]
            except ValueError:
                return match.group(0)
            if seccion in PUBLICADOS:
                return match.group(0)
            return f"[{texto_enlace}]({REPO}/tree/main/{objetivo.relative_to(RAIZ).as_posix()})"
        try:
            relativo = objetivo.relative_to(RAIZ).as_posix()
        except ValueError:
            return match.group(0)
        return f"[{texto_enlace}]({REPO}/blob/main/{relativo}{sufijo})"

    return ENLACE_MD.sub(reescribir, texto)


def ancla(texto: str) -> str:
    limpio = re.sub(r"[^\w\s-]", "", re.sub(r"<[^>]+>", "", texto)).strip().lower()
    return re.sub(r"[\s_]+", "-", limpio)


def markdown_a_html(fuente: str, carpeta: Path) -> str:
    """Conversor acotado al subconjunto de Markdown que usa este repositorio."""
    fuente = convertir_enlaces(fuente, carpeta)
    lineas = fuente.split("\n")
    salida: list[str] = []
    indice = 0
    pila_listas: list[str] = []

    def cerrar_listas(nivel: int = 0) -> None:
        while len(pila_listas) > nivel:
            salida.append(f"</{pila_listas.pop()}>")

    while indice < len(lineas):
        linea = lineas[indice]
        despojada = linea.strip()

        if despojada.startswith("```"):
            cerrar_listas()
            lenguaje = despojada[3:].strip()
            cuerpo: list[str] = []
            indice += 1
            while indice < len(lineas) and not lineas[indice].strip().startswith("```"):
                cuerpo.append(lineas[indice])
                indice += 1
            fuente_bloque = html.escape(chr(10).join(cuerpo))
            if lenguaje.lower() == "mermaid":
                # El diagrama se entrega como <pre class="mermaid"> para que la
                # librería lo transforme en el navegador. Si no carga, queda un
                # bloque de código legible en vez de una caja vacía.
                salida.append(f'<pre class="mermaid">{fuente_bloque}</pre>')
            else:
                clase = f' class="lang-{html.escape(lenguaje)}"' if lenguaje else ""
                salida.append(f"<pre><code{clase}>{fuente_bloque}</code></pre>")
            indice += 1
            continue

        if not despojada:
            cerrar_listas()
            indice += 1
            continue

        encabezado = re.match(r"^(#{1,6})\s+(.*)$", despojada)
        if encabezado:
            cerrar_listas()
            nivel = len(encabezado.group(1))
            contenido = en_linea(encabezado.group(2))
            salida.append(f'<h{nivel} id="{ancla(encabezado.group(2))}">{contenido}</h{nivel}>')
            indice += 1
            continue

        # HTML de bloque escrito a mano (el README usa <div align="center"> para la
        # portada). Se deja pasar tal cual en vez de escaparlo como texto.
        if re.match(r"^</?(div|p|br|img|table|details|summary|section)\b", despojada, re.I):
            cerrar_listas()
            salida.append(despojada)
            indice += 1
            continue

        if despojada.startswith(">"):
            cerrar_listas()
            cita: list[str] = []
            while indice < len(lineas) and lineas[indice].strip().startswith(">"):
                cita.append(lineas[indice].strip().lstrip(">").strip())
                indice += 1
            # Alertas de GitHub: > [!NOTE] / [!IMPORTANT] / [!WARNING] / [!TIP] / [!CAUTION].
            alerta = re.match(r"^\[!(\w+)\]\s*(.*)$", cita[0]) if cita else None
            if alerta:
                etiqueta = alerta.group(1).capitalize()
                cita[0] = alerta.group(2)
                cuerpo = en_linea(" ".join(c for c in cita if c))
                salida.append(
                    f'<blockquote class="alerta alerta-{alerta.group(1).lower()}">'
                    f"<p><strong>{etiqueta}</strong></p><p>{cuerpo}</p></blockquote>"
                )
            else:
                salida.append(f"<blockquote><p>{en_linea(' '.join(cita))}</p></blockquote>")
            continue

        if despojada.startswith("|") and indice + 1 < len(lineas) \
                and re.match(r"^\|[\s:|-]+\|$", lineas[indice + 1].strip()):
            cerrar_listas()
            def celdas(fila: str) -> list[str]:
                return [c.strip() for c in fila.strip().strip("|").split("|")]

            cabecera = celdas(lineas[indice])
            indice += 2
            filas: list[list[str]] = []
            while indice < len(lineas) and lineas[indice].strip().startswith("|"):
                filas.append(celdas(lineas[indice]))
                indice += 1
            th = "".join(f"<th>{en_linea(c)}</th>" for c in cabecera)
            tbody = "".join(
                "<tr>" + "".join(f"<td>{en_linea(c)}</td>" for c in fila) + "</tr>"
                for fila in filas
            )
            salida.append(
                f'<div class="tabla"><table><thead><tr>{th}</tr></thead>'
                f"<tbody>{tbody}</tbody></table></div>"
            )
            continue

        if re.match(r"^[-*+]\s+|^\d+[.)]\s+", despojada):
            sangria = len(linea) - len(linea.lstrip())
            nivel = sangria // 2 + 1
            etiqueta = "ul" if re.match(r"^[-*+]\s", despojada) else "ol"
            while len(pila_listas) > nivel:
                salida.append(f"</{pila_listas.pop()}>")
            if len(pila_listas) < nivel:
                salida.append(f"<{etiqueta}>")
                pila_listas.append(etiqueta)
            contenido = re.sub(r"^[-*+]\s+|^\d+[.)]\s+", "", despojada)
            casilla = re.match(r"^\[([ xX])\]\s*(.*)$", contenido)
            if casilla:
                marcado = " checked" if casilla.group(1).lower() == "x" else ""
                salida.append(
                    f'<li class="tarea"><input type="checkbox" disabled{marcado}> '
                    f"{en_linea(casilla.group(2))}</li>"
                )
            else:
                salida.append(f"<li>{en_linea(contenido)}</li>")
            indice += 1
            continue

        if set(despojada) <= {"-"} and len(despojada) >= 3:
            cerrar_listas()
            salida.append("<hr>")
            indice += 1
            continue

        cerrar_listas()
        parrafo: list[str] = []
        while indice < len(lineas) and lineas[indice].strip() and \
                not re.match(r"^(#{1,6}\s|>|\||```|[-*+]\s|\d+[.)]\s|---|</?(div|p|br|img|table|details|summary|section)\b)",
                             lineas[indice].strip(), re.I):
            parrafo.append(lineas[indice].strip())
            indice += 1
        if parrafo:
            salida.append(f"<p>{en_linea(' '.join(parrafo))}</p>")
        else:
            indice += 1

    cerrar_listas()
    return "\n".join(salida)


# --------------------------------------------------------------------------- #
# Plantilla del sitio
# --------------------------------------------------------------------------- #

ESTILOS = """
*,*::before,*::after{box-sizing:border-box}
:root{
  --fondo:#ffffff;--fondo-2:#f5f7fa;--texto:#12181f;--tenue:#5a6572;
  --borde:#dfe4ea;--acento:#0b62d0;--acento-suave:#e8f0fc;--codigo:#f2f4f7;
  --sombra:0 1px 2px rgba(16,24,40,.06),0 8px 24px rgba(16,24,40,.06);
}
@media (prefers-color-scheme:dark){:root:not([data-tema="claro"]){
  --fondo:#0e1116;--fondo-2:#161b22;--texto:#e7edf5;--tenue:#9aa7b6;
  --borde:#242c37;--acento:#5aa2ff;--acento-suave:#132339;--codigo:#161b22;
  --sombra:0 1px 2px rgba(0,0,0,.4),0 8px 24px rgba(0,0,0,.35);
}}
:root[data-tema="oscuro"]{
  --fondo:#0e1116;--fondo-2:#161b22;--texto:#e7edf5;--tenue:#9aa7b6;
  --borde:#242c37;--acento:#5aa2ff;--acento-suave:#132339;--codigo:#161b22;
  --sombra:0 1px 2px rgba(0,0,0,.4),0 8px 24px rgba(0,0,0,.35);
}
html{scroll-behavior:smooth}
body{margin:0;background:var(--fondo);color:var(--texto);
  font:16px/1.65 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  -webkit-text-size-adjust:100%}
a{color:var(--acento);text-decoration:none}
a:hover{text-decoration:underline}
header.superior{position:sticky;top:0;z-index:20;background:var(--fondo);
  border-bottom:1px solid var(--borde);padding:.7rem 1.1rem;
  display:flex;gap:1rem;align-items:center;flex-wrap:wrap}
header.superior .marca{font-weight:700;letter-spacing:-.01em}
header.superior .marca span{color:var(--tenue);font-weight:400;font-size:.85rem;display:block}
header.superior nav{margin-left:auto;display:flex;gap:.9rem;flex-wrap:wrap;font-size:.9rem}
button.tema{background:var(--fondo-2);border:1px solid var(--borde);color:var(--texto);
  border-radius:999px;padding:.3rem .8rem;cursor:pointer;font-size:.85rem}
.envoltura{display:grid;grid-template-columns:290px minmax(0,1fr);gap:2rem;
  max-width:1280px;margin:0 auto;padding:1.6rem 1.1rem 4rem}
aside{position:sticky;top:72px;align-self:start;max-height:calc(100vh - 96px);
  overflow-y:auto;font-size:.9rem;padding-right:.4rem}
aside h2{font-size:.72rem;text-transform:uppercase;letter-spacing:.09em;
  color:var(--tenue);margin:1.3rem 0 .45rem}
aside ul{list-style:none;margin:0;padding:0}
aside li{margin:.12rem 0}
aside a{display:block;padding:.28rem .55rem;border-radius:7px;color:var(--texto)}
aside a:hover{background:var(--fondo-2);text-decoration:none}
aside a.activo{background:var(--acento-suave);color:var(--acento);font-weight:600}
main{min-width:0}
main h1{font-size:1.95rem;line-height:1.2;letter-spacing:-.02em;margin:.2rem 0 1rem}
main h2{font-size:1.3rem;margin:2.1rem 0 .7rem;padding-bottom:.3rem;border-bottom:1px solid var(--borde)}
main h3{font-size:1.05rem;margin:1.5rem 0 .5rem}
main p{margin:.75rem 0}
blockquote{margin:1.1rem 0;padding:.7rem 1rem;background:var(--fondo-2);
  border-left:3px solid var(--acento);border-radius:0 8px 8px 0;color:var(--tenue)}
blockquote p{margin:0}
blockquote p+p{margin-top:.4rem}
blockquote.alerta{border-left-width:4px}
blockquote.alerta>p:first-child{color:var(--acento);text-transform:uppercase;
  font-size:.75rem;letter-spacing:.08em}
blockquote.alerta-warning,blockquote.alerta-caution{border-left-color:#d97706}
blockquote.alerta-warning>p:first-child,blockquote.alerta-caution>p:first-child{color:#d97706}
div[align="center"]{text-align:center}
div[align="center"] h1,div[align="center"] h2{border:none}
div[align="center"] img{display:inline-block;margin:.15rem}
code{background:var(--codigo);padding:.13em .38em;border-radius:5px;
  font:.87em ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
pre{background:var(--codigo);border:1px solid var(--borde);border-radius:10px;
  padding:.9rem 1rem;overflow-x:auto}
pre code{background:none;padding:0}
pre.mermaid{background:var(--fondo-2);border:1px solid var(--borde);border-radius:12px;
  padding:1.1rem;overflow-x:auto;text-align:center;font:.85em ui-monospace,Menlo,Consolas,monospace;
  color:var(--tenue);min-height:3rem}
pre.mermaid[data-processed="true"]{color:inherit;font:inherit}
pre.mermaid svg{max-width:100%;height:auto}
.tabla{overflow-x:auto;margin:1rem 0;border:1px solid var(--borde);border-radius:10px}
table{border-collapse:collapse;width:100%;font-size:.93rem}
th,td{text-align:left;padding:.55rem .75rem;border-bottom:1px solid var(--borde);vertical-align:top}
th{background:var(--fondo-2);font-weight:600;white-space:nowrap}
tbody tr:last-child td{border-bottom:none}
li.tarea{list-style:none;margin-left:-1.2rem}
li.tarea input{margin-right:.45rem}
hr{border:none;border-top:1px solid var(--borde);margin:2rem 0}
img{max-width:100%;height:auto}
.buscador{width:100%;padding:.5rem .75rem;border:1px solid var(--borde);border-radius:9px;
  background:var(--fondo-2);color:var(--texto);font-size:.9rem}
.resultados{margin-top:.6rem;max-height:52vh;overflow-y:auto}
.hero{background:var(--fondo-2);border:1px solid var(--borde);border-radius:14px;
  padding:1.6rem;margin-bottom:1.6rem;box-shadow:var(--sombra)}
.hero h1{margin-top:0}
.cifras{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:.8rem;margin-top:1.2rem}
.cifra{background:var(--fondo);border:1px solid var(--borde);border-radius:11px;padding:.85rem}
.cifra b{display:block;font-size:1.5rem;letter-spacing:-.02em}
.cifra span{color:var(--tenue);font-size:.8rem}
.pastilla{display:inline-block;background:var(--acento-suave);color:var(--acento);
  border-radius:999px;padding:.1rem .6rem;font-size:.75rem;font-weight:600}
footer{border-top:1px solid var(--borde);color:var(--tenue);font-size:.85rem;
  padding:1.4rem 1.1rem;text-align:center}
@media (max-width:900px){
  .envoltura{grid-template-columns:1fr;gap:1rem}
  aside{position:static;max-height:none;border-bottom:1px solid var(--borde);padding-bottom:1rem}
}
"""

GUION_MERMAID = """
// Los diagramas son el único recurso externo del sitio. Se cargan como módulo
// desde un CDN con versión fijada; si la carga falla —red, bloqueo, offline— el
// bloque queda como código legible y el resto de la página funciona igual.
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11.12.0/dist/mermaid.esm.min.mjs';

const raiz = document.documentElement;
const oscuro = () => (raiz.getAttribute('data-tema')
  || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'oscuro' : 'claro')) === 'oscuro';

const pintar = async () => {
  mermaid.initialize({
    startOnLoad: false,
    securityLevel: 'strict',
    theme: oscuro() ? 'dark' : 'default',
    flowchart: { curve: 'basis', useMaxWidth: true },
    fontFamily: 'ui-sans-serif, system-ui, "Segoe UI", Roboto, sans-serif'
  });
  const nodos = document.querySelectorAll('pre.mermaid');
  nodos.forEach(n => {
    if (!n.dataset.fuente) n.dataset.fuente = n.textContent;
    n.innerHTML = n.dataset.fuente;
    n.removeAttribute('data-processed');
  });
  try { await mermaid.run({ nodes: nodos }); } catch (e) { /* queda el código visible */ }
};

pintar();
document.addEventListener('tema-cambiado', pintar);
"""

GUION = """
(function(){
  var raiz=document.documentElement;
  var guardado=null;
  try{guardado=localStorage.getItem('tema');}catch(e){}
  if(guardado){raiz.setAttribute('data-tema',guardado);}
  var boton=document.getElementById('tema');
  if(boton){boton.addEventListener('click',function(){
    var oscuro=window.matchMedia('(prefers-color-scheme: dark)').matches;
    var actual=raiz.getAttribute('data-tema')||(oscuro?'oscuro':'claro');
    var nuevo=actual==='oscuro'?'claro':'oscuro';
    raiz.setAttribute('data-tema',nuevo);
    try{localStorage.setItem('tema',nuevo);}catch(e){}
    document.dispatchEvent(new CustomEvent('tema-cambiado'));
  });}

  var caja=document.getElementById('buscador');
  var lista=document.getElementById('resultados');
  if(!caja||!lista||!window.INDICE)return;
  var base=lista.getAttribute('data-base')||'';
  function pintar(consulta){
    var q=consulta.trim().toLowerCase();
    if(q.length<2){lista.innerHTML='';return;}
    var encontrados=window.INDICE.filter(function(e){
      return e.t.toLowerCase().indexOf(q)>=0||e.p.toLowerCase().indexOf(q)>=0;
    }).slice(0,40);
    if(!encontrados.length){lista.innerHTML='<p style="color:var(--tenue)">Sin resultados.</p>';return;}
    lista.innerHTML='<ul>'+encontrados.map(function(e){
      return '<li><a href="'+base+e.u+'">'+e.n+'. '+e.t+'</a></li>';
    }).join('')+'</ul>';
  }
  caja.addEventListener('input',function(){pintar(caja.value);});
})();
"""


def pagina(titulo: str, cuerpo: str, base: str, menu: str) -> str:
    """Arma una página del sitio.

    Los estilos, el guion y el índice de búsqueda van en archivos aparte bajo
    `assets/`: embebidos, el índice de las 336 clases se repetiría en cada una de
    las 419 páginas y el sitio pasaría de ~2 MB a ~40 MB.
    """
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(titulo)} · {html.escape(TITULO)}</title>
<meta name="description" content="{html.escape(SUBTITULO)}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><text y='26' font-size='26'>🏛️</text></svg>">
<link rel="stylesheet" href="{base}assets/estilos.css">
</head>
<body>
<header class="superior">
  <div class="marca"><a href="{base}index.html" style="color:inherit">{html.escape(TITULO)}</a>
  <span>{html.escape(SUBTITULO)}</span></div>
  <nav>
    <a href="{base}CURRICULUM.html">Currículo</a>
    <a href="{base}docs/00_MASTER_FLOW.html">Flujo maestro</a>
    <a href="{base}case-studies/">Casos</a>
    <a href="{REPO}">GitHub</a>
    <button class="tema" id="tema" type="button">Tema</button>
  </nav>
</header>
<div class="envoltura">
<aside>
  <input class="buscador" id="buscador" type="search" placeholder="Buscar entre las 336 clases…" aria-label="Buscar clases">
  <div class="resultados" id="resultados" data-base="{base}"></div>
  {menu}
</aside>
<main>
{cuerpo}
</main>
</div>
<footer>
  Material educativo · no constituye asesoría legal, tributaria, contable ni laboral ·
  <a href="{REPO}">código fuente</a>
</footer>
<script src="{base}assets/indice.js"></script>
<script src="{base}assets/sitio.js"></script>
<script type="module" src="{base}assets/diagramas.js"></script>
</body>
</html>
"""


# --------------------------------------------------------------------------- #
# Construcción
# --------------------------------------------------------------------------- #

def recolectar() -> list[Path]:
    documentos = [p for p in RAIZ.glob("*.md")]
    for carpeta, _ in SECCIONES:
        documentos += sorted((RAIZ / carpeta).rglob("*.md"))
    return [
        p for p in documentos
        if not any(parte in IGNORADOS for parte in p.relative_to(RAIZ).parts)
    ]


def construir_menu(curriculo: list[dict], packs: list[dict], base: str) -> str:
    raiz_docs = sorted((RAIZ / "docs").glob("*.md"))
    enlaces_docs = "".join(
        f'<li><a href="{base}docs/{p.stem}.html">{p.stem.split("_", 1)[1].replace("_", " ").title()}</a></li>'
        for p in raiz_docs
    )
    partes = "".join(
        f'<li><a href="{base}curriculum/{carpeta}/index.html">'
        f'{pack["part"]:02d}. {html.escape(pack["titulo"])}</a></li>'
        for pack, carpeta in packs
    )
    # El bloque de descargas solo aparece si el manual ya fue compilado. En el
    # job de CI que solo construye el sitio no existe, y enlazarlo igual dejaría
    # 336 enlaces rotos en el propio verificador.
    descargas = ""
    if HAY_MANUAL:
        version = (RAIZ / "VERSION").read_text(encoding="utf-8").strip()
        enlace_partes = (
            f'\n  <li><a href="{base}downloads/partes/">📄 PDF por parte</a></li>'
            if HAY_PARTES else ""
        )
        descargas = f"""
<h2>Descargas</h2>
<ul>
  <li><a href="{base}downloads/modern-business-creation-program-manual-v{version}.pdf">📕 Manual completo (PDF)</a></li>{enlace_partes}
</ul>"""
    return f"""{descargas}
<h2>Programa</h2>
<ul>
  <li><a href="{base}index.html">Inicio</a></li>
  <li><a href="{base}docs/19_GLOSSARY.html">Glosario maestro</a></li>
  <li><a href="{base}CURRICULUM.html">Currículo completo</a></li>
  <li><a href="{base}ROADMAP.html">Roadmap</a></li>
  <li><a href="{base}STATUS.html">Estado verificable</a></li>
  <li><a href="{base}CONTRIBUTING.html">Contribuir</a></li>
  <li><a href="{base}SECURITY.html">Seguridad</a></li>
</ul>
<h2>Manuales</h2>
<ul>{enlaces_docs}</ul>
<h2>Las 24 partes</h2>
<ul>{partes}</ul>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="valida sin escribir en disco")
    args = parser.parse_args()

    curriculo = json.loads((RAIZ / "manifests" / "curriculum.json").read_text(encoding="utf-8"))
    packs_raw = json.loads((RAIZ / "manifests" / "part_packs.json").read_text(encoding="utf-8"))

    carpetas_parte = {}
    for carpeta in sorted((RAIZ / "curriculum").glob("part-*")):
        carpetas_parte[int(carpeta.name.split("-")[1])] = carpeta.name
    packs = [(p, carpetas_parte[p["part"]]) for p in packs_raw]

    documentos = recolectar()

    indice_busqueda = []
    for clase in curriculo:
        carpeta = carpetas_parte[clase["part"]]
        subcarpeta = next(
            d.name for d in (RAIZ / "curriculum" / carpeta).iterdir()
            if d.is_dir() and d.name.startswith(f"class-{clase['class']:02d}-")
        )
        indice_busqueda.append({
            "n": f"{clase['global_class']:03d}",
            "t": clase["title"],
            "p": clase["part_title"],
            "u": f"curriculum/{carpeta}/{subcarpeta}/index.html",
        })
    indice_json = json.dumps(indice_busqueda, ensure_ascii=False, separators=(",", ":"))

    paginas: list[tuple[Path, str]] = []

    for documento in documentos:
        relativo = documento.relative_to(RAIZ)
        if documento.name == "README.md" and relativo.parent != Path("."):
            destino = SALIDA / relativo.parent / "index.html"
        elif documento.name == "README.md":
            destino = SALIDA / "index.html"
        else:
            destino = SALIDA / relativo.with_suffix(".html")

        profundidad = len(destino.relative_to(SALIDA).parts) - 1
        base = "../" * profundidad
        fuente = documento.read_text(encoding="utf-8")
        titulo_match = re.search(r"^#\s+(.*)$", fuente, re.M)
        titulo = titulo_match.group(1) if titulo_match else documento.stem

        cuerpo = markdown_a_html(fuente, documento.parent)
        if destino.name == "index.html" and profundidad == 0:
            cuerpo = f'<div class="hero">{cuerpo}</div>'

        paginas.append((
            destino,
            pagina(re.sub(r"<[^>]+>", "", titulo), cuerpo, base,
                   construir_menu(curriculo, packs, base)),
        ))

    if args.check:
        total = sum(len(contenido) for _, contenido in paginas)
        print(f"OK: {len(paginas)} páginas compilan correctamente ({total // 1024} KB).")
        return 0

    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    SALIDA.mkdir(parents=True)
    (SALIDA / ".nojekyll").write_text("", encoding="utf-8")

    # El manual en PDF se compila aparte con scripts/generar_manual.py y vive en
    # output/; aquí solo se copia a las descargas del sitio si ya está generado.
    if HAY_MANUAL:
        destino_descargas = SALIDA / "downloads"
        for pdf in sorted(MANUALES.rglob("*.pdf")):
            copia = destino_descargas / pdf.relative_to(MANUALES)
            copia.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(pdf, copia)

    activos = SALIDA / "assets"
    activos.mkdir()
    (activos / "estilos.css").write_text(ESTILOS.strip() + "\n", encoding="utf-8")
    (activos / "sitio.js").write_text(GUION.strip() + "\n", encoding="utf-8")
    (activos / "diagramas.js").write_text(GUION_MERMAID.strip() + "\n", encoding="utf-8")
    (activos / "indice.js").write_text(
        f"window.INDICE={indice_json};\n", encoding="utf-8"
    )

    for destino, contenido in paginas:
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(contenido, encoding="utf-8")

    # Índice navegable de los PDF por parte: sin él, /downloads/partes/ da 404.
    partes_pdf = sorted((SALIDA / "downloads" / "partes").glob("*.pdf"))
    if partes_pdf:
        filas = "".join(
            f'<li><a href="{p.name}">{p.stem.replace("manual-part-", "Parte ").replace("-", " ")}</a>'
            f' <span style="color:var(--tenue)">· {p.stat().st_size // 1024} KB</span></li>'
            for p in partes_pdf
        )
        (SALIDA / "downloads" / "partes" / "index.html").write_text(
            pagina("PDF por parte",
                   f"<h1>📄 PDF por parte</h1><p>Cada parte del programa como documento "
                   f"independiente, con portada, índice y sus 14 clases.</p><ul>{filas}</ul>",
                   "../../", construir_menu(curriculo, packs, "../../")),
            encoding="utf-8",
        )

    # Redirección desde la ruta corta de casos y plantillas.
    for carpeta in ("case-studies", "templates", "docs", "curriculum"):
        indice = SALIDA / carpeta / "index.html"
        if indice.exists():
            continue
        enlaces = "".join(
            f'<li><a href="{p.relative_to(SALIDA / carpeta).as_posix()}">{p.stem}</a></li>'
            for p in sorted((SALIDA / carpeta).glob("*.html"))
        )
        indice.parent.mkdir(parents=True, exist_ok=True)
        indice.write_text(
            pagina(carpeta, f"<h1>{carpeta}</h1><ul>{enlaces}</ul>", "../",
                   construir_menu(curriculo, packs, "../")),
            encoding="utf-8",
        )

    rotos = verificar_enlaces()
    if rotos:
        print(f"FALLÓ: {len(rotos)} destino(s) internos rotos en el sitio generado:")
        for destino, veces in sorted(rotos.items(), key=lambda x: -x[1])[:20]:
            print(f"  {veces}x  {destino}")
        return 1

    print(f"OK: sitio generado en site/ con {len(paginas)} páginas y sin enlaces internos rotos.")
    return 0


def verificar_enlaces() -> dict[str, int]:
    """Recorre el HTML emitido y devuelve los destinos internos que no existen."""
    rotos: dict[str, int] = {}
    for archivo in SALIDA.rglob("*.html"):
        texto = archivo.read_text(encoding="utf-8")
        for destino in re.findall(r'(?:href|src)="([^"]+)"', texto):
            if destino.startswith(("http://", "https://", "mailto:", "data:", "#")):
                continue
            objetivo = (archivo.parent / destino.partition("#")[0]).resolve()
            if objetivo.is_dir():
                objetivo = objetivo / "index.html"
            if not objetivo.exists():
                rotos[destino] = rotos.get(destino, 0) + 1
    return rotos


if __name__ == "__main__":
    sys.exit(main())
