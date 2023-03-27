#import re
import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree



page = requests.get('http://10.160.2.16/readings.htm', auth=('admin', 'Admin'))
soup = BeautifulSoup(page.content, 'lxml')

mydivs = soup.find(id='llpopup', attrs={"class": "first_secondrow_cell"})

#results = soup.find(id='ll-popup-context'.text)
#job_elements = results.find_all("div", class_="ll-popup-context")
#v = soup.findAll('tr')
#data = soup.find("div", {"class":"menu_width", "id":"instrument_values"})
#print(data)
#title = soup.title
#print(title.text)
#print(page.text)
#print(job_elements)
#print(mydivs)
#print(v)

