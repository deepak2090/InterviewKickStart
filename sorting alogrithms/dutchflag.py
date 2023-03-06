array = ['R', 'G', 'R', 'R', 'G', 'B', 'G', 'B', 'R', 'R', 'R', 'G']

#RGB

def dutchflag(array):
    firstptr = -1
    i = 0
    while i <= len(array)-1:
        if array[i] == 'R':
            firstptr +=1
            array[i], array[firstptr] = array[firstptr], array[i]
        i +=1

    mid = firstptr
    i = mid + 1
    while i <= len(array)-1:
        if array[i] == 'G':
            mid +=1
            array[mid], array[i] = array[i], array[mid]
        i +=1
    return array

print(dutchflag(array))
