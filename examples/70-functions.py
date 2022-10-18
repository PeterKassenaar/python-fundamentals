# functions - example of some functions

# 1. Simple example, take a string as parameter and return Hello + that string
def sayHello(firstname):
    return str.format('Hello {0}!', firstname)


print(sayHello('Peter'))  # Hello Peter!
print(sayHello('Sandra'))  # Hello Sandra!

# 2. A function with multiple parameters
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# 2a. Mini workshop: write code here that *calls* the functions with 2 numbers
# ... your code here ...

# 2b. Also write code that call the function with 2 variables. 
# Q: must the variables have the same name (here: 'a' and 'b') as the parameters? 
# ... your code here ...

# 3. Another function. We calculate the square of a passed in value (called 'number')
# def squared(number):
#     return number * number

# print(squared(5))  # ?? what will be the outcome?

# def formatAddress(name, address, city):
#     return str.format('''
#         {0}
#         {1}
#         {2}
#      ''', name, address, city)

# a = 'Peter Kassenaar'
# b = 'Laarstraat 47'
# c = 'Zutphen, NL'
# print (a, b, c) # Q: will this work?

# ***************************
# 4. Workshop - create Calculator functions
# Try this yourself first!
# ***************************

# see: 70-calculator.py