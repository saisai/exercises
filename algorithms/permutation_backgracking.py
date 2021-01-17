
def swap(arr, i, j, tt):
    
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    print(tt, arr)


def printArr(arr, n):
    for i in range(n):
        print(arr[i], end='')
    print()

def print_helper(arr, n, i):
    print('i ', i)

    if i == n:
        printArr(arr, n)

    #for x in range(n):

    x = i
    while x < n:
        print('x ', x)
        swap(arr, x, i, 'a')

        print_helper(arr, n, i+1)

        print("backtracking ", x, "->", i)
        swap(arr, x, i, 'b') #backtrakcing

        x += 1


def print_permutation(arr, n):
    print_helper(arr, n, 0)

print_permutation(['A', 'B', 'C'], 3)

# https://www.youtube.com/watch?v=eUnNw2lR01M&ab_channel=SandeepKumar
