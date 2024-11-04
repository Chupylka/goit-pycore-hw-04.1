# список усіх батьківських шляхів

from pathlib import Path

p = Path("/Users/vitalinka/vscode-basics/module5/54.py")
print(type(p))


perents = list(p.parents)
print(perents)


#for i in p.parents:       (1 віріант)
#    print(i)

#print(p.parent)
#print(p.name)              (2 віріант)
#print(p.suffix)