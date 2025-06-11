from collections import deque

def is_palindrome(s):
    # Нормалізація рядка: прибираємо пробіли, переводимо в нижній регістр
    normalized = ''.join(c.lower() for c in s if c.isalnum())
    
    # Додаємо символи до двосторонньої черги
    char_deque = deque(normalized)
    
    # Порівнюємо символи з обох кінців
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

print(is_palindrome("Step on no pets"))              # True
print(is_palindrome("maam"))                         # True
print(is_palindrome("I go to work tomorrow"))        # False

