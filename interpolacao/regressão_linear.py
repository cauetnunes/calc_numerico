import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Inserir seus dados
x_data = np.array([1872, 1890, 1900, 1920, 1940, 1950, 1970, 1960, 1980, 1991, 1996, 2000, 2005, 2014])
y_data = np.array([9.9, 14.3, 17.4, 30.6, 41.2, 51.9, 70.2, 93.1, 119.0, 146.2, 157.1, 169.8, 184.2, 202.7])

# Criar uma instância do modelo de regressão linear
model = LinearRegression()

# Transformar os dados para incluir termos polinomiais de grau 2 (função quadrática)
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x_data.reshape(-1, 1))

# Ajustar o modelo aos dados transformados
model.fit(x_poly, y_data)

# Coeficientes do modelo
a = model.coef_[0]
b = model.coef_[1]
c = model.intercept_

# Criar um gráfico de dispersão
plt.scatter(x_data, y_data, label='Dados')

# Gerar pontos da função quadrática ajustada
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = a * x_fit**2 + b * x_fit + c

# Plotar a função quadrática ajustada
plt.plot(x_fit, y_fit, 'r-', label='Ajuste Quadrático')

# Configurar o gráfico
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title(f'Função Quadrática Ajustada: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}')
plt.grid()

# Mostrar o gráfico
plt.show()
