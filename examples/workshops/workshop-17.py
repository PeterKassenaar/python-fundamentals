# Workshop 17
# Create a function that takes a list of numbers as its parameter
# Calculate:
#   The sum of the list
#   The average of the list
#   The minimum value in the list
#   The maximum value in the list
# Return the outcome from the function as a tuple
# Deconstruct/unpack the values and print them to the screen

listNumbers = [24, 45, 18, 87, 54, 66, 29, 38, 47, 24, 56, 61, 19, 21, 22, 24, 45]
def calculate(numbers):
    # 1. Calculate sum
    sum = 0
    for number in numbers:
        sum += number
    
    # 2. Calculate average
    average = sum / len(numbers)

    # 3. Minimum value
    minValue = min(listNumbers)

    # 4. Maximum value
    maxValue = max(listNumbers)

    # 5. Return a tuple with the outcome(s)
    return (sum, average, minValue, maxValue)

# *************************
# 6. Using the function
# *************************
(s, a, smallest, biggest) = calculate(listNumbers)
print('Sum = ', s)
print('Average = ', a)
print('Minimum value = ', smallest)
print('Maximum value = ', biggest)