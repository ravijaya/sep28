from random import shuffle

items = list(range(1, 201))
# shuffle(items)
print(items)
print()

m = filter(lambda n: n % 7 == 0, items)
print(list(m))
