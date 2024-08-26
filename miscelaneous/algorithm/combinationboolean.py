
memo = {}
def combinationsum(values, target):
    if target ==0:
        return []
    if target <0:
        return None

    for val in values:
        remainder = target - val
        
        if result is not None:
            result = combinationsum(values, remainder)
            return result + [val]
 
#print(combinationsum([7,14],300))
print(combinationsum([2,3,5],8))
print(combinationsum([2,3,44],7))
