from pathlib import Path
import shutil

# interate the first level folder
# if there is a folder => start recursion
# if there is a file => copy file
# how to copy file? 
# 1. get file extension, 
# 2. craet folder with that extension, 
# 3. copy file

source = Path("Task4")
output = Path("sorted_task4")

def read_folder(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            read_folder(el)
        else:
            coppy_file(el)  


def coppy_file(file: Path):
    ext = file.suffix
    new_path = output / ext
    new_path.mkdir(exist_ok=True, parents=True)
    shutil.copyfile(file, new_path / file.name)  

read_folder(source)