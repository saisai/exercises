import time
import random

import requests
from bs4 import BeautifulSoup
import aiohttp
import asyncio

data = open('data.txt', encoding='utf-8')

soup = BeautifulSoup(data, 'html.parser')

host = 'http://rosettacode.org'

links = []
for result in soup.find_all('li'):
    url = host + result.find('a').get('href')
    links.append(url)

#print(links)
#data = requests.get('http://rosettacode.org/wiki/I_before_E_except_after_C')
#print('Batch File' in data.text)

#i = 0
#for d in random.sample(links, 15):
    #if i >= 10:
        #break
    #print(d)

def test():
    for link in random.sample(links, 10):
        
        data = requests.get(link)
        if 'Batch File' in data.text:
            print(link)
        time.sleep(5)

test()
