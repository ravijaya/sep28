try:
    value_1 = int(input('enter the value 1:'))
    value_2 = int(input('enter the value 2:'))

    print(value_1 / value_2)

except TypeError as error:
    print(error)
except ValueError as error:
    print(error)
except Exception as error:  # generic
    print(error)
