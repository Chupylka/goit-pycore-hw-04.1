import numpy as np
# Код оголошення векторів не можна змінювати
a = np.array([[1, 2, 3, 4, 5]])
b = np.array([[1/2, 1, 2, 3, 4]])

res = a - b.T
