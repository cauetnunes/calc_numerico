import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Função exponencial para ajuste
def exponential_function(x, a, b, c):
    return a * np.exp(b * (x - 1872)) + c

# Inserir seus dados
x_data = np.array([1872, 1890, 1900, 1920, 1940, 1950, 1970, 1960, 1980, 1991, 1996])
y_data = np.array([9.9, 14.3, 17.4, 30.6, 41.2, 51.9, 70.2, 93.1, 119.0, 146.2, 157.1])

# Ajustar a função exponencial aos dados
params, covariance = curve_fit(exponential_function, x_data, y_data, maxfev=10000)

# Parâmetros ajustados
a, b, c = params

# Criar um gráfico de dispersão
plt.scatter(x_data, y_data, label='Dados')

# Gerar pontos da função exponencial ajustada
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = exponential_function(x_fit, a, b, c)

# Plotar a função exponencial ajustada
plt.plot(x_fit, y_fit, 'r-', label='Ajuste Exponencial')

# Calcular os resíduos
residuals = y_data - exponential_function(x_data, a, b, c)

# Calcular o desvio padrão dos resíduos
std_deviation_residuals = np.std(residuals)

# Configurar o gráfico
plt.xlabel('Ano')
plt.ylabel('Valor')
plt.legend()
plt.title(f'Função Exponencial Ajustada: y = {a:.2f} * e^({b:.6f} * (x - 1872)) + {c:.2f}\nDesvio Padrão dos Resíduos: {std_deviation_residuals:.2f}')
plt.grid()

# Mostrar o gráfico
plt.show()

# Imprimir a função exponencial ajustada e o desvio padrão dos resíduos
print(f'Função Exponencial Ajustada: y = {a:.2f} * e^({b:.6f} * (x - 1872)) + {c:.2f}')
print(f'Desvio Padrão dos Resíduos: {std_deviation_residuals:.2f}')
