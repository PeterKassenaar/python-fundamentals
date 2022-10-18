# scopes.py - illustration of the Python LEGB scope model

# 1. Consider a simple loop:
def numbers():
    i = 0
    while i <=10:
        print(i)
        i += 1
    print ('i is now: ', i)

numbers()
# 2. Here 'numbers' has global scope, while 'i' has local scope. 
# But outside the while-loop, i still exists!

# 3. Variable names can be shadowed:
# Lets say we have a variable 'count':
count = 5

# 4. This function simply prints the current value of 'count'
# def show_count():
#     print('count is now: ', count)

# # 5. This function sets the count to whatever number is passed in (right?):
# def set_count(c):
#     count = c

# show_count() # 5 - as expected
# set_count(10) # We set 'count' to 10 - right?
# show_count() # still 5 - WTF?

# Answer: we set a shadowed variable count, but dit not update
# the Global variable count. 

# If we want this, use the keyword 'global', like so:
# def set_global_count(c):
#     global count # keyword global
#     count = c

# show_count() # 5 - as expected
# set_global_count(10) # updat the count value
# show_count() # 10 - as expected
