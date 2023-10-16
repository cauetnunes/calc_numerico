import numpy as np

def gauss_seidel(A, b, tol=1e-10, max_iter=1000):
    x = np.zeros_like(b, dtype=np.double)
    T = A - np.diag(np.diag(A))
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x_old[i + 1:])) / A[i, i]
        if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tol:
            print(f"Convergiu após {k+1} iterações.")
            return x
    print("Não convergiu após o máximo de iterações.")
    return x

A = np.array([[10, 1, 1], [1, 10, 1], [1, 1, 10]])
b = np.array([12, -12, 12])

x = gauss_seidel(A, b)
print("Solução x:", x)
