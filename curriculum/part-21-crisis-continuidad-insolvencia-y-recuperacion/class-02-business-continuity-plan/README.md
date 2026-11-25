# Clase 282 — Business Continuity Plan

> **Parte 21 · Crisis, continuidad, insolvencia y recuperación** — clase 2 de 14

**Estado de evidencia:** `VERIFICADO-FUENTE` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** definir qué procesos se restablecen primero y con qué recursos<br>
**Entregable:** plan de continuidad con priorización de procesos, recursos mínimos, roles y calendario de ensayos

## 🎯 Propósito

Construir el plan de continuidad sobre un análisis de impacto y ensayarlo, porque un plan nunca probado falla en la ejecución.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —definir qué procesos se restablecen primero y con qué recursos— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **BCP** | Plan de continuidad del negocio. |
| **BIA** | Análisis de impacto que prioriza procesos críticos. |
| **Proceso crítico** | Aquel cuya interrupción produce el mayor daño. |
| **Ensayo** | Ejercicio que verifica que el plan funciona. |

## 🗺️ Modelo mental: Qué se restablece primero cuando la operación se detiene

> **La idea en una frase:** El plan de continuidad se construye sobre el análisis de impacto: primero se determina qué procesos deben restablecerse y en qué orden, y solo después se diseñan las respuestas; un plan nunca ensayado falla.

![Esquema: Qué se restablece primero cuando la operación se detiene](modelo-mental.svg)

**Cómo leerlo:** Cada peldaño es una prioridad. El análisis de impacto decide cuáles procesos son críticos; las respuestas se diseñan para esos y no para todos por igual.

**Para recordarlo:** Es el plan de evacuación de un hospital: primero se salva a quien está en riesgo vital y después se organiza el resto.

## 📖 Desarrollo

### 1. El fondo del asunto

El BCP se construye sobre el análisis de impacto: primero se determina qué procesos deben restablecerse y en qué orden, y solo después se diseñan las respuestas. Un plan nunca ensayado falla en la ejecución, porque las dependencias reales solo aparecen al probarlo.

### 2. Cómo se traduce en la práctica

Haz un análisis de impacto en el negocio: qué procesos son críticos, cuánto tiempo pueden detenerse y qué recursos requieren. Define el orden de restablecimiento y las alternativas (trabajo remoto, local alterno, proveedor de respaldo). Ensaya el plan al menos una vez al año con un escenario realista y registra lo que falló. Actualiza el plan cuando cambie la operación.

### 3. Marco aplicable y quién interviene

- Ley 20.720 sobre reorganización y liquidación de empresas y personas
- Ley 19.983 sobre mérito ejecutivo de la factura para cobranza
- continuidad de negocio: BIA, RTO, RPO y plan de comunicación de crisis

**Autoridades o contrapartes involucradas:** Superintendencia de Insolvencia y Reemprendimiento, Tribunales civiles, Dirección del Trabajo.
**Profesionales de apoyo:** abogado de insolvencia, veedor o liquidador, CFO, comunicaciones. La participación concreta depende del riesgo, del
tamaño de la empresa y de la actividad económica.

### 4. Cómo se decide, paso a paso

Decide con tres preguntas. Uno: ¿qué procesos, si se detienen, causan el mayor daño y en cuánto tiempo? Dos: ¿qué recursos necesita cada uno (personas, sistemas, proveedores, local)? Tres: ¿en qué orden se restablecen? Una empresa de logística descubre que, tras un corte de sistemas, lo crítico es seguir despachando los pedidos urgentes en horas; los reportes de gestión pueden esperar una semana.

### 5. En qué se apoya

- **Normativa oficial consolidada** (Biblioteca del Congreso Nacional · LeyChile): Las normas laborales y comerciales, consultables en la Biblioteca del Congreso Nacional, definen obligaciones que continúan durante una interrupción de la operación.
- **Relaciones laborales y obligaciones del empleador** (Dirección del Trabajo): La Dirección del Trabajo informa los derechos y deberes laborales ante suspensiones temporales de la operación.

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

Plan de continuidad con priorización de procesos, recursos mínimos, roles y calendario de ensayos.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] la priorización proviene de un análisis de impacto
- [ ] existe calendario de ensayos con registro de resultados
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Escribir el plan y no ensayarlo nunca.
- Priorizar procesos por importancia percibida y no por impacto medido.

**Característicos de la parte 21:**

- Esperar a la cesación de pagos para buscar asesoría y perder la opción de reorganización.
- Recortar costos destruyendo la capacidad que permite recuperarse.

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

1. ¿Tu priorización viene de un análisis de impacto o de la percepción de importancia?
2. ¿Cuándo ensayaste el plan por última vez y qué falló?
3. ¿Quién ejecuta el plan si la persona designada no está disponible?

## 🔗 Fuentes oficiales

**Biblioteca del Congreso Nacional · LeyChile — Normativa oficial consolidada**  
<https://www.bcn.cl/leychile/> · verificado 2026-11-05

- *Qué contiene:* Publica el texto oficial y consolidado de leyes, decretos y reglamentos, con la versión vigente a una fecha, el historial de modificaciones y la tramitación que las originó.
- *Cómo leerla:* Usa siempre el selector de versión vigente a la fecha en que ejecutarás el trámite, no la última publicada. Y lee el artículo transitorio: en normas en implantación gradual —jornada, datos personales— ahí está la fecha que realmente te aplica.
- *Uso en esta clase:* aporta el marco de «Normativa oficial consolidada» para definir qué procesos se restablecen primero y con qué recursos.

**Dirección del Trabajo — Relaciones laborales y obligaciones del empleador**  
<https://www.dt.gob.cl/> · verificado 2026-11-05

- *Qué contiene:* Concentra el Código del Trabajo aplicado: dictámenes que interpretan la norma en casos concretos, la plataforma Mi DT para registrar contratos y finiquitos, y las guías de fiscalización.
- *Cómo leerla:* Los dictámenes valen más que las guías divulgativas: describen cómo la autoridad resolvió un caso real. Busca por materia y contrasta la fecha, porque un dictamen posterior puede cambiar el criterio anterior.
- *Uso en esta clase:* aporta el marco de «Relaciones laborales y obligaciones del empleador» para definir qué procesos se restablecen primero y con qué recursos.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 281 · Mapa de amenazas y escenarios de crisis](../class-01-mapa-de-amenazas-y-escenarios-de-crisis/README.md) | [Parte 21](../README.md) · [Programa](../../../README.md) | [283 · Disaster Recovery para tecnología →](../class-03-disaster-recovery-para-tecnologia/README.md) |
