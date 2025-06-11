#_1_
#Алгоритм із часовою складністю O(1) — це константний час. Функція get_first_item просто повертає перше число списку.
#def get_first_item(items):
#    return items[0]
# Завжди виконується одна операція, незалежно від розміру списку
#print(get_first_item([1, 2, 3, 4, 5]))


#_2_
# Алгоритм із часовою складністю O(n) просто проходить по списку чисел і друкує кожне число, а отже, кожне число у списку обробляється один раз
# #def print_all_items(items):
#    for item in items:
#        print(item)
# Кількість операцій прямо пропорційна кількості елементів у списку
#print_all_items([1, 2, 3, 4, 5])


#_3_
#O(n2) може бути порівняння всіх пар векторів у списку, для перевірки того, чи є вони ортогональні
#def dot_product(v1, v2):
#    return sum(x*y for x, y in zip(v1, v2))

#def get_orthogonal_pairs(vectors):
#    n = len(vectors)
#    orthogonal_pairs = []
    
#    for i in range(n):
#        for j in range(i+1, n):
#            if dot_product(vectors[i], vectors[j]) == 0:
#                orthogonal_pairs.append((i, j))
            
#    return orthogonal_pairs

#vectors = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]]
#print(get_orthogonal_pairs(vectors))


#_4_
#O(n 3) є множення матриць
#def multiply_matrices(A, B):
#    n = len(A)
#    C = [[0 for _ in range(n)] for _ in range(n)]
    
#    for i in range(n):
#        for j in range(n):
#            for k in range(n):
#                C[i][j] += A[i][k] * B[k][j]

#    return C

#A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

#print(multiply_matrices(A, B))


#__5__
#import matplotlib.pyplot as plt
#import numpy as np

# Визначаємо діапазон n
#n = np.arange(1, 100)

# Обчислюємо значення для різних часових складностей
#O_1 = np.ones_like(n)
#O_n = n
#O_n_squared = n**2
#O_n_cubed = n**3

# Побудова графіка
#plt.figure(figsize=(12, 8))
#plt.plot(n, O_1, label="O(1)")
#plt.plot(n, O_n, label="O(n)")
#plt.plot(n, O_n_squared, label="O(n^2)")
#plt.plot(n, O_n_cubed, label="O(n^3)")
#plt.xlabel("n")
#plt.ylabel("Operations")
#plt.title("Основні часові складності алгоритмів")
#plt.legend()
#plt.grid(True, which="both", ls="--", c='0.65')
#plt.yscale("log")# Встановлюємо логарифмічну шкалу для осі y
#plt.show()


#__6__
#отримання елемента з масиву за індексом
# def get_item_by_index(items, index):
#   return items[index]

#операція обернення списку
# def reverse_list(items):
#    return items[::-1]


#динамічного програмування є обчислення чисел Фібоначчі
#def fibonacci(n):
#    fib = [0, 1] + [0]*(n-1)
#    for i in range(2, n+1):
#        fib[i] = fib[i-1] + fib[i-2]
#    return fib[n]
#print(fibonacci(10))# Output: 55

