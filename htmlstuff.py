import bs4
import requests


newfile = open("C:\\Users\\HP 15\\Desktop\\csscourse\\css cheetsheet\\index file.html")
example = bs4.BeautifulSoup(newfile.read())
elem = example.select(".container")

str(elem)

elem[0].get("href")
elem[0].attrs
