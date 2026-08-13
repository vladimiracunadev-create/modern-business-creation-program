# Roadmap

El programa está completo en cobertura: las 24 partes y las 336 clases existen, se generan desde
manifiestos y pasan los controles automáticos. Lo que sigue es profundidad, verificación y
material complementario.

## Hecho — v1.1.0

- [x] 24 partes y 336 clases generadas desde `manifests/`, sin contenido duplicado entre clases.
- [x] Contenido propio por clase: 4 conceptos operacionales, desarrollo, decisión habilitada, entregable, errores y criterios de aceptación.
- [x] 24 paquetes de conocimiento por parte con marco normativo, autoridades, profesionales y riesgos.
- [x] 20 manuales transversales, 20 casos sectoriales y 24 plantillas operativas.
- [x] Catálogo de 28 fuentes oficiales con URL https y 53 cuerpos normativos mapeados.
- [x] Sitio HTML estático de 421 páginas con buscador de clases y tema claro/oscuro, sin dependencias externas.
- [x] CI con validación de estructura, enlaces, codificación, sincronía manifiesto–README, markdownlint, build del sitio y tests.
- [x] Workflow de seguridad con gitleaks, bandit y pip-audit.
- [x] Capa pedagógica: propósito, desarrollo aplicado y preguntas de comprobación en las 336 clases.
- [x] 360 diagramas mermaid — uno por clase y uno por parte — validados en CI.
- [x] Narrativa, mapa visual, glosario y bibliografía en cada una de las 24 partes.
- [x] Fuentes oficiales con qué contienen y cómo leerlas, no solo el enlace.
- [x] Glosario maestro de 1.251 términos generado desde los conceptos del currículo.
- [x] Manual integral en PDF de 1.541 páginas y un PDF por parte, publicados como descarga.

## En curso — v1.2

- [ ] Revalidar contra fuente oficial las clases marcadas `DINAMICO` (partes 11, 15 y 16) y registrar la fecha de verificación por clase.
- [ ] Ampliar cada caso de `case-studies/` con economía unitaria numérica y calendario de habilitación.
- [ ] Añadir ejemplos numéricos trabajados en las partes 08 y 09 (contabilidad y finanzas).
- [ ] Enlazar cada plantilla de `templates/` desde las clases que la usan.

## Planificado — v1.3

- [ ] Autoevaluación por parte: banco de preguntas con corrección automática en el sitio.
- [ ] Calendario de obligaciones periódicas exportable (ICS) según actividad y régimen.
- [ ] Simulador de decisiones societarias y tributarias en Python estándar.

## Explorado y descartado

- **Traducción a inglés.** El valor del programa es la especificidad chilena; una traducción sin
  adaptar la jurisdicción produciría material engañoso.
- **Contenido normativo copiado.** Se cita la fuente y se enseña a leerla; reproducir el texto legal
  garantiza que quede obsoleto sin aviso.
- **Fechas y tasas embebidas como verdad permanente.** Los datos que cambian se marcan `DINAMICO` y
  se remiten a la fuente en lugar de fijarse en el texto.

## Cómo proponer un cambio

Ver [`CONTRIBUTING.md`](CONTRIBUTING.md). En resumen: el contenido se edita en `manifests/`, no en
los `README.md` generados, y toda afirmación regulatoria necesita fuente oficial y fecha de
verificación.
