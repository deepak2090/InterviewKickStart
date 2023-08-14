array = [1,2,3]


def get_permutations(arr):
    #keeping kth element as index swap kth element with all remaining elements
    #except previous elements of k
    result = []
    def helper(arr, k):
        if len(arr) == k:
            result.append(list(arr))
        for i in range(k,len(arr)):
            arr[i], arr[k] = arr[k], arr[i]
            helper(arr, k+1)
            arr[i], arr[k] = arr[k], arr[i]
    helper(arr,0)
    return result

output = get_permutations(array)
print(output)
def permutations(arr):
    return

totalresult = []
slate = ""
def perm_slate(arr, i ,slate):
    if i == len(arr):
        totalresult.append(slate)
    else:
        for i in range(i, len(arr)):
            pass