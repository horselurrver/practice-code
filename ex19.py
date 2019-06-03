import requests
from bs4 import BeautifulSoup
url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
soup = BeautifulSoup(r.text)
print(soup.find_all('p'))

for line in soup.select('p[data-reactid]'):
    print(line.get_text())
