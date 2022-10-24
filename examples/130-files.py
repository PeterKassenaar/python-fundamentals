# Using a file for writing and reading
# If the file doesn't exist, Python will create it

# 1. Opening the file for writing
myFile = open(file='settings.txt', mode='wt', encoding='utf-8')

# 2. Writing to the file
myFile.write('name=Peter\n')
myFile.write('email=info@kassenaar.com\n')
myFile.write('age=22')

# 3. Closing the file
myFile.close()

# 4. Opening the file again, this time for reading
# myFile = open(file='settings.txt', mode='rt', encoding='utf-8')
# settings = [] # we're storing the results as tuples in this list

# ************************************
# READING INTO TUPLE
# 5. Read the contents and convert them
# for i in myFile.readlines():
#     tmp = i.split('=')
#     # strip out the newline char
#     settings.append((tmp[0], tmp[1].replace('\n', '')))

# # 6. Don't forget to close the file
# myFile.close()

# 7. Print to console
# print(settings)

# ***************************** 
# READING INTO DICT
# 8. Creating a new 'settings' variable, this time as a dictionary,
# and using the 'with' statement to automatically close the file 
# after usage.
# settings = {}
# with open(file='settings.txt', mode='rt', encoding='utf-8') as myFile:
#     for i in myFile.readlines():
#         key, value = i.split('=')        
#         settings[key] = value.replace('\n', '')        
#     # Alternate syntax:
    # for line in myFile:
    #     key, val = line.split('=')
    #     settings[key] = val.replace('\n', '')

# settings.txt is now automatically closed, as the with-block has ended
# print (settings)

# Print a formatted string of the dictionary
# print('My name is {0}, my email is {1} and I am {2} years old'
#         .format(settings['name'], settings['email'], settings['age']))

# ***************************** 
# READING INTO LIST
# 9. Reading multiple lines into a list
# with open(file='settings.txt', mode='rt', encoding='utf-8') as myFile:
#     lines = myFile.readlines() # read all lines into a list
#     print(lines)

