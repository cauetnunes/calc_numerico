import numpy as np

A = np.array([
    [3, 4, 7, 20],
    [20, 25, 40, 50],
    [10, 15, 20, 22],
    [10, 8, 10, 15]
])

b = np.array([504, 1970, 970, 601])

result = np.linalg.solve(A, b)
print(result)
