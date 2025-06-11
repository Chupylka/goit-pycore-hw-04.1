fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin orange"]



# fruits_with_only_two_vowels = [
#     f for f in fruits if len([True for s in f if s in ["a", "e", "i", "o", "u"]]) == 2
#     ]

# res = [fruit for fruit in fruits if len(fruit) > 5]
# print(res)

# {"mango": 5}
#d = {}
# for fruit in fruits:
#     d[fruit] = len(fruit)


d = {fruit: len(fruit) for fruit in fruits}
print(d)