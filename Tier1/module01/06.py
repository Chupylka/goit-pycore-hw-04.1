# buble sort, binary, merge, quick, fast, random - sort
import random
array = [1, 2, 4, 2, 122, 13]


sorted_array = sorted(array)
attempt = 0

while array != sorted_array:
    attempt += 1
    random.shuffle(array)
    print(f"# {attempt}, arr: {array}")
    

    