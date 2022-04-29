import requests
from bs4 import BeautifulSoup
import json
from datetime import date

import re

ulineskus = {
    'H-3187C': 'https://www.uline.com/Product/Detail/H-3187C/Wire-Shelving-Accessories/Additional-Chrome-Wire-Shelves-48-x-24?keywords=h-3187c',
    'H-6797C':'https://www.uline.com/Product/Detail/H-6797C/Wire-Shelving-Accessories/Post-for-Chrome-Wire-Shelving-72?keywords=H-6797C',
    'H-6781G': 'https://www.uline.com/Product/Detail/H-6781G/Industrial-Wire-Shelving/Additional-Epoxy-Wire-Shelves-48-x-24-Green?keywords=H-6781G',
    'H-4799' : 'https://www.uline.com/Product/Detail/H-4799/Industrial-Wire-Shelving/Additional-Stainless-Steel-Wire-Shelves-48-x-24?keywords=H-4799',
    'H-5469-SHELF': 'https://www.uline.com/Product/Detail/H-5469-SHELF/Industrial-Wire-Shelving/Additional-Solid-Stainless-Steel-Shelves-48-x-24?keywords=H-5469-SHELF'

}
output = {'SKU': [], "Price": [], "Site":[], "Date":[]}
regex = re.compile("'productPrice': '[0-9]+'")
for sku in ulineskus:
    print(sku)
    url = ulineskus[sku]
    req = requests.get(url)
    output['SKU'] += [sku]
    output['Site'] += ['ULine']
    output['Date'] += [date.today()]
    try:        
        price= str(regex.findall(req.text)[0]).replace("'productPrice': ", '').replace(' ', '').replace("'", '')
        print(price)
        output['Price']+=[price]
    except:
        output['Price']+='Not Found'



for i in output:
    print(i)
    print(len(output[i]))