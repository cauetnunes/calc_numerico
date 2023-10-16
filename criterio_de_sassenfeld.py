import numpy as np

# Dados do problema
A = np.array([
    [10, 1, 1],
    [1, 10, 1],
    [1, 1, 10]
])
b = np.array([12, -12, 12])
n = len(b)

# Verificação do critério de Sassenfeld
beta = np.zeros(n)
for i in range(n):
    sum1 = sum(abs(A[i,j])*beta[j] for j in range(i))
    sum2 = sum(abs(A[i,j]) for j in range(i+1, n))
    beta[i] = (sum1 + sum2) / abs(A[i,i])

if max(beta) >= 1:
    print("O critério de Sassenfeld não é satisfeito.")
else:
    print("O critério de Sassenfeld é satisfeito!")
    
