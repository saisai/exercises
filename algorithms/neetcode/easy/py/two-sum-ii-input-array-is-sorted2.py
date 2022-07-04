
class S:

    def __call__(self, numbers, target):

        beg, end = 0, len(numbers) - 1
        while beg <= end:
            if numbers[beg] + numbers[end] == target: return [beg + 1, end + 1]
            elif numbers[beg] + numbers[end] < target: beg += 1
            else: end -= 1

numbers = [2,7,11,15]
target = 9

print(S()(numbers, target))

