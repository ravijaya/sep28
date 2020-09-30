print(range(1, 10))

for item in range(1, 10):
    print(item)

print()

temp1 = [hex(i) for i in range(1, 11)]   # list comphension
print(temp1)
print()

temp2 = {i: hex(i) for i in range(1, 11)}   # dict comprehension
print(temp2)
print()

temp3 = {hex(i) for i in range(1, 11)}  # set comprehension
print(temp3)
print(type(temp3))


