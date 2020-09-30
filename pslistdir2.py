"""cherry picking"""

# import os
# from mod-name import item1, item2, ......
from os import listdir
from os.path import isdir, isfile, join


def ls(dir_path='.'):
    """function definition """
    # print(listdir(dir_path))
    # print()

    for temp in listdir(dir_path):
        abs_path = join(dir_path, temp)

        if isfile(abs_path):
            print(f'{abs_path}: is a file')
        elif isdir(abs_path):
            print(f'{abs_path}: is a directory')


ls()  # raw string r''
