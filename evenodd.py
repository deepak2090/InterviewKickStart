#this is a polish national flag question
from traceback import print_tb


array = [5,6,1,8,33,9,10,55,12,47]


def InplaceEvenodd(array):
    evenptr = -1
    for i in range(0,len(array)):
        if array[i]%2 ==0:
            evenptr+=1
            array[i], array[evenptr] = array[evenptr], array[i]
    return array

print(InplaceEvenodd(array))

