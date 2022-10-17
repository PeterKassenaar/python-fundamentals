# for-loops.py - example of using for to
# loop over a collection (or: 'iterable sequence')

# 1. Iterating over a list
capitals = ['London', 'Paris', 'New York', 'Berlin', 'Tokyo']
for capital in capitals:
    print(capital)

# Works! In other languages, the temp variable capital is garbage collected
print(capital)

# 2. Iterating over a dict
song = {
    'artist': 'Madonna',
    'title': 'Like a virgin',
    'length': '4:44',
    'charts': 1
}
for key in song:
    print(key, ':', song[key])

# Workshop: create a new dict, iterate over all keys in the dict and print to the console
