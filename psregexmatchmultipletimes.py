"""multiple times"""
import re

s = 'the Python and the perl scripting pythON pythoN'
pattern = 'P.+?N'

print(re.finditer(pattern, s, re.I))
print()

for m in re.finditer(pattern, s, re.I):
    print(m.group())
    print(m.span())
    print()

print(re.findall(pattern, s, re.I))
print(re.findall(pattern, s, re.I)[:3])

