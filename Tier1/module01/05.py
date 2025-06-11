import random


# loop

coin = {1: "Opel", 2: "Reshka"}
count_O = 0
count_P = 0
sequence = []

while count_O < 3 and count_P < 3:
    choice = random.randint(1, 2)

    if choice == 1:
        count_O += 1
        count_P = 0
    else:
        count_P = 0
        count_O += 1

    name = coin[choice]
    sequence.append(name)

print(sequence)
print(len(sequence))

