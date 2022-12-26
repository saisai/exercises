import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://raw.githubusercontent.com/quinnj/Rosetta-Julia/master/unixdict.txt'
words = urllib.request.urlopen(url).read().decode('utf-8').split()
ordered = [word for word in words if word == ''.join(sorted(word))]
maxlen = len(max(ordered, key=len))
maxorderedwords = [word for word in ordered if len(word) == maxlen]
print(' '.join(maxorderedwords))