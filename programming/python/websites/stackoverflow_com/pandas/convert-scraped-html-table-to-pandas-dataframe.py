import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.rijdendetreinen.nl/en/train-archive/2022-01-12/amsterdam-centraal'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')

columns = soup.find('div', class_='row header')
columns = columns.text.strip().split('\n\n')

tables = soup.find_all('div', class_='row service')
data = []
for table in tables:
    row = table.find_all('div', recursive=False)
    data.append([cell.text.replace('\n', '') for cell in row[:-1]] + [row[-1].find('span')['title']])

print(columns)
for idx, d in enumerate(data):
    if idx > 3:
        break
    print(d)

df = pd.DataFrame(data, columns=columns)
print(df)
