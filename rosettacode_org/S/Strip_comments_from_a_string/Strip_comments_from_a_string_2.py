
import re

line = '''apples, pears # and bananas
               apples, pears ; and bananas
            '''

m = re.match(r'^([^#]*)#(.*)$', line)
if m:
    line = m.group(1)
    print(line)


