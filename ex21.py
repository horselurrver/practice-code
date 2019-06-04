import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, features="html.parser")

spans = soup.find_all('span')
h2 = soup.find_all('h2')

results = []
for line in spans:
    if 'class' not in str(line):
        #print(line.get_text().strip())
        results.append(line.get_text().strip())
for line in h2:
    #print(line.get_text().strip())
    results.append(line.get_text().strip())

newset = set(results)

string = ''
for item in newset:
    if (len(item) > 0):
        string = string + item + '\n'

with open('ex21.txt', 'w') as open_file:
    open_file.write(string)
