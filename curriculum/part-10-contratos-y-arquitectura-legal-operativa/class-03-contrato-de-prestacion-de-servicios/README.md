# Clase 129 — Contrato de prestación de servicios

> **Parte 10 · Contratos y arquitectura legal operativa** — clase 3 de 14

**Estado de evidencia:** `VERIFICADO-FUENTE` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** definir el estándar de la obligación y el mecanismo de control de cambios<br>
**Entregable:** contrato de servicios con estándar de obligación, entregables, hitos y procedimiento de cambios

## 🎯 Propósito

Definir si la obligación es de medios o de resultado y establecer por escrito el procedimiento de orden de cambio, que es lo que protege el margen.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —definir el estándar de la obligación y el mecanismo de control de cambios— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **Contrato de servicios** | Obligación de hacer con estándar de diligencia o de resultado. |
| **Obligación de medios** | Compromiso de diligencia sin garantizar resultado. |
| **Obligación de resultado** | Compromiso de entregar un resultado determinado. |
| **Orden de cambio** | Documento que modifica alcance, plazo o precio. |

## 🗺️ Flujo de razonamiento

```mermaid
flowchart TB
    C["Contexto del caso<br/>actividad · escala · comuna"]
    C --> A1["Contrato de servicios"]
    C --> A2["Obligación de medios"]
    C --> A3["Obligación de resultado"]
    C --> A4["Orden de cambio"]
    A1 & A2 & A3 & A4 --> D{{"definir el estándar de la<br/>obligación y el mecanismo de<br/>control de cambios"}}
    D --> E["Entregable<br/>contrato de servicios con<br/>estándar de obligación,<br/>entregables, hitos y<br/>procedimiento de cambios"]
    E --> V{"¿Cumple el criterio<br/>de aceptación?"}
    V -->|sí| S["Evidencia archivada<br/>y clase siguiente"]
    V -->|no| C
```

## 📖 Desarrollo

### 1. El fondo del asunto

La distinción entre obligación de medios y de resultado determina cuándo hay incumplimiento. En servicios profesionales conviene pactar medios con entregables definidos; en desarrollos a medida el cliente exigirá resultado. La orden de cambio es lo que protege el margen frente al scope creep.

### 2. Cómo se traduce en la práctica

En servicios profesionales conviene pactar medios con entregables definidos; en desarrollos a medida el cliente exigirá resultado. Aceptar obligación de resultado sobre variables que no se controlan —integraciones de terceros, datos del cliente— es asumir un riesgo que no se puede gestionar.

### 3. Marco aplicable y quién interviene

- Código Civil en materia de obligaciones, contratos y responsabilidad
- Código de Comercio para actos mercantiles
- Ley 19.983 sobre mérito ejecutivo de la factura
- Ley 21.131 sobre pago a treinta días

**Autoridades o contrapartes involucradas:** Tribunales ordinarios, Centros de arbitraje (CAM Santiago).
**Profesionales de apoyo:** abogado comercial, responsable de contratos, finanzas. La participación concreta depende del riesgo, del
tamaño de la empresa y de la actividad económica.

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

Contrato de servicios con estándar de obligación, entregables, hitos y procedimiento de cambios.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] el estándar de la obligación está explícito
- [ ] existe procedimiento escrito de orden de cambio
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Asumir obligación de resultado sobre variables que no se controlan.
- Aceptar cambios de alcance sin orden de cambio ni ajuste de precio.

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

1. ¿Tus contratos comprometen medios o resultado, y sobre qué variables?
2. ¿Qué procedimiento sigues cuando el cliente pide algo fuera de alcance?
3. ¿Cuánto alcance adicional entregaste sin cobrar el último proyecto?

## 🔗 Fuentes oficiales

**Biblioteca del Congreso Nacional · LeyChile — Normativa oficial consolidada**  
<https://www.bcn.cl/leychile/> · verificado 2026-08-19

- *Qué contiene:* Publica el texto oficial y consolidado de leyes, decretos y reglamentos, con la versión vigente a una fecha, el historial de modificaciones y la tramitación que las originó.
- *Cómo leerla:* Usa siempre el selector de versión vigente a la fecha en que ejecutarás el trámite, no la última publicada. Y lee el artículo transitorio: en normas en implantación gradual —jornada, datos personales— ahí está la fecha que realmente te aplica.
- *Uso en esta clase:* aporta el marco de «Normativa oficial consolidada» para definir el estándar de la obligación y el mecanismo de control de cambios.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 128 · Cotización, orden de compra y aceptación](../class-02-cotizacion-orden-de-compra-y-aceptacion/README.md) | [Parte 10](../README.md) · [Programa](../../../README.md) | [130 · Contrato de suministro →](../class-04-contrato-de-suministro/README.md) |
