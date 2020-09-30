"""demo for the simple inheritance """


class Person:
    """base class"""

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def get_info(self):
        print('first name :', self.fname)
        print('last name :', self.lname)


if __name__ == '__main__':
    p = Person('larry', 'wall')
    p.get_info()
