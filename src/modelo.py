from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def entrenar_modelo(X, y):

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    modelo = DecisionTreeClassifier(max_depth=4, random_state=42)

    # c. Entrenar el modelo con los datos de entrenamiento
    modelo.fit(X_train, y_train)


    return modelo, X_train, X_test, y_train, y_test