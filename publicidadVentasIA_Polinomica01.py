import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Datos reales simulados
publicidad = np.array([100, 200, 300, 400, 500, 600]).reshape(-1, 1)
ventas = np.array([1200, 2100, 2700, 3100, 3300, 3400])

# Transformar a polinomio grado 2
poly = PolynomialFeatures(degree=2)
publicidad_poly = poly.fit_transform(publicidad)

# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(publicidad_poly, ventas)

# Predicción
x_pred = np.linspace(100, 600, 100).reshape(-1, 1)
y_pred = modelo.predict(poly.transform(x_pred))

# Mostrar ecuación
a, b, c = modelo.coef_[2], modelo.coef_[1], modelo.intercept_
print(f"Ventas ≈ {a:.2f}*(Publicidad)^2 + {b:.2f}*(Publicidad) + {c:.2f}")

# Gráfico
plt.scatter(publicidad, ventas, color='blue', label='Datos reales')
plt.plot(x_pred, y_pred, color='red', label='Regresión polinómica')
plt.xlabel('Publicidad (USD)')
plt.ylabel('Ventas (USD)')
plt.title('Relación entre publicidad y ventas')
plt.legend()
plt.show()
