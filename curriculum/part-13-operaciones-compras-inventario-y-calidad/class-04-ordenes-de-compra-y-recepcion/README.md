# Clase 172 — Órdenes de compra y recepción

> **Parte 13 · Operaciones, compras, inventario y calidad** — clase 4 de 14
> Estado: `GUIA-PRACTICA` · Jurisdicción: **Chile-first** · Fecha base normativa: **07-08-2026**

## Objetivo

Comprender **órdenes de compra y recepción** dentro del sistema de creación y operación de una empresa,
y quedar en condiciones de tomar la decisión que esta clase habilita:
*implementar el control de tres vías antes de autorizar cualquier pago*.

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
| **Orden de compra** | documento que formaliza el pedido con condiciones |
| **Recepción** | verificación de lo recibido contra lo pedido |
| **Tres vías** | conciliación entre orden, recepción y factura |
| **Diferencia de recepción** | discrepancia en cantidad, calidad o precio |

## Desarrollo

El control de tres vías —orden, recepción y factura— es el control antifraude y antierror más eficaz en compras. Sin él, se pagan cantidades no recibidas, precios distintos a los pactados y servicios no prestados, y el descuadre aparece meses después sin poder reconstruirse.

## Marco aplicable en esta parte

- ISO 9001 como referencia de sistema de gestión de calidad
- teoría de restricciones para capacidad y cuellos de botella
- trazabilidad de lote exigida en rubros regulados (alimentos, salud, químicos)

**Autoridades o contrapartes involucradas:** SEREMI de Salud en rubros con trazabilidad sanitaria, SERNAC en garantía y postventa.

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

Procedimiento de compra y recepción con conciliación de tres vías y tratamiento de diferencias.

El documento debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable,
riesgos identificados y próximos pasos.

## Reto

Resolver la misma materia para una segunda línea de negocio con distinta carga regulatoria,
y explicar por escrito **qué cambió y por qué**.

### Criterio de aceptación

- [ ] ningún pago se autoriza sin las tres vías conciliadas
- [ ] las diferencias tienen procedimiento de resolución
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## Errores comunes

- pagar facturas sin verificar recepción efectiva
- recibir sin comparar contra la orden y aceptar diferencias de precio
- inventario teórico que no coincide con el físico y destruye la promesa de entrega
- proveedor crítico único sin plan alternativo

## Profesionales a considerar

Jefe de operaciones, comprador, encargado de calidad, prevencionista. La participación concreta depende del riesgo, el tamaño de la
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

- **ChileAtiende / Autoridad Sanitaria** — Autorización sanitaria de alimentos: <https://www.chileatiende.gob.cl/fichas/172-autorizacion-sanitaria-de-alimentos>
- **SERNAC** — Consumidor y comercio electrónico: <https://www.sernac.cl/>

Lecturas complementarias: [`docs/15_BOOKS_AND_LEARNING_PATH.md`](../../../docs/15_BOOKS_AND_LEARNING_PATH.md)
y [`docs/16_OFFICIAL_SOURCE_CATALOG.md`](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

[← 171. Compras y homologación de proveedores](../class-03-compras-y-homologacion-de-proveedores/README.md) · [Índice de la parte](../README.md) · [173. Inventario, conteos y trazabilidad →](../class-05-inventario-conteos-y-trazabilidad/README.md)
