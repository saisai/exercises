

def permute(value, i, length):
    print('value ', value, 'i ', i, 'length ', length)
    if i == length:
        print(''.join(value))
        #return
    else:
        for j in range(i, length):
            value[i], value[j] = value[j], value[i]
            permute(value, i + 1, length)
            value[i], value[j] = value[j], value[i]

val = "abc"
print(len(val))
#val = ['a', 'b', 'c']
print(len(val))
permute(list(val), 0, len(val))


'''
def permute(data, i, length):
    if i == length:
        print(''.join(data))
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]


string = "ABC"
n = len(string)
data = list(string)
permute(data, 0, n)
'''