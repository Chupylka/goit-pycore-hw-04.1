# ПОРАДА: використовувати завжди search


import re

claim = "People love Python."


print (re.search("Python", claim))



print (re.match("Python", claim)) # очікує що слово буде стояти на початку (не використовується з extra текстом)



