# Simple workshop - recreate the table of a number, using range()
print('table of 4:')
table = 4
for i in range(1, 11):    
    result = i * table
    print(str.format('{0} x {1} = {2}', i, table, result))

# OR: Let the user input a number with the keyboard:
# print('what number do you want the table for?:')
# table = int(input())
# for i in range(1, 11):    
#     result = i * table
#     print(str.format('{0} x {1} = {2}', i, table, result))
