"""user defined iterables """

# infinite stream of content, logwatch , tail -f

items = [1, 2, 3]

temp = (item ** item for item in items)  # generator expression
print(temp)
print()

for i in temp:
     print(i)
