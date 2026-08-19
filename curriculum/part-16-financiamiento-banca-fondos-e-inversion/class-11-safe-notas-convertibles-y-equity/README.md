# Clase 221 — SAFE, notas convertibles y equity

> **Parte 16 · Financiamiento, banca, fondos e inversión** — clase 11 de 14

**Estado de evidencia:** `DINAMICO` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** definir qué instrumento se usa y modelar la dilución en la conversión<br>
**Entregable:** modelo de tabla de capitalización con conversión de todos los instrumentos vigentes

## 🎯 Propósito

Modelar la tabla de capitalización post-conversión antes de firmar instrumentos convertibles, porque se acumulan y convierten juntos.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —definir qué instrumento se usa y modelar la dilución en la conversión— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **SAFE** | Acuerdo de inversión que convierte en acciones en un evento futuro. |
| **Nota convertible** | Préstamo que convierte en participación bajo condiciones. |
| **Descuento y valuation cap** | Mecanismos que fijan el precio de conversión. |
| **Conversión** | Momento en que el instrumento se transforma en acciones. |

## 🗺️ Flujo de razonamiento

```mermaid
flowchart TB
    C["Contexto del caso<br/>actividad · escala · comuna"]
    C --> A1["SAFE"]
    C --> A2["Nota convertible"]
    C --> A3["Descuento y valuation cap"]
    C --> A4["Conversión"]
    A1 & A2 & A3 & A4 --> D{{"definir qué instrumento se usa<br/>y modelar la dilución en la<br/>conversión"}}
    D --> E["Entregable<br/>modelo de tabla de<br/>capitalización con conversión<br/>de todos los instrumentos<br/>vigentes"]
    E --> V{"¿Cumple el criterio<br/>de aceptación?"}
    V -->|sí| S["Evidencia archivada<br/>y clase siguiente"]
    V -->|no| C
```

## 📖 Desarrollo

### 1. El fondo del asunto

Los instrumentos convertibles postergan la valorización pero no la eliminan: se acumulan y convierten juntos, a veces produciendo una dilución mucho mayor que la anticipada. Modelar la tabla de capitalización post-conversión antes de firmar es la única forma de saber qué se está entregando.

### 2. Cómo se traduce en la práctica

Postergar la valorización no la elimina: la traslada a un momento donde varios instrumentos convierten a la vez, con descuentos y topes que pueden producir una dilución mucho mayor que la anticipada. Fijar un valuation cap sin modelar su efecto es firmar sin saber qué se entrega.

### 3. Marco aplicable y quién interviene

- FOGAPE y sistema de garantías estatales
- Ley 21.521 Fintec para plataformas de financiamiento colectivo
- instrumentos SAFE, notas convertibles y aumentos de capital en SpA

**Autoridades o contrapartes involucradas:** CMF, CORFO, SERCOTEC, BancoEstado y banca comercial.
**Profesionales de apoyo:** CFO, abogado corporativo, asesor financiero, contador. La participación concreta depende del riesgo, del
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

Modelo de tabla de capitalización con conversión de todos los instrumentos vigentes.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] la tabla post-conversión está modelada con todos los instrumentos
- [ ] el efecto del cap y del descuento está cuantificado
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Firmar varios convertibles sin modelar la dilución acumulada.
- Fijar un valuation cap sin entender su efecto en la conversión.

**Característicos de la parte 16:**

- Financiar activos de largo plazo con líneas de corto plazo.
- Usar factoring de forma estructural y erosionar el margen.

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

1. ¿Cuánta participación conservarías si convirtieran todos tus instrumentos hoy?
2. ¿Qué efecto tiene el valuation cap que aceptaste en distintos escenarios de valorización?
3. ¿Cuántos convertibles tienes vigentes y con qué condiciones cada uno?

## 🔗 Fuentes oficiales

**Biblioteca del Congreso Nacional · LeyChile — Normativa oficial consolidada**  
<https://www.bcn.cl/leychile/> · verificado 2026-08-19

- *Qué contiene:* Publica el texto oficial y consolidado de leyes, decretos y reglamentos, con la versión vigente a una fecha, el historial de modificaciones y la tramitación que las originó.
- *Cómo leerla:* Usa siempre el selector de versión vigente a la fecha en que ejecutarás el trámite, no la última publicada. Y lee el artículo transitorio: en normas en implantación gradual —jornada, datos personales— ahí está la fecha que realmente te aplica.
- *Uso en esta clase:* aporta el marco de «Normativa oficial consolidada» para definir qué instrumento se usa y modelar la dilución en la conversión.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 220 · Venture capital y rondas](../class-10-venture-capital-y-rondas/README.md) | [Parte 16](../README.md) · [Programa](../../../README.md) | [222 · Valoración empresarial básica →](../class-12-valoracion-empresarial-basica/README.md) |
