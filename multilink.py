#! python 3
# multilink code meant to open up sereval links of a search result in new tabs

import bs4
import sys
import requests
import webbrowser


print("googling.....")  # display text while googling
term = requests.get("https://google.com/search?q=" + " ".join(sys.argv[1:]))
term.raise_for_status()

# retrieve top search results links

soup = bs4.BeautifulSoup(term.text)
linkElem = soup.select(".r a")

# looping through tabs to open each link

numlink = min(5, len(linkElem))
for i in numlink:
    webbrowser.get("https://google.com" + linkElem[i].get("href"))
