# Política de seguridad

Este repositorio no ejecuta servicios ni procesa datos de terceros: es contenido educativo más
scripts de generación y validación en Python estándar. Aun así, tiene dos superficies de riesgo
reales y ambas se controlan en CI.

## Superficies de riesgo

| Superficie | Riesgo | Control |
|---|---|---|
| Contenido del currículo y plantillas | Filtración de datos personales reales (RUT, nombres, direcciones) o de credenciales en ejemplos | `gitleaks` sobre el árbol de archivos en cada push y pull request |
| Scripts de `scripts/` | Ejecución insegura, rutas no controladas, consumo de entradas no validadas | `bandit` con severidad media y alta en cada push y pull request |
| Workflows de GitHub Actions | Permisos excesivos o acciones sin fijar | Permisos mínimos declarados por workflow y acciones fijadas por versión mayor |
| Sitio de GitHub Pages | Inclusión de recursos externos | El sitio es autocontenido: sin CDN, sin fuentes remotas, sin analítica |

## Qué nunca debe entrar al repositorio

- RUT, nombres, direcciones, correos o antecedentes de personas o empresas reales.
- Claves, tokens, certificados, credenciales o archivos de firma electrónica, aunque sean de prueba.
- Documentos societarios, tributarios o laborales reales de un caso concreto.
- Capturas de pantalla con datos identificables.

Todos los casos y ejemplos del programa usan **datos ficticios**.

## Reportar una vulnerabilidad o una filtración

**No abras un issue público.** Usa el canal privado de GitHub:

1. Ve a la pestaña **Security** del repositorio.
2. **Report a vulnerability** (GitHub Private Vulnerability Reporting).
3. Describe el hallazgo, cómo reproducirlo y el impacto que le atribuyes.

Si el hallazgo es un dato personal publicado por error, indícalo de forma explícita para priorizar
su eliminación del historial.

### Tiempos de respuesta

| Etapa | Objetivo |
|---|---|
| Acuse de recibo | 72 horas |
| Evaluación inicial | 7 días |
| Corrección o plan de mitigación | 30 días |

## Alcance

Está en alcance todo lo que vive en este repositorio: contenido, scripts, workflows y el sitio
publicado en GitHub Pages.

Está fuera de alcance la infraestructura de GitHub y los sitios de terceros enlazados como fuentes
oficiales (SII, Dirección del Trabajo, CMF, INAPI y demás organismos), que tienen sus propios
canales de reporte.

## Divulgación

Se agradece la divulgación coordinada. Publicaremos el detalle una vez corregido, con crédito a
quien reportó si así lo desea.
