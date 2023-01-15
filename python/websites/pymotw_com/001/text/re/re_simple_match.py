import re

pattern = 'this'
text = 'Does this next match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print(dir(match))
print(dir(match.re))
print(dir(match.regs))
print(dir(match.span))
print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
    match.re.pattern, match.string, s, e, text[s:e]
))