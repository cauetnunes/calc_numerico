import numpy as np

def gauss_seidel(A, b, tol=1e-5, max_iter=1000):
    x = np.zeros_like(b)
    n = A.shape[0]
    for _ in range(max_iter):
        x_prev = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))
            s2 = sum(A[i][j] * x_prev[j] for j in range(i + 1, n))
            x[i] = (b[i] - s1 - s2) / A[i][i]
        if np.linalg.norm(x - x_prev, np.inf) < tol:
            return x
    return x

A = np.array([
    [3, 4, 7, 20],
    [20, 25, 40, 50],
    [10, 15, 20, 22],
    [10, 8, 10, 15]
])

b = np.array([504, 1970, 970, 601])

result = gauss_seidel(A, b)
print(result)
