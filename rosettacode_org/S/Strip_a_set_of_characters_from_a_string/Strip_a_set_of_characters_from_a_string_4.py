

import re

def stripchars(s, chars):
    return re.sub('[%s]+' % re.escape(chars), '', s)

print(stripchars("She was a soul stripper. She took my heart!", "aei"))
