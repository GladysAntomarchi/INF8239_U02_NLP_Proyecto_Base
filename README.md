# INF-8239 · Unidad 02 · Proyecto NLP

Profesor: Edwin Ramón José Nolasco
Estudiante: Gladys Antomarchi

Proyecto base para LAB04–LAB06. No sustituya la comprensión por ejecución mecánica.

## Inicio rápido

```bash
uv python install 3.12
uv sync
uv run pytest -q
uv run python scripts/audit_data.py
```

Copie `.env.example` como `.env` y configure el dataset aprobado.

## Dataset

### Dataset seleccionado

Para LAB04 se seleccionó **Inflation Research Abstracts Classification**, disponible públicamente en UCI Machine Learning Repository:

https://archive.ics.uci.edu/dataset/1125/inflation+research+abstracts+classification

El archivo original utilizado es:

`classified_abstracts.json`

El archivo original debe colocarse en:

`data/raw/classified_abstracts.json`

Los datos originales no se incluyen en Git.

### Preparación de los datos

Para generar la versión utilizada por el proyecto:

```bash
uv run python scripts/prepare_data.py
