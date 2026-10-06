# Cierre interpretativo LAB05

**Resultado principal:**  
Se entrenaron y compararon tres pipelines de clasificación de texto utilizando la misma partición estratificada: DummyClassifier como baseline, Complement Naive Bayes y regresión logística, todos con TF-IDF integrado dentro del pipeline para prevenir fuga de información.

**Modelo seleccionado y evidencia:**  
La regresión logística fue seleccionada al obtener un F1 macro de 0.837, frente a 0.442 del DummyClassifier y 0.459 de Complement Naive Bayes. También alcanzó accuracy de 0.89 y un comportamiento más equilibrado entre ambas clases.

**Clase con mayor dificultad:**  
La clase `1` presentó mayor dificultad. Su recall fue 0.73 y su F1 fue 0.74. La matriz de confusión registró 16 falsos negativos, frente a 14 falsos positivos.

**Tipo de error más frecuente:**  
El análisis manual de 20 errores mostró que las categorías más frecuentes fueron etiqueta discutible, terminología técnica ambigua y predicción estadística confundida con machine learning.

**Impacto en el contexto:**  
La principal dificultad surge porque artículos de econometría, estadística predictiva y machine learning comparten vocabulario como *prediction*, *forecast*, *regression*, *Bayesian* y *model*. TF-IDF identifica asociaciones léxicas, pero no comprende plenamente la frontera conceptual entre estas metodologías.

**Limitación del dataset:**  
El corpus presenta desbalance de clases, abstracts duplicados y se limita a literatura académica en inglés relacionada con inflación. Por ello, los resultados no deben generalizarse automáticamente a otros dominios.

**Decisión antes del despliegue:**  
Se conserva la regresión logística como modelo seleccionado, pero cualquier publicación o uso posterior debe mantener las advertencias de dominio, documentar los errores observados y realizar validaciones adicionales antes de aplicar el modelo fuera de este contexto.