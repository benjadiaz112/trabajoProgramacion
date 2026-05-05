# Importamos las funciones de tus otros archivos
from carga_data import preparar_datos
from modelo import entrenar_modelo
from evaluacion import evaluar_modelo
from visualizacion import graficar_arbol

def iniciar_sistema():
    print("==========================================")
    print(" INICIANDO FLUJO DE MACHINE LEARNING ")
    print("==========================================\n")


    X, y, nombres_columnas, nombres_clases = preparar_datos()


    modelo, X_train, X_test, y_train, y_test = entrenar_modelo(X, y)
    print("\n[OK] Modelo entrenado exitosamente.")

    evaluar_modelo(modelo, X_test, y_test)


    graficar_arbol(modelo, nombres_columnas, nombres_clases)
    
    print("\n==========================================")
    print(" PROCESO FINALIZADO CON ÉXITO ")
    print("==========================================")


if __name__ == "__main__":
    iniciar_sistema()