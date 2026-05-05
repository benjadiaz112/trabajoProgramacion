from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def entrenar_modelo(X, y):
    # a. Dividir los datos en entrenamiento y prueba (train_test_split)
    # Usamos 20% para test (test_size=0.2) y una semilla (random_state) para que siempre de igual
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # b. Crear un modelo de árbol de decisión
    # Le ponemos una profundidad máxima (max_depth) para que el gráfico sea legible
    modelo = DecisionTreeClassifier(max_depth=4, random_state=42)

    # c. Entrenar el modelo con los datos de entrenamiento
    modelo.fit(X_train, y_train)

    # Retornamos el modelo listo y los datos de prueba para evaluarlos después
    return modelo, X_train, X_test, y_train, y_test