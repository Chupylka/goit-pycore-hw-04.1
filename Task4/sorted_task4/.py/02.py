import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 100 or quantity > (max - min + 1):
        return[]
    lottery_numbers = random.sample(range(min, max + 1), quantity)
    return sorted(lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Numbers: 23, 41, 37", lottery_numbers)

