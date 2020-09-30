items = [2, 1, 3, 4, 3, 5, 6, 7]
items.sort()

print(items)
exit()
temp = []

for item in items:
    temp.append(hex(item))

print(temp)
print()

# list comprehension
items = [2, 1, 3, 4, 3, 5, 6, 7]
temp2 = [hex(item) for item in items]   # list comprehension
print(temp2)
print()

items = [2, 1, 3, 4, 3, 5, 6, 7]
temp2 = [i ** 2 for i in items]
print(temp2)
print()

temp3 = [i for i in items]
print(temp3)
print()

temp4 = [i for i in items if i % 2]  # compound list comp.
print(temp4)
print()