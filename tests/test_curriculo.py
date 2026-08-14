"""Pruebas estructurales del currículo y de los manifiestos.

No verifican exactitud jurídica —eso exige revisión humana— sino las invariantes que
el repositorio promete: numeración continua, contenido propio por clase, fuentes
existentes y ausencia de texto de plantilla repetido entre clases.
"""

from __future__ import annotations

import json
import re
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
        cls.contenido = json.loads((MANIFESTS / "part_content.json").read_text(encoding="utf-8"))
        cls.clases = {}
        for archivo in sorted((MANIFESTS / "classes").glob("*.json")):
            for entrada in json.loads(archivo.read_text(encoding="utf-8")):
                cls.clases[entrada["n"]] = entrada
        cls.pedagogia = {}
        for archivo in sorted((MANIFESTS / "pedagogia").glob("*.json")):
            for entrada in json.loads(archivo.read_text(encoding="utf-8")):
                cls.pedagogia[entrada["n"]] = entrada

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

    def test_fuentes_estan_explicadas(self) -> None:
        """Una fuente enlazada sin explicar obliga a adivinar qué parte importa."""
        for fuente in self.fuentes:
            with self.subTest(fuente=fuente["id"]):
                self.assertGreaterEqual(len(fuente["que_dice"].split()), 15)
                self.assertGreaterEqual(len(fuente["como_leerla"].split()), 15)
                self.assertRegex(fuente["verificado"], r"^\d{4}-\d{2}-\d{2}$")

    def test_pedagogia_completa_por_clase(self) -> None:
        for numero in self.clases:
            with self.subTest(clase=numero):
                entrada = self.pedagogia.get(numero)
                self.assertIsNotNone(entrada, f"clase {numero} sin capa pedagógica")
                # Umbrales calibrados sobre la distribución real (propósito
                # 14-33 palabras, desarrollo 35-58): detectan una entrada vacía o
                # truncada sin obligar a inflar las que ya son precisas.
                self.assertGreaterEqual(len(entrada["proposito"].split()), 12)
                self.assertGreaterEqual(len(entrada["desarrollo2"].split()), 30)
                self.assertEqual(len(entrada["preguntas"]), 3)
                for pregunta in entrada["preguntas"]:
                    self.assertTrue(pregunta.rstrip().endswith("?"), pregunta)

    def test_propositos_y_preguntas_no_se_repiten(self) -> None:
        propositos = Counter(e["proposito"] for e in self.pedagogia.values())
        self.assertEqual([t for t, n in propositos.items() if n > 1], [])
        preguntas = Counter(p for e in self.pedagogia.values() for p in e["preguntas"])
        self.assertEqual([p for p, n in preguntas.items() if n > 1], [])

    def test_etapas_cubren_las_partes_sin_solapes(self) -> None:
        etapas = cargar("etapas.json")
        cubiertas = [p for e in etapas for p in e["partes"]]
        self.assertEqual(sorted(cubiertas), list(range(1, TOTAL_PARTES + 1)),
                         "las etapas deben cubrir las 24 partes exactamente una vez")
        for etapa in etapas:
            with self.subTest(etapa=etapa["etapa"]):
                # Consecutivas: una etapa con partes salteadas rompería el mapa
                # del recorrido, que dibuja cada etapa como una cadena continua.
                self.assertEqual(etapa["partes"],
                                 list(range(etapa["partes"][0], etapa["partes"][-1] + 1)))
                self.assertGreaterEqual(len(etapa["promesa"].split()), 30)
                self.assertTrue(etapa["salida"])
                self.assertTrue(etapa["color"])

    def test_partes_tienen_temario_y_nombre_corto(self) -> None:
        for parte in self.contenido:
            with self.subTest(parte=parte["part"]):
                self.assertGreaterEqual(len(parte["temario"].split()), 8)
                # El nombre corto rotula los nodos del mapa: si crece, el
                # diagrama deja de ser legible de un vistazo.
                self.assertLessEqual(len(parte["corto"]), 20)

    def test_bloque_de_partes_del_readme_generado(self) -> None:
        readme = (RAIZ / "README.md").read_text(encoding="utf-8")
        self.assertIn("<!-- partes:inicio -->", readme)
        self.assertIn("<!-- partes:fin -->", readme)
        bloque = readme.split("<!-- partes:inicio -->")[1].split("<!-- partes:fin -->")[0]
        for etapa in cargar("etapas.json"):
            self.assertIn(f"Etapa {etapa['etapa']} — {etapa['nombre']}", bloque)
        # Una fila por parte: `| NN | [Título](...)`. Contar así y no por
        # substring evita confundirlas con la columna de número de clases.
        filas = re.findall(r"^\| (\d{2}) \| \[", bloque, re.M)
        self.assertEqual([int(f) for f in filas], list(range(1, TOTAL_PARTES + 1)))

    def test_contenido_de_parte_completo(self) -> None:
        partes = {c["part"] for c in self.contenido}
        self.assertEqual(partes, set(range(1, TOTAL_PARTES + 1)))
        for parte in self.contenido:
            with self.subTest(parte=parte["part"]):
                self.assertGreaterEqual(len(parte["narrativa"].split()), 120)
                self.assertIn("flowchart", parte["diagrama"])
                self.assertGreaterEqual(len(parte["lecturas"]), 3)
                self.assertGreaterEqual(len(parte["conexiones"].split()), 25)

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
            if len(p.read_text(encoding="utf-8").split()) < 900
        ]
        self.assertEqual(cortos, [], f"clases por debajo del mínimo de profundidad: {cortos[:5]}")

    def test_todo_readme_del_curriculo_tiene_diagrama(self) -> None:
        sin_diagrama = [
            p.relative_to(RAIZ).as_posix()
            for p in CURRICULUM.rglob("README.md")
            if "```mermaid" not in p.read_text(encoding="utf-8")
        ]
        self.assertEqual(sin_diagrama, [], f"README sin diagrama: {sin_diagrama[:5]}")

    def test_glosario_generado_y_poblado(self) -> None:
        glosario = (RAIZ / "docs" / "19_GLOSSARY.md").read_text(encoding="utf-8")
        terminos = glosario.count("\n| **")
        self.assertGreaterEqual(terminos, 1000, f"glosario con solo {terminos} términos")
        self.assertIn("Glosario maestro", glosario)

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

    def test_version_coincide_con_el_badge_del_readme(self) -> None:
        version = (RAIZ / "VERSION").read_text(encoding="utf-8").strip()
        readme = (RAIZ / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"badge/version-{version}-", readme,
                      "el badge de versión del README quedó atrás respecto de VERSION")

    def test_enlaces_al_manual_usan_el_alias_estable(self) -> None:
        """El PDF versionado cambia de nombre en cada release y dejaría 404.

        El sitio publica además `downloads/manual.pdf` apuntando a la última
        versión; el README debe enlazar ese alias y no el archivo versionado.
        """
        readme = (RAIZ / "README.md").read_text(encoding="utf-8")
        versionados = re.findall(r"downloads/[\w-]*manual-v[\d.]+\.pdf", readme)
        self.assertEqual(versionados, [], f"enlaces versionados al manual: {versionados}")
        self.assertIn("downloads/manual.pdf", readme)


if __name__ == "__main__":
    unittest.main()
