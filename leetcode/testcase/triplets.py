from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1= min2 = float('inf')
        for idx,num in enumerate(nums):
            if min1 < min2 <num:
                print(min1,min2,num)
                return True
            if num < min1:
                min1 = num
            elif min1 < num < min2: #this ensures min2 never exceeds num and keeps min1 as first min
                min2 = num
        
        return False


obj = Solution()
nums = [5,4,3,2,22,8,11,7,12,0]
print(obj.increasingTriplet(nums))