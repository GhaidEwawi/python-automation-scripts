# Scraping a website that have multiple pages

from bs4 import BeautifulSoup
import requests

url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
for index, i in enumerate(items):
    itemName = i.find('h4', class_='card-title').text.strip('\n')
    itemPrice = i.find('h5').text
    print(f'{index+1} Price: {itemPrice}, Item Name: {itemName}')

pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')

count = 1
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum is not None:
        x = link.get('href')
        urls.append(x)

    print(urls)
    for i in urls:
        newUrl = url + i
        response = requests.get(newUrl)
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for i in items:
            itemName = i.find('h4', class_='card-title').text.strip('\n')
            itemPrice = i.find('h5').text
            print(f'{count} Price: {itemPrice}, Item Name: {itemName}')
            count += 1