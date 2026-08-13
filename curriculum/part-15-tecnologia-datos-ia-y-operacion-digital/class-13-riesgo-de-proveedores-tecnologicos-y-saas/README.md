# Clase 209 — Riesgo de proveedores tecnológicos y SaaS

> **Parte 15 · Tecnología, datos, IA y operación digital** — clase 13 de 14

**Estado de evidencia:** `DINAMICO` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** definir qué se evalúa antes de contratar un proveedor tecnológico<br>
**Entregable:** ficha de evaluación de proveedores SaaS con seguridad, datos, continuidad y salida

## 🎯 Propósito

Evaluar seguridad, ubicación de datos, continuidad y salida antes de contratar un proveedor tecnológico, porque la responsabilidad no se traslada.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —definir qué se evalúa antes de contratar un proveedor tecnológico— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **Riesgo de proveedor** | Exposición derivada de depender de un tercero tecnológico. |
| **Cláusula de salida** | Derecho a terminar y obtener los datos. |
| **Portabilidad** | Capacidad de exportar datos en formato usable. |
| **Evaluación de proveedor** | Revisión de seguridad, continuidad y cumplimiento. |

## 🗺️ Flujo de razonamiento

```mermaid
flowchart TB
    C["Contexto del caso<br/>actividad · escala · comuna"]
    C --> A1["Riesgo de proveedor"]
    C --> A2["Cláusula de salida"]
    C --> A3["Portabilidad"]
    C --> A4["Evaluación de proveedor"]
    A1 & A2 & A3 & A4 --> D{{"definir qué se evalúa antes de<br/>contratar un proveedor<br/>tecnológico"}}
    D --> E["Entregable<br/>ficha de evaluación de<br/>proveedores SaaS con<br/>seguridad, datos, continuidad<br/>y salida"]
    E --> V{"¿Cumple el criterio<br/>de aceptación?"}
    V -->|sí| S["Evidencia archivada<br/>y clase siguiente"]
    V -->|no| C
```

## 📖 Desarrollo

### 1. El fondo del asunto

Contratar SaaS traslada operación pero no responsabilidad: frente al cliente y frente a la autoridad de datos responde la empresa. Antes de contratar hay que verificar seguridad, ubicación de datos, acuerdo de tratamiento y forma de exportación al terminar.

### 2. Cómo se traduce en la práctica

Frente al cliente y frente a la autoridad de datos responde la empresa, no el proveedor. Descubrir al terminar que la exportación de datos no es usable —formatos propietarios, sin relaciones, sin históricos— es el escenario que convierte una migración planificada en una pérdida de información.

### 3. Marco aplicable y quién interviene

- Ley 21.663 Marco de Ciberseguridad y su reglamentación
- Ley 21.719 en lo relativo a tratamiento automatizado y decisiones basadas en datos
- controles de referencia tipo CIS Controls y NIST CSF adaptados a pyme

**Autoridades o contrapartes involucradas:** ANCI, CSIRT Nacional, Agencia de Protección de Datos Personales (en implementación).
**Profesionales de apoyo:** responsable de TI, consultor de ciberseguridad, analista de datos, abogado de datos. La participación concreta depende del riesgo, del
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

Ficha de evaluación de proveedores saas con seguridad, datos, continuidad y salida.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] cada proveedor crítico tiene ficha de evaluación completa
- [ ] la portabilidad de datos está verificada, no solo declarada
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Contratar sin acuerdo de tratamiento de datos personales.
- Descubrir al terminar que la exportación de datos no es usable.

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

1. ¿Tienes acuerdo de tratamiento de datos con cada proveedor que los procesa?
2. ¿Probaste alguna vez exportar tus datos y verificar que sirven?
3. ¿Qué pasa con tu operación si ese proveedor cierra en 30 días?

## 🔗 Fuentes oficiales

**Biblioteca del Congreso Nacional · LeyChile — Normativa oficial consolidada**  
<https://www.bcn.cl/leychile/> · verificado 2026-08-07

- *Qué contiene:* Publica el texto oficial y consolidado de leyes, decretos y reglamentos, con la versión vigente a una fecha, el historial de modificaciones y la tramitación que las originó.
- *Cómo leerla:* Usa siempre el selector de versión vigente a la fecha en que ejecutarás el trámite, no la última publicada. Y lee el artículo transitorio: en normas en implantación gradual —jornada, datos personales— ahí está la fecha que realmente te aplica.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 208 · Agentes de IA con humano en el circuito](../class-12-agentes-de-ia-con-humano-en-el-circuito/README.md) | [Parte 15](../README.md) · [Programa](../../../README.md) | [210 · Gobierno tecnológico y costos FinOps →](../class-14-gobierno-tecnologico-y-costos-finops/README.md) |
