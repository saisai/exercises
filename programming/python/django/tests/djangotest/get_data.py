import json 
import requests


from bs4 import BeautifulSoup as bs 

request = requests.get('https://github.com/django/django/tree/stable/5.0.x/tests')

print(request)
print(type(request.text))

url = "https://github.com/django/django/tree/stable/5.0.x/tests/%s"
result = json.loads(request.text)

for key, data in result['payload'].items():

    if key == "tree":
        for kk, val in data.items():

            if kk == "items":
                for obj in val:
                    if obj['contentType'] != "file":
                        print(url % (obj['name']))
                
