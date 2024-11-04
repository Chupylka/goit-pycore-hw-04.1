from pathlib import Path



def parse_file(path):
    for el in path.iterdir(): # iterdir - повертає ітерат (список) зі всіма елементами в поточній папці
        if el.is_dir():
            parse_file(el)
        else:
            print(f"The is folder {el}")


print(parse_file(Path("Task4")))

#from pathlib import Path
#def parse_file(path):
#    for el in path.iterdir(): # iterdir - повертає ітерат (список) зі всіма елементами в поточній папці
#        if el.is_dir():
#            parse_file(el)
#        else:
#            print(f"The is folder {el}")
#print(parse_file(Path("Task4")))