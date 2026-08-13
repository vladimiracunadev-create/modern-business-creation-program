# Clase 032 — Suscripción y SaaS

> **Parte 03 · Modelos de negocio y líneas de ingreso** — clase 4 de 14

**Estado de evidencia:** `GUIA-PRACTICA` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** definir el ciclo de cobro, la política de renovación y el umbral de churn tolerable<br>
**Entregable:** modelo de suscripción con MRR, churn, NRR y punto de equilibrio de adquisición

## 🎯 Propósito

Entender que la suscripción convierte el problema de vender en el problema de retener, y que sin medir churn el crecimiento bruto no significa nada.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —definir el ciclo de cobro, la política de renovación y el umbral de churn tolerable— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **Suscripción** | Cobro recurrente por acceso continuo a un servicio. |
| **MRR** | Ingreso recurrente mensual normalizado. |
| **Churn** | Porcentaje de clientes o ingreso que se pierde por período. |
| **NRR** | Ingreso neto retenido incluyendo expansión y contracción de la base existente. |

## 🗺️ Flujo de razonamiento

```mermaid
flowchart TB
    C["Contexto del caso<br/>actividad · escala · comuna"]
    C --> A1["Suscripción"]
    C --> A2["MRR"]
    C --> A3["Churn"]
    C --> A4["NRR"]
    A1 & A2 & A3 & A4 --> D{{"definir el ciclo de cobro, la<br/>política de renovación y el<br/>umbral de churn tolerable"}}
    D --> E["Entregable<br/>modelo de suscripción con MRR,<br/>churn, NRR y punto de<br/>equilibrio de adquisición"]
    E --> V{"¿Cumple el criterio<br/>de aceptación?"}
    V -->|sí| S["Evidencia archivada<br/>y clase siguiente"]
    V -->|no| C
```

## 📖 Desarrollo

### 1. El fondo del asunto

El modelo de suscripción cambia el problema de vender a retener. Un churn mensual de 5% implica renovar toda la base en veinte meses, lo que hace imposible crecer si la adquisición no supera esa fuga. En Chile además hay que resolver medios de pago recurrentes y las reglas de renovación automática frente al consumidor.

### 2. Cómo se traduce en la práctica

Un churn mensual de 5 % renueva toda la base en veinte meses: crecer exige adquirir más rápido que la fuga, indefinidamente. Además, en Chile la renovación automática frente a consumidores exige información clara y un mecanismo de baja accesible; una política de retención basada en dificultar la salida es infracción, no estrategia.

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

Modelo de suscripción con mrr, churn, nrr y punto de equilibrio de adquisición.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] churn y NRR están calculados con datos o supuestos justificados
- [ ] la política de renovación cumple deberes de información al consumidor
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Renovación automática sin información clara ni mecanismo de baja accesible.
- Celebrar crecimiento bruto de clientes ignorando el churn.

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

1. ¿Cuál es tu churn de clientes y cuál el de ingresos? ¿Por qué difieren?
2. ¿Tu NRR está sobre 100 %? Si no, ¿cuánto debes adquirir solo para no caer?
3. ¿Cómo puede un cliente dar de baja su suscripción y en cuántos pasos?

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
| [← 031 · Modelo de servicios profesionales](../class-03-modelo-de-servicios-profesionales/README.md) | [Parte 03](../README.md) · [Programa](../../../README.md) | [033 · Comercio electrónico D2C →](../class-05-comercio-electronico-d2c/README.md) |
