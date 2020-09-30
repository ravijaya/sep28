from os.path import isdir, isfile, getsize, getmtime, join
from os import listdir
from time import ctime


path = r'/tmp'

abs_path = join(path, listdir(path)[3])
print(abs_path)
print(isfile(abs_path))
print(isdir(abs_path))
print()
print(getsize(abs_path))
print(getmtime(abs_path))
print(ctime(getmtime(abs_path)))