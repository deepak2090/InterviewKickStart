def get_minimum_path_sum(triangle):

    # Write your code here.
    table = []
    if len(triangle) == 0:
        return None
    elif len(triangle) == 1:
        table.append(triangle[0])
        return min(table[-1])
    elif len(triangle) == 2:
        table.append(triangle[0][0])
        table.append([triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1]])
        return min(table[-1])
    else:
        table.append(triangle[0])
        table.append([triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1]])    
        for row in range(2, len(triangle)):
            rowvalues = [None] * (row + 1)
            rowvalues[0] = table[row-1][0] + triangle[row][0] 
            rowvalues[-1] = table[row-1][-1] + triangle[row][-1]
            for col in range(1, len(rowvalues)-1):
                rowvalues[col] = min(table[row-1][col-1] , table[row-1][col]) + triangle[row][col]
            table.append(rowvalues)
        return min(table[-1])

triangle =  [
[50],
[30, 30],
[-5, -5, -5],
[32, 32, 32, 32],
[-10, -10, -10, -10, -10]
]


"""triangle = [
[2]]
"""
"""

x = get_minimum_path_sum(triangle)
print(x)
import sys

print(sys.path)
"""