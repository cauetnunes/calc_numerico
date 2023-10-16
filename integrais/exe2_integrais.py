import numpy as np

# Dados fornecidos
L = 1  # metro
theta_0 = np.radians(42)  # convertendo graus para radianos
g = 9.81  # aceleração da gravidade em m/s^2
k = np.sin(theta_0/2)

# Definindo a função a ser integrada
def f(x):
    return 1/np.sqrt(1 - k**2 * np.sin(x)**2)

# Implementando a regra 3/8 de Simpson
a = 0
b = np.pi/2
h = (b - a)/3

integral = f(a) + 3*f(a + h) + 3*f(a + 2*h) + f(b)
integral *= (3*h/8)

# Calculando o período T
T = 4 * np.sqrt(L/g) * integral

print(f"O período T do pêndulo é aproximadamente: {T:.4f} segundos")
