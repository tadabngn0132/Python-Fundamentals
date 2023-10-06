import os

def read_folder(path, level):
    print_spaces(level)
    if os.path.isdir(path):
        print('+', path.split('/')[-1])
    else:
        print('-', path.split('/')[-1])
    if os.path.isdir(path):
        level += 1
        list_paths = os.listdir(path)
        for p in list_paths:
            read_folder(path + '/' + p, level)

def print_spaces(level):
    for i in range(level):
        print(' ', end='')

read_folder('d:\Pythoncode', 0)