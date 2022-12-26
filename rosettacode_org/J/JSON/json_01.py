import json

data = json.loads('{ "foo": 1, "bar": [10, "apples"]}')
print(data)

sample = {"blue": [1, 2], "ocean": "water"}
json_string = json.dumps(sample)
print(json_string)

