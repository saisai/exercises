
import re

def test_space(param):
    if param.strip():
        print("no space")
        print(param)
    else:
        print("space")
        print(param)


t = ' ' + ' '        
test_space(t)

t = ' ' + 'ttt'        
test_space(t)      



def check_duplicate():
    
    test = {}
    seen = set()
    emp = ['a', 'b', 'c', 'd', 'a']
    for a in emp:
        print(a)
        if a not in seen:
            seen.add(a)
            
    print(seen)

check_duplicate()        
