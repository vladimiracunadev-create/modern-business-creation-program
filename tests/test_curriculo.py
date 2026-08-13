"""Pruebas estructurales del currículo y de los manifiestos.

No verifican exactitud jurídica —eso exige revisión humana— sino las invariantes que
el repositorio promete: numeración continua, contenido propio por clase, fuentes
existentes y ausencia de texto de plantilla repetido entre clases.
"""

from __future__ import annotations

import json
import unittest
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
MANIFESTS = RAIZ / "manifests"
CURRICULUM = RAIZ / "curriculum"

TOTAL_CLASES = 336
TOTAL_PARTES = 24


def cargar(nombre: str):
    return json.loads((MANIFESTS / nombre).read_text(encoding="utf-8"))


class ManifiestosTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.curriculo = cargar("curriculum.json")
        cls.packs = cargar("part_packs.json")
        cls.fuentes = cargar("official_sources.json")
        cls.clases = {}
        for archivo in sorted((MANIFESTS / "classes").glob("*.json")):
            for entrada in json.loads(archivo.read_text(encoding="utf-8")):
                cls.clases[entrada["n"]] = entrada

    def test_cantidad_de_clases_y_partes(self) -> None:
        self.assertEqual(len(self.curriculo), TOTAL_CLASES)
        self.assertEqual(len(self.packs), TOTAL_PARTES)

    def test_numeracion_global_continua(self) -> None:
        numeros = [c["global_class"] for c in self.curriculo]
        self.assertEqual(numeros, list(range(1, TOTAL_CLASES + 1)))

    def test_cada_clase_tiene_contenido_propio(self) -> None:
        faltan = [c["global_class"] for c in self.curriculo if c["global_class"] not in self.clases]
        self.assertEqual(faltan, [], f"clases sin contenido específico: {faltan[:5]}")

    def test_contenido_completo_por_clase(self) -> None:
        obligatorios = ("conceptos", "desarrollo", "decision", "entregable", "errores", "criterios")
        for numero, entrada in self.clases.items():
            with self.subTest(clase=numero):
                for campo in obligatorios:
                    self.assertIn(campo, entrada)
                    self.assertTrue(entrada[campo], f"campo vacío: {campo}")
                self.assertEqual(len(entrada["conceptos"]), 4)
                for concepto in entrada["conceptos"]:
                    self.assertEqual(len(concepto), 2)
                self.assertGreaterEqual(len(entrada["desarrollo"].split()), 30)

    def test_desarrollos_no_se_repiten(self) -> None:
        """Regresión: en la v0.1.0 las 336 clases compartían el mismo cuerpo."""
        repetidos = [t for t, n in Counter(e["desarrollo"] for e in self.clases.values()).items() if n > 1]
        self.assertEqual(repetidos, [], "hay párrafos de desarrollo duplicados entre clases")

    def test_decisiones_no_se_repiten(self) -> None:
        repetidas = [t for t, n in Counter(e["decision"] for e in self.clases.values()).items() if n > 1]
        self.assertEqual(repetidas, [], "hay decisiones duplicadas entre clases")

    def test_fuentes_citadas_existen(self) -> None:
        conocidas = {f["id"] for f in self.fuentes}
        for entrada in self.clases.values():
            with self.subTest(clase=entrada["n"]):
                self.assertLessEqual(set(entrada.get("fuentes", [])), conocidas)
        for pack in self.packs:
            with self.subTest(parte=pack["part"]):
                self.assertLessEqual(set(pack["fuentes"]), conocidas)
                self.assertTrue(pack["fuentes"], "la parte no declara fuentes")

    def test_fuentes_usan_https(self) -> None:
        for fuente in self.fuentes:
            with self.subTest(fuente=fuente["id"]):
                self.assertTrue(fuente["url"].startswith("https://"))

    def test_packs_completos(self) -> None:
        estados = {"VERIFICADO-FUENTE", "GUIA-PRACTICA", "SECTORIAL", "DINAMICO"}
        for pack in self.packs:
            with self.subTest(parte=pack["part"]):
                self.assertIn(pack["estado"], estados)
                self.assertGreaterEqual(len(pack["resumen"].split()), 25)
                self.assertEqual(len(pack["resultados"]), 4)
                self.assertGreaterEqual(len(pack["riesgos"]), 4)
                self.assertTrue(pack["marco"])


class ArbolTest(unittest.TestCase):
    def test_una_carpeta_por_parte(self) -> None:
        carpetas = [p for p in CURRICULUM.glob("part-*") if p.is_dir()]
        self.assertEqual(len(carpetas), TOTAL_PARTES)

    def test_un_readme_por_clase(self) -> None:
        readmes = list(CURRICULUM.glob("part-*/class-*/README.md"))
        self.assertEqual(len(readmes), TOTAL_CLASES)

    def test_readmes_de_clase_tienen_profundidad(self) -> None:
        cortos = [
            p.relative_to(RAIZ).as_posix()
            for p in CURRICULUM.glob("part-*/class-*/README.md")
            if len(p.read_text(encoding="utf-8").split()) < 400
        ]
        self.assertEqual(cortos, [], f"clases por debajo del mínimo de profundidad: {cortos[:5]}")

    def test_documentos_transversales_presentes(self) -> None:
        for nombre in ("README.md", "CURRICULUM.md", "STATUS.md", "ROADMAP.md",
                       "CHANGELOG.md", "CONTRIBUTING.md", "SECURITY.md",
                       "CODE_OF_CONDUCT.md", "SOURCES.md", "LICENSE", "VERSION"):
            with self.subTest(archivo=nombre):
                self.assertTrue((RAIZ / nombre).exists(), f"falta {nombre}")

    def test_version_coincide_con_changelog(self) -> None:
        version = (RAIZ / "VERSION").read_text(encoding="utf-8").strip()
        changelog = (RAIZ / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertIn(f"## [{version}]", changelog)


if __name__ == "__main__":
    unittest.main()
