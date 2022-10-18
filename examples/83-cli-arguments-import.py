# cli-arguments-import.py. Importing the module that calls a url. 
# Pass in the url from this programm

# 1. Import the correct module
# We have to use  __import__ here, because the filename starts with a number
cli_arguments = __import__('82-cli-arguments')

# 2. call the main() function with the required parameter. It prints
# out the list of users, from our external/imported module.
cli_arguments.main('https://jsonplaceholder.typicode.com/users')
