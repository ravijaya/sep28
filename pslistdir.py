"""python's iterator"""

import os


def ls(dir_path='.'):
    """function definition """
    print(os.listdir(dir_path))
    print()

    for item in os.listdir(dir_path):
        print(item)


ls()  # raw string r''
