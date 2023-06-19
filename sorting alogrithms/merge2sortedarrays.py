first = [1, 3, 5]
second = [2, 4, 6, 0, 0, 0]


#inplace merged algorithm
def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    i = len(first)-1
    j = len(first) -1 
    k = len(second) - 1
    while i >=0 and j >=0:
        if first[i] >= second[j]:
            second[k] = first[i]
            k -=1
            i -=1
        else:
            second[k] = second[j]
            k -=1
            j -=1
    while i >=0:
        second[k] = first[i]
        k -=1
        i -=1
    #while for j is not needed as it would be a reduntant code
    return second


print(merge_one_into_another(first, second))

def merge2arrays(arr1, arr2):
    merged = []
    i = 0
    j = 0
    while i < len(arr1) and j <len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i +=1
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

result = merge2arrays(array1,array2)
print(result)