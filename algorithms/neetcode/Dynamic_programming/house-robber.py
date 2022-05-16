
class S:

    def __call__(self, nums):

        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

nums = [1,2,3,1]
print(S()(nums))
