import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Função quadrática para ajuste


def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c


# Inserir seus dados
x_data = np.array([1872, 1890, 1900, 1920, 1940, 1950, 1970, 1960, 1980, 1991, 1996])
y_data = np.array([9.9, 14.3, 17.4, 30.6, 41.2, 51.9, 70.2, 93.1, 119.0, 146.2, 157.1])

# Ajustar a função quadrática aos dados
params, covariance = curve_fit(quadratic_function, x_data, y_data)

# Parâmetros ajustados
a, b, c = params

print (params)

# Criar um gráfico de dispersão
plt.scatter(x_data, y_data, label='Dados')

# Gerar pontos da função quadrática ajustada
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = quadratic_function(x_fit, a, b, c)

# Plotar a função quadrática ajustada
plt.plot(x_fit, y_fit, 'r-', label='Ajuste Quadrático')

# Calcular os resíduos
residuals = y_data - quadratic_function(x_data, a, b, c)

# Calcular o desvio padrão dos resíduos
std_deviation_residuals = np.std(residuals)

# Configurar o gráfico
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title(
    f'Função Quadrática Ajustada: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}\nDesvio Padrão dos Resíduos: {std_deviation_residuals:.2f}')
plt.grid()

# Mostrar o gráfico
plt.show()

# Imprimir a função quadrática ajustada e o desvio padrão dos resíduos
print(f'Função Quadrática Ajustada: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}')
print(f'Desvio Padrão dos Resíduos: {std_deviation_residuals:.2f}')

# Imprimir a função quadrática ajustada e o desvio padrão dos resíduos
fit_equation = f'Função Quadrática Ajustada: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}'
print(fit_equation)
print(f'Desvio Padrão dos Resíduos: {std_deviation_residuals:.2f}')

# Calcular os valores ajustados de y_data
y_adjusted = quadratic_function(x_data, a, b, c)

# Imprimir os valores originais e os valores ajustados
for x, y_original, y_calculated in zip(x_data, y_data, y_adjusted):
    print(f'x: {x}, y_original: {y_original:.2f}, y_calculated: {y_calculated:.2f}')
