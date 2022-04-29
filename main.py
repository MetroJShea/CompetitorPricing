import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date
import re
import cloudscraper




output = {'SKU': [], "Price": [], "Site":[], "Date":[]}

#___________________________GLOBAL  INDUSTRIAL___________________________
print('checking global industrial')

giskus = (
    'S2448C',
    'P74C',
    'S2448Z',
    'P74Z',
    'S2448N',
    'P74N',
    'S2448S',
    'P74S',
    'S2448SS',
 )

for sku in giskus:
    url = 'https://www.globalindustrial.com/searchResult'

    req = requests.get(url, {'q':{sku}}).text
    soup = BeautifulSoup(req, 'lxml')

    price = soup.select_one('p[class="price"]')
    price = price.text.replace(" ", '').replace('\n', '').replace('\t', '')
    output['SKU'] += [sku]
    output['Price']+=[price]
    output['Site'] += ['Global Industrial']
    output['Date'] += [date.today()]


#______________________WEBSTAURANT___________________________
print('checking webstaurant')
webstaurantskus = (
    '460EC2448',
    '460ECP74',
    '460EG2448',
    '460EGP74',
    '460SW2448',
    '460SSP74',
    '2448C',
    '2448V',
    '2448E',
    '2448S',
    'P74-C',
    'P74-E',
    'P74-V',
    '2448NC',
    '74P',
    '2448NK3',
    '74PK3',
    '2448NS',
    '74PS',
    '2448FS',
)

for sku in webstaurantskus:
    url = f'https://www.webstaurantstore.com/search/{sku}.html'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    price = soup.select_one('p[data-testid="price"]')
    output['SKU'] += [sku]
    output['Site'] += ['Webstaurant']
    output['Date'] += [date.today()]
    found = False
    try:        
        price = price.text.replace('From', '').replace('/Each', '').replace(' ', '')
        output['Price']+=[price]
        found = True
    except:
        if not found:
            price = soup.select_one('p[class="price"]')      
            try:        
                price = price.text.replace('From', '').replace('/Each', '').replace(' ', '')
                output['Price']+=[price]
                found = True
            except:
                
                output['Price']+=['Not found']  
        
    


#________________________ULINE____________________________________

ulineskus = {
    'H-3187C': 'https://www.uline.com/Product/Detail/H-3187C/Wire-Shelving-Accessories/Additional-Chrome-Wire-Shelves-48-x-24?keywords=h-3187c',
    'H-6797C':'https://www.uline.com/Product/Detail/H-6797C/Wire-Shelving-Accessories/Post-for-Chrome-Wire-Shelving-72?keywords=H-6797C',
    'H-6781G': 'https://www.uline.com/Product/Detail/H-6781G/Industrial-Wire-Shelving/Additional-Epoxy-Wire-Shelves-48-x-24-Green?keywords=H-6781G',
    'H-4799' : 'https://www.uline.com/Product/Detail/H-4799/Industrial-Wire-Shelving/Additional-Stainless-Steel-Wire-Shelves-48-x-24?keywords=H-4799',
    'H-5469-SHELF': 'https://www.uline.com/Product/Detail/H-5469-SHELF/Industrial-Wire-Shelving/Additional-Solid-Stainless-Steel-Shelves-48-x-24?keywords=H-5469-SHELF'

}



print('checking Uline')
regex = re.compile("'productPrice': '[0-9]+'")
for sku in ulineskus:
    url = ulineskus[sku]
    req = requests.get(url)
    output['SKU'] += [sku]
    output['Site'] += ['ULine']
    output['Date'] += [date.today()]
    try:        
        price= str(regex.findall(req.text)[0]).replace("'productPrice': ", '').replace(' ', '').replace("'", '')        
        output['Price']+=[price]
    except:
        output['Price']+='Not Found'


#_____________KATOM________________________
print('Checking Katom')
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

for sku in katomskus:
    
    url = f'https://www.katom.com/search?w={sku}'
    scraper = cloudscraper.create_scraper()
    html = scraper.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    output['SKU']+=[sku]
    output['Date']+=[date.today()]
    output['Site']+=['Katom']
    try:
        price = soup.select_one('strong[class="kPrice"]').text
        output["Price"]+=[price]
    except:
        output["Price"]+=['Not Found']
    

#________________________GRAINGER___________________
print('Checking Grainger')
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
    output['SKU'] += [sku]
    output['Site'] += ['Grainger']
    output['Date'] += [date.today()]
    try:
        price = query.text.replace(" ", '').replace('\n', '')
        output['Price']+=[price]
    except:
        output['Price']+=['Not Found']

df = pd.DataFrame(output)

df.to_csv('Competitor Pricing.csv', index=False)