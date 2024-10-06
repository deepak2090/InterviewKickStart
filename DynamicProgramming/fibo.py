
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <=1:
        return 1
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
print(fib(8))

def permutation(nums, length, slate):
    result = []
    def helper(nums, length, slate):
        if len(slate[:]) == length:
            result.append(slate[:])
            return
        for idx in range(len(nums)):
            slate.append(nums[idx])
            helper(nums[:idx] + nums[idx+1:], length, slate)
            slate.pop()
            
    helper(nums, length, [])
    return result

def combinations(nums, length, slate):
    result = []
    def helper(nums, length, slate):
        if len(slate[:]) == length:
            result.append(slate[:])
            return
        for idx in range(len(nums)):
            slate.append(nums[idx])
            helper(nums[idx+1:], length, slate)
            slate.pop()
            
    helper(nums, length, [])
    return result


def bracket(nums, length, slate):
    result = []
    def helper(nums, length, slate):
        if len(slate[:]) == length:
            char = ""
            for val in slate[:]:
                char+= val
            result.append(char)
            return
        for idx in range(len(nums)):
            slate.append(nums[idx])
            helper(nums[:idx] + nums[idx+1:], length, slate)
            slate.pop()
            
    helper(nums, length, [])
    return result

x = permutation(["(",")", "{", "}"], 2, [])
x.sort()
print(x, len(x))
y = combinations([1,2,3,4,5], 2, [])
y.sort()
print(y, len(y))
z = bracket(["(",")", "{", "}"], 2, [])
print(z, len(z))