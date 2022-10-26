#! python3
# MapIt.py, from P. 268 'Automate the Boring stuff with Python', by Al Seigwart
#  Opening an address in Google Maps from the command line.
#********************************
# NOTE: It doesn't always work from VS Code directly. However, it works if 
# You open the program (Ctrl+F5) from another Terminal, or from the Debug Console. 
# Must have something to do with permissions or paths, but I don't understand why.

# It works fine when run from a command shell like Terminal or Powershell
#********************************

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # get address from command line
    address = sys.argv[1:]
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

# Similar idea: 'open several social network sites that you regularly check'
# addresses = [
#     'https://www.twitter.com',
#     'https://www.nos.nl',
#     'https://www.vanduurenmedia.nl'
# ]
# for address in addresses:
#     webbrowser.open(address)