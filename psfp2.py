"""functional programming"""

items = [3, 1, 5, 4, 6, 3, 6]

m = map(hex, items)
print(m)

for item in m:
    print(item)

print()
s = 'peter pan'
m = map(ord, s)
print(list(m))