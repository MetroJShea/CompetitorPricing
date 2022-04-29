import requests
import cloudscraper
from bs4 import BeautifulSoup
import re

katomskus = (
    'FF2448C',
    'FF2448G',
    'FF2448SSS',
    'FPS2448VNGN',
    'FG074C',
    'FGN074C',
    'FG074G',
    'FGN074G',
    'FG074SS',
)
regex = re.compile('\$\d+(?:\.\d+)?')
for sku in katomskus:
    
    url = f'https://www.katom.com/search?w={sku}'
    scraper = cloudscraper.create_scraper()
    html = scraper.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    
    try:
        price = soup.select_one('strong[class="kPrice"]').text
        print(price)
    except:
        print(f'{sku} not found')
    
    
    
    
    
    
    # url = 'https://www.google.com/search'

    # param = {'q' : f'{sku}'}
    # req = requests.get(url, params = param)
    # html = req.text
    # soup = BeautifulSoup(html, 'lxml')
    # print(regex.findall(html)[0])


#<span class="xUrNXd UMOHqf">$43.71</span>