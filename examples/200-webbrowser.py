# 200-webbrowser - opening a webbrowser from code. 
# In this case the (Dutch) retailer site bol.com
# It reads an article, authorname or other keyword from the command line and 
# adds it to the base URL. If no keyword is provided, we
# copy the value from the clipboard using the pyperclip module.
# See https://pypi.org/project/pyperclip/ for more info.

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

# Open web browser
webbrowser.open(baseUrl + keyword)
