# Clase 153 — Ley Marco de Ciberseguridad y ciberhigiene empresarial

> **Parte 11 · Consumidor, e-commerce, privacidad, IP y seguridad digital** — clase 13 de 14

**Estado de evidencia:** `DINAMICO` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** determinar si la empresa tiene obligaciones directas o derivadas de sus clientes<br>
**Entregable:** diagnóstico de ciberhigiene con controles básicos implementados y brechas priorizadas

## 🎯 Propósito

Determinar si la empresa tiene obligaciones directas bajo la Ley 21.663 o si las recibirá trasladadas por contrato desde clientes regulados.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —determinar si la empresa tiene obligaciones directas o derivadas de sus clientes— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **Ley 21.663** | Ley marco de ciberseguridad. |
| **Servicio esencial** | Actividad cuya interrupción afecta significativamente. |
| **Operador de importancia vital** | Entidad calificada con obligaciones reforzadas. |
| **Ciberhigiene** | Conjunto de prácticas básicas que reducen la mayoría del riesgo. |

## 🗺️ Flujo de razonamiento

```mermaid
flowchart TB
    C["Contexto del caso<br/>actividad · escala · comuna"]
    C --> A1["Ley 21.663"]
    C --> A2["Servicio esencial"]
    C --> A3["Operador de importancia<br/>vital"]
    C --> A4["Ciberhigiene"]
    A1 & A2 & A3 & A4 --> D{{"determinar si la empresa tiene<br/>obligaciones directas o<br/>derivadas de sus clientes"}}
    D --> E["Entregable<br/>diagnóstico de ciberhigiene<br/>con controles básicos<br/>implementados y brechas<br/>priorizadas"]
    E --> V{"¿Cumple el criterio<br/>de aceptación?"}
    V -->|sí| S["Evidencia archivada<br/>y clase siguiente"]
    V -->|no| C
```

## 📖 Desarrollo

### 1. El fondo del asunto

La Ley 21.663 crea la ANCI y establece obligaciones para servicios esenciales y operadores de importancia vital, incluyendo reporte de incidentes. Aunque una pyme no esté calificada, sus clientes regulados le trasladarán exigencias por contrato: es más barato adoptar la ciberhigiene básica antes de que la exija un cliente.

### 2. Cómo se traduce en la práctica

Aunque no sea operador de importancia vital, sus clientes regulados exigirán controles, auditorías y notificación de incidentes por cláusula contractual. Anticipar la ciberhigiene básica convierte el cumplimiento en argumento comercial en vez de en obstáculo descubierto durante una negociación.

### 3. Marco aplicable y quién interviene

- Ley 19.496 sobre protección de los derechos de los consumidores y su Reglamento de Comercio Electrónico
- Ley 19.628 sobre protección de la vida privada, vigente hasta la entrada en régimen de la Ley 21.719
- Ley 21.719 sobre protección de datos personales, con vigencia el 1 de diciembre de 2026
- Ley 19.039 sobre propiedad industrial y Ley 17.336 sobre propiedad intelectual
- Ley 21.663 Marco de Ciberseguridad

**Autoridades o contrapartes involucradas:** SERNAC, Agencia de Protección de Datos Personales (en implementación), INAPI, ANCI.
**Profesionales de apoyo:** abogado de consumo y datos, DPO o responsable de privacidad, responsable de seguridad de la información. La participación concreta depende del riesgo, del
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

Diagnóstico de ciberhigiene con controles básicos implementados y brechas priorizadas.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] el diagnóstico determina la condición de la empresa frente a la ley
- [ ] los controles básicos están implementados y verificados
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Asumir que la ley no aplica y descubrir la exigencia por vía contractual.
- Implementar controles sin verificar que funcionan.

**Característicos de la parte 11:**

- Publicar precio o stock que después no se puede honrar.
- Tratar datos personales sin base de licitud ni registro de actividades de tratamiento.

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

1. ¿Alguno de tus clientes está regulado y podría trasladarte exigencias?
2. ¿Qué controles básicos tienes implementados y verificados, no solo declarados?
3. ¿Podrías responder hoy un cuestionario de seguridad de un cliente grande?

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
| [← 152 · Derecho de autor y licencias de software](../class-12-derecho-de-autor-y-licencias-de-software/README.md) | [Parte 11](../README.md) · [Programa](../../../README.md) | [154 · Respuesta a incidentes y evidencia →](../class-14-respuesta-a-incidentes-y-evidencia/README.md) |
