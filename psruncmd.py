from sys import platform
from subprocess import check_output


if platform in ['linux', 'darwin']:
    cmd = ['/sbin/ifconfig']
elif platform == 'win32':
    cmd = ['ipconfig']

op = check_output(cmd)
print(op.decode())  # bytes into str