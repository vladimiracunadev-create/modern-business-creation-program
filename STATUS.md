# Estado del programa

Números verificables contra el repositorio. Cada cifra se puede reproducir con los comandos de la
sección final; el CI vuelve a comprobarlas en cada push.

| Métrica | Valor |
|---|---:|
| Versión | 1.0.0 |
| Partes | 24 |
| Clases | 336 |
| Clases por parte | 14 |
| Palabras totales del currículo | 281.184 |
| Palabras por clase | 787–910 (mediana 835) |
| Conceptos con definición operacional | 1.344 |
| Decisiones habilitadas (una por clase) | 336 |
| Entregables definidos | 336 |
| Criterios de aceptación específicos | 336 conjuntos |
| Manuales transversales (`docs/`) | 20 |
| Casos de líneas de negocio (`case-studies/`) | 20 |
| Plantillas operativas (`templates/`) | 24 |
| Fuentes oficiales catalogadas | 28 |
| Cuerpos normativos mapeados | 53 |
| Páginas del sitio HTML | 421 |
| Workflows de CI | 3 |
| Fecha base normativa | 07-08-2026 |

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
| `scripts/generar_clases.py --check` | que ningún README de clase o parte esté desincronizado respecto de su manifiesto, y que no queden carpetas huérfanas |
| `scripts/validar_estructura.py` | coherencia de manifiestos, existencia de las 336 clases, las 14 secciones obligatorias por clase, las 5 de cada parte, todos los enlaces relativos y que las fuentes sean https |
| `scripts/validar_encoding.py` | UTF-8 sin BOM y sin mojibake, por round-trip cp1252 en vez de lista de secuencias |
| `scripts/generar_sitio.py --check` | que las 421 páginas del sitio compilen |
| `markdownlint-cli2` | Markdown estructuralmente válido en todo el repositorio |
| `python -m unittest discover -s tests` | pruebas estructurales del currículo y los manifiestos |
| `gitleaks` | ausencia de secretos en el árbol de archivos |
| `bandit` | análisis estático de los scripts de Python |

## Cómo reproducir las cifras

```bash
# Partes y clases
ls -d curriculum/part-* | wc -l
find curriculum -mindepth 3 -name README.md | wc -l

# Palabras del currículo
find curriculum -mindepth 3 -name README.md -exec cat {} + | wc -w

# Manuales, casos, plantillas y fuentes
ls docs/*.md | wc -l
ls case-studies/*.md | wc -l
ls templates/* | wc -l
python -c "import json;print(len(json.load(open('manifests/official_sources.json',encoding='utf-8'))))"

# Páginas del sitio
python scripts/generar_sitio.py && find site -name '*.html' | wc -l
```

## Lo que estos controles no garantizan

El CI verifica estructura, sincronía, codificación y enlaces. **No verifica exactitud jurídica ni
vigencia normativa**: eso exige revisión humana contra la fuente oficial. Las partes marcadas como
`DINAMICO` cambian por definición, y el resto envejece con cada reforma.

Última revisión manual de la base normativa: **2026-08-07**.
