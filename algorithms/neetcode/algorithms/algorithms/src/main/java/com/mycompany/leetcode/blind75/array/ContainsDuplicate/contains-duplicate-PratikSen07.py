
class S:
    def containsDuplicate(self, nums):
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)
             
nums = [1,2,3,1]   
print(S().containsDuplicate(nums))