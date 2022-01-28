import requests
import pandas as pd

headers =   {
    'accept':'application/json, text/javascript, */*; q=0.01',
    'accept-encoding':'gzip, deflate, br',
    'referer':'https://www.brilliantearth.com/lab-diamonds-search/',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'x-requested-with':'XMLHttpRequest'
    }

final = []
for page in range(1,10):
    print(f'Scraping page {page}')
    new_url = f'https://www.brilliantearth.com/lab-diamonds/list/?page={page}&shapes=Round&cuts=Fair%2CGood%2CVery%20Good%2CIdeal%2CSuper%20Ideal&colors=J%2CI%2CH%2CG%2CF%2CE%2CD&clarities=SI2%2CSI1%2CVS2%2CVS1%2CVVS2%2CVVS1%2CIF%2CFL&polishes=Good%2CVery%20Good%2CExcellent&symmetries=Good%2CVery%20Good%2CExcellent&fluorescences=Very%20Strong%2CStrong%2CMedium%2CFaint%2CNone&min_carat=0.30&max_carat=8.18&min_table=45.00&max_table=82.50&min_depth=5.00&max_depth=85.80&min_price=350&max_price=128290&stock_number=&row=0&requestedDataSize=200&order_by=price&order_method=asc&currency=%24&has_v360_video=&dedicated=&min_ratio=1.00&max_ratio=2.75&exclude_quick_ship_suppliers=&MIN_PRICE=350&MAX_PRICE=128290&MIN_CARAT=0.3&MAX_CARAT=8.18&MIN_TABLE=45&MAX_TABLE=82.5&MIN_DEPTH=5&MAX_DEPTH=85.8'
    resp = requests.get(new_url,headers=headers).json()

    for diamond in resp['diamonds']:
        diamond.pop('v360_src',None) #remove long video and images links to clean up csv
        diamond.pop('images',None)
        final.append(diamond)

df = pd.DataFrame(final)
df.to_csv('diamonds.csv',encoding='utf-8',index=False)
print('Saved to diamonds.csv')
