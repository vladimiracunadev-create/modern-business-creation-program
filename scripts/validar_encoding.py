#!/usr/bin/env python3
"""Verifica que todo el repositorio sea UTF-8 limpio y sin mojibake.

El drift de codificación aparece cuando un archivo se edita con una herramienta que
asume cp1252/latin-1: el texto queda leíble en esa máquina y roto para todo el resto.
Se detecta por dos vías: archivos que no decodifican como UTF-8, y texto que sí
decodifica pero es el resultado visible de una doble codificación.

La detección es por round-trip y no por lista de secuencias sospechosas: si una línea
puede codificarse a cp1252 y volver a decodificarse como UTF-8 dando un texto distinto,
entonces lo que se leyó fue UTF-8 interpretado como cp1252. Además, escribir el patrón
de forma literal haría que este mismo archivo se autodenunciara al ser escaneado.
"""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]

EXTENSIONES = {".md", ".json", ".py", ".yml", ".yaml", ".csv", ".txt", ".html", ".css", ".js"}
IGNORADOS = {".git", "node_modules", "site", ".venv", "__pycache__"}

REEMPLAZO = chr(0xFFFD)  # U+FFFD REPLACEMENT CHARACTER


def es_mojibake(linea: str) -> str | None:
    """Devuelve el texto que la línea debería decir, o None si está bien."""
    if REEMPLAZO in linea:
        return "carácter de reemplazo U+FFFD"
    try:
        recuperado = _a_bytes_cp1252(linea).decode("utf-8")
    except (ValueError, UnicodeDecodeError):
        return None
    return f"debería decir {recuperado.strip()!r}" if recuperado != linea else None


def _a_bytes_cp1252(linea: str) -> bytes:
    """Deshace la lectura cp1252 carácter a carácter.

    cp1252 deja cinco posiciones sin definir (0x81, 0x8D, 0x8F, 0x90, 0x9D). Un texto
    mojibake las arrastra como controles U+0081..U+009D, así que `str.encode('cp1252')`
    fallaría justo en las comillas tipográficas rotas, que es el caso que interesa.
    """
    salida = bytearray()
    for caracter in linea:
        try:
            salida += caracter.encode("cp1252")
        except UnicodeEncodeError:
            if ord(caracter) > 0xFF:
                raise ValueError("carácter fuera del rango de un byte")
            salida.append(ord(caracter))
    return bytes(salida)


def archivos() -> list[Path]:
    return sorted(
        p for p in RAIZ.rglob("*")
        if p.is_file()
        and p.suffix.lower() in EXTENSIONES
        and not any(parte in IGNORADOS for parte in p.relative_to(RAIZ).parts)
    )


def main() -> int:
    errores: list[str] = []
    revisados = 0

    for archivo in archivos():
        crudo = archivo.read_bytes()
        relativo = archivo.relative_to(RAIZ).as_posix()

        if crudo.startswith(b"\xef\xbb\xbf"):
            errores.append(f"{relativo}: tiene BOM UTF-8 (debe guardarse sin BOM)")

        try:
            texto = crudo.decode("utf-8")
        except UnicodeDecodeError as error:
            errores.append(f"{relativo}: no es UTF-8 válido ({error.reason} en byte {error.start})")
            continue

        revisados += 1
        for numero, linea in enumerate(texto.splitlines(), 1):
            diagnostico = es_mojibake(linea)
            if diagnostico:
                errores.append(f"{relativo}:{numero}: {diagnostico}")
                break

    if errores:
        print(f"FALLÓ la validación de codificación con {len(errores)} problema(s):")
        for error in errores[:40]:
            print(f"  ERROR: {error}")
        if len(errores) > 40:
            print(f"  ... y {len(errores) - 40} más")
        return 1

    print(f"OK: {revisados} archivos en UTF-8 sin BOM y sin mojibake.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
