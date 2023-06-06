from py.xml import html

def intersection(array1,array2,array3):
    dict = {}
    for i in range(len(array1)):
        if array1[i] in dict:
            dict[array1[i]] +=1
        else:
            dict[array1[i]]=1
    
    for i in range(len(array2)):
        if array2[i] in dict:
            dict[array2[i]] +=1
        else:
            dict[array2[i]]=1
    for i in range(len(array3)):
        if array3[i] in dict:
            dict[array3[i]] +=1
        else:
            dict[array3[i]]=1
    result = []
    for key in dict.keys():
        if dict[key] ==3:
            result.append(key)
    return result
        
    
arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

res = intersection(arr1,arr2,arr3)
print(res)