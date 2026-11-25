# Clase 139 — Gestión y repositorio de contratos

> **Parte 10 · Contratos y arquitectura legal operativa** — clase 13 de 14

**Estado de evidencia:** `VERIFICADO-FUENTE` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** definir dónde viven los contratos y quién controla vencimientos<br>
**Entregable:** repositorio de contratos con metadatos completos y alertas de vencimiento configuradas

## 🎯 Propósito

Centralizar los contratos con metadatos y alertas, para que saber a qué está obligada la empresa no dependa de la memoria de una persona.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —definir dónde viven los contratos y quién controla vencimientos— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **Repositorio de contratos** | Archivo central con versión vigente de cada contrato. |
| **Metadatos** | Datos de control: contraparte, monto, vigencia, preaviso, responsable. |
| **Alerta de vencimiento** | Aviso anticipado antes de la fecha crítica. |
| **Versión vigente** | Documento firmado con sus anexos y modificaciones. |

## 🗺️ Modelo mental: El ciclo de vida de un contrato bien gestionado

> **La idea en una frase:** El repositorio de contratos es la diferencia entre saber a qué está obligada la empresa y descubrirlo cuando alguien reclama; con metadatos y alertas, el control deja de depender de la memoria.

![Esquema: El ciclo de vida de un contrato bien gestionado](modelo-mental.svg)

**Qué mirar primero:** El ciclo muestra que gestionar un contrato no termina con la firma: sigue con el archivo, las alertas y la decisión de cada vencimiento.

**Una imagen cotidiana:** Es un calendario de cumpleaños: no necesitas recordar todas las fechas, solo asegurarte de que el sistema te avise a tiempo.

## 📖 Desarrollo

### 1. El fondo del asunto

El repositorio de contratos es la diferencia entre saber a qué está obligada la empresa y descubrirlo cuando alguien reclama. Con metadatos y alertas, el control de vencimientos deja de depender de la memoria de una persona, que es como funciona en la mayoría de las pymes.

### 2. Cómo se traduce en la práctica

Define dónde viven los contratos (una carpeta o sistema único), con quién tiene acceso y cómo se nombran las versiones. Registra metadatos básicos: partes, objeto, fechas, montos, preaviso y responsable. Configura alertas y revisa mensualmente los vencimientos. Un repositorio simple y mantenido supera a uno sofisticado pero abandonado.

### 3. Marco aplicable y quién interviene

- Código Civil en materia de obligaciones, contratos y responsabilidad
- Código de Comercio para actos mercantiles
- Ley 19.983 sobre mérito ejecutivo de la factura
- Ley 21.131 sobre pago a treinta días

**Autoridades o contrapartes involucradas:** Tribunales ordinarios, Centros de arbitraje (CAM Santiago).
**Profesionales de apoyo:** abogado comercial, responsable de contratos, finanzas. La participación concreta depende del riesgo, del
tamaño de la empresa y de la actividad económica.

### 4. Antes y después

Antes: los contratos de una empresa están repartidos en correos y escritorios; al auditarla, nadie encuentra la versión firmada de dos contratos y uno ya estaba vencido. Después: usa una carpeta única con un índice de metadatos (partes, fecha, monto, vencimiento, responsable) y alertas a 120 y 60 días. En el primer año evita tres renovaciones automáticas no deseadas y responde a una auditoría en un día (caso ilustrativo).

### 5. En qué se apoya

- **The Checklist Manifesto** (Metropolitan Books): Gawande muestra cómo las listas y rutinas simples evitan errores en procesos repetitivos, como el control de vencimientos de contratos.
- **Normativa oficial consolidada** (Biblioteca del Congreso Nacional · LeyChile): Las normas civiles y comerciales, consultables en la Biblioteca del Congreso Nacional, fundan la obligatoriedad de lo pactado, que el repositorio permite conocer.

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

Repositorio de contratos con metadatos completos y alertas de vencimiento configuradas.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] cada contrato tiene metadatos completos y responsable
- [ ] las alertas se disparan antes del plazo de preaviso
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Mantener los contratos dispersos en correos de distintas personas.
- Archivar el contrato sin sus anexos y modificaciones posteriores.

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

1. ¿Dónde vive hoy la versión vigente de cada contrato y quién puede acceder?
2. ¿Están los anexos y modificaciones junto al contrato original?
3. ¿Qué alerta te avisa antes del plazo de preaviso de cada renovación?

## 🔗 Fuentes oficiales

**Biblioteca del Congreso Nacional · LeyChile — Normativa oficial consolidada**  
<https://www.bcn.cl/leychile/> · verificado 2026-11-05

- *Qué contiene:* Publica el texto oficial y consolidado de leyes, decretos y reglamentos, con la versión vigente a una fecha, el historial de modificaciones y la tramitación que las originó.
- *Cómo leerla:* Usa siempre el selector de versión vigente a la fecha en que ejecutarás el trámite, no la última publicada. Y lee el artículo transitorio: en normas en implantación gradual —jornada, datos personales— ahí está la fecha que realmente te aplica.
- *Uso en esta clase:* aporta el marco de «Normativa oficial consolidada» para definir dónde viven los contratos y quién controla vencimientos.

**Servicio de Impuestos Internos — Nuevos contribuyentes, inicio de actividades y DTE**  
<https://www.sii.cl/ayudas/nuevos_contribuyentes/boleta-vys-facturador.html> · verificado 2026-11-05

- *Qué contiene:* Reúne el circuito completo del contribuyente nuevo: obtención de RUT, declaración de inicio de actividades, elección de códigos de actividad económica y habilitación para emitir documentos tributarios electrónicos.
- *Cómo leerla:* Sepáralo en dos actos distintos que la página trata seguidos: el RUT identifica, el inicio de actividades habilita. Lo que te bloquea para facturar casi siempre está en el segundo, no en el primero.
- *Uso en esta clase:* aporta el marco de «Nuevos contribuyentes, inicio de actividades y DTE» para definir dónde viven los contratos y quién controla vencimientos.

**Metropolitan Books — The Checklist Manifesto**  
<https://openlibrary.org/isbn/9780312430009> · verificado 2026-11-25

- *Qué contiene:* Muestra cómo listas de verificación simples reducen errores evitables en trabajos complejos. Se usa como lectura de apoyo conceptual y no como fuente normativa.
- *Cómo leerla:* Úsalo como marco conceptual para entender el porqué de la práctica, nunca como prueba de lo que exige la ley chilena; para eso están las fuentes oficiales de la clase.
- *Uso en esta clase:* aporta el marco de «The Checklist Manifesto» para definir dónde viven los contratos y quién controla vencimientos.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 138 · Contratos con proveedores críticos](../class-12-contratos-con-proveedores-criticos/README.md) | [Parte 10](../README.md) · [Programa](../../../README.md) | [140 · Cuándo debe intervenir un abogado →](../class-14-cuando-debe-intervenir-un-abogado/README.md) |
