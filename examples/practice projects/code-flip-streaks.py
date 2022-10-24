# P. 107, 'coin flip streaks', from 'Automate the boring stuff with Python', Seigwart.
# ***************************************
# Assignment: Write a program to find out how often a
# streak of six heads or a streak of six tails comes
# up in a randomly generated list of heads and tails.
# Your program breaks up the experiment into two parts:
# - the first part generates a list of randomly selected 'heads' and 'tails' values,
# - the second part checks if there is a streak in it.
# Put all of this code in a loop that repeats the experiment
# 10,000 times so we can find out what percentage of the coin flips
# contains a streak of six heads or tails in a row.
# ***************************************
from random import randint

num_experiments = 10000
num_flips = 1000
num_streaks = 0
for _ in range(num_experiments):
    flips = ''.join([str(randint(0, 1)) for _ in range(num_flips)])
    if '111111' in flips or '000000' in flips:
        num_streaks += 1

print(' percentage: ', 100.0 * num_streaks / num_experiments)

# Some Explanation (PK):
# - using 3 variables
# - using _ as a loop variable that is not used, e.g. can be ignored. More info: https://www.datacamp.com/tutorial/role-underscore-python.
# - using randint() to generate a 0 (heads) or 1 (tail). 
# - using .join() to add this to a long string.
# - check if a series of 6 heads (111111) or tails (000000) is in the long string.
# - if yes, add 1 to the num_streaks variable
# - in the end, calculate the percentage in what number of ranges the series occur.

# You will typically find:
# if num_flips is a low number (say: 10), we get a low percentage. For instance: 9.0. 
# This means that if we flip a coin 10 times, in only 9% of the tries we get a streak of 6 heads or 6 tails.

# if num_flips is bigger (say: 100 ), we get a bigger percentage. For instance: 80.45.
# This means that if we flip a coin 100 times, in 80.45% of the tries we get a streak of 6 heads or 6 tails.

# if num_flips is really big (say: 1000 ), we almost always get 100%.
# This means that if we flip a coin 1000 times, in all of the tries we get at least once a streak of 6 heads or 6 tails.

