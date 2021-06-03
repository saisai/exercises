import urllib.request

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

mx, url = 0,  'https://raw.githubusercontent.com/quinnj/Rosetta-Julia/master/unixdict.txt'

for word in urllib.request.urlopen(url).read().decode('utf-8').split():
    lenword = len(word)
    if lenword >= mx and word == ''.join(sorted(word)):
        if lenword > mx:
            words, mx = [], lenword
        words.append(word)
print(' '.join(words))