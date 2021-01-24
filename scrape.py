# Simple scraping of quotes website.

import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"

# Response contains the html of the requested page
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

for i in range(len(quotes)): 
    print(quotes[i].text)
    print(authors[i].text)
    for tag in tags[i].find_all('a', class_='tag'):
        print(tag.text)