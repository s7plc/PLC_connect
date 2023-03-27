import requests
from bs4 import BeautifulSoup


page = requests.get('https://ya.ru/')

soup = BeautifulSoup(page.content, "html.parser")

usd = soup.find('span', class_='DFlfde SwHCTb')

print(soup)
