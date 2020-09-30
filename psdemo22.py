from pprint import pprint as pp

data = [line for line in open('tiny.txt')]
pp(data)
print()
pp(set(data))
print()

data = {line for line in open('tiny.txt')}
pp(data)


# set aka unordered collections
# {1, 2, 3} or {3, 2, 1}

