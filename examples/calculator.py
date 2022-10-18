# ***************************
# 4. Workshop #12- create Calculator functions
# Try this yourself first!
# ***************************
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if (b == 0):
        return 'Can not divide by zero!'
    return a / b

# Calling your functions, but only if 
# this file is executed directly and 
# not imported in another file:
a = 10
b = 20
print(add(a, b))
print(subtract(a, b))
print(multiply(a, b))
print(divide(a, b))
