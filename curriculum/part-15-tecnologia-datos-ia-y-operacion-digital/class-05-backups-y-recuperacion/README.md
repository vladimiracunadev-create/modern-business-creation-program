# Clase 201 — Backups y recuperación

> **Parte 15 · Tecnología, datos, IA y operación digital** — clase 5 de 14

**Estado de evidencia:** `DINAMICO` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** definir RPO, RTO y calendario de pruebas de restauración<br>
**Entregable:** política de respaldos con RPO, RTO, esquema de copias y registro de pruebas de restauración

## 🎯 Propósito

Probar la restauración con cronómetro, porque un respaldo no probado es una hipótesis y no un respaldo.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —definir RPO, RTO y calendario de pruebas de restauración— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **Respaldo** | Copia de datos que permite restaurar. |
| **RPO** | Máxima pérdida de datos aceptable, medida en tiempo. |
| **RTO** | Tiempo máximo aceptable para restaurar el servicio. |
| **Prueba de restauración** | Ejercicio que verifica que el respaldo funciona. |

## 🗺️ Modelo mental: RPO y RTO sobre la línea de una falla

> **La idea en una frase:** Un respaldo no probado no es un respaldo: la prueba de restauración debe hacerse periódicamente y con cronómetro, porque el tiempo real de recuperación casi siempre supera al estimado.

![Esquema: RPO y RTO sobre la línea de una falla](modelo-mental.svg)

**Cómo leerlo:** La línea muestra los dos relojes de una falla. A la izquierda de la falla está lo que podrías perder; a la derecha, lo que tardas en volver. Ambos deben decidirse antes, no durante.

**Piénsalo así:** Es el seguro de un auto: importa cuánto cubre y cuánto tarda en pagar, y solo lo sabes de verdad si probaste el procedimiento.

## 📖 Desarrollo

### 1. El fondo del asunto

Un respaldo no probado no es un respaldo. La prueba de restauración debe hacerse periódicamente y con cronómetro, porque el RTO real casi siempre supera al estimado. La regla mínima es tener al menos una copia fuera del sistema principal y fuera de línea.

### 2. Cómo se traduce en la práctica

Define para cada sistema el RPO y el RTO aceptables según el costo de perder datos y de estar detenido. Aplica la regla mínima de tres copias, en dos medios distintos y una fuera del lugar. Prueba la restauración cada trimestre con cronómetro y registra los resultados. Guarda los procedimientos escritos fuera de los sistemas que se restauran.

### 3. Marco aplicable y quién interviene

- Ley 21.663 Marco de Ciberseguridad y su reglamentación
- Ley 21.719 en lo relativo a tratamiento automatizado y decisiones basadas en datos
- controles de referencia tipo CIS Controls y NIST CSF adaptados a pyme

**Autoridades o contrapartes involucradas:** ANCI, CSIRT Nacional, Agencia de Protección de Datos Personales (en implementación).
**Profesionales de apoyo:** responsable de TI, consultor de ciberseguridad, analista de datos, abogado de datos. La participación concreta depende del riesgo, del
tamaño de la empresa y de la actividad económica.

### 4. Los números, paso a paso

Una tienda hace respaldos cada noche, es decir, un RPO de hasta 24 horas: si falla a las 18:00, pierde las ventas del día. Calcula que perder un día cuesta 2 millones y que cada hora sin sistema cuesta 300.000. Prueba la restauración con cronómetro: tarda 9 horas, no las 2 que estimaba, y descubre que un archivo clave no estaba en el respaldo. Cambia a respaldos cada hora y añade una copia fuera de la oficina (cifras ilustrativas).

### 5. En qué se apoya

- **Site Reliability Engineering** (O'Reilly): Beyer y sus coautores tratan la planificación de recuperación y las pruebas periódicas de procedimientos como parte de la confiabilidad de un servicio.
- **The Phoenix Project** (IT Revolution): Kim y sus coautores muestran, en forma de novela, cómo la preparación y la práctica de la recuperación de sistemas cambian el resultado de una crisis operacional.

*Las lecturas de apoyo ofrecen marcos conceptuales; lo que exige la ley chilena se verifica en las fuentes oficiales de esta clase.*

## 🧪 Taller guiado

Aplica esta clase a **una** de las siguientes líneas de negocio y repite después el ejercicio con
una segunda línea de carga regulatoria distinta:

| Línea | Carga regulatoria |
|---|---|
| SaaS B2B con IA | media |
| Servicios profesionales | baja |
| E-commerce D2C | media |
| Alimentos o foodtech | alta |
| Exportación de servicios | media |
| Fintech regulada | alta |
| Construcción o servicios técnicos | alta |

**Secuencia de trabajo:**

1. Delimita el contexto: actividad económica, escala, comuna y etapa de la empresa.
2. Reúne los antecedentes que la decisión exige y anota la fecha de cada fuente.
3. Identifica las alternativas reales, incluida la de no hacer nada.
4. Evalúa el impacto en mercado, caja, personas, regulación y operación.
5. Toma la decisión y regístrala con sus supuestos.
6. Produce el entregable.
7. Contrástalo contra el criterio de aceptación.
8. Anota lo que requiere validación profesional y programa su revisión.

### 📦 Entregable

Política de respaldos con rpo, rto, esquema de copias y registro de pruebas de restauración.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] existe registro de al menos una restauración probada
- [ ] hay copia fuera del entorno principal
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Confiar en respaldos automáticos nunca probados.
- Mantener todas las copias en el mismo entorno que los datos originales.

**Característicos de la parte 15:**

- Respaldos que nunca se probaron y no restauran cuando se necesitan.
- Accesos compartidos y credenciales que sobreviven a la salida de una persona.

## 🇨🇱 Checklist Chile

- [ ] ¿existe norma o autoridad específica para esta materia?
- [ ] ¿la fuente consultada está vigente a la fecha de ejecución?
- [ ] ¿se activa algún trámite ante el SII?
- [ ] ¿se activa algún requisito municipal o sectorial?
- [ ] ¿afecta a consumidores o al tratamiento de datos personales?
- [ ] ¿afecta a trabajadores o a la seguridad y salud en el trabajo?
- [ ] ¿afecta a impuestos, contabilidad o caja?
- [ ] ¿afecta a contratos o a propiedad intelectual?
- [ ] ¿requiere renovación, reporte periódico o revalidación?

## ❓ Preguntas de comprobación

1. ¿Cuándo restauraste por última vez desde tu respaldo y cuánto demoró?
2. ¿Tienes alguna copia fuera de línea y fuera del entorno principal?
3. ¿Cuánta información puedes permitirte perder y tu RPO lo respeta?

## 🔗 Fuentes oficiales

**Biblioteca del Congreso Nacional · LeyChile — Normativa oficial consolidada**  
<https://www.bcn.cl/leychile/> · verificado 2026-11-05

- *Qué contiene:* Publica el texto oficial y consolidado de leyes, decretos y reglamentos, con la versión vigente a una fecha, el historial de modificaciones y la tramitación que las originó.
- *Cómo leerla:* Usa siempre el selector de versión vigente a la fecha en que ejecutarás el trámite, no la última publicada. Y lee el artículo transitorio: en normas en implantación gradual —jornada, datos personales— ahí está la fecha que realmente te aplica.
- *Uso en esta clase:* aporta el marco de «Normativa oficial consolidada» para definir RPO, RTO y calendario de pruebas de restauración.

**Corporación de Fomento de la Producción — Innovación, inversión y garantías**  
<https://www.corfo.cl/> · verificado 2026-11-05

- *Qué contiene:* Reúne los instrumentos de fomento a la innovación y la inversión, incluidos programas de capital semilla, escalamiento, garantías y cobertura de riesgo para el sistema financiero.
- *Cómo leerla:* Filtra por etapa de la empresa antes que por monto. Y verifica el componente de innovación que exige cada instrumento: presentar una expansión comercial como innovación es la causa más común de rechazo.
- *Uso en esta clase:* aporta el marco de «Innovación, inversión y garantías» para definir RPO, RTO y calendario de pruebas de restauración.

**O'Reilly — Site Reliability Engineering**  
<https://openlibrary.org/isbn/9781491929124> · verificado 2026-11-25

- *Qué contiene:* Prácticas de confiabilidad de servicios de Google: objetivos de nivel de servicio, presupuesto de error y gestión de incidentes.
- *Cómo leerla:* Úsalo como marco conceptual para entender el porqué de la práctica, nunca como prueba de lo que exige la ley chilena; para eso están las fuentes oficiales de la clase.
- *Uso en esta clase:* aporta el marco de «Site Reliability Engineering» para definir RPO, RTO y calendario de pruebas de restauración.

**IT Revolution — The Phoenix Project**  
<https://openlibrary.org/isbn/9781950508921> · verificado 2026-11-25

- *Qué contiene:* Novela sobre operaciones de tecnología, flujo de trabajo y los orígenes de DevOps. Se usa como lectura de apoyo conceptual y no como fuente normativa.
- *Cómo leerla:* Úsalo como marco conceptual para entender el porqué de la práctica, nunca como prueba de lo que exige la ley chilena; para eso están las fuentes oficiales de la clase.
- *Uso en esta clase:* aporta el marco de «The Phoenix Project» para definir RPO, RTO y calendario de pruebas de restauración.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 200 · Cloud, hosting y continuidad](../class-04-cloud-hosting-y-continuidad/README.md) | [Parte 15](../README.md) · [Programa](../../../README.md) | [202 · Ciberseguridad por capas para pyme →](../class-06-ciberseguridad-por-capas-para-pyme/README.md) |
