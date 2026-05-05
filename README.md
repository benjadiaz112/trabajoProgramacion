Clasificación de Vinos - Machine Learning 🍷 Este proyecto consiste en el desarrollo de un modelo de Machine Learning (Árbol de Decisión) para clasificar diferentes tipos de vinos según sus componentes químicos, realizado para el Encargo 2 de la carrera de Informática en Duoc UC.

🚀 Estrategia de Ramificación (GitHub Flow) En este encargo, hemos implementado GitHub Flow para gestionar el código de manera profesional:

main: Contiene la versión estable y funcional del proyecto.

features/: Ramas dedicadas a nuevas funcionalidades.

Rama actual de trabajo: features/arbol-decision-benjamin.

Nota: No trabajamos directamente en la raíz (main) para proteger la integridad del código base y permitir revisiones antes de la integración final.

📊 Sobre el Modelo El modelo utiliza un DecisionTreeClassifier con las siguientes características técnicas:

Profundidad Máxima (max_depth=4): Configurada para mantener un equilibrio entre precisión y legibilidad, evitando el overfitting (sobreajuste).

Criterio de Evaluación: Se utiliza el Accuracy (Exactitud) medido sobre un conjunto de test del 20%.

Dataset: Basado en el dataset clásico de vinos (178 muestras y 13 características químicas).

🛠️ Tecnologías Utilizadas Lenguaje: Python

Librerías: scikit-learn, pandas, matplotlib

Control de Versiones: Git & GitHub

Metodología: GitHub Flow.