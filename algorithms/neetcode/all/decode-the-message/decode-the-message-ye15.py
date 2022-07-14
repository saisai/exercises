'''
https://leetcode.com/problems/decode-the-message/discuss/2239164/python3-2-line
https://leetcode.com/problems/decode-the-message/

'''
from collections import OrderedDict
from string import *

class S:
    def decodeMessage(self, key: str, message: str) -> str:

        mp = dict(zip(OrderedDict.fromkeys(key.replace(' ', '')).keys(), ascii_lowercase), **{' ': ' '})
        return ''.join(map(mp.get, message))


key = "eljuxhpwnyrdgtqkviszcfmabo"
message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
print(S().decodeMessage(key, message))
