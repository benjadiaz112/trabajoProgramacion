# Informe de Análisis: Clasificación de Vinos

## a. ¿Qué accuracy obtuvo el modelo?
El modelo obtuvo una exactitud (**Accuracy**) de **0.97 (97%)**.
Esto significa que de cada 100 vinos en el conjunto de prueba, el modelo clasificó correctamente a 97 de ellos. Es un rendimiento excelente para un modelo de clasificación multiclase.

## b. ¿Qué variable aparece en la raíz del árbol?
La variable que aparece en la raíz (el nodo superior) es **`flavanoids`**.
* **Interpretación:** El algoritmo determinó que el nivel de flavonoides es el indicador químico más importante para realizar la primera división de los datos y separar las clases de vino con mayor eficiencia.



## c. El modelo, ¿parece confiable? Justifique.
**Sí, el modelo es altamente confiable.**
* **Justificación:** No solo presenta un Accuracy elevado, sino que al observar el `classification_report`, las métricas de *Precision* y *Recall* para las tres clases (class_0, class_1, class_2) son balanceadas y superiores al 0.90. Esto indica que el modelo no tiene "puntos ciegos" con ninguna de las categorías de vino.

## d. ¿Se observa overfitting o underfitting?
El modelo se encuentra en un punto de equilibrio óptimo, aunque con una ligera tendencia al **overfitting** controlado:
* **No hay Underfitting:** Ya que el modelo fue capaz de capturar la complejidad del dataset y obtener una puntuación alta.
* **Control de Overfitting:** Al haber limitado la profundidad del árbol con `max_depth=4`, evitamos que el modelo se memorice cada dato específico. El hecho de que el Accuracy en el set de **prueba** (datos nuevos) sea tan alto, confirma que el modelo generaliza bien.




## e. ¿Qué otras variables parecen más relevantes?
Basado en los primeros niveles del árbol de decisión, las variables más influyentes después de la raíz son:
1.  **`color_intensity`**: Es la variable principal para distinguir entre los vinos de la clase 1 y clase 2.
2.  **`proline`**: Un aminoácido que aparece como un fuerte discriminador en los niveles secundarios del árbol.
3.  **`od280/od315_of_diluted_wines`**: Aparece frecuentemente para purificar los nodos finales (hojas).