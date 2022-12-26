import time
import random
from pathlib import Path

import requests
from bs4 import BeautifulSoup
import aiohttp
import asyncio

data = open('data.txt', encoding='utf-8')

soup = BeautifulSoup(data, 'html.parser')

host = 'http://rosettacode.org'

def generate_link():
    links = []
    with open('links.txt', 'w+', encoding='utf-8') as f:
        for result in soup.find_all('li'):
            url = host + result.find('a').get('href')
            #links.append(url)
            f.write(url)
            f.write('\n')


def test():
    tmp_file = Path('links.txt')
    if not tmp_file.is_file():
        print('no file')
        generate_link()
        
    links = [f.strip('\n') for f in open('links.txt', encoding='utf-8')]
    #print(links)
    
    for link in random.sample(links, 20):        
        data = requests.get(link)
        if 'Batch File' in data.text:
            print(link)
        time.sleep(5)
    
test()



#print(links)
#data = requests.get('http://rosettacode.org/wiki/I_before_E_except_after_C')
#print('Batch File' in data.text)

#i = 0
#for d in random.sample(links, 15):
    #if i >= 10:
        #break
    #print(d)