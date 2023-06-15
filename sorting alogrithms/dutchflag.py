import random

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

array = [44,33,55,55,33,44,44,33]

def dutchproblemint(array):
    pivotidx = random.randint(0,len(array)-1)
    #array[0] , array[pivotidx] = array[pivotidx], array[0]
    lessptr = -1
    greaterptr = len(array)
    print("pivot is", array[pivotidx], pivotidx)
    for i in range(1,len(array)):
        if array[i] < array[pivotidx]:
            lessptr +=1
            array[i], array[lessptr] = array[lessptr], array[i]
        if array[i] > array[pivotidx]:
            greaterptr -=1
            array[i], array[greaterptr] = array[greaterptr], array[i]
        if array[i] == array[pivotidx]:
            if pivotidx >= lessptr and pivotidx > 0:
                pivotidx -=1
            else:
                if pivotidx < len(array):
                    pivotidx +=1
            array[i], array[pivotidx] = array[pivotidx], array[i]
    return array
print(dutchproblemint(array))




            
