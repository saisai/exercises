"""
Read json sting from file and display pretty.
"""

import ast 
import json

text = open("test.txt", 'r', encoding="utf-8").read()
#print(type(text))
#print(json.loads(text, strict=False))

tt = json.loads(text, strict=False)
print(json.dumps(tt, indent=4, sort_keys=True))

#print(ast.literal_eval(t))
#print(ast.literal_eval(text))


# https://docs.python.org/3/library/ast.html

#https://pypi.org/project/ast2json/

# https://pythonhosted.org/pyrser/tutorial1.html

# https://codeblogmoney.com/json-pretty-print-using-python/

# https://www.geeksforgeeks.org/pretty-print-json-in-python/

# https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
