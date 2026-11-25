"""Pruebas de los anexos (`annexes/`): profundidad, estructura, figuras, fuentes y acceso."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ANEXOS = RAIZ / "annexes"
MANIFIESTO = RAIZ / "manifests" / "anexos.json"

PALABRAS_MINIMAS = 5000
FAQ_MINIMAS = 15
# Los anexos 1 a 14 describen un tipo de empresa y comparten estructura; los demás
# (empresa en un día, SII, municipalidades) describen un trámite o una institución.
ULTIMO_TIPO_DE_EMPRESA = 14
SECCIONES_BASE = (
    "Ficha rápida", "Historia y evolución", "Marco legal", "Cómo se constituye",
    "Capital, aportes y propiedad", "Administración y gobierno", "Responsabilidad", "Tributación",
    "Obligaciones laborales, contables y sectoriales", "Antes de construir: lista de verificación",
    "Cuándo conviene y cuándo no", "Cuándo llamar a un profesional",
)
SECCIONES_AMPLIACION = (
    "Escenarios resueltos", "Catálogo de errores y cómo corregirlos", "Alternativas y variantes de diseño",
    "Vinculación con otros anexos y con las clases", "Plantillas y listas de trabajo", "Autoevaluación",
)
SECCIONES_FINALES = ("Preguntas frecuentes", "Fuentes y vigencia")
# Anexos ya ampliados (seis secciones de profundización antes de las preguntas frecuentes).
EXTENDIDOS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}


def palabras(texto: str) -> int:
    return len(re.findall(r"\w+", texto))


class AnexosTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifiesto = json.loads(MANIFIESTO.read_text(encoding="utf-8"))
        cls.archivos = sorted(p for p in ANEXOS.glob("[0-9][0-9]-*.md"))

    def numero(self, archivo: Path) -> int:
        return int(archivo.name[:2])

    def test_hay_un_manifiesto_por_anexo(self) -> None:
        en_disco = {self.numero(p) for p in self.archivos}
        en_manifiesto = {a["n"] for a in self.manifiesto}
        self.assertEqual(en_disco, en_manifiesto)

    def test_cada_anexo_tiene_mas_de_5000_palabras(self) -> None:
        for archivo in self.archivos:
            with self.subTest(anexo=archivo.name):
                self.assertGreaterEqual(palabras(archivo.read_text(encoding="utf-8")), PALABRAS_MINIMAS)

    def test_los_tipos_de_empresa_tienen_la_estructura_comun(self) -> None:
        for archivo in self.archivos:
            if self.numero(archivo) > ULTIMO_TIPO_DE_EMPRESA:
                continue
            titulos = tuple(re.findall(r"^## \d+\. (.+)$", archivo.read_text(encoding="utf-8"), re.M))
            with self.subTest(anexo=archivo.name):
                self.assertEqual(titulos[:len(SECCIONES_BASE)], SECCIONES_BASE)
                self.assertEqual(titulos[-2:], SECCIONES_FINALES)
                medio = titulos[len(SECCIONES_BASE):-2]
                if self.numero(archivo) in EXTENDIDOS:
                    self.assertEqual(medio[:len(SECCIONES_AMPLIACION)], SECCIONES_AMPLIACION)
                else:
                    self.assertEqual(medio, ())

    def test_todos_traen_preguntas_frecuentes_y_fuentes(self) -> None:
        for archivo in self.archivos:
            texto = archivo.read_text(encoding="utf-8")
            with self.subTest(anexo=archivo.name):
                self.assertRegex(texto, r"(?m)^## \d+\. Preguntas frecuentes$")
                self.assertRegex(texto, r"(?m)^## \d+\. Fuentes y vigencia$")
                preguntas = re.findall(r"^\*\*\d+\. .+\?\*\*$", texto, re.M)
                self.assertGreaterEqual(len(preguntas), FAQ_MINIMAS)
                self.assertRegex(texto, r"Fecha de consulta de las fuentes:\*\* \d{4}-\d{2}-\d{2}")

    def test_las_fuentes_son_enlaces_https_y_no_se_citan_leyes_sin_enlace(self) -> None:
        for archivo in self.archivos:
            texto = archivo.read_text(encoding="utf-8")
            seccion = texto.split("Fuentes y vigencia", 1)[1]
            enlaces = re.findall(r"\]\((https://[^)\s]+)\)", seccion)
            with self.subTest(anexo=archivo.name):
                self.assertGreaterEqual(len(enlaces), 5)
                self.assertFalse(re.search(r"\]\(http://", seccion))

    def test_las_figuras_referenciadas_existen_y_coinciden_con_el_manifiesto(self) -> None:
        for archivo in self.archivos:
            texto = archivo.read_text(encoding="utf-8")
            usadas = set(re.findall(r"!\[[^\]]+\]\(img/([a-z0-9-]+\.svg)\)", texto))
            entrada = next(a for a in self.manifiesto if a["n"] == self.numero(archivo))
            esperadas = {f"{entrada['slug']}-{k}.svg" for k in range(1, len(entrada["figuras"]) + 1)}
            with self.subTest(anexo=archivo.name):
                self.assertGreaterEqual(len(usadas), 3)
                self.assertEqual(usadas, esperadas)
                for nombre in usadas:
                    self.assertTrue((ANEXOS / "img" / nombre).exists(), nombre)

    def test_las_figuras_tienen_descripcion_accesible(self) -> None:
        for svg in (ANEXOS / "img").glob("*.svg"):
            texto = svg.read_text(encoding="utf-8")
            with self.subTest(figura=svg.name):
                self.assertIn('role="img"', texto)
                self.assertRegex(texto, r"<title[^>]*>.+</title>")
                self.assertRegex(texto, r"<desc[^>]*>.{40,}</desc>")

    def test_las_figuras_de_un_anexo_no_repiten_arquetipo_consecutivo(self) -> None:
        for anexo in self.manifiesto:
            tipos = [f["tipo"] for f in anexo["figuras"]]
            with self.subTest(anexo=anexo["slug"]):
                self.assertTrue(all(a != b for a, b in zip(tipos, tipos[1:])), tipos)

    def test_estan_los_21_anexos_previstos(self) -> None:
        """01 a 14 son tipos de empresa; 15 a 18, trámites e instituciones; 19 a 21, decisiones estratégicas."""
        self.assertEqual({self.numero(p) for p in self.archivos}, set(range(1, 22)))
        palabras_clave = {
            15: "empresa-en-un-dia", 16: "servicio-de-impuestos-internos", 17: "municipalidades", 18: "domicilio-oficinas-virtuales",
            19: "pactos-de-socios", 20: "cambios-de-estructura", 21: "insolvencia",
        }
        for numero, clave in palabras_clave.items():
            with self.subTest(anexo=numero):
                self.assertTrue(any(clave in p.name for p in self.archivos if self.numero(p) == numero))

    def test_los_anexos_se_alcanzan_desde_el_readme_principal(self) -> None:
        readme = (RAIZ / "README.md").read_text(encoding="utf-8")
        self.assertIn("annexes/README.md", readme)
        indice = (ANEXOS / "README.md").read_text(encoding="utf-8")
        for archivo in self.archivos:
            with self.subTest(anexo=archivo.name):
                self.assertIn(f"]({archivo.name})", indice)

    def test_cada_anexo_enlaza_al_anterior_y_al_siguiente(self) -> None:
        archivos = sorted(self.archivos, key=self.numero)
        for i, archivo in enumerate(archivos):
            texto = archivo.read_text(encoding="utf-8")
            with self.subTest(anexo=archivo.name):
                self.assertIn("](README.md)", texto)
                self.assertIn("## En 60 segundos", texto)
                self.assertIn("## Para seguir leyendo", texto)
                self.assertEqual(texto.count("**Navegación:**"), 2)
                if i:
                    self.assertIn(f"]({archivos[i - 1].name})", texto)
                if i < len(archivos) - 1:
                    self.assertIn(f"]({archivos[i + 1].name})", texto)

    def test_el_readme_principal_describe_cada_anexo(self) -> None:
        readme = (RAIZ / "README.md").read_text(encoding="utf-8")
        self.assertIn("| N.º | Anexo | Qué encontrarás |", readme)
        for anexo in self.manifiesto:
            with self.subTest(anexo=anexo["n"]):
                self.assertGreaterEqual(len(anexo["descripcion"].split()), 15)
                self.assertEqual(len(anexo["resumen"]), 5)
                self.assertGreaterEqual(len(anexo["relacionados"]), 3)
                self.assertIn(anexo["descripcion"], readme)

    def test_los_ejemplos_numericos_se_declaran_ilustrativos(self) -> None:
        for archivo in self.archivos:
            texto = archivo.read_text(encoding="utf-8")
            if re.search(r"\*\*Ejemplo ilustrativo", texto):
                continue
            with self.subTest(anexo=archivo.name):
                self.assertRegex(texto, r"ilustrativ")

    def test_no_se_afirman_leyes_inexistentes_sobre_sociedades_bic(self) -> None:
        """Chile no tiene ley de sociedades BIC publicada; ningún anexo debe sugerirla como vigente."""
        for archivo in self.archivos:
            texto = archivo.read_text(encoding="utf-8").lower()
            with self.subTest(anexo=archivo.name):
                if "beneficio e interés colectivo" in texto:
                    self.assertRegex(texto, r"no (existe|hay|cuenta)[^.]{0,120}(ley|régimen)")


if __name__ == "__main__":
    unittest.main()
