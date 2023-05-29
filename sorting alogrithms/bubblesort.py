"""find smallest number for ith operation and arrange at first , keep this for entire row
on(n2)"""
array = [5,2,8,1,4,99,77]
def bubblesort(Array):
    #find smallest element of  n-1 the row and append to 1st row
    for i in range(len(Array)):
        for m in range(len(Array)-1, i,-1):
            if Array[m] < Array[m-1]:
                Array[m], Array[m-1] = Array[m-1], Array[m]
    return Array

print(bubblesort(array))