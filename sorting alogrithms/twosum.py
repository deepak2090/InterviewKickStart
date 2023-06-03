

array = [4,2,5,7,1,9]

def twosum(array):
    resultlist = []
    for i in range(len(array)):
        for k in range(i+1,len(array)):
            resultlist.append([array[i],array[k]])
    return resultlist



def twosumsort(array, target):
    array.sort()
    resultlist = []
    left = 0
    right = len(array) -1
    while left <  right:
        currentsum = array[left] + array[right]
        if target == currentsum:
            resultlist.append([array[left], array[right]])
            left +=1
        elif target < currentsum:
            right -=1
        else:
            left +=1
    return resultlist



def twosumhashmap(array, target):
    dict = {}
    result = []
    for i in range(len(array)):
        if target- array[i] in dict:
            result.append([array[i], target - array[i]])
        else:
            dict[array[i]] = 1
    return result

res =twosumhashmap(array,6)
print(res)
