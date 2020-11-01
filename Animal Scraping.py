import requests
from bs4 import BeautifulSoup

html = requests.get('https://lib2.colostate.edu/wildlife/atoz.php?sortby=Common_Name&letter=ALL', verify=False).text
soup = BeautifulSoup(html, 'html.parser')
for div in soup.find_all('div', {'class': 'tab'}):
    for tr in div.find_all('tr'):
        print(tr.text.strip())