# some tests. This page is not to be used on its own

import webbrowser
import requests
import bs4
import sys
import pyperclip

try:
    pass
    #  *************** KNMI
    # res = requests.get('https://www.knmi.nl/nederland-nu/weer/verwachtingen')
    # res.raise_for_status()  # always call this!
    # kassenaarFile = open('kassenaar.com.txt')
    # knmiSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    # elements = knmiSoup.select('p.margin-top-0')
    # print('num elements: {}'.format(len(elements)))

    # print('text elements: {}'.format(elements))

    # # print('attributes: {}'.format(el[0].attrs))
    # for i in range(len(elements)):
    #     print('Verwachting: {}'.format(elements[i].get_text()))

    # total_bytes = 0
    #  write to disk
    # with open('kassenaar.com.txt', 'wb') as playFile:
    #     for chunk in res.iter_content(10000):
    #         total_bytes += playFile.write(chunk)
    # print('total bytes written: {0}.'.format(total_bytes))

    #  *************** NOS
    # res = requests.get('https://nos.nl/')
    # res.raise_for_status() # always call this!
    # nosSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    # baseUrl = 'https://nos.nl'
    # elements = nosSoup.select('.sc-89385b10-0 span')
    # print('num elements: {}'.format(len(elements)))
    # links = nosSoup.select('.sc-89385b10-0 a')
    # print('num links: {}'.format(len(links)))
    # for i in range(len(elements)):
    #     print('text: {0}, link: {1}\n'.format(
    #         elements[i].getText(), links[i].get('href')
    #     ))
    #     # open webbrowser with article
    #     webbrowser.open(baseUrl + links[i].get('href') )
    #     # break if the maximum of 10 articles is reached
    #     if i > 9:
    #         break

    # *************** BOL.com - search for products
    # print('Search BOL.com and open first 10 results.')
    # keyword = input('What do you want to search for? ')
    # res = requests.get('https://www.bol.com/nl/nl/s/?searchtext=' + keyword)
    # res.raise_for_status()  # always call this!
    # bolSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    # baseUrl = 'https://bol.com'
    # elements = bolSoup.select('.product-title')
    # print('num elements: {}'.format(len(elements)))

    # for i in range(len(elements)):
    #     print('text: {0}, link: https://bol.com{1}\n'.format(
    #         elements[i].getText(), elements[i].get('href')
    #     ))
    #     # open webbrowser with result
    #     webbrowser.open(baseUrl + elements[i].get('href'))
    #     # break if the maximum of 10 products is reached
    #     if i > 9:
    #         break

    # ********************* Funda - search for houses: not
    # possible using webbrowser.open(), site is prevented from scraping
    # baseUrl = 'https://www.funda.nl/koop/'
    # if(len(sys.argv) > 1):
    #     # a keyword is provided via command line
    #     keyword =''.join(sys.argv[1:])
    # else:
    #     # get keyword from clipboard
    #     keyword = pyperclip.paste()

    # if len(keyword) == 0:
    #     keyword = '7201' # fallback keyword if none provided via command line or clipboard

    # # Open web browser
    # webbrowser.open(baseUrl + keyword)
except Exception as ex:
    print('There was a problem: %s' % ex)
