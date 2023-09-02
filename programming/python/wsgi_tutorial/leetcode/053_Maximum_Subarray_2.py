
def solutions(left, right):

    results = []

    left_idx =0
    right_idx = 0
    while left and left_idx < len(left) and right and right_idx < len(right):
        #print(left)
        if left and left[left_idx] not in results:
            results.append(left[left_idx])
            left_idx += 1

        if right and right[right_idx] not in results:
            results.append(right[right_idx])
            right_idx += 1


    if left:
        #print('l', left)
        #print('l', left[0])
        if left[0] not in results:
            results.append(left[0])

    if right and right[0] not in results:
        #print('r', right)
        #print('r', right[0])
        results.append(right[0])

    print(results)

    return results

    """
    print('len l', len(left))

    print('len r', len(right))
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        print(left[left_idx])

        left_idx += 1

        print(right[right_idx])
        right_idx += 1
    """


def solve(nums):

    if len(nums) <= 1:
        return nums

    middle = len(nums) // 2
    left = nums[:middle]
    right = nums[middle:]
    #print("left 1", left)
    #print("right 1", right)
    left = solve(left)
    right = solve(right)
    #print('left', left)
    #print('right', right)

    return solutions(left, right)

numss = [-2,1,-3,4,-1,2,1,-5,4]
solve(numss)


