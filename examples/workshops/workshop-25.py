# Reading configuration data from a file and using it in a program.
# In this case we read a name and URL from a file and fetch data from the URL.
import requests

# 1. Try Reading configuration info from file
try:
    settings = {}
    # 2. Open the file and store contents
    with open(file='url.config', mode='rt', encoding='utf-8') as config:
        for i in config.readlines():
            key, value = i.split('=')        
            settings[key] = value.replace('\n', '')      
    # 3. Variables
    url = settings['url']
    name = settings['name']

    # 4. Make request to external API
    response = requests.get(url)

    # 5. Print a list of users
    print ('Users from {0}: '.format(name))
    users_json = response.json()
    for user in users_json:
        print (user['id'] , ':', user['name'], '(',user['company']['name'],')') 
# 6. Simply catch all exceptions. 
# Of course you can split this out in file/IO exceptions, ValueErrors and so on.
except Exception as err:
    print('Oh no, something bad happened! :: ', err)
