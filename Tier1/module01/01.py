

class TriangleDoesNotExist(Exception):
    pass
try:
    a = float(input("enter side a >>>"))
    b = float(input("enter side b >>>"))
    c = float(input("enter side c >>>"))

    if (a > b + c) or (b > a + c) or (c > b + a):
        raise ValueError("Such triangle does not exist")
    ratio = a / b
except ZeroDivisionError as e:
    print("Can not delete to 0")
    radio = 0
except ValueError as e:
    print(e)
except Exception as e:
    print("Incorrect date")
else:
    print("Here is the result", ratio) #застосовується коли розпочинається дія
finally:
    print("Let's close the file")
