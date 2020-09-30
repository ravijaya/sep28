try:
    items = {}
    print(items['lang'])
except (FileNotFoundError, IOError, IndexError, NameError, KeyError) as error:
    print('same')