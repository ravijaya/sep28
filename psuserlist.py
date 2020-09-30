# fmt-str
# :fmt-str

def get_user_list(data_file):
    users = [line.split(':')[0] for line in open(data_file)]  # list comprehension
    users.sort()

    line_no = 1

    for user in users:
        print('{:>6}  {}'.format(line_no, user))  # string formatting
        line_no += 1


get_user_list('passwd.txt')
