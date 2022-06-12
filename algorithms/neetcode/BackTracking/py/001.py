
ll = []
def permutation(l, start, end):
    global ll    
    if start == end:
        #print('l ', l)
        if l not in [['b1', 'g', 'b2'], ['b2', 'g', 'b1']]:
            #print('ll ', l)
            yield l
            #ll.append(l)
    else:
        for i in range(start, end  + 1):
            l[start], l[i] = l[i], l[start]
            permutation(l, start + 1, end)
            l[start], l[i]= l[i], l[start]

for a in permutation(['b1', 'b2', 'g'], 0, 2):
    print(a)
