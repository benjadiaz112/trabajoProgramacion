import pandas as pd
from sklearn.datasets import load_wine

def preparar_datos():
  
    wine = load_wine()

  

    df = pd.DataFrame(wine.data, columns=wine.feature_names)
    
    # Agregamos la columna objetivo (target)
    df['target'] = wine.target


    print("--- ANÁLISIS EXPLORATORIO ---")
    
  
    print("\ni. Primeros 5 registros:")
    print(df.head())

   
    print("\nii. Nombres de las variables (Features):")
    print(wine.feature_names)

    # iii. Clases
    print("\niii. Clases de vino:")
    print(wine.target_names)

   
    print("\niv. Cantidad de datos (filas, columnas):")
    print(df.shape)

    # v. Estadísticas
    print("\nv. Estadísticas principales:")
    print(df.describe())


    X = df.drop('target', axis=1) 
    y = df['target']              

    return X, y, wine.feature_names, wine.target_names


if __name__ == "__main__":
    preparar_datos()