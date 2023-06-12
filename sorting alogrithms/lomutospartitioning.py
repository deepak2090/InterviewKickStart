

array = [4,2,8,7,1,3,5,6,-2,0,1]


def lomutopartioning(array, pivot):
    orangeptr = 0
    greenptr = 0
    for i in range(len(array)):
        if array[i] ==  pivot:
            array[0], array[i] = array[i] , array[0]
    for i in range(1,len(array)):
        if array[i] > pivot:
            greenptr +=1
        else:
            greenptr +=1
            orangeptr +=1     
            array[greenptr], array[orangeptr] = array[orangeptr], array[greenptr]
    array[0], array[orangeptr] = array[orangeptr], array[0]
    return array
print(lomutopartioning(array, -2))
