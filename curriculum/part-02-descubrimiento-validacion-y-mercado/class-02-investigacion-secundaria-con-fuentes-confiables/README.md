# Clase 016 — Investigación secundaria con fuentes confiables

> **Parte 02 · Descubrimiento, validación y mercado** — clase 2 de 14

**Estado de evidencia:** `GUIA-PRACTICA` · **Jurisdicción:** Chile-first · **Fecha base normativa:** 07-08-2026<br>
**Decisión que habilita:** definir qué fuentes se usarán y con qué frecuencia se revalidan<br>
**Entregable:** tabla de datos y tendencias de mercado con fuente, URL, fecha de consulta, fecha de corte, método, limitación y confianza

## 🎯 Propósito

Construir una base de datos y tendencias de mercado con fuentes primarias trazables, método, limitación y confianza declarados.

## 📚 Resultados de aprendizaje

Al finalizar esta clase podrás:

1. **Definir** con precisión los cuatro conceptos de la tabla siguiente y usarlos para describir un caso real.
2. **Explicar** por qué esta materia condiciona decisiones de otras partes del programa.
3. **Decidir** —definir qué fuentes se usarán y con qué frecuencia se revalidan— y justificar la decisión por escrito.
4. **Producir** el entregable de la clase y contrastarlo contra su criterio de aceptación.
5. **Distinguir** el dato estable del dato dinámico que exige revalidación en la fuente oficial.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| **Fuente primaria** | Dato producido por quien lo genera: organismo oficial, registro, censo. |
| **Fuente secundaria** | Interpretación o resumen elaborado por un tercero. |
| **Fecha de corte** | Momento al que corresponde el dato y a partir del cual envejece. |
| **Trazabilidad** | Posibilidad de reconstruir de dónde salió cada cifra. |

## 🗺️ Flujo de razonamiento

```mermaid
flowchart TB
    C["Contexto del caso<br/>actividad · escala · comuna"]
    C --> A1["Fuente primaria"]
    C --> A2["Fuente secundaria"]
    C --> A3["Fecha de corte"]
    C --> A4["Trazabilidad"]
    A1 & A2 & A3 & A4 --> D{{"definir qué fuentes se usarán<br/>y con qué frecuencia se<br/>revalidan"}}
    D --> E["Entregable<br/>tabla de datos y tendencias de<br/>mercado con fuente, URL, fecha<br/>de consulta, fecha de corte,<br/>método, limitación y confianza"]
    E --> V{"¿Cumple el criterio<br/>de aceptación?"}
    V -->|sí| S["Evidencia archivada<br/>y clase siguiente"]
    V -->|no| C
```

## 📖 Desarrollo

### 1. El fondo del asunto

En Chile la investigación secundaria seria se apoya en INE, Banco Central, estadísticas del SII por rubro y registros sectoriales. Cada cifra usada en una decisión debe tener fuente, fecha, método y limitación; una cifra sin trazabilidad no se puede defender ante un banco, un inversionista ni un comité. Las tendencias se registran como series o señales observables, con nivel de confianza y preguntas todavía abiertas, no como adjetivos sobre el mercado.

### 2. Cómo se traduce en la práctica

En Chile la investigación seria se apoya en el INE para población y empleo, el Banco Central para series macro y las estadísticas del SII por rubro y tamaño. La regla es bajar el dato a la comuna cuando el negocio sea local y conservar fecha de corte, método, limitación y señal observable: un promedio nacional o una tendencia sin serie rara vez describe el mercado alcanzable.

### 3. Marco aplicable y quién interviene

- método de descubrimiento de clientes y experimentación acotada
- Jobs to Be Done como marco de resultados esperados
- estadística oficial chilena: INE, Banco Central, Censo y encuestas sectoriales

**Autoridades o contrapartes involucradas:** INE, Banco Central de Chile, SII (estadísticas de empresas por rubro).
**Profesionales de apoyo:** fundador, investigador de mercado, analista de datos. La participación concreta depende del riesgo, del
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

Tabla de datos y tendencias de mercado con fuente, url, fecha de consulta, fecha de corte, método, limitación y confianza.

Debe incluir decisión, supuestos, fuentes con fecha de consulta, responsable, riesgos
identificados y próximos pasos.

## 🏆 Reto verificable

Resuelve la misma materia para una segunda línea de negocio con distinta carga regulatoria y
explica por escrito **qué cambió, por qué y qué fuente lo determina**.

## ✅ Criterio de aceptación

- [ ] cada cifra tiene fuente primaria identificable, fecha y método
- [ ] cada tendencia declara señal observable, limitación y nivel de confianza
- [ ] los datos dinámicos están marcados para revalidación
- [ ] cada afirmación regulatoria está referida a una fuente oficial con fecha de consulta;
- [ ] los datos dinámicos quedan marcados para revalidación;
- [ ] hay un responsable asignado y evidencia reproducible del trabajo.

## ⚠️ Errores frecuentes

**Propios de esta clase:**

- Citar una nota de prensa que a su vez cita un informe que nadie leyó.
- Usar una cifra de mercado global como si describiera el mercado chileno.

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

1. ¿Cuál es la fuente primaria, fecha, método y limitación de cada cifra que usas?
2. ¿Qué señal observable sostiene cada tendencia y qué otra explicación podría producirla?
3. ¿Qué cifras son dinámicas, qué confianza les asignas y cuándo toca revalidarlas?

## 🔗 Fuentes oficiales

**Instituto Nacional de Estadísticas — Estadística oficial de población, empleo y actividad**  
<https://www.ine.gob.cl/> · verificado 2026-09-01

- *Qué contiene:* Produce la estadística oficial del país: población y hogares por comuna, empleo, remuneraciones, IPC e índices sectoriales de actividad.
- *Cómo leerla:* Es la base de cualquier dimensionamiento bottom-up serio en Chile. Baja el dato por comuna cuando el negocio sea local; los promedios nacionales rara vez describen el mercado al que realmente puedes llegar.
- *Uso en esta clase:* aporta el marco de «Estadística oficial de población, empleo y actividad» para definir qué fuentes se usarán y con qué frecuencia se revalidan.

**Banco Central de Chile — Estadísticas macroeconómicas, tipo de cambio y UF**  
<https://www.bcentral.cl/> · verificado 2026-09-01

- *Qué contiene:* Publica las series oficiales de tipo de cambio, UF, UTM, tasas de interés, cuentas nacionales y balanza de pagos, además de la normativa cambiaria aplicable a operaciones con el exterior.
- *Cómo leerla:* Toma de aquí toda serie que uses en una proyección y guarda la fecha de descarga. Si la empresa cobra o paga en moneda extranjera, la serie de tipo de cambio es el insumo para medir la exposición, no una referencia informativa.
- *Uso en esta clase:* aporta el marco de «Estadísticas macroeconómicas, tipo de cambio y UF» para definir qué fuentes se usarán y con qué frecuencia se revalidan.

**Servicio de Impuestos Internos — Nuevos contribuyentes, inicio de actividades y DTE**  
<https://www.sii.cl/ayudas/nuevos_contribuyentes/boleta-vys-facturador.html> · verificado 2026-09-01

- *Qué contiene:* Reúne el circuito completo del contribuyente nuevo: obtención de RUT, declaración de inicio de actividades, elección de códigos de actividad económica y habilitación para emitir documentos tributarios electrónicos.
- *Cómo leerla:* Sepáralo en dos actos distintos que la página trata seguidos: el RUT identifica, el inicio de actividades habilita. Lo que te bloquea para facturar casi siempre está en el segundo, no en el primero.
- *Uso en esta clase:* aporta el marco de «Nuevos contribuyentes, inicio de actividades y DTE» para definir qué fuentes se usarán y con qué frecuencia se revalidan.

Complementos del repositorio: [glosario](../../../docs/19_GLOSSARY.md) ·
[ruta de lecturas](../../../docs/15_BOOKS_AND_LEARNING_PATH.md) ·
[catálogo de fuentes](../../../docs/16_OFFICIAL_SOURCE_CATALOG.md).

> [!IMPORTANT]
> Material educativo. Para una decisión real de alto impacto hay que verificar la fuente oficial
> vigente y validar con el profesional competente.

---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 015 · Formulación del problema empresarial](../class-01-formulacion-del-problema-empresarial/README.md) | [Parte 02](../README.md) · [Programa](../../../README.md) | [017 · Entrevistas de descubrimiento sin sesgos →](../class-03-entrevistas-de-descubrimiento-sin-sesgos/README.md) |
