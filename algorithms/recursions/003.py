
class S:
    def test(self, nums):
        def recur(n):
            if n < 0:
                return
            for i in range(n - 1, -1, -1):
                print(n)
                recur(nums[i] - 1)
               
        recur(len(nums))
print(S().test([1,2,3]))

def test():
    nums = [1, 2, 3]
    for i in range(len(nums) - 1, -1, -1):
        print(nums[i])

#test()