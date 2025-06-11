import numpy as np
A = np.array([[
    [-1, 1, 2],
    [0, -1, -3],
    [4, -3, 2]
]])
B = np.array([[
    [1],
    [-4],
    [7]
]])

# Напиши функцію для вирішення системи матричним методом
def solve_inv_matrix(a, b, verbose=False):
    try:
        A_inv = np.linalg.inv(A)
        x = np.dot(A_inv, B)
        if verbose:
            print(f"Обернена матриця A_inv:\n{A_inv}")
        return x
    except np.linalg.LinAlgError:
        return "Матриця A не має оберненої, система не має єдиного рішення."

print(f"Вектор рішення: \r\n {solve_inv_matrix(A, B)}")