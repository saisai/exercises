from urllib import response
import requests
import re
import time
import json 

data = [f.strip('\n') for f in open('idontknoooolinks.txt')]

#response = requests.get("https://leetcode.com/discuss/topic/2516837/python-3-math-explanation/")
#response = requests.get("https://leetcode.com/discuss/topic/11792/3-line-c-stdunique/")
#print(response.url)
#print("login/?next" in response.url)

#r = "https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/11792/3-line-c-stdunique"

#obj = re.search(r'/problems/(.*)/discuss/', r)
#print(obj.group(1))

def get_links(data):        
    links_list = []
    
    idx = 0
    for r in data:
        
        #if idx > 3: break
        response = requests.get(r)        
        if "login/?next" in response.url:
            links_list.append({"lock":(r,)})
            
        else:
            link = response.url
            result = re.search(r'/problems/(.*)/discuss/', link)
            links_list.append({result.group(1):(link, r)})
        idx += 1
        time.sleep(1)
    return links_list

with open('results.txt', '+a') as f:
    for d in get_links(data):
        f.write(json.dumps(d))
        f.write('\n')
        #print(d, file=json.dumps(d))
        
# https://stackoverflow.com/questions/67475333/typeerror-write-argument-must-be-str-not-dict-python
# https://stackoverflow.com/questions/3368969/find-string-between-two-substrings


