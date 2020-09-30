import re

s = 'the python and the perl scripting'
s = 'the apple cost me $5.12'
pattern = '\$5\.12'   # non-greedy match

m = re.search(pattern, s, re.I)

if m:
    print(m)
    print('match string :', m.group())
    print(m.start())
    print(m.end())
else:
    print('failed to match :(')

