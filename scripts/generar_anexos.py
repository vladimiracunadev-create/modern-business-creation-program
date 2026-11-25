#!/usr/bin/env python3
"""Genera las figuras SVG de los anexos desde `manifests/anexos.json`.

Los anexos (`annexes/*.md`) se redactan a mano; sus figuras salen de este
manifiesto con el mismo motor que los modelos mentales de las clases.

    python scripts/generar_anexos.py          # escribe annexes/img/*.svg
    python scripts/generar_anexos.py --check  # falla si algún SVG no coincide
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from svg_modelos import dibujar_figura  # noqa: E402

MANIFIESTO = RAIZ / "manifests" / "anexos.json"
SALIDA = RAIZ / "annexes" / "img"

ACENTOS_GRUPO = {
    "personas": "#2E8B57", "sociedades-personas": "#2563EB", "sociedades-capital": "#7C3AED",
    "especial": "#C2410C", "otras": "#0F766E", "tramites": "#374151",
}


def esperados() -> dict[Path, str]:
    anexos = json.loads(MANIFIESTO.read_text(encoding="utf-8"))
    salida: dict[Path, str] = {}
    for anexo in anexos:
        acento = ACENTOS_GRUPO[anexo["grupo"]]
        for k, fig in enumerate(anexo["figuras"], start=1):
            rotulo = f"Anexo {anexo['n']:02d} · {anexo['titulo']}"
            salida[SALIDA / f"{anexo['slug']}-{k}.svg"] = dibujar_figura(anexo["n"], rotulo, acento, fig)
    return salida


def main() -> int:
    pendientes = esperados()
    if "--check" in sys.argv:
        malos = [
            p.relative_to(RAIZ).as_posix() for p, svg in pendientes.items()
            if not p.exists() or p.read_text(encoding="utf-8") != svg
        ]
        sobrantes = [
            p.relative_to(RAIZ).as_posix() for p in SALIDA.glob("*.svg") if p not in pendientes
        ] if SALIDA.exists() else []
        if malos or sobrantes:
            print(f"FALLÓ: {len(malos)} figura(s) desincronizada(s), {len(sobrantes)} sobrante(s).")
            for m in (malos + sobrantes)[:20]:
                print(f"  - {m}")
            return 1
        print(f"OK: {len(pendientes)} figuras de anexos sincronizadas con el manifiesto")
        return 0
    SALIDA.mkdir(parents=True, exist_ok=True)
    for p, svg in pendientes.items():
        p.write_text(svg, encoding="utf-8", newline="\n")
    print(f"OK: {len(pendientes)} figuras generadas en annexes/img/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
