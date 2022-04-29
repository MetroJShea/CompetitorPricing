import requests
import cloudscraper
from bs4 import BeautifulSoup

graingerskus = (
    '5GRY9',
    '5GTD9',
    '2448C',
    'P74C',
    '2448S',
    'P74S-2',
    '21Z811',
    '22A713',
    '21Z842',
    '22A721',
    '22A230',

)

for sku in graingerskus:
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    param = {'searchQuery': f'{sku}', 'searchBar': 'true'}
    req = requests.get('https://www.grainger.com/search', params = param, headers = header, timeout=10)
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    query = soup.select_one('span[class="pricing__price"]')
    print(query.text.replace(" ", '').replace('\n', ''))

