import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory_structure(path, prefix=""):
    """
    Recursively displays the directory structure with color-coded files and folders.
 Folders are displayed in blue, files in white.
    """
    try:
        entries = list(path.iterdir())
    except PermissionError:
        print(f"{Fore.RED}Permission denied: {path}")
        return

    for idx, entry in enumerate(entries):
        connector = "└── " if idx == len(entries) - 1 else "├── "

        if entry.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}{entry.name}")
            print_directory_structure(entry, prefix + ("    " if idx == len(entries) - 1 else "│   "))
        else:
            print(f"{prefix}{connector}{Fore.WHITE}{entry.name}")

def main():
    if len(sys.argv) < 2:
        print("Please provide the path to the directory as an argument.")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists() or not dir_path.is_dir():
        print("Invalid directory path.")
        sys.exit(1)

    print(f"{Fore.GREEN}Structure of directory: {dir_path}\n")
    print_directory_structure(dir_path)

if __name__ == "__main__":
    main()
