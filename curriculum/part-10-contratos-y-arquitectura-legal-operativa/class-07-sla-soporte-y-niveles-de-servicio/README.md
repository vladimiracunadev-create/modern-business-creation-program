# Clase 133 — SLA, soporte y niveles de servicio

> **Parte 10 · Contratos y arquitectura legal operativa** — clase 7 de 14

**Estado de evidencia:** `VERIFICADO-FUENTE` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** definir métricas, exclusiones y consecuencias del nivel de servicio<br>
**Entregable:** SLA con métricas medibles, método de medición, exclusiones y créditos de servicio

## 🎯 Propósito

Convertir el SLA en un compromiso medible definiendo método, responsable de medición, exclusiones y consecuencia.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —definir métricas, exclusiones y consecuencias del nivel de servicio— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **SLA** | Acuerdo de nivel de servicio con métricas y compromisos. |
| **Disponibilidad** | Porcentaje de tiempo en que el servicio está operativo. |
| **Tiempo de respuesta y de resolución** | Plazos comprometidos por severidad. |
| **Crédito de servicio** | Compensación por incumplimiento del sla. |

## 🗺️ Modelo mental: Disponibilidad medida y consecuencia pactada

> **La idea en una frase:** Un SLA sin medición no es un compromiso, es una declaración: debe definir cómo se mide, quién mide, qué se excluye y cuál es la consecuencia.

![Esquema: Disponibilidad medida y consecuencia pactada](modelo-mental.svg)

**Qué mirar primero:** Cada banda es un nivel de cumplimiento con su efecto. Los umbrales y créditos son un ejemplo; lo importante es que estén escritos, medidos y con una consecuencia clara.

**Piénsalo así:** Es la garantía de un electrodoméstico: vale por lo que dice y por cómo se hace efectiva, no por el folleto.

## 📖 Desarrollo

### 1. El fondo del asunto

Un SLA sin medición no es un compromiso, es una declaración. Debe definir cómo se mide, quién mide, qué se excluye (mantenimiento programado, fuerza mayor, causas del cliente) y cuál es la consecuencia. El crédito de servicio suele ser el límite de responsabilidad del proveedor.

### 2. Cómo se traduce en la práctica

Define las métricas (disponibilidad, tiempo de respuesta, tiempo de resolución), la forma de medirlas, el responsable de la medición y las exclusiones (mantención programada, fuerza mayor, causas del cliente). Fija créditos de servicio y el derecho de terminar tras incumplimientos reiterados. Establece cómo se reportan los resultados y cada cuánto se revisan.

### 3. Marco aplicable y quién interviene

- Código Civil en materia de obligaciones, contratos y responsabilidad
- Código de Comercio para actos mercantiles
- Ley 19.983 sobre mérito ejecutivo de la factura
- Ley 21.131 sobre pago a treinta días

**Autoridades o contrapartes involucradas:** Tribunales ordinarios, Centros de arbitraje (CAM Santiago).
**Profesionales de apoyo:** abogado comercial, responsable de contratos, finanzas. La participación concreta depende del riesgo, del
tamaño de la empresa y de la actividad económica.

### 4. Antes y después

Antes: un proveedor promete «alta disponibilidad» en su contrato y, tras una caída de 9 horas, el cliente reclama pero no hay métrica ni crédito pactado. Después: un SLA fija 99,9 % medido por un monitor independiente, excluye mantenciones programadas con aviso y establece créditos escalonados. La siguiente caída de 4 horas activa un crédito automático y el proveedor mejora su plan de continuidad (caso ilustrativo).

### 5. En qué se apoya

- **Normativa oficial consolidada** (Biblioteca del Congreso Nacional · LeyChile): El Código Civil y el Código de Comercio regulan las obligaciones contractuales y sus remedios, que fundan la exigibilidad de los créditos de servicio pactados.
- **Site Reliability Engineering** (O'Reilly): Beyer y sus coautores explican los objetivos de nivel de servicio y el presupuesto de error como forma de medir y gestionar la confiabilidad de un servicio.

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

Sla con métricas medibles, método de medición, exclusiones y créditos de servicio.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] cada métrica indica método y responsable de medición
- [ ] las exclusiones están enumeradas de forma cerrada
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Comprometer disponibilidad superior a la que ofrece la infraestructura contratada.
- Definir sla sin especificar quién mide y con qué herramienta.

**Característicos de la parte 10:**

- Aceptar términos y condiciones de un proveedor crítico sin leer la limitación de responsabilidad.
- Operar con orden de compra sin contrato marco en servicios recurrentes.

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

1. ¿Quién mide tu SLA, con qué herramienta y quién resuelve una discrepancia?
2. ¿Puede tu infraestructura sostener la disponibilidad que comprometiste?
3. ¿Están las exclusiones enumeradas de forma cerrada o abierta?

## 🔗 Fuentes oficiales

**Biblioteca del Congreso Nacional · LeyChile — Normativa oficial consolidada**  
<https://www.bcn.cl/leychile/> · verificado 2026-11-05

- *Qué contiene:* Publica el texto oficial y consolidado de leyes, decretos y reglamentos, con la versión vigente a una fecha, el historial de modificaciones y la tramitación que las originó.
- *Cómo leerla:* Usa siempre el selector de versión vigente a la fecha en que ejecutarás el trámite, no la última publicada. Y lee el artículo transitorio: en normas en implantación gradual —jornada, datos personales— ahí está la fecha que realmente te aplica.
- *Uso en esta clase:* aporta el marco de «Normativa oficial consolidada» para definir métricas, exclusiones y consecuencias del nivel de servicio.

**Servicio de Impuestos Internos — Nuevos contribuyentes, inicio de actividades y DTE**  
<https://www.sii.cl/ayudas/nuevos_contribuyentes/boleta-vys-facturador.html> · verificado 2026-11-05

- *Qué contiene:* Reúne el circuito completo del contribuyente nuevo: obtención de RUT, declaración de inicio de actividades, elección de códigos de actividad económica y habilitación para emitir documentos tributarios electrónicos.
- *Cómo leerla:* Sepáralo en dos actos distintos que la página trata seguidos: el RUT identifica, el inicio de actividades habilita. Lo que te bloquea para facturar casi siempre está en el segundo, no en el primero.
- *Uso en esta clase:* aporta el marco de «Nuevos contribuyentes, inicio de actividades y DTE» para definir métricas, exclusiones y consecuencias del nivel de servicio.

**O'Reilly — Site Reliability Engineering**  
<https://openlibrary.org/isbn/9781491929124> · verificado 2026-11-25

- *Qué contiene:* Prácticas de confiabilidad de servicios de Google: objetivos de nivel de servicio, presupuesto de error y gestión de incidentes.
- *Cómo leerla:* Úsalo como marco conceptual para entender el porqué de la práctica, nunca como prueba de lo que exige la ley chilena; para eso están las fuentes oficiales de la clase.
- *Uso en esta clase:* aporta el marco de «Site Reliability Engineering» para definir métricas, exclusiones y consecuencias del nivel de servicio.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 132 · Propiedad intelectual en contratos](../class-06-propiedad-intelectual-en-contratos/README.md) | [Parte 10](../README.md) · [Programa](../../../README.md) | [134 · Limitación de responsabilidad y garantías →](../class-08-limitacion-de-responsabilidad-y-garantias/README.md) |
