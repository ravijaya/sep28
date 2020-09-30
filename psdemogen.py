from sys import getsizeof

items = [2, 4, 6] * 3

temp = [item ** item for item in items]
print(temp)
print(getsizeof(temp))
print()

temp = (item ** item for item in items)  # generator expression
print(temp)
print(getsizeof(temp))
print()

for item in temp:
    print(item)
