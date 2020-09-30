def demo():
    try:
        value_1 = int(input('enter the value 1:'))
        value_2 = int(input('enter the value 2:'))
        return value_1 + value_2
    except Exception as error:  # generic
        print('we are at except block: ', error)
    else:
        print('else-block of the exception handling')
        # print(value_1 * value_2)


if __name__ == '__main__':
    print(demo())
