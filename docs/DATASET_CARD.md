# Dataset Card

## Identificación

- **Nombre:** Inflation Research Abstracts Classification
- **Fuente original:** UCI Machine Learning Repository
- **URL:** https://archive.ics.uci.edu/dataset/1125/inflation+research+abstracts+classification
- **Responsable:** Daniela Agostina Gonzalez
- **Institución:** Facultad de Ciencias Económicas, Universidad Nacional de Córdoba
- **Versión o fecha:** Dataset donado/publicado en 2025
- **Licencia:** CC BY 4.0
- **Idioma:** Inglés
- **Número de registros:** 1,138
- **Formato original:** JSON

## Propósito y variable objetivo

El dataset contiene abstracts de investigaciones relacionadas con inflación.

El propósito del laboratorio es utilizar el texto de los abstracts para una tarea de clasificación binaria.

- **Característica textual principal:** `Abstract`
- **Variable objetivo:** `Label`

Las categorías de `Label` son:

- `0`: artículo no clasificado como relacionado con metodologías de machine learning o inteligencia artificial.
- `1`: artículo clasificado como relacionado con metodologías de machine learning o inteligencia artificial.

El uso previsto es académico y se limita al desarrollo de técnicas de procesamiento de lenguaje natural, clasificación de texto y análisis de embeddings.

## Diccionario de datos

| Columna | Tipo | Descripción | Valores o unidad |
|---|---|---|---|
| DOI | Texto / identificador | Identificador digital del artículo científico. | DOI del artículo; puede presentar valores faltantes. |
| Abstract | Texto | Resumen del artículo científico relacionado con inflación. | Texto libre en inglés. |
| Label | Categórica binaria | Clase asignada al artículo según su relación con ML/IA. | `0` = No; `1` = Sí |

## Procedimiento de obtención

El dataset fue localizado en el UCI Machine Learning Repository y descargado desde su fuente oficial.

El archivo original se conserva sin modificaciones en:

`data/raw/classified_abstracts.json`

Para adaptarlo a la arquitectura del proyecto se creó:

`scripts/prepare_data.py`

Este script lee el archivo JSON original y genera:

`data/processed/dataset.csv`

La transformación conserva las columnas `DOI`, `Abstract` y `Label`.

La configuración del proyecto se realiza mediante el archivo `.env` utilizando rutas relativas.

## Calidad observada

- 1,138 textos.
- 13 abstracts duplicados.
- Clase `0`: 79.09 % (aprox. 900 registros).
- Clase `1`: 20.91 % (aprox. 238 registros).
- Mediana de longitud: 1,021 caracteres.
- Percentil 90: 1,709.9 caracteres.
- Percentil 99: 3,352.3 caracteres.
- Longitud máxima: 14,076 caracteres.

## Interpretación de la auditoría

**Observación:** existe desbalance entre las clases y se identificaron 13 textos duplicados.

**Evidencia:** la auditoría reporta aproximadamente 79 % para `Label=0` y 21 % para `Label=1`, además de 13 duplicados.

**Interpretación:** si posteriormente se evaluara únicamente con `accuracy`, el desempeño podría verse favorecido por la clase mayoritaria. Los duplicados también podrían provocar fuga de información si aparecen tanto en entrenamiento como en prueba.

**Decisión:** conservar el archivo original intacto, documentar ambos riesgos y eliminar duplicados antes del modelado.

## Cinco ejemplos anonimizados

1. Abstract sobre pronóstico de inflación mediante redes neuronales recurrentes. Etiqueta: `1`.
2. Abstract sobre modelos tradicionales de predicción de inflación. Etiqueta: `0`.
3. Abstract que utiliza técnicas ensemble para analizar inflación. Etiqueta: `1`.
4. Abstract sobre expectativas de inflación y política monetaria sin uso explícito de ML/IA. Etiqueta: `0`.
5. Abstract relacionado con redes neuronales para pronóstico económico. Etiqueta: `1`.

## Población cubierta y excluida

El dataset cubre artículos científicos relacionados con inflación dentro del conjunto recopilado por sus autores.

No representa necesariamente:

- toda la literatura científica sobre inflación;
- investigaciones posteriores al periodo de recopilación;
- documentos escritos en otros idiomas;
- noticias, publicaciones en redes sociales o documentos empresariales;
- documentos no académicos;
- otros dominios fuera del estudio económico de la inflación.

## Riesgos, sesgos y usos prohibidos

### Riesgos y sesgos previsibles

- Desbalance entre las clases.
- Posible sesgo de selección derivado de las fuentes utilizadas para recopilar los artículos.
- Simplificación del problema mediante una etiqueta binaria.
- Presencia de abstracts duplicados.
- Posible pérdida de representatividad frente a literatura no incluida en el corpus.
- Limitación al idioma inglés.

### Usos prohibidos o fuera de alcance

Este dataset y los modelos derivados no deben utilizarse para:

- evaluar automáticamente la calidad científica de un artículo;
- evaluar investigadores o instituciones;
- sustituir revisiones bibliográficas humanas;
- inferir causalidad;
- aplicar el modelo directamente a otros dominios sin validación;
- tomar decisiones automáticas de alto impacto.