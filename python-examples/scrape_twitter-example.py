"""scrape twitter example going to web page for twitter profile."""
# author: James Campbell
# date: 2015 06 02
# Date Updated: 3 July 2019
import urllib.request
import urllib.parse
import random
from bs4 import BeautifulSoup

useragents = ['Mozilla/5.0', 'Bandicout Broadway 2.4', 'Carls Crawler Critter 1.0',
              'Dirty Dungeon Diksearch 69', 'Internet Explorer but better']


def singlerando(listofterms):
    randomed = random.choice(listofterms)
    return randomed


def parseT(twitterpage):
    soup = BeautifulSoup(twitterpage, "lxml")  # create a new bs4 object from the html data loaded
    for script in soup(["script", "style"]):  # remove all javascript and stylesheet code
        script.extract()
    # get text
    tester = soup.find_all("p", class_="tweet-text")
    print(tester[1].text)
    exit()


def searchT(searchfor):
    randomuseragent = singlerando(useragents)  # select a random user agent from list
    headers = {'User-Agent': randomuseragent}  # get random header from above
    url = 'https://twitter.com/%s' % searchfor  # GOOGLE ajax API string
    search_response_pre = urllib.request.Request(
        url, None, headers)  # key to get the random headers to work
    search_response = urllib.request.urlopen(search_response_pre)
    search_results = search_response.read().decode("utf8")
    # print(search_results)
    parseT(search_results)


diction = []
subset = []
twitteruser = input('Enter twitter user: ')
searchT(twitteruser)
