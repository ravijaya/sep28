"""user defined exception"""


class RangeError(Exception):
    pass


def check_4_limit(value):
    if not .3 <= value <= .7:
        raise RangeError(f'value not in the range: {value}')


if __name__ == '__main__':
    try:
        check_4_limit(.158)
    except RangeError as error:
        print(error)