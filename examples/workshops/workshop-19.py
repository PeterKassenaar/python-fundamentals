# workshop-19. Example of getting numbers 
# and adding them, until Ctrl-C is pressed.

# We capture exceptions using try-except
# More info on available exceptions: https://docs.python.org/3/library/exceptions.html

import sys

def getNumbers():
    sum = 0
    while True:
        try:
            value = int(input())
            sum += value
        except ValueError:
            print ('Sorry, can not add this item. Please enter only numbers')
        except KeyboardInterrupt:
            print('Sum: ', sum)
            sys.exit()

print('Enter numbers, press Ctrl+C to stop')
getNumbers()