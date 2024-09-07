
def howsum(target, inputarray):
    if target == 0:
        return []
    if target <0:
        return None
    for idx in range(len(inputarray)):
        remainder = target - inputarray[idx]
        result = howsum(remainder, inputarray)
        if result is not None:
            result.append(inputarray[idx])
            return result
    return None
print(howsum(25,[7,14]))

def dicthowsum(target, inputarray, memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target <0:
        return None
    for idx in range(len(inputarray)):
        remainder = target - inputarray[idx]
        #result = dicthowsum(remainder, inputarray)
        memo[remainder] = dicthowsum(remainder, inputarray, memo)
        if memo[remainder] is not None:
            memo[remainder].append(inputarray[idx])
            return memo[remainder]
    memo[target] = None
    return None


print(dicthowsum(15,[3,5]))
print(dicthowsum(5,[1,3,0]))
print(dicthowsum(22,[2,4,6,8,10,12]))
print(dicthowsum(300,[7,14]))
print(dicthowsum(15,[3,5]))