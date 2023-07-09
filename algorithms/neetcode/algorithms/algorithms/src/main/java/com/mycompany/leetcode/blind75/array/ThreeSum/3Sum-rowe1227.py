from typing import List

class S:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
        
        N, P = set(n), set(p)
        
        if z:
            for num in P:
                if -1* num in N:
                    res.add((-1*num, 0, num))
        
        if len(z) >= 3:
            res.add((0,0,0))
            
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -1 * (n[i] +n[j])
                if target in P:                    
                    res.add(tuple(sorted([n[i], n[j], target]) ))
                    
        
        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
	    #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))
                    
        return res 

nums = [-1,0,1,2,-1,-4]
print(S().threeSum(nums))