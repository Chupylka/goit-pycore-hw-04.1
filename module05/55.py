# перевірка чи існує папка

from pathlib import Path

p = Path("/Users/vitalinka/vscode-basics/module5/51.py")

# print(p.exists()) # False or True в залежності чи існує папка

# print(p.is_file())  # чи за конкретним шляхом знаходиться папка чи там знаходиться файл

print(p.is_dir())

