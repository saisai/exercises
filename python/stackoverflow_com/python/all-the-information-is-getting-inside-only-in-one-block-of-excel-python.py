
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://virtualhs.pwcs.edu/about/faculty'
res = requests.get(url)

soup = BeautifulSoup(res.content, 'html.parser')
departments = soup.find_all('h3')

rows = []
for department in departments:
    for teacher in department.find_next('ul').find_all('li'):
        row = {
                'teacher': teacher.text,
                'department': department.text
                }
        rows.append(row)

df = pd.DataFrame(rows)
df.to_csv('now.csv', index=False)

