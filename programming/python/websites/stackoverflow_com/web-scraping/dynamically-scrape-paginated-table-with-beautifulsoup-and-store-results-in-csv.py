import requests,time,random
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
url = 'https://aviation-safety.net/wikibase/'
req = requests.get(url , headers = headers)
soup = BeautifulSoup(req.text, 'html.parser')


data = []

for url in ['https://aviation-safety.net/'+a['href'] for a in soup.select('a[href*="/wikibase/dblist.php"]')]:
    while True:

        html = requests.get(url, headers = headers)
        soup = BeautifulSoup(html.text, 'html.parser')

        data.append(pd.read_html(soup.prettify())[0])

        # If more than one page then iterate through all of them        
        if soup.select_one('div.pagenumbers span.current + a'):
            url = 'https://aviation-safety.net/wikibase/dblist.php'+soup.select_one('div.pagenumbers span.current + a')['href']
        else:
            break
        time.sleep(random.random())

df = pd.concat(data)
df.loc[:, ~df.columns.str.contains('^Unnamed')].to_csv('aviation-safety.csv', index=False)

