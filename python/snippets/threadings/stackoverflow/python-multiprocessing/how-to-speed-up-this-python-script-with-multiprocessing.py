import pandas as pd
import multiprocessing
import requests

path = '.'
df = pd.read_excel(path)

dates = df.Date
hometeams = df.HomeTeam
awayteams = df.AwayTeam

matches_odds = list()

def fetch(data):
    i, (a, b, c) = data
    try:
        r = requests.get(f'https://www.betexplorer.com/results/soccer/?year={a.split(" ")[3]}&month={monthToNum(a.split(" ")[2])}&day={a.split(" ")[1]}')
    except requests.exceptions.ConnectionError:
        sleep(10)
        r = requests.get(f'https://www.betexplorer.com/results/soccer/?year={a.split(" ")[3]}&month={monthToNum(a.split(" ")[2])}&day={a.split(" ")[1]}')
      
    soup = BeautifulSoup(r.text, 'html.parser')
    f = soup.find_all('td', class_="table-main__tt")

    for tag in f: 
        match = fuzz.ratio(f'{b} - {c}', tag.find('a').text)
        hour = a.split(" ")[4]
        if hour.split(':')[0] == '23':
            act_hour = '00' + ':' + hour.split(':')[1]
        else:
            act_hour = str(int(hour.split(':')[0]) + 1) + ':' + hour.split(':')[1]
        if match > 70 and act_hour == tag.find('span').text:
            href_id = tag.find('a')['href']

            table = get_odds(href_id)
            matches_odds.append(table)
          
    print(i, ' of ', len(dates))

if __name__ == '__main__':  
    num_processes = 20
    with multiprocessing.Pool(num_processes) as pool:
        pool.map(fetch, enumerate(zip(dates, hometeams, awayteams)))

    # https://stackoverflow.com/questions/70696332/how-to-speed-up-this-python-script-with-multiprocessing
    # PS: The monthToNum function just replace the month name to his number

