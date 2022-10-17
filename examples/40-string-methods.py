# string methods - some commonly used methods on strings. 
# But: see https://docs.python.org/3/library/string.html 
# for (a lot!) more information.

# 0. Example strings
hello = 'Hello World'
virgin = 'like a virgin'

# 1. some string methods
print (hello.upper()) # HELLO WORLD
print (hello.lower()) # hello world

print (virgin.capitalize())
print (virgin.startswith('l')) # True
print (virgin.startswith('L')) # False
print (virgin.upper().startswith('L')) # True

print (hello.find('o'))
print (hello[0:5])

# 2. string formatting
print (str.format('My message to everyone is: {0}!', hello))
