# 1. Definition of some tuples
t1 = ('Holland', 1, True)
t2 = ('apple', 'pear', 'orange')
t3 = t1 + t2
t4 = 1, 1, 2, 3, 5, 6, 8, 2, 1, 4, 1, 3, 5, 6, 1 # (...) can be omitted

# 2. Working with tuples
print(t1[0])  # Holland
print(len(t1))  # 3
# t[0]= 'Belgium' # TypeError: 'tuple' object does not support item assignment
print(t3)  # ('Holland', 1, True, 'apple', 'pear', 'orange')
print(type(t1))  # <class 'tuple'>
print(t4.count(1))  # 5

# 3. Tuples vs. Lists
# Memory usages:
# import sys
# a_list = [] # define empty list (can be omitted)
# a_tuple = () # define empty tuple (can be omitted)
# a_list = [1, 2, 3, 4,5, 6]
# a_tuple = (1, 2, 3, 4,5, 6)
# print('Memory usage of list: ', sys.getsizeof(a_list))
# print('Memory usage of tuple: ',sys.getsizeof(a_tuple))

# 4. Tuples vs. Lists
# Lookup time:
# import time
 
# l=list(range(10000001))
# t=tuple(range(10000001))
 
# start = time.time_ns()
# for i in range(len(t)):
#     a = t[i]
# end = time.time_ns()
# print("Total lookup time for Tuple(): ", end - start)
 
# start = time.time_ns()
# for i in range(len(l)):
#     a = l[i]
# end = time.time_ns()
# print("Total lookup time for List[]: ", end - start)

# 5. Destructuring tuples
# size = (1024, 768)
# width, height = size
# print (width) # 1024
# print (height) # 768

# 6. Example: getting the minimum and maximum age of a group users
userAges = (24, 45, 18, 87, 54, 66, 29, 38, 47, 24, 56, 61, 19, 21, 22, 24, 45)
# def minMaxAge(ages):
#     # returning two values, using the built-in min() and max() function
#     return min(ages), max(ages)

# 6a. What does the function return?
# print('returned from function: ', minMaxAge(userAges))

# 6b. Destructuring the values in different variables
# minAge, maxAge = minMaxAge(userAges)
# print ('minimum age:', minAge)
# print ('maximum age:', maxAge)

#7. Testing if a value is in a tuple, use the 'in' operator
# print(19 in userAges) # True
# print(62 in userAges) # False
# print(62 not in userAges) # True

# 8. Inefficient! Works, but don't do this:
# ageToCheck = 19
# for value in userAges:
#     if value == ageToCheck:
#         print(ageToCheck, 'is in the collection!')
#         break

# 9. Tuple methods:
# print(userAges.count(24)) # 3
# print(userAges.index(45)) # 1

# 10. Slicing a tuple, using the :index notation
# print(userAges[:3]) # create a new tuple with the first three items
# print(userAges[-3:]) # create a new tuple with the LAST three items
# print(userAges[3:5]) # create a new tuple with items between position 3 and 5 (NOT including the last position, so we get 2 values)
