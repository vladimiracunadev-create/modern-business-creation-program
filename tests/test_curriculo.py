"""Pruebas estructurales del currículo y de los manifiestos.

No verifican exactitud jurídica —eso exige revisión humana— sino las invariantes que
el repositorio promete: numeración continua, contenido propio por clase, fuentes
existentes y ausencia de texto de plantilla repetido entre clases.
"""

from __future__ import annotations

import csv
import json
import math
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
        cls.fuentes = json.loads(
            (MANIFESTS.parent / "sources" / "bibliography.json").read_text(encoding="utf-8")
        )["entries"]
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
        conocidas = {f["manifest_id"] for f in self.fuentes}
        for entrada in self.clases.values():
            with self.subTest(clase=entrada["n"]):
                self.assertLessEqual(set(entrada.get("fuentes", [])), conocidas)
        for pack in self.packs:
            with self.subTest(parte=pack["part"]):
                self.assertLessEqual(set(pack["fuentes"]), conocidas)
                self.assertTrue(pack["fuentes"], "la parte no declara fuentes")

    def test_fuentes_usan_https(self) -> None:
        for fuente in self.fuentes:
            with self.subTest(fuente=fuente["manifest_id"]):
                self.assertTrue(fuente["locator"].startswith("https://"))

    def test_fuentes_estan_explicadas(self) -> None:
        """Una fuente enlazada sin explicar obliga a adivinar qué parte importa."""
        for fuente in self.fuentes:
            with self.subTest(fuente=fuente["manifest_id"]):
                self.assertGreaterEqual(len(fuente["que_contiene"].split()), 15)
                self.assertGreaterEqual(len(fuente["como_leerla"].split()), 15)
                self.assertRegex(fuente["accessed"], r"^\d{4}-\d{2}-\d{2}$")

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


class IntegracionViabilidadTest(unittest.TestCase):
    """La integración debe vivir en artefactos reutilizados, no en clases nuevas."""

    def test_expediente_reune_los_seis_dominios(self) -> None:
        expediente = (RAIZ / "templates" / "01_idea_thesis.md").read_text(encoding="utf-8")
        for seccion in (
            "## 01 Mercado",
            "## 02 Cliente",
            "## 03 Costos",
            "## 04 Modelo",
            "## 05 Aliados",
            "## 06 Proyección",
        ):
            with self.subTest(seccion=seccion):
                self.assertIn(seccion, expediente)
        for pregunta in (
            "¿Existe mercado?",
            "¿Existe un cliente identificable?",
            "¿Hay evidencia de un problema real?",
            "¿El modelo genera ingresos?",
            "¿La estructura de costos permite sostenerlo?",
            "¿Qué aliados son críticos?",
            "¿Cuánto capital necesita?",
            "¿Qué supuesto podría destruir el negocio?",
            "¿Qué evidencia falta antes de invertir más?",
        ):
            with self.subTest(pregunta=pregunta):
                self.assertIn(pregunta, expediente)

    def test_cliente_separa_evidencia_hipotesis_e_interpretacion(self) -> None:
        plantilla = (RAIZ / "templates" / "02_customer_interview.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Evidencia del cliente", plantilla)
        self.assertIn("Hipótesis del equipo", plantilla)
        self.assertIn("Interpretación", plantilla)
        for campo in (
            "Qué intentaba lograr",
            "Qué observó",
            "Qué escuchó",
            "Dolores observados",
            "Ganancias esperadas",
            "Disposición a pagar demostrada",
            "Criterios de compra",
            "Objeciones",
        ):
            self.assertIn(campo, plantilla)

    def test_canvas_registra_evidencia_y_version(self) -> None:
        plantilla = (RAIZ / "templates" / "03_business_model_canvas.md").read_text(
            encoding="utf-8"
        )
        for campo in (
            "Hipótesis",
            "Evidencia",
            "Fuente y fecha",
            "Confianza",
            "Riesgo si es falsa",
            "Próximo experimento",
            "Historial de versiones",
        ):
            self.assertIn(campo, plantilla)

    def test_informe_de_mercado_cubre_sintesis_ejecutiva(self) -> None:
        plantilla = (RAIZ / "templates" / "04_market_sizing.md").read_text(encoding="utf-8")
        for campo in (
            "TAM:",
            "SAM:",
            "SOM a 12–24 meses:",
            "Tendencias relevantes:",
            "Competidores directos:",
            "Competidores indirectos:",
            "Sustitutos y statu quo:",
            "Benchmarks comparables",
            "Barreras de entrada:",
            "Señales de crecimiento o contracción:",
            "Preguntas todavía no resueltas:",
        ):
            self.assertIn(campo, plantilla)
        self.assertIn("Toda cifra debe tener fuente", plantilla)

    def test_ejemplo_financiero_es_aritmeticamente_reproducible(self) -> None:
        ruta = RAIZ / "templates" / "08_unit_economics.csv"
        with ruta.open(encoding="utf-8", newline="") as archivo:
            filas = list(csv.DictReader(archivo))
        self.assertEqual([f["escenario"] for f in filas], ["conservador", "base", "expansivo"])
        for fila in filas:
            with self.subTest(escenario=fila["escenario"]):
                volumen = int(fila["supuesto_volumen_unidades"])
                precio = int(fila["supuesto_precio_unitario"])
                variable_unitario = int(fila["supuesto_costo_directo_variable_unitario"])
                fijo = int(fila["supuesto_costo_indirecto_fijo"])
                semifijo = int(fila["supuesto_costo_indirecto_semifijo"])
                capacidad = int(fila["supuesto_capacidad_unidades"])
                variable_total = volumen * variable_unitario
                indirecto_total = fijo + semifijo
                contribucion_unitaria = precio - variable_unitario
                contribucion_total = volumen * contribucion_unitaria
                self.assertEqual(int(fila["calculo_ventas"]), volumen * precio)
                self.assertEqual(int(fila["calculo_ingresos"]), volumen * precio)
                self.assertEqual(int(fila["calculo_costo_directo_variable_total"]), variable_total)
                self.assertEqual(int(fila["calculo_costo_indirecto_total"]), indirecto_total)
                self.assertEqual(int(fila["calculo_opex"]), variable_total + indirecto_total)
                self.assertEqual(int(fila["calculo_margen_contribucion_unitario"]), contribucion_unitaria)
                self.assertEqual(int(fila["calculo_margen_contribucion_total"]), contribucion_total)
                self.assertEqual(int(fila["calculo_margen_operacional"]), contribucion_total - indirecto_total)
                self.assertEqual(
                    int(fila["calculo_punto_equilibrio_unidades"]),
                    math.ceil(indirecto_total / contribucion_unitaria),
                )
                self.assertAlmostEqual(float(fila["calculo_utilizacion"]), volumen / capacidad, places=4)

    def test_clases_existentes_contienen_los_puentes(self) -> None:
        clases = {}
        for archivo in sorted((MANIFESTS / "classes").glob("*.json")):
            for entrada in json.loads(archivo.read_text(encoding="utf-8")):
                clases[entrada["n"]] = entrada
        expectativas = {
            28: "secciones 01 Mercado y 02 Cliente",
            29: "registro de evidencia por bloque",
            116: "planilla base de costos",
            196: "tres escenarios financieros",
            275: "mapa de aliados priorizado",
            329: "secciones 03 y 06",
            336: "Expediente de viabilidad completo",
        }
        for numero, fragmento in expectativas.items():
            with self.subTest(clase=numero):
                self.assertIn(fragmento, clases[numero]["entregable"])


class IntegracionMedviTest(unittest.TestCase):
    """Evita que el caso transversal pierda rigor o quede desconectado del currículo."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.ruta = RAIZ / "case-studies" / "21-medvi-empresa-ai-native-y-control.md"
        cls.caso = cls.ruta.read_text(encoding="utf-8")
        cls.clases = {}
        for archivo in sorted((MANIFESTS / "classes").glob("*.json")):
            for entrada in json.loads(archivo.read_text(encoding="utf-8")):
                cls.clases[entrada["n"]] = entrada
        cls.fuentes = json.loads(
            (RAIZ / "sources" / "bibliography.json").read_text(encoding="utf-8")
        )["entries"]

    def test_expediente_separa_categorias_de_evidencia(self) -> None:
        for categoria in (
            "HECHO VERIFICADO",
            "CIFRA REPORTADA",
            "ALEGACIÓN",
            "ACTUACIÓN REGULATORIA",
            "RESPUESTA DE MEDVi",
            "INTERPRETACIÓN",
            "LECCIÓN EMPRESARIAL",
        ):
            with self.subTest(categoria=categoria):
                self.assertIn(categoria, self.caso)

    def test_expediente_distingue_categorias_farmaceuticas(self) -> None:
        for categoria in (
            "FDA-approved drug",
            "Generic FDA-approved drug",
            "Compounded drug",
            "Counterfeit drug",
        ):
            with self.subTest(categoria=categoria):
                self.assertIn(categoria, self.caso)
        self.assertIn("no es por definición falsificado", self.caso)

    def test_expediente_contiene_due_diligence_y_matrices(self) -> None:
        self.assertIn("un fondo analiza invertir US$5 millones", self.caso)
        self.assertIn("Founder bottleneck", self.caso)
        for tension in (
            "Velocidad × control",
            "Automatización × supervisión",
            "Crecimiento × compliance",
            "Outsourcing × responsabilidad",
            "Margen × riesgo",
        ):
            with self.subTest(tension=tension):
                self.assertIn(tension, self.caso)

    def test_expediente_conserva_su_capa_visual(self) -> None:
        self.assertGreaterEqual(self.caso.count("```mermaid"), 6)
        for icono in ("🧭", "🤖", "🧩", "💊", "⚠️", "🎛️", "🔎", "🚨", "🛡️"):
            with self.subTest(icono=icono):
                self.assertIn(icono, self.caso)

    def test_clases_enlazan_el_caso_sin_alterar_la_numeracion(self) -> None:
        esperadas = {13, 40, 155, 208, 223, 254, 267, 284, 296}
        self.assertEqual(set(self.clases), set(range(1, TOTAL_CLASES + 1)))
        enlazadas = {
            numero
            for numero, entrada in self.clases.items()
            if entrada.get("caso_aplicado", {}).get("ruta")
            == "case-studies/21-medvi-empresa-ai-native-y-control.md"
        }
        self.assertEqual(enlazadas, esperadas)

    def test_fuentes_medvi_tienen_fecha_de_consulta(self) -> None:
        esperadas = {
            "FDA_MEDVI",
            "FDA_COMPOUNDING",
            "FDA_COUNTERFEIT",
            "FDA_GL1",
            "MEDVI_RESPONSE",
            "NYT_MEDVI_PROFILE",
            "FUTURISM_MEDVI",
        }
        registradas = {fuente["manifest_id"]: fuente for fuente in self.fuentes}
        self.assertLessEqual(esperadas, set(registradas))
        for identificador in esperadas:
            with self.subTest(fuente=identificador):
                self.assertEqual(registradas[identificador]["accessed"], "2026-10-04")


if __name__ == "__main__":
    unittest.main()
