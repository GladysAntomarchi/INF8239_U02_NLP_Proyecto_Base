# LAB06 · Embeddings y análisis responsable de redes

## Experimento con Word2Vec

### Comparación del parámetro `window`

**Hipótesis.** Al aumentar `window` de 5 a 10, Word2Vec consideraría un contexto más amplio alrededor de cada palabra, por lo que se esperaba obtener vecinos con relaciones más temáticas o de dominio.

**Resultado.** El tamaño del vocabulario se mantuvo en 10,159 palabras y la cobertura permaneció en 1.0. Sin embargo, los vecinos de `inflation` cambiaron. Con `window=5` aparecieron términos como `interest`, `exchange` y `observed`, mientras que con `window=10` surgieron términos como `growth`, `gap` y `aggregate`.

**Interpretación.** El cambio de `window` no afectó la cobertura ni el tamaño del vocabulario, pero sí modificó el tipo de contexto capturado. Una ventana mayor incorpora relaciones más amplias dentro del contexto, por lo que puede reflejar asociaciones temáticas más generales.

**Decisión.** Se documenta el experimento con `window=10`, aunque el valor original `window=5` se conserva como referencia base. La similitud entre palabras se interpreta como proximidad de contexto dentro de este corpus, no como sinonimia universal.