"""variable len arguments """

from zipfile import ZipFile
from glob import glob


class MakeZip:
    def __init__(self, archive_name, *args):
        self.name = archive_name
        self.archive_content = args
        self.save()

    def save(self):
        zf = ZipFile(self.name, mode='w')

        for filename in self.archive_content:
            zf.write(filename)
            print(f'{filename} : added')

        zf.close()


if __name__ == '__main__':
    MakeZip('source.zip', *glob('*.py'))
