# Paso 1: Importar librerías
from sklearn.utils.fixes import np_base_version
print("Importar librerías v2...")


import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Paso 2: Crear un dataset ficticio
# Características: [metros2, habitaciones, antigüedad]
print("Carga de dataset con datos de casas...")
X = np.array([
    [50, 1, 10],
    [80, 2, 5],
    [120, 3, 20],
    [60, 2, 15],
    [100, 3, 8],
    [85, 2, 12],
    [45, 1, 30],
    [70, 2, 18],
    [110, 3, 7],
    [95, 3, 25],
    [50, 1, 10],
    [80, 2, 5],
    [120, 3, 20],
    [60, 2, 15],
    [100, 3, 8],
    [85, 2, 12],
    [45, 1, 30],
    [70, 2, 18],
    [110, 3, 7],
    [95, 3, 25]

])

# Precio en miles de dólares (Y)
y = np.array([70, 120, 200, 90, 180, 130, 55, 100, 190, 150, 70, 120, 200, 90, 180, 130, 55, 100, 190, 150])

# Paso 3: Dividir datos en entrenamiento y prueba
print("Dividir datos en entrenamiento y prueba...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Paso 4: Crear y entrenar el modelo
print("Crear y entrenar el modelo...")
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Paso 5: Evaluar modelo
print("Cálculo de precisión...")
precision = modelo.score(X_test, y_test)
print(f"     Precisión del modelo: {precision:.2f}")


# Paso 6: Predecir el precio de una casa nueva
# Ejemplo: casa de 90 m2, 2 habitaciones, 10 años
print("Predecir precio...")
nueva_casa = np.array([[90, 2, 10]])
prediccion = modelo.predict(nueva_casa)
print(f"     Precio estimado: {prediccion[0]:.2f} mil dólares")



