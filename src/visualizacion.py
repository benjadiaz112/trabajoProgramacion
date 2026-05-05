import matplotlib.pyplot as plt
from sklearn import tree

def graficar_arbol(modelo, nombres_columnas, nombres_clases):
    # a. Graficar el árbol de decisión
    # b. Estilizar el gráfico creado
    plt.figure(figsize=(20, 10)) # Definimos el tamaño de la imagen
    
    tree.plot_tree(
        modelo, 
        feature_names=nombres_columnas, # Nombre de los químicos (Alcohol, etc)
        class_names=nombres_clases,    # Nombre de los vinos (class_0, etc)
        filled=True,                   # Colorea los cuadros según la clase
        rounded=True,                  # Bordes redondeados para que se vea mejor
        fontsize=12                    # Tamaño de letra legible
    )

    # Añadimos un título
    plt.title("Árbol de Decisión - Clasificación de Vinos (Dataset: load_wine)")
    
    # Guardamos el gráfico para que lo puedas poner en tu informe
    plt.savefig("docs/arbol_vinos.png")
    print("\n--- VISUALIZACIÓN ---")
    print("El gráfico ha sido guardado en 'docs/arbol_vinos.png'. Ábrelo para verlo.")
    
    plt.show()  