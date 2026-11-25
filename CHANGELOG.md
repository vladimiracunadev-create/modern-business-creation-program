# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).
Versionado según [SemVer](https://semver.org/lang/es/).

## [Sin publicar]

### Añadido

- **17 anexos de profundidad** en `annexes/` (más de 5.000 palabras cada uno, 82 figuras SVG, fuentes con
  enlace oficial, lista «antes de construir» y 20 preguntas frecuentes): persona natural con giro (01), EIRL (02),
  sociedad limitada (03), colectiva comercial (04), comandita simple y por acciones (05), SpA (06), anónima
  cerrada (07) y abierta (08), cooperativa (09), sociedad de garantía recíproca (10), sociedad civil (11),
  corporaciones, asociaciones y fundaciones (12), Estatuto Pyme (13), sucursal de sociedad extranjera (14),
  Empresa en un Día / Registro de Empresas y Sociedades (15), Servicio de Impuestos Internos (16) y
  municipalidades (17). Se redactaron sobre el texto de las leyes leído en la Biblioteca del Congreso Nacional
  (fecha de consulta 2026-11-25). No existe en Chile una ley de sociedades BIC, por lo que no hay anexo sobre
  ese tipo y una prueba impide afirmarla.
- Acceso desde el README principal y desde `docs/01_COMPANY_TYPES_CHILE.md`; páginas propias en el sitio.
- `scripts/generar_anexos.py` (con `--check` en CI) renderiza las figuras desde `manifests/anexos.json` y
  `tests/test_anexos.py` (12 pruebas) exige profundidad, secciones, preguntas frecuentes, fuentes y figuras.

### Corregido en el motor de figuras

- Motor de SVG: texto de bajo contraste en los peldaños oscuros de la escalera, etiquetas del embudo que se
  superponían y títulos que desbordaban su caja en el mapa de actores (afectaba también a algunas clases).

- **Modelo mental SVG propio en cada una de las 336 clases** (`modelo-mental.svg`), generado desde
  `manifests/visuales/` con 14 arquetipos (matriz, embudo, ciclo, escalera, balanza, línea de
  tiempo, capas, árbol de decisión, mapa de actores, curva, semáforo, barras, flujo y
  diagrama de Venn). Clases consecutivas nunca comparten arquetipo, y cada SVG es accesible
  y autocontenido.
- **Pedagogía variable por clase**: idea en una frase, cómo leer el esquema, analogía, ejemplo
  trabajado en siete formatos (caso, numérico, diálogo, error, antes/después, decisión,
  simulación), desarrollo práctico sin repetir el fondo del asunto y bloque «En qué se apoya».
- 127 fuentes en el registro (libros con ISBN-13 válido verificado en Open Library; sin páginas
  citadas). Ningún libro queda sin citar. Los ejemplos numéricos son ilustrativos.
- Pruebas: 71 (antes 61), incluida la variación de arquetipos y formatos entre clases contiguas.

- Guía `docs/22_REPUTACION_CRISIS_Y_CONFIANZA.md` (21 secciones): reputación inicial, asuntos
  públicos, reclamos y controversias, política de comunicación, matriz de severidad S0–S4, roles,
  sustitutos, comité de crisis por tamaño y vocería, control de daños en 72 horas, fallas
  operacionales, protección de personas afectadas, obligaciones con autoridades, conflictos
  laborales y con proveedores, comunicación de liquidez, recuperación con indicadores y
  simulaciones. Separa **obligación legal**, **recomendación profesional** y **medida voluntaria**.
- Caso 23 (`case-studies/23-…`): siete simulaciones ilustrativas (microempresa con controversia
  pública, falla de producto, publicaciones falsas, filtración de datos, conflicto laboral público,
  pérdida de un socio, liquidez y reclamos), cada una con diagnóstico, responsables, evidencia,
  alternativas, decisiones, consecuencias y seguimiento.
- Nueve plantillas (25 a 33): política de comunicación, matriz de severidad, control de daños,
  escalamiento y vocería, registro de incidentes, plan de respuesta y recuperación, guías por
  audiencia, 16 indicadores de confianza y diez simulaciones de mesa.
- Bloque «Reputación y confianza» en 31 clases existentes (partes 11, 12, 13, 14, 19, 20 y 21),
  renderizado desde el campo `reputacion` de los manifiestos, sin crear clases ni alterar la
  numeración (336). Conserva intacto el bloque «Protección del conocimiento».
- Trece fuentes verificadas el 2026-11-25 (BCN) y cuatro normas en la matriz legal (Leyes 21.855,
  19.733 y 20.730 y Código Penal arts. 412 a 431).
- Diez pruebas de regresión (`ReputacionCrisisTest`), entre ellas una que impide que la vigencia de
  la Ley 21.719 vuelva a la fecha derogada.
- Guía `docs/21_INTELIGENCIA_ECONOMICA_Y_PROTECCION_DEL_CONOCIMIENTO.md` sobre inteligencia
  económica y competitiva lícita, espionaje industrial, ingeniería social, HUMINT, secretos
  comerciales, terceros, contrainteligencia, protección de ejecutivos y crisis, con tres niveles de
  empresa, ejemplos sectoriales, terminología bilingüe, evaluación, matriz de contenidos y marco
  legal chileno separado en obligaciones, recomendaciones y medidas voluntarias.
- Caso 22 (`case-studies/22-nvidia-…`): sospecha de inteligencia extranjera sobre un ejecutivo de
  NVIDIA, tratada como investigación **no concluida** (corte 2026-11-12), que separa información
  oficialmente conocida, sospecha o alegación, posición de parte y desconocido.
- Bloque «Protección del conocimiento» en 38 clases existentes, renderizado por el generador desde
  el campo `proteccion` de los manifiestos, sin crear clases ni alterar la numeración (336).
- Trece fuentes en el registro (textos consolidados de la BCN, casos del Departamento de Justicia
  de EE. UU., informe del CRS y prensa del caso NVIDIA); una queda `pendiente` por PDF no abierto.
- La Ley 20.169 y los arts. 284 a 284 sexies del Código Penal entran a la matriz legal; el
  watchlist incorpora el seguimiento del caso NVIDIA.
- Diez pruebas de regresión (`ProteccionConocimientoTest`).

### Corregido

- **Vigencia de la Ley 21.719.** La Ley 21.855 (Diario Oficial, 23-11-2026) sustituyó el 1-12-2026
  por el **15-10-2027**. Se corrigió en clases, partes, glosario, guías, manifiestos y README. El
  título histórico de la clase 147 conserva «desde 1-dic-2026» para no alterar la numeración ni los
  enlaces; su contenido ya refleja la fecha nueva.
- «Secreto empresarial» pasa a «secreto comercial», la denominación vigente en la Ley 19.039 (DFL 4
  de 2022) y en el Código Penal (clases 131 y 151, glosario, parte 11 y activos).

### Cambiado

- Se integra la Ley 21.850 (Diario Oficial, 17-10-2026) sin crear clases ni alterar la numeración:
  guía `docs/20_LEY_21850_RECONSTRUCCION_NACIONAL.md` con vigencias, ejemplos numéricos, casos,
  taller, errores y pendientes de revisión humana.
- Quince clases existentes (régimen, Pro Pyme, Operación Renta, fiscalización, contratación,
  remuneraciones, SENCE, exportación de servicios, compliance tributario y crisis de caja) enlazan la
  guía desde un bloque «Actualización normativa»; el generador lo renderiza desde `actualizacion`.
- Se registran el texto del Diario Oficial y la ficha de LeyChile en el registro de fuentes y la
  ley en la matriz legal; la ficha BCN queda `pendiente` porque no cargó en la consulta automática.
- El README ("Contexto normativo 2026"), STATUS, ROADMAP y el marco aplicable de las partes 7, 12,
  17 y 18 incorporan la Ley 21.850; se corrigen cifras vencidas (páginas del manual y del sitio,
  manuales, fuentes y cuerpos normativos).
- Se revalida el registro de fuentes (2026-11-05: 45 de 48 resuelven; ProChile pasa a su URL vigente,
  `sma`, `sec-madoff-controls` y `nyt-medvi-profile` siguen `pendiente` por certificado o bloqueo 403).
  La prueba de MEDVi deja de fijar la fecha de consulta, que avanza con cada revalidación.
- Se incorpora el calendario 2027 a 2030: PPM transitorio del régimen general (7.º transitorio), PPM
  Pro Pyme de 0,23 % desde 2029, tasa Pro Pyme de 15 % en 2028 (Circular SII 53 de 2025), ganancia de
  capital bursátil, arriendo de viviendas económicas y la cotización adicional del empleador de la
  Ley 21.735 hasta 6,4 % en agosto de 2030; las clases 96 y 161 enlazan los nuevos apartados.
- Las circulares y resoluciones del SII, el decreto de catálogo de servicios del conocimiento y la
  tasa Pro Pyme posterior a 2027 quedan marcados como pendientes, no como normas aplicables.

- Se incorpora MEDVi como caso empresarial transversal para estudiar una empresa AI-native con
  estructura interna mínima, IA, contratistas, proveedores clínicos, farmacias, plataformas y
  socios comerciales, sin reducir la operación a «dos personas hicieron todo».
- El expediente separa hechos, cifras reportadas, alegaciones, actuación regulatoria, respuesta
  corporativa, interpretación y lección; distingue medicamentos aprobados, genéricos aprobados,
  compounded y falsificados con fuentes FDA consultadas el 04-10-2026.
- Nueve clases existentes enlazan el caso desde modelo empresarial, afiliados, contratación,
  responsabilidad, due diligence, controles, founder bottleneck, crisis y riesgo de persona clave.
- Se añade una due diligence progresiva de US$5 millones, matrices de tensión y pruebas de
  regresión para conservar las fuentes, la precisión farmacéutica y los enlaces curriculares.
- El caso incorpora un panel ejecutivo, iconografía semántica y siete diagramas Mermaid para
  visualizar modelo operativo, cronología, red externa, precisión farmacéutica, founder bottleneck,
  due diligence y respuesta de crisis también en el sitio publicado.
- Se conectan estudio de mercado, conocimiento del cliente, estructura de costos, modelo de
  negocios, alianzas y proyección mediante un único expediente progresivo de viabilidad, sin
  crear partes ni clases nuevas.
- Las plantillas de mercado, entrevistas, Canvas, costos, caja y economía unitaria distinguen
  evidencia, hipótesis, interpretación, fuente, fecha, confianza, riesgo y escenario cuando
  corresponde; incluyen un ejemplo financiero verificable en tres escenarios.
- Se amplían las clases existentes que ya enseñaban estas materias y el capstone las integra en
  una decisión de inversión; seis pruebas nuevas evitan que la conexión vuelva a fragmentarse.
- Se adopta un modelo de licencias por material: MIT para código y CC BY-NC-SA 4.0 para el
  contenido educativo, las plantillas y las metodologías originales.
- Se documentan el uso comercial, las marcas, los componentes de terceros y el historial de la
  transición, preservando las concesiones MIT de las revisiones publicadas hasta `c8a17b9`.
- El README, las contribuciones y el manual generado muestran el nuevo alcance de forma expresa.
- `pypdf` se actualiza a 6.21.4 (antes 6.19.0) para cerrar las 18 alertas que `pip-audit` volvió a
  reportar en el workflow de seguridad.
- El workflow mensual de fuentes conserva la rama y emite una advertencia, en vez de fallar,
  cuando la configuración del repositorio impide que GitHub Actions cree el PR automático.

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
- **Cierre del README** al estilo del resto de los programas: bloque centrado con enlaces rápidos
  —empezar por la clase 001, sitio, glosario, PDF y roadmap—, llamada a dar estrella y badges
  sociales del repositorio.
- **Alias estable `downloads/manual.pdf`** publicado por el sitio junto al PDF versionado, para
  que los enlaces del README no queden en 404 al subir de versión.

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
