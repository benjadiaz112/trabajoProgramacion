from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def evaluar_modelo(modelo, X_test, y_test):
    # a. Realizar predicciones sobre el conjunto de prueba
    # Le pasamos los datos que el modelo nunca vio (X_test)
    y_pred = modelo.predict(X_test)

    # b. Calcular el accuracy del modelo
    accuracy = accuracy_score(y_test, y_pred)

    # c. Analizar el desempeño obtenido
    print("--- EVALUACIÓN DEL MODELO ---")
    print(f"\nAccuracy (Exactitud): {accuracy:.2f}")
    
    print("\nReporte Detallado:")
    # Esto nos da Precision, Recall y F1-Score por cada tipo de vino
    print(classification_report(y_test, y_pred))

    print("\nMatriz de Confusión:")
    # Nos muestra dónde se confundió exactamente (ej: confundió vino tipo 1 con tipo 2)
    print(confusion_matrix(y_test, y_pred))

    return accuracy