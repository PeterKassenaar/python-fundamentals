# P. 198: Practice Projects, Sandwich maker implemented as 'pizza-maker', from 'Automate the boring stuff with Python', Seigwart.
# ***************************
# Assignment: Write a program that asks users for their sandwich preferences.
# The program should use PyInputPlus to ensure that they enter valid input,
# such as:
# - Using InputMenu() for a pizza type ('small, medium large, wagon wheel' I made that up myself, PK)
# - using InputMenu() for a topping type ('margherita, pepperoni, mushroom, vegetables, doner, garlic' )
# - using InputYesNo() to ask if they want cheese
# - if so, using inputMenu() to ask for a chees type: cheddar, swiss, mozzarella.
# - using InputMenu() to ask if the want sides: potatowedges, icecream, chopsticks, softdrink
# - using InputInt() to as how many pizzas they want. Make sure this number is 1 or higher
#
# come up with a price for each of the options, and have your program display
# a total cost after the user enters their selection .
# More info on installing: https://pypi.org/project/PyInputPlus/

import pyinputplus as pyip

# Variables. We choose to store items as dicts. You can do it simpler if you want
pizza = {}
sizes = {
    'small': 6.95,
    'medium': 9.95,
    'large': 12.95,
    'wagon wheel': 15.95}
toppings = {
    'margeritha': 1.5,
    'pepperoni': 1.95,
    'mushroom': 1.5,
    'vegetables': 2.3,
    'doner': 2.8,
    'garlic': 2.2
}
cheese = {
    'cheddar': 1.45,
    'swiss': 1.80,
    'mozzarella': 2.40
}
sides = {
    'potatowedges': 4.10,
    'icecream': 4.95,
    'chopsticks': 1.95,
    'softdrink': 1.95
}
num_pizzas = 0
total_cost = 0.0

# ****************************
# Main program
# ****************************
print('Thank you for visiting Peter\'s Pizza Palace. How can we serve you today?')
# 1. Ask size
pizza_size = pyip.inputMenu(
    list(sizes.keys()),
    prompt='Please select your pizza size:\n',
    numbered=True)
choice = (pizza_size, sizes[pizza_size])
print('your choice', choice)
# if pyip.inputYesNo('Is this size correct? (Y/N) ') == 'yes': # refactor the code, so that a user can confirm every choice!
pizza['size'] = choice

# 2. Ask toppings
pizza_toppings = pyip.inputMenu(
    list(toppings.keys()),
    prompt='Please select your topping:\n',
    numbered=True)
choice = (pizza_toppings, toppings[pizza_toppings])
print('your choice', choice)
# if pyip.inputYesNo('Is this the correct topping? (Y/N) ') == 'yes':
pizza['topping'] = choice

# 3. Ask if they want extra cheese
if pyip.inputYesNo('Do you want extra cheese on your pizza? (Y/N) ') == 'yes':
    pizza_cheese = pyip.inputMenu(
        list(cheese.keys()),
        prompt='Pick your cheese:\n',
        numbered=True)
    choice = (pizza_cheese, cheese[pizza_cheese])
    print('your choice', choice)
    # if pyip.inputYesNo('Is this the correct cheese flavour? (Y/N) ') == 'yes':
    pizza['cheese'] = choice

# 4. Ask if they want a side dish
if pyip.inputYesNo('Do you want a side dish with this pizza? (Y/N) ') == 'yes':
    pizza_side = pyip.inputMenu(
        list(sides.keys()),
        prompt='Pick your side dish:\n',
        numbered=True)
    choice = (pizza_side, sides[pizza_side])
    print('your choice', choice)
    # if pyip.inputYesNo('Is this the correct side dish (Y/N) ') == 'yes':
    pizza['side'] = choice

# 5. Ultimately : ask how many pizzas they want
num_pizzas = pyip.inputInt(prompt='How many pizzas do you want? (1-99) ')


# Calculate total cost
for item in pizza:
    # this is the second item in the tuple, the cost
    total_cost += pizza[item][1]

print('COST per pizza:  {0:.2f} euro'.format(total_cost))
print('You ordered {0} pizzas, so that makes {0} x {1:.2f} = EUR {2:.2f}'.format(
    num_pizzas,
    total_cost,
    num_pizzas * total_cost
))
print('Thank you for your order!')
