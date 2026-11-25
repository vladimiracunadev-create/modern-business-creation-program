# Clase 209 — Riesgo de proveedores tecnológicos y SaaS

> **Parte 15 · Tecnología, datos, IA y operación digital** — clase 13 de 14

**Estado de evidencia:** `DINAMICO` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** definir qué se evalúa antes de contratar un proveedor tecnológico<br>
**Entregable:** ficha de evaluación de proveedores SaaS con seguridad, datos, continuidad y salida

## 🎯 Propósito

Evaluar seguridad, ubicación de datos, continuidad y salida antes de contratar un proveedor tecnológico, porque la responsabilidad no se traslada.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —definir qué se evalúa antes de contratar un proveedor tecnológico— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **Riesgo de proveedor** | Exposición derivada de depender de un tercero tecnológico. |
| **Cláusula de salida** | Derecho a terminar y obtener los datos. |
| **Portabilidad** | Capacidad de exportar datos en formato usable. |
| **Evaluación de proveedor** | Revisión de seguridad, continuidad y cumplimiento. |

## 🗺️ Modelo mental: Qué proveedor tecnológico exige más cuidado

> **La idea en una frase:** Contratar un SaaS traslada la operación pero no la responsabilidad: frente al cliente y frente a la autoridad de datos responde la empresa, de modo que antes de contratar hay que evaluar seguridad, ubicación de datos y salida.

![Esquema: Qué proveedor tecnológico exige más cuidado](modelo-mental.svg)

**Lectura guiada:** Ubica cada proveedor según la sensibilidad de los datos y la dependencia que generas. El cuadrante superior derecho exige evaluación formal antes de firmar.

**Piénsalo así:** Es dejar tus llaves y documentos con una empresa de custodia: importa su seguridad, dónde guarda las cosas y qué pasa si cierra.

## 📖 Desarrollo

### 1. El fondo del asunto

Contratar SaaS traslada operación pero no responsabilidad: frente al cliente y frente a la autoridad de datos responde la empresa. Antes de contratar hay que verificar seguridad, ubicación de datos, acuerdo de tratamiento y forma de exportación al terminar.

### 2. Cómo se traduce en la práctica

Antes de contratar, evalúa seguridad, certificaciones, ubicación y subencargados de los datos, continuidad, portabilidad y salida, y obligación de notificar incidentes. Firma un acuerdo de tratamiento cuando el proveedor trate datos personales por tu cuenta. Documenta la evaluación y repítela cada año para los proveedores críticos.

### 3. Marco aplicable y quién interviene

- Ley 21.663 Marco de Ciberseguridad y su reglamentación
- Ley 21.719 en lo relativo a tratamiento automatizado y decisiones basadas en datos
- controles de referencia tipo CIS Controls y NIST CSF adaptados a pyme

**Autoridades o contrapartes involucradas:** ANCI, CSIRT Nacional, Agencia de Protección de Datos Personales (en implementación).
**Profesionales de apoyo:** responsable de TI, consultor de ciberseguridad, analista de datos, abogado de datos. La participación concreta depende del riesgo, del
tamaño de la empresa y de la actividad económica.

### 4. Antes y después

Antes: una empresa contrata un CRM por su precio y sube allí su base de clientes sin evaluar nada; cuando el proveedor sufre una filtración, descubre que sus datos estaban en otra región y que su contrato no obligaba a avisar. Después: usa una lista de verificación con seguridad, ubicación de los datos, cláusula de salida, portabilidad y notificación de incidentes, y rechaza a dos proveedores que no cumplían (caso ilustrativo).

### 5. En qué se apoya

- **Ley 21.719 — Protección y tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales** (Biblioteca del Congreso Nacional): La Ley 21.719 distingue al responsable y al encargado del tratamiento y regula sus obligaciones, entre ellas las de seguridad y las de notificar vulneraciones.
- **Normativa oficial consolidada** (Biblioteca del Congreso Nacional · LeyChile): La Biblioteca del Congreso Nacional publica las normas de datos y ciberseguridad que condicionan el contrato con proveedores tecnológicos.

*Las lecturas de apoyo ofrecen marcos conceptuales; lo que exige la ley chilena se verifica en las fuentes oficiales de esta clase.*

## 🛡️ Protección del conocimiento: Riesgos de las relaciones con terceros

[Guía de inteligencia económica y protección del conocimiento, sección 9](../../../docs/21_INTELIGENCIA_ECONOMICA_Y_PROTECCION_DEL_CONOCIMIENTO.md#9-riesgos-de-las-relaciones-con-terceros)

**Lente para esta clase:** Un SaaS o un cliente integrado es a la vez herramienta y canal de acceso: el riesgo incluye qué hace el proveedor con tus datos y quién lo controla.

| Nivel | Medida proporcionada |
|---|---|
| **Emprendedor o microempresa** | Antes de subir información de clientes a una herramienta nueva, lee quién la opera y dónde la guarda. |
| **Pyme** | Lista de herramientas externas que tocan datos sensibles, con dueño interno y decisión de mantener o retirar cada una. |
| **Gran empresa o multinacional** | Evaluación de riesgo de proveedores tecnológicos con cláusulas de acceso, auditoría y salida, y revisión de cambios de propietario. |

**Actividad sin crear sistemas:** Lista las herramientas externas que tocan tu información sensible y quién en la empresa autorizó cada una.

**Términos:** Riesgo de terceros (*Third-Party Risk*) · Cadena de suministro (*Supply Chain*)

**Caso en desarrollo:** [NVIDIA: sospecha de espionaje y protección del conocimiento](../../../case-studies/22-nvidia-sospecha-de-espionaje-y-proteccion-del-conocimiento.md#2-sospecha-o-alegación). Un cliente que compra mucho también puede ser un canal de influencia: analiza qué control exigirías sobre su acceso a tu tecnología y qué ocurre si la sospecha es solo una alegación. Es una investigación **no concluida**: separa lo oficial, lo alegado y lo desconocido.

*Enfoque defensivo: reconocer, prevenir, documentar y escalar. No enseña a obtener información de forma indebida; la calificación jurídica de un hecho concreto corresponde a un abogado.*

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

Ficha de evaluación de proveedores saas con seguridad, datos, continuidad y salida.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] cada proveedor crítico tiene ficha de evaluación completa
- [ ] la portabilidad de datos está verificada, no solo declarada
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Contratar sin acuerdo de tratamiento de datos personales.
- Descubrir al terminar que la exportación de datos no es usable.

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

1. ¿Tienes acuerdo de tratamiento de datos con cada proveedor que los procesa?
2. ¿Probaste alguna vez exportar tus datos y verificar que sirven?
3. ¿Qué pasa con tu operación si ese proveedor cierra en 30 días?

## 🔗 Fuentes oficiales

**Biblioteca del Congreso Nacional · LeyChile — Normativa oficial consolidada**  
<https://www.bcn.cl/leychile/> · verificado 2026-11-05

- *Qué contiene:* Publica el texto oficial y consolidado de leyes, decretos y reglamentos, con la versión vigente a una fecha, el historial de modificaciones y la tramitación que las originó.
- *Cómo leerla:* Usa siempre el selector de versión vigente a la fecha en que ejecutarás el trámite, no la última publicada. Y lee el artículo transitorio: en normas en implantación gradual —jornada, datos personales— ahí está la fecha que realmente te aplica.
- *Uso en esta clase:* aporta el marco de «Normativa oficial consolidada» para definir qué se evalúa antes de contratar un proveedor tecnológico.

**CNBC — Nvidia investigates CEO Jensen Huang's relationship with alleged Chinese spy (08-11-2026)**  
<https://www.cnbc.com/2026/11/08/nvidia-jensen-huang-investigation-china-spy.html> · verificado 2026-11-12

- *Qué contiene:* Reporta la comunicación del director ejecutivo al personal, la investigación independiente abierta por el directorio, las alegaciones atribuidas a agencias de inteligencia y a otros medios, la vinculación con un cliente llamado Megaspeed y la solicitud de tres comisiones del Congreso.
- *Cómo leerla:* Es prensa y el caso sigue abierto: úsala para fijar quién afirma qué y cuándo, no como prueba. Separa lo declarado por la empresa de lo atribuido a fuentes, y verifica los comunicados oficiales de NVIDIA a medida que avance la investigación.
- *Uso en esta clase:* aporta el marco de «Nvidia investigates CEO Jensen Huang's relationship with alleged Chinese spy (08-11-2026)» para definir qué se evalúa antes de contratar un proveedor tecnológico.

**Biblioteca del Congreso Nacional — Ley 21.719 — Protección y tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales**  
<https://www.bcn.cl/leychile/navegar?idNorma=1209272> · verificado 2026-11-25

- *Qué contiene:* Reemplaza el texto de la Ley 19.628. Su artículo 14 sexies obliga a reportar a la Agencia las vulneraciones de seguridad con riesgo razonable para los titulares y a avisar a estos cuando hay datos sensibles, de menores de catorce años o económicos.
- *Cómo leerla:* Úsala como estándar de diseño del protocolo de incidentes. La vigencia de sus modificaciones se fijó en el 15-10-2027 por la Ley 21.855: comprueba la fecha en la ficha de la BCN antes de planificar.
- *Uso en esta clase:* aporta el marco de «Ley 21.719 — Protección y tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales» para definir qué se evalúa antes de contratar un proveedor tecnológico.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 208 · Agentes de IA con humano en el circuito](../class-12-agentes-de-ia-con-humano-en-el-circuito/README.md) | [Parte 15](../README.md) · [Programa](../../../README.md) | [210 · Gobierno tecnológico y costos FinOps →](../class-14-gobierno-tecnologico-y-costos-finops/README.md) |
