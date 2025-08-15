# Paso 1: Importar librerías
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Paso 2: Cargar dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Características:", iris.feature_names)
print("Clases:", iris.target_names)

# Paso 3: Graficar dos características
plt.figure(figsize=(6, 4))
for i, color in zip(range(3), ['red', 'green', 'blue']):
    plt.scatter(
        X[y == i, 0],  # longitud del sépalo
        X[y == i, 1],  # ancho del sépalo
        label=iris.target_names[i],
        color=color
    )

plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title("Flores Iris: Sepalo longitud vs ancho")
plt.legend()
plt.show()

# Paso 4: Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 5: Crear modelo y entrenar
modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_train, y_train)

# Paso 6: Evaluar modelo
precision = modelo.score(X_test, y_test)
print(f"Precisión del modelo: {precision:.2f}")

# Paso 7: Predecir una flor nueva
nueva_flor = [[5.1, 3.5, 1.4, 0.2]]
prediccion = modelo.predict(nueva_flor)
print("Predicción para la nueva flor:", iris.target_names[prediccion][0])
