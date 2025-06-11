import numpy as np

# Оголошуємо матриці розміру (3, 3) для A та (3, 1) для B
A = np.array([
    [-1, 1, 2],
    [0, -1, -3],
    [4, -3, 2]
])

B = np.array([
    [1],
    [-4],
    [7]
])

# Функція для вирішення системи методом оберненої матриці
def solve_inv_matrix(a, b, verbose=False):
    try:
        A_inv = np.linalg.inv(a)
        x = np.dot(A_inv, b)
        if verbose:
            print(f"Обернена матриця A_inv:\n{A_inv}")
        return x
    except np.linalg.LinAlgError:
        return "Матриця A не має оберненої, система не має єдиного рішення."

print(f"Вектор рішення методом оберненої матриці: \r\n{solve_inv_matrix(A, B)}")

# Функція для вирішення системи методом Крамера
def solve_cramer(a, b, verbose=False):
    det_A = np.linalg.det(a)
    if det_A == 0:
        return "Система не має єдиного рішення (детермінант матриці A дорівнює нулю)."
    
    n = a.shape[1]
    x = np.zeros(n)
    
    for i in range(n):
        A_i = a.copy()
        # Замінюємо i-й стовпець матриці A на вектор B
        A_i[:, [i]] = b
        det_A_i = np.linalg.det(A_i)
        x[i] = det_A_i / det_A
        
        if verbose:
            print(f"det(A_{i+1}) = {det_A_i}")
    
    return x

print(f"Вектор рішення методом Крамера: \r\n{solve_cramer(A, B)}")
