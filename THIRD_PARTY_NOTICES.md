# Avisos de terceros

Este archivo registra materiales y dependencias de terceros identificados en
la auditoría de licencias del 2026-09-22. La licencia del proyecto no sustituye
los términos de sus titulares.

## Fuentes oficiales y obras referenciadas

El currículo cita normas, resoluciones, formularios, dictámenes, guías y
publicaciones de organismos públicos chilenos. Sus localizadores, organismos
responsables y fechas de verificación están registrados en
[`sources/bibliography.json`](sources/bibliography.json) y resumidos en
[`SOURCES.md`](SOURCES.md).

El repositorio no concede derechos sobre esos materiales. Cada fuente conserva
su régimen jurídico, requisitos de atribución, condiciones de reutilización y
versión oficial. Los títulos, enlaces, hechos y breves descripciones incluidos
para identificación tampoco implican patrocinio del organismo correspondiente.

## Componentes y referencias de software

| Componente | Uso en el proyecto | Régimen del tercero |
|---|---|---|
| [ReportLab 5.0.0](https://pypi.org/project/reportlab/5.0.0/) | Generación de los manuales PDF | BSD; copyright de ReportLab Inc. y sus contribuyentes |
| [pypdf 6.16.0](https://pypi.org/project/pypdf/6.16.0/) | Verificación de los PDF generados | BSD-3-Clause; titulares y contribuyentes de pypdf |
| [Mermaid 11.12.0](https://github.com/mermaid-js/mermaid/tree/v11.12.0) | Renderizado de diagramas en el sitio mediante jsDelivr | MIT; copyright de Knut Sveidqvist y contribuyentes |
| [Contributor Covenant 2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) | Inspiración declarada de `CODE_OF_CONDUCT.md` | Texto y atribución del proyecto Contributor Covenant; el documento local es una adaptación |

ReportLab y pypdf son dependencias de construcción y no se copian en este
repositorio. Mermaid se carga desde un CDN en el sitio generado y no se vende ni
se relicencia como parte del contenido educativo.

## Contribuciones futuras

Quien incorpore material de terceros debe identificar el titular, la fuente y
la licencia o base jurídica que permite su uso. No debe marcar ese material
como MIT o CC BY-NC-SA 4.0 si no tiene autoridad para hacerlo. Las reglas de
contribución están en [`CONTRIBUTING.md`](CONTRIBUTING.md).
