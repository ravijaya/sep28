import re

s = 'the python and the perl scripting'
#s = 'the apple cost me $5.12'
pattern = 'P.+?N'   # non-greedy match

m = re.search(pattern, s, re.I)
print(m)
print()
if m:
    print(m)
    print('match string :', m.group())
    print(m.start())
    print(m.end())
else:
    print('failed to match :(')

