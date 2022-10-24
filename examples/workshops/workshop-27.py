from fileinput import filename
from os import path
import sys

print('Enter a filename to work with::')
fileName = input()
if path.exists(fileName):
    handle = open(file=fileName, mode='at', encoding='utf-8')
else:
    handle = open(file=fileName, mode='wt', encoding='utf-8')

print('Enter text to append to the file. Press Enter after every line.')
print('Enter "quit" to exit the program.')
while True:
    textToAppend = input()
    if (textToAppend.lower() == 'quit'):
        sys.exit()
    else:
        handle.write(textToAppend + '\n')
