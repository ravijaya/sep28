try:
    value_1 = int(input('enter the value 1:'))
    value_2 = int(input('enter the value 2:'))
except Exception as error:  # generic
    print('we are at except block: ', error)
finally:
    print('finally-block of the exception handling')

