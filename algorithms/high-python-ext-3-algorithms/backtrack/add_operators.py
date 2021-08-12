
"""
Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary) +, -, or *
between the digits so they prevuate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""

def add_operators(num, target):
    """
    :type num: str
    :type target: int
    :rtype: List[str]
    """

    def dfs(res, path, num, target, pos, prev, multed):
        #print('pos ', pos, 'len(num) ', len(num))
        if pos == len(num):            
            if target == prev:
                print('target ', target, 'prev ', prev)
                print('path ', path)
                res.append(path)
            return
        for i in range(pos, len(num)):
            print(' i ', i)
            if i != pos and num[pos] == '0': # all digits have to be used
                print('break ')
                break
            cur = int(num[pos:i+1])
            print('cur ', cur, ' pos ', pos)
            if pos == 0:
                print(' pos 0 here ' )
                dfs(res, path + str(cur), num, target, i + 1, cur ,cur)
            else:
                print(' pos not 0 ', pos)
                dfs(res, path + "+" + str(cur), num, target, i+1, prev + cur, cur)
                #dfs(res, path + "-" + str(cur), num, target, i+1, prev - cur, -cur)
                #dfs(res, path + "*" + str(cur), num, target, i+ 1, prev - multed + multed * cur, multed * cur)

    res = []
    if not num:
        return res
    dfs(res, "", num, target, 0, 0, 0)
    return res
    
    
r1 = add_operators("123", 6)
print(r1)
