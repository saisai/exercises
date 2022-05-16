import pdb

def permutation(l, start, end):
    pdb.set_trace()
    def backtrack(l, start, end, res):
        if start == end:
            if l != ['b1', 'g', 'b2'] and l != ['b2', 'g', 'b1']:
                res.append(l)
        else:
            for i in range(start, end  + 1):
                l[start], l[i] = l[i], l[start]
                backtrack(l, start + 1, end, res)
                l[start], l[i]= l[i], l[start]

    res = []
    backtrack(l, start, end, res)
    print('res', res)
    return res

c = permutation(['b1', 'b2', 'g'], 0, 2)

for a in c:
    print(c)

