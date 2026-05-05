# Importamos las funciones de tus otros archivos
from carga_data import preparar_datos
from modelo import entrenar_modelo
from evaluacion import evaluar_modelo
from visualizacion import graficar_arbol

def iniciar_sistema():
    print("==========================================")
    print(" INICIANDO FLUJO DE MACHINE LEARNING ")
    print("==========================================\n")

    # 1. Preparación de datos (obtenemos X, y y los nombres)
    X, y, nombres_columnas, nombres_clases = preparar_datos()

    # 2. Entrenamiento (obtenemos el modelo y los sets divididos)
    modelo, X_train, X_test, y_train, y_test = entrenar_modelo(X, y)
    print("\n[OK] Modelo entrenado exitosamente.")

    # 3. Evaluación (calculamos métricas y accuracy)
    evaluar_modelo(modelo, X_test, y_test)

    # 4. Visualización (generamos el gráfico del árbol)
    graficar_arbol(modelo, nombres_columnas, nombres_clases)
    
    print("\n==========================================")
    print(" PROCESO FINALIZADO CON ÉXITO ")
    print("==========================================")

# Punto de entrada del programa
if __name__ == "__main__":
    iniciar_sistema()