result = []
def triplets(nums):
    nums.sort()

    if len(nums) >=3:
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:            
                total = nums[left] + nums[right] + nums[i]
                if total == 0:
                    result.append([nums[left], nums[right], nums[i]])
                    break
                elif total <0:
                    left +=1
                elif total > 0:
                    right -=1
    return result
nums = [-1,0,1,2,-1,-4]

triplets(nums)