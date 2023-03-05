array = [5,3,2,8,1,0,77,45]

def mergehelper(array, start, end):
    if start >=end:
        return
    mid = (start + end)//2
    mergehelper(array, start, mid)
    mergehelper(array, mid+1, end)
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

