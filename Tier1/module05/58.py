#fh = open("test.txt", "r")
#lines = []
#for line in fh.readlines():
#    lines.append(line.strip())
#lines = [el.strip() for el in fh.readlines()] #скорочення до (2-4)
#print(lines)


# list comprehension (наповнення списку)
# l = [<res> <for> <if>]



#numbers = []
#for i in range(101):
#    if i % 2 == 1:
#        numbers.append(i)
#print(numbers)
#numbers = [i for i in range(101) if i % 2 == 1]
#print(numbers)

# numbers = [i if i % 2 == 1 else 0 for i in range(101)]
# print(numbers)