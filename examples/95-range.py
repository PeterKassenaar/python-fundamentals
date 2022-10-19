# range.py - example on ranges -
# A range is a sequence, representing an arithmic progression of integers.

# 1.  simple range example
# myRange = range(5)
# print (myRange) # range(0, 5)

# for i in range(5):
#     print (i)

# 2.  Range with start/stop value
#  The stop value is NOT included (it can be the start value for a next range)
# for i in range(10, 15):
#     print (i)

#  3. Creating a list of a range
# print(list(range(10, 15))) # [10, 11, 12, 13, 14]

#  4. Combining ranges in a list
# print(list(range(10, 15)) + list(range(15,20))) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# 5. Step argument:
# print(list(range (10, 20, 2))) # [10, 12, 14, 16, 18]

#  6. Using enumerate(), which creates pairs of tuples with an index value
# myList = range(10, 15)
# for p in enumerate(myList):
#     print(p)

#  7. OR: using a list of non-numeric values
# myList = ('Intel', 'Apple', 'Microsoft', 'Google', 'Facebook')
# for q in enumerate(myList):
#     print(q)

# myList = ('Intel', 'Apple', 'Microsoft', 'Google', 'Facebook')
# for index, company in enumerate(myList):
#     print(str.format('Company id: {0} - name: {1}', index, company))
    # Alternative syntax for str.format():
    # print(f'Company id: {0} - name: {1}', index, company)
    # OR:
    # print('Company id: {0} - name: {1}'.format(index, company))
