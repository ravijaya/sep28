from zipfile import ZipFile
from os.path import isdir
from os import mkdir

extract_path = '/tmp/catch32'

if not isdir(extract_path):
    mkdir(extract_path)


zf = ZipFile('source.zip', mode='r')

zf.extractall(extract_path)

zf.close()