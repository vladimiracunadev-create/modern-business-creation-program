# Fuentes

## Jerarquía de fuentes

Este repositorio sigue un orden de preferencia estricto. Una afirmación regulatoria respaldada por
una fuente de nivel inferior cuando existe una superior se considera un defecto de contenido.

| Nivel | Fuente | Uso |
|---:|---|---|
| 1 | **BCN / LeyChile** | Texto legal vigente y consolidado |
| 2 | **Organismo competente** (SII, DT, CMF, INAPI, UAF, Aduanas, SEC, SUBTEL, SEA, SMA, SENCE, SERNATUR, SEREMI de Salud) | Interpretación, formularios, plazos y trámites |
| 3 | **ChileAtiende / Registro de Empresas y Sociedades** | Descripción operativa de trámites |
| 4 | **Instituciones de fomento** (Sercotec, Corfo, ProChile, ChileCompra) | Instrumentos, convocatorias y requisitos |
| 5 | **Estadística oficial** (INE, Banco Central) | Datos de mercado y contexto económico |
| — | Prensa, blogs, consultoras | **No se usan** como respaldo de una afirmación normativa |

## Catálogo

El catálogo completo, con identificador, organismo, tema y URL, vive en
[`manifests/official_sources.json`](manifests/official_sources.json) y se publica en
[`docs/16_OFFICIAL_SOURCE_CATALOG.md`](docs/16_OFFICIAL_SOURCE_CATALOG.md).

Cada clase declara las fuentes que le corresponden; el validador comprueba que todo identificador
citado exista en el catálogo y que la URL sea `https://`.

El mapa de cuerpos normativos por materia está en
[`manifests/legal_sources.json`](manifests/legal_sources.json) y en
[`docs/03_LEGAL_MATRIX_CHILE.md`](docs/03_LEGAL_MATRIX_CHILE.md).

## Regla de vigencia

Las fuentes cambian sin aviso. El material distingue cuatro estados de evidencia y solo el primero
se considera estable:

| Estado | Significado |
|---|---|
| `VERIFICADO-FUENTE` | Referido a fuente oficial primaria o institucional |
| `GUIA-PRACTICA` | Síntesis educativa que debe adaptarse al caso concreto |
| `SECTORIAL` | Aplica solo si la actividad cae en ese sector |
| `DINAMICO` | Tasa, plazo, convocatoria o norma en transición que **debe revisarse a la fecha de ejecución** |

Antes de ejecutar cualquier trámite real, hay que abrir la fuente y confirmar que sigue vigente.

## Fecha de corte

**07-08-2026.** Los cambios normativos posteriores a esa fecha no están incorporados; el
seguimiento de lo que viene está en [`docs/17_2026_WATCHLIST.md`](docs/17_2026_WATCHLIST.md).
