"""functional programming"""

import re
import sys

pattern = 'login'
# pattern = '^r'

matched_lines = filter(lambda line: re.search(pattern, line, re.I), open('passwd.txt'))
print(matched_lines)
print(sys.getsizeof(matched_lines))

result = [line for line in open('passwd.txt') if re.search(pattern, line, re.I)]
print(result)
print(sys.getsizeof(result))

# generator

# for matched_line in matched_lines:
#     print(matched_line, end='')