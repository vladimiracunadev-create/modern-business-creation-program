# Clase 204 — Datos maestros y calidad de datos

> **Parte 15 · Tecnología, datos, IA y operación digital** — clase 8 de 14
> Estado: `DINAMICO` · Jurisdicción: **Chile-first** · Fecha base normativa: **07-08-2026**

## Objetivo

Comprender **datos maestros y calidad de datos** dentro del sistema de creación y operación de una empresa,
y quedar en condiciones de tomar la decisión que esta clase habilita:
*definir las entidades maestras, sus reglas de calidad y su responsable*.

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
| **Dato maestro** | información de referencia usada por varios procesos |
| **Duplicado** | registro repetido que fragmenta la información |
| **Regla de calidad** | criterio que define un dato válido |
| **Responsable del dato** | persona a cargo de su exactitud |

## Desarrollo

Sin datos maestros gobernados, cada área tiene su propia versión del cliente y ningún reporte cuadra. Definir formato, regla de validación y responsable por entidad maestra es prerequisito de cualquier analítica: sin eso, los reportes se discuten en vez de usarse.

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

Diccionario de datos maestros con formato, regla de validación y responsable por entidad.

El documento debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable,
riesgos identificados y próximos pasos.

## Reto

Resolver la misma materia para una segunda línea de negocio con distinta carga regulatoria,
y explicar por escrito **qué cambió y por qué**.

### Criterio de aceptación

- [ ] cada entidad maestra tiene responsable designado
- [ ] existen reglas de validación aplicadas en el origen
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## Errores comunes

- construir reportes sobre datos maestros duplicados
- no asignar responsable de la calidad de cada entidad maestra
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

[← 203. Gestión de secretos y privilegios](../class-07-gestion-de-secretos-y-privilegios/README.md) · [Índice de la parte](../README.md) · [205. Analítica y BI empresarial →](../class-09-analitica-y-bi-empresarial/README.md)
