
def fib(n):
    
    sum = [0,1,0]
    for i in range(2,n):
        temp = sum[0] + sum[1]
        sum[2] = temp
        sum[0] = sum[1]
        sum[1]= temp
    return sum[2]
print(fib(99))
