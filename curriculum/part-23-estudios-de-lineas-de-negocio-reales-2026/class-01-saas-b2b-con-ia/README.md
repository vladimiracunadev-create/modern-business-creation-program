# Clase 309 — SaaS B2B con IA

> **Parte 23 · Estudios de líneas de negocio reales 2026** — clase 1 de 14

**Estado de evidencia:** `SECTORIAL` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** validar margen con costo de inferencia y resolver el marco de tratamiento de datos<br>
**Entregable:** modelo de negocio SaaS con IA que incluye costo de inferencia, retención proyectada y acuerdo de datos

## 🎯 Propósito

Modelar un SaaS con IA incorporando el costo de inferencia, que rompe el supuesto de margen casi total del software tradicional.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —validar margen con costo de inferencia y resolver el marco de tratamiento de datos— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **SaaS B2B con IA** | Software por suscripción con componentes de modelos. |
| **Costo de inferencia** | Costo variable por uso de modelos, que afecta el margen. |
| **Acuerdo de tratamiento de datos** | Contrato que regula el uso de datos del cliente. |
| **Retención neta** | Indicador determinante de la viabilidad del modelo. |

## 🗺️ Modelo mental: Un margen que ya no es casi total

> **La idea en una frase:** El SaaS con IA introduce un costo variable relevante que rompe el supuesto de margen casi total del software tradicional; la viabilidad depende de que el precio contemple ese costo y de resolver el tratamiento de datos.

![Esquema: Un margen que ya no es casi total](modelo-mental.svg)

**Cómo leerlo:** Las tres barras comparan el margen de un software tradicional con dos versiones con IA. La diferencia entre las dos últimas es lo que cuesta fijar mal el precio de cada consulta al modelo.

**Piénsalo así:** Es una cafetería que, además del arriendo, paga cada taza de café servida: más clientes no son gratis y el precio de la taza debe cubrir su costo.

## 📖 Desarrollo

### 1. El fondo del asunto

El SaaS con IA introduce un costo variable relevante que rompe el supuesto de margen casi total del software tradicional. La viabilidad depende de que el precio contemple ese costo y de que los acuerdos con clientes permitan el tratamiento de datos que el servicio requiere.

### 2. Cómo se traduce en la práctica

Calcula el costo de inferencia por cliente y por uso, con escenarios de baja, media y alta intensidad. Diseña el precio con límites, tramos y cobro por exceso. Verifica con el proveedor de modelos dónde se procesan los datos y firma acuerdos de tratamiento con tus clientes. Monitorea el margen por cliente y la retención neta, y ajusta los planes si el costo cambia.

### 3. Marco aplicable y quién interviene

- matriz de líneas de negocio 2026 del repositorio (manifests/business_lines_2026.json)
- regulación sectorial aplicable según actividad económica
- economía unitaria por modelo: suscripción, proyecto, transacción, retail y servicio

**Autoridades o contrapartes involucradas:** autoridad sectorial según la línea analizada, SII, SERNAC, municipalidad.
**Profesionales de apoyo:** fundador, consultor sectorial, abogado regulatorio, contador. La participación concreta depende del riesgo, del
tamaño de la empresa y de la actividad económica.

### 4. Los números, paso a paso

Una empresa cobra $50.000 mensuales por cliente por un asistente con IA. Cada cliente hace 2.000 consultas y cada una cuesta $12 en costo de inferencia: $24.000 al mes, es decir 48 % del precio. Con solo otros costos del 5 %, el margen es 47 %. Al cambiar su precio a $70.000 con un límite de consultas incluidas y un cobro por exceso, el margen sube a cerca del 60 %. Además firma acuerdos de tratamiento de datos con sus clientes (cifras ilustrativas).

### 5. En qué se apoya

- **Lean Analytics** (O'Reilly): Croll y Yoskovitz describen las métricas de margen, retención y costo de servir de los negocios de software y su efecto en la viabilidad.
- **Ley 21.719 — Protección y tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales** (Biblioteca del Congreso Nacional): La Ley 21.719 regula el tratamiento de datos personales y la relación entre responsable y encargado, que se formaliza en un acuerdo con los clientes.

*Las lecturas de apoyo ofrecen marcos conceptuales; lo que exige la ley chilena se verifica en las fuentes oficiales de esta clase.*

## 🛡️ Protección del conocimiento: Ejemplos por tipo de empresa

[Guía de inteligencia económica y protección del conocimiento, sección 15](../../../docs/21_INTELIGENCIA_ECONOMICA_Y_PROTECCION_DEL_CONOCIMIENTO.md#15-ejemplos-por-tipo-de-empresa)

**Lente para esta clase:** Para una empresa de software el activo es el código y la arquitectura: la fuga ocurre por cuentas olvidadas, repositorios abiertos y desarrolladores que se van.

| Nivel | Medida proporcionada |
|---|---|
| **Emprendedor o microempresa** | Todo el código en cuentas de la empresa y la propiedad asignada por contrato. |
| **Pyme** | Revisión mensual de cuentas con lista firmada y contrato de cesión del código. |
| **Gran empresa o multinacional** | Gobierno de repositorios, clasificación de código y controles de salida de personal. |

**Actividad sin crear sistemas:** Lista quién tiene acceso al código y quién ya no debería tenerlo.

**Términos:** Código fuente (*Source Code*) · Cesión de derechos (*Assignment of Rights*)

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

Modelo de negocio saas con ia que incluye costo de inferencia, retención proyectada y acuerdo de datos.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] el costo de inferencia está incorporado al margen
- [ ] el acuerdo de tratamiento de datos está definido
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Fijar precio de suscripción sin modelar el costo variable de inferencia.
- Procesar datos de clientes con modelos sin acuerdo de tratamiento.

**Característicos de la parte 23:**

- Entrar a un sector regulado subestimando el costo y el plazo de habilitación.
- Asumir márgenes de referencia internacional que no aplican al mercado chileno.

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

1. ¿Cuánto representa el costo de inferencia sobre tu precio de suscripción?
2. ¿Tu contrato con clientes autoriza el tratamiento que el servicio necesita?
3. ¿Cuál es tu NRR proyectado y qué lo sostiene?

## 🔗 Fuentes oficiales

**Biblioteca del Congreso Nacional · LeyChile — Normativa oficial consolidada**  
<https://www.bcn.cl/leychile/> · verificado 2026-11-05

- *Qué contiene:* Publica el texto oficial y consolidado de leyes, decretos y reglamentos, con la versión vigente a una fecha, el historial de modificaciones y la tramitación que las originó.
- *Cómo leerla:* Usa siempre el selector de versión vigente a la fecha en que ejecutarás el trámite, no la última publicada. Y lee el artículo transitorio: en normas en implantación gradual —jornada, datos personales— ahí está la fecha que realmente te aplica.
- *Uso en esta clase:* aporta el marco de «Normativa oficial consolidada» para validar margen con costo de inferencia y resolver el marco de tratamiento de datos.

**Servicio de Impuestos Internos — Nuevos contribuyentes, inicio de actividades y DTE**  
<https://www.sii.cl/ayudas/nuevos_contribuyentes/boleta-vys-facturador.html> · verificado 2026-11-05

- *Qué contiene:* Reúne el circuito completo del contribuyente nuevo: obtención de RUT, declaración de inicio de actividades, elección de códigos de actividad económica y habilitación para emitir documentos tributarios electrónicos.
- *Cómo leerla:* Sepáralo en dos actos distintos que la página trata seguidos: el RUT identifica, el inicio de actividades habilita. Lo que te bloquea para facturar casi siempre está en el segundo, no en el primero.
- *Uso en esta clase:* aporta el marco de «Nuevos contribuyentes, inicio de actividades y DTE» para validar margen con costo de inferencia y resolver el marco de tratamiento de datos.

**O'Reilly — Lean Analytics**  
<https://openlibrary.org/isbn/9781449335717> · verificado 2026-11-25

- *Qué contiene:* Propone métricas por etapa de una startup y cómo elegir la métrica que importa en cada momento.
- *Cómo leerla:* Úsalo como marco conceptual para entender el porqué de la práctica, nunca como prueba de lo que exige la ley chilena; para eso están las fuentes oficiales de la clase.
- *Uso en esta clase:* aporta el marco de «Lean Analytics» para validar margen con costo de inferencia y resolver el marco de tratamiento de datos.

**Biblioteca del Congreso Nacional — Ley 21.719 — Protección y tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales**  
<https://www.bcn.cl/leychile/navegar?idNorma=1209272> · verificado 2026-11-25

- *Qué contiene:* Reemplaza el texto de la Ley 19.628. Su artículo 14 sexies obliga a reportar a la Agencia las vulneraciones de seguridad con riesgo razonable para los titulares y a avisar a estos cuando hay datos sensibles, de menores de catorce años o económicos.
- *Cómo leerla:* Úsala como estándar de diseño del protocolo de incidentes. La vigencia de sus modificaciones se fijó en el 15-10-2027 por la Ley 21.855: comprueba la fecha en la ficha de la BCN antes de planificar.
- *Uso en esta clase:* aporta el marco de «Ley 21.719 — Protección y tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales» para validar margen con costo de inferencia y resolver el marco de tratamiento de datos.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| **Inicio de la parte** | [Parte 23](../README.md) · [Programa](../../../README.md) | [310 · Agencia de automatización e IA aplicada →](../class-02-agencia-de-automatizacion-e-ia-aplicada/README.md) |
