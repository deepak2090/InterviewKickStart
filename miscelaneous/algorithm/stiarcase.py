def staircase(m,n):
    if (m ==0 and n==0):
        return 0
    elif (m==0 or n==0):
        return 1
    elif (m==1 and n==1):
        return 1
    return staircase(m-1,n) +staircase(m,n-1)

print(staircase(3,3))
    