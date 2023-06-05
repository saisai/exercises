import copy
from typing import List

class S:
    def duplicateZeros(self, arr: List[int]) -> None:
        
        count_dup_zeros = 0
        arr_len = len(arr) - 1
        for left in range(arr_len + 1):
            if left > arr_len - count_dup_zeros:
                break
            
            if arr[left] == 0:
                if arr_len - count_dup_zeros == left:
                    arr[arr_len] = 0
                    arr_len -= 1
                    break
                count_dup_zeros += 1
        print("arr_len", arr_len)
        print("count_dup_zeros", count_dup_zeros)
        
        last = arr_len-count_dup_zeros
        print("last", last)
        
        for pos in range(last, -1,-1):
            if arr[pos]==0:
                arr[pos+count_dup_zeros] = 0
                count_dup_zeros-=1
                arr[pos+count_dup_zeros] = 0
            else:
                arr[pos+count_dup_zeros] = arr[pos]
        print(id(arr))

arrs = [1,0,2,3,0,4,5,0]   
S().duplicateZeros(arrs)
print(arrs)
print(id(arrs))