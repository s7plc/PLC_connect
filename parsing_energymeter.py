#import re
import requests
from bs4 import BeautifulSoup

page = requests.get('http://10.160.2.16/readings.htm?sel=realtime_2').text
#html_text = requests.get(vgm_url, auth=('admin', 'Admin')).text
soup = BeautifulSoup(page, 'html.parser')


results = soup.find(id="updateStatus")

print(results)
print(page)