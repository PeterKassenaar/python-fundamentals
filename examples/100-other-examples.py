#  Some other, random, Python techniques and -examples

# ****************
# 1. Formatting strings
# ****************
from copy import copy


name = 'Peter'
age = 12
# # Fully notated string.format()
# print(str.format('I am {0} and I am {1} years old!', name, age))

# # Omitting the numbers, if you are sure of the exact order
# print(str.format('I am {} and I am {} years old!', name, age))

# # using the .format() option
# print('I am {0} and I am {1} years old!'. format(name, age))

# # using 'f' before a string
# print(f'I am {name} and I am {age} years old!')

# ****************
# 2. Negative indexing in lists
# ****************
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(myList[-1])  # reads backwards, so 10 printed
# print(myList[-2])  # 9, and so on

# #  2a. Slicing
# print(myList[:3])  # [1, 2, 3] (element 0, 1, 2)
# print(myList[3:])  # [4, 5, 6, 7, 8, 9, 10] (element 3 onwards until the end)
# print(myList[3:6])  # [4, 5, 6] (element 3 to 5 (NOT including element 6))
# print(myList[1:-1])  # [2, 3, 4, 5, 6, 7, 8, 9] (omit first and last item)
# yourlist = myList[:]  # create a copy of myList and store it in yourList
# print(yourlist is myList)  # False, since we have two objects
# print(yourlist == myList)  # True, since the contents are the same

# However, this creates a SHALLOW copy. Both variable point to the same object.
# If you change a value in one list, it is changed in the other also!

# use the copy() library if you want/need DEEP copies of objects
# import copy
# anotherList = copy.deepcopy(myList)
# print (anotherList)

# ****************
# 3. Deleting items using del()
# ****************
# companies = ['intel', 'microsoft', 'apple', 'google', 'facebook']
# del (companies[1])
# print(companies) # ['intel', 'apple', 'google', 'facebook']

# ****************
# 4. Sorting and reversing a list
# ****************
# companies.sort()
# print(companies) # ['apple', 'facebook', 'google', 'intel', 'microsoft']

# companies.reverse()
# print(companies) # ['microsoft', 'intel', 'google', 'facebook', 'apple']

# # 4a. Creating a new, sorted list (instead of sorting in place)
# companies = ['intel', 'microsoft', 'apple', 'google', 'facebook']
# newCompanies = sorted(companies)
# print(newCompanies)  # create a copy, original list companies untouched

# reversedCompanies = reversed(companies)
# print(list(reversedCompanies))  # create a copy, original list companies untouched

# (we use the list() constructor because reversed() returns an 'iterator'
# of type <list_reverseiterator object at 0x00000202DA46B670>.)

#  
# ****************
# 5. Comprehension
# ****************
numbers = [1, 2, 3, 4, 5]
doubled = [2 * i for i in numbers] # instead of writing a for-loop, we double the numbers in one statement
print (doubled)

# Lets use a list of companies again. We want to know the number of characters of every company:
companies = ['intel', 'microsoft', 'apple', 'google', 'facebook']
length = ['{0} has {1} characters'.format(company, len(company)) 
        for company in companies]
for item in length:
    print (item)
