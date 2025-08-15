# Machine Learning supervisado: regresión lineal para predecir precios de casas
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


# 1. Crear datos ficticios
np.random.seed(42)
tamano = np.random.randint(50, 200, 10)  # tamaño en m²
precio = tamano * 1.5 + np.random.randint(-20, 20, 10)  # precio en miles USD con algo de ruido

# 2. Crear DataFrame
df = pd.DataFrame({'Tamaño (m2)': tamano, 'Precio (miles USD)': precio})

# 3. Separar variables predictoras y objetivo
X = df[['Tamaño (m2)']]  # DataFrame
y = df[['Precio (miles USD)']]  # DataFrame para mantener consistencia

# 4. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Crear y entrenar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 6. Predecir en datos de prueba
y_pred = modelo.predict(X_test)

# 7. Calcular RMSE manualmente
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("RMSE indica que tan desviadas están las predicciones de la realidad")
print("     se calcula en la misma unidad que el precio (miles de dólares)")
print("RMSE (raíz cuadrada, del MSE error cuadrático medio ):", rmse)

# 8. Mostrar coeficientes del modelo
print("Coeficiente (pendiente):", modelo.coef_[0][0])
print("Intercepto:", modelo.intercept_[0])

# 9. Predicción de nueva casa usando DataFrame
nuevo_tamano = pd.DataFrame({'Tamaño (m2)': [120, 152]})
precio_estimado = modelo.predict(nuevo_tamano)
for i in range(len(nuevo_tamano)):
    tam = nuevo_tamano['Tamaño (m2)'].iloc[i]
    precio_nuevo = precio_estimado[i][0]
    print(f"Precio estimado para {tam} m2: {precio_nuevo:.2f} miles USD")
    
"""
print("-------------------------------")
print(tamano)
print(precio)
print(df)
print(X)
print(y)
print(nuevo_tamano)
print(precio_estimado)
"""

# Gráfico
X_rango = pd.DataFrame({'Tamaño (m2)': np.linspace(min(tamano), max(tamano), 100)})
y_rango = modelo.predict(X_rango)
plt.scatter(tamano, precio, color='blue', label='Datos reales')
plt.plot(X_rango, y_rango, color='red', label='Recta de regresión')
plt.xlabel('Tamaño (m2)')
plt.ylabel('Precio (miles USD)')
plt.title('Relación entre tamaño y precio')
plt.legend()
plt.show()
