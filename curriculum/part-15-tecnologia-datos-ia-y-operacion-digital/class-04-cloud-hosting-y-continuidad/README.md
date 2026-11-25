# Clase 200 — Cloud, hosting y continuidad

> **Parte 15 · Tecnología, datos, IA y operación digital** — clase 4 de 14

**Estado de evidencia:** `DINAMICO` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** elegir infraestructura considerando disponibilidad, ubicación de datos y costo de salida<br>
**Entregable:** decisión de infraestructura con disponibilidad comprometida, región y evaluación de costo de salida

## 🎯 Propósito

Elegir infraestructura evaluando disponibilidad, ubicación de los datos y costo de salida, no solo precio mensual.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —elegir infraestructura considerando disponibilidad, ubicación de datos y costo de salida— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **Cloud** | Infraestructura contratada como servicio. |
| **Disponibilidad** | Porcentaje de tiempo operativo comprometido. |
| **Región** | Ubicación geográfica de los datos. |
| **Bloqueo de proveedor** | Dificultad de migrar por dependencia técnica. |

## 🗺️ Modelo mental: La comodidad de la nube y el costo de irse

> **La idea en una frase:** La ubicación de los datos importa por normativa y latencia; la dependencia del proveedor se acumula silenciosamente con cada servicio propietario que se adopta.

![Esquema: La comodidad de la nube y el costo de irse](modelo-mental.svg)

**Lectura guiada:** Compara los dos platos. Lo que ganas es visible desde el primer día; lo que se acumula, solo cuando quieres cambiar de proveedor o cuando una autoridad pregunta dónde están tus datos.

**Una analogía:** Es mudarse a un departamento amoblado: es cómodo hoy, pero cada mueble que no es tuyo hace más difícil irse mañana.

## 📖 Desarrollo

### 1. El fondo del asunto

La ubicación de los datos importa por normativa y por latencia. La dependencia del proveedor se acumula silenciosamente con cada servicio propietario que se adopta; evaluar el costo de salida al momento de entrar es lo que mantiene la opción abierta.

### 2. Cómo se traduce en la práctica

Antes de elegir infraestructura, define tus requisitos de disponibilidad, la región donde pueden estar los datos y el costo de salida. Prefiere estándares abiertos y formatos exportables. Documenta cada servicio propietario que uses y su alternativa. Revisa los contratos: plazos, penalidades y devolución de datos. Evalúa cada año si la dependencia sigue siendo aceptable.

### 3. Marco aplicable y quién interviene

- Ley 21.663 Marco de Ciberseguridad y su reglamentación
- Ley 21.719 en lo relativo a tratamiento automatizado y decisiones basadas en datos
- controles de referencia tipo CIS Controls y NIST CSF adaptados a pyme

**Autoridades o contrapartes involucradas:** ANCI, CSIRT Nacional, Agencia de Protección de Datos Personales (en implementación).
**Profesionales de apoyo:** responsable de TI, consultor de ciberseguridad, analista de datos, abogado de datos. La participación concreta depende del riesgo, del
tamaño de la empresa y de la actividad económica.

### 4. Antes y después

Antes: una empresa de reservas adopta servicios exclusivos de un proveedor y, tres años después, quiere cambiarse por un alza de precios; descubre que reconstruir su arquitectura costaría más que seguir pagando. Después: define en cada nueva contratación cómo exportaría sus datos y qué alternativas existen, elige estándares abiertos donde puede y documenta la región de sus datos. Cambia de proveedor un servicio secundario en pocas semanas (caso ilustrativo).

### 5. En qué se apoya

- **Ley 21.719 — Protección y tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales** (Biblioteca del Congreso Nacional): La Ley 21.719 regula las transferencias y el tratamiento de datos personales, relevantes para decidir la ubicación de los datos en servicios en la nube.
- **Designing Data-Intensive Applications** (O'Reilly): Kleppmann explica los compromisos de diseño de sistemas de datos confiables y mantenibles, que ayudan a evaluar qué dependencia técnica se asume al elegir un servicio.

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

Decisión de infraestructura con disponibilidad comprometida, región y evaluación de costo de salida.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] la ubicación de los datos está identificada
- [ ] el costo de salida está evaluado
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Elegir proveedor sin evaluar el costo de una eventual migración.
- Desconocer en qué país residen los datos de clientes.

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

1. ¿En qué país residen los datos de tus clientes y lo sabes con certeza?
2. ¿Cuánto costaría migrar a otro proveedor si tuvieras que hacerlo?
3. ¿Qué disponibilidad te comprometió el proveedor y cómo la verificas?

## 🔗 Fuentes oficiales

**Biblioteca del Congreso Nacional · LeyChile — Normativa oficial consolidada**  
<https://www.bcn.cl/leychile/> · verificado 2026-11-05

- *Qué contiene:* Publica el texto oficial y consolidado de leyes, decretos y reglamentos, con la versión vigente a una fecha, el historial de modificaciones y la tramitación que las originó.
- *Cómo leerla:* Usa siempre el selector de versión vigente a la fecha en que ejecutarás el trámite, no la última publicada. Y lee el artículo transitorio: en normas en implantación gradual —jornada, datos personales— ahí está la fecha que realmente te aplica.
- *Uso en esta clase:* aporta el marco de «Normativa oficial consolidada» para elegir infraestructura considerando disponibilidad, ubicación de datos y costo de salida.

**Biblioteca del Congreso Nacional — Ley 21.719 — Protección y tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales**  
<https://www.bcn.cl/leychile/navegar?idNorma=1209272> · verificado 2026-11-25

- *Qué contiene:* Reemplaza el texto de la Ley 19.628. Su artículo 14 sexies obliga a reportar a la Agencia las vulneraciones de seguridad con riesgo razonable para los titulares y a avisar a estos cuando hay datos sensibles, de menores de catorce años o económicos.
- *Cómo leerla:* Úsala como estándar de diseño del protocolo de incidentes. La vigencia de sus modificaciones se fijó en el 15-10-2027 por la Ley 21.855: comprueba la fecha en la ficha de la BCN antes de planificar.
- *Uso en esta clase:* aporta el marco de «Ley 21.719 — Protección y tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales» para elegir infraestructura considerando disponibilidad, ubicación de datos y costo de salida.

**O'Reilly — Designing Data-Intensive Applications**  
<https://openlibrary.org/isbn/9781449373320> · verificado 2026-11-25

- *Qué contiene:* Explica los principios de sistemas de datos confiables, escalables y mantenibles. Se usa como lectura de apoyo conceptual y no como fuente normativa.
- *Cómo leerla:* Úsalo como marco conceptual para entender el porqué de la práctica, nunca como prueba de lo que exige la ley chilena; para eso están las fuentes oficiales de la clase.
- *Uso en esta clase:* aporta el marco de «Designing Data-Intensive Applications» para elegir infraestructura considerando disponibilidad, ubicación de datos y costo de salida.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 199 · Dominio, correo, identidad y accesos](../class-03-dominio-correo-identidad-y-accesos/README.md) | [Parte 15](../README.md) · [Programa](../../../README.md) | [201 · Backups y recuperación →](../class-05-backups-y-recuperacion/README.md) |
