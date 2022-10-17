# lists
# Official documentation: https://docs.python.org/3/glossary.html#term-list

# 1. A list of numbers
numbers = [10, -3, 6, 567, 90]
print(numbers[4])  # 90

numbers[4] = 100
print(numbers[4])  # 100

# 2. A list of strings
fruits = ['apple', 'pear', 'orange']
print(fruits[0])  # 'apple'
# print(fruits[3])  # IndexError - out of range (since our list only has 3 items, starting at 0 )

# 3. A list can contain multiple types
# fruits[1] = 7
# print(fruits) # valid. ['apple', 7, 'orange']

# 4. List methods
# fruits.append('pineapple')
# print (fruits)

# print(fruits.pop()) # pineapple

# fruits.remove('apple')
# print (fruits) # ['pear', 'orange']

# fruits.sort()
# print(fruits) # ['orange', 'pear']

# 5. Getting the length of a list
# use the top level len() function
print (len(fruits)) # 2

# 6. Example: printing the items in a list using a while() loop. 
# (This is easier using a for-loop, but you can also do it manually like so:
# i = len(fruits) - 1
# while i >= 0:
#     print( fruits[i])
#     i -= 1
# print ('done')
