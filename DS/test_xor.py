def maximumStrongPairXor(nums):
    nums.sort()
    n = len(nums)
    l = 0
    r = 0
    res = 0

    while r < n:
        print(l,r)
        x = nums[l]
        y = nums[r]
        if y - x > x:
            l += 1
            continue
        for i in range(l, r):
            res = max(res, nums[i] ^ y)
        r += 1
    return res
nums = [-1,6,25,30]
maximumStrongPairXor(nums)


x = [1, 0, 0, 0, 1, 1, 0, 0, 1, 2, 1, 2, 1, 0, 2]
zeroptr = 0
twoptr = len(x)-1
currptr = 0
while currptr <= twoptr:
    if x[currptr] ==0:
        x[currptr], x[zeroptr] = x[zeroptr], x[currptr]
        zeroptr+=1
        currptr+=1
    elif x[currptr] ==2:
        x[currptr], x[twoptr] = x[twoptr], x[currptr]
        twoptr-=1
    else:
        currptr+=1
print(x)

nums = [1,2,3,]
def subset(nums):
    
    result = []
    def subsethelper(nums,i,slate):
        if i == len(nums):
            result.append(slate[:])
        else:
            for idx in range(i,len(nums)):
                nums[idx], nums[0] = nums[0], nums[idx]
                slate.append(nums[0])
                subsethelper(nums, i+1, slate)
                nums[idx], nums[0] = nums[0], nums[idx]
                slate.pop()

    subsethelper(nums, 0, [])
    return result
result = subset(nums)
print("result is",result)