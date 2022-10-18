# Command Line Arguments
# Defining a main() function that receives the url

import sys
import requests

# 1. break the code up into different functions - 
# URL is now passed from the command line
# url = 'https://jsonplaceholder.typicode.com/users'

# 2. Getting the data
def getData(url):
    response = requests.get(url)
    return response.json()

# 3. Printing the users
def printUsers(users):
    print('List of users: ')
    for user in users:
        print(user['id'], ':', user['name'], '(', user['company']['name'], ')')

def main(url):
    users = getData(url)
    printUsers(users)
    
# 4. Only execute directly if called from the command line,
# using the URL parameter
if __name__ == '__main__':
    main(sys.argv[1])