# p. 107, comma-code, from 'Automate the boring stuff with Python', Seigwart.
# ***************************************
# Assignment: Take a list value as an argument and return a string
#  with all the items  separated by a comma and a space, with 'and' 
# inserted before the last item. 
# ***************************************

# 1. So: suppose we have a list of fruits
fruits = ['apple', 'orange', 'banana', 'pear', 'grape']

#  2. We want a string: 'Apple, orange, banana, pear and grape'
# What would be ways to achieve this?

def buildString(myList):
    if len(myList) > 1:
        # prepare the last item
        lastItem = '{0} and {1}'.format(str(myList[-2]), str(myList[-1]))

        # create a result for the first items. We already covered the last two items.
        result = ''
        for item in myList[:-2]:
            result += str(item) + ', '

        # result = ', '.join((myList[:-2])) # this works if the list has only strings. But we need to address *any* input type.
        result += lastItem
        return result.capitalize()
    else:
        return 'Error: no valid list provided.'


print(buildString(fruits))
