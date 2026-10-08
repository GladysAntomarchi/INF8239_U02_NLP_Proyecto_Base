# INF-8239 · Unidad 02 · Proyecto NLP

**Estudiante:** Gladys Antomarchi 
**Profesor:** Edwin Ramón José Nolasco  
**Asignatura:** Ciencia de Datos II (INF-8239)

Proyecto correspondiente a LAB04 y LAB05 de la Unidad 02. El objetivo es desarrollar un flujo reproducible de Procesamiento de Lenguaje Natural (NLP), desde la selección y auditoría de un corpus público hasta el entrenamiento, evaluación, análisis de errores e implementación de un clasificador de texto.

---

## Dataset y auditoría

Se seleccionó el dataset **Inflation Research Abstracts Classification**, disponible en el UCI Machine Learning Repository:

https://archive.ics.uci.edu/dataset/1125/inflation+research+abstracts+classification

El corpus contiene **1,138 abstracts académicos en inglés** relacionados con inflación.

- **Variable textual:** `Abstract`
- **Variable objetivo:** `Label`
- **Licencia:** CC BY 4.0
- **Idioma:** Inglés

La pregunta de clasificación utilizada es:

> ¿Es posible clasificar, a partir del contenido de un abstract científico relacionado con inflación, si el artículo está asociado o no con metodologías de machine learning o inteligencia artificial?

La auditoría inicial identificó:

- 1,138 registros.
- 0 valores nulos en `Abstract`.
- 0 valores nulos en `Label`.
- 13 abstracts duplicados.
- Clase `0`: 79.09 %.
- Clase `1`: 20.91 %.
- Mediana de longitud: 1,021 caracteres.
- Percentil 90: 1,709.9 caracteres.
- Percentil 99: 3,352.3 caracteres.
- Longitud máxima: 14,076 caracteres.

El corpus presenta un desbalance importante entre las clases. Por esta razón, `accuracy` no se utiliza como única métrica para evaluar el desempeño de los modelos.

Los textos duplicados se eliminan antes de realizar la partición entrenamiento/prueba para reducir el riesgo de fuga de información.

El archivo original utilizado es:

```text
data/raw/classified_abstracts.json
```

Los datos originales no se incluyen en Git.

Para preparar la versión procesada del dataset:

```bash
uv run python scripts/prepare_data.py
```

La versión procesada se genera en:

```text
data/processed/dataset.csv
```

Para ejecutar la auditoría:

```bash
uv run python scripts/audit_data.py
```

---

## Modelado y resultados

En LAB05 se compararon tres pipelines de clasificación de texto utilizando TF-IDF dentro de cada pipeline:

1. `DummyClassifier` como baseline.
2. `ComplementNB`.
3. `LogisticRegression`.

Todos los modelos fueron evaluados sobre la misma partición estratificada.

| Modelo | F1 macro | Accuracy |
|---|---:|---:|
| DummyClassifier | 0.442 | 0.79 |
| Complement Naive Bayes | 0.459 | 0.79 |
| Logistic Regression | **0.837** | **0.89** |

La **regresión logística** presentó el comportamiento más equilibrado y fue seleccionada como modelo final.

El baseline obtuvo aproximadamente 79 % de `accuracy`, pero su `recall` para la clase `1` fue 0.00. Esto demuestra que `accuracy` aislada puede ser engañosa cuando existe desbalance entre las clases.

Complement Naive Bayes obtuvo un `recall` de 0.02 para la clase `1`.

La regresión logística obtuvo:

| Clase | Precision | Recall | F1 |
|---|---:|---:|---:|
| 0 | 0.93 | 0.94 | 0.93 |
| 1 | 0.75 | 0.73 | 0.74 |

Resultados globales:

- **F1 macro:** 0.837
- **Accuracy:** 0.89

La matriz de confusión registró:

- 209 verdaderos negativos.
- 14 falsos positivos.
- 16 falsos negativos.
- 43 verdaderos positivos.

En total, el modelo clasificó correctamente **252 de 282 observaciones** del conjunto de prueba.

Para entrenar nuevamente los modelos:

```bash
uv run python scripts/train_text.py
```

Los principales resultados se encuentran en:

```text
reports/text_metrics.csv
reports/confusion_text.png
reports/error_analysis.csv
models/text_model.joblib
```

---

## Análisis de errores

Se revisaron manualmente 20 errores producidos por la regresión logística.

| Categoría | Cantidad |
|---|---:|
| Etiqueta discutible | 6 |
| Terminología técnica ambigua | 5 |
| Predicción estadística confundida con ML | 4 |
| ML explícito pero minoritario | 2 |
| ML poco explícito | 1 |
| ML diluido en texto largo | 1 |
| Texto insuficiente | 1 |

Los tres tipos de error más frecuentes representan **15 de los 20 casos analizados**.

La principal dificultad observada se relaciona con la similitud léxica entre textos de:

- econometría;
- estadística predictiva;
- forecasting;
- machine learning.

Términos como `prediction`, `forecast`, `regression`, `Bayesian` y `model` pueden aparecer tanto en artículos etiquetados como clase `0` como en artículos etiquetados como clase `1`.

Esto evidencia una limitación de TF-IDF: representa asociaciones léxicas, pero no comprende completamente la diferencia conceptual entre estadística tradicional, econometría y machine learning.

El análisis completo está disponible en:

```text
reports/error_analysis_summary.md
reports/error_analysis_categorized.csv
```

---

## Aplicación Streamlit

Se implementó una aplicación Streamlit para reutilizar el modelo entrenado.

Para ejecutarla:

```bash
uv run streamlit run app/streamlit_app.py
```

La aplicación permite introducir un texto y obtener la clase predicha.

Ejemplo relacionado con ML/IA:

```text
This study uses machine learning and neural networks to forecast inflation.
```

Predicción obtenida:

```text
1
```

Ejemplo fuera del dominio:

```text
The weather is beautiful and I enjoy walking in the park.
```

Predicción obtenida:

```text
0
```

La aplicación muestra una advertencia indicando que la salida debe interpretarse dentro del dominio y de las limitaciones documentadas del dataset.

---

## Configuración del entorno

El proyecto utiliza:

- Python 3.12
- `uv`
- `uv.lock`
- rutas relativas
- archivo `.env`
- pruebas automatizadas con `pytest`

Para instalar Python 3.12:

```bash
uv python install 3.12
```

Para sincronizar las dependencias:

```bash
uv sync
```

Para verificar la versión de Python:

```bash
uv run python --version
```

Copiar:

```text
.env.example
```

como:

```text
.env
```

Configuración utilizada:

```text
DATA_SOURCE=local
DATASET_PATH=data/processed/dataset.csv
DATASET_URL=
TEXT_COLUMN=Abstract
TARGET_COLUMN=Label
RANDOM_STATE=42
```

El archivo `.env` no se incluye en Git.

---

## Pruebas automatizadas

Para ejecutar todas las pruebas:

```bash
uv run pytest -q
```

Resultado de la última ejecución:

```text
6 passed
```

Las pruebas verifican:

- contrato de datos;
- columnas requeridas;
- textos no vacíos;
- existencia de al menos dos clases;
- estructura de los pipelines;
- capacidad de los modelos para producir predicciones.

---

## Portabilidad y reproducibilidad

El proyecto utiliza rutas relativas y excluye del repositorio:

- `.env`
- `.venv`
- datos originales
- datos procesados locales

También se generó:

```text
requirements-cloud.txt
```

para facilitar la ejecución en entornos compatibles con `pip`.

La secuencia básica para reproducir el proyecto es:

```bash
uv python install 3.12
uv sync
uv run python scripts/prepare_data.py
uv run python scripts/audit_data.py
uv run pytest -q
uv run python scripts/train_text.py
uv run streamlit run app/streamlit_app.py
```

---

## Estructura del proyecto

```text
INF8239_U02_NLP_Proyecto_Base/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
│
├── docs/
│   ├── DATASET_CARD.md
│   └── dataset_candidates.csv
│
├── models/
│   └── text_model.joblib
│
├── reports/
│   ├── confusion_text.png
│   ├── text_metrics.csv
│   ├── error_analysis.csv
│   ├── error_analysis_categorized.csv
│   ├── error_analysis_summary.md
│   ├── lab05_conclusion.md
│   └── ejercicio03_conclusion.md
│
├── scripts/
│   ├── prepare_data.py
│   ├── audit_data.py
│   ├── download_data.py
│   ├── train_text.py
│   └── categorize_errors.py
│
├── src/
│   └── inf8239_u02/
│
├── tests/
│   ├── test_data_contract.py
│   └── test_text_model.py
│
├── .env.example
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
├── requirements-cloud.txt
├── requirements-colab.txt
└── uv.lock
```

---

## Documentación principal

La documentación del proyecto incluye:

```text
docs/DATASET_CARD.md
docs/dataset_candidates.csv
reports/lab05_conclusion.md
reports/ejercicio03_conclusion.md
```

---

## Limitaciones

El corpus está compuesto por abstracts académicos en inglés relacionados con inflación.

Las principales limitaciones identificadas son:

- desbalance entre clases;
- presencia inicial de textos duplicados;
- dificultad para diferenciar conceptualmente entre estadística predictiva, econometría y machine learning;
- dependencia de asociaciones léxicas propias de TF-IDF;
- dominio temático específico;
- idioma inglés.

Por estas razones, el modelo no debe generalizarse automáticamente a otros idiomas, dominios o tipos de documentos sin realizar una validación adicional.

---

## Uso responsable

Este proyecto corresponde a una demostración académica.

Las predicciones del modelo no constituyen decisiones automáticas y deben interpretarse dentro del dominio y de las limitaciones documentadas.

---

## Estado del proyecto

- LAB04: selección, preparación y auditoría del corpus — completado.
- LAB05: clasificación, evaluación, análisis de errores y aplicación — completado.
- Pruebas automatizadas: 6 aprobadas.
- Modelo seleccionado: Logistic Regression con TF-IDF.
- F1 macro obtenido: 0.837.

## LAB06 · Embeddings y análisis responsable de redes

En LAB06 se entrenó un modelo Word2Vec sobre el corpus textual del proyecto y se realizó un análisis estructural de una red de demostración utilizando centralidades, comunidades y modularidad.

### Embeddings con Word2Vec

Para entrenar los embeddings:

```bash
uv run python scripts/embeddings_network.py --word inflation
```

Resultado base con `window=5`:

- Vocabulario: 10,159 términos.
- Cobertura: 1.0.
- Palabra analizada: `inflation`.

Entre los vecinos obtenidos aparecieron términos como:

- `observed`
- `unemployment`
- `interest`
- `level`
- `exchange`
- `aggregate`

La similitud entre palabras se interpreta como proximidad de contexto dentro de este corpus y no como sinonimia universal.

### Experimento con el parámetro `window`

Se comparó el valor original `window=5` con `window=10`.

Con `window=10`:

- el vocabulario se mantuvo en 10,159 términos;
- la cobertura permaneció en 1.0;
- cambiaron los vecinos semánticos de `inflation`.

Entre los vecinos obtenidos con `window=10` aparecieron términos como:

- `unemployment`
- `level`
- `growth`
- `aggregate`
- `gap`
- `observed`

El cambio de `window` no modificó la cobertura ni el tamaño del vocabulario, pero sí cambió el tipo de contexto capturado. Una ventana mayor incorpora relaciones más amplias dentro del texto y puede reflejar asociaciones temáticas más generales.

### Red de demostración

Para ejecutar los embeddings junto con el análisis de red:

```bash
uv run python scripts/embeddings_network.py --word inflation --network-demo
```

La red de demostración produjo:

- 34 nodos.
- 78 aristas.
- 3 comunidades detectadas.
- Modularidad: 0.411.

Los artefactos generados son:

```text
reports/centralities.csv
reports/network.png
reports/social_network.graphml
models/word2vec.model
```

### Centralidades

Los resultados mostraron que:

- el nodo `33` obtuvo la mayor centralidad de grado: `0.5152`;
- el nodo `33` obtuvo el mayor PageRank: `0.0970`;
- el nodo `0` obtuvo la mayor centralidad de intermediación o betweenness: `0.4376`.

Estas métricas describen propiedades estructurales distintas.

Una centralidad de grado alta indica mayor cantidad relativa de conexiones directas. Una betweenness alta indica mayor participación en caminos mínimos entre nodos. Un PageRank alto indica conexión con nodos que también tienen relevancia estructural.

### Interpretación responsable

Es válido afirmar que ciertos nodos presentan mayor conectividad, intermediación o relevancia estructural según una métrica específica.

No es válido afirmar únicamente a partir de estas métricas que un nodo sea “la persona más influyente”, líder real o causa del comportamiento de la red.

De igual forma, las comunidades detectadas representan agrupaciones estructurales según el algoritmo y no identidades sociales definitivas.

### Evidencia y documentación

La interpretación completa de LAB06 se encuentra en:

```text
reports/lab06_embeddings_network.md
```

Las pruebas automatizadas se ejecutaron con:

```bash
uv run pytest tests/test_embeddings_network.py -q
```

Resultado:

```text
2 passed
```
