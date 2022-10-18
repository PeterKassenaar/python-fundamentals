# Example realisation of workshop #11.
# Of course there are multiple ways of doing this.

# This code shows a list of Country names from the RESTCountries API in the console

# 1. import request library to easily fire HTTP-requests.
# More info: https://pypi.org/project/requests/

import requests
import json
# 2. Variables
url = 'https://restcountries.com/v3.1/all'
urlName = 'https://restcountries.com/v3.1/name/'
response = requests.get(url)


# Helper line, Print formatted json
# print(json.dumps(response.json(), sort_keys=False, indent=4))

# 3. Output
print('List of countries A-Z (we only print the first 20 names:')
countries = response.json()

i = 0
for country in countries:
    # Only print the first 20 countries. Remove this 
    # line if you want to see *all* countries
    if i < 20:
        print(country['name']['common'])
    i += 1
        
# ******************************
# Optional assignment:
# If you only want to see countries based on keyboard input
# ******************************
# print('Please type (part of) a country name to search for:')
# countryName = input()
# response = requests.get(urlName + countryName)
# countries = response.json()

# print('We found:')
# for country in countries:
#         print(country['name']['common'])
