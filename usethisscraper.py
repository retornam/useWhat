from BeautifulSoup import BeautifulSoup as soup
import csv
import requests
import soupselect; soupselect.monkeypatch()


def scraper():
    '''
        This script scrapes http://usesthis.com/interviews/
        for each interview, saves  the interviewees name,
        product name, product description, link to  the product
        to a csv file named everyone.csv
    '''
    outputFile = open('everyone.csv', 'a')
    scrapecount = 0
    response = requests.request('get', 'http://usesthis.com/interviews/')
    html = soup(response.text)
    interviewLinks = html.findSelect('#interviews li h2 a')
    linkLength = len(interviewLinks)
    while scrapecount < (linkLength):
        response = requests.request('get', interviewLinks[scrapecount]['href'])
        html = soup(response.text)
        person = html.findSelect('.person')[0].text
        product = html.findSelect('#contents article.contents p a')
        productLength = len(product)
        csvWriter = csv.writer(outputFile)
        for x in range(0, productLength, 1):
            try:
                print person, product[x].text, product[x]['title'], product[x]['href']
                csvWriter.writerow([person, product[x].text, product[x]['title'], product[x]['href']])
            except Exception as e:
                print '%s, %s, %s, %s' % ('Exception', 'Exception', 'Exception', e)
        scrapecount += 1
scraper()
