
class S:

    def find132pattern(self, nums):

        stack = [] # pair [num, minLeft], mono decreasing
        curMin = nums[0]

        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n > stack[-1][1]:
                return True

            stack.append([n, curMin])
            curMin = min(curMin, n)
        return False

nums = [1,2,3,4]
nums = [3,1,4,2]
print(S().find132pattern(nums))

