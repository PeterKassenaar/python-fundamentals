#  workshop 22- getting the same dummy user data as in previous examples,
#  but now assigning the returned value to classes

import uuid  # for generating unique, random id's, see https://bobbyhadz.com/blog/python-generate-unique-id for details
import requests

# 0. Our classes - we only implement the
#  returned data partially (e.g. not every field)
class Address:
    # TODO: create a class for addresses and add it as a property to the Person class
    pass


class Person:

    def __init__(self, name, email, website, company):
        self.name = name
        self.email = email
        self.website = website
        self.company = company
        self._id = uuid.uuid4() # generate random, unique ID for every user  

    def getId(self):
        return self._id
    # more methods...


# 1. Variables
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

# 2. We should use try-except here, but omitting that for brevity.
users_json = response.json()
users_list: list[Person] = [] # We're using static typing here! We say 'users_list is of type list with Person objects'
for user in users_json:
    # 3. We have to add a Person object to the list of users
    newUser = Person(
        name=user['name'],
        email=user['email'],
        website=user['website'],
        company=user['company']['name']        
    )
    # omitting the rest of the returned properties here, 
    # and append the user to the list.
    users_list.append(newUser)
    

# 3. Printing the list of users. Because we used static typing
# on line 37, we get intellisense on the properties.
for user in users_list:    
    print('{0} - {1}, {2}, ({3})\n'
            .format(user.getId(), user.name, user.email, user.company))
    # Optional: using the prettyprint-package, pprint, or pp. Look this up for yourself!

