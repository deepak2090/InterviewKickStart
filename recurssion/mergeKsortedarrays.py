arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9],[11,88,99], [1,2,3,100, 101]]

def mergeksortedarrays(arrays):
    if len(arrays) == 1:
        return arrays[0]
    mid = len(arrays)//2
    left = mergeksortedarrays(arrays[:mid]) 
    right = mergeksortedarrays(arrays[mid:])
    merged = merge(left , right)
    return merged

def merge(arr1, arr2):
    merged = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
    while i < len(arr1):
        merged.append(arr1[i])
        i+=1
    while j < len(arr2):
        merged.append(arr2[j])
        j+=1
    return merged