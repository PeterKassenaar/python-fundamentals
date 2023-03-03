from fileinput import filename
import webbrowser
import requests
import bs4
import sys
import pyperclip

try:
    # 1. UI instructions for the user
    print('Search BOL.com and open first 10 results.')
    keyword = input('What do you want to search for? ')
    print('Searching...')

    # 2. Get the results
    res = requests.get('https://www.bol.com/nl/nl/s/?searchtext=' + keyword)
    res.raise_for_status()

    # 3. Parse the HTML
    bolcom = bs4.BeautifulSoup(res.text, 'html.parser')
    baseUrl = 'https://bol.com'

    #  4. Get the found elements and their prices
    elements = bolcom.select('.product-title')
    prices = bolcom.select('meta[itemprop]')
    print('Number of found items: {}'.format(len(elements)))

    # 5. If the search DID NOT return elements, the list with prices is empty.
    # Check for that.
    if prices == []: # (or simply, if not prices:... )
        print('Sorry, could not find results for "{0}"'.format(keyword))
    else:
        # 6. We have results. Print them to screen and save to file
        fileName = keyword + '_prices.txt'
        with open(fileName, mode='wt', encoding='utf-8') as file:
            # 7. Use only the first 10 found items/producs. Adjust if you want more.
            items = min(10, len(elements))
            #  8. Write header to file
            file.write('Title, Price\n')

            # 9. Print items to screen and save title and price to file
            for i in range(items):
                print('{0}. {1}, https://bol.com{2}, EUR {3}.\n'.format(
                    i,
                    elements[i].getText(),
                    elements[i].get('href'),
                    prices[i].attrs['content']
                ))
                file.write('{0}, {1}\n'.format(
                    elements[i].getText().replace(',', ''), # strip out possible comma's in the title, as we want to save a CSV-like format!
                    prices[i].attrs['content']
                ))
            # 10. Show confirmation to the user
            print('File saved to disk: {0}'.format(fileName))

# 11. Catch if something went wrong.
except Exception as ex:
    print('Oh nooo! There was a problem: {0}'.format(ex))
