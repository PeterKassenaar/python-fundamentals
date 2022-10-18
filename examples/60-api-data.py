# api-data - example on how to talk to an external API
# and print the results to the screen.
# As an example we use the https://jsonplaceholder.typicode.com/users API for that.

# 0. Import the correct packages (remember to 'pip install requests' if you haven't done that yet)
import requests
import json

# 1. Variables
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

# 2. (Un)comment the next lines to see them in action
print(response.status_code)  # 200 - if everything went OK!
print(response.json())  # Print all data from the response - works, but unreadable

# 3. Print formatted json
# print(json.dumps(response.json(),sort_keys=False, indent=4 ))  # Print all data from the response - works, but unreadable

# 4. Print a list of users
# print ('List of users: ')
# users_json = response.json()
# for user in users_json:
#     print (user['id'] , ':', user['name'], '(',user['company']['name'],')')    
#     # 4a. same result (more or less) using string.format()
#     # print (str.format('{0}: {1}, works at: {2} ({3}) ', 
#     #     user['id'], user['name'], 
#     #     user['company']['name'], user['email']))
