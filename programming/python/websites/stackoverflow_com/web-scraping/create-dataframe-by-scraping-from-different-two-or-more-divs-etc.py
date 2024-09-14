import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

headers =   {
    'accept':'*/*',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    }

url = 'https://www.racingtv.com/racecards/catterick-bridge/372180-watch-racing-tv-now-novices-hurdle-gbb-race?'

resp = requests.get(url,headers=headers)
print(resp)

soup = BeautifulSoup(resp.text,'html.parser')
table = soup.find('div',{'class':'page__content__section racecard'})

race_id = url.split('/')[-1].split('-')[0]
race_name = soup.find('div',class_='race__name').text.strip()
race_date = soup.find('div',class_='race__date').text.strip()
clean_date = datetime.strptime(race_date,'%d %b %Y').strftime('%Y%m%d')
race_info1 = soup.find_all('div',class_='race__subtitle')[0].text.strip()
race_info2 = soup.find_all('div',class_='race__subtitle')[1].text.strip()

final = []
for row in table.find_all('div',class_='racecard__runner--content'):
    try:
        num = row.find('div',class_='racecard__runner__cloth-number').text.strip()
        last_days_ugly = row.find('div',class_='racecard__runner__name').find('a').find('sup').text
        horse_name = row.find('div',class_='racecard__runner__name').find('a').text.strip().replace(last_days_ugly,'')
        horse_link = 'http://www.racingtv.com'+row.find('div',class_='racecard__runner__name').find('a')['href']
        last_race_days = last_days_ugly.strip().replace('(','').replace(')','')
        for people in row.find_all('div',class_='racecard__runner__person'):
            if 'J:' in people.getText():
                jockey = people.find('a').text.strip()
                jockey_link = 'http://www.racingtv.com'+people.find('a')['href']
            if 'T:' in people.getText():
                trainer = people.find('a').text.strip()
                trainer_link = 'http://www.racingtv.com'+people.find('a')['href']
        form = row.find('div',class_='racecard__runner__column--form_lr').find_all('div')[0].text.strip()
        equip = row.find('div',class_='racecard__runner__column--form_lr').find_all('div')[1].text.strip()
        weight = row.find('div',class_='racecard__runner__column--weight_age').find_all('div')[0].text.strip()
        age = row.find('div',class_='racecard__runner__column--weight_age').find_all('div')[1].text.strip()
        o_r = row.find('div',class_='racecard__runner__column--or').text.strip()
        odds = row.find('div',class_='racecard__runner__column--price').getText()
        odds_dec = row.find('div',class_='racecard__runner__column--price').find('ruk-odd')['data-js-odds-decimal']
        odds_data = row.find('div',class_='racecard__runner__column--price').find('ruk-odd')['data-js-odd-alternatives']

    except AttributeError: #skip blank starting gates
        continue

    item = {
        'race_url' : url,
        'race_id': race_id,
        'race_name':race_name,
        'race_date':clean_date,
        'race_info1':race_info1,
        'race_info2':race_info2,
        'num': num,
        'horse_name':horse_name,
        'horse_link':horse_link,
        'last_race_days':last_race_days,
        'jockey':jockey,
        'jockey_link':jockey_link,
        'trainer':trainer,
        'trainer_link':trainer_link,
        'form':form,
        'equip':equip,
        'weight':weight,
        'age':age,
        'o_r':o_r,
        'odds':odds,
        'odds_dec':odds_dec,
        'odds_data':odds_data
    }
    final.append(item)

df = pd.DataFrame(final)
df.to_csv('racingtv.csv',index=False)

print('Saved to racingtv.csv')
