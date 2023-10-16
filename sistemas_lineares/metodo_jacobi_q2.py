import numpy as np

# Número máximo de iterações
N = 1000

# Tolerância
tol = 1e-5

# Valor inicial para x
x = np.zeros(4)

for _ in range(N):
    x_new = np.zeros(4)
    
    x_new[0] = (504 - 4*x[1] - 7*x[2] - 20*x[3]) / 3
    x_new[1] = (1970 - 20*x[0] - 40*x[2] - 50*x[3]) / 25
    x_new[2] = (970 - 10*x[0] - 15*x[1] - 22*x[3]) / 20
    x_new[3] = (601 - 10*x[0] - 8*x[1] - 10*x[2]) / 15

    # Critério de parada
    if np.linalg.norm(x_new - x, ord=np.inf) < tol:
        break

    x = x_new

print(x)
