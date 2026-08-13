# Clase 033 — Comercio electrónico D2C

> **Parte 03 · Modelos de negocio y líneas de ingreso** — clase 5 de 14

**Estado de evidencia:** `GUIA-PRACTICA` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** determinar la contribución real por pedido y el nivel de servicio comprometido<br>
**Entregable:** modelo de contribución por pedido con todos los costos variables y tasa de devolución

## 🎯 Propósito

Calcular la contribución real por pedido antes de escalar inversión publicitaria, porque el margen bruto del producto no dice nada sobre la rentabilidad del canal.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —determinar la contribución real por pedido y el nivel de servicio comprometido— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **D2C** | Venta directa al consumidor sin intermediario. |
| **Contribución por pedido** | Margen después de producto, envío, medios de pago y devolución. |
| **Retracto** | Derecho del consumidor a desistir en los plazos y casos legales. |
| **Costo logístico inverso** | Costo de recibir y reponer un producto devuelto. |

## 🗺️ Flujo de razonamiento

```mermaid
flowchart TB
    C["Contexto del caso<br/>actividad · escala · comuna"]
    C --> A1["D2C"]
    C --> A2["Contribución por pedido"]
    C --> A3["Retracto"]
    C --> A4["Costo logístico inverso"]
    A1 & A2 & A3 & A4 --> D{{"determinar la contribución<br/>real por pedido y el nivel de<br/>servicio comprometido"}}
    D --> E["Entregable<br/>modelo de contribución por<br/>pedido con todos los costos<br/>variables y tasa de devolución"]
    E --> V{"¿Cumple el criterio<br/>de aceptación?"}
    V -->|sí| S["Evidencia archivada<br/>y clase siguiente"]
    V -->|no| C
```

## 📖 Desarrollo

### 1. El fondo del asunto

El e-commerce D2C se evalúa por contribución por pedido, no por margen bruto del producto: comisiones de pasarela, despacho, embalaje y devoluciones consumen puntos que rara vez se modelan al inicio. Además activa el Reglamento de Comercio Electrónico con deberes de información, confirmación y retracto.

### 2. Cómo se traduce en la práctica

Comisión de pasarela, despacho, embalaje y devoluciones consumen puntos que rara vez se modelan al inicio. Y el Reglamento de Comercio Electrónico exige informar precio total antes del pago, confirmar la compra con sus condiciones y respetar el retracto: la operación debe poder sostener lo que la web promete.

### 3. Marco aplicable y quién interviene

- Business Model Canvas y Lean Canvas como instrumentos de diseño
- Ley 19.496 sobre protección de los derechos de los consumidores para modelos B2C
- Ley 20.169 sobre competencia desleal y DL 211 en modelos de plataforma

**Autoridades o contrapartes involucradas:** SERNAC, FNE, SII.
**Profesionales de apoyo:** fundador, abogado comercial, contador de gestión. La participación concreta depende del riesgo, del
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

Modelo de contribución por pedido con todos los costos variables y tasa de devolución.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] la contribución por pedido incluye devoluciones y medios de pago
- [ ] las condiciones publicadas son cumplibles por la operación actual
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Publicar plazos de despacho que la operación no puede cumplir.
- No considerar la logística inversa en el costo del pedido.

**Característicos de la parte 03:**

- Copiar un modelo extranjero sin verificar su viabilidad regulatoria o logística en chile.
- Sumar líneas de negocio antes de que la primera sea rentable.

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

1. ¿Cuál es tu contribución por pedido después de devoluciones y medios de pago?
2. ¿El plazo de despacho publicado se cumple según tu histórico real?
3. ¿Un cliente puede ver el costo total, con envío, antes de iniciar el pago?

## 🔗 Fuentes oficiales

**Servicio Nacional del Consumidor — Ley 19.496, comercio electrónico y garantía legal**  
<https://www.sernac.cl/> · verificado 2026-08-07

- *Qué contiene:* Publica la interpretación aplicada de la Ley del Consumidor: deberes de información en la oferta, reglas del comercio electrónico, garantía legal, contratos de adhesión y el procedimiento de reclamos.
- *Cómo leerla:* Entra por el rubro de tu negocio y revisa las alertas y procedimientos colectivos publicados: muestran qué está fiscalizando el servicio ahora, que es mejor predictor de tu riesgo que la lectura abstracta de la ley.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 032 · Suscripción y SaaS](../class-04-suscripcion-y-saas/README.md) | [Parte 03](../README.md) · [Programa](../../../README.md) | [034 · Retail físico y omnicanal →](../class-06-retail-fisico-y-omnicanal/README.md) |
