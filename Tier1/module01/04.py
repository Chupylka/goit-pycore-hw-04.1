# ф-ція яка генерує нам рандомний номер машини


# AK 2023 HI


# 0-9, ["A", "B", "C", "E", "H", "I", "K", "M", "O", "P", "T", "X"]


import random


def generate_plate_number():
    set_of_leters = ["A", "B", "C", "E", "H", "I", "K", "M", "O", "P", "T", "X"]
    set_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    l1 = random.choices(set_of_leters, k=2)
    l2 = random.choices(set_of_numbers, k=4)
    l3 = random.choices(set_of_leters, k=2)
    return "".join(l1 + [" "] + l2 + [" "] + l3)

plate_number = generate_plate_number()
print(plate_number)

generate_plate_number()

