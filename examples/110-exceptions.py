# exceptions.py - some examples on exception handling

# ***************************************
#  1. Given the following function:
# def divide(a, b):
#     if (b == 0):
#         return 'Can not divide by zero!'
#     return a / b

# ***************************************
# 2. We can catch errors with try-except blocks
def divide(a, b):
    try:
        result= a / b
    except:
        result = 'Error, Invalid argument provided!'
    return result

print(divide(10,2)) #5
print(divide(10,0)) # 'Error, Invalid argument provided!'

# ***************************************
# 3. However, we want to catch *specific* errors, so using its name:
# def divide(a, b):
#     try:
#         result= a / b
#     except ZeroDivisionError:
#         result = 'Error, you can not divide by zero (0)!'
#     return result

# print(divide(10,2)) #5
# print(divide(10,0)) # 'Error, you can not divide by zero (0)!'

# ***************************************
# 4. We can handle multiple errors with except-blocks.
# Lets assume we have a function that converts strings to numbers

# def convertToInt(value):
#     result = -1  # assume error, return -1 in that case
#     try:
#         result = int(value)
#         print('conversion succeeded: ', result)
#     except TypeError:
#         print('TypeError, input value has the wrong Type.')
#     except ValueError:
#         print('ValueError, input value can not be converted.')

#     return result

# convertToInt('123') # OK
# convertToInt([1, 2, 3]) # Error
# convertToInt('Hello world') # Error

# ***************************************
# 5. We can combine handling the errors;
# By using the exception object and aliasing it as 'e', we
# get access to the actual error
# def convertToInt(value):
#     result = -1  # assume error, return -1 in that case
#     try:
#         result = int(value)
#         print('conversion succeeded: ', result)
#     except (TypeError, ValueError) as e:
#         print('Error, we cannot convert your value: {0}'.format(e))  

#     return result

# convertToInt('123') # OK
# convertToInt([1, 2, 3]) # Error
# convertToInt('Hello world') # Error

# ***************************************
# 6. Handle the errors silently, using pass.
# def convertToInt(value):
#     result = -1  # assume error, return -1 in that case
#     try:
#         result = int(value)
#     except (TypeError, ValueError) as e:
#         pass

#     return result

# print(convertToInt('123')) # OK
# print(convertToInt([1, 2, 3])) # Error, but program continues, as we have handled the error and return -1
# print(convertToInt('Hello world')) # Error, idem, -1

# ***************************************
# 7. Better practice - don't return arbitrary values (like -1), but
# (re)raise the error
# def convertToInt(value):
#     try:
#         return int(value)
#     except (TypeError, ValueError) as e:
#         print ('Error, conversion failed: {0}'.format(e))
#         raise (e)

# print(convertToInt('123')) 
# print(convertToInt([1, 2, 3]))
# print(convertToInt('Hello world')) 

# ***************************************
# 8. Document the API of your functions, using docstrings
# def convertToInt(value):
#     """Convert a value to an integer

#     Args: 
#         value - the number to be converted

#     Returns:
#         the integer of the value that was converted

#     Raises:
#         Prints an error if the value can not be converted
#         and reraises the thrown error.
#      """
#     try:
#         return int(value)
#     except (TypeError, ValueError) as e:
#         print ('Error, conversion failed: {0}'.format(e))
#         raise (e)

# print(convertToInt('123')) 
# print(convertToInt([1, 2, 3]))
# print(convertToInt('Hello world')) 

# ***************************************
# 9. Use finally if you have code that you always want to run
# def convertToInt(value):
#     """Convert a value to an integer

#     Args: 
#         value - the number to be converted

#     Returns:
#         the integer of the value that was converted

#     Raises:
#         Prints an error if the value can not be converted
#         and reraises the thrown error.
#      """
#     try:
#         return int(value)
#     except (TypeError, ValueError) as e:
#         print ('Error, conversion failed: {0}'.format(e))
#         raise (e)
#     finally: 
#         print('this code is always executed')

# print(convertToInt('123')) 
# print(convertToInt([1, 2, 3]))
# print(convertToInt('Hello world')) 