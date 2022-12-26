from collections import deque

def ack_ix(m, n):
    "Paddy3118's iterative with optimisations on m"

    stack = deque([])
    print(stack)
    stack.extend([m, n])
    print(stack)

    while len(stack) > 1:
        n, m = stack.pop(), stack.pop()
        print('n ', n, 'm ', m)

        if m == 0:
            stack.append(n + 1)
        elif m == 1:
            stack.append(n + 2)
        elif m == 2:
            stack.append(2 * n + 3)
        elif m == 3:
            stack.append(2**(n+3) - 3)
        elif n == 0:
            stack.extend([m -1, 1])
        else:
            stack.extend([m - 1, m, n -1])
    return stack[0]

print(ack_ix(0, 0))
print(ack_ix(3, 4))
