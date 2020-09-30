from pprint import pprint as pp

content = [line.split(':') for line in open('passwd.txt')]

content = [line.split(':') for line in open('passwd.txt') if line.startswith('r')]

pp(content)