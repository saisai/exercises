import json 
from pathlib import Path
import sys
data = [f.strip('\n') for f in open('results.txt')]

def listdirs(rootdir):
    dir_list = []
    for path in Path(rootdir).iterdir():
        if path.is_dir():
            #if str(path) != "__pycache__" or not str(path).find("\n") != -1:
            #print(str(path))
            if str(path) != "__pycache__" and str(path).find("\\n") == -1:
                #print(path)
                dir_list.append(str(path))
            listdirs(path)
    return dir_list
            
dir_results = listdirs('.')

results = []
for d in data:
    #print(d)
    #print(type(d))
    r = json.loads(d)
    
    #print(r)
    #print(key, val)
    key = list(r.keys())[0]
    #print(key)
    if "lock" not in key:
        if key not in dir_results:
            #print("no ", key, r.get(key)[0])
            results.append([key, r.get(key)[0]])
idx = 0
for j in results:
    if idx > 3: break
    print(j)

    idx += 1
