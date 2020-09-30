# fmt-str
# :fmt-str


def get_user_list(data_file, target_file):
    users = [line.split(':')[0] for line in open(data_file)]  # list comprehension
    users.sort()

    line_no = 1

    fw = open(target_file, 'w')

    for user in users:
        content = '{:>6}  {}'.format(line_no, user)  # string formatting
        print(content)
        fw.write(content + '\n')
        line_no += 1

    fw.close()


get_user_list('passwd.txt', 'passwd.dat')


"""
file modes
~~~~~~~~~~
read        r
write       w
append      a
"""