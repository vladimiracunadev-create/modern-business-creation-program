# Clase 320 — Logística de última milla

> **Parte 23 · Estudios de líneas de negocio reales 2026** — clase 12 de 14

**Estado de evidencia:** `SECTORIAL` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** validar la densidad necesaria y resolver la figura contractual de los repartidores<br>
**Entregable:** modelo de última milla con densidad requerida, costo por entrega y análisis de la relación laboral

## 🎯 Propósito

Calcular la densidad de ruta necesaria y resolver la figura contractual de los repartidores antes de escalar cobertura.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —validar la densidad necesaria y resolver la figura contractual de los repartidores— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **Última milla** | Tramo final de entrega al destinatario. |
| **Densidad de ruta** | Cantidad de entregas por kilómetro recorrido. |
| **Costo por entrega** | Costo total dividido por entregas efectivas. |
| **Relación laboral del repartidor** | Calificación de la figura contractual. |

## 🗺️ Modelo mental: Cuántas entregas por ruta justifican el modelo

> **La idea en una frase:** La rentabilidad de la última milla depende de la densidad: sin volumen concentrado, el costo por entrega hace inviable el modelo; la calificación de la relación con los repartidores es otro riesgo estructural.

![Esquema: Cuántas entregas por ruta justifican el modelo](modelo-mental.svg)

**Lectura guiada:** Cada banda es una decisión sobre una zona. Con baja densidad, aumentar el servicio solo aumenta pérdidas. La figura contractual de los repartidores debe resolverse antes de crecer.

**Una analogía:** Es una ruta de bus con pocos pasajeros: cuando va casi vacía, cada viaje cuesta más de lo que recauda.

## 📖 Desarrollo

### 1. El fondo del asunto

La rentabilidad de la última milla depende de la densidad: sin volumen concentrado el costo por entrega hace inviable el modelo. La calificación de la relación con los repartidores es un riesgo laboral relevante en Chile y debe resolverse antes de escalar la operación.

### 2. Cómo se traduce en la práctica

Mide la densidad por zona y horario y calcula el costo por entrega. Concentra tus operaciones donde haya volumen y evita expandirte a zonas deficitarias. Resuelve la figura contractual de los repartidores con asesoría laboral: la ley mira los hechos y no el nombre del contrato. Cumple las obligaciones de seguridad y de seguro de quienes trabajan en la calle.

### 3. Marco aplicable y quién interviene

- matriz de líneas de negocio 2026 del repositorio (manifests/business_lines_2026.json)
- regulación sectorial aplicable según actividad económica
- economía unitaria por modelo: suscripción, proyecto, transacción, retail y servicio

**Autoridades o contrapartes involucradas:** autoridad sectorial según la línea analizada, SII, SERNAC, municipalidad.
**Profesionales de apoyo:** fundador, consultor sectorial, abogado regulatorio, contador. La participación concreta depende del riesgo, del
tamaño de la empresa y de la actividad económica.

### 4. Pruébalo tú: mini simulación

Calcula para una zona: entregas por hora, costo por hora del repartidor y costo por entrega. Si un repartidor cuesta 6.000 pesos la hora y hace tres entregas, cada entrega cuesta 2.000; con seis entregas, 1.000. Define el umbral mínimo de densidad para operar la zona. Después, escribe cómo se contrata a los repartidores y qué señales de subordinación (horarios, supervisión, exclusividad) existen en tu modelo. Los valores del ejercicio son ilustrativos.

### 5. En qué se apoya

- **Relaciones laborales y obligaciones del empleador** (Dirección del Trabajo): La Dirección del Trabajo informa los criterios para calificar la relación entre una plataforma o empresa y quienes reparten.
- **Normativa oficial consolidada** (Biblioteca del Congreso Nacional · LeyChile): El Código del Trabajo y las normas sobre trabajo en plataformas digitales, consultables en la BCN, regulan la relación con los repartidores.

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

Modelo de última milla con densidad requerida, costo por entrega y análisis de la relación laboral.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] la densidad mínima rentable está calculada
- [ ] la figura contractual de los repartidores está analizada con criterio de subordinación
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Escalar cobertura geográfica sin alcanzar densidad rentable.
- Operar con repartidores en figura que en los hechos configura relación laboral.

**Característicos de la parte 23:**

- Entrar a un sector regulado subestimando el costo y el plazo de habilitación.
- Asumir márgenes de referencia internacional que no aplican al mercado chileno.

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

1. ¿Cuántas entregas por kilómetro necesitas para ser rentable?
2. ¿La relación con tus repartidores configura subordinación en los hechos?
3. ¿Qué costo tendría una reclasificación retroactiva de esas relaciones?

## 🔗 Fuentes oficiales

**Dirección del Trabajo — Relaciones laborales y obligaciones del empleador**  
<https://www.dt.gob.cl/> · verificado 2026-11-05

- *Qué contiene:* Concentra el Código del Trabajo aplicado: dictámenes que interpretan la norma en casos concretos, la plataforma Mi DT para registrar contratos y finiquitos, y las guías de fiscalización.
- *Cómo leerla:* Los dictámenes valen más que las guías divulgativas: describen cómo la autoridad resolvió un caso real. Busca por materia y contrasta la fecha, porque un dictamen posterior puede cambiar el criterio anterior.
- *Uso en esta clase:* aporta el marco de «Relaciones laborales y obligaciones del empleador» para validar la densidad necesaria y resolver la figura contractual de los repartidores.

**Biblioteca del Congreso Nacional · LeyChile — Normativa oficial consolidada**  
<https://www.bcn.cl/leychile/> · verificado 2026-11-05

- *Qué contiene:* Publica el texto oficial y consolidado de leyes, decretos y reglamentos, con la versión vigente a una fecha, el historial de modificaciones y la tramitación que las originó.
- *Cómo leerla:* Usa siempre el selector de versión vigente a la fecha en que ejecutarás el trámite, no la última publicada. Y lee el artículo transitorio: en normas en implantación gradual —jornada, datos personales— ahí está la fecha que realmente te aplica.
- *Uso en esta clase:* aporta el marco de «Normativa oficial consolidada» para validar la densidad necesaria y resolver la figura contractual de los repartidores.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 319 · Energía solar y servicios de eficiencia](../class-11-energia-solar-y-servicios-de-eficiencia/README.md) | [Parte 23](../README.md) · [Programa](../../../README.md) | [321 · Turismo de experiencias →](../class-13-turismo-de-experiencias/README.md) |
