from os import listdir
from os.path import isfile, getsize, getmtime, join, basename
from time import ctime
from pprint import pprint as pp


class DirectoryListing:
    def __init__(self, *args):
        self.directories = args
        self.container = {}
        self.read_directories()

    def read_directories(self):
        for dir_name in self.directories:
            generator_for_absolute_path = (join(dir_name, item) for item in listdir(dir_name))
            filenames = filter(isfile, generator_for_absolute_path)

            temp = {}

            for filename in filenames:
                file_prop = [getsize(filename), ctime(getmtime(filename))]
                filename = basename(filename)
                #self.container.setdefault(dir_name, {})[filename] = file_prop
                temp[filename] = file_prop

            self.container[dir_name] = temp

if __name__ == '__main__':
    dl = DirectoryListing(r'/tmp', r'/home/ravijaya')
    pp(dl.container)
