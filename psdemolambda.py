"""
functional programming

syntax for the lambda function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        lambda arg1, arg2, ... : expression
"""

power = lambda x, n=0: x ** n

print(power)
print()
print(power(3, 4))
print()
print(power(3))