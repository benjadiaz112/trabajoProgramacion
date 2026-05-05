import pandas as pd
from sklearn.datasets import load_wine

def preparar_datos():
    # a. Cargar el dataset load_wine
    wine = load_wine()

    # b. Transformarlo a dataframe
    # Creamos el DF con las características (features)
    df = pd.DataFrame(wine.data, columns=wine.feature_names)
    
    # Agregamos la columna objetivo (target)
    df['target'] = wine.target

    # c. Realizar un análisis exploratorio
    print("--- ANÁLISIS EXPLORATORIO ---")
    
    # i. Primeros registros
    print("\ni. Primeros 5 registros:")
    print(df.head())

    # ii. Nombres de variables
    print("\nii. Nombres de las variables (Features):")
    print(wine.feature_names)

    # iii. Clases
    print("\niii. Clases de vino:")
    print(wine.target_names)

    # iv. Cantidad de datos
    print("\niv. Cantidad de datos (filas, columnas):")
    print(df.shape)

    # v. Estadísticas
    print("\nv. Estadísticas principales:")
    print(df.describe())

    # d. Separar variables independientes (X) y variable objetivo (y)
    X = df.drop('target', axis=1) # Todas las columnas menos 'target'
    y = df['target']              # Solo la columna 'target'

    return X, y, wine.feature_names, wine.target_names

# Esto permite probar el archivo solo si lo ejecutas directamente
if __name__ == "__main__":
    preparar_datos()