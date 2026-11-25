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
        def con_visual(p) -> bool:
            texto = p.read_text(encoding="utf-8")
            if "```mermaid" in texto:
                return True
            return "](modelo-mental.svg)" in texto and (p.parent / "modelo-mental.svg").exists()

        sin_diagrama = [
            p.relative_to(RAIZ).as_posix() for p in CURRICULUM.rglob("README.md") if not con_visual(p)
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
                # Una revalidación mensual avanza `accessed`; lo que no puede es
                # quedar vacío, mal formado ni anterior a la consulta original.
                fecha = registradas[identificador]["accessed"]
                self.assertRegex(fecha, r"^\d{4}-\d{2}-\d{2}$")
                self.assertGreaterEqual(fecha, "2026-10-04")



class LeyReconstruccionTest(unittest.TestCase):
    """Ley 21.850: se integra en clases existentes, sin cambiar la numeración."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.curriculo = cargar("curriculum.json")
        cls.fuentes = json.loads(
            (MANIFESTS.parent / "sources" / "bibliography.json").read_text(encoding="utf-8")
        )["entries"]
        cls.clases = {}
        for archivo in sorted((MANIFESTS / "classes").glob("*.json")):
            for entrada in json.loads(archivo.read_text(encoding="utf-8")):
                cls.clases[entrada["n"]] = entrada

    def test_ley_21850_se_integra_sin_alterar_la_numeracion(self) -> None:
        esperadas = {85, 89, 90, 91, 92, 96, 97, 98, 155, 160, 161, 236, 244, 246, 263, 285, 287}
        self.assertEqual(set(self.clases), set(range(1, TOTAL_CLASES + 1)))
        integradas = {n for n, e in self.clases.items() if e.get("actualizacion")}
        self.assertEqual(integradas, esperadas)
        guia = (RAIZ / "docs" / "20_LEY_21850_RECONSTRUCCION_NACIONAL.md").read_text(encoding="utf-8")
        for numero in integradas:
            with self.subTest(clase=numero):
                self.assertIn("Actualización normativa: Ley 21.850", self.readme_de(numero))
        for frase in ("0,7 %", "75 UTM", "25,5 %", "Pendiente de SII", "revisión humana",
                      "Calendario consolidado 2027–2030", "6,4 %", "Circular 53"):
            self.assertIn(frase, guia)

    def test_ley_21850_registra_fuentes_con_fecha(self) -> None:
        registradas = {f["manifest_id"]: f for f in self.fuentes}
        for identificador in ("LEY_21850_DO", "LEY_21850_BCN"):
            with self.subTest(fuente=identificador):
                self.assertEqual(registradas[identificador]["accessed"], "2026-11-05")

    def test_ejemplo_ley_21850_es_aritmeticamente_reproducible(self) -> None:
        """Carga total empresa más propietario de la guía, con la fórmula escrita en ella."""
        for tasa, restitucion, total in ((27.0, 0.35, 44.45), (25.5, 0.30, 42.65),
                                         (24.0, 0.20, 39.80), (23.0, 0.0, 35.0)):
            neto = 35.0 - tasa * (1 - restitucion)
            self.assertAlmostEqual(tasa + neto, total, places=2)
        utm, base = 70_000, 36_000_000 * 0.75
        self.assertEqual(min(base * 0.15, 75 * utm) * 4, 16_200_000)
        self.assertEqual(min(base * 0.20, 75 * utm) * 4, 21_000_000)

    def test_calendario_2027_2030_es_aritmeticamente_reproducible(self) -> None:
        """PPM transitorio del régimen general y costo de planilla de la guía."""
        for anterior, nueva, reduccion in ((27.0, 25.5, 5.56), (25.5, 24.0, 5.88), (24.0, 23.0, 4.17)):
            self.assertAlmostEqual((1 - nueva / anterior) * 100, reduccion, places=2)
        self.assertAlmostEqual(2.0 * (1 - 0.0556), 1.8888, places=4)
        self.assertEqual(round(30_000_000 * 0.018888), 566_640)
        for tasa, costo in ((3.5, 350_000), (4.25, 425_000), (5.0, 500_000), (5.7, 570_000), (6.4, 640_000)):
            self.assertEqual(round(10_000_000 * tasa / 100), costo)
        for tasa, ppm in ((0.125, 25_000), (0.25, 50_000), (0.23, 46_000)):
            self.assertEqual(round(20_000_000 * tasa / 100), ppm)

    def readme_de(self, numero: int) -> str:
        clase = next(c for c in self.curriculo if c["global_class"] == numero)
        for carpeta in CURRICULUM.glob(f"part-{clase['part']:02d}-*"):
            for ruta in carpeta.glob(f"class-{clase['class']:02d}-*/README.md"):
                return ruta.read_text(encoding="utf-8")
        raise AssertionError(f"sin README para la clase {numero}")


class ProteccionConocimientoTest(unittest.TestCase):
    """Inteligencia económica y espionaje empresarial: integrado sin crear clases."""

    CLASES = {
        9, 16, 21, 38, 49, 68, 128, 131, 138, 151, 154, 156, 168, 171, 188, 190, 199, 202,
        203, 209, 217, 223, 239, 252, 253, 256, 258, 261, 262, 275, 281, 284, 290, 293, 296,
        309, 312, 316,
    }
    DOC = "docs/21_INTELIGENCIA_ECONOMICA_Y_PROTECCION_DEL_CONOCIMIENTO.md"
    CASO = "case-studies/22-nvidia-sospecha-de-espionaje-y-proteccion-del-conocimiento.md"

    @staticmethod
    def _ancla(encabezado: str) -> str:
        texto = re.sub(r"[^\w\s-]", "", encabezado.strip().lower())
        return re.sub(r"\s", "-", texto)

    @classmethod
    def setUpClass(cls) -> None:
        cls.guia = (RAIZ / cls.DOC).read_text(encoding="utf-8")
        cls.caso = (RAIZ / cls.CASO).read_text(encoding="utf-8")
        cls.clases = {}
        for archivo in sorted((MANIFESTS / "classes").glob("*.json")):
            for entrada in json.loads(archivo.read_text(encoding="utf-8")):
                cls.clases[entrada["n"]] = entrada
        cls.fuentes = {
            f["manifest_id"]: f
            for f in json.loads(
                (RAIZ / "sources" / "bibliography.json").read_text(encoding="utf-8")
            )["entries"]
        }
        cls.anclas_guia = {
            cls._ancla(h) for h in re.findall(r"^## (.+)$", cls.guia, flags=re.M)
        }
        cls.anclas_caso = {
            cls._ancla(h) for h in re.findall(r"^## (.+)$", cls.caso, flags=re.M)
        }

    def test_no_se_crean_clases_ni_se_altera_la_numeracion(self) -> None:
        self.assertEqual(set(self.clases), set(range(1, TOTAL_CLASES + 1)))
        integradas = {n for n, e in self.clases.items() if e.get("proteccion")}
        self.assertEqual(integradas, self.CLASES)

    def test_cada_bloque_tiene_tres_niveles_y_enlaces_que_existen(self) -> None:
        for numero in sorted(self.CLASES):
            bloque = self.clases[numero]["proteccion"]
            with self.subTest(clase=numero):
                self.assertEqual(len(bloque["niveles"]), 3)
                for nivel in bloque["niveles"]:
                    self.assertGreaterEqual(len(nivel.split()), 8)
                self.assertGreaterEqual(len(bloque["lente"].split()), 15)
                self.assertGreaterEqual(len(bloque["ejercicio"].split()), 10)
                self.assertGreaterEqual(len(bloque["terminos"]), 2)
                self.assertIn(bloque["ancla"], self.anclas_guia)
                if bloque.get("caso"):
                    self.assertIn(bloque["caso"]["ancla"], self.anclas_caso)

    def test_readme_de_cada_clase_integrada_trae_el_bloque(self) -> None:
        curriculo = cargar("curriculum.json")
        for clase in curriculo:
            numero = clase["global_class"]
            if numero not in self.CLASES:
                continue
            carpeta = next(
                CURRICULUM.glob(f"part-{clase['part']:02d}-*/class-{clase['class']:02d}-*")
            )
            texto = (carpeta / "README.md").read_text(encoding="utf-8")
            with self.subTest(clase=numero):
                self.assertIn("## 🛡️ Protección del conocimiento", texto)
                self.assertIn("Enfoque defensivo", texto)

    def test_guia_cubre_las_veinte_secciones_y_los_tres_niveles(self) -> None:
        encabezados = re.findall(r"^## (\d+)\. ", self.guia, flags=re.M)
        self.assertEqual(encabezados, [str(i) for i in range(1, 21)])
        for frase in (
            "Emprendedor o microempresa", "Pyme", "Gran empresa o multinacional",
            "Business Intelligence", "Competitive Intelligence", "Economic Intelligence",
            "Industrial Espionage", "Trade Secret", "Social Engineering", "HUMINT",
            "Honey Trap", "Elicitation", "Pretexting", "Insider Threat", "Counterintelligence",
            "Obligaciones legales", "Recomendaciones", "Medidas voluntarias",
            "Por qué no se crean clases",
        ):
            with self.subTest(frase=frase):
                self.assertIn(frase, self.guia)

    def test_guia_cita_los_articulos_verificados_en_bcn(self) -> None:
        for frase in (
            "art. 86", "tres requisitos copulativos", "284 quinquies", "284 sexies",
            "Ley 21.595, art. 2", "Ley 21.459", "Ley 20.169", "154 ter",
            "no menciona expresamente la obtención de secretos",
        ):
            with self.subTest(frase=frase):
                self.assertIn(frase, self.guia)

    def test_terminologia_vigente_es_secreto_comercial(self) -> None:
        for numero, entrada in self.clases.items():
            with self.subTest(clase=numero):
                self.assertNotIn("ecreto empresarial", json.dumps(entrada, ensure_ascii=False))

    def test_caso_nvidia_separa_conocido_alegado_y_pendiente(self) -> None:
        for etiqueta in (
            "INFORMACIÓN OFICIALMENTE CONOCIDA",
            "SOSPECHA O ALEGACIÓN",
            "NEGACIÓN O POSICIÓN DE PARTE",
            "INVESTIGACIÓN NO CONCLUIDA",
            "DESCONOCIDO",
            "LECCIÓN EMPRESARIAL",
        ):
            with self.subTest(etiqueta=etiqueta):
                self.assertIn(etiqueta, self.caso)
        self.assertIn("No afirma que NVIDIA haya sufrido", self.caso)
        self.assertIn("Ninguna de las fuentes citadas", self.caso)
        self.assertIn("12-11-2026", self.caso)

    def test_ejercicios_no_exigen_construir_sistemas(self) -> None:
        self.assertIn("No requieren crear ningún sistema informático", self.caso)
        self.assertIn(
            "Ninguno exige construir un sistema informático", " ".join(self.guia.split())
        )

    def test_fuentes_nuevas_registradas_con_fecha_y_uso(self) -> None:
        esperadas = {
            "LEY_20169_BCN", "DFL4_PROPIEDAD_INDUSTRIAL", "CP_SECRETO_COMERCIAL",
            "LEY_21595_BCN", "LEY_21459_BCN", "CT_RESERVA_BCN", "CRS_EEA", "DOJ_COCA_COLA",
            "DOJ_KOLON", "DOJ_LEVANDOWSKI", "CNBC_NVIDIA", "NBC_NVIDIA", "NEXTGOV_NVIDIA",
        }
        self.assertLessEqual(esperadas, set(self.fuentes))
        for identificador in esperadas:
            with self.subTest(fuente=identificador):
                fuente = self.fuentes[identificador]
                self.assertEqual(fuente["accessed"], "2026-11-12")
                self.assertTrue(fuente["used_in"])
        self.assertEqual(self.fuentes["DOJ_COCA_COLA"]["status"], "pendiente")

    def test_matriz_legal_registra_las_normas_nuevas(self) -> None:
        nombres = {n["name"] for n in cargar("legal_sources.json")}
        self.assertIn("Ley 20.169", nombres)
        self.assertIn("Código Penal, arts. 284 a 284 sexies", nombres)


class ReputacionCrisisTest(unittest.TestCase):
    """Reputación, crisis y confianza: integrado sin crear clases ni alterar la numeración."""

    CLASES = {
        154, 163, 164, 166, 168, 176, 179, 184, 187, 193, 194, 195, 253, 258, 264, 265, 268,
        274, 276, 281, 283, 284, 285, 286, 287, 289, 290, 291, 292, 293, 294,
    }
    DOC = "docs/22_REPUTACION_CRISIS_Y_CONFIANZA.md"
    CASO = "case-studies/23-reputacion-y-crisis-siete-casos.md"
    PLANTILLAS = {
        25: "25_politica_comunicacion_corporativa.md",
        26: "26_matriz_severidad_reputacional.csv",
        27: "27_procedimiento_control_de_danos.md",
        28: "28_protocolo_escalamiento_y_voceria.md",
        29: "29_registro_incidentes_reputacionales.csv",
        30: "30_plan_respuesta_y_recuperacion.md",
        31: "31_guias_comunicacion_por_audiencia.md",
        32: "32_indicadores_de_confianza.csv",
        33: "33_simulaciones_crisis_pyme.md",
    }

    @staticmethod
    def _ancla(encabezado: str) -> str:
        texto = re.sub(r"[^\w\s-]", "", encabezado.strip().lower())
        return re.sub(r"\s", "-", texto)

    @classmethod
    def setUpClass(cls) -> None:
        cls.guia = (RAIZ / cls.DOC).read_text(encoding="utf-8")
        cls.caso = (RAIZ / cls.CASO).read_text(encoding="utf-8")
        cls.clases = {}
        for archivo in sorted((MANIFESTS / "classes").glob("*.json")):
            for entrada in json.loads(archivo.read_text(encoding="utf-8")):
                cls.clases[entrada["n"]] = entrada
        cls.fuentes = {
            f["manifest_id"]: f
            for f in json.loads(
                (RAIZ / "sources" / "bibliography.json").read_text(encoding="utf-8")
            )["entries"]
        }
        cls.anclas_guia = {
            cls._ancla(h) for h in re.findall(r"^## (.+)$", cls.guia, flags=re.M)
        }
        cls.anclas_caso = {
            cls._ancla(h) for h in re.findall(r"^## (.+)$", cls.caso, flags=re.M)
        }

    def test_no_se_crean_clases_ni_se_altera_la_numeracion(self) -> None:
        self.assertEqual(set(self.clases), set(range(1, TOTAL_CLASES + 1)))
        integradas = {n for n, e in self.clases.items() if e.get("reputacion")}
        self.assertEqual(integradas, self.CLASES)
        # El bloque anterior de protección del conocimiento se conserva intacto.
        self.assertEqual(sum(1 for e in self.clases.values() if e.get("proteccion")), 38)

    def test_cada_bloque_tiene_tres_niveles_obligacion_recomendacion_y_enlaces(self) -> None:
        for numero in sorted(self.CLASES):
            bloque = self.clases[numero]["reputacion"]
            with self.subTest(clase=numero):
                self.assertEqual(len(bloque["niveles"]), 3)
                for nivel in bloque["niveles"]:
                    self.assertGreaterEqual(len(nivel.split()), 8)
                self.assertGreaterEqual(len(bloque["lente"].split()), 15)
                self.assertGreaterEqual(len(bloque["ejercicio"].split()), 10)
                self.assertGreaterEqual(len(bloque["obligacion"].split()), 12)
                self.assertGreaterEqual(len(bloque["recomendacion"].split()), 12)
                self.assertGreaterEqual(len(bloque["terminos"]), 2)
                self.assertIn(bloque["ancla"], self.anclas_guia)
                self.assertTrue((RAIZ / bloque["plantilla"]["ruta"]).exists())
                if bloque.get("caso"):
                    self.assertIn(bloque["caso"]["ancla"], self.anclas_caso)
                    self.assertGreaterEqual(len(bloque["caso"]["lente"].split()), 10)

    def test_readme_de_cada_clase_integrada_trae_el_bloque(self) -> None:
        for clase in cargar("curriculum.json"):
            numero = clase["global_class"]
            if numero not in self.CLASES:
                continue
            carpeta = next(
                CURRICULUM.glob(f"part-{clase['part']:02d}-*/class-{clase['class']:02d}-*")
            )
            texto = (carpeta / "README.md").read_text(encoding="utf-8")
            with self.subTest(clase=numero):
                self.assertIn("## 🤝 Reputación y confianza", texto)
                self.assertIn("**Obligación legal:**", texto)
                self.assertIn("**Recomendación profesional:**", texto)

    def test_guia_cubre_las_veintiuna_secciones_y_distingue_obligacion_de_recomendacion(
        self,
    ) -> None:
        encabezados = re.findall(r"^## (\d+)\. ", self.guia, flags=re.M)
        self.assertEqual(encabezados, [str(i) for i in range(1, 22)])
        for frase in (
            "[Obligación legal]", "[Recomendación profesional]", "[Voluntaria]",
            "Matriz de severidad reputacional", "Comité de crisis por tamaño",
            "Vocería de fundadores y representantes legales", "Protección de personas afectadas",
            "Conflictos laborales y con proveedores", "Recuperación de confianza",
            "Indicadores de confianza", "Lo que **no** es obligación legal",
            "Relaciones institucionales y asuntos públicos",
            "Gestión de reclamos y controversias",
        ):
            with self.subTest(frase=frase):
                self.assertIn(frase, self.guia)

    def test_guia_cita_los_plazos_y_articulos_leidos_en_la_bcn(self) -> None:
        plano = " ".join(self.guia.split())
        for frase in (
            "alerta en **3 horas**", "actualización en **72 horas**", "**15 días corridos**",
            "prescribe a los 20 días", "1.000 palabras", "art. 14 sexies", "Ley 21.855",
            "15 de octubre de 2027", "art. 211-C", "30 días", "arts. 45 y 46", "art. 76",
            "art. 345", "arts. 289 y 291", "10 a 50 UTM", "50 a 150 UTM", "Ley 21.131",
            "arts. 9 y 10", "art. 54",
        ):
            with self.subTest(frase=frase):
                self.assertIn(frase, plano)

    def test_la_vigencia_de_la_ley_21719_no_quedo_en_la_fecha_derogada(self) -> None:
        # La Ley 21.855 sustituyó el 1-12-2026 por el 15-10-2027: ningún texto de clase,
        # parte ni manifiesto puede seguir afirmándolo como fecha de vigencia.
        rutas = list((RAIZ / "curriculum").rglob("README.md")) + list(MANIFESTS.rglob("*.json"))
        for ruta in rutas:
            texto = ruta.read_text(encoding="utf-8")
            with self.subTest(archivo=str(ruta.relative_to(RAIZ))):
                self.assertNotIn("vigencia el 1 de diciembre de 2026", texto)
                self.assertNotIn("vigente desde el 1 de diciembre de 2026", texto)
                self.assertNotIn("antes del 1 de diciembre de 2026", texto)
        parte_11 = next((CURRICULUM).glob("part-11-*"))
        clase_147 = next(parte_11.glob("class-07-*")) / "README.md"
        self.assertIn("15 de octubre de 2027", clase_147.read_text(encoding="utf-8"))

    def test_siete_casos_con_las_siete_secciones_y_naturaleza_ilustrativa(self) -> None:
        casos = re.split(r"^## (?=\d+\. )", self.caso, flags=re.M)[1:]
        self.assertEqual(len(casos), 7)
        for numero, cuerpo in enumerate(casos, start=1):
            for seccion in (
                "Diagnóstico", "Responsables", "Evidencia", "Alternativas", "Decisiones",
                "Consecuencias", "Seguimiento",
            ):
                with self.subTest(caso=numero, seccion=seccion):
                    self.assertIn(f"### {seccion}", cuerpo)
        self.assertIn("son ficticias", self.caso)
        self.assertIn("simulaciones ilustrativas", self.caso.lower())

    def test_plantillas_operativas_existen_y_tienen_lo_esencial(self) -> None:
        for numero, nombre in self.PLANTILLAS.items():
            with self.subTest(plantilla=numero):
                self.assertTrue((RAIZ / "templates" / nombre).exists())
        matriz = (RAIZ / "templates" / self.PLANTILLAS[26]).read_text(encoding="utf-8")
        for nivel in ("S0,", "S1,", "S2,", "S3,", "S4,"):
            self.assertIn(nivel, matriz)
        indicadores = (RAIZ / "templates" / self.PLANTILLAS[32]).read_text(encoding="utf-8")
        self.assertEqual(len(indicadores.strip().splitlines()) - 1, 16)
        registro = (RAIZ / "templates" / self.PLANTILLAS[29]).read_text(encoding="utf-8")
        cabecera = registro.splitlines()[0]
        for columna in (
            "severidad", "hecho_verificado", "alegaciones_no_verificadas",
            "autoridades_informadas", "proxima_actualizacion", "causa_raiz",
        ):
            self.assertIn(columna, cabecera)
        simulaciones = (RAIZ / "templates" / self.PLANTILLAS[33]).read_text(encoding="utf-8")
        for i in range(1, 11):
            self.assertIn(f"### S-{i:02d} ·", simulaciones)

    def test_fuentes_nuevas_registradas_con_fecha_y_uso(self) -> None:
        esperadas = {
            "LEY_19496_BCN", "LEY_19733_BCN", "LEY_20730_BCN", "CT_BCN", "LEY_21643_BCN",
            "LEY_16744_BCN", "LEY_21131_BCN", "LEY_20720_BCN", "LEY_18045_BCN",
            "LEY_21663_BCN", "LEY_21719_BCN", "LEY_21855_BCN", "CP_HONRA_BCN",
        }
        self.assertLessEqual(esperadas, set(self.fuentes))
        for identificador in esperadas:
            with self.subTest(fuente=identificador):
                fuente = self.fuentes[identificador]
                self.assertEqual(fuente["accessed"], "2026-11-25")
                self.assertEqual(fuente["status"], "verificada")
                self.assertTrue(fuente["used_in"])

    def test_matriz_legal_registra_las_normas_nuevas(self) -> None:
        nombres = {n["name"]: n for n in cargar("legal_sources.json")}
        for nombre in ("Ley 21.855", "Ley 19.733", "Ley 20.730"):
            self.assertIn(nombre, nombres)
        self.assertIn("15-10-2027", nombres["Ley 21.719"]["scope"])


FORMATOS_VALIDOS = {"caso", "numerico", "dialogo", "error", "antes_despues", "decision", "simulacion"}


class ModelosMentalesTest(unittest.TestCase):
    """Cada clase con modelo mental trae un gráfico propio, un ejemplo y su fundamento."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.visuales = {}
        for archivo in sorted((MANIFESTS / "visuales").glob("*.json")):
            for entrada in json.loads(archivo.read_text(encoding="utf-8")):
                cls.visuales[entrada["n"]] = entrada
        cls.clases = {}
        for archivo in sorted((MANIFESTS / "classes").glob("*.json")):
            for entrada in json.loads(archivo.read_text(encoding="utf-8")):
                cls.clases[entrada["n"]] = entrada
        for archivo in sorted((MANIFESTS / "pedagogia").glob("*.json")):
            for entrada in json.loads(archivo.read_text(encoding="utf-8")):
                cls.clases[entrada["n"]].update(entrada)
        cls.fuentes = {
            f["manifest_id"]: f
            for f in json.loads(
                (RAIZ / "sources" / "bibliography.json").read_text(encoding="utf-8")
            )["entries"]
        }
        cls.curriculo = {c["global_class"]: c for c in cargar("curriculum.json")}

    def _carpeta(self, numero: int):
        clase = self.curriculo[numero]
        return next(
            CURRICULUM.glob(f"part-{clase['part']:02d}-*/class-{clase['class']:02d}-*")
        )

    def test_la_parte_14_tiene_su_modelo_mental_y_cada_uno_es_distinto(self) -> None:
        self.assertTrue(set(range(183, 197)) <= set(self.visuales))
        tipos = [self.visuales[n]["tipo"] for n in range(183, 197)]
        # Los dos de «curva» difieren por subtipo; el resto son arquetipos distintos.
        firmas = [
            (v["tipo"], v["datos"].get("tipo")) for v in (self.visuales[n] for n in range(183, 197))
        ]
        self.assertEqual(len(set(firmas)), 14, f"arquetipos repetidos: {tipos}")

    def test_clases_contiguas_nunca_comparten_arquetipo(self) -> None:
        for numero in sorted(self.visuales):
            if numero + 1 in self.visuales:
                with self.subTest(clase=numero):
                    a, b = self.visuales[numero], self.visuales[numero + 1]
                    self.assertNotEqual(
                        (a["tipo"], a["datos"].get("tipo")), (b["tipo"], b["datos"].get("tipo"))
                    )

    def test_cada_modelo_trae_idea_lectura_analogia_ejemplo_y_fundamento(self) -> None:
        for numero, v in sorted(self.visuales.items()):
            with self.subTest(clase=numero):
                self.assertGreaterEqual(len(v["idea"].split()), 14)
                self.assertGreaterEqual(len(v["lectura"].split()), 14)
                self.assertGreaterEqual(len(v["analogia"].split()), 10)
                self.assertGreaterEqual(len(v["ejemplo"].split()), 35)
                self.assertGreaterEqual(len(v["fundamento"]), 1)
                for apoyo in v["fundamento"]:
                    self.assertIn(apoyo["fuente"], self.fuentes)
                    self.assertGreaterEqual(len(apoyo["apoyo"].split()), 12)
                self.assertTrue((self._carpeta(numero) / "modelo-mental.svg").exists())

    def test_los_ejemplos_numericos_se_declaran_ilustrativos(self) -> None:
        for numero, v in sorted(self.visuales.items()):
            if re.search(r"\d", v["ejemplo"]):
                with self.subTest(clase=numero):
                    self.assertRegex(v["ejemplo"], r"ilustrativ")

    def test_el_desarrollo_practico_no_repite_el_fondo_del_asunto(self) -> None:
        for numero in sorted(self.visuales):
            fondo = set(re.findall(r"\w{5,}", self.clases[numero]["desarrollo"].lower()))
            practica = set(re.findall(r"\w{5,}", self.clases[numero]["desarrollo2"].lower()))
            solape = len(fondo & practica) / max(len(practica), 1)
            with self.subTest(clase=numero):
                self.assertLess(solape, 0.5, f"solape {solape:.0%}")

    def test_los_libros_del_registro_tienen_isbn_y_se_citan(self) -> None:
        libros = {k: f for k, f in self.fuentes.items() if f["type"] == "book"}
        self.assertGreaterEqual(len(libros), 9)
        for identificador, libro in libros.items():
            with self.subTest(libro=identificador):
                self.assertEqual(len(libro["isbn13"]), 13)
                self.assertEqual(
                    libro["locator"], f"https://openlibrary.org/isbn/{libro['isbn13']}"
                )
                self.assertTrue(libro["used_in"])

    def test_el_svg_es_accesible_y_autocontenido(self) -> None:
        for numero in sorted(self.visuales):
            texto = (self._carpeta(numero) / "modelo-mental.svg").read_text(encoding="utf-8")
            with self.subTest(clase=numero):
                self.assertIn("<title", texto)
                self.assertIn("<desc", texto)
                self.assertIn('role="img"', texto)
                self.assertNotIn("http://www.w3.org/1999/xlink", texto)
                self.assertNotRegex(texto, r"<script|<image|href=\"http")

    def test_el_readme_de_la_clase_trae_las_cinco_piezas_pedagogicas(self) -> None:
        for numero in sorted(self.visuales):
            texto = (self._carpeta(numero) / "README.md").read_text(encoding="utf-8")
            with self.subTest(clase=numero):
                for pieza in (
                    "## 🗺️ Modelo mental:", "**La idea en una frase:**", "(modelo-mental.svg)",
                    "### 5. En qué se apoya",
                ):
                    self.assertIn(pieza, texto)
                self.assertRegex(texto, r"\*\*(Cómo leerlo|Qué mirar primero|Lectura guiada):\*\*")
                self.assertRegex(
                    texto, r"\*\*(Una analogía|Piénsalo así|Para recordarlo|Una imagen cotidiana):\*\*"
                )
                self.assertRegex(texto, r"### 4\. (Caso trabajado|Los números, paso a paso|Una conversación que enseña|Un error y su corrección|Antes y después|Cómo se decide, paso a paso|Pruébalo tú: mini simulación)")
                self.assertIn(self.visuales[numero]["formato"], FORMATOS_VALIDOS)

    def test_los_formatos_pedagogicos_varian_dentro_de_cada_parte(self) -> None:
        por_parte: dict[int, set] = {}
        for numero, v in self.visuales.items():
            por_parte.setdefault(self.curriculo[numero]["part"], set()).add(v["formato"])
        for parte, formatos in por_parte.items():
            with self.subTest(parte=parte):
                self.assertGreaterEqual(len(formatos), 4, f"parte {parte}: {sorted(formatos)}")

    def test_clases_contiguas_no_repiten_formato_pedagogico(self) -> None:
        for numero in sorted(self.visuales):
            if numero + 1 in self.visuales:
                with self.subTest(clase=numero):
                    self.assertNotEqual(
                        self.visuales[numero]["formato"], self.visuales[numero + 1]["formato"]
                    )


if __name__ == "__main__":
    unittest.main()
