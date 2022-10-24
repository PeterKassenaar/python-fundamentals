# Optional Workshop - appending text to a file
from os import path
import sys

# UI instructions
print('Enter a filename to work with::')
fileName = input()

# Check if file exists
if path.exists(fileName):
    handle = open(file=fileName, mode='at', encoding='utf-8')
else:
    handle = open(file=fileName, mode='wt', encoding='utf-8')

# UI instructions
print('Enter text to append to the file. Press Enter after every line.')
print('Enter "quit" to exit the program.')

# User input & adding to file
while True:
    textToAppend = input()
    if (textToAppend.lower() == 'quit'):
        sys.exit()
    else:
        handle.write(textToAppend + '\n')  # Append newline yourself!
