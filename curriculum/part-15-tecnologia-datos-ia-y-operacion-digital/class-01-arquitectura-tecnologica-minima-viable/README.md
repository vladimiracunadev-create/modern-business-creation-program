# Clase 197 — Arquitectura tecnológica mínima viable

> **Parte 15 · Tecnología, datos, IA y operación digital** — clase 1 de 14

**Estado de evidencia:** `DINAMICO` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** definir el conjunto mínimo de sistemas y cuál es fuente de verdad para cada dato<br>
**Entregable:** mapa de arquitectura con sistemas, fuente de verdad por dato e integraciones necesarias

## 🎯 Propósito

Definir el conjunto mínimo de sistemas y, sobre todo, cuál es la fuente de verdad de cada dato crítico.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —definir el conjunto mínimo de sistemas y cuál es fuente de verdad para cada dato— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **Arquitectura mínima viable** | Conjunto mínimo de sistemas que sostiene la operación. |
| **Sistema de registro** | Fuente única de verdad para un tipo de dato. |
| **Integración** | Conexión que evita reingreso manual de datos. |
| **Costo total** | Licencias, implementación, soporte y salida. |

## 🗺️ Flujo de razonamiento

```mermaid
flowchart TB
    C["Contexto del caso<br/>actividad · escala · comuna"]
    C --> A1["Arquitectura mínima viable"]
    C --> A2["Sistema de registro"]
    C --> A3["Integración"]
    C --> A4["Costo total"]
    A1 & A2 & A3 & A4 --> D{{"definir el conjunto mínimo de<br/>sistemas y cuál es fuente de<br/>verdad para cada dato"}}
    D --> E["Entregable<br/>mapa de arquitectura con<br/>sistemas, fuente de verdad por<br/>dato e integraciones<br/>necesarias"]
    E --> V{"¿Cumple el criterio<br/>de aceptación?"}
    V -->|sí| S["Evidencia archivada<br/>y clase siguiente"]
    V -->|no| C
```

## 📖 Desarrollo

### 1. El fondo del asunto

La arquitectura mínima viable de una pyme chilena suele ser facturación electrónica, contabilidad, CRM, almacenamiento y comunicación, integrados entre sí. Cada sistema adicional agrega costo de integración y de gobierno; la pregunta correcta no es qué software es mejor sino cuál es el mínimo que sostiene la operación.

### 2. Cómo se traduce en la práctica

La arquitectura mínima de una pyme chilena suele ser facturación electrónica, contabilidad, CRM, almacenamiento y comunicación, integrados entre sí. Cada sistema adicional agrega costo de integración y de gobierno; la pregunta correcta no es qué software es mejor sino cuál es el mínimo que sostiene la operación.

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

Mapa de arquitectura con sistemas, fuente de verdad por dato e integraciones necesarias.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] cada dato crítico tiene una única fuente de verdad
- [ ] el costo total incluye implementación y salida
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Adquirir herramientas sin definir cuál es la fuente de verdad de cada dato.
- Evaluar software solo por licencia sin incluir implementación y salida.

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

1. ¿Cuál es la fuente de verdad de tus datos de clientes, y cuántos sistemas la disputan?
2. ¿Qué datos reingresas manualmente de un sistema a otro?
3. ¿Incluiste implementación y costo de salida al evaluar tu último software?

## 🔗 Fuentes oficiales

**Biblioteca del Congreso Nacional · LeyChile — Normativa oficial consolidada**  
<https://www.bcn.cl/leychile/> · verificado 2026-08-19

- *Qué contiene:* Publica el texto oficial y consolidado de leyes, decretos y reglamentos, con la versión vigente a una fecha, el historial de modificaciones y la tramitación que las originó.
- *Cómo leerla:* Usa siempre el selector de versión vigente a la fecha en que ejecutarás el trámite, no la última publicada. Y lee el artículo transitorio: en normas en implantación gradual —jornada, datos personales— ahí está la fecha que realmente te aplica.
- *Uso en esta clase:* aporta el marco de «Normativa oficial consolidada» para definir el conjunto mínimo de sistemas y cuál es fuente de verdad para cada dato.

**Corporación de Fomento de la Producción — Innovación, inversión y garantías**  
<https://www.corfo.cl/> · verificado 2026-08-19

- *Qué contiene:* Reúne los instrumentos de fomento a la innovación y la inversión, incluidos programas de capital semilla, escalamiento, garantías y cobertura de riesgo para el sistema financiero.
- *Cómo leerla:* Filtra por etapa de la empresa antes que por monto. Y verifica el componente de innovación que exige cada instrumento: presentar una expansión comercial como innovación es la causa más común de rechazo.
- *Uso en esta clase:* aporta el marco de «Innovación, inversión y garantías» para definir el conjunto mínimo de sistemas y cuál es fuente de verdad para cada dato.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| **Inicio de la parte** | [Parte 15](../README.md) · [Programa](../../../README.md) | [198 · Comprar, construir o integrar software →](../class-02-comprar-construir-o-integrar-software/README.md) |
