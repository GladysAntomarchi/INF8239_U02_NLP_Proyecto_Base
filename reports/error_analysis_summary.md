# Análisis de errores del clasificador de texto

Se analizaron manualmente 20 errores producidos por el modelo de regresión logística.

## Distribución de categorías

| Categoría | Cantidad |
|---|---:|
| Etiqueta discutible | 6 |
| Terminología técnica ambigua | 5 |
| Predicción estadística confundida con ML | 4 |
| ML explícito pero minoritario | 2 |
| ML poco explícito | 1 |
| ML diluido en texto largo | 1 |
| Texto insuficiente | 1 |

## Interpretación

**Observación:** las categorías más frecuentes fueron `etiqueta discutible`, `terminología técnica ambigua` y `predicción estadística confundida con ML`.

**Evidencia:** 15 de los 20 errores revisados pertenecen a esas tres categorías.

**Interpretación:** la principal dificultad del clasificador no parece relacionarse con negación o ironía, sino con la similitud del vocabulario utilizado en investigaciones econométricas, estadísticas y de machine learning. Expresiones como *prediction*, *forecast*, *regression*, *Bayesian* o *model* aparecen en ambos tipos de artículos y pueden inducir al modelo TF-IDF a confundirlos.

También se observaron casos en los que una técnica de ML aparece explícitamente, pero ocupa una parte pequeña dentro de un abstract dominado por vocabulario económico. Asimismo, algunos registros presentan una frontera conceptual discutible entre métodos estadísticos tradicionales y técnicas de ML/IA.

**Decisión:** conservar la regresión logística como modelo seleccionado por su desempeño global, pero documentar esta limitación. Un experimento posterior podría evaluar representaciones o características que distingan mejor técnicas econométricas tradicionales de métodos explícitos de ML/IA.