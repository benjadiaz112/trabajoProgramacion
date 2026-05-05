import matplotlib.pyplot as plt
from sklearn import tree

def graficar_arbol(modelo, nombres_columnas, nombres_clases):

    plt.figure(figsize=(20, 10))
    
    tree.plot_tree(
        modelo, 
        feature_names=nombres_columnas, 
        class_names=nombres_clases,   
        filled=True,                 
        rounded=True,                
        fontsize=12                
    )

    # Añadimos un título
    plt.title("Árbol de Decisión - Clasificación de Vinos (Dataset: load_wine)")
    
    
    plt.savefig("docs/arbol_vinos.png")
    print("\n--- VISUALIZACIÓN ---")
    print("El gráfico ha sido guardado en 'docs/arbol_vinos.png'. Ábrelo para verlo.")
    
    plt.show()  