from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def evaluar_modelo(modelo, X_test, y_test):


    y_pred = modelo.predict(X_test)


    accuracy = accuracy_score(y_test, y_pred)


    print("--- EVALUACIÓN DEL MODELO ---")
    print(f"\nAccuracy (Exactitud): {accuracy:.2f}")
    
    print("\nReporte Detallado:")
    
    print(classification_report(y_test, y_pred))

    print("\nMatriz de Confusión:")
 
    print(confusion_matrix(y_test, y_pred))

    return accuracy