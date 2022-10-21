# collatz sequence or -conjecture
# One of the most famous, unsolved problems in mathematics.
# More info: https://en.wikipedia.org/wiki/Collatz_conjecture

# 1. collatz() function
# If number is even, divide by 2 and return
# If number is odd, multiply by #, add 1 and return
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return (number * 3) + 1


# 2. Main program
print('Enter a positive number, it will be used in the collatz conjecture.')
print('For more information, see https://en.wikipedia.org/wiki/Collatz_conjecture')
print('Your number: ')

try:
    # 3. variables
    totalSteps = 0
    value = int(input())

    # 4. check correct input, otherwise raise
    if value > 0:
        calculatedValue = collatz(value)
    else:
        raise ValueError

    # 5. run until the sequence reaches 1
    while calculatedValue != 1:
        print(calculatedValue)
        calculatedValue = collatz(calculatedValue)
        totalSteps += 1

    # 6. we're done
    print(calculatedValue, ': the end')
    print('Total steps: ', totalSteps)

# 7. Catch errors
except ValueError:
    print('Sorry, invalid input. Please enter a valid, positive (integer) number.')
