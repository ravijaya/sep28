from json import load
from pprint import pprint as pp

try:
    names = ['size', 'mtime']
    content = load(open('tmp.json'))
    for dir_name, file_items in content.items():
        print(dir_name)
        for filename, fileprop in file_items.items():
            print(f"\t{filename}")
            for name, value in zip(names, fileprop):
                print(f'\t\t{name} : {value}')
            print()

except FileNotFoundError as err:
    print(err)