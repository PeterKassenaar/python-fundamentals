# 210-webbrowser-save.py - We can save a webpage to disk, using the 
# requests package.

import webbrowser, pyperclip, sys

baseUrl = 'https://www.bol.com/nl/nl/s/?searchtext='
if(len(sys.argv) > 1):
    # a keyword is provided via command line
    keyword = ' '.join(sys.argv[1:])
else:
    # get keyword from clipboard
    keyword = pyperclip.paste()

if len(keyword) == 0:
    keyword = 'Pirates of the Carribean' # fallback keyword if none provided via command line or clipboard

# ****************************
# Using requests here 
# ****************************
import requests
try:
    res = requests.get('https://www.bol.com/nl/nl/s/?searchtext=' + keyword)
    res.raise_for_status()  # always call this!
    # Save the result to a file, using the keyword as the filename
    newFile = open(keyword+ '.html', mode='wb')
    numBytes = 0
    for chunk in res.iter_content(100000):
        numBytes += newFile.write(chunk)        
    print('Request successful, total bytes written: {0}.'.format(numBytes))
except Exception as ex:
    print('Oh no! Something went wrong: ', ex)


# Open web browser with the results page
webbrowser.open(baseUrl + keyword)
