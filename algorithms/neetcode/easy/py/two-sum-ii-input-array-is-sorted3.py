
class S:

    def __call__(self, numbers, target):

        seen = {}
        for i in range(len(numbers)):
            required = target - numbers[i]
            if required in seen:
                return [seen[required], i + 1,]
            else:
                seen[numbers[i]] = i + 1


numbers = [2,7,11,15]
target = 9

print(S()(numbers, target))

