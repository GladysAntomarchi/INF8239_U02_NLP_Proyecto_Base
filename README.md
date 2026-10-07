# INF-8239 · Unidad 02 · Proyecto NLP

**Estudiante:** Gladys [Apellido]  
**Profesor:** Edwin Ramón José Nolasco  
**Asignatura:** Ciencia de Datos II (INF-8239)

Proyecto correspondiente a LAB04 y LAB05 de la Unidad 02. El objetivo es desarrollar un flujo reproducible de Procesamiento de Lenguaje Natural (NLP), desde la selección y auditoría de un corpus público hasta el entrenamiento, evaluación e implementación de un clasificador de texto.

## Dataset y auditoría

Se seleccionó el dataset **Inflation Research Abstracts Classification**, disponible en el UCI Machine Learning Repository:

https://archive.ics.uci.edu/dataset/1125/inflation+research+abstracts+classification

El corpus contiene **1,138 abstracts académicos en inglés** relacionados con inflación. La variable textual es `Abstract` y la variable objetivo es `Label`.

La pregunta de clasificación es:

> ¿Es posible clasificar, a partir del contenido de un abstract científico relacionado con inflación, si el artículo está asociado o no con metodologías de machine learning o inteligencia artificial?

La auditoría inicial identificó 0 valores nulos en `Abstract` y `Label`, 13 abstracts duplicados y un desbalance de clases: **79.09 % para la clase 0 y 20.91 % para la clase 1**.

Los textos duplicados se eliminan antes de realizar la partición entrenamiento/prueba para reducir el riesgo de fuga de información.

El archivo original utilizado es:

```text
data/raw/classified_abstracts.json

Los datos originales no se incluyen en Git.
Para preparar el datase
uv run python scripts/prepare_data.py

Para ejecutar la auditoría:
uv run python scripts/audit_data.py

La versión procesada se genera en:
data/processed/dataset.csv

Modelado y resultados
En LAB05 se compararon tres pipelines de clasificación utilizando TF-IDF dentro de cada pipeline:
Modelo	F1 macro	Accuracy
DummyClassifier	0.442	0.79
Complement Naive Bayes	0.459	0.79
Logistic Regression	0.837	0.89


La regresión logística presentó el mejor comportamiento y fue seleccionada como modelo final.
Para la clase 1 obtuvo:
- Precision: 0.75
- Recall: 0.73
- F1: 0.74
La matriz de confusión registró:
- 209 verdaderos negativos
- 14 falsos positivos
- 16 falsos negativos
- 43 verdaderos positivos
En total, el modelo clasificó correctamente 252 de 282 observaciones del conjunto de prueba.
Para entrenar nuevamente los modelos:

uv run python scripts/train_text.py

Los principales resultados se encuentran en:
reports/text_metrics.csv
reports/confusion_text.png
reports/error_analysis.csv
models/text_model.joblib

Análisis de errores
Se revisaron manualmente 20 errores de clasificación.
Categoría	Cantidad
Etiqueta discutible	6
Terminología técnica ambigua	5
Predicción estadística confundida con ML	4
ML explícito pero minoritario	2
ML poco explícito	1
ML diluido en texto largo	1
Texto insuficiente	1


Los tres tipos de error más frecuentes representan 15 de los 20 casos analizados.
La principal dificultad observada se relaciona con la similitud léxica entre textos de econometría, estadística predictiva, forecasting y machine learning. Términos como prediction, forecast, regression, Bayesian y model pueden aparecer en ambas clases.
El análisis completo está disponible en:
reports/error_analysis_summary.md
reports/error_analysis_categorized.csv

Ejecución y reproducibilidad
El proyecto utiliza Python 3.12 y uv.
Para reproducir el entorno:
uv python install 3.12
uv sync

Copiar .env.example como .env y utilizar:
DATA_SOURCE=local
DATASET_PATH=data/processed/dataset.csv
DATASET_URL=
TEXT_COLUMN=Abstract
TARGET_COLUMN=Label
RANDOM_STATE=42

Para ejecutar las pruebas:
uv run pytest -q

Resultado de la última ejecución:
6 passed

Para ejecutar la aplicación Streamlit:
uv run streamlit run app/streamlit_app.py

El proyecto también incluye requirements-cloud.txt para facilitar su ejecución en entornos compatibles con pip.
Estructura principal
INF8239_U02_NLP_Proyecto_Base/
├── app/
├── data/
├── docs/
├── models/
├── reports/
├── scripts/
├── src/
├── tests/
├── .env.example
├── pyproject.toml
├── README.md
├── requirements-cloud.txt
└── uv.lock

La documentación principal se encuentra en:
docs/DATASET_CARD.md
docs/dataset_candidates.csv
reports/lab05_conclusion.md
reports/ejercicio03_conclusion.md

Limitaciones y uso responsable
El corpus está formado por abstracts académicos en inglés relacionados con inflación y presenta desbalance entre las clases. Además, TF-IDF se basa principalmente en asociaciones léxicas y no comprende completamente la diferencia conceptual entre estadística tradicional, econometría y machine learning.
Por esta razón, el modelo no debe generalizarse automáticamente a otros idiomas, dominios o tipos de documentos sin validación adicional.
La aplicación constituye una demostración académica. Sus predicciones deben interpretarse dentro del dominio y las limitaciones documentadas del dataset.

Esta versión me gusta **mucho más para tu entrega**. Tiene toda la información importante, pero no da la sensación de que cada dos líneas comienza una sección nueva.

Y sí: la parte que mostraste de **“Matriz de confusión” → bloque con la ruta → “Análisis de errores”** se siente excesivamente


