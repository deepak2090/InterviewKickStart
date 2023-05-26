def pascals(n):
    #define a blank array which will contain further empty lists
    table = []
    table.append([1]) #append first 2 rows
    table.append([1,1])
    for row in range(2,n):
        value = [None] * row
        table.append(value)
        table[row][0] = 1
        table[row][-1] = 1
        for col in range(1,row-1):
            table[row][col] = table[row-1][col-1] + table[row-1][col]
    return table


"""[[1],
 [1, 1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1],
 [1, 5, 10, 10, 5, 1],
 [1, 6, 15, 20, 15, 6, 1]]
 """

x =  pascals(8)
print(x)

def Twodarray(n):
    #remember this is very critical
    table = [[0] * n for i in range(n)]
    for i in range(n):
        table[0][i] = 1
        table[i][0] = 1

    for row in range(1,n):
        for col in range(1,n):
            table[row][col] = table[row-1][col-1] + table[row-1][col]
    return table

y = Twodarray(6)
print(y)
"""
[[1, 1, 1, 1, 1, 1],
 [1, 2, 2, 2, 2, 2],
 [1, 3, 4, 4, 4, 4],
 [1, 4, 7, 8, 8, 8],
 [1, 5, 11, 15, 16, 16],
 [1, 6, 16, 26, 31, 32]]
 """



def find_pascal_triangle(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    #define a 2d empty triangle
    table = []
    if n == 0:
        return None
    elif n ==1:
        table.append([1])
        return table
    else:
        table.append([1])
        table.append([1,1])
        for i in range(2, n):
            row = [None] * (i+1)
            #table.append(value)
            #[0] = 1
            #table[i][-1] = 1
            row[0] = 1
            row[-1] = 1
            for col in range(1,i):
                row[col] = table[i-1][col-1] + table[i-1][col]
            table.append(row)
    return table


x = find_pascal_triangle(9)
print(x)