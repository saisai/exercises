import requests

s = requests.Session()

headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    }
home = 'https://www.utahrealestate.com/search/map.search'
step = s.get(home,headers=headers)

headers =   {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Host':'www.utahrealestate.com',
    'Origin':'https://www.utahrealestate.com',
    'Referer':'https://www.utahrealestate.com/search/map.search',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
    }

for page in range(1,5):
    url = f'https://www.utahrealestate.com/search/map.inline.results/pg/{page}/sort/entry_date_desc/paging/0/dh/862'
    data = s.post(url,headers=headers).json()
    results = len(data['listing_data'])
    print(data['html'])
    print(f'Scraped {results} results from page {page}')
