# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).
Versionado según [SemVer](https://semver.org/lang/es/).

## [1.2.0] — 2026-08-13

### Añadido

- **Las 24 partes agrupadas en 6 etapas.** `manifests/etapas.json` define cada etapa con su
  color, su promesa —qué sabes hacer al terminarla— y su salida. El README y `CURRICULUM.md`
  presentan las partes por etapa en vez de como una tabla plana de 24 filas.
- **Columna «contenido central» por parte.** Cada parte declara su temario en una línea, de modo
  que la tabla dice de qué trata sin abrir el README, y un nombre corto para rotular el mapa.
- **Bloque de partes del README generado.** El generador sustituye el contenido entre los
  marcadores `<!-- partes:inicio -->` y `<!-- partes:fin -->`, y `--check` falla si quedó
  desincronizado: la tabla de partes ya no puede divergir del manifiesto.
- **Sección «Calidad y CI»** con la tabla de los tres workflows y qué cubre cada uno, más los
  comandos equivalentes para correr los mismos validadores en local.
- **Sección «Qué es y qué no es este programa»** a dos columnas, y cierre con la idea fuerza.
- Cada README de parte muestra ahora a qué etapa pertenece, su salida y su contenido central.

### Cambiado

- El mapa del recorrido de `CURRICULUM.md` se dibuja desde `etapas.json`: si cambia la
  agrupación de partes, el diagrama la sigue en vez de quedar describiendo otro recorrido.
- `STATUS.md` incorpora las etapas y los controles nuevos.
- Las pruebas suben de 20 a 23: cobertura y consecutividad de las etapas, temario y nombre corto
  de cada parte, y sincronía del bloque de partes del README.

## [1.1.0] — 2026-08-13

### Añadido

- **Capa pedagógica en las 336 clases.** `manifests/pedagogia/` aporta a cada clase un propósito
  en prosa, un segundo bloque de desarrollo que baja el concepto a la práctica chilena y tres
  preguntas de comprobación contrastables contra el propio negocio. El currículo pasa de 281.184
  a **419.186 palabras**, con mediana de 1.239 por clase.
- **360 diagramas mermaid.** Uno por clase, construido con sus propios conceptos, decisión y
  entregable, de modo que no hay dos iguales; y uno por parte, dibujado a mano para el flujo de
  esa materia. El validador rechaza cualquier README sin diagrama.
- **Narrativa por parte.** `manifests/part_content.json` añade a las 24 partes lema, tres
  párrafos de contexto, mapa visual, conexiones con las demás partes y pauta bibliográfica.
- **Fuentes explicadas.** Las 32 fuentes oficiales traen ahora *qué contienen* y *cómo leerlas*,
  con fecha de verificación. Las clases dejan de enlazar la fuente para pasar a enseñarla.
- **Glosario maestro.** `docs/19_GLOSSARY.md` se genera desde los 1.344 conceptos del currículo:
  1.251 términos con definición operacional y enlace a la clase donde se introducen. Cada parte
  incluye además el glosario de sus propias clases.
- **Manual en PDF.** `scripts/generar_manual.py` compila con reportlab el manual integral de
  **1.541 páginas** y un PDF por parte, con portada, índice, encabezado corrido y numeración.
  Los diagramas se transcriben a esquema legible en vez de volcarse como sintaxis.
- **Diagramas en el sitio.** Los bloques mermaid se renderizan en el navegador y degradan a
  código legible si la librería no carga; el tema del diagrama sigue al tema de la página.
- Nuevas fuentes en el catálogo: SUSESO, Superintendencia de Insolvencia, INE y Banco Central.
- `requirements.txt` con dependencias fijadas y `pip-audit` en el workflow de seguridad.

### Cambiado

- **Rediseño visual de todos los README.** Cabecera con estado, decisión y entregable; secciones
  con emoji; tablas para conceptos, talleres y errores; alertas de GitHub; y tabla de navegación
  anterior/índice/siguiente al pie.
- `CURRICULUM.md` abre con el mapa del recorrido completo y añade la idea central de cada parte.
- El validador de estructura pasa a exigir las secciones nuevas y la presencia del diagrama.
- El control de dependencias del workflow de seguridad deja de exigir cero dependencias y pasa a
  exigir que todas estén fijadas a versión exacta y auditadas.

## [1.0.0] — 2026-08-13

### Añadido

- **Contenido específico por clase.** `manifests/classes/` con 336 entradas: 4 conceptos con
  definición operacional, párrafo de desarrollo, decisión que la clase habilita, entregable
  concreto, errores propios y criterios de aceptación verificables.
- **Paquetes de conocimiento por parte.** `manifests/part_packs.json` con resumen, resultados,
  marco normativo, autoridades, profesionales, riesgos, fuentes y estado de evidencia de cada una
  de las 24 partes.
- **Generador del currículo.** `scripts/generar_clases.py` renderiza los 336 README de clase, los
  24 de parte y `CURRICULUM.md` desde los manifiestos, con navegación anterior/siguiente y
  eliminación de carpetas huérfanas. Modo `--check` para el CI.
- **Sitio HTML para GitHub Pages.** `scripts/generar_sitio.py` construye 421 páginas estáticas con
  buscador de clases en cliente, tema claro/oscuro, navegación lateral y cero dependencias
  externas; conversor Markdown propio sin librerías de terceros.
- **Validadores.** `scripts/validar_estructura.py` (coherencia de manifiestos, secciones
  obligatorias, enlaces internos, fuentes https) y `scripts/validar_encoding.py` (UTF-8 sin BOM y
  detección de mojibake por round-trip cp1252).
- **Pruebas.** `tests/` con verificaciones estructurales del currículo y los manifiestos.
- **CI en tres workflows.** `ci.yml` (estructura, sincronía, codificación, markdownlint, build del
  sitio y tests), `security.yml` (gitleaks y bandit) y `deploy-pages.yml` (publicación).
- **Documentación al estándar del resto de los programas.** `STATUS.md` con cifras reproducibles,
  `ROADMAP.md`, `VERSION`, y README con badges, tabla de partes y contrato de clase.
- Configuración de repositorio: `.gitignore`, `.gitattributes`, `.editorconfig`,
  `.markdownlint-cli2.jsonc` y `.gitleaks.toml`.

### Cambiado

- **Reescritura completa del cuerpo de las 336 clases.** Antes compartían el mismo texto de
  plantilla (~200 palabras idénticas salvo el título); ahora cada una tiene contenido propio, con
  787–910 palabras y mediana de 835. Total del currículo: 281.184 palabras.
- `CURRICULUM.md` pasa de lista plana a tabla con rango de clases y estado de evidencia por parte.
- `LICENSE` completa el texto MIT y aclara el régimen de las fuentes oficiales citadas.
- `CONTRIBUTING.md`, `SECURITY.md` y `CODE_OF_CONDUCT.md` pasan de nota breve a política operativa.
- El validador `scripts/validate_repo.py` se reemplaza por los dos validadores especializados.

### Corregido

- Carpeta de clase huérfana en la parte 22 tras el cambio de reglas de slug.
- Enlaces internos rotos entre clases: ahora se generan y se verifican en CI.

## [0.1.0] — 2026-08-07

### Añadido

- Estructura inicial: 24 partes, 336 clases, 20 manuales, 20 líneas de negocio y 24 plantillas.
- Matriz normativa Chile 2026 y catálogo de fuentes oficiales.
- Watchlist de datos personales, jornada de 42 horas, fintech y regímenes Pro Pyme.

[1.2.0]: https://github.com/vladimiracunadev-create/modern-business-creation-program/releases/tag/v1.2.0
[1.1.0]: https://github.com/vladimiracunadev-create/modern-business-creation-program/releases/tag/v1.1.0
[1.0.0]: https://github.com/vladimiracunadev-create/modern-business-creation-program/releases/tag/v1.0.0
[0.1.0]: https://github.com/vladimiracunadev-create/modern-business-creation-program/releases/tag/v0.1.0
