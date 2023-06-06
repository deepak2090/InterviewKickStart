array = [5,3,2,8,1,0,77,45,-22,-33]

def mergehelper(array, start, end):
    #if it is a leaf node then return
    if start ==end:
        return
    mid = (start + end)//2
    #if it is a bigger problem not a leaf keep dividing the array as below
    mergehelper(array, start, mid)
    mergehelper(array, mid+1, end)
    #assume the same middle node has been sorted now you have to merge it.
    i = start
    j = mid+1
    aux = []
    while (i<=mid) and (j<=end):
        if array[i]<= array[j]:
            aux.append(array[i])
            i+=1
        elif array[j]<array[i]:
            aux.append(array[j])
            j+=1
    while i <=mid:
        aux.append(array[i])
        i+=1
    while j <=end:
        aux.append(array[j])
        j+=1
    array[start:end +1] = aux

def mergesort(array):
    mergehelper(array, 0, len(array)-1)
    return array

print(mergesort(array))

