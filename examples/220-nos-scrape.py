# nos-scrape.py -open the frontpage of NOS.nl (a large Dutch news site)
# and read ('scrape') the righthand columns with latest news articles.
# Get all links and text in a list and open each article in a new browser tab

import bs4, webbrowser, requests
try:
    # 1. Make request
    res = requests.get('https://nos.nl/')
    res.raise_for_status()  # always call this to raise an error if something went wrong!

    # 2. Save and parse response in a variable
    nos = bs4.BeautifulSoup(res.text, 'html.parser')
    baseUrl = 'https://nos.nl'

    # 3. Select the correct elements. CHECK in Chrome DevTools if this is not working.
    # NOS might have changed their classnames or element order. Always make sure your
    # scraping program is up-to-date.
    elements = nos.select('.sc-89385b10-0 span')
    print('num elements: {}'.format(len(elements)))
    links = nos.select('.sc-89385b10-0 a')
    print('num links: {}'.format(len(links)))

    # calculate tabs to open. Maximum 10, but less if len(elements) is smaller.
    tabsToOpen = min(10, len(elements))
    for i in range(tabsToOpen):
        print('text: {0},\n link: {1}\n'.format(
            elements[i].getText(), links[i].get('href')
        ))
        # open webbrowser with article
        webbrowser.open(baseUrl + links[i].get('href'))

except Exception as ex:
    print('Oh no! Something went wrong: ', ex)
