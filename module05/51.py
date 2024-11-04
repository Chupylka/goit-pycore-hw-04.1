# \n - початок з нового рядка
# каредка - рисочка курсока

# charcter meaning
# "r" - open for reading (default)
# "w" - open for writing, truncating the file first
# "x" - create a new file and open it for writing
# "a" - open forwriting, appending to the end of the file if it exists
# "b" binary mode
# "t" text mode (default)
# "+" open a disk file for updating (writing and writing)


#--------------------------------------------------
# щоб створити файл
#file = open("test.txt", "r")
#print(file)
#print(dir(file))
#file.write("Hello worrd\n")
#file.write("Glory to Ukraine\n")
#file.close()
#----------------------------------------------------


#----------------------------------------------------
# щоб отримати ввесь контент файлу
#file = open("test.txt", "r")
#print(file.read())
#file.close()
#----------------------------------------------------


#----------------------------------------------------
# повертає список з рядками
#file = open("test.txt", "r")
#print(file.readlines())
#file.close()
#----------------------------------------------------


#----------------------------------------------------
# кількість символів
#file = open("test.txt", "r")
#print(file.tell())
#print(file.read(5))
#file.seek(0)
#print(file.tell())
#print(file.read(5))
#print(file.tell())
#file.close()


#--------------------------------------------------------
# щоб записати д-кілька рядків


# with - щоб файл не зависав в системі

with open("test.txt", "a") as f1:
    f1.write("\nIvan, Walker, Kansas")
    




