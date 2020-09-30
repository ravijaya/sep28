import re


def grep_me(pattern, filename):
    for line in open(filename):
        if re.search(pattern, line, re.I):
            print(line, end='')


grep_me('bash$', 'passwd.txt')
