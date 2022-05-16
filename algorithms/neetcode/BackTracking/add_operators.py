import pdb

def add_operators(num, target):

    def dfs(res, path, num, target, pos, prev, multed):
        pdb.set_trace()
        if pos == len(num):
            if target == prev:
                res.append(path)
            return
        for i in range(pos, len(num)):
            if i != pos and num[pos] == '0': # all digits have to be used
                break
            cur = int(num[pos:i+1])
            if pos == 0:
                dfs(res, path + str(cur), num, target, i+1, cur, cur)
            else:
                dfs(res, path + "+" + str(cur), num, target, i+1, prev + cur, cur)
                dfs(res, path + "-" + str(cur), num, target, i+1, prev - cur, -cur)
                dfs(res, path + "*" + str(cur), num, target, i+1, prev-multed + multed * cur, multed * cur)

    res = []
    if not num:
        return res
    dfs(res, "", num, target, 0, 0, 0)
    return res

print(add_operators("123", 6))
#print(add_operators("232", 8))

# https://github.com/keon/algorithms/blob/master/algorithms/backtrack/add_operators.py

