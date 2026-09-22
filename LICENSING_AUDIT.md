# Auditoría de licenciamiento

**Repositorio:** `vladimiracunadev-create/modern-business-creation-program`

**Fecha de auditoría:** 2026-09-22

**Revisión base:** `c8a17b9a5d4bf56bf5b59660ca216f3224bb82d4`

## Objetivo y método

La auditoría revisó el árbol versionado, los artefactos generados, el historial
Git y las atribuciones existentes para separar código, contenido original y
material de terceros. Se inspeccionaron `LICENSE`, `README.md`, documentación,
336 clases, 20 casos, 24 plantillas, manifiestos, scripts, pruebas, workflows,
fuentes oficiales registradas, generadores de HTML/PDF y contribuyentes.

También se buscaron afirmaciones actuales que presentaran todo el repositorio
como MIT. Las referencias históricas se conservaron como historia y no se
reescribieron como si el nuevo modelo hubiera existido desde el inicio.

## Inventario auditado

| Superficie | Resultado |
|---|---|
| Licencia anterior | MIT cubría expresamente código, documentación y material original |
| Currículo y clases | 24 partes, 336 clases y 360 archivos Markdown en `curriculum/`; contenido educativo original |
| Casos | 20 estudios sectoriales originales en `case-studies/` |
| Plantillas y checklists | 24 artefactos editables en `templates/`; originales |
| Guías y manuales | 20 documentos Markdown en `docs/` antes de esta transición, más README, currículo, glosario y materiales raíz |
| Metodologías y datos curriculares | 18 manifiestos JSON que alimentan clases, partes, pedagogía y líneas de negocio |
| Código | 7 scripts Python versionados, pruebas, 4 workflows y archivos de configuración; sitio y PDF generados desde estas fuentes |
| Simuladores | No existe un simulador de software autónomo; las simulaciones detectadas son ejercicios o plantillas educativas |
| Documentos oficiales | No se detectaron copias extensas versionadas de formularios o publicaciones oficiales; se registran enlaces, metadatos, citas breves y descripciones |
| Dependencias y obras de terceros | ReportLab, pypdf, Mermaid y la referencia a Contributor Covenant quedaron documentados en `THIRD_PARTY_NOTICES.md` |
| Historial | 13 commits en la revisión base; la licencia MIT apareció desde el primer commit auditado |
| Contribuidores | Un autor y committer en todo el historial: Vladimir Acuña (`vladimir.acuna.dev@gmail.com`) |

Los conteos anteriores describen la revisión base y se conservan como evidencia
histórica de esta auditoría; no son métricas dinámicas del estado futuro.

## Hallazgos

1. `LICENSE` afirmaba que MIT cubría código, documentación y material original.
2. `README.md` repetía esa afirmación en el badge, la tabla de estado y la
   sección de licencia.
3. El generador del manual PDF imprimía una única fila `Licencia: MIT`.
4. El sitio generado heredaba del README el badge, la tabla y el párrafo MIT.
5. `CHANGELOG.md` contiene una referencia histórica correcta a la licencia MIT
   de la publicación inicial; se mantiene como registro del pasado.
6. Las normas y publicaciones oficiales se enlazan y atribuyen por organismo,
   pero la licencia anterior necesitaba separar de manera más visible su régimen.
7. No se encontró una plantilla o metodología que justificara crear una reserva
   propietaria especial; CC BY-NC-SA 4.0 cubre el conjunto original.
8. La rama estaba limpia y `main` coincidía con `origin/main` al iniciar la
   auditoría.
9. La regeneración cambió el manual de 1.549 a 1.551 páginas y el sitio de 426
   a 427 páginas; además, README y `STATUS.md` declaraban 20/23 pruebas cuando
   la suite real contenía 25. Esos marcadores actuales se sincronizaron sin
   alterar la referencia histórica de 23 pruebas en `CHANGELOG.md`.

## Decisiones aplicadas

| Categoría | Decisión |
|---|---|
| Código | MIT, con alcance explícito en `LICENSE` |
| Contenido educativo original | CC BY-NC-SA 4.0 mediante `LICENSE-CONTENT.md` |
| Plantillas y metodologías originales | CC BY-NC-SA 4.0, sin excepciones reservadas actuales |
| Fuentes oficiales y terceros | Exclusión expresa; régimen y atribución originales |
| Uso comercial | Acuerdo separado con Vladimir Acuña para el contenido CC; sin alterar licencias de terceros |
| Marcas | Ningún derecho de marca se concede con MIT o CC |
| Historia | Se preservan íntegramente las concesiones MIT anteriores hasta `c8a17b9` |
| Contribuciones futuras | Licencia de entrada alineada por tipo de aporte en `CONTRIBUTING.md` |

## Límite efectivo de la transición

La transición rige desde el commit que incorpora estos archivos. No intenta
revocar derechos MIT ya concedidos. En especial, la revisión `c8a17b9` y las
anteriores permanecen disponibles bajo sus términos MIT originales. Por ello,
el cambio protege el licenciamiento de la rama y las versiones futuras, pero no
impide la explotación permitida de copias históricas obtenidas bajo MIT.

CC BY-NC-SA 4.0 tampoco convierte en exclusivos hechos, ideas, métodos no
protegibles, textos oficiales o material de terceros. Solo licencia derechos
que Vladimir Acuña está autorizado a conceder sobre el contenido original.

## Archivos de control creados o actualizados

- `LICENSE`
- `LICENSE-CONTENT.md`
- `THIRD_PARTY_NOTICES.md`
- `TRADEMARKS.md`
- `docs/LICENSING_HISTORY.md`
- `docs/COMMERCIAL_USE.md`
- `README.md`
- `STATUS.md`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `scripts/generar_manual.py`

## Verificación

La revisión local terminó con estos resultados:

- 363 archivos generados sincronizados con los manifiestos;
- 336 clases en 24 partes y 427 archivos Markdown con enlaces válidos;
- 470 archivos en UTF-8 sin BOM ni mojibake;
- 32 fuentes oficiales coherentes;
- 25 pruebas estructurales aprobadas;
- 427 archivos aprobados por `markdownlint-cli2` 0.18.1;
- sitio generado con 427 páginas y sin enlaces internos rotos;
- manual integral compilado y verificado: 1.551 páginas, 4,0 MB, portada y
  versión correctas;
- scripts y pruebas Python compilados sin errores;
- `git diff --check` sin errores de espacios.

El CI remoto volverá a ejecutar los controles configurados después del push.
