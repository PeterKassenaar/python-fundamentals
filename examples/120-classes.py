# classes.py - some examples on classes
# Using classes in Python is absolutely not mandatory,
# but can be helpful in certain situations. For instance
# if the built-in types (list, tuples, string, etc) are not
# flexible enough.
# Beware however that you don't make your code overly complex!

# 1. definition of a class
class Person:
    # 2. Private variable
    _name = ''

    # 3. __init__ (e.g. 'constructor' of the class)
    def __init__(self, name, age, email, hair='brown'):
        self._name = name
        self.age = age
        self.email = email
        self.hair = hair

    # 4. Getter and setter for the private variable
    def getName(self):
        return self._name

    def setName(self, newName):
        self._name = newName

    # 5. Class method
    def sayHello(self):
        return 'Hello, my name is {0}!'.format(self._name)


# 6. Instantiation of a class. NOTE: No keyword 'new'
person = Person('Peter', email='test@test.com', age=12)
print(person.getName())
print(person.sayHello())
print('My hair is' + person.hair)

# 7. Another person
person2 = Person(name='Sandra',
                 age=12,
                 email='sandra@sandra.com',
                 hair='Blond')
print(f'{person2._name}\'s hair is {person2.hair}')

# 8. Check the type of the variable
print(type(person2))