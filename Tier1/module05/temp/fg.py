#функції
# camelCase, PaskalCase, snake_case
# covner string from camelCase to snake_case
# між 2 ф-ціями повинно бути 2 порожні рядки



#declaration (оголошення ф-ції)
#function sigature: def + name + list of params (сігнатура ф-ції)
def convert_camel_to_snake_case(text, is_pascal_case): # якщо ф-ція має більше ніж 5 параметрів її треба розбити на менші ф-ції (підставляє з ліва на право в аргумент)
    # scope (область визначеності)
    res = ""
    for char in text:
        if char.isupper():
            res += "_" + char.lower()
        else:
            res += char
    if is_pascal_case:
        res = res[1:]
    return res

# function call (виклик ф-ції)
# () -> call operator (оператор виклику)

# name arguments (іменовані параметри)
convert_text = convert_camel_to_snake_case(is_pascal_case= False, text="dbPassword") # аргументи #("DbPassword", True)-стандартний запит
print(convert_text)

convert_text = convert_camel_to_snake_case(text="DbPassword", is_pascal_case= True)#(text="DbPassword", is_pascal_case= True) запит на пряму
print(convert_text)
# Positional argument cannot appear after keyword arguments(non named arguments before named arguments)