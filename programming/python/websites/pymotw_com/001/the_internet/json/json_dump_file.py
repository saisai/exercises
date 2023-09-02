import io
import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0, 'd': True}]

f = io.StringIO()
json.dump(data, f)

print(f.getvalue())