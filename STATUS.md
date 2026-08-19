# Estado del programa

Números verificables contra el repositorio. Cada cifra se puede reproducir con los comandos de la
sección final; el CI vuelve a comprobarlas en cada push.

## Contenido

| Métrica | Valor |
|---|---:|
| Versión | 1.2.0 |
| Etapas | 6 |
| Partes | 24 |
| Clases | 336 |
| Clases por parte | 14 |
| Palabras totales del currículo | 436.795 |
| Palabras por clase | 1.143–1.798 (mediana 1.290) |
| Diagramas mermaid | 360 (uno por clase + uno por parte) |
| Conceptos con definición operacional | 1.344 |
| Términos del glosario maestro | 1.251 |
| Preguntas de comprobación | 1.008 (3 por clase) |
| Decisiones habilitadas (una por clase) | 336 |
| Entregables definidos | 336 |
| Criterios de aceptación específicos | 336 conjuntos |
| Narrativas de parte | 24 |
| Manuales transversales (`docs/`) | 20 |
| Casos de líneas de negocio (`case-studies/`) | 20 |
| Plantillas operativas (`templates/`) | 24 |
| Fuentes en el registro | 32 (28 citadas · 30 verificadas · 2 pendientes) |
| Cuerpos normativos mapeados | 53 |
| Revalidación de fuentes | por fuente (`accessed` en `sources/bibliography.json`); última pasada 2026-08-19 |

## Publicación

| Superficie | Valor |
|---|---:|
| Páginas del sitio HTML | 426 |
| Enlaces internos verificados en el sitio | 26.400+ |
| Manual integral en PDF | 1.549 páginas · ~4,0 MB |
| PDF por parte | 24 · ~63 páginas cada uno |
| Workflows de CI | 4 |
| Dependencias de terceros | 2, fijadas a versión exacta |

## Cobertura por estado de evidencia

| Estado | Partes |
|---|---:|
| `VERIFICADO-FUENTE` | 9 |
| `GUIA-PRACTICA` | 10 |
| `DINAMICO` | 3 |
| `SECTORIAL` | 2 |

## Controles automáticos

| Control | Qué verifica |
|---|---|
| `scripts/generar_clases.py --check` | que ningún README de clase o parte, ni `CURRICULUM.md`, ni el glosario, ni el bloque de partes del README estén desincronizados respecto de su manifiesto, y que no queden carpetas huérfanas |
| `scripts/validar_estructura.py` | coherencia de manifiestos, existencia de las 336 clases, las 13 secciones obligatorias por clase y las 9 de cada parte, presencia del diagrama, todos los enlaces relativos y que las fuentes sean https |
| `scripts/validar_encoding.py` | UTF-8 sin BOM y sin mojibake, por round-trip cp1252 en vez de lista de secuencias |
| `scripts/generar_sitio.py` | que las 426 páginas compilen y que ninguno de sus enlaces internos rompa |
| `scripts/generar_manual.py` | que el manual compile y que la portada y el número de páginas sean los esperados |
| `markdownlint-cli2` | Markdown estructuralmente válido en todo el repositorio |
| `python -m unittest discover -s tests` | 23 pruebas: currículo, manifiestos, pedagogía, cobertura de etapas y sincronía del README |
| `gitleaks` | ausencia de secretos en el árbol de archivos |
| `bandit` | análisis estático de los scripts de Python |
| `pip-audit` | vulnerabilidades conocidas en las dependencias fijadas |

## Cómo reproducir las cifras

```bash
# Partes y clases
ls -d curriculum/part-* | wc -l
find curriculum -mindepth 3 -name README.md | wc -l

# Palabras del currículo
find curriculum -mindepth 3 -name README.md -exec cat {} + | wc -w

# Diagramas
grep -rl '```mermaid' curriculum | wc -l

# Términos del glosario y fuentes
grep -c '^| \*\*' docs/19_GLOSSARY.md
python -c "import json;print(len(json.load(open('sources/bibliography.json',encoding='utf-8'))['entries']))"
python scripts/verify-sources

# Páginas del sitio y del manual
python scripts/generar_sitio.py && find site -name '*.html' | wc -l
python scripts/generar_manual.py
```

## Lo que estos controles no garantizan

El CI verifica estructura, sincronía, codificación, enlaces y que los artefactos compilen.
**No verifica exactitud jurídica ni vigencia normativa**: eso exige revisión humana contra la
fuente oficial. Las partes marcadas como `DINAMICO` cambian por definición, y el resto envejece
con cada reforma.

Última revisión manual de la base normativa: **2026-08-07**.
