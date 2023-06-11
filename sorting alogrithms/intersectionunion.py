

arr1 = [1,2,3,4,5,6,6,7,7,8,9,10,10]
arr2 = [3,4,5,6,7,8,9,10,10,11,11]

def intersection(array1,array2):
    i = 0
    j = 0
    result = []
    while i < len(array1) and j < len(array2):
        if array1[i] == array2[j]:
            result.append(array1[i])
            i+=1
            j+=1
        elif array1[i-1] == array1[i]:
            i+=1
        elif array1[i] < array2[j]:
            i +=1
        else:
            j+=1
        if i >1 and j >1:
            if array1[i-1] == array1[i]:
                i+=1
            if array2[j-1] == array2[j]:
                j+=1
    return result
print(intersection(arr1,arr2))

def union(array1, array2):
    i = 0
    j = 0
    result = []
    while i < len(array1) and j < len(array2):
        if array1[i] == array2[j]:
            result.append(array1[i])
            i+=1
            j+=1
        elif array1[i-1] == array1[i]:
            i+=1
        elif array1[i] < array2[j]:
            result.append(array1[i])
            i +=1
        else:
            result.append(array2[j])
            j+=1
        if i >1 and j >1:
            if array1[i-1] == array1[i]:
                i+=1
            if array2[j-1] == array2[j]:
                j+=1
    while j < len(array2):
        if j > 1 and array2[j-1] != array2[j]:
            result.append(array2[j])
        j+=1
    return result
print(union(arr1,arr2))
