# Clase 026 — MVP, prototipo y concierge test

> **Parte 02 · Descubrimiento, validación y mercado** — clase 12 de 14

**Estado de evidencia:** `GUIA-PRACTICA` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** decidir qué se entrega manualmente y qué se automatiza en la primera versión<br>
**Entregable:** definición de MVP con lo que sí incluye, lo que no incluye y lo que se hará manual

## 🎯 Propósito

Definir la primera versión por lo que permite aprender, no por lo que permite lucir, y decidir explícitamente qué se entrega a mano antes de automatizar.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —decidir qué se entrega manualmente y qué se automatiza en la primera versión— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **MVP** | Versión mínima que permite aprender lo crítico entregando valor real. |
| **Prototipo** | Representación que permite evaluar sin operar. |
| **Concierge test** | Entrega manual del servicio para validar antes de automatizar. |
| **Deuda de aprendizaje** | Conocimiento no adquirido por saltarse la etapa manual. |

## 🗺️ Modelo mental: Concierge test: primero a mano, después con software

> **La idea en una frase:** El concierge test entrega a mano lo que después será software: su valor no es ahorrar desarrollo sino descubrir las excepciones reales del proceso.

![Esquema: Concierge test: primero a mano, después con software](modelo-mental.svg)

**Lectura guiada:** Sigue los pasos de izquierda a derecha. El rombo es la decisión: solo se automatiza lo que se repite y compensa su costo. Si no, se vuelve atrás y se ajusta la oferta.

**Para recordarlo:** Es cocinar para tus primeros clientes en la cocina de tu casa: antes de comprar un horno industrial, aprendes qué piden y qué platos se repiten.

## 📖 Desarrollo

### 1. El fondo del asunto

El concierge test es la forma más barata de validar servicios: se entrega manualmente lo que después será software. Su valor no es ahorrar desarrollo sino descubrir las excepciones reales del proceso, que son justamente lo que hace fracasar la automatización prematura.

### 2. Cómo se traduce en la práctica

Elige un cliente dispuesto a probar y entrega el servicio con herramientas simples, sin programar. Registra por escrito cada excepción, cada pregunta y el tiempo que toma. Repite con tres a cinco clientes y revisa cuáles tareas aparecen siempre. Esas son candidatas a automatizar; las demás se mantienen manuales o se eliminan. Decláralo al cliente: honestidad sobre cómo se presta el servicio.

### 3. Marco aplicable y quién interviene

- método de descubrimiento de clientes y experimentación acotada
- Jobs to Be Done como marco de resultados esperados
- estadística oficial chilena: INE, Banco Central, Censo y encuestas sectoriales

**Autoridades o contrapartes involucradas:** INE, Banco Central de Chile, SII (estadísticas de empresas por rubro).
**Profesionales de apoyo:** fundador, investigador de mercado, analista de datos. La participación concreta depende del riesgo, del
tamaño de la empresa y de la actividad económica.

### 4. Una conversación que enseña

Fundador: «¿Cómo entregamos el informe a los primeros tres clientes?». Socia: «A mano: yo lo armo con sus datos y se lo mando». Fundador: «¿Y qué descubrimos?». Socia: «Que dos de tres tienen datos distintos en cada mes y que el tercero pide un gráfico que no habíamos pensado». Fundador: «Si lo hubiéramos programado primero, habríamos construido el formato equivocado». Después de cuatro semanas deciden automatizar solo las dos tareas que se repetían en los tres casos (conversación ilustrativa).

### 5. En qué se apoya

- **The Lean Startup (2011)** (Crown Business): Ries describe el producto mínimo viable y el concierge como formas de aprender del cliente con el menor esfuerzo posible, antes de construir la solución completa.
- **Running Lean** (O'Reilly): Maurya propone iterar el modelo de negocio con experimentos cortos y un producto mínimo, aprendiendo de cada cliente real.

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

Definición de mvp con lo que sí incluye, lo que no incluye y lo que se hará manual.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] el MVP entrega valor real a un cliente identificado
- [ ] está explícito qué se opera manualmente y por qué
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Construir producto completo antes de haber entregado el servicio a mano una vez.
- Llamar mvp a un producto incompleto que no entrega ningún valor.

**Característicos de la parte 02:**

- Entrevistar buscando confirmación en vez de refutación.
- Estimar mercado de arriba hacia abajo sin conexión con capacidad real de venta.

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

1. ¿Qué parte de tu MVP entregarás manualmente y por cuánto tiempo?
2. ¿Qué aprendizaje concreto buscas obtener con esta versión?
3. ¿Tu MVP entrega valor real a alguien identificable o es un producto incompleto?

## 🔗 Fuentes oficiales

**Biblioteca del Congreso Nacional · LeyChile — Normativa oficial consolidada**  
<https://www.bcn.cl/leychile/> · verificado 2026-11-05

- *Qué contiene:* Publica el texto oficial y consolidado de leyes, decretos y reglamentos, con la versión vigente a una fecha, el historial de modificaciones y la tramitación que las originó.
- *Cómo leerla:* Usa siempre el selector de versión vigente a la fecha en que ejecutarás el trámite, no la última publicada. Y lee el artículo transitorio: en normas en implantación gradual —jornada, datos personales— ahí está la fecha que realmente te aplica.
- *Uso en esta clase:* aporta el marco de «Normativa oficial consolidada» para decidir qué se entrega manualmente y qué se automatiza en la primera versión.

**Servicio de Cooperación Técnica — Fomento para micro y pequeñas empresas**  
<https://www.sercotec.cl/> · verificado 2026-11-05

- *Qué contiene:* Publica las convocatorias vigentes con sus bases: perfil de empresa elegible, monto del subsidio, cofinanciamiento exigido, gastos financiables y obligaciones de rendición.
- *Cómo leerla:* Lee las bases desde el final: la sección de rendición decide si podrás quedarte con el subsidio. Muchos proyectos se adjudican y después devuelven fondos por no poder acreditar el gasto en la forma exigida.
- *Uso en esta clase:* aporta el marco de «Fomento para micro y pequeñas empresas» para decidir qué se entrega manualmente y qué se automatiza en la primera versión.

**ProChile — Programas, estudios de mercado y promoción**  
<https://www.prochile.gob.cl/> · verificado 2026-11-05

- *Qué contiene:* Publica estudios de mercado por país y sector, agendas de negocios, ferias, y los programas de cofinanciamiento de actividades de promoción.
- *Cómo leerla:* Los estudios de mercado por país son el mejor uso gratuito: entregan tamaño, canales, competencia y requisitos de entrada verificados, que es justo lo que una estimación bottom-up necesita.
- *Uso en esta clase:* aporta el marco de «Programas, estudios de mercado y promoción» para decidir qué se entrega manualmente y qué se automatiza en la primera versión.

**Crown Business — The Lean Startup (2011)**  
<https://openlibrary.org/isbn/9780307887894> · verificado 2026-11-25

- *Qué contiene:* Propone construir, medir y aprender con ciclos cortos y con indicadores accionables, en lugar de métricas de vanidad.
- *Cómo leerla:* Úsalo como marco conceptual para entender el porqué de la práctica, nunca como prueba de lo que exige la ley chilena; para eso están las fuentes oficiales de la clase.
- *Uso en esta clase:* aporta el marco de «The Lean Startup (2011)» para decidir qué se entrega manualmente y qué se automatiza en la primera versión.

**O'Reilly — Running Lean**  
<https://openlibrary.org/isbn/9781449331900> · verificado 2026-11-25

- *Qué contiene:* Método para iterar un modelo de negocio con el lienzo lean y experimentos cortos. Se usa como lectura de apoyo conceptual y no como fuente normativa.
- *Cómo leerla:* Úsalo como marco conceptual para entender el porqué de la práctica, nunca como prueba de lo que exige la ley chilena; para eso están las fuentes oficiales de la clase.
- *Uso en esta clase:* aporta el marco de «Running Lean» para decidir qué se entrega manualmente y qué se automatiza en la primera versión.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 025 · Experimentos de demanda antes de invertir](../class-11-experimentos-de-demanda-antes-de-invertir/README.md) | [Parte 02](../README.md) · [Programa](../../../README.md) | [027 · Precio como experimento de mercado →](../class-13-precio-como-experimento-de-mercado/README.md) |
