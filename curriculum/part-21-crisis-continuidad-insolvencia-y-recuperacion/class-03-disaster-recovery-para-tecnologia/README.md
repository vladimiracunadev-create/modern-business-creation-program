# Clase 283 — Disaster Recovery para tecnología

> **Parte 21 · Crisis, continuidad, insolvencia y recuperación** — clase 3 de 14
> Estado: `VERIFICADO-FUENTE` · Jurisdicción: **Chile-first** · Fecha base normativa: **07-08-2026**

## Objetivo

Comprender **disaster recovery para tecnología** dentro del sistema de creación y operación de una empresa,
y quedar en condiciones de tomar la decisión que esta clase habilita:
*definir el orden de recuperación tecnológica y probarlo*.

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
| **DRP** | plan de recuperación tecnológica |
| **RTO y RPO** | tiempo de recuperación y pérdida de datos tolerables |
| **Sitio alternativo** | infraestructura de respaldo para operar |
| **Prueba de recuperación** | ejercicio de restauración completo |

## Desarrollo

El DRP traduce el BCP a infraestructura: qué sistemas se levantan primero, desde qué copia y en cuánto tiempo. La prueba debe ser completa, no solo de restauración de archivos: incluye accesos, integraciones y validación de que la operación puede continuar realmente.

## Marco aplicable en esta parte

- Ley 20.720 sobre reorganización y liquidación de empresas y personas
- Ley 19.983 sobre mérito ejecutivo de la factura para cobranza
- continuidad de negocio: BIA, RTO, RPO y plan de comunicación de crisis

**Autoridades o contrapartes involucradas:** Superintendencia de Insolvencia y Reemprendimiento, Tribunales civiles, Dirección del Trabajo.

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

Plan de recuperación tecnológica con rto, rpo, secuencia de restauración y registro de pruebas.

El documento debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable,
riesgos identificados y próximos pasos.

## Reto

Resolver la misma materia para una segunda línea de negocio con distinta carga regulatoria,
y explicar por escrito **qué cambió y por qué**.

### Criterio de aceptación

- [ ] los RTO son alcanzables con la infraestructura actual
- [ ] existe registro de al menos una prueba completa
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## Errores comunes

- definir RTO ambiciosos que la infraestructura contratada no puede cumplir
- probar la restauración de archivos y no la continuidad completa de la operación
- esperar a la cesación de pagos para buscar asesoría y perder la opción de reorganización
- recortar costos destruyendo la capacidad que permite recuperarse

## Profesionales a considerar

Abogado de insolvencia, veedor o liquidador, cfo, comunicaciones. La participación concreta depende del riesgo, el tamaño de la
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
- **Dirección del Trabajo** — Trabajo y empleadores: <https://www.dt.gob.cl/>

Lecturas complementarias: [`docs/15_BOOKS_AND_LEARNING_PATH.md`](../../../docs/15_BOOKS_AND_LEARNING_PATH.md)
y [`docs/16_OFFICIAL_SOURCE_CATALOG.md`](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

[← 282. Business Continuity Plan](../class-02-business-continuity-plan/README.md) · [Índice de la parte](../README.md) · [284. Gestión de crisis reputacional →](../class-04-gestion-de-crisis-reputacional/README.md)
