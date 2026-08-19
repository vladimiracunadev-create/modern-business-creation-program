# Contribuir

Gracias por querer mejorar este programa. Las reglas de abajo existen para que el material siga
siendo verificable y no se degrade en opiniones sin respaldo.

## Regla número uno: el contenido vive en `manifests/`

Los `README.md` de `curriculum/` **se generan**. Editarlos a mano hace fallar el CI.

| Quiero cambiar… | Edito… |
|---|---|
| El contenido de una clase | `manifests/classes/parts-NN-NN.json` (entrada con `"n"` = número global) |
| El marco normativo, riesgos o fuentes de una parte | `manifests/part_packs.json` |
| El título o la posición de una clase | `manifests/curriculum.json` |
| Una fuente oficial | `sources/bibliography.json` (después: `python scripts/verify-sources --escribir`) |
| La plantilla con que se renderiza una clase | `scripts/generar_clases.py` |

Después de editar:

```bash
python scripts/generar_clases.py
python scripts/validar_estructura.py
python scripts/validar_encoding.py
python -m unittest discover -s tests -v
```

## Reglas de contenido

Toda mejora debe:

1. **preservar la secuencia pedagógica**: una clase no puede exigir conceptos que aún no se enseñaron;
2. **citar fuente primaria** cuando trate regulación — organismo o LeyChile, nunca una nota de prensa;
3. **registrar la fecha de verificación** de cualquier dato que pueda cambiar;
4. **no presentar una tasa, monto o plazo dinámico como permanente**;
5. **indicar si una obligación es general o sectorial**, y para qué actividad;
6. **incluir criterio de aceptación verificable** en el entregable;
7. **ser específica de la clase**: si el texto sirve igual para otra clase, no aporta.

## Reglas de forma

- Español de Chile, sin anglicismos innecesarios y sin tono publicitario.
- UTF-8 sin BOM. `scripts/validar_encoding.py` rechaza mojibake y BOM.
- Markdown que pase `markdownlint-cli2` con la configuración del repositorio.
- Enlaces relativos que existan: `scripts/validar_estructura.py` los revisa todos.
- URL de fuentes siempre `https://`.

## Qué no se acepta

- Datos personales reales: RUT, nombres, direcciones, antecedentes de personas o empresas concretas.
- Claves, tokens, certificados o credenciales, aunque sean de ejemplo.
- Texto legal reproducido en extenso; se cita y se enlaza.
- Afirmaciones regulatorias sin fuente.
- Contenido generado sin revisión que repita la misma estructura entre clases.

## Flujo de trabajo

1. Crea una rama desde `main`.
2. Haz el cambio en `manifests/` y regenera.
3. Ejecuta los cuatro comandos de validación de arriba; todos deben pasar.
4. Abre un pull request describiendo **qué cambió, por qué y contra qué fuente**.
5. El CI debe quedar en verde antes de la revisión.

## Reportar un problema

- **Error de contenido o de norma:** abre un issue indicando clase, afirmación cuestionada y fuente que la contradice.
- **Vulnerabilidad o dato personal filtrado:** no abras un issue público; sigue [`SECURITY.md`](SECURITY.md).
