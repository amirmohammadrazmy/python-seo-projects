import requests
from bs4 import BeautifulSoup
url = input("paste url here: ")
getpage= requests.get(url)

getpage_soup= BeautifulSoup(getpage.text, 'html.parser')

all_links= getpage_soup.findAll('a')

for link in all_links:
    print (link)
