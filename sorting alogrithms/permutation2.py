def permuteUnique(nums):
    result = []
    
    def helper(nums,i,slate):
        if i == len(nums):
            #print(i, len(nums))
            result.append(slate[:])
        else:
            
            for idx in range(i, len(nums)):
                hmap = {}
                if nums[idx] not in hmap:
                    hmap[nums[idx]]=1
                    nums[i], nums[idx] = nums[idx], nums[i]
                    slate.append(nums[i])
                    helper(nums,i+1,slate)
                    #print(i, len(nums))
                    nums[i], nums[idx] = nums[idx], nums[i]
                    slate.pop()
    helper(nums,0,[])
    return result
x = []
x = permuteUnique([1,1,1])
print(x)