import re, sys, requests, time, concurrent.futures
url='https://mb-api.abuse.ch/api/v1'
array=[]
with open("hashes.txt") as f:
    for line in f:
        array.append({'query':'get_info','hash':line.rstrip("\n")})

def function(payload):
    with requests.post(url, data=payload,stream=True) as response:
        html = response.json()
        return(html)

start = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    processes = {executor.submit(function, query) for query in array}
    for result in concurrent.futures.as_completed(processes):
        print(result.result()['query_status'])

print(f"Time taken: {time.time() - start}")

