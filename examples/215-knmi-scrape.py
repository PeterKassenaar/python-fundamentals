# knmi-scrape.py - we can open the weather forecast page from knmi.nl
# and read ('scrape') the text of the forecast for next week from the page.

# 0. Import the correct modules
import requests, bs4

# 1. Try
try:
    # 1a. Make request
    res = requests.get('https://www.knmi.nl/nederland-nu/weer/verwachtingen')
    res.raise_for_status()  # always call this!
    # 1b. parse the results in knmi variable
    knmi = bs4.BeautifulSoup(res.text, 'html.parser')

    # 1c. Select correct element(s)
    elements = knmi.select('#weather > div:nth-child(2) > div.col-sm-12.col-md-7 > p.margin-top-0')

    # 1d. In this case: print the number of elements and text of the first element
    print('num elements: {}'.format(len(elements)))
    print('text elements: {}'.format(elements[0].getText()))

    # 1e. Some other examples of what we can do with the response bs4-object
    print(knmi.title.getText()) # KNMI - Weer - Verwachtingen
    print(elements[0].attrs) # {'class': ['margin-top-0']}
    print(elements[0].attrs.get('class')) #  ['margin-top-0']
    print('number of links in this page: ', len(knmi.find_all('a'))) # 65 (at the time of writing of this page)

except Exception as ex:
    print('Oh no! Something went wrong: ', ex)


    #content > div.body > div > ul > li:nth-child(11) > a > span.cell.content > span.title
