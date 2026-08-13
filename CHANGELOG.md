# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).
Versionado según [SemVer](https://semver.org/lang/es/).

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

[1.0.0]: https://github.com/vladimiracunadev-create/modern-business-creation-program/releases/tag/v1.0.0
[0.1.0]: https://github.com/vladimiracunadev-create/modern-business-creation-program/releases/tag/v0.1.0
