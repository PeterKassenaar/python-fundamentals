# Command Line Arguments
# Restructuring the code from 60-api-data.py, so that:
# - we can call this module from the REPL
# - we can import it in another file
# - we can pass the url in as a parameter

import requests

# 1. break the code up into different functions
url = 'https://jsonplaceholder.typicode.com/users'

# 2. Getting the data
def getData(url):
    response = requests.get(url)
    return response.json()

# 3. Printing the users
def printUsers(users):
    print('List of users: ')
    for user in users:
        print(user['id'], ':', user['name'], '(', user['company']['name'], ')')

# 4. Only execute directly if called from the command line
if __name__ == '__main__':
    users = getData(url)
    printUsers(users)
