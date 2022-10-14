# Simple example on if-statements
a = True
if a:
    print('Variable a is True')
else:
    print ('Variable a is False')


# Next two statements are the same, 
# because of implicit conversion to bool.
if bool('I love pizza'):
    print('I love pizza!')

# is the same as...
if 'I love pizza':
    print('I love pizza!')

# elif - if you have multiple if-statements w/ else-clauses
b = 100
if b > 100:
    print('Variable b is greater than 100')
elif b == 100:
    print('Variable b is exactly 100')
else:
    print('Variable b is less than 100')
