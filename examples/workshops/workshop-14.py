# Example realisation of workshop #14.
# Of course there are multiple ways of doing this.

# This program can be loaded directly, or imported in another module.
# If loaded directly, it accepts a country name to 
# search for as command line parameter.

# 1. import libraries

import requests
import sys

# 2. The endpoint URL to talk to
urlName = 'https://restcountries.com/v3.1/name/'

# 3. Getting countries, based on URL + name
def getCountries(name):    
    response = requests.get(urlName + name)
    return response.json()

# 4. Print the found countries
def printCountries(countries):  
    for country in countries:
        print(country['name']['common'])

# 5. main() function which is called from command line or from enclosing module/application.
def main(name):
    countries = getCountries(name)
    printCountries(countries)

if __name__ == '__main__':
    main(sys.argv[1])
