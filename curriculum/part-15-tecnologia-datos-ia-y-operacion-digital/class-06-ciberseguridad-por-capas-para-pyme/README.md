# Clase 202 — Ciberseguridad por capas para pyme

> **Parte 15 · Tecnología, datos, IA y operación digital** — clase 6 de 14

**Estado de evidencia:** `DINAMICO` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** implementar los controles básicos que cubren la mayor parte del riesgo<br>
**Entregable:** plan de ciberhigiene con los controles básicos implementados y verificados

## 🎯 Propósito

Implementar los cuatro controles básicos que cubren la mayor parte del riesgo, en vez de invertir en herramientas avanzadas sin base.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —implementar los controles básicos que cubren la mayor parte del riesgo— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **Defensa en capas** | Controles superpuestos que reducen el riesgo acumulado. |
| **Autenticación multifactor** | Verificación con más de un factor. |
| **Actualización** | Aplicación de parches de seguridad. |
| **Concientización** | Formación de las personas frente a ingeniería social. |

## 🗺️ Modelo mental: Cuatro controles que reducen la mayor parte del riesgo

> **La idea en una frase:** Para una pyme, la mayor parte del riesgo se reduce con cuatro controles: doble factor en todos los accesos, actualizaciones al día, respaldos probados y formación básica del equipo.

![Esquema: Cuatro controles que reducen la mayor parte del riesgo](modelo-mental.svg)

**Qué mirar primero:** Cada capa cubre una vía de ataque distinta. Ninguna es perfecta, pero juntas dejan fuera a la mayoría de los ataques oportunistas que afectan a empresas pequeñas.

**Para recordarlo:** Es cerrar una casa: puerta con llave, ventanas con seguro, alarma y vecinos atentos; cada medida es modesta, pero juntas disuaden a la mayoría.

## 📖 Desarrollo

### 1. El fondo del asunto

Para una pyme, la mayor parte del riesgo se reduce con cuatro controles: multifactor en todos los accesos, actualizaciones al día, respaldos probados y formación básica del equipo. Son baratos y se omiten por comodidad, hasta el primer incidente de fraude por correo.

### 2. Cómo se traduce en la práctica

Activa doble factor en correo, finanzas, nube y sistemas críticos. Programa actualizaciones automáticas y revisa los equipos olvidados. Prueba tus respaldos. Capacita a todo el equipo en el reconocimiento de correos y llamadas fraudulentas y comparte ejemplos reales. Define a quién se reporta un incidente. Son controles baratos que se mantienen en el tiempo.

### 3. Marco aplicable y quién interviene

- Ley 21.663 Marco de Ciberseguridad y su reglamentación
- Ley 21.719 en lo relativo a tratamiento automatizado y decisiones basadas en datos
- controles de referencia tipo CIS Controls y NIST CSF adaptados a pyme

**Autoridades o contrapartes involucradas:** ANCI, CSIRT Nacional, Agencia de Protección de Datos Personales (en implementación).
**Profesionales de apoyo:** responsable de TI, consultor de ciberseguridad, analista de datos, abogado de datos. La participación concreta depende del riesgo, del
tamaño de la empresa y de la actividad económica.

### 4. Pruébalo tú: mini simulación

Haz el diagnóstico de tu empresa con cuatro preguntas: ¿cuántas cuentas con acceso a datos importantes tienen doble factor?, ¿cuántos equipos tienen actualizaciones pendientes?, ¿cuándo fue la última prueba de restauración? y ¿cuándo fue la última capacitación sobre correos fraudulentos? Asigna a cada una una nota de 0 a 10 y escribe la acción que mejoraría la peor. Fija una fecha para repetir el diagnóstico en tres meses. El ejercicio es ilustrativo.

### 5. En qué se apoya

- **Ley 21.459 — Delitos informáticos** (Biblioteca del Congreso Nacional): La Ley 21.459 tipifica los delitos informáticos, que son la figura legal de los ataques que estos controles buscan prevenir.
- **Accelerate** (IT Revolution): Forsgren, Humble y Kim muestran evidencia de que prácticas técnicas como la automatización y los controles disciplinados se asocian a mejor desempeño operacional.

*Las lecturas de apoyo ofrecen marcos conceptuales; lo que exige la ley chilena se verifica en las fuentes oficiales de esta clase.*

## 🛡️ Protección del conocimiento: Ingeniería social empresarial

[Guía de inteligencia económica y protección del conocimiento, sección 6](../../../docs/21_INTELIGENCIA_ECONOMICA_Y_PROTECCION_DEL_CONOCIMIENTO.md#6-ingeniería-social-empresarial)

**Lente para esta clase:** Las capas técnicas fallan cuando alguien entrega la clave: incluye en la defensa la capa humana, con reglas simples y respaldo para quien duda.

| Nivel | Medida proporcionada |
|---|---|
| **Emprendedor o microempresa** | Cuatro hábitos: verificar, no compartir claves, reportar lo extraño y no apurarse por la urgencia ajena. |
| **Pyme** | Inducción de ingreso y recordatorio trimestral con ejemplos de pretextos y mensajes fraudulentos. |
| **Gran empresa o multinacional** | Programa de concientización con métricas de reporte y simulacros dirigidos a cargos de alto riesgo. |

**Actividad sin crear sistemas:** Prepara tres ejemplos de mensajes de pretexting dirigidos a tu empresa y explica qué indicador los delataría.

**Términos:** Pretexting (*Pretexting*) · Spear phishing (*Spear Phishing*)

*Enfoque defensivo: reconocer, prevenir, documentar y escalar. No enseña a obtener información de forma indebida; la calificación jurídica de un hecho concreto corresponde a un abogado.*

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

Plan de ciberhigiene con los controles básicos implementados y verificados.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] el multifactor está activo en todos los accesos críticos
- [ ] los controles básicos están verificados, no solo declarados
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Invertir en herramientas avanzadas sin tener multifactor activado.
- Tratar la seguridad como proyecto puntual y no como rutina.

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

1. ¿Tienes multifactor activo en correo, banco y sistemas críticos?
2. ¿Quién verifica que las actualizaciones se aplicaron y con qué frecuencia?
3. ¿Tu equipo sabría reconocer un correo de suplantación de un proveedor?

## 🔗 Fuentes oficiales

**Biblioteca del Congreso Nacional · LeyChile — Normativa oficial consolidada**  
<https://www.bcn.cl/leychile/> · verificado 2026-11-05

- *Qué contiene:* Publica el texto oficial y consolidado de leyes, decretos y reglamentos, con la versión vigente a una fecha, el historial de modificaciones y la tramitación que las originó.
- *Cómo leerla:* Usa siempre el selector de versión vigente a la fecha en que ejecutarás el trámite, no la última publicada. Y lee el artículo transitorio: en normas en implantación gradual —jornada, datos personales— ahí está la fecha que realmente te aplica.
- *Uso en esta clase:* aporta el marco de «Normativa oficial consolidada» para implementar los controles básicos que cubren la mayor parte del riesgo.

**Biblioteca del Congreso Nacional — Ley 21.459 — Delitos informáticos**  
<https://www.bcn.cl/leychile/navegar?idNorma=1177743> · verificado 2026-11-12

- *Qué contiene:* Tipifica el ataque a la integridad de un sistema, el acceso ilícito, la interceptación ilícita, el ataque a datos, la falsificación y el fraude informáticos, la receptación de datos y las circunstancias agravantes, además de reglas de investigación.
- *Cómo leerla:* El acceso ilícito exige superar barreras técnicas o excederse de la autorización; no cubre el uso indebido por quien accede con permiso. «Espionaje informático» es una categoría de estudio, no el nombre de un delito de esta ley.
- *Uso en esta clase:* aporta el marco de «Ley 21.459 — Delitos informáticos» para implementar los controles básicos que cubren la mayor parte del riesgo.

**IT Revolution — Accelerate**  
<https://openlibrary.org/isbn/9781942788379> · verificado 2026-11-25

- *Qué contiene:* Presenta evidencia sobre qué prácticas de ingeniería se asocian con mejor desempeño en la entrega de software.
- *Cómo leerla:* Úsalo como marco conceptual para entender el porqué de la práctica, nunca como prueba de lo que exige la ley chilena; para eso están las fuentes oficiales de la clase.
- *Uso en esta clase:* aporta el marco de «Accelerate» para implementar los controles básicos que cubren la mayor parte del riesgo.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 201 · Backups y recuperación](../class-05-backups-y-recuperacion/README.md) | [Parte 15](../README.md) · [Programa](../../../README.md) | [203 · Gestión de secretos y privilegios →](../class-07-gestion-de-secretos-y-privilegios/README.md) |
