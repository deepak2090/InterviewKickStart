
def square(n):
    x = [['' for i in range(n)] for i in range(n)]
    return x
square(5)

def queen(x):
    for row in range(len(x)):
        for col in range(len(x)):
            if isvalid(x[row][col]):
                x[row][col] == 'q'
    return x 



