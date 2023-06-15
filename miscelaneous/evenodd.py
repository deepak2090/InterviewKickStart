#this is a polish national flag question
from traceback import print_tb


array = [5,6,1,8,33,9,10,55,12,47]

#what the logic states is set evenptr at start I.E. is -1 and if
#it finds a even number, increment the evenpointer and swap the element 
#between I pointer and evenptr

def InplaceEvenodd(array):
    evenptr = -1
    for i in range(0,len(array)):
        if array[i]%2 ==0:
            evenptr+=1
            array[i], array[evenptr] = array[evenptr], array[i]
    return array

print(InplaceEvenodd(array))

print('update')

array1 = [88,77,11,20,40, 5,6,1,8,33,9,10,55,12,47]
def inplaceoddeven(array):
    oddptr = -1
    for evenptr in range(len(array)):
        if array[evenptr] % 2 == 1:
            oddptr +=1
            array[evenptr], array[oddptr] = array[oddptr], array[evenptr]
    return array

print(inplaceoddeven(array1))
