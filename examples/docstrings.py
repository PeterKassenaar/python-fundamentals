'''Explanation of docstrings.

 This is the same file as 82-cli-arguments.py, but
 now enhanced with Docstrings, documenting the code
 so it can be invoked with the built-in Python help system.

 See https://peps.python.org/pep-0257/ for more information.
'''
import sys
import requests

def getData(url):
    '''Get data from a URL

    Args:
        url: the URL of the Typicode/jsonplaceholder API

    Returns:
        A list of (dummy) users from the API
    '''
    response = requests.get(url)
    return response.json()

# 3. Printing the users
def printUsers(users):
    '''Print a list of users on the screen

    Args:
        users: the list of users to print

    Returns:
        Nothing
    '''
    print('List of users: ')
    for user in users:
        print(user['id'], ':', user['name'], '(', user['company']['name'], ')')

def main(url):
    '''The main function that is run when the program starts

    Args:
        url: the URL of the Typicode/jsonplaceholder API. This 
        can come from the command line or from an external/enclosing application.

    Returns:
        Nothing
    '''
    users = getData(url)
    printUsers(users)
    
# 4. Only execute directly if called from the command line,
# using the URL parameter
if __name__ == '__main__':
    main(sys.argv[1])