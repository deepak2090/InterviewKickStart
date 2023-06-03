"""
The basic idea of insertion sort is as follows:

Start with the second element (index 1) and consider it as the key.
Compare the key with the elements to its left in the sorted portion of the array.
If the key is smaller, shift the elements to the right to make space for the key,
and insert the key into its correct position.
Repeat steps 2 and 3 for the remaining unsorted elements of the array.
Continue this process until the entire array is sorted.
"""
array = [5,2,8,1,4,99,77,11,554,333,222,0,-12]
x = [5,2,8,1,4,99,77,11,554,333,222,0,-12]
def insertionsort(array):
    for i in range(1,len(array)):
        temp = array[i]
        red = i-1
        while red >=0 and array[red] > temp: #while is preferred as arrays are already sorted
            array[red+1] = array[red] #i am right shifting rather than swapping to save extra operations of O(3)
            red -=1 #then checking the next left red pointer to get the exact place to be shifted once done assing temp to array[red]
        array[red+1] = temp
    return array
x.sort()
print(insertionsort(array)==x)


