# Clase 208 — Agentes de IA con humano en el circuito

> **Parte 15 · Tecnología, datos, IA y operación digital** — clase 12 de 14
> Estado: `DINAMICO` · Jurisdicción: **Chile-first** · Fecha base normativa: **07-08-2026**

## Objetivo

Comprender **agentes de ia con humano en el circuito** dentro del sistema de creación y operación de una empresa,
y quedar en condiciones de tomar la decisión que esta clase habilita:
*definir qué puede ejecutar un agente y qué requiere aprobación humana*.

## Resultados verificables

Al finalizar, quien estudia esta clase puede:

1. definir los conceptos de la tabla siguiente sin recurrir a una definición memorizada;
2. explicar cómo esta materia condiciona a las demás partes del programa;
3. tomar la decisión declarada arriba y justificarla por escrito;
4. producir el entregable de la clase con criterio de aceptación verificable;
5. identificar qué dato es estable y cuál es dinámico y requiere revalidación en la fuente.

## Conceptos clave

| Concepto | Definición operacional |
|---|---|
| **Agente** | sistema que ejecuta acciones de forma autónoma para lograr un objetivo |
| **Humano en el circuito** | punto obligatorio de aprobación antes de una acción con efecto |
| **Trazabilidad** | registro de qué hizo el agente, con qué datos y con qué resultado |
| **Alcance de acción** | conjunto de operaciones que el agente puede ejecutar |

## Desarrollo

Un agente que actúa sobre sistemas reales debe tener alcance limitado, credenciales propias con menor privilegio y aprobación humana para acciones irreversibles: pagos, envíos, publicaciones y borrados. La trazabilidad es lo que permite auditar y corregir cuando algo sale mal.

## Marco aplicable en esta parte

- Ley 21.663 Marco de Ciberseguridad y su reglamentación
- Ley 21.719 en lo relativo a tratamiento automatizado y decisiones basadas en datos
- controles de referencia tipo CIS Controls y NIST CSF adaptados a pyme

**Autoridades o contrapartes involucradas:** ANCI, CSIRT Nacional, Agencia de Protección de Datos Personales (en implementación).

## Flujo de trabajo

1. Delimitar el contexto: actividad económica, escala, comuna y etapa de la empresa.
2. Reunir los antecedentes que la decisión exige y verificar su fecha.
3. Identificar las alternativas reales, incluida la de no hacer nada.
4. Evaluar el impacto en mercado, caja, personas, regulación y operación.
5. Tomar la decisión y dejarla registrada con sus supuestos.
6. Ejecutar o simular el flujo hasta producir el entregable.
7. Contrastar el resultado contra el criterio de aceptación.
8. Anotar lo que requiere validación profesional y programar su revisión.

## Taller guiado

Aplicar esta clase a **una** de las siguientes líneas de negocio, y repetir el ejercicio con una
segunda línea de carga regulatoria distinta:

- SaaS B2B con IA;
- servicios profesionales;
- e-commerce D2C;
- alimentos o foodtech;
- exportación de servicios;
- fintech regulada;
- construcción o servicios técnicos.

### Entregable

Diseño de agente con alcance de acción, credenciales, puntos de aprobación y registro de trazas.

El documento debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable,
riesgos identificados y próximos pasos.

## Reto

Resolver la misma materia para una segunda línea de negocio con distinta carga regulatoria,
y explicar por escrito **qué cambió y por qué**.

### Criterio de aceptación

- [ ] las acciones irreversibles requieren aprobación humana
- [ ] existe registro completo de trazas de ejecución
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## Errores comunes

- dar al agente credenciales amplias por comodidad
- permitir acciones irreversibles sin aprobación humana
- respaldos que nunca se probaron y no restauran cuando se necesitan
- accesos compartidos y credenciales que sobreviven a la salida de una persona

## Profesionales a considerar

Responsable de ti, consultor de ciberseguridad, analista de datos, abogado de datos. La participación concreta depende del riesgo, el tamaño de la
empresa y la actividad económica; este material no reemplaza esa asesoría.

## Checklist Chile

- [ ] ¿existe norma o autoridad específica para esta materia?
- [ ] ¿la fuente consultada está vigente a la fecha de ejecución?
- [ ] ¿se activa algún trámite ante el SII?
- [ ] ¿se activa algún requisito municipal o sectorial?
- [ ] ¿afecta a consumidores o al tratamiento de datos personales?
- [ ] ¿afecta a trabajadores o a la seguridad y salud en el trabajo?
- [ ] ¿afecta a impuestos, contabilidad o caja?
- [ ] ¿afecta a contratos o a propiedad intelectual?
- [ ] ¿requiere renovación, reporte periódico o revalidación?

## Fuentes oficiales

- **Biblioteca del Congreso Nacional - LeyChile** — Normativa oficial consolidada: <https://www.bcn.cl/leychile/>
- **CORFO** — Innovación, inversión y garantías: <https://www.corfo.cl/>

Lecturas complementarias: [`docs/15_BOOKS_AND_LEARNING_PATH.md`](../../../docs/15_BOOKS_AND_LEARNING_PATH.md)
y [`docs/16_OFFICIAL_SOURCE_CATALOG.md`](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

[← 207. IA generativa en operaciones](../class-11-ia-generativa-en-operaciones/README.md) · [Índice de la parte](../README.md) · [209. Riesgo de proveedores tecnológicos y SaaS →](../class-13-riesgo-de-proveedores-tecnologicos-y-saas/README.md)
