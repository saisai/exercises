import io
import json

f = io.StringIO('[{"a": "A", "c": 3.0, "b": [2, 4]}]')
print(type(json.load(f)))
#print(json.load(f))

d = open('test.txt').read()
print(type(d))
print(d)
print(json.load(io.StringIO(d)))