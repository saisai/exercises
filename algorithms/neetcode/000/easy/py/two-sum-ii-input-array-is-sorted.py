
class S:

    def __call__(self, numbers, target):

        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum < target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []

numbers = [2,7,11,15]
target = 9
print(S()(numbers, target))
