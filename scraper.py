from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://ikman.lk/en/ads/colombo/apartment-rentals'

page = requests.get(url)
print(page)

soup = BeautifulSoup(page.text, 'lxml')

lists = soup.find('ul', class_='list--3NxGO')
item = lists.find_all('div', class_='content--3JNQz')
tittles = lists.find_all('h2')
prices = lists.find_all('div', class_="price--3SnqI color--t0tGX")


for details in item:
    print(details.get_text())

for tittle in tittles:
    print(tittle.get_text())

for price in prices:
    print(price.get_text())
