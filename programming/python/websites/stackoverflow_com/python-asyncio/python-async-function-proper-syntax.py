import asyncio
import platform
import aiohttp

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

url = 'https://services.rappi.com.br/api/ms/web-proxy/dynamic-list/cpgs/'

req_headers = {'authority': 'services.rappi.com.br', 'accept': 'application/json',
               'authorization': 'Bearer ft.gAAAAABjMbGKkc2fkTMa2M2EKuBrCM1Z1vU5Ww1Fw03CjpJEb9UF1DO1TAjwpAD0H0NIImuMjWFcOkUURseLzJIi0DNSOr-oRWcZWgcnHLm2Ed6rDLvxQ2ikdGLtyVXZRqgGHWOMlBPVSKjYLb6NMZmAeHhAsGNjiQ3vP5VEdb_ULA9S5Lpo8H7-ElhKufmlVqQ6CrDyTUsyQeZ3IzbNCbN8MBLFhgRxVMZSwyl640YXF9ZvQUI1sibP-Ko86xrin_2EXEmAdEk7aSl9u0ezlmnBL6Wk8a7CwSJUEUAwAjrNdJTLSodjQaiVVx7TZ0rQEkzPgceaH7wtpmvl--6txmRDnBu4g0na3Km19K1LNzs0fz7-_Go8Qlg=',
               'deviceid': '957933bd-cdc4-4876-ad00-bc00a1d55c29',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

json_data = {"dynamic_list_request":
    {
        "limit": 100, "offset": 0, "context": "sub_aisles",
        "state": {"lat": "-23.5516221", "lng": "-46.7404627"}
    },
    "dynamic_list_endpoint": "context/content",
    "proxy_input":
        {
            "seo_friendly_url": "900597707-assai-atacadista-super-sao-paulo",
            "aisle_friendly_url": "",
        }
}

json_data2 = {"dynamic_list_request":
    {
        "limit": 100, "offset": 0, "context": "aisle_detail",
        "state": {"lat": "-23.5516221", "lng": "-46.7404627"}
    },
    "dynamic_list_endpoint": "context/content",
    "proxy_input":
        {
            "seo_friendly_url": "900597707-assai-atacadista-super-sao-paulo",
            "aisle_friendly_url": "bebidas",  
            'subaisle_friendly_url': "" 
        }
}
market_list = ['900597707-assai-atacadista-super-sao-paulo', '900520986-makro-atacadista-sao-paulo']
data = [{'sub_category': 'temperos-e-molhos', 'category': 'mercearia'},
        {'sub_category': 'massas', 'category': 'mercearia'}]


async def fetch_items(session, markets):
    local_items = []
    json_data2['proxy_input']['seo_friendly_url'] = markets
    print((json_data2['proxy_input']['subaisle_friendly_url'], json_data2['proxy_input']['aisle_friendly_url'],
            json_data2['proxy_input']['seo_friendly_url']))
    async with session.post(url, headers=req_headers, json=json_data2) as response:
        try:
            json_body = await response.json()
            json_body = json_body['dynamic_list_response']['data']['components']
        except KeyError:
            return
        for sections in json_body:
            local_items.extend(items for items in sections['resource']['products'])
    return local_items


async def fetch(url, session):
    list_items = []
    global data
    for cats in data:
        json_data2['proxy_input']['subaisle_friendly_url'] = cats['sub_category']
        json_data2['proxy_input']['aisle_friendly_url'] = cats['category']
        pending_tasks = [asyncio.create_task(fetch_items(session, markets)) for markets in market_list]
        for result in await asyncio.gather(*pending_tasks):
            list_items.extend(result)

    return list_items


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:  # there is no repetition here: no point in using .gather
        body = await fetch(url, session)
    return body


for data in asyncio.run(main()):
    print(data)
    
# https://stackoverflow.com/questions/73855591/python-async-function-proper-syntax
