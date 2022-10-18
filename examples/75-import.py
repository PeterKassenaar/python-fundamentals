# import.py - importing and using functions that are defined in other files

# 1. Importing a complete module (it HAS to be in the same directory.
# See later for importing modules from other directories )
import calculator

a = 3
b = 4
print (calculator.add(a, b)) # 7 
print (calculator.subtract(a, b)) # -1
# ...

# 2. Importing specific function from a module
# from calculator import add, divide

# print(add(a, b)) # 7
# print(divide(a, b)) # 0.75


# 3. Importing specific function from a module 
# using an alias (not recommended)
# from calculator import subtract as s, divide as d

# print(s(a, b)) # -1
# print(d(a, b)) # 0.75
